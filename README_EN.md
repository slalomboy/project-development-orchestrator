# Project Development Orchestrator

For individuals and teams that need a reusable Agent Skill workflow. This package addresses a concrete workflow problem and returns an auditable next step instead of claiming external completion.

**Current status:** `v0.1.0-alpha.1` is the first fixed source version. No GitHub Release is provided. **Next step:** install the fixed Tag, run one minimal invocation, and keep every external action behind human approval. [中文主入口](README.md).

## Problem and result

- 识别新建、续做与接管场景
- 建立需求—验收—测试追溯
- 判断版本影响
- 输出交付与回滚状态

## Installation

Install the fixed Tag: `git clone --branch v0.1.0-alpha.1 --depth 1 https://github.com/slalomboy/project-development-orchestrator.git`. Install the repository root as a Skill.

## First use

Invoke it with the example in [Quickstart](docs/en/quickstart.md).

## Workflow

The Skill confirms the input and authorization boundary, selects the minimum capability, produces a local reviewable result, and stops before any external action.

## Verified scope

The repository structure, fixed version, required paths, temporary-directory installation, bilingual facts, license, and sensitive-data boundary are covered by deterministic checks.

## Limitations

- 不包含私有治理规则、账号、项目清单或交付数据
- 不自动部署、推送、付费或改权限
- 专业实现仍交给对应领域能力

## Version, license, and provenance

- Version: `v0.1.0-alpha.1`.
- License: [`Apache-2.0`](LICENSE), explicitly selected by the owner.
- Provenance: a public-light rewrite of an internally developed Dalin AI Works capability. Private paths, credentials, customer data, and internal control planes are excluded.
- Status: `PUBLICATION_AUTHORIZED_PENDING_REMOTE_VERIFICATION`.

[中文主入口](README.md) · [English docs](docs/en/README.md) · [License record](LICENSE-DECISION.md)
