# 快速开始

[English](en/quickstart.md) · [返回首页](../README.md)

1. 从固定 Tag 克隆：`git clone --branch v0.5.0-alpha.1 --depth 1 https://github.com/slalomboy/project-development-orchestrator.git`。
2. 先运行：`python3 -m unittest discover -s project-development-orchestrator/tests -p 'test_*.py'`。
3. 确认目标 Skill 目录不存在后再复制。
4. 第一次调用只读核对项目事实，停在计划与验收，不部署、不推送。

若项目已有 `project-state.json`，先运行 `python3 scripts/validate_project_state.py <path>`，事实与旧状态冲突时以新鲜证据为准。
