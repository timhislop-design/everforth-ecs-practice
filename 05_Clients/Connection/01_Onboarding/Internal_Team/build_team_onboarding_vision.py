# -*- coding: utf-8 -*-
"""Build: Connection - ECS Team Onboarding & Vision Guide (INTERNAL).
Built via EcsDocument. Internal Use Only footer (default). Internal candid tone."""
import sys, os
REPO = "/sessions/eager-epic-davinci/mnt/everforth-ecs-practice"
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta
LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
OUT = os.path.join(REPO, "05_Clients", "Connection", "01_Onboarding", "Internal_Team",
                   "Connection_Team_Onboarding_and_Vision.docx")

doc = EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL - TEAM ONBOARDING",
    title="Connection Engagement\nTeam Onboarding & Vision",
    subtitle="How we deliver Connection - the vision, the discipline, and your part in it",
    org="ECS Federal - ServiceNow Practice",
    audience="ECS delivery team - EM, Solution Architect, Process Consultant, Technical Consultant(s), Practice Lead",
    companion_to="OOTB Delivery Playbook - Engagement Delivery Guidelines - Role & Accountability Quick-Reference",
    doc_id="INT-CONN-ONB-01", version="1.0", status="Draft",
    running_header_label="Internal - Connection Team Onboarding",
), logo_path=LOGO)

doc.add_cover_page()
doc.page_break()

doc.h1("How to Use This Guide", numbered=False)
doc.para(
    "This is the first thing every ECS consultant reads when joining the Connection engagement. It sets the vision, "
    "explains the discipline we deliver by, and points you to exactly what your role needs - no more, no less. It is "
    "deliberately short. Read it once, then use the Engagement Delivery Guidelines for the operating rules and the "
    "Role & Accountability Quick-Reference for your specific reading path.")
doc.callout("Connection is our first engagement under this model. How we deliver it sets the pattern - and the proof - for every engagement that follows.")

doc.h1("The Vision - Why This Matters", numbered=True)
doc.para(
    "Connection is a ServiceNow reimplementation, but the real work is changing how a customer relates to their "
    "platform: out of a domain-separated, heavily customized instance and onto a clean, OOTB-aligned, AI-ready "
    "foundation. We call the theme “Modernizing the Core.” We stand up proven baseline capability first, and "
    "anything that deviates is captured and managed - not lost, and not quietly built.")
doc.h2("Discipline is what makes this viable")
doc.para(
    "OOTB-first is not a slogan; it is an economic model. Without the discipline, an OOTB engagement quietly collapses "
    "into a custom-build engagement at the same price - which is how practices lose money on this model. With the "
    "discipline, each engagement compounds into the next: reusable artifacts, shared decision patterns, and customers "
    "who have experienced the approach and refer more like it. Every consultant on Connection is a steward of that "
    "discipline.")
doc.h2("What we are proving")
doc.para(
    "Because Connection is the first engagement, we are proving the model works end to end: that the team can absorb "
    "the approach quickly, that the client stays aligned without being overwhelmed, and that leadership can see "
    "engagement health early through simple checks. Deliver Connection well and the next engagement starts easier.")

doc.h1("The Connection Engagement at a Glance", numbered=True)
doc.para("The authoritative source is SOW v2.0 (the Project Charter). The essentials:")
doc.table(headers=["Item", "Detail"], rows=[
    ["Client", "Connection (PC Connection)"],
    ["What", "18-week Phase 1 OOTB reimplementation - exit domain separation; modern, AI-ready core"],
    ["Phase 1 scope", "ITSM Core, Service Catalog, Employee Center (VA, AI Search, KM), CMDB/CSDM, HAM foundations, integrations"],
    ["Cadence", "Two-week sprints - Sprints 0-8 across 4 stages; Go-Live Week 16; Hypercare Weeks 17-18"],
    ["Success metrics", "MTTR, SLA attainment, change success rate - tracked in Platform Analytics from day one"],
])

doc.h1("The OOTB-First Discipline", numbered=True)
doc.para(
    "Every in-scope build begins by demonstrating standard ServiceNow. Customization is the exception, never the "
    "default. The discipline is enforced where it actually lives: in the workshop, in the moment a process owner with "
    "ten years of legacy customization decides whether to accept the OOTB pattern. Done well, a workshop ends with a "
    "signed-off user story headed straight to the sprint. Done badly, it ends with a list of “things to think "
    "about” that return as customization requests two weeks later.")
doc.callout("The Rule of Three: if a requirement is met by (1) Configuration, (2) UI Policy, or (3) Flow Designer, build it. If not, it is a customization - and it goes through the deviation path before any work starts. The Engagement Delivery Guidelines cover the mechanics.")

doc.h1("Curate, Don't Copy", numbered=True)
doc.para(
    "The OOTB practice library (folders 00-03) is comprehensive because it is the whole body of practice knowledge. "
    "Connection uses a curated subset of it - distilled by role for the team, and right-sized for the client. Do not "
    "dump the library on anyone. The onboarding map (01_Onboarding/ONBOARDING_MAP.md) defines what each role pulls and "
    "what the client sees and when. When in doubt, give people the one thing they need for the moment in front of them.")

doc.h1("Your Reading Path by Role", numbered=True)
doc.para(
    "Each role has a short Core path to read before Sprint 0 and a Just-in-Time set pulled per sprint. The full detail, "
    "including what you own and your heaviest sprints, is in the Role & Accountability Quick-Reference. In summary:")
doc.bullet("Engagement Manager - Delivery Playbook (setup + customer mgmt), Governance Operating Guide, the SOW.")
doc.bullet("Solution Architect - Delivery Playbook, Adopt-vs-Reengineer guidance, the relevant Accelerator Pack blueprints.")
doc.bullet("Process Consultant - Decision Topic Guides and Workshop Pre-Reads for in-scope processes.")
doc.bullet("Technical Consultant(s) - Sprint 0 setup and the Accelerator Packs for in-scope modules.")
doc.bullet("Practice Lead - trust-but-verify metrics, the two-key model, escalation triggers.")

doc.h1("How We Stay Honest", numbered=True)
doc.para(
    "Engagement health is visible from outside the engagement so leadership can support without micromanaging. Three "
    "simple mechanisms do the work: a weekly health report (velocity, customization count, dependency slips), the "
    "Customization Council that gates every deviation, and the Governance Triage Log that records every decision in the "
    "open. Your job on the team is to surface issues early - most engagements that fail do so because a hard "
    "conversation was avoided or had too late, not because of technical execution.")
doc.callout("If you are ever unsure whether something is OOTB or a deviation, stop and raise it. A 30-second question in standup beats a customization discovered at UAT.")

doc.save(OUT)
print("Saved:", OUT)
