# Project Development Orchestrator

[中文](README.md) · [Finished-capability map](docs/en/productization-map.md)

Move a software project from an ambiguous request to a verifiable, traceable, and recoverable delivery state. The Skill maintains project truth, specification, planning, evidence, version, and rollback boundaries while routing specialist implementation to the relevant capability.

> Status: public alpha · Fixed source: [`v0.5.0-alpha.1`](https://github.com/slalomboy/project-development-orchestrator/tree/v0.5.0-alpha.1) · Apache-2.0 · Python 3.10+ · No automatic deployment, publication, push, or permission change

## User problem and result

Finished code is not the same as a delivered project. Requirements, source, packages, installation, Tags, Releases, and user-visible results are often collapsed into one completion claim. This Skill keeps those truth surfaces separate and requires evidence before lifecycle state advances.

Use it for greenfield, brownfield, or takeover software work. Do not use it for pure Q&A or one-off copy, and do not treat it as a replacement for frontend, database, video, or other specialist Skills.

## Finished capabilities

- `FIN-PM-000`: complete control plane from intake through verification, versioning, rollback, and review;
- `FIN-PM-001`: six-field brief, specification, acceptance criteria, and change boundary;
- `FIN-PM-002`: task plan with owners, dependencies, acceptance, and test traceability;
- `FIN-PM-003`: delivery-truth audit across source, candidate, installation, platform trust, Git/Release, and user distribution;
- `FIN-PM-004`: aligned version, Tag, artifact, compatibility, and rollback record.

See the [finished-capability map](docs/en/productization-map.md) for inputs, outputs, claimable handouts, and upgrade paths.

## Install

    git clone --branch v0.5.0-alpha.1 --depth 1 https://github.com/slalomboy/project-development-orchestrator.git
    cp -R project-development-orchestrator "$HOME/.codex/skills/project-development-orchestrator"
    python3 -m unittest discover -s project-development-orchestrator/tests -p 'test_*.py'

Confirm that the target directory does not already exist. The repository intentionally provides no overwrite installer.

## First successful path

Ask an Agent:

> Use `project-development-orchestrator` to take over this project. Read the repository, version, tests, and current state first. Return the objective, scope, exclusions, risks, acceptance, and one next action. Do not deploy or push.

The first useful result is a fact-backed current stage, gaps, evidence, and one next action—not a claim that the code merely looks correct.

## Skill workflow and routing

1. Complete the six-field intake and choose the smallest risk profile.
2. Trace requirements, acceptance, architecture, tasks, and tests with stable IDs.
3. Confirm scope and authority, then route implementation to specialist Skills.
4. Advance verification only with fresh behavioral evidence.
5. Report source, candidate, installation, platform trust, Git/Release, and user distribution separately.
6. Record version, remaining risk, rollback, and one next action.

[Quickstart](docs/en/quickstart.md) · [Usage](docs/en/usage.md) · [Limitations](docs/en/limitations.md)

## Verified results

- 15/15 package tests pass.
- Valid and invalid `project-state.json` transitions and missing evidence are reproducible.
- Templates, references, state validator, and Skill entry are included in the public candidate.
- Source-candidate verification does not prove deployment, Release, installed behavior, or user-side distribution.

## Limitations, privacy, and public boundary

The public package excludes private roles, customer data, accounts, credentials, internal project records, and machine-specific paths. External writes, dependency installation, migration, deployment, publication, pushes, permissions, and destructive operations still require explicit authorization. The Skill cannot decide material cost, architecture, or safety choices for the user.

Market demand is **not validated**. The evidence proves repeatable behavior and project use only; it does not prove demand or business outcomes.

## License and provenance

Original code and documentation use [Apache License 2.0](LICENSE). Maintainer: Dalin AI Works. Third-party tools, platforms, and project code retain their own licenses. A fixed Tag is source traceability only; this version has no GitHub Release.
