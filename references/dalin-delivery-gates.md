# Lifecycle Gates

## Canonical Profile Application

Use only the orchestrator's canonical `lightweight`, `standard`, and `full` profile values in `project-state.json`.

| Canonical profile | Delivery use | Minimum finish line |
|---|---|---|
| `lightweight` | One user, one risky assumption, internal/demo validation | One vertical slice, local persistence, failure state, manual walkthrough; clearly labeled prototype |
| `standard` | Real customer trial or normal product work | Product-grade flow, state coverage, runtime/package and installed-app verification |
| `full` | Paid, public, production, regulated, complex migration, long-term ownership or multi-platform delivery | Signing/platform trust as applicable, platform matrix, immutable Tag, Release assets, rollback and post-release smoke |

A `lightweight` validation is time- and scope-bounded. Record its start date, end date and risky assumption in Current state. At the end or before a second validation window, reclassify the canonical profile; repeated windows do not reset accumulated product scope. Upgrade to `standard` before using real customer data, starting customer trial, writing to external systems, using paid/production integrations, or promising a customer-installable build. Use `full` when the verified risks match the intake definition. A desktop-named internal prototype must run its core flow in the real desktop shell. A local installable demo may remain `lightweight` only when it is not distributed to customers and candidate plus installed-app evidence are recorded.

## Thirteen Gates

| Gate | Required output | Exit evidence |
|---|---|---|
| 0 Project truth | mode, profile, repo/path/version/artifact/install/release facts | current evidence, not memory |
| 1 Customer problem | first user, scenario, pain, desired result | result stated without feature jargon |
| 2 Product boundary | included, excluded, promises, success | new requests can be classified |
| 3 Business loop | input → system → confirmation → output → execution → feedback | actor and handoff for every step |
| 4 Current contract | input, state, AI, output, API, version contracts | one trace from requirement to output |
| 5 Technical preflight | smallest architecture, costs, risks, downgrade | three main risks controlled |
| 6 Vertical slice | one user, one scenario, one result, one failure | stranger completes it |
| 7 Productization | states, progress, errors, recovery, history | failure is understandable and recoverable |
| 8 External capability | adapter, permission, cost, rate, idempotency, fallback | outage does not erase local result |
| 9 Runtime | desktop/deployment start, data dirs, migration, upgrade | real delivery shape completes core flow |
| 10 Quality | contract, focused, regression, runtime, semantic/visual evidence | all applicable layers pass freshly |
| 11 Candidate/install | versioned assets, backup, install, smoke, rollback | installed behavior matches candidate |
| 12 Release/recovery | commit, Tag, Release, assets, checksums, docs | version is retrievable and reproducible |
| 13 Feedback | evidence, root layer, change class, prevention asset | issue enters the correct gate |

## Iteration Loop

For every material change:

1. Capture expected, actual, environment, and evidence.
2. Classify requirement change, contract drift, defect, data, environment, or delivery-state mismatch.
3. Locate root layer and affected truth surfaces.
4. Rewrite objective, scope, exclusions, acceptance, version impact, authority, and rollback.
5. Make the behavior test fail first; implement the smallest complete fix.
6. Run focused, regression, safety, semantic/visual, runtime, candidate, and installed checks as applicable.
7. Update state, changelog/log, artifacts, blockers, and one next action.

## Vertical Slice Minimum

A slice includes real state transition, local persistence or the chosen durable store, one expected failure with recovery, re-entry/restart behavior, and a stranger walkthrough. Save the walkthrough script, environment, result, failure points and highest proven state.

If the product name or customer outcome presents AI output as primary value, AI quality is a core risk by default. Separate interaction-loop validation from AI-capability validation. A mock adapter may validate UI and contracts only; promotion to product requires an isolated set of real-call cases covering representative output quality, malformed/failed responses, latency and cost boundaries. Any exception must be explicit in the Current contract and label AI as placeholder rather than validated value.

The stranger walkthrough is performed by someone not involved in implementation, without live coaching. Record any hint required as a failure or usability gap.

## Long-Running Operation Contract

When operations are slow, paid, writing, or share mutable progress/results, the Current contract defines:

- conflict key and which operations are mutually exclusive;
- owner/operation ID and stale-result write protection;
- progress source, cancellation, timeout and restart behavior;
- success, failure and cancellation lock release;
- restoration of each control's original enabled/disabled state;
- partial-success persistence and failed-unit-only retry;
- idempotency and avoidance of repeat cost for completed units.

Lock only conflicting operations. Navigation, local-data viewing, history/results viewing and safe read-only diagnostics remain available by default. A global “disable the whole app” shortcut requires a specific safety reason and acceptance test.

## Current Authority Rule

Maintain one Current entry each for product definition, execution target, business/data/output contract, project state, acceptance, and release record. Mark old entries historical or superseded. Never ask a future agent to reconcile several equal “current” documents.

## Responsibility Rule

For every action label exactly one owner: system, operator, real-world executor, or external platform. Re-evaluate ownership when capabilities change.
