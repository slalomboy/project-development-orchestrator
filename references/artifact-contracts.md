# Artifact Contracts

Use stable IDs so decisions remain traceable across files.

| Artifact | Required content | Traceability |
|---|---|---|
| Project brief | Problem, users, core flow, must-have, excluded, constraints, success | Source for requirements |
| PRD/spec | `REQ-*`, behavior, priority, `AC-*`, assumptions, exclusions | Each requirement links to acceptance |
| Architecture | system boundary, components, data, interfaces, security, risks, `ADR-*` | Decisions link to `REQ-*` |
| Tasks | `TASK-*`, deliverable, dependencies, status, verification | Each task links to `REQ-*` and `TEST-*` |
| Test plan | `TEST-*`, linked `AC-*`, setup, action, expected result, evidence | Every approved acceptance criterion is covered |
| Change proposal | `CHG-*`, rationale, impact, ADDED/MODIFIED/REMOVED requirements | Keeps approved truth separate from proposals |
| Release plan | version, included changes, migration, verification, rollback | Links delivered tasks and evidence |
| Decision record | `ADR-*`, context, options, decision, consequences, rollback | Links impacted requirements and risks |
| Project state | stage, status, artifacts, decisions, blockers, approvals, evidence, next action | Index to current project truth |

Start from `assets/templates/`. Remove optional sections that do not apply, but never remove required traceability, verification, exclusions, risk, or rollback fields for the selected profile.

Store artifacts where project conventions place durable documentation. Do not create a parallel documentation universe when an existing structure already serves the same contract.
