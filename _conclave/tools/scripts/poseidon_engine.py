"""
poseidon_engine.py — Conclave RAG Engine
Semantic search over Conclave's collective memory: squad learnings, user model,
eval signals, preferences, run history. Powered by ChromaDB + sentence-transformers.

Usage:
  python3 _conclave/tools/scripts/poseidon_engine.py index               # full re-index
  python3 _conclave/tools/scripts/poseidon_engine.py index --incremental # only changed files
  python3 _conclave/tools/scripts/poseidon_engine.py query --q "text" --n 5
  python3 _conclave/tools/scripts/poseidon_engine.py query --q "text" --squad carousel --n 5
  python3 _conclave/tools/scripts/poseidon_engine.py query --q "text" --mode eval --n 5
  python3 _conclave/tools/scripts/poseidon_engine.py query --q "text" --quality good --n 5
  python3 _conclave/tools/scripts/poseidon_engine.py status
  python3 _conclave/tools/scripts/poseidon_engine.py reset
"""

import os
import sys
import json
import hashlib
import argparse
from datetime import datetime, timezone

try:
    import chromadb
    from chromadb.utils import embedding_functions
    DEPS_OK = True
except ImportError:
    DEPS_OK = False


ROOT_DIR   = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
CHROMA_DIR = os.path.join(ROOT_DIR, "_conclave", "state", "memory", ".chroma")
MEMORY_DIR = os.path.join(ROOT_DIR, "_conclave", "state", "memory")
SQUADS_DIR = os.path.join(ROOT_DIR, "squads")
HISTORY_DIR= os.path.join(ROOT_DIR, "_conclave", "state", "history")
MANIFEST   = os.path.join(MEMORY_DIR, ".index-manifest.json")

COLLECTION_NAME = "conclave_memory"
EMBED_MODEL     = "all-MiniLM-L6-v2"
MAX_CHUNK_CHARS = 1200  # ~300 tokens; keeps chunks retrievable without truncation
JSONL_MAX_LINES = 200   # index only the last N lines from large JSONL streams


# ── manifest (incremental indexing) ──────────────────────────────────────────

def load_manifest() -> dict:
    if os.path.exists(MANIFEST):
        with open(MANIFEST) as f:
            try:
                return json.load(f)
            except Exception:
                return {}
    return {}


def save_manifest(m: dict):
    with open(MANIFEST, "w") as f:
        json.dump(m, f, indent=2)


def file_sig(path: str) -> str:
    """Return mtime+size string as a cheap change-detection signature."""
    try:
        st = os.stat(path)
        return f"{st.st_mtime_ns}:{st.st_size}"
    except OSError:
        return ""


# ── chunking helpers ──────────────────────────────────────────────────────────

def _chunk_text(text: str, max_chars: int = MAX_CHUNK_CHARS) -> list[str]:
    """Split on markdown headers first, then hard-split oversized chunks."""
    import re
    raw = re.split(r"(?m)^(?=#{1,3} )", text)
    chunks = []
    for block in raw:
        block = block.strip()
        if not block:
            continue
        if len(block) <= max_chars:
            chunks.append(block)
        else:
            # hard split at paragraph boundaries
            paras = block.split("\n\n")
            current = ""
            for p in paras:
                if len(current) + len(p) + 2 > max_chars:
                    if current:
                        chunks.append(current.strip())
                    current = p
                else:
                    current = (current + "\n\n" + p).strip()
            if current:
                chunks.append(current.strip())
    return chunks or [text[:max_chars]]


def _chunk_id(source: str, idx: int, text: str) -> str:
    h = hashlib.md5(text.encode()).hexdigest()[:8]
    base = os.path.relpath(source, ROOT_DIR).replace(os.sep, "_").replace(".", "_")
    return f"{base}__{idx}__{h}"


# ── engine class ─────────────────────────────────────────────────────────────

