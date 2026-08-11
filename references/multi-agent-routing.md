# Multi-Agent Routing

## Operating Principle

Default to one primary agent. Use subagents only when delegation has a measurable advantage, authorization covers the task, work can be isolated, and available quota evidence supports the extra cost. Agent capacity is a ceiling, never a target.

The primary agent remains accountable for scope, integration, verification, versioning, records, release boundaries, and the final claim. A subagent report is candidate evidence, not completion evidence.

## Authorization

- Current-task authorization explicitly permits delegation for the named task.
- A user may grant standing authorization for future suitable project work. Standing authorization permits bounded delegation under this reference; it does not expand project scope, external-write authority, production access, release authority, destructive permissions, or permission to create another generation of agents.
- General implementation approval without current-task or standing authorization does not permit delegation.
- Record which authorization applies before dispatch.

## Eligibility Gate

Delegate only when every applicable answer is yes:

1. There are at least two meaningful work domains, or one specialist review whose expected value exceeds its coordination cost.
2. Each delegated task has a clear goal, inputs, scope, exclusions, output, acceptance criteria, and file ownership.
3. The domains have no unresolved sequential dependency or shared mutable state.
4. Delegation is likely to save material elapsed time, reduce a material risk, or add an independent verification perspective.
5. The primary agent can review and integrate every result within the remaining time and resource budget.

Do not delegate a small bounded task that the primary agent can finish faster than it can specify, dispatch, review, and integrate.

## Quota and Capacity Gate

Use only quota evidence actually exposed by the system, API, or session. Never estimate Token balance, monetary credit, rate limits, or remaining agent capacity from prose length or intuition.

Choose the smallest mode that produces a real benefit:

| Resource state | Mode |
|---|---|
| Quota constrained, rate-limited, or insufficient reserve | Primary agent only |
| quota is unknown | Conservative mode: primary agent only by default; at most one read-only or high-value specialist under standing authorization. Use two only when the current task explicitly requests multi-agent work and the domains are strongly independent |
| Quota evidence is sufficient | Use minimum useful delegation, normally one or two subagents, bounded by independent domains and free slots |
| Quota evidence is ample and current task explicitly requests broad parallelism | Up to the minimum of useful independent domains and live free slots; preserve capacity for integration or recovery |

Never fill every available slot merely because it exists. Reserve enough time and quota for primary-agent integration and fresh verification. If reliable quota data is unavailable, state that fact in the internal decision record and use the conservative row.

## Delegation Contract

Every subagent task must state:

- objective and expected value;
- allowed inputs and required context;
- scope and excluded work;
- read-only or write authority;
- exact file ownership or an explicit no-write rule;
- expected output and acceptance criteria;
- dependencies and shared resources;
- stop conditions and escalation path;
- prohibition on recursive delegation unless separately authorized.

Prefer read-only investigation, review, and evidence gathering in parallel. For writes, one file has one owner at a time. Shared manifests, lockfiles, changelogs, project state, release records, and integration files belong to the primary agent unless explicitly assigned to a single integration owner.

## Execution Modes

- **Inline:** primary agent performs all work.
- **Sequential delegation:** use when a specialist result is needed before the next task can start.
- **Parallel delegation:** use only for isolated domains with no shared mutable state.

Before parallel dispatch, identify file ownership, worktree or directory isolation, databases, ports, caches, generated outputs, accounts, and external systems. Any unresolved overlap means sequential execution or read-only delegation.

## Stop, Downgrade, and Integration

Immediately stop or downgrade delegation when quota becomes constrained, tasks overlap, a shared root cause appears, agents repeat work, evidence quality is poor, an agent exceeds scope, integration time threatens final verification, or shared resources become unstable.

After results return, the primary agent must:

1. review every result and actual file change;
2. reject unsupported claims and resolve contradictions;
3. check ownership and scope compliance;
4. run fresh integrated verification;
5. record material delegation, cost or quota uncertainty, evidence, and unresolved risks.

## Planning Record

For standard or full project work, record: authorization source, eligible domains, selected mode, quota evidence or unknown status, number of subagents, ownership map, expected benefit, stop conditions, integration owner, and final verification owner. For lightweight work, a concise commentary decision is sufficient.
