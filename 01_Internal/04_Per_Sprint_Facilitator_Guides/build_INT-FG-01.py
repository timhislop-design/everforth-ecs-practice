"""
Build INT-FG-01 — Sprint 1 Platform Foundation Facilitator Guide
Internal audience — operational, prescriptive.
Pairs with: 03_Shared/04_Sprint_Workbooks/01 Sprint 01 Platform - DRAFT.docx
Contains: workshop agenda, decision pre-fills, demo flow, common pitfalls, retro template.
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

OUT = os.path.join(HERE, "INT-FG-01_Sprint1_Platform_Facilitator_Guide_INTERNAL.docx")

doc = EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL · PER-SPRINT FACILITATOR GUIDE",
    title="Sprint 1 — Platform Foundation\nFacilitator Guide",
    subtitle="Workshop agenda, decision pre-fills, demo flow, common pitfalls, and retro template for Sprint 1 Platform Foundation",
    audience="ECS Lead Consultant, Solution Architect, Engagement Manager",
    companion_to="Sprint 1 Platform Workbook · INT-TBV-06 Sprint Demo Discipline Audit · Foundation Data Accelerator Pack (AP-01)",
    doc_id="INT-FG-01",
    version="1.0",
    status="Released",
    running_header_label="Internal · Sprint 1 Platform Foundation Facilitator Guide",
), logo_path=LOGO)

doc.add_cover_page()
doc.page_break()

# =============================================================================
# How to Use This Guide
# =============================================================================
doc.h1("How to Use This Guide", numbered=False)
doc.para(
    "This guide is for the ECS consultant or solution architect facilitating the Sprint 1 Platform "
    "Foundation workshops. Read it fully before the sprint starts. The sprint workbook "
    "(03_Shared/04_Sprint_Workbooks/01 Sprint 01 Platform - DRAFT.docx) is the customer-facing "
    "artifact; this guide is the consultant-facing playbook for running it."
)
doc.para(
    "Sprint 1 is the most consequential sprint in the engagement. The decisions made here — "
    "CSDM alignment, user and group structure, SLA framework, assignment model — cascade into "
    "every subsequent sprint. Getting Sprint 1 right compresses the rest of the engagement. "
    "Getting it wrong creates rework that never fully clears."
)
doc.callout(
    "Sprint 1 rule: no configuration without a decision. Every configuration choice in Sprint 1 "
    "has a named decision in the sprint workbook. If the customer has not made the decision, the "
    "configuration does not get built. Do not configure based on assumptions — park the item and "
    "schedule a follow-up decision before the next sprint demo."
)
doc.page_break()

# =============================================================================
# 1. Sprint Overview
# =============================================================================
doc.h1("Sprint Overview")
doc.table(
    headers=["Item", "Detail"],
    rows=[
        ["Sprint number", "Sprint 1 of 6 (Month 1, Week 3-4)"],
        ["Duration", "2 weeks"],
        ["Primary discipline", "Platform Foundation — instance configuration, users, groups, CSDM baseline, SLA framework, assignment model"],
        ["Sprint goal", "A fully configured platform baseline that every subsequent sprint builds on top of. Users loaded, groups created, CSDM taxonomy agreed, SLA framework in place, assignment rules drafted."],
        ["Customer participants required", "IT Director or CIO (decision authority), ITSM Process Owner, IT operations team lead, HR/AD representative (for user data), 2-3 process SMEs"],
        ["ECS participants", "Lead Consultant (facilitator), Solution Architect (platform config), Engagement Manager (governance and decision log)"],
        ["Key artifacts produced", "Sprint 1 Platform Workbook (completed), Foundation Data Accelerator Pack (AP-01) with real customer data, initial CSDM service taxonomy, SLA definition matrix, assignment rule baseline"],
        ["Sprint demo audience", "Same as workshop participants + IT leadership who did not attend workshops"],
        ["Dependency: blocks", "Sprint 2 (Catalog and Employee Center) cannot start without: user/group structure complete, CSDM taxonomy agreed, SLA framework drafted"],
    ],
    col_widths_in=[2.4, 7.0],
)
doc.page_break()

# =============================================================================
# 2. Workshop Agenda
# =============================================================================
doc.h1("Workshop Agenda")
doc.para(
    "Sprint 1 typically runs three workshops across the two-week sprint window. The agenda below "
    "is the recommended structure. Adjust timing based on customer availability, but do not "
    "compress the decision-making time — the workshops are where decisions get made, not where "
    "decisions get discussed."
)

doc.h2("Workshop 1 — Platform Architecture and User Structure (Half day, Week 1)")
doc.table(
    headers=["Time", "Topic", "Owner", "Decision required"],
    rows=[
        ["0:00-0:20", "Sprint 1 kickoff — scope, goals, working agreements", "ECS EM", "None"],
        ["0:20-0:50", "Instance architecture review — environments, MID Servers, integrations confirmed", "ECS SA", "Environment naming, MID Server host assignment"],
        ["0:50-1:30", "User data review — AD export validated, group structure proposed", "ECS Lead + customer HR/AD rep", "Group naming convention, group-to-assignment-group mapping"],
        ["1:30-2:00", "CSDM intro — service taxonomy concepts, demo of OOTB CSDM", "ECS Lead", "None (conceptual only — decisions in Workshop 2)"],
        ["2:00-2:15", "Wrap, open items, decision log review", "ECS EM", "None"],
    ],
    col_widths_in=[0.8, 3.8, 2.0, 2.76],
)

doc.h2("Workshop 2 — CSDM Taxonomy and SLA Framework (Half day, Week 1)")
doc.table(
    headers=["Time", "Topic", "Owner", "Decision required"],
    rows=[
        ["0:00-0:10", "Open items from Workshop 1", "ECS EM", "Close open items from W1 decision log"],
        ["0:10-1:00", "CSDM taxonomy workshop — Business Services, Technical Services, Applications", "ECS SA + customer process owner", "Top 15-20 Business Services named and described; Applications mapped to Technical Services"],
        ["1:00-1:40", "SLA framework — priority matrix, target times, business-hours calendar", "ECS Lead + customer IT Director", "Priority definitions (P1-P4), response and resolution targets, business hours definition"],
        ["1:40-2:00", "SLA exceptions and contractual requirements", "ECS EM + customer", "List of contractual SLA obligations with written documentation"],
        ["2:00-2:15", "Wrap, open items, decision log review", "ECS EM", "None"],
    ],
    col_widths_in=[0.8, 3.8, 2.0, 2.76],
)

doc.h2("Workshop 3 — Assignment Model and Configuration Review (Half day, Week 2)")
doc.table(
    headers=["Time", "Topic", "Owner", "Decision required"],
    rows=[
        ["0:00-0:10", "Open items from Workshop 2", "ECS EM", "Close open items from W2 decision log"],
        ["0:10-0:50", "Assignment rules — group-to-category mapping, routing logic, escalation paths", "ECS Lead + customer team leads", "Assignment rule matrix (category x priority x group)"],
        ["0:50-1:20", "Configuration review — walk through what has been built in the instance so far", "ECS SA", "Customer confirms or flags each configuration item"],
        ["1:20-1:50", "Foundation Data Accelerator Pack walkthrough — customer completes remaining workbook tabs", "ECS Lead", "Workbook tabs signed off or flagged for follow-up"],
        ["1:50-2:00", "Sprint demo preview and retro prep", "ECS EM", "None"],
    ],
    col_widths_in=[0.8, 3.8, 2.0, 2.76],
)
doc.page_break()

# =============================================================================
# 3. Decision Pre-Fills — ECS Recommendations
# =============================================================================
doc.h1("Decision Pre-Fills — ECS Recommendations")
doc.para(
    "These are the decisions that come up in every Sprint 1. The ECS recommendation column is "
    "what you should propose in the workshop. If the customer pushes back, use the rationale. "
    "If they override the recommendation, document it in the decision log with their reason."
)

doc.table(
    headers=["Decision", "ECS Recommendation", "Rationale", "Common pushback"],
    rows=[
        [
            "Number of assignment groups",
            "Start with functional teams (Service Desk, Desktop Support, Network, Security, App Support). Do not mirror org chart.",
            "Assignment groups should reflect how work flows, not how the org is structured. Org charts change; workflows are more stable.",
            "'We need a group for every team.' Counter: groups can always be added; they are almost never successfully removed once they are created."
        ],
        [
            "CSDM service taxonomy depth",
            "Two levels: Business Service > Technical Service. No third level in Sprint 1.",
            "Third-level taxonomy in Sprint 1 creates scope creep and delays. Add depth in Sprint 4 (CSDM sprint) once the team has seen OOTB CSDM operate.",
            "'Our services are complex and need three levels.' Counter: agree — but Sprint 1 is not the sprint to model that complexity. Get the first two levels right first."
        ],
        [
            "SLA priority tiers",
            "Four tiers: P1 (Critical), P2 (High), P3 (Medium), P4 (Low). Do not add P5 or sub-tiers.",
            "Four tiers is the OOTB default and covers the vast majority of customer SLA requirements. Sub-tiers multiply SLA definitions without adding operational value.",
            "'We need P1A and P1B for different critical types.' Counter: use impact/urgency matrix to differentiate within P1 rather than adding tiers."
        ],
        [
            "Business hours definition",
            "One standard business hours calendar to start (e.g., Mon-Fri 8am-6pm customer local time). Add shift schedules in Sprint 3 if needed.",
            "Multiple business hours calendars in Sprint 1 create SLA complexity before the team understands how the SLA engine works.",
            "'We have 24/7 operations.' Counter: 24/7 SLAs are a simple OOTB schedule — configure it, but keep it as a second schedule, not a replacement."
        ],
        [
            "User import method",
            "ServiceNow LDAP/AD integration via MID Server. Import users directly from AD, not from a spreadsheet export.",
            "Spreadsheet imports require manual refresh. AD integration is self-maintaining and is the OOTB best practice for user management.",
            "'Our AD is messy and we are not ready to connect it.' Counter: connect AD in read-only mode first; clean it up in parallel. A messy AD is better than manual spreadsheet management."
        ],
    ],
    col_widths_in=[1.8, 2.4, 2.4, 2.76],
)
doc.page_break()

# =============================================================================
# 4. Demo Flow — Sprint 1 Platform Foundation
# =============================================================================
doc.h1("Demo Flow — Sprint 1 Sprint Demo")
doc.para(
    "The Sprint 1 demo shows the platform foundation in operation — not the full ITSM workflow "
    "(that is Sprint 1 Incident, a separate workbook). The platform demo proves to the customer "
    "that their data is in the system and the structural decisions they made are reflected correctly."
)

doc.h2("What to show (10-12 minutes)")
doc.bullet("User list: open the user list and filter to the customer's domain. Show that AD import populated real names, emails, departments, locations. 'Your people are in ServiceNow.'")
doc.bullet("Group structure: open the assignment groups list. Show the groups defined in Workshop 1. Show one group membership. 'Your team structure is in ServiceNow.'")
doc.bullet("CSDM service map: open the service taxonomy. Show the Business Services and their Technical Service children. 'Your service catalog backbone is in ServiceNow.'")
doc.bullet("SLA definition: open one SLA definition (P2 incident). Show response target, resolution target, business hours calendar, escalation notification. 'Your SLA commitments are configured.'")
doc.bullet("Assignment rule: open one assignment rule. Show the conditions (category + priority) and the target group. 'Incidents will route automatically.'")

doc.h2("What NOT to show in the Sprint 1 platform demo")
doc.bullet("Incident creation or workflow — save that for the Sprint 1 Incident demo")
doc.bullet("Catalog items — save for Sprint 2")
doc.bullet("Virtual Agent — save for Sprint 3")
doc.para("The platform demo is structural, not operational. Keep it short and anchored to the decisions the customer made.")

doc.h2("Sprint Demo Discipline Audit (INT-TBV-06)")
doc.para(
    "After the demo, complete the Sprint Demo Discipline Audit (INT-TBV-06). Score the demo "
    "against the C-1/C-2/C-3 configuration discipline criteria and the L-1/L-2/L-3 language "
    "discipline criteria. Submit the completed audit to the Delivery Manager within 24 hours "
    "of the demo."
)
doc.page_break()

# =============================================================================
# 5. Common Pitfalls
# =============================================================================
doc.h1("Common Pitfalls — Sprint 1")
doc.table(
    headers=["Pitfall", "How it shows up", "How to prevent it"],
    rows=[
        [
            "User data is not ready",
            "Customer shows up to Workshop 1 without an AD export or with a stale spreadsheet from 6 months ago. Sprint 1 stalls waiting for user data.",
            "Send the Foundation Data Accelerator Pack (AP-01) workbooks to the customer two weeks before Sprint 1 starts. Confirm receipt and completion in the Sprint 0 kickoff. Block Workshop 1 from starting until the user data is validated."
        ],
        [
            "CSDM taxonomy becomes a philosophy debate",
            "The CSDM workshop turns into a 3-hour discussion about what a 'service' is. No decisions are made. Workshop 2 needs to be rescheduled.",
            "Time-box the taxonomy debate to 30 minutes. Come in with a pre-filled starting point based on common IT services for the customer's industry. 'Here is where customers like you typically start — let's adjust from here' is faster than starting from a blank page."
        ],
        [
            "Too many groups created in Workshop 1",
            "Customer insists on a group for every team and sub-team. You leave Workshop 1 with 40 assignment groups.",
            "Present the ECS recommended group list before Workshop 1 opens. Anchor to functional workflows, not org structure. If they insist on more than 20 groups, flag it in the Customization Variance Tracker (INT-TBV-03) and note the maintenance overhead."
        ],
        [
            "SLA targets set to aspirational rather than achievable levels",
            "Customer sets P2 resolution to 2 hours. Current system data shows P2 resolution averaging 18 hours. The team will breach the SLA on Day 1.",
            "Pull SLA compliance data from the current system in Sprint 0. Present the data in Workshop 2. 'Your current P2 resolution average is 18 hours. Setting the target at 2 hours means you will breach every day. Let us set a realistic target and build toward the aspirational one.'"
        ],
        [
            "Decision log is not maintained during workshops",
            "Decisions are made verbally in the room. By Workshop 2, no one agrees on what was decided in Workshop 1. Rework ensues.",
            "The Engagement Manager owns the decision log. Every decision gets written in the log before the room moves to the next topic. Read the decision log back at the end of each workshop. Do not leave the room without agreement on what was decided."
        ],
    ],
    col_widths_in=[2.0, 3.4, 4.0],
)
doc.page_break()

# =============================================================================
# 6. Sprint Retro Template
# =============================================================================
doc.h1("Sprint 1 Retro Template")
doc.para(
    "Run the retro in the final 30 minutes of the last day of Sprint 1. Include: ECS team, "
    "customer project team, and the EM. Customer stakeholders who did not attend workshops are "
    "optional. Keep it to 30 minutes — this is a working retro, not a ceremony."
)

doc.h2("Retro structure (30 minutes)")
doc.table(
    headers=["Block", "Time", "Questions", "Owner"],
    rows=[
        ["What went well", "8 min", "What did we decide efficiently? What data was ready? What workshops ran smoothly?", "ECS Lead facilitates, all contribute"],
        ["What slowed us down", "8 min", "What decisions took longer than expected? What data was missing? What will we do differently in Sprint 2?", "ECS Lead facilitates, all contribute"],
        ["Open items and carry-forwards", "8 min", "What decisions are still open? What configuration is blocked? What needs to happen before Sprint 2 Workshop 1?", "ECS EM reads from decision log"],
        ["Sprint 2 preview", "4 min", "What is Sprint 2 scope? What data does the customer need to prepare?", "ECS Lead"],
        ["Action items", "2 min", "Each open item gets an owner and a due date", "ECS EM"],
    ],
    col_widths_in=[1.8, 0.7, 4.2, 2.66],
)

doc.h2("Retro output — record before leaving the room")
doc.bullet("Updated decision log (all open items assigned and dated)")
doc.bullet("Carry-forward items list (items that move to Sprint 2 backlog)")
doc.bullet("Sprint 1 health score (Delivery Manager completes INT-TBV-02 Engagement Health Dashboard within 48 hours)")
doc.bullet("Customer data prep list for Sprint 2 (sent to customer within 24 hours of retro)")

doc.callout(
    "The retro is not optional. Every sprint that skips a retro accumulates unresolved issues "
    "that surface as scope disputes in the final sprint. The 30-minute investment in Sprint 1 "
    "pays back in every subsequent sprint."
)

doc.save(OUT)
print(f"Saved: {OUT}")
