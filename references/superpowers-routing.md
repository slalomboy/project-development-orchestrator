# Superpowers Routing

## Authority and Boundary

Project Development Orchestrator remains the lifecycle control plane. It owns classification, authorization, state, version, records, verification, release and rollback. Superpowers supplies conditional development methods.

- Do not use `using-superpowers` as a second lifecycle control plane. Treat it as a Skill-discovery reminder only.
- Pure Q&A, explanation, translation, chat, one-off copy and read-only reporting stay outside the development workflow unless the user names a Skill.
- Invoke only the smallest stage-appropriate method; never load the full chain by default.
- User, global and project instructions override Superpowers defaults. Existing project documentation conventions override Superpowers default paths such as `docs/superpowers/`.
- The orchestrator owns approval gates. A Superpowers recommendation cannot authorize writes, dependencies, worktrees, subagents, deployment, publication or destructive actions.
- Direct execution does not create a separate Superpowers approval chain when requirements and scope are clear. Material cost, architecture, dependency, security, migration, release or permission decisions remain gated.
- Local commits follow project and user authorization. Push, pull request, publication, deployment and release remain separately gated actions.

## Stage Routing

| Signal | Use | Do not use when |
|---|---|---|
| Unsettled feature or material design choice | `brainstorming` | Direction is clear or work is read-only |
| Approved multi-step implementation | `writing-plans` | A sufficient plan exists or work is one bounded action |
| Testable feature, fix, refactor or behavior change | `test-driven-development` | User-approved exception for prototype, generated code or config-only change |
| Bug, failed test or unexpected behavior | `systematic-debugging` | No observed failure |
| Completion, fixed, passing or ready claim | `verification-before-completion` | Never skip; scale evidence to the claim |
| Feature work needs isolation | `using-git-worktrees` | Already isolated, unsuitable repo or user declines |
| Approved plan, sequential current-task execution | `executing-plans` | No approved plan |
| Authorized delegation of independent plan tasks | `subagent-driven-development` | No delegation approval or shared mutable state |
| Authorized parallel independent tasks | `dispatching-parallel-agents` | Sequential, overlapping or unauthorized work |
| Substantial change or merge candidate | `requesting-code-review` | No implementation |
| Actionable review feedback | `receiving-code-review` | No feedback |
| Verified real branch/worktree ready to integrate | `finishing-a-development-branch` | No branch/worktree or failing tests |
| Creating or changing a reusable Skill | `writing-skills` | Project-specific or one-off guidance |
| Conversation-start Skill discovery | `using-superpowers` | Never expose as a separate workflow |

## Delegation Guard

Do not spawn subagents merely because a Superpowers plan recommends it. Apply [multi-agent-routing.md](multi-agent-routing.md): require current-task or standing authorization, isolated ownership, a positive cost-benefit decision, and quota-aware minimum useful delegation. Default to inline execution when no valid delegation authorization or eligibility decision exists. General implementation approval does not imply delegation approval, and recursive delegation requires separate authorization.

## Artifact and Completion Rules

- Store artifacts where the project keeps durable truth; do not create a parallel tree solely for a Superpowers default.
- Record selected Superpowers methods, decisions, approvals, verification evidence and deviations in project state and configured project or global logs when they are material.
- Superpowers checks supplement, but do not replace, project acceptance criteria, built-artifact verification, version alignment, project state or configured global logs.
- If a Superpowers instruction conflicts with an authorization, privacy, safety, release or rollback boundary, follow the higher-priority boundary and record the deviation.