class PoseidonEngine:
    def __init__(self):
        if not DEPS_OK:
            print("Error: Missing dependencies.")
            print("Run: pip install chromadb sentence-transformers")
            sys.exit(1)

        self.client = chromadb.PersistentClient(path=CHROMA_DIR)
        self.emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name=EMBED_MODEL
        )
        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME,
            embedding_function=self.emb_fn
        )
        self.manifest = load_manifest()
        self._indexed = 0
        self._skipped = 0

    # ── indexing ──────────────────────────────────────────────────────────────

    def index(self, incremental: bool = False):
        print(f"[poseidon] Indexing memory ({('incremental' if incremental else 'full')})...")

        # 1. Global memory files
        self._index_md(os.path.join(MEMORY_DIR, "company.md"),           "global", "company", incremental)
        self._index_md(os.path.join(MEMORY_DIR, "user-model.md"),        "global", "user_model", incremental)
        self._index_md(os.path.join(MEMORY_DIR, "preferences.md"),       "global", "preferences", incremental)
        self._index_md(os.path.join(MEMORY_DIR, "global-preferences.md"),"global", "global_preferences", incremental)
        self._index_md(os.path.join(MEMORY_DIR, "linkedin-insights.md"), "global", "linkedin_insights", incremental)
        self._index_md(os.path.join(MEMORY_DIR, "visual-identity.md"),   "global", "visual_identity", incremental)

        # 2. Signal streams (last N lines only — append-only, can be large)
        self._index_jsonl(os.path.join(MEMORY_DIR, "session-log.jsonl"),    "signal", "session_log", incremental)
        self._index_jsonl(os.path.join(MEMORY_DIR, "gossip.jsonl"),         "signal", "gossip", incremental)
        self._index_jsonl(os.path.join(MEMORY_DIR, "skill-signals.jsonl"),  "signal", "skill_signals", incremental)
        self._index_jsonl(os.path.join(MEMORY_DIR, "skill-candidates.jsonl"),"signal","skill_candidates", incremental)
        self._index_jsonl(os.path.join(MEMORY_DIR, "implicit-signals.jsonl"),"signal","implicit_signals", incremental)

        # 3. Squad memories
        if os.path.exists(SQUADS_DIR):
            for squad in sorted(os.listdir(SQUADS_DIR)):
                sp = os.path.join(SQUADS_DIR, squad)
                if not os.path.isdir(sp):
                    continue
                mem = os.path.join(sp, "_memory")
                self._index_md(os.path.join(mem, "memories.md"),    "squad", f"squad_{squad}_memories",  incremental, squad=squad)
                self._index_md(os.path.join(mem, "runs.md"),         "squad", f"squad_{squad}_runs",      incremental, squad=squad)
                self._index_jsonl(os.path.join(mem, "squad-signals.jsonl"),   "signal", f"squad_{squad}_signals",  incremental, squad=squad)
                self._index_jsonl(os.path.join(mem, "implicit-signals.jsonl"),"signal", f"squad_{squad}_implicit", incremental, squad=squad)

                # Index last 5 run outputs (steps.jsonl only — full md outputs are too large)
                output_dir = os.path.join(sp, "output")
                if os.path.exists(output_dir):
                    runs = sorted(
                        [d for d in os.listdir(output_dir) if os.path.isdir(os.path.join(output_dir, d))],
                        reverse=True
                    )[:5]
                    for run_id in runs:
                        steps_path = os.path.join(output_dir, run_id, "steps.jsonl")
                        self._index_jsonl(steps_path, "eval", f"squad_{squad}_steps_{run_id}", incremental, squad=squad, run_id=run_id)

        # 4. History chronicle
        if os.path.exists(HISTORY_DIR):
            for entry in sorted(os.listdir(HISTORY_DIR)):
                if entry.endswith(".md"):
                    self._index_md(os.path.join(HISTORY_DIR, entry), "history", "chronicle", incremental)

        save_manifest(self.manifest)
        print(f"[poseidon] Done. Indexed: {self._indexed} chunks, skipped: {self._skipped} (unchanged).")

    def _index_md(self, path: str, layer: str, category: str, incremental: bool,
                  squad: str = "", run_id: str = ""):
        if not os.path.isfile(path) or os.path.getsize(path) == 0:
            return
        sig = file_sig(path)
        if incremental and self.manifest.get(path) == sig:
            self._skipped += 1
            return

        with open(path, encoding="utf-8") as f:
            text = f.read()

        chunks = _chunk_text(text)
        ids, docs, metas = [], [], []
        for i, chunk in enumerate(chunks):
            cid = _chunk_id(path, i, chunk)
            # Delete old versions of this chunk if they exist
            try:
                self.collection.delete(ids=[cid])
            except Exception:
                pass
            ids.append(cid)
            docs.append(chunk)
            title = chunk.split("\n")[0].replace("#", "").strip()[:80]
            metas.append({
                "source":   os.path.relpath(path, ROOT_DIR),
                "layer":    layer,
                "category": category,
                "section":  title,
                "squad":    squad,
                "run_id":   run_id,
                "quality":  "",
                "ts":       datetime.now(timezone.utc).isoformat(),
            })

        if ids:
            self.collection.upsert(ids=ids, documents=docs, metadatas=metas)
            self._indexed += len(ids)

        self.manifest[path] = sig

    def _index_jsonl(self, path: str, layer: str, category: str, incremental: bool,
                     squad: str = "", run_id: str = ""):
        if not os.path.isfile(path) or os.path.getsize(path) == 0:
            return
        sig = file_sig(path)
        if incremental and self.manifest.get(path) == sig:
            self._skipped += 1
            return

        ids, docs, metas = [], [], []
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()

        # For large files only index the tail (most recent signals)
        tail = lines[-JSONL_MAX_LINES:] if len(lines) > JSONL_MAX_LINES else lines

        for i, line in enumerate(tail):
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
            except Exception:
                continue

            # Build a human-readable representation for embedding
            text = self._jsonl_to_text(data)
            if not text:
                continue

            cid = _chunk_id(path, i, text)
            ids.append(cid)
            docs.append(text)

            quality = data.get("quality", data.get("verdict", ""))
            ts      = data.get("ts", "")
            skill   = data.get("skill", "")
            metas.append({
                "source":   os.path.relpath(path, ROOT_DIR),
                "layer":    layer,
                "category": category,
                "section":  skill or category,
                "squad":    data.get("squad", squad),
                "run_id":   data.get("run_id", run_id),
                "quality":  quality,
                "ts":       ts,
            })

        if ids:
            self.collection.upsert(ids=ids, documents=docs, metadatas=metas)
            self._indexed += len(ids)

        self.manifest[path] = sig

    @staticmethod
    def _jsonl_to_text(data: dict) -> str:
        """Render a JSONL record as a human-readable string for embedding."""
        event = data.get("event", "")
        skill = data.get("skill", "")
        squad = data.get("squad", "")
        quality = data.get("quality", "")
        ts = data.get("ts", "")

        # Skill eval signal (eval harness)
        if data.get("eval_source") == "validate_step":
            failed = data.get("criteria_failed", [])
            passed = data.get("criteria_passed", 0)
            total  = data.get("criteria_total", 0)
            return (
                f"Eval signal — skill: {skill}, squad: {squad}, quality: {quality}, "
                f"step: {data.get('step','')}, passed: {passed}/{total}, "
                f"failed criteria: {'; '.join(failed) if failed else 'none'} [{ts}]"
            )

        # Squad quality signal
        if "delivered" in data:
            return (
                f"Squad run signal — squad: {squad}, quality: {quality}, "
                f"delivered: {data.get('delivered')}, run: {data.get('run_id','')}, "
                f"domain: {data.get('domain','')} [{ts}]"
            )

        # Implicit signal
        if "signal_type" in data:
            return (
                f"Implicit signal — squad: {squad}, type: {data['signal_type']}, "
                f"value: {data.get('value','')}, quality: {quality} [{ts}]"
            )

        # Gossip entry
        if "preference" in data and "category" in data:
            return (
                f"Cross-squad preference — squad: {squad}, domain: {data.get('domain','')}, "
                f"category: {data['category']}, preference: {data['preference']} [{ts}]"
            )

        # Session log
        if event == "run.session":
            return (
                f"Session — squad: {squad}, topic: {data.get('topic','')}, "
                f"output: {data.get('output_type','')}, quality: {quality}, "
                f"domain: {data.get('domain','')} [{ts}]"
            )

        # Steps.jsonl (run step index)
        if "step" in data and "type" in data:
            if data["type"] == "validate":
                failed = data.get("criteria_failed", [])
                return (
                    f"Validate step — squad: {squad}, step: {data['step']}, "
                    f"skill: {data.get('skill','')}, status: {data.get('status','')}, "
                    f"criteria: {data.get('criteria_passed',0)}/{data.get('criteria_total',0)} passed, "
                    f"failed: {'; '.join(failed) if failed else 'none'} [{ts}]"
                )
            if data["type"] == "review":
                return (
                    f"Review step — squad: {squad}, verdict: {data.get('verdict','')}, "
                    f"stage: {data.get('stage','')}, reviewer: {data.get('reviewer','')}, "
                    f"cycle: {data.get('cycle','')} [{ts}]"
                )

        # Skill signal (run-level)
        if skill and quality and not data.get("eval_source"):
            return (
                f"Skill signal — skill: {skill}, squad: {squad}, quality: {quality}, "
                f"run: {data.get('run_id','')} [{ts}]"
            )

        # Fallback: compact JSON representation
        compact = {k: v for k, v in data.items() if v}
        return json.dumps(compact, ensure_ascii=False)[:MAX_CHUNK_CHARS]

    # ── querying ──────────────────────────────────────────────────────────────

    def query(
        self,
        text: str,
        n: int = 5,
        squad: str = "",
        domain: str = "",
        quality: str = "",
        mode: str = "general",
        layer: str = "",
    ) -> list[dict]:
        """
        Query the index with optional filters.

        mode:
          general  — all sources, ranked by similarity
          eval     — only eval/validate signals (criterion-level failures)
          signals  — only quality signals (squad-signals, skill-signals)
          memory   — only squad memories and global preferences
          gossip   — only cross-squad gossip entries
        """
        where_clauses = []

        # Mode-based layer filter
        if mode == "eval":
            where_clauses.append({"category": {"$in": ["skill_signals", "eval"]}})
        elif mode == "signals":
            where_clauses.append({"layer": {"$eq": "signal"}})
        elif mode == "memory":
            where_clauses.append({"layer": {"$in": ["global", "squad"]}})
        elif mode == "gossip":
            where_clauses.append({"category": {"$eq": "gossip"}})
        elif layer:
            where_clauses.append({"layer": {"$eq": layer}})

        # Squad filter
        if squad:
            where_clauses.append({"squad": {"$eq": squad}})

        # Quality filter
        if quality:
            where_clauses.append({"quality": {"$eq": quality}})

        # Combine clauses
        where = None
        if len(where_clauses) == 1:
            where = where_clauses[0]
        elif len(where_clauses) > 1:
            where = {"$and": where_clauses}

        # Fetch slightly more than n to allow re-ranking
        fetch_n = min(n * 3, 50)

        try:
            kw = dict(query_texts=[text], n_results=fetch_n)
            if where:
                kw["where"] = where
            results = self.collection.query(**kw)
        except Exception as e:
            return [{"error": str(e)}]

        docs      = results["documents"][0]
        metas     = results["metadatas"][0]
        distances = results["distances"][0]

        # Re-rank: boost recent + good quality signals
        scored = []
        for doc, meta, dist in zip(docs, metas, distances):
            score = 1.0 - dist  # cosine similarity (higher = better)

            # Recency boost (0–0.1)
            ts_str = meta.get("ts", "")
            try:
                ts = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
                age_days = (datetime.now(timezone.utc) - ts).days
                recency_boost = max(0.0, 0.1 * (1.0 - age_days / 180))
            except Exception:
                recency_boost = 0.0

            # Quality boost
            q = meta.get("quality", "")
            quality_boost = 0.1 if q == "good" else (-0.05 if q == "miss" else 0.0)

            # Squad relevance boost (if squad filter was set, already filtered; but for domain)
            final_score = score + recency_boost + quality_boost
            scored.append((final_score, doc, meta))

        scored.sort(key=lambda x: x[0], reverse=True)

        # Deduplicate by content fingerprint (skip near-identical chunks)
        seen_fps = set()
        deduped = []
        for s, doc, meta in scored:
            fp = hashlib.md5(doc.strip().encode()).hexdigest()
            if fp in seen_fps:
                continue
            # Also skip chunks that are mostly whitespace or empty sections
            if len(doc.strip()) < 30:
                continue
            seen_fps.add(fp)
            deduped.append((s, doc, meta))

        return [
            {
                "score":    round(s, 4),
                "content":  doc,
                "source":   meta.get("source", ""),
                "squad":    meta.get("squad", ""),
                "quality":  meta.get("quality", ""),
                "ts":       meta.get("ts", ""),
                "section":  meta.get("section", ""),
                "layer":    meta.get("layer", ""),
            }
            for s, doc, meta in deduped[:n]
        ]

    # ── status ────────────────────────────────────────────────────────────────

    def status(self):
        count = self.collection.count()
        manifest_files = len(self.manifest)
        print(f"[poseidon] Collection: {COLLECTION_NAME}")
        print(f"[poseidon] Total chunks indexed: {count}")
        print(f"[poseidon] Files tracked in manifest: {manifest_files}")
        print(f"[poseidon] Chroma path: {CHROMA_DIR}")

    # ── reset ─────────────────────────────────────────────────────────────────

    def reset(self):
        self.client.delete_collection(COLLECTION_NAME)
        if os.path.exists(MANIFEST):
            os.remove(MANIFEST)
        print("[poseidon] Index and manifest cleared.")


