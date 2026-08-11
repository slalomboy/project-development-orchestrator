import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
const root = path.resolve(import.meta.dirname, '..');
const skill = fs.readFileSync(path.join(root, 'SKILL.md'), 'utf8');
assert.match(skill, /^---\nname: project-development-orchestrator\n/m);
assert.equal(fs.readFileSync(path.join(root, 'VERSION'), 'utf8').trim(), '0.1.0-alpha.1');
for (const f of ['README.md','README_EN.md','LICENSE','repository-publication-manifest.yaml','repository-audit-report.md']) assert.ok(fs.existsSync(path.join(root, f)), f);

console.log(JSON.stringify({status:'VALID',repository:'project-development-orchestrator',version:'0.1.0-alpha.1'}));
