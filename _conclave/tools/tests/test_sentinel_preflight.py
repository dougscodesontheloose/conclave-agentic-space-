import importlib.util
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
SCRIPT_PATH = REPO_ROOT / "_conclave" / "tools" / "scripts" / "sentinel_preflight.py"
SPEC = importlib.util.spec_from_file_location("sentinel_preflight", SCRIPT_PATH)
SENTINEL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SENTINEL)


class ParseAgentPathsTests(unittest.TestCase):
    def parse(self, content):
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / "squad-party.csv"
            csv_path.write_text(content, encoding="utf-8")
            return SENTINEL.parse_agent_paths(csv_path)

    def test_parses_header_based_format(self):
        paths = self.parse(
            "id,name,title,icon,execution,path\n"
            "writer,Gibson Writer,Writer,pen,inline,./agents/writer.agent.md\n"
        )

        self.assertEqual(paths, ["./agents/writer.agent.md"])

    def test_parses_legacy_format_without_dropping_first_agent(self):
        paths = self.parse(
            "./agents/first.agent.md,First Agent,icon,Role\n"
            "./agents/second.agent.md,Second Agent,icon,Role\n"
        )

        self.assertEqual(
            paths,
            ["./agents/first.agent.md", "./agents/second.agent.md"],
        )


class RepositoryLayoutTests(unittest.TestCase):
    def test_skills_directory_points_to_repository_catalog(self):
        self.assertEqual(Path(SENTINEL.SKILLS_DIR), REPO_ROOT / "skills")


if __name__ == "__main__":
    unittest.main()
