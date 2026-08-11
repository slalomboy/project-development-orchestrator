# Capability Routing

Inspect actual availability and select the minimum useful set. Specialist Skills execute domain work; this Skill owns lifecycle state, authorization, version, verification and handoff.

Superpowers is a conditional development-method layer, not a second control plane. When a Superpowers process Skill may apply, use [superpowers-routing.md](superpowers-routing.md) to select only the stage-appropriate method.

| Signal | Preferred route | Responsibility |
|---|---|---|
| Product discovery, UX research, audit | Product Design | Brief, research, alternatives and design QA |
| Editable UI screens, prototypes or design systems | Penpot MCP by default; Figma only for explicit Figma requests or existing Figma assets | Components, tokens, layouts, libraries and handoff |
| Zero-cost interactive UI validation or desktop/web behavior preview | Local HTML/CSS prototype plus Browser | Clickable states, responsive behavior and evidence |
| React, Next.js or Vercel | Relevant Vercel Skills | Architecture, implementation, performance and deployment |
| Database, auth, storage or Postgres | Supabase Skills when Supabase is present | Schema, RLS, performance and migrations |
| Repository, PR, CI or release | GitHub Skills | Checks, review and publishing workflow |
| Data, KPI, dashboard or analysis | Data Analytics | Evidence, metrics, charts and validation |
| Word, spreadsheet, slides or PDF | Documents, Spreadsheets, Presentations or PDF | Artifact production and visual verification |
| Internet research or current technical evidence | agent-reach | Source-backed retrieval |
| Images | imagegen | Raster generation or editing |
| Video or motion | Video, HyperFrames, Remotion, Seedance or Videocut | Production and verification |
| Payment | Region- and platform-appropriate payment Skill | Payment only after business and compliance context |

For UI work, apply [ui-design-gate.md](ui-design-gate.md). A bounded lightweight validation may use one recorded visual brief; new product-grade UI or a broad redesign without an accepted source requires exactly three materially distinct directions and an explicit target selection before implementation. Formalize approved directions in Penpot MCP by default, beginning with read-only inspection and small reversible writes. Use Figma only when the user explicitly requests it, an existing Figma file or library must remain the source of truth, or Penpot lacks a required capability. Use a local interactive prototype when an external design platform is unnecessary. Verify the full flow and state matrix in a browser or app against the selected source; desktop delivery also requires real-shell evidence.

Treat Penpot MCP credentials as global secrets. Never write the MCP URL, key, or query parameters into a project file, log, generated artifact, or public repository.

Global instructions may name unavailable capabilities. Check the current capability list every time, disclose missing dependencies, choose a safe fallback, and never claim an uninstalled Skill was used.
