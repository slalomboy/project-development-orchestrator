import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import test from 'node:test';

const root = path.resolve(import.meta.dirname, '..');
const required = ['README.md','README_EN.md','SKILL.md','VERSION','LICENSE-DECISION.md','LICENSE','repository-publication-manifest.yaml','repository-audit-report.md','docs/en/README.md','docs/en/quickstart.md','docs/en/usage.md','docs/en/limitations.md'];

test('required public candidate files exist', () => { for (const f of required) assert.ok(fs.existsSync(path.join(root, f)), f); });
test('version and bilingual facts are consistent', () => { const all = required.filter(f => fs.existsSync(path.join(root,f))).map(f => fs.readFileSync(path.join(root,f),'utf8')).join('\n'); assert.match(all, /0\.1\.0-alpha\.1/); assert.match(all, /zh-CN,en/); });
test('public package excludes sensitive and drifting references', () => { const files=[]; const walk=d=>fs.readdirSync(d,{withFileTypes:true}).forEach(e=>e.name==='tests'?null:e.isDirectory()?walk(path.join(d,e.name)):files.push(path.join(d,e.name))); walk(root); const all=files.map(f=>fs.readFileSync(f,'utf8')).join('\n'); const patterns=[new RegExp('/'+'Users'+'/'),new RegExp('/'+'home'+'/'),new RegExp('gh'+'p_[A-Za-z0-9]+'),new RegExp('github'+'_pat_'),new RegExp('BEGIN OPEN'+'SSH PRIVATE KEY'),new RegExp('blob'+'/main'),new RegExp('tree'+'/main'),new RegExp('Cook'+'ie:')]; for (const p of patterns) assert.doesNotMatch(all,p); });
