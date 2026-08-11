---
name: project-development-orchestrator
description: Use when starting, continuing, taking over, changing, debugging, testing, deploying, documenting, or releasing a software project, including product, UI/UX, frontend, backend, database, authentication, storage, integrations, analytics, and technical documentation. Do not use for pure Q&A, explanations, chat, or one-off copy drafts.
---

# Project Development Orchestrator

## Purpose

Act as the lifecycle control plane. Establish project truth, select the smallest useful workflow, maintain recoverable state, route specialist Skills, enforce authorization gates, and close work with real verification, versioning, records, and rollback.

## Non-Negotiable Rules

1. Begin read-only unless execution is already authorized. Preserve user files and unrelated changes.
2. Read applicable instructions and existing project facts before planning.
3. Keep durable state in `project-state.json`; verified code, artifacts, and live behavior override stale state.
4. Never claim a user-visible result from source inspection alone.
5. Deployment, publishing, pushing, production data changes, permission expansion, and destructive recovery require explicit approval.
6. `直接执行` skips the approval wait for agreed implementation, not discovery, state, tests, logging, or release authorization.

## Start or Resume

1. Classify mode: `greenfield`, `brownfield`, or `takeover`.
2. Find the nearest instructions and inspect README, docs, manifests, version, tests, configuration, outputs, deployment facts, and Git state when present.
3. If `project-state.json` exists, validate it with `scripts/validate_project_state.py`; reconcile conflicts against verified facts.
4. Select profile: `lightweight`, `standard`, or `full`. Read [intake.md](references/intake.md) for selection and the six-field intake.
5. Read [lifecycle.md](references/lifecycle.md) to enter or resume the correct stage.
6. For Dalin AI Works software, cross-project reuse, or work needing stronger delivery discipline, read [dalin-delivery-gates.md](references/dalin-delivery-gates.md).
7. For new UI, broad redesign, flow changes or product-grade visual work, read [ui-design-gate.md](references/ui-design-gate.md) before editing UI code.
8. For packaging, installation, release or completion claims, read [delivery-truth-gates.md](references/delivery-truth-gates.md).
9. When a Superpowers process Skill may apply, read [superpowers-routing.md](references/superpowers-routing.md) before invoking it. This Skill remains the lifecycle control plane.
10. When delegation or parallel work may add value, read [multi-agent-routing.md](references/multi-agent-routing.md) and assess authorization, independence, ownership, quota evidence, and integration cost before dispatch.

For pure explanation, read-only reporting, or a one-off draft, answer directly and stop using this Skill.

## Control Loop

For every stage:

1. Confirm inputs and unresolved decisions.
2. Create only the artifacts required by the selected profile; use [artifact-contracts.md](references/artifact-contracts.md).
3. For greenfield work follow the baseline-spec flow; for brownfield or takeover changes follow [spec-management.md](references/spec-management.md).
4. Select only installed capabilities needed for this stage using [capability-routing.md](references/capability-routing.md). Name their roles to the user. Apply the UI design gate before product-grade UI implementation and the delivery-truth gate before packaging or completion claims. If multi-agent work is eligible, choose inline, sequential, or parallel execution using [multi-agent-routing.md](references/multi-agent-routing.md); default to the minimum useful delegation.
5. For mutations, provide objective, scope, exclusions, steps, risks, version impact, verification, success criteria, the multi-agent and quota decision when relevant, and the exact authorization phrase. Wait unless already authorized.
6. Execute within scope, test before implementation where applicable, and avoid unrelated refactors.
7. Apply [quality-gates.md](references/quality-gates.md), record evidence, update `project-state.json`, and set one concrete `next_action`.
8. If a gate fails, preserve evidence and return to the responsible stage. Do not advance by relabeling the result.

## State and Recovery

Copy `assets/templates/project-state.json` into the project documentation area chosen by existing conventions. Keep artifact IDs, active change, decisions, blockers, pending approvals, last verification evidence, and next action current. A new session must resume from state plus project facts rather than asking the user to repeat history.

Use `blocked` only for an actual impasse, `paused` for an intentional stop, and `completed` only when required verification passed with evidence. Validate the state after every stage transition.

## Approval Gates

Explicit approval is required for:

- First-release scope when it materially changes cost, time, or product promise.
- Architecture choices with significant cost, lock-in, security, or migration impact.
- New dependencies, external writes, permission expansion, data migration, or destructive action.
- Deployment, publication, push, release, or production operation.

Do not repeatedly ask for approval for read-only discovery, drafts, tests, or implementation already covered by the agreed scope.

## Version and Records

Inspect the existing version convention first; default to Semantic Versioning. Keep version source, changelog or release notes, lockfiles, tags, deployment metadata, project state, project log, and configured global log consistent when applicable and authorized. Never alter a released version in place.

## Completion Gate

Before completion, confirm all applicable items:

- Project instructions, mode, profile, facts, and state were established.
- Approved requirements have acceptance criteria and trace to tasks and tests.
- Scope and authorization were respected; changes are not silently absorbed.
- Delegation, if used, had valid authorization, isolated ownership, bounded quota, reviewed outputs, and primary-agent integration evidence.
- Automated checks and user-visible behavior were freshly verified.
- Product-grade UI changes had an accepted visual target, state matrix, design contract and rendered evidence; `lightweight` validation exceptions were bounded and recorded.
- Failure, empty, loading, permission, data, security, migration, and rollback states were checked where relevant.
- Long-running operations define conflicts, ownership, release paths, partial-result persistence, failed-unit-only retry and safe read-only availability where applicable.
- Version and records agree with the delivered artifact.
- Source, candidate package, installed app, platform trust, Git/Tag/Release assets and customer distribution were reported as parallel truth surfaces; the overall conclusion matches the weakest required surface.
- `project-state.json` validates, contains evidence, and names the next action.
- Remaining risks, unverified areas, and rollback are explicit.

If any required item is false, report incomplete or blocked status instead of success.
