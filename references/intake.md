# Intake and Profile Selection

## Six-field intake

Capture these before specification:

1. **Problem**: the costly or important problem to solve.
2. **Users**: primary users and important secondary actors.
3. **Core flow**: the shortest successful end-to-end journey.
4. **Must-have**: first-release capabilities that make the result useful.
5. **Excluded**: explicit non-goals for this release.
6. **Constraints**: platform, deadline, budget, compliance, integrations, data, or technology limits.

Use existing evidence first. Ask one question at a time only when the answer materially changes scope, architecture, safety, or acceptance. Mark non-critical unknowns as reversible assumptions with an owner and validation point.

## Profiles

| Profile | Use when | Required core artifacts |
|---|---|---|
| `lightweight` | Prototype, small internal tool, isolated fix | Brief, tasks, acceptance/test evidence, state |
| `standard` | Default product or feature work | Brief, PRD/spec, architecture, tasks, test plan, release record, state |
| `full` | Production data, payment, privacy, regulated use, complex migration or long-term team ownership | Standard set plus security, migration, operations, risk and rollback detail |

Recommend the smallest profile that controls the real risk. The user may override it. Escalate the profile if verified facts reveal higher risk.

For bounded `lightweight` validation, record the start date, end date and risky assumption. Reclassify before a second validation window or when real customer data, customer trial, external writes, paid/production integrations or customer-installable delivery enter scope. Repeated validation windows do not reset accumulated product scope.

## Intake exit gate

- The six fields are answered or explicitly assumed.
- Success is observable.
- First-release boundary and non-goals are explicit.
- High-risk unknowns have an owner and next validation action.
