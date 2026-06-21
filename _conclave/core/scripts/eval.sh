#!/usr/bin/env bash
# eval.sh — Eval Harness aggregation script
# Reads per-step eval signals from skill-signals.jsonl (eval_source: "validate_step")
# and steps.jsonl files across all squad runs. Emits a JSON summary to stdout for
# POSEIDON criterion-level pattern detection.
#
# Invoked by: poseidon.agent.md (as part of /conclave tide, section: Eval Currents)
# Output: single-line JSON to stdout
# Exit codes: 0 = success (even if no eval signals found)
#
# Requires: bash 3.2+, grep, awk, sed — no jq dependency

set -euo pipefail

CWD="${CWD:-$(pwd)}"

mem_dir="${CWD}/_conclave/state/memory"
squads_dir="${CWD}/squads"
skill_signals="${mem_dir}/skill-signals.jsonl"

# ── helpers ──────────────────────────────────────────────────────────────────

count_lines() { [ -f "$1" ] && wc -l < "$1" | tr -d ' ' || echo 0; }

extract_field() {
  # extract_field <file_or_string> <field_name>
  # Returns value of "field":"value" from a JSON line (string values only)
  echo "$1" | grep -oE "\"${2}\":\"[^\"]*\"" | head -1 | sed "s/\"${2}\":\"//;s/\"$//"
}

extract_array_field() {
  # Extracts a JSON array value: "field":["a","b"] → a|b (pipe-separated)
  echo "$1" | grep -oE "\"${2}\":\[[^]]*\]" | head -1 | sed "s/\"${2}\":\[//;s/\]$//" | tr ',' '\n' | sed 's/"//g' | tr '\n' '|' | sed 's/|$//'
}

extract_int_field() {
  echo "$1" | grep -oE "\"${2}\":[0-9]+" | head -1 | sed "s/\"${2}\"://"
}

# ── 1. Read eval signals from skill-signals.jsonl ────────────────────────────
# Filter only lines with eval_source: validate_step

eval_signals_tmp=$(mktemp 2>/dev/null || echo "/tmp/eval_signals_$$")
: > "$eval_signals_tmp"

if [ -f "$skill_signals" ] && [ -s "$skill_signals" ]; then
  grep '"eval_source":"validate_step"' "$skill_signals" >> "$eval_signals_tmp" 2>/dev/null || true
fi

