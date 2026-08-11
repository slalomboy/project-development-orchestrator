# Specification Management

## Greenfield baseline flow

1. Approve the project brief.
2. Create requirements and acceptance criteria as the baseline specification.
3. Record architecture decisions and tasks linked to the baseline.
4. Implement and verify against acceptance criteria.
5. After release, treat the approved specification as Current truth.

## Brownfield and takeover change flow

Keep Current truth separate from proposed work:

1. Inspect current code, behavior, docs and deployment evidence.
2. Create a Change proposal with a `CHG-*` ID, rationale, impact, tasks and spec deltas.
3. Express deltas as `ADDED`, `MODIFIED`, or `REMOVED`; include complete acceptance behavior for every changed requirement.
4. Obtain approval for scope and material decisions before implementation.
5. Implement and verify only the approved change.
6. Archive the change by merging verified deltas into Current truth and recording version and evidence.

## Change control

- Never silently overwrite approved requirements.
- When scope expands, report impact on time, risk, version and excluded work.
- A small correction may amend an active proposal; a materially different outcome gets a new proposal.
- Rejected proposals remain as decision evidence or are marked rejected; they are not represented as current behavior.
- If code, documentation and production disagree, label the discrepancy and establish verified truth before planning.
