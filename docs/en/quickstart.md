# Quickstart

[中文指南](../quickstart.md) · [中文主入口](../../README.md) · [Back to English README](../../README_EN.md)

1. Clone the fixed Tag: `git clone --branch v0.5.0-alpha.1 --depth 1 https://github.com/slalomboy/project-development-orchestrator.git`.
2. Run `python3 -m unittest discover -s project-development-orchestrator/tests -p 'test_*.py'`.
3. Confirm that the target Skill directory does not already exist before copying.
4. Make the first call read-only. Stop at a plan and acceptance boundary; do not deploy or push.

When `project-state.json` exists, run `python3 scripts/validate_project_state.py <path>` first. Fresh evidence wins when state and verified facts disagree.
