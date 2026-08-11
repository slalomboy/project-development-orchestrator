# Lifecycle

Stages advance only when the exit gate has evidence. Record every transition in `project-state.json`.

| Stage | Purpose | Exit gate |
|---|---|---|
| `intake` | Capture the six-field project brief | Scope, success and constraints are usable |
| `discovery` | Establish repository, user, system and deployment facts | Unknowns and risks are bounded |
| `specification` | Define requirements and acceptance behavior | Requirements are approved and traceable |
| `design` | Decide UX, architecture, data, security and integrations | Material decisions and trade-offs are approved |
| `planning` | Split work into testable tasks | Tasks trace to requirements and tests |
| `implementation` | Build within approved scope | Tasks complete and automated checks pass |
| `verification` | Prove real behavior and acceptance | Fresh evidence covers required paths and states |
| `release` | Version, deploy, verify and prepare rollback | Release authorized and customer-visible health proven |
| `operate` | Monitor, learn and manage changes | Next change or operational action is recorded |

## Transitions

- Normal path follows the table order.
- A failed gate returns to the stage that owns the defect.
- Requirement changes return to `specification`; architecture-impacting changes also reopen `design`.
- `blocked` records the exact impasse and needed external change. `paused` records intentional suspension and resumption conditions.
- `completed` requires passed verification with evidence; release is not required for work whose agreed deliverable is a draft or local artifact.

## Resume protocol

1. Validate state.
2. Re-read linked artifacts and current repository or deployment facts.
3. Reconcile discrepancies; facts win over stale descriptions.
4. Restate current stage, last verified evidence, blockers, pending approvals and next action.
5. Continue without re-collecting settled information.
