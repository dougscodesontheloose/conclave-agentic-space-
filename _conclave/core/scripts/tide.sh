#!/usr/bin/env bash
# tide.sh — POSEIDON aggregation script
# Reads all JSONL streams in the Conclave memory layer and emits a JSON summary
# to stdout. Pure bash + jq-free (uses awk/grep) so it runs anywhere.
#
# Invoked by: poseidon.agent.md (/conclave tide)
# Output: single-line JSON to stdout
# Exit codes: 0 = success (even if no streams found)

set -euo pipefail

CWD="${CWD:-$(pwd)}"
HOME_DIR="${HOME}"

mem_dir="${CWD}/_conclave/state/memory"
log_dir="${CWD}/_conclave/runtime/logs"
squads_dir="${CWD}/squads"

# Stream candidates (project-local)
skill_signals="${mem_dir}/skill-signals.jsonl"
skill_candidates="${mem_dir}/skill-candidates.jsonl"
session_log="${mem_dir}/session-log.jsonl"
audit_log="${log_dir}/audit.jsonl"
gossip="${mem_dir}/gossip.jsonl"
user_model="${mem_dir}/user-model.md"
company_md="${mem_dir}/company.md"

# Helpers
count_lines() { [ -f "$1" ] && wc -l < "$1" | tr -d ' ' || echo 0; }
last_entry_date() {
  if [ -f "$1" ] && [ -s "$1" ]; then
    tail -1 "$1" | grep -oE '"ts":"[^"]*"' | head -1 | sed 's/"ts":"//;s/"$//'
  else
    echo ""
  fi
}
file_age_days() {
  if [ -f "$1" ]; then
    if [[ "$OSTYPE" == "darwin"* ]]; then
      mtime=$(stat -f %m "$1")
    else
      mtime=$(stat -c %Y "$1")
    fi
    now=$(date +%s)
    echo $(( (now - mtime) / 86400 ))
  else
    echo -1
  fi
}

# --- Maintenance Hooks ---
scripts_dir="${CWD}/_conclave/tools/scripts"
if [ -f "${scripts_dir}/promote_signals.py" ]; then
  python3 "${scripts_dir}/promote_signals.py" 2>/dev/null || true
fi
if [ -f "${scripts_dir}/archive_logs.py" ]; then
  python3 "${scripts_dir}/archive_logs.py" 2>/dev/null || true
fi

# --- Skill signal aggregation ---
declare_skill_quality_summary() {
  [ -f "$skill_signals" ] || { echo "[]"; return; }
  # group by skill, count last-5 quality buckets
  awk -F'"skill":"' '/"skill":"/ {
    split($2, a, "\""); skill=a[1];
    quality="";
    if (match($0, /"quality":"[^"]*"/)) {
      q = substr($0, RSTART+11, RLENGTH-12); quality=q;
    }
    if (skill && quality) print skill "\t" quality;
  }' "$skill_signals" | tail -100 > /tmp/tide_skill_signals.tmp 2>/dev/null || true

  if [ ! -s /tmp/tide_skill_signals.tmp ]; then echo "[]"; return; fi

  # For each skill, take last 5 signals and count miss/partial/good
  skills=$(awk '{print $1}' /tmp/tide_skill_signals.tmp | sort -u)
  out="["
  first=1
  for s in $skills; do
    last5=$(grep -P "^${s}\t" /tmp/tide_skill_signals.tmp 2>/dev/null | tail -5)
    miss=$(echo "$last5" | grep -c 'miss' || true)
    partial=$(echo "$last5" | grep -c 'partial' || true)
    good=$(echo "$last5" | grep -c 'good' || true)
    total=$(echo "$last5" | wc -l | tr -d ' ')
    if [ $first -eq 0 ]; then out="${out},"; fi
    out="${out}{\"skill\":\"${s}\",\"last_n\":${total},\"miss\":${miss},\"partial\":${partial},\"good\":${good}}"
    first=0
  done
  out="${out}]"
  echo "$out"
  rm -f /tmp/tide_skill_signals.tmp
}

