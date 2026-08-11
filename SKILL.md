---
name: project-development-orchestrator
description: Use when a user needs project development orchestrator with explicit evidence and authorization boundaries.
---

# Project Development Orchestrator

## Workflow

1. Confirm the user's input, intended result, ownership, and external-action boundary.
2. Select only the minimum capability required for the request.
3. Produce a local, reviewable artifact with sources, assumptions, limitations, and next action.
4. Stop before deployment, publishing, account writes, spending, permission changes, or any other external side effect unless separately authorized.
5. Report what was verified and what remains blocked.

## Capabilities

- 识别新建、续做与接管场景
- 建立需求—验收—测试追溯
- 判断版本影响
- 输出交付与回滚状态

## Hard boundaries

- 不包含私有治理规则、账号、项目清单或交付数据
- 不自动部署、推送、付费或改权限
- 专业实现仍交给对应领域能力

## Example request

使用 project-development-orchestrator 接手这个现有项目，先只读盘点事实并给出最小修复计划。
