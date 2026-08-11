# Quality Gates

Apply gates proportional to the selected profile and risk.

## Product and specification

- First-release boundary, exclusions and observable success are explicit.
- Every approved requirement has acceptance criteria and an owner or source.
- Assumptions that could change the result have a validation action.

## Design and architecture

- Core user flow, failure, empty, loading and permission states are covered.
- New product-grade UI or broad redesign has an accepted visual target, information architecture, page-state matrix, design contract and captured rendered evidence. Use [ui-design-gate.md](ui-design-gate.md).
- Data ownership, interfaces, security boundaries and migration impact are explicit.
- Material trade-offs have a decision record and rollback or exit strategy.

## Implementation

- Tests are written before behavior changes where applicable.
- Build, type, lint, unit and integration checks run according to project conventions.
- No unrelated refactor or user-owned change is absorbed.

## Verification

- Acceptance is tested against the built artifact or live behavior, not only source.
- Evidence includes commands, results, screenshots, queries, or artifact inspection appropriate to the claim.
- Failure paths, permissions, data integrity and edge states are checked where relevant.

## Release and operations

- Version, changelog, migration, environment and deployment records agree.
- Apply [delivery-truth-gates.md](delivery-truth-gates.md): source, candidate, installed application, platform trust, Git/Release assets and customer distribution remain parallel truth surfaces.
- Release requires explicit approval and a tested or clearly bounded rollback.
- Customer-visible version and health are verified after deployment.
- Monitoring, unresolved risks and the next operational action are recorded.
