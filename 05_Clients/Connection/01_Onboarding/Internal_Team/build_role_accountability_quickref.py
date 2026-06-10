# -*- coding: utf-8 -*-
"""Build: Connection - Role & Accountability Quick-Reference (INTERNAL).
Built via EcsDocument. Internal Use Only footer (default). One section per role."""
import sys, os
REPO = "/sessions/eager-epic-davinci/mnt/everforth-ecs-practice"
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta
LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
OUT = os.path.join(REPO, "05_Clients", "Connection", "01_Onboarding", "Internal_Team",
                   "Connection_Role_and_Accountability_QuickRef.docx")

doc = EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL - ROLE QUICK-REFERENCE",
    title="Connection Engagement\nRole & Accountability Quick-Reference",
    subtitle="What you own, what you read, and when you are heaviest",
    org="ECS Federal - ServiceNow Practice",
    audience="ECS delivery team - EM, Solution Architect, Process Consultant, Technical Consultant(s), Practice Lead",
    companion_to="Team Onboarding & Vision - Engagement Delivery Guidelines - ONBOARDING_MAP",
    doc_id="INT-CONN-ROLE-01", version="1.0", status="Draft",
    running_header_label="Internal - Connection Role Quick-Reference",
), logo_path=LOGO)

doc.add_cover_page()
doc.page_break()

doc.h1("How to Use This Quick-Reference", numbered=False)
doc.para(
    "Find your role, read your one section, and you know what you own, what to read before Sprint 0, what to pull "
    "just-in-time, and which sprints you are heaviest in. The decision-rights table below ends \"who owns this?\" "
    "debates before they start. Curate, don't copy - read your path, reference the rest.")

doc.h1("Decision Rights at a Glance", numbered=True)
doc.table(headers=["Role", "Owns the decision on"], rows=[
    ["Engagement Manager (EM)", "Customer relationship, scope/budget, escalation; chairs the Customization Council; PCR authority."],
    ["Solution Architect (SA)", "Architecture & CSDM; OOTB vs customization (Rule of Three pass/fail); technical sign-off; code/config review."],
    ["Process Consultant (PC)", "Workshop facilitation; requirements-to-stories; sprint cadence; story-level Definition of Done."],
    ["Technical Consultant(s) (TC)", "Configuration, integration builds, data loads, story-level test."],
    ["Practice Lead (PM)", "Trust-but-verify oversight; the technical-path key in the two-key decision; escalation authority."],
])

doc.h1("Engagement Manager (EM)", numbered=True)
doc.para("You own the customer relationship and the engagement's health. You chair the Customization Council and hold PCR authority.")
doc.bullet("Core reading: OOTB Delivery Playbook (Sections 1 and 4), Internal Governance Operating Guide, SOW v2.0.")
doc.bullet("Just-in-time: per-sprint facilitator guides; trust-but-verify metrics; lessons learned.")
doc.bullet("Heaviest: Sprint 0 (setup, decision rights, dependencies) and every governance checkpoint thereafter.")
doc.bullet("Your check: weekly health report to practice management by Friday COB; Yellow/Red triggers a Monday 1:1.")

doc.h1("Solution Architect (SA)", numbered=True)
doc.para("You own the architecture and the OOTB-first call. You write the impact assessment for every deviation before it reaches a decision.")
doc.bullet("Core reading: OOTB Delivery Playbook (Sections 2 and 3), Adopt-vs-Reengineer cheatsheets, the in-scope Accelerator Pack blueprints.")
doc.bullet("Just-in-time: discipline how-to guides; CMDB/CSDM and integration packs as each sprint requires.")
doc.bullet("Heaviest: Stage 1 (CSDM data model, greenfield) and the ITSM/Change design workshops in Stages 1-2.")
doc.bullet("Your check: every customization carries a completed impact assessment; nothing reaches the Council without one.")

doc.h1("Process Consultant (PC)", numbered=True)
doc.para("You run the workshops where the OOTB discipline is won or lost, and you turn requirements into signed-off stories.")
doc.bullet("Core reading: Decision Topic Guides and Workshop Pre-Reads for the in-scope processes.")
doc.bullet("Just-in-time: per-sprint customer briefs; UAT test packs.")
doc.bullet("Heaviest: the workshop-dense build sprints (ITSM Core, Catalog, Employee Experience) across Stages 1-2.")
doc.bullet("Your check: each workshop ends with a signed-off story, not a list of \"things to think about.\"")

doc.h1("Technical Consultant(s) (TC)", numbered=True)
doc.para("You build. Configuration, integrations, and data - the standard way unless a deviation has cleared the two-key decision.")
doc.bullet("Core reading: Sprint 0 setup materials and the Accelerator Packs for in-scope modules.")
doc.bullet("Just-in-time: discipline how-to guides; demo scripts; sprint workbooks.")
doc.bullet("Heaviest: the build sprints in Stage 2 (ITSM Core, Change/CAB, Employee Center) and Stage 3 (HAM, analytics).")
doc.bullet("Your check: peer review complete and no P1 defects before a story is called done.")

doc.h1("Practice Lead (PM)", numbered=True)
doc.para("You provide independent oversight. You hold the technical-path key in the two-key decision and the escalation authority.")
doc.bullet("Core reading: trust-but-verify metrics and thresholds; the two-key model and SLAs; escalation triggers.")
doc.bullet("Just-in-time: weekly health reports; impact assessments awaiting the second key.")
doc.bullet("Heaviest: weekly at health-report review; on-demand whenever a deviation needs the technical-path key (48-hour SLA).")
doc.bullet("Your check: no customization is built on business need alone - the technical path is independently approved.")

doc.callout("Roles are confirmed and named during Sprint 0 and recorded in ENGAGEMENT_BRIEF.md. Update the bracketed names there as the team is staffed.")

doc.save(OUT)
print("Saved:", OUT)