# --- Squad signal aggregation ---
declare_squad_quality_summary() {
  out="["
  first=1
  if [ -d "$squads_dir" ]; then
    for sd in "$squads_dir"/*/; do
      [ -d "$sd" ] || continue
      name=$(basename "$sd")
      sig="${sd}_memory/squad-signals.jsonl"
      [ -f "$sig" ] || continue
      total=$(wc -l < "$sig" | tr -d ' ')
      good=$(grep -c '"quality":"good"' "$sig" 2>/dev/null || echo 0)
      partial=$(grep -c '"quality":"partial"' "$sig" 2>/dev/null || echo 0)
      miss=$(grep -c '"quality":"miss"' "$sig" 2>/dev/null || echo 0)
      # last 5 vs prior 5 trend (very rough)
      last5_good=$(tail -5 "$sig" | grep -c '"quality":"good"' || echo 0)
      prior5_good=$(head -n -5 "$sig" 2>/dev/null | tail -5 | grep -c '"quality":"good"' || echo 0)
      trend="stable"
      if [ "$last5_good" -lt "$prior5_good" ] && [ "$total" -ge 6 ]; then trend="declining"; fi
      if [ "$last5_good" -gt "$prior5_good" ] && [ "$total" -ge 6 ]; then trend="rising"; fi
      # native-only check
      native_only=false
      if [ -f "${sd}squad.yaml" ]; then
        non_native=$(grep -E "^\s*-\s+" "${sd}squad.yaml" 2>/dev/null | grep -vE "web_search|web_fetch" | grep -A0 "skills:" | head -10 || true)
        if [ -z "$non_native" ]; then native_only=true; fi
      fi
      if [ $first -eq 0 ]; then out="${out},"; fi
      out="${out}{\"squad\":\"${name}\",\"runs\":${total},\"good\":${good},\"partial\":${partial},\"miss\":${miss},\"trend\":\"${trend}\",\"native_only\":${native_only}}"
      first=0
    done
  fi
  out="${out}]"
  echo "$out"
}

# --- Memory file overlap heuristic ---
# Uses a temp file for "seen" set so we work on bash 3.2 (macOS default) without associative arrays.
declare_memory_overlap_count() {
  [ -d "$mem_dir" ] || { echo 0; return; }
  collisions=0
  tmp=$(mktemp 2>/dev/null || echo "/tmp/tide_seen_$$")
  : > "$tmp"
  for f in "$mem_dir"/*.md; do
    [ -f "$f" ] || continue
    h1=$(grep -m1 '^# ' "$f" 2>/dev/null | head -1)
    [ -z "$h1" ] && continue
    if grep -Fxq "$h1" "$tmp" 2>/dev/null; then
      collisions=$((collisions + 1))
    else
      printf '%s\n' "$h1" >> "$tmp"
    fi
  done
  rm -f "$tmp"
  echo "$collisions"
}

# --- Backup hygiene ---
declare_old_backups() {
  count=$(find "$CWD" -name "*.bak-*" -type f -mtime +30 2>/dev/null | wc -l | tr -d ' ')
  echo "${count:-0}"
}

# --- Cadence check ---
declare_run_cadence() {
  recent=0
  prior=0
  if [ -d "$squads_dir" ]; then
    for sig in "$squads_dir"/*/_memory/squad-signals.jsonl; do
      [ -f "$sig" ] || continue
      recent=$((recent + $(awk -v cutoff="$(date -u -v-7d +%Y-%m-%dT00:00:00Z 2>/dev/null || date -u --date='7 days ago' +%Y-%m-%dT00:00:00Z 2>/dev/null)" '$0 ~ /"ts":"/ { match($0, /"ts":"[^"]*"/); ts=substr($0, RSTART+6, RLENGTH-7); if (ts > cutoff) c++ } END {print c+0}' "$sig" 2>/dev/null || echo 0)))
      prior=$((prior + $(awk -v cutoff_high="$(date -u -v-7d +%Y-%m-%dT00:00:00Z 2>/dev/null || date -u --date='7 days ago' +%Y-%m-%dT00:00:00Z 2>/dev/null)" -v cutoff_low="$(date -u -v-14d +%Y-%m-%dT00:00:00Z 2>/dev/null || date -u --date='14 days ago' +%Y-%m-%dT00:00:00Z 2>/dev/null)" '$0 ~ /"ts":"/ { match($0, /"ts":"[^"]*"/); ts=substr($0, RSTART+6, RLENGTH-7); if (ts > cutoff_low && ts <= cutoff_high) c++ } END {print c+0}' "$sig" 2>/dev/null || echo 0)))
    done
  fi
  echo "{\"last_7d\":${recent},\"prior_7d\":${prior}}"
}

# --- Streams snapshot ---
streams_json="["
add_stream() {
  local path="$1"; local label="$2"
  local lines=$(count_lines "$path")
  local last=$(last_entry_date "$path")
  if [ "$streams_json" != "[" ]; then streams_json="${streams_json},"; fi
  streams_json="${streams_json}{\"label\":\"${label}\",\"path\":\"${path}\",\"lines\":${lines},\"last_ts\":\"${last}\"}"
}
add_stream "$skill_signals"     "skill-signals"
add_stream "$skill_candidates"  "skill-candidates"
add_stream "$session_log"       "session-log"
add_stream "$audit_log"         "audit"
add_stream "$gossip"            "gossip"
streams_json="${streams_json}]"

# --- User model status ---
um_age=$(file_age_days "$user_model")
company_age=$(file_age_days "$company_md")

# --- Compose final JSON ---
cat <<EOF
{
  "generated_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "cwd": "${CWD}",
  "streams": ${streams_json},
  "skills": $(declare_skill_quality_summary),
  "squads": $(declare_squad_quality_summary),
  "memory_overlaps": $(declare_memory_overlap_count),
  "old_backups": $(declare_old_backups),
  "cadence": $(declare_run_cadence),
  "user_model_age_days": ${um_age},
  "company_md_age_days": ${company_age}
}
EOF
