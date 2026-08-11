import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_project_state.py"


def valid_state():
    return {
        "schema_version": "1.0",
        "project": {"name": "Example", "slug": "example"},
        "mode": "greenfield",
        "profile": "standard",
        "stage": "planning",
        "status": "active",
        "version": "0.1.0",
        "artifacts": [{"id": "PRD-001", "path": "docs/prd.md", "status": "approved"}],
        "active_change": None,
        "decisions": [],
        "blockers": [],
        "pending_approvals": [],
        "last_verification": {"status": "pending", "evidence": []},
        "next_action": "Create implementation tasks",
        "updated_at": "2026-07-12T12:00:00+08:00",
    }


class ValidateProjectStateTests(unittest.TestCase):
    def run_validator(self, state):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "project-state.json"
            path.write_text(json.dumps(state), encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(VALIDATOR), str(path)],
                capture_output=True,
                text=True,
                check=False,
            )

    def test_valid_state_passes(self):
        result = self.run_validator(valid_state())
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("VALID", result.stdout)

    def test_missing_required_field_fails(self):
        state = valid_state()
        del state["next_action"]
        result = self.run_validator(state)
        self.assertEqual(result.returncode, 1)
        self.assertIn("next_action", result.stdout)

    def test_invalid_stage_fails(self):
        state = valid_state()
        state["stage"] = "coding"
        result = self.run_validator(state)
        self.assertEqual(result.returncode, 1)
        self.assertIn("stage", result.stdout)

    def test_completed_state_requires_passed_verification(self):
        state = valid_state()
        state["status"] = "completed"
        result = self.run_validator(state)
        self.assertEqual(result.returncode, 1)
        self.assertIn("verification", result.stdout.lower())


if __name__ == "__main__":
    unittest.main()
