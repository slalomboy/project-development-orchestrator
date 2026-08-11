# Quality and Release Truth

## Evidence Layers

| Layer | Evidence |
|---|---|
| Contract | fields, states, quantities, error codes, compatibility |
| Focused behavior | a test that failed for the intended reason, then passed |
| Regression | full suite, static checks, security and version consistency |
| Semantic/visual | human review of customer text, output depth, layout and workflow |
| Runtime | real shell/deployment, directories, ports, permissions, migration |
| Candidate | package version, architecture, signature status, checksum, package smoke |
| Installed | installed version/resources, launch, isolated core flow, rollback |
| Release | commit, immutable Tag, Release, assets, download and post-release smoke |

## Six Truth Surfaces

Always report separately:

1. source checkout;
2. candidate package;
3. installed application;
4. signing/notarization/platform trust;
5. Git commit, Tag, Release and assets;
6. customer-visible distribution and behavior.

Never infer one from another. A checksum is file integrity, not signing or successful installation. A Git push is not a Release. A screen observation is a lead, not release evidence.

These are parallel truth surfaces, not a ladder. A later surface such as Release cannot cover a missing installed-app, signing, or customer-distribution surface.

Minimum installed-app evidence is: actual install/upgrade completion, installed version and architecture, first launch, core isolated flow, quit/relaunch, data location and rollback result. Unpacking, mounting, package smoke, Finder visibility, or an installer prompt is candidate evidence only.

Minimum package smoke is: archive/package integrity, payload and install target, package version and architecture, signature status, required-resource presence, sensitive/debug-resource audit, and an unpacked/package-contained health or core-flow check when technically possible. It never claims system installation.

“Applicable” may be waived only by the authority accepted by `project-development-orchestrator`, with the excluded surface, reason, risk and highest remaining state recorded. Difficulty, missing equipment or deadline does not turn a required surface into not applicable. Missing required `full`-profile installation, platform-trust, or customer-distribution evidence always downgrades the overall conclusion; authority may accept the risk but cannot convert missing evidence into a pass.

## Version and Asset Gate

For each version, align version sources, customer-visible version, lockfiles, changelog, build metadata, commit, Tag, release notes, platform assets, checksums, compatibility and known issues. Do not alter a released version in place.

When the product produces installable/deployable artifacts, designate one canonical update bundle containing the manifest, source commit/Tag, notes, platform artifacts or explicit missing statuses, checksums, verification, compatibility and rollback.

Treat “GitHub sync” as separate permissions and results for source push, Tag, Release creation, asset upload and repository visibility. Do not infer one from the phrase alone when the requested action or risk differs.

Unsigned or ad-hoc-signed assets may be retained as local or explicit prerelease candidates only when the project policy names that channel and the accepted authority approves the risk. They cannot satisfy a formal signed-delivery gate; disclose platform warnings and the rollback path.

## Completion Language

Use only the highest proven state:

- plan only;
- source candidate verified;
- local package candidate verified;
- installed application verified;
- release published and rechecked;
- customer distribution verified.

Report a status for each of the six truth surfaces first, then one overall conclusion equal to the weakest required surface. List missing gates immediately after it. Test counts, package names, Finder views, or installer prompts never upgrade the state by themselves.

Minimum customer-distribution evidence is a remote download from the intended surface, checksum/package identity, install, launch, displayed version and isolated core flow. If customer-side execution is unavailable, report distribution unverified rather than using the customer as the first install test.