# ── CLI ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    os.chdir(ROOT_DIR)

    parser = argparse.ArgumentParser(description="Poseidon RAG Engine")
    sub = parser.add_subparsers(dest="action")

    # index
    p_idx = sub.add_parser("index", help="Build or update the index")
    p_idx.add_argument("--incremental", action="store_true",
                       help="Only re-index files that changed since last run")

    # query
    p_qry = sub.add_parser("query", help="Semantic search")
    p_qry.add_argument("--q",       required=True, help="Query string")
    p_qry.add_argument("--n",       type=int, default=5, help="Number of results (default: 5)")
    p_qry.add_argument("--squad",   default="",     help="Filter to a specific squad")
    p_qry.add_argument("--domain",  default="",     help="Domain hint (informational)")
    p_qry.add_argument("--quality", default="",     help="Filter by quality: good|partial|miss")
    p_qry.add_argument("--mode",    default="general",
                       choices=["general","eval","signals","memory","gossip"],
                       help="Query mode (default: general)")
    p_qry.add_argument("--layer",   default="",     help="Filter by layer: global|squad|signal|eval|history")

    # status
    sub.add_parser("status", help="Show index stats")

    # reset
    sub.add_parser("reset", help="Delete the index and manifest")

    args = parser.parse_args()
    if not args.action:
        parser.print_help()
        sys.exit(0)

    engine = PoseidonEngine()

    if args.action == "index":
        engine.index(incremental=getattr(args, "incremental", False))

    elif args.action == "query":
        results = engine.query(
            text=args.q,
            n=args.n,
            squad=args.squad,
            domain=args.domain,
            quality=args.quality,
            mode=args.mode,
            layer=args.layer,
        )
        print(json.dumps(results, indent=2, ensure_ascii=False))

    elif args.action == "status":
        engine.status()

    elif args.action == "reset":
        engine.reset()
