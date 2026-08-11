# UI and Page Design Gate

## Decision

| Situation | Required design depth |
|---|---|
| Backend/CLI only | No UI gate |
| `lightweight` validation prototype | One lightweight visual brief and reusable tokens; record design debt |
| Small scoped edit with selected existing style | Audit the affected flow; preserve surrounding system |
| New product UI or broad redesign | Full gate below; no UI implementation before an accepted visual target is recorded |

“Today”, “make it premium”, “use your judgment”, “skip mockups”, existing code, or a working page do not waive the product-grade gate. If speed is essential, reduce the number of screens in the slice; do not make visual decisions silently in production code.

A broad redesign changes two or more of navigation/IA, global layout, design tokens, shared components, or several core pages. Renaming it a prototype or splitting the commits does not reduce the gate.

## Full Gate

### 1. Product and Flow Brief

Define first user, job, start state, completion state, core action, frequency, risk, desktop/mobile constraints, content density, brand assets, accessibility needs, and intended emotion.

### 2. Information Architecture

Produce:

- navigation groups and route map;
- primary workflow and alternate/error paths;
- page inventory with owner and priority;
- shared regions and cross-page actions;
- content hierarchy for each core page.

Do not design screens independently from the workflow.

### 3. Page-State Matrix

For every core page define applicable states:

| State | Questions |
|---|---|
| first-use/empty | What teaches the next action? |
| populated | What is primary, secondary, and scannable? |
| loading/long-running | Is progress honest; can the user leave or cancel? |
| partial | What succeeded, failed, and remains? |
| validation/error | Is the cause and recovery action specific? |
| permission/locked | What is unavailable and how is access restored? |
| success | What changed and what is next? |
| historical/stale | Is freshness and regeneration clear? |

For long-running work, also show which operation owns progress, what remains usable, whether results are partial, and whether retry will repeat completed or paid units. UI disabled state must reflect the operation contract rather than a blanket page lock.

### 4. Visual Target

Translate adjectives such as “premium” into observable choices: density, spacing rhythm, typography scale, color role, surface hierarchy, border/shadow use, icon style, motion, and data emphasis.

- New UI/redesign without a selected source: use Product Design context + ideation and show exactly three materially different directions. The user selects one.
- Existing screenshot/Figma/mock/reference: use it only if it is current enough for the requested scope and the user accepts it as the target; record source, acceptance and allowed deviations.
- Existing-flow audit: capture the current flow in this run and tie findings to accepted screenshots.

The three directions must differ on at least four of these axes: information density, layout/navigation model, typography, surface hierarchy, color strategy, data emphasis, component shape, or motion. Three color swaps are one direction. Record the user's explicit selection and the selected asset/version before implementation.

### 5. Design Contract

Freeze before implementation:

- layout grid, content widths, sidebar/header behavior;
- spacing, radius, typography, color and elevation tokens;
- component states and action hierarchy;
- table/form/card/modal/notification rules;
- responsive breakpoints or desktop minimum width;
- light/dark behavior when applicable;
- focus, contrast, hit target and keyboard expectations;
- motion purpose and reduced-motion behavior.

### 6. Implementation and QA

Implement shared layout/tokens/components before page exceptions. Then verify:

1. selected target versus rendered output;
2. full workflow, not isolated hero screens;
3. representative long text, empty data, errors and partial success;
4. regular, narrow and minimum supported sizes;
5. light/dark themes when supported;
6. keyboard focus, contrast, click targets and zoom;
7. browser prototype and real desktop shell separately;
8. installed application when the delivery target is desktop.

## Acceptance Record

Save the brief, selected target, state matrix, accepted screenshots, deviations, known gaps, and recheck scope. Structural QA does not replace human visual or language review.

Core pages are every page required by the selected vertical slice; applicable states come from its contract and observed flow, not convenience. The acceptance record maps each core page/state/size/theme to a screenshot or named blocker and records source/commit, app version, environment and capture time. A vague approval such as “looks fine” selects a target only when the exact direction and asset are visible in the same decision record.

## Red Flags

- Coding while deciding the visual direction
- “Premium” with no observable definition
- Reviewing only the dashboard
- Happy-path screenshots only
- Browser screenshot used as desktop-app proof
- Component consistency claimed without state coverage
- UI polish hiding a broken workflow or contract
