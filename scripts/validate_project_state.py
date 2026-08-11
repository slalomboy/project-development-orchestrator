#!/usr/bin/env python3
import json
import sys
from pathlib import Path


REQUIRED = {
    "schema_version",
    "project",
    "mode",
    "profile",
    "stage",
    "status",
    "version",
    "artifacts",
    "active_change",
    "decisions",
    "blockers",
    "pending_approvals",
    "last_verification",
    "next_action",
    "updated_at",
}
MODES = {"greenfield", "brownfield", "takeover"}
PROFILES = {"lightweight", "standard", "full"}
STAGES = {
    "intake",
    "discovery",
    "specification",
    "design",
    "planning",
    "implementation",
    "verification",
    "release",
    "operate",
}
STATUSES = {"active", "blocked", "paused", "completed"}


def validate(state):
    errors = []
    missing = sorted(REQUIRED - set(state))
    if missing:
        errors.append("missing required fields: " + ", ".join(missing))
    if state.get("mode") not in MODES:
        errors.append("mode must be one of: " + ", ".join(sorted(MODES)))
    if state.get("profile") not in PROFILES:
        errors.append("profile must be one of: " + ", ".join(sorted(PROFILES)))
    if state.get("stage") not in STAGES:
        errors.append("stage must be one of: " + ", ".join(sorted(STAGES)))
    if state.get("status") not in STATUSES:
        errors.append("status must be one of: " + ", ".join(sorted(STATUSES)))
    project = state.get("project")
    if not isinstance(project, dict) or not project.get("name") or not project.get("slug"):
        errors.append("project must contain non-empty name and slug")
    verification = state.get("last_verification")
    if not isinstance(verification, dict) or "status" not in verification or "evidence" not in verification:
        errors.append("last_verification must contain status and evidence")
    if state.get("status") == "completed" and (
        not isinstance(verification, dict) or verification.get("status") != "passed" or not verification.get("evidence")
    ):
        errors.append("completed status requires passed verification with evidence")
    if not isinstance(state.get("next_action"), str) or not state.get("next_action", "").strip():
        errors.append("next_action must be a non-empty string")
    return errors


def main(argv):
    if len(argv) != 2:
        print("Usage: validate_project_state.py PATH", file=sys.stderr)
        return 2
    path = Path(argv[1])
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"INVALID: {error}")
        return 1
    errors = validate(state)
    if errors:
        for error in errors:
            print(f"INVALID: {error}")
        return 1
    print(f"VALID: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