# Also sweep steps.jsonl from all squad runs (last 10 runs per squad)
if [ -d "$squads_dir" ]; then
  for squad_dir in "$squads_dir"/*/; do
    [ -d "$squad_dir" ] || continue
    output_dir="${squad_dir}output"
    [ -d "$output_dir" ] || continue
    # get last 10 run folders sorted by name (YYYY-MM-DD-HHmmss format → natural sort)
    run_dirs=$(ls -1 "$output_dir" 2>/dev/null | sort -r | head -10)
    for run_id in $run_dirs; do
      steps_file="${output_dir}/${run_id}/steps.jsonl"
      [ -f "$steps_file" ] || continue
      # extract validate-type entries that have a skill field
      grep '"type":"validate"' "$steps_file" 2>/dev/null | grep '"skill":"' >> "$eval_signals_tmp" 2>/dev/null || true
    done
  done
fi

eval_total=$(wc -l < "$eval_signals_tmp" | tr -d ' ')

if [ "$eval_total" -eq 0 ]; then
  rm -f "$eval_signals_tmp"
  echo '{"eval_signals":0,"skills":[],"recurring_failures":[],"note":"no eval signals yet — add type:validate steps with skill_contract to pipelines"}'
  exit 0
fi

# ── 2. Aggregate per-skill quality distribution ───────────────────────────────

skills_tmp=$(mktemp 2>/dev/null || echo "/tmp/eval_skills_$$")
: > "$skills_tmp"

while IFS= read -r line; do
  skill=$(extract_field "$line" "skill")
  quality=$(extract_field "$line" "quality")
  [ -z "$skill" ] && continue
  [ -z "$quality" ] && continue
  echo "${skill}	${quality}" >> "$skills_tmp"
done < "$eval_signals_tmp"

skills_json="["
first_skill=1
skill_names=$(awk '{print $1}' "$skills_tmp" | sort -u 2>/dev/null)

for s in $skill_names; do
  [ -z "$s" ] && continue
  rows=$(grep -P "^${s}\t" "$skills_tmp" 2>/dev/null || true)
  total=$(echo "$rows" | grep -c . 2>/dev/null || echo 0)
  good=$(echo "$rows" | grep -c $'\tgood$' 2>/dev/null || echo 0)
  partial=$(echo "$rows" | grep -c $'\tpartial$' 2>/dev/null || echo 0)
  miss=$(echo "$rows" | grep -c $'\tmiss$' 2>/dev/null || echo 0)
  last5_rows=$(grep -P "^${s}\t" "$skills_tmp" 2>/dev/null | tail -5 || true)
  last5_miss=$(echo "$last5_rows" | grep -c $'\tmiss$' 2>/dev/null || echo 0)
  last5_partial=$(echo "$last5_rows" | grep -c $'\tpartial$' 2>/dev/null || echo 0)
  last5_bad=$((last5_miss + last5_partial))
  if [ $first_skill -eq 0 ]; then skills_json="${skills_json},"; fi
  skills_json="${skills_json}{\"skill\":\"${s}\",\"eval_runs\":${total},\"good\":${good},\"partial\":${partial},\"miss\":${miss},\"last5_bad\":${last5_bad}}"
  first_skill=0
done
skills_json="${skills_json}]"

# ── 3. Aggregate recurring criterion failures ─────────────────────────────────
# For each skill, find criteria that appear in failed_criteria across multiple runs

criteria_tmp=$(mktemp 2>/dev/null || echo "/tmp/eval_criteria_$$")
: > "$criteria_tmp"

while IFS= read -r line; do
  skill=$(extract_field "$line" "skill")
  quality=$(extract_field "$line" "quality")
  [ -z "$skill" ] && continue
  [ "$quality" = "good" ] && continue  # only failures matter
  # Extract failed_criteria array items
  failed_section=$(echo "$line" | grep -oE '"criteria_failed":\[[^]]*\]' | head -1 | sed 's/"criteria_failed":\[//;s/\]$//')
  [ -z "$failed_section" ] && continue
  # each item is "text" — strip quotes and split by ","
  echo "$failed_section" | tr ',' '\n' | sed 's/^ *"//;s/" *$//' | while IFS= read -r criterion; do
    [ -z "$criterion" ] && continue
    echo "${skill}	${criterion}"
  done >> "$criteria_tmp"
done < "$eval_signals_tmp"

# Count occurrences per skill+criterion, emit those appearing 2+ times
recurring_json="["
first_rec=1

if [ -s "$criteria_tmp" ]; then
  sort "$criteria_tmp" | uniq -c | sort -rn | while read -r count skill_criterion; do
    [ "$count" -lt 2 ] && break
    skill=$(echo "$skill_criterion" | cut -f1)
    criterion=$(echo "$skill_criterion" | cut -f2-)
    # escape for JSON
    criterion_escaped=$(echo "$criterion" | sed 's/"/\\"/g')
    if [ $first_rec -eq 0 ]; then recurring_json="${recurring_json},"; fi
    recurring_json="${recurring_json}{\"skill\":\"${skill}\",\"criterion\":\"${criterion_escaped}\",\"fail_count\":${count}}"
    first_rec=0
  done 2>/dev/null || true
fi
recurring_json="${recurring_json}]"

# ── 4. Cleanup and emit ───────────────────────────────────────────────────────

rm -f "$eval_signals_tmp" "$skills_tmp" "$criteria_tmp"

cat <<EOF
{
  "generated_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "eval_signals": ${eval_total},
  "skills": ${skills_json},
  "recurring_failures": ${recurring_json}
}
EOF
