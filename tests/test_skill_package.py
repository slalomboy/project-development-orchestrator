import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SkillPackageTests(unittest.TestCase):
    def read(self, relative):
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_required_package_files_exist(self):
        required = [
            "SKILL.md",
            "VERSION",
            "CHANGELOG.md",
            "agents/openai.yaml",
            "references/lifecycle.md",
            "references/intake.md",
            "references/artifact-contracts.md",
            "references/spec-management.md",
            "references/capability-routing.md",
            "references/superpowers-routing.md",
            "references/multi-agent-routing.md",
            "references/quality-gates.md",
            "references/dalin-delivery-gates.md",
            "references/ui-design-gate.md",
            "references/delivery-truth-gates.md",
            "references/failure-patterns.md",
            "assets/templates/project-state.json",
            "assets/templates/project-brief.md",
            "assets/templates/prd.md",
            "assets/templates/architecture.md",
            "assets/templates/tasks.md",
            "assets/templates/test-plan.md",
            "assets/templates/release-plan.md",
            "assets/templates/decision-record.md",
            "assets/templates/change-proposal.md",
            "assets/templates/new-project-delivery-brief.md",
            "assets/templates/ui-design-brief.md",
            "scripts/validate_project_state.py",
        ]
        missing = [path for path in required if not (ROOT / path).is_file()]
        self.assertEqual(missing, [])

    def test_skill_contains_control_plane_contract(self):
        skill = self.read("SKILL.md")
        for phrase in [
            "greenfield",
            "brownfield",
            "takeover",
            "lightweight",
            "standard",
            "full",
            "project-state.json",
            "explicit approval",
            "Completion Gate",
        ]:
            self.assertIn(phrase, skill)

    def test_references_cover_lifecycle_and_recovery(self):
        lifecycle = self.read("references/lifecycle.md")
        for stage in [
            "intake",
            "discovery",
            "specification",
            "design",
            "planning",
            "implementation",
            "verification",
            "release",
            "operate",
        ]:
            self.assertIn(stage, lifecycle)
        intake = self.read("references/intake.md")
        for field in ["Problem", "Users", "Core flow", "Must-have", "Excluded", "Constraints"]:
            self.assertIn(field, intake)
        specs = self.read("references/spec-management.md")
        self.assertIn("Current truth", specs)
        self.assertIn("Change proposal", specs)
        self.assertIn("Archive", specs)

    def test_templates_have_traceability_contracts(self):
        required_tokens = {
            "assets/templates/prd.md": ["REQ-", "AC-", "Excluded"],
            "assets/templates/architecture.md": ["ADR-", "REQ-", "Risk"],
            "assets/templates/tasks.md": ["TASK-", "REQ-", "TEST-"],
            "assets/templates/test-plan.md": ["TEST-", "AC-", "Evidence"],
            "assets/templates/release-plan.md": ["Version", "Verification", "Rollback"],
            "assets/templates/change-proposal.md": ["CHG-", "ADDED", "MODIFIED", "REMOVED"],
        }
        for path, tokens in required_tokens.items():
            content = self.read(path)
            for token in tokens:
                self.assertIn(token, content, f"{token} missing from {path}")

    def test_metadata_and_version(self):
        self.assertEqual(self.read("VERSION").strip(), "0.5.0-alpha.1")
        self.assertIn("## [0.5.0] - 2026-08-01", self.read("CHANGELOG.md"))
        skill = self.read("SKILL.md")
        self.assertRegex(skill, r"\A---\nname: project-development-orchestrator\n")
        metadata = self.read("agents/openai.yaml")
        self.assertIn("$project-development-orchestrator", metadata)
        self.assertIn('display_name: "项目开发总控"', metadata)

    def test_ui_routing_prefers_penpot_with_explicit_figma_fallback(self):
        routing = self.read("references/capability-routing.md")
        self.assertIn("Penpot MCP by default", routing)
        self.assertIn("Use Figma only when the user explicitly requests it", routing)
        self.assertIn("Local HTML/CSS prototype plus Browser", routing)
        self.assertIn("Treat Penpot MCP credentials as global secrets", routing)

    def test_dalin_delivery_and_ui_gates_are_integrated(self):
        skill = self.read("SKILL.md")
        for reference in ["dalin-delivery-gates.md", "ui-design-gate.md", "delivery-truth-gates.md"]:
            self.assertIn(reference, skill)
        ui = self.read("references/ui-design-gate.md")
        for phrase in ["exactly three", "Page-State Matrix", "accepted visual target", "real desktop shell"]:
            self.assertIn(phrase, ui)
        lifecycle = self.read("references/dalin-delivery-gates.md")
        for phrase in ["Long-Running Operation Contract", "failed-unit-only retry", "canonical `lightweight`"]:
            self.assertIn(phrase, lifecycle)
        delivery = self.read("references/delivery-truth-gates.md")
        for phrase in ["parallel truth surfaces", "Minimum installed-app evidence", "weakest required surface"]:
            self.assertIn(phrase, delivery)

    def test_superpowers_is_a_conditional_method_layer(self):
        routing = self.read("references/superpowers-routing.md")
        for phrase in [
            "Project Development Orchestrator remains the lifecycle control plane",
            "Do not use `using-superpowers` as a second lifecycle control plane",
            "Pure Q&A",
            "project documentation conventions override Superpowers default paths",
            "Do not spawn subagents merely because a Superpowers plan recommends it",
            "Default to inline execution",
            "Direct execution does not create a separate Superpowers approval chain",
            "Local commits follow project and user authorization",
            "Record selected Superpowers methods",
            "verification-before-completion",
        ]:
            self.assertIn(phrase, routing)

        for skill in [
            "using-superpowers",
            "brainstorming",
            "writing-plans",
            "test-driven-development",
            "systematic-debugging",
            "verification-before-completion",
            "using-git-worktrees",
            "subagent-driven-development",
            "dispatching-parallel-agents",
            "executing-plans",
            "requesting-code-review",
            "receiving-code-review",
            "finishing-a-development-branch",
            "writing-skills",
        ]:
            self.assertIn(skill, routing)

        capability_routing = self.read("references/capability-routing.md")
        self.assertIn("superpowers-routing.md", capability_routing)
        skill_body = self.read("SKILL.md")
        self.assertIn("superpowers-routing.md", skill_body)

    def test_multi_agent_routing_is_bounded_and_budget_aware(self):
        routing = self.read("references/multi-agent-routing.md")
        for phrase in [
            "Default to one primary agent",
            "standing authorization",
            "quota evidence",
            "quota is unknown",
            "minimum useful delegation",
            "shared mutable state",
            "file ownership",
            "stop or downgrade",
            "primary agent remains accountable",
        ]:
            self.assertIn(phrase, routing)

        skill = self.read("SKILL.md")
        self.assertIn("multi-agent-routing.md", skill)
        superpowers = self.read("references/superpowers-routing.md")
        self.assertIn("multi-agent-routing.md", superpowers)

    def test_state_template_is_valid_json(self):
        state = json.loads(self.read("assets/templates/project-state.json"))
        self.assertEqual(state["schema_version"], "1.0")
        self.assertEqual(state["profile"], "standard")

    def test_no_unresolved_placeholders_in_instructions(self):
        instruction_files = [ROOT / "SKILL.md", *sorted((ROOT / "references").glob("*.md"))]
        pattern = re.compile(r"\b(?:TBD|TODO|FIXME|XXX)\b")
        failures = [str(path.relative_to(ROOT)) for path in instruction_files if pattern.search(path.read_text(encoding="utf-8"))]
        self.assertEqual(failures, [])


if __name__ == "__main__":
    unittest.main()
