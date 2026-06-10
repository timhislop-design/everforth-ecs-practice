# -*- coding: utf-8 -*-
"""Build: Connection - Engagement Delivery Guidelines (INTERNAL).
Built via EcsDocument. Internal Use Only footer (default). The operating rules for Connection."""
import sys, os
REPO = "/sessions/eager-epic-davinci/mnt/everforth-ecs-practice"
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta
LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
OUT = os.path.join(REPO, "05_Clients", "Connection", "01_Onboarding", "Internal_Team",
                   "Connection_Engagement_Delivery_Guidelines.docx")

doc = EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL - DELIVERY GUIDELINES",
    title="Connection Engagement\nDelivery Guidelines",
    subtitle="How we operate on Connection - the discipline, the gates, and the conversations",
    org="ECS Federal - ServiceNow Practice",
    audience="ECS delivery team - EM, Solution Architect, Process Consultant, Technical Consultant(s), Practice Lead",
    companion_to="Team Onboarding & Vision - OOTB Delivery Playbook - Internal Governance Operating Guide - SOW v2.0",
    doc_id="INT-CONN-GDL-01", version="1.0", status="Draft",
    running_header_label="Internal - Connection Delivery Guidelines",
), logo_path=LOGO)

doc.add_cover_page()
doc.page_break()

doc.h1("How to Use This Document", numbered=False)
doc.para(
    "These are the operating rules for the Connection engagement - the practical mechanics behind the OOTB-first "
    "discipline. Read the Team Onboarding & Vision Guide first for the why; this document is the how. It is the "
    "engagement-specific companion to the OOTB Delivery Playbook and the Internal Governance Operating Guide; where "
    "this document and the SOW differ, the SOW (the Project Charter) governs.")

doc.h1("The OOTB-First Operating Model", numbered=True)
doc.para(
    "Default to OOTB. Every in-scope build begins with a demonstration of standard ServiceNow functionality. A delta "
    "from the baseline is acceptable only when it is (a) tied to a documented business outcome, (b) not achievable by "
    "configuring an OOTB capability, and (c) signed off through the two-key decision. We present the OOTB alternative "
    "first, every time - including to a Sponsor who asks for the legacy pattern.")
doc.callout("Frame outcomes, not features, with the customer: \"Your outcome is faster change cycle time; OOTB delivers it; the legacy seven-step workflow does not.\"")

doc.h1("The Rule of Three", numbered=True)
doc.para("Before anything is treated as a customization, it must fail all three tests. If a requirement can be met by any of these, it is a standard story - no Customization Request needed:")
doc.table(headers=["#", "Test", "If it fits"], rows=[
    ["1", "Configuration", "Build it as a standard story; straight to the sprint."],
    ["2", "UI Policy", "Build it as a standard story; straight to the sprint."],
    ["3", "Flow Designer (no-code)", "Build it as a standard story; straight to the sprint."],
])
doc.para("Only a requirement that fails all three is a customization, and customizations follow the deviation path below.", italic=True)

doc.h1("The Deviation Path", numbered=True)
doc.para(
    "When a requirement fails the Rule of Three, the Solution Architect drafts an impact assessment - business need, "
    "OOTB alternatives considered, scope and budget estimate, and upgrade impact - before any decision is made. The "
    "request then goes to the two-key decision: the Connection Sponsor approves the business need, and the ECS Practice "
    "Lead approves the technical path. Both keys are required.")
doc.h2("Service levels")
doc.bullet("Two-key decision within 48 hours of the impact assessment being published.")
doc.bullet("Total wall-clock time from surface to decision: 5 business days maximum.")
doc.bullet("If it is blocking active sprint work, the SA flags it urgent and the SLAs compress to 24 hours total.")

doc.h1("The Customization Council", numbered=True)
doc.para(
    "The Council gates every Customization Request to keep the discipline intact. No exceptions, no \"just this one,\" "
    "and no decisions in hallway conversations.")
doc.table(headers=["Aspect", "Rule"], rows=[
    ["Cadence", "Weekly, 30 minutes, Customization Requests only. If none are pending, the meeting is canceled."],
    ["Chair", "Engagement Manager. Solution Architect presents the impact assessment."],
    ["Decision cap", "Cumulative cap of 5 approved customizations across Phase 1."],
    ["At customization #6", "Triggers a PCR conversation: the customer descopes to compensate, accepts a PCR, or reverses recent approvals."],
    ["Logging", "Every request - approved, rejected, or deferred - is logged in the Governance Triage Log within 24 hours."],
])

doc.h1("Definition of Done", numbered=True)
doc.para("The SOW's Definition of Done is contractual. These operational gates are how the team enforces it on every story:")
doc.bullet("Acceptance criteria were approved by the Product Owner before build began, and all are met and validated at close.")
doc.bullet("Integration touchpoints exercised in sub-production (if the story touches integrations).")
doc.bullet("Peer code/config review complete; no P1 defects open against the story.")
doc.bullet("Any deviation logged in the Triage Log with its scope/budget/upgrade implications and PCR status.")

doc.h1("Trust-but-Verify - Engagement Health", numbered=True)
doc.para(
    "Health is reported weekly so problems surface early. The Engagement Manager sends the metrics to practice "
    "management every Friday by close of business. Yellow or Red status triggers a Monday 1:1 to plan the response.")
doc.table(headers=["Signal", "Watch for"], rows=[
    ["Sprint velocity", "3-sprint average vs. planned; sustained drop below 75% is a red flag."],
    ["Customization count", "Approaching the cap of 5; reaching 6 forces a PCR conversation."],
    ["Dependency slips", "Unchecked Sprint 0/1 readiness items; three or more slips is a red flag."],
])
doc.callout("Engagement is RED if any of: two or more red metrics; customization count >= 6 mid-Phase; three or more dependency slips; or velocity below 75% for three consecutive sprints.")

doc.h1("Working With the Client - Do's and Don'ts", numbered=True)
doc.para("The conversations decide engagement health more than the technical execution does. Hold the discipline with partnership, not preaching.")
doc.h2("Do")
doc.bullet("Demonstrate the OOTB pattern first, then discuss - end each workshop with a signed-off story, not a list of \"things to think about.\"")
doc.bullet("Capture every deviation request transparently in the Triage Log, even the ones you expect to reject.")
doc.bullet("Have the hard conversation early - a dependency slip or scope drift named in week 3 is cheap; named at UAT it is not.")
doc.bullet("Frame to the Sponsor in terms of their outcomes and the maintenance burden avoided.")
doc.h2("Don't")
doc.bullet("Don't accept a customization in the room - it goes to the Council, every time.")
doc.bullet("Don't let \"Internal Use Only\" material or candid internal framing reach the client.")
doc.bullet("Don't frame the customer's prior choices as wrong - we are modernizing the core, not litigating the past.")
doc.bullet("Don't silently absorb scope - log it, surface it, and let governance decide.")

doc.save(OUT)
print("Saved:", OUT)
