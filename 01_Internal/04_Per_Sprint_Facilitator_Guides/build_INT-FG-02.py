"""
Build INT-FG-02 — Sprint 1 Incident Management Facilitator Guide
Internal audience — operational, prescriptive.
Pairs with: 03_Shared/04_Sprint_Workbooks/02 Sprint 01 Incident - DRAFT.docx
Contains: sprint overview, workshop agendas, decision pre-fills, common pitfalls, retro template.
Companion to: INT-DS-01 (Incident Management Demo Script)
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

OUT = os.path.join(HERE, "INT-FG-02_Sprint1_Incident_Facilitator_Guide_INTERNAL.docx")

doc = EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL · PER-SPRINT FACILITATOR GUIDE",
    title="Sprint 1 — Incident Management\nFacilitator Guide",
    subtitle="Workshop agenda, decision pre-fills, OOTB defense language, common pitfalls, and retro template for Sprint 1 Incident Management",
    audience="ECS Lead Consultant, Solution Architect, Engagement Manager",
    companion_to="Sprint 1 Incident Workbook · INT-DS-01 Incident Management Demo Script · INT-TBV-06 Sprint Demo Discipline Audit",
    doc_id="INT-FG-02",
    version="1.0",
    status="Released",
    running_header_label="Internal · Sprint 1 Incident Management Facilitator Guide",
), logo_path=LOGO)

doc.add_cover_page()
doc.page_break()

# =============================================================================
# How to Use This Guide
# =============================================================================
doc.h1("How to Use This Guide", numbered=False)
doc.para(
    "This guide is for the ECS consultant or solution architect facilitating the Sprint 1 Incident "
    "Management workshops. Read it alongside the Sprint 1 Incident Workbook "
    "(03_Shared/04_Sprint_Workbooks/02 Sprint 01 Incident - DRAFT.docx), which is the customer-facing "
    "artifact. This guide is the internal playbook for running it — what to say, what to pre-fill, "
    "where the conversations get hard, and how to recover."
)
doc.para(
    "Incident Management is where every customer has opinions shaped by years of workarounds. "
    "Categories that evolved organically. States that were added to track edge cases. Routing rules "
    "that reflect org chart history, not service ownership. The facilitator's job is not to dismiss "
    "those opinions but to distinguish between what the customer actually needs and what they have "
    "always done because no one challenged it. ServiceNow OOTB Incident Management is capable enough "
    "to handle 95% of what the customer needs — the workshop is about surfacing which 5% is genuinely "
    "different and governing it through the Customization Council."
)
doc.callout(
    "The governing principle for Sprint 1 Incident: configure to the OOTB standard first, demonstrate "
    "it working, then consider exceptions. Customers who see OOTB Incident Management working correctly "
    "accept far more of it than customers who are asked to approve configuration decisions on a whiteboard."
)
doc.page_break()

# =============================================================================
# 1. Sprint Overview
# =============================================================================
doc.h1("Sprint Overview")
doc.table(
    headers=["Item", "Detail"],
    rows=[
        ["Sprint number", "Sprint 1 of 6 (Month 1, Week 3-4), concurrent with Platform Foundation (INT-FG-01)"],
        ["Duration", "2 weeks (workshops in Week 3; configuration in Week 3-4; demo in Week 4)"],
        ["Primary discipline", "Incident Management — category taxonomy, state lifecycle, priority matrix, assignment, SLA linkage, notifications, and Major Incident definition"],
        ["Sprint goal", "A configured Incident Management baseline that handles the customer's top 10 incident types correctly in the OOTB workflow, with a documented list of governed exceptions for the Customization Council."],
        ["Customer participants required", "ITSM Process Owner (decision authority for Incident), Service Desk Manager, 3-4 Tier 1/Tier 2 team leads (for routing and assignment validation), IT Director or delegate (for final sprint demo)"],
        ["ECS participants", "Lead Consultant (facilitator), Solution Architect (configuration), Engagement Manager (decision log and governance)"],
        ["Key artifacts produced", "Sprint 1 Incident Workbook (completed decisions), Incident category taxonomy (final), Priority matrix (agreed), Assignment rule baseline (tested), Notification template baseline, Major Incident definition, Governed exceptions log"],
        ["Sprint demo audience", "Service Desk Manager + IT Director + any stakeholders whose workflows were discussed during the sprint"],
        ["Dependency: blocks", "Problem Management (Sprint 3) cannot start without Incident category taxonomy finalized. Virtual Agent topic design (Sprint 5) requires confirmed Incident categories."],
    ],
    col_widths_in=[2.4, 7.0],
)
doc.page_break()

# =============================================================================
# 2. Workshop Agendas
# =============================================================================
doc.h1("Workshop Agendas")
doc.para(
    "Sprint 1 Incident Management runs two core workshops plus a follow-up validation session. "
    "All three are designed for 90-minute blocks. The third session (Assignment and Notification "
    "Validation) can be done async if all participants can confirm the configuration in the live instance."
)

doc.h2("Workshop 1 — Category Taxonomy and State Lifecycle (90 min)")
doc.table(
    headers=["Time", "Agenda Item", "Facilitation Notes"],
    rows=[
        ["0:00–0:10", "Welcome and context (ECS)", "Frame the session: 'Today we are locking the Incident category taxonomy and the state lifecycle. These two decisions affect every Incident record from day one. Everything else in Incident Management is adjustable after go-live; these two are the hardest to change.'"],
        ["0:10–0:30", "Current state review: what categories exist today?", "Ask the Service Desk Manager to share the current category list. Do not judge — write everything on the board. Then ask: 'Which of these categories do your analysts actually use, and which exist because someone added them three years ago and no one removed them?' This is the pruning conversation."],
        ["0:30–0:55", "OOTB category structure recommendation", "Present the ECS-recommended category taxonomy (pre-filled in the Decision Pre-Fills section below). Walk through each category and ask: 'Does this cover your needs? What is missing?' Do not add categories during the session — park additions for the Governed Exceptions log."],
        ["0:55–1:10", "State lifecycle walkthrough", "Walk through the OOTB Incident state lifecycle: New → In Progress → On Hold → Resolved → Closed. Ask: 'Is there a state your team uses today that is not here?' Common additions: 'Pending Customer', 'Pending Vendor' — both map to On Hold with a Hold Reason field (OOTB). Demonstrate this in the live instance."],
        ["1:10–1:25", "Decision record", "Confirm the decisions made. ECS documents in the Decision Log. Any unresolved items go to the Parking Lot with a named owner and a due date before next workshop."],
        ["1:25–1:30", "Next steps", "Confirm Workshop 2 date. ECS to configure the agreed taxonomy in the dev environment before Workshop 2."],
    ],
    col_widths_in=[1.0, 2.6, 5.8],
)

doc.h2("Workshop 2 — Priority Matrix, Assignment, and SLA (90 min)")
doc.table(
    headers=["Time", "Agenda Item", "Facilitation Notes"],
    rows=[
        ["0:00–0:10", "Review Workshop 1 decisions (ECS)", "Confirm the category taxonomy and state lifecycle are agreed. Show the dev instance with the taxonomy configured. This builds confidence that decisions translate to working configuration quickly."],
        ["0:10–0:35", "Priority matrix definition", "Present the OOTB 4-tier priority matrix (P1 Critical / P2 High / P3 Medium / P4 Low) with the standard Impact × Urgency calculation. Ask: 'Is there a scenario your team handles that this matrix does not cover?' Common issue: 'VIP users always get P1.' ECS response: the Priority Lookup rules in OOTB Incident Management can automatically elevate priority based on caller VIP flag — demonstrate this."],
        ["0:35–0:55", "Assignment model", "Walk through the OOTB assignment model: category drives assignment group via Assignment Lookup Rules. Present the ECS pre-filled assignment matrix (category → assignment group). Ask: 'Which of these assignment groups exist today? Which need to be created?' ECS to update the Foundation Data Pack group list based on this conversation."],
        ["0:55–1:10", "SLA linkage", "Confirm the SLA definitions from Sprint 1 Platform (INT-FG-01). Map each priority level to its SLA definition. Walk through the OOTB SLA engine: Response SLA (clock starts on creation) and Resolution SLA (clock stops on Resolved state). Ask: 'Are there SLA exceptions — specific categories or callers that have different SLAs?' Document exceptions in the Governed Exceptions log."],
        ["1:10–1:25", "Decision record", "Confirm all decisions. ECS documents in the Decision Log. Parking Lot items go to the Customization Council if they involve configuration deviations."],
        ["1:25–1:30", "Next steps", "ECS to configure priority matrix, assignment rules, and SLA linkage before the validation session. Schedule validation session for 48 hours after this workshop."],
    ],
    col_widths_in=[1.0, 2.6, 5.8],
)

doc.h2("Workshop 3 — Assignment and Notification Validation (60 min)")
doc.table(
    headers=["Time", "Agenda Item", "Facilitation Notes"],
    rows=[
        ["0:00–0:10", "Live instance walkthrough (ECS)", "Open the dev instance. Create a test Incident for each category agreed in Workshop 1. Show the auto-assignment, priority calculation, and SLA clock starting."],
        ["0:10–0:40", "Customer validation — category by category", "Walk through each category with the relevant team lead: 'I created an incident with this category. It auto-assigned to this group. The SLA is this. Does this match your expectation?' Capture any discrepancies in the Decision Log — do not fix on the spot during the session."],
        ["0:40–0:55", "Notification review", "Review the OOTB notification templates: 'Incident Assigned' (to assignee), 'Incident Resolved' (to caller), 'SLA Breach Warning' (to assignment group manager). Ask: 'Who else needs to know when an Incident is created, updated, or resolved?' Add stakeholders to the notification rule — this is configuration, not customization."],
        ["0:55–1:00", "Decisions and next steps", "Confirm sprint demo date. ECS to fix any discrepancies identified during validation. Sprint demo script is INT-DS-01."],
    ],
    col_widths_in=[1.0, 2.6, 5.8],
)
doc.page_break()

# =============================================================================
# 3. Decision Pre-Fills — ECS Recommendations
# =============================================================================
doc.h1("Decision Pre-Fills — ECS Recommendations")
doc.para(
    "These are the ECS pre-filled recommendations for the five core Incident Management decisions. "
    "Pre-fill these in the sprint workbook before Workshop 1. The customer will confirm, adjust, or "
    "reject each one. Your job is to defend the OOTB recommendation using the language in the "
    "Rationale column — not to capitulate immediately when the customer pushes back."
)

doc.h2("Decision 1 — Incident Category Taxonomy")
doc.table(
    headers=["ECS Recommendation", "Rationale", "Common Pushback", "ECS Response"],
    rows=[
        ["Top-level categories: Hardware, Software, Network, Access, Service Request (SR is separate — do not mix SR and Incident categories).",
         "OOTB Incident Management and Service Request Management share the category taxonomy. Mixing Incident and SR categories produces reporting noise and incorrect SLA assignment.",
         "'We have 47 categories today — we can't reduce to 5.'",
         "'Your 47 categories are sub-categories of these 5 top-level groups. We keep the granularity at the sub-category level where analysts need it for routing. The parent categories drive reporting and SLA — that is where the simplification delivers value.'"],
        ["Sub-categories: no more than 8 per top-level category. Total taxonomy: ≤ 40 sub-categories.",
         "Category lists with more than 40 sub-categories show consistent mis-categorization patterns — analysts default to the first or most familiar option and ignore the rest.",
         "'We need more than 8 sub-categories under Software — we have 15.'",
         "'Let us look at which of your 15 sub-categories have been used in the last 90 days. In most environments, 3-5 sub-categories account for 80% of the volume. The rest are aspirational. We can keep the full list — but let us confirm which ones are actually used before we configure all 15.'"],
        ["No 'Other' or 'General' sub-categories.",
         "'Other' becomes the default for every analyst who does not want to think about categorization. After 90 days, 30-40% of your Incident records are in 'Other' and your category reporting is meaningless.",
         "'We need Other for incidents that don't fit the taxonomy.'",
         "'If an incident genuinely does not fit the taxonomy, that is evidence the taxonomy is missing a category — add the missing category to the Customization Council agenda. If it happens frequently, it warrants a real category. If it is rare, it probably fits an existing category and the analyst just did not know which one.'"],
    ],
    col_widths_in=[2.2, 2.2, 2.0, 3.0],
)

doc.h2("Decision 2 — Incident State Lifecycle")
doc.table(
    headers=["ECS Recommendation", "Rationale", "Common Pushback", "ECS Response"],
    rows=[
        ["OOTB states only: New → In Progress → On Hold → Resolved → Closed. Do not add custom states.",
         "Each custom state requires custom transition rules, custom SLA conditions, and custom reporting. The maintenance cost compounds with every upgrade.",
         "'We need a Pending Customer state and a Pending Vendor state.'",
         "'Both of those are On Hold sub-states. OOTB On Hold has a Hold Reason field where analysts enter Pending Customer or Pending Vendor. The SLA clock pauses on On Hold regardless of the reason. Reporting can filter by Hold Reason. You get the same outcome without a custom state.'"],
        ["Closed state requires a closure code (chosen from a configured list) and a resolution summary.",
         "Closure codes are required for Problem Management to identify repeat incident patterns. Resolution summaries are required for Knowledge Article creation. Both are OOTB fields.",
         "'Our analysts do not fill in closure codes — they just close the ticket.'",
         "'That is a process gap, not a system gap. We can make closure code mandatory on the Closed transition — the system will not let the analyst close without selecting a code. The closure code list needs to be short and meaningful, which is what we are designing in Workshop 1.'"],
    ],
    col_widths_in=[2.2, 2.2, 2.0, 3.0],
)

doc.h2("Decision 3 — Priority Matrix")
doc.table(
    headers=["ECS Recommendation", "Rationale", "Common Pushback", "ECS Response"],
    rows=[
        ["4-tier OOTB matrix: P1 Critical (Sev 1 Impact × Sev 1 Urgency), P2 High, P3 Medium, P4 Low. Use OOTB Priority Lookup Rules — do not hardcode priority in category rules.",
         "OOTB Priority Lookup Rules calculate priority dynamically from Impact × Urgency. Hardcoded priorities break when the impact or urgency of the incident is different from the category average.",
         "'Some categories always need to be P1 — why do we need Impact and Urgency?'",
         "'If a category always results in P1 Impact and P1 Urgency, then the Priority Lookup Rule will always produce P1 for that category — which is what you want. But it also means that a low-urgency incident in that category (e.g., a non-critical system in maintenance mode) gets the right priority automatically instead of being forced to P1 by a hardcoded rule. The dynamic calculation is more accurate, not less.'"],
        ["VIP caller automatic priority elevation via OOTB VIP flag on the user record.",
         "VIP elevation is a common requirement in government and financial services environments. OOTB supports this without custom code.",
         "'Our VIPs need P1 regardless of impact.'",
         "'Agreed — and OOTB supports this. If the caller has the VIP flag set on their user record, a Priority Lookup Rule escalates the priority automatically. No custom code, no workaround. We set the VIP flag on the right users in Sprint 1 Platform.'"],
    ],
    col_widths_in=[2.2, 2.2, 2.0, 3.0],
)

doc.h2("Decision 4 — Assignment Model")
doc.table(
    headers=["ECS Recommendation", "Rationale", "Common Pushback", "ECS Response"],
    rows=[
        ["Category-driven assignment: OOTB Assignment Lookup Rules map Incident category → assignment group. Do not use Skills-based routing at MVP.",
         "Skills-based routing requires accurate agent skill profiles, which take 3-6 months to calibrate. Category-driven assignment is accurate from day one.",
         "'We want incidents routed to the individual agent, not the group.'",
         "'Individual agent routing requires either skill profiles (not ready at MVP) or round-robin logic (treats all agents as equivalent — not what you want). Group routing is the right starting point. Agents pull from the group queue based on availability. We can add individual assignment rules in Phase 2 once you have 90 days of data on which agents handle which incident types.'"],
        ["Tier 1 assignment group per major category. Single Tier 2 escalation group per domain. No more than 3 tiers.",
         "More than 3 tiers creates routing loops and unclear ownership. The most common pattern in over-tiered environments: incidents bounce between Tier 2 and Tier 3 for days before anyone owns the resolution.",
         "'We have 5 tiers of support for some incident types.'",
         "'Walk me through a real incident that required all 5 tiers. Almost always, tiers 4 and 5 are vendor escalation or specialist consultation — those are not assignment groups in ServiceNow, they are work notes or related records. The 5-tier structure in the old system was often a workaround for unclear ownership, not a genuine process requirement.'"],
    ],
    col_widths_in=[2.2, 2.2, 2.0, 3.0],
)

doc.h2("Decision 5 — Major Incident Definition")
doc.table(
    headers=["ECS Recommendation", "Rationale", "Common Pushback", "ECS Response"],
    rows=[
        ["OOTB Major Incident criteria: Priority 1 with a named Major Incident Manager assigned. Major Incident workflow: automated notification to MIM on P1 creation, dedicated Major Incident workspace, automated stakeholder bridge communication.",
         "A defined Major Incident process prevents the most common P1 failure mode: too many people in the room with no one clearly in charge. The OOTB Major Incident workspace and task model enforce ownership.",
         "'We do not need a formal Major Incident process — our team handles P1s informally.'",
         "'What happens when a P1 occurs and three senior engineers are all making changes to the system simultaneously without coordinating? Informal works when the team is small and the incident is contained. Major Incident process is what works when the incident spans multiple teams and executives are asking for updates every 15 minutes. We are building this for the worst-case scenario, not the best case.'"],
    ],
    col_widths_in=[2.2, 2.2, 2.0, 3.0],
)
doc.page_break()

# =============================================================================
# 4. Common Pitfalls
# =============================================================================
doc.h1("Common Pitfalls")
doc.para(
    "These are the most frequent Sprint 1 Incident Management problems. Read them before "
    "the first workshop. Recognizing a pitfall in the moment is the difference between "
    "redirecting and losing 45 minutes to a conversation that should have lasted 5."
)

pitfalls = [
    ("Pitfall 1 — The Category Proliferation Spiral",
     "The customer shows up to Workshop 1 with a list of 80 categories and wants to migrate them all. "
     "The session becomes a line-by-line review that never reaches the decision.\n\n"
     "Early signal: the customer's pre-read material includes a spreadsheet with hundreds of rows.\n\n"
     "Redirect: 'Before we review the full list, let us look at this from the top down. We have 2 "
     "hours. What are the 5 most important categories for your SLA reporting, and which 5 categories "
     "create the most routing problems today? Let us solve those 10 first.' "
     "Then do the full list as an async exercise with a deadline of 48 hours."),
    ("Pitfall 2 — The 'Our Process Is Unique' Blocker",
     "After you present the OOTB priority matrix, the customer says: 'Our environment is too complex "
     "for a standard 4-tier model. We need at least 8 priority levels.' This is almost never true — "
     "it is usually a sign that the current system is being used to track work that is not actually "
     "incident management.\n\n"
     "Early signal: any customer with more than 6 priority levels.\n\n"
     "Redirect: 'Walk me through the most recent incident that required a priority level that P1 "
     "through P4 could not have handled.' If they can name one, understand the actual requirement. "
     "If they struggle to name one, that is evidence the extra levels are not being used as designed."),
    ("Pitfall 3 — The Assignment Group Ownership Gap",
     "You present the ECS-recommended assignment model and the customer agrees — but when you ask "
     "'Who is the manager of this assignment group?' there is silence. Assignment groups without named "
     "managers have no accountability, no SLA oversight, and no escalation path.\n\n"
     "Early signal: the customer's HR/org chart data is not ready for the sprint.\n\n"
     "Redirect: 'Assignment groups without managers are where incidents go to be ignored. Before we "
     "configure the groups, we need a named manager for each one. That is a customer action item with "
     "a deadline of 48 hours. The configuration waits for this data.'"),
    ("Pitfall 4 — Scope Creep Into Problem Management",
     "The customer's process owner is also the Problem Management owner and they start designing the "
     "Problem workflow during the Incident workshop because 'we cannot design Incident without "
     "knowing the Problem flow.'\n\n"
     "Early signal: the conversation shifts to root cause analysis before you have finished the "
     "priority matrix.\n\n"
     "Redirect: 'Problem Management is Sprint 3. What we need from this session is the Incident "
     "category taxonomy and closure code list, because the closure code is what triggers a Problem "
     "record. Let us lock the Incident closure codes now and put the full Problem design on the "
     "Sprint 3 agenda.'"),
    ("Pitfall 5 — The 'We Need This For Reporting' Custom State",
     "A stakeholder says: 'We need a Pending Approval state so we can report on incidents waiting "
     "for management approval before resolution.' This is a legitimate reporting need being solved "
     "with the wrong tool.\n\n"
     "Early signal: any request for a new state that includes the word 'reporting' or 'visibility.'\n\n"
     "Redirect: 'The On Hold state with a Hold Reason of Pending Approval gives you the same "
     "reporting view without a custom state. Let me show you the OOTB report filtered by On Hold "
     "reason — it shows exactly which incidents are waiting for approval, for how long, and who "
     "owns the decision. Custom state = same data, higher maintenance cost.'"),
]

for title, content in pitfalls:
    doc.h2(title)
    doc.para(content)

doc.page_break()

# =============================================================================
# 5. Sprint Demo Discipline
# =============================================================================
doc.h1("Sprint Demo Discipline")
doc.para(
    "The Sprint 1 Incident Management demo is guided by INT-DS-01 (Incident Management Demo Script). "
    "Read it before the demo. The notes below complement the script with facilitator guidance "
    "specific to this sprint context."
)

doc.h2("Pre-Demo Checklist")
doc.table(
    headers=["#", "Check", "Owner", "Status"],
    rows=[
        ["1", "Category taxonomy configured in dev instance (agreed categories only — no placeholders)", "ECS SA", "☐"],
        ["2", "Priority Lookup Rules configured and tested (P1 VIP elevation confirmed working)", "ECS SA", "☐"],
        ["3", "Assignment Lookup Rules configured for at least 3 categories with real customer groups", "ECS SA", "☐"],
        ["4", "SLA definitions linked to priorities and confirmed showing correct clock in test incidents", "ECS SA", "☐"],
        ["5", "Notification templates configured with customer branding (logo, correct org name)", "ECS SA", "☐"],
        ["6", "Test incident pre-created for each of the top 3 categories (ready for live demo walk-through)", "ECS Lead", "☐"],
        ["7", "Major Incident test scenario configured (P1 test incident with MIM notification ready)", "ECS Lead", "☐"],
        ["8", "INT-TBV-06 Sprint Demo Discipline Audit printed and brought to demo", "EM", "☐"],
    ],
    col_widths_in=[0.4, 5.8, 1.4, 1.0],
)

doc.h2("Demo Tone Guidance")
doc.para(
    "The Incident demo audience includes the Service Desk Manager (highly operational, "
    "cares about the analyst experience), the IT Director (cares about SLA compliance and "
    "reporting), and potentially some Tier 1 analysts (cares about whether the system is "
    "easier or harder than what they have today). "
)
doc.para(
    "Frame the demo for each audience: 'For the analysts — here is how they log an incident "
    "and how the system routes it without them having to decide where it goes. For the Service "
    "Desk Manager — here is the queue view and the SLA compliance dashboard. For the IT Director — "
    "here is the category-by-volume report and the P1 resolution time trend.'"
)
doc.callout(
    "Demo rule: configure with real customer data. Categories the customer recognized in Workshop 1, "
    "group names from their org chart, SLA targets they approved. A demo with placeholder data "
    "('Category A', 'Group 1') destroys credibility and creates doubt about whether the system "
    "actually works for their environment."
)

doc.h2("Handling Demo Questions")
doc.table(
    headers=["Question", "ECS Response"],
    rows=[
        ["'Can we change the category taxonomy after go-live?'",
         "Yes — categories are configuration, not code. Changes to the taxonomy affect new records only; historical records retain their original category. We recommend a quarterly taxonomy review process, not ad-hoc changes."],
        ["'What happens to incidents created in the old system?'",
         "Historical incidents from the old system are migrated as closed records for reference and reporting. They are not live incidents in ServiceNow. The migration approach is scoped in Sprint 0 and executed in Sprint 6."],
        ["'Can analysts override the auto-assigned priority?'",
         "Yes — analysts with the itil role can change priority. Priority override is logged in the audit trail. We recommend a monthly report on priority overrides as a quality check — high override rates indicate the Priority Lookup Rules need tuning."],
        ["'How do we handle incidents that span multiple categories?'",
         "OOTB: a single category on the Incident record. Related incidents (same root cause, different categories) are linked via the Related Incidents related list. The parent-child relationship is visible on both records. This is the OOTB approach and it is more maintainable than multi-category incident records."],
        ["'What if our SLA targets are different for different customers or contracts?'",
         "OOTB supports per-customer SLA targets via Contract-based SLAs. The SLA definition can include a Contract condition — if the caller's account matches the contract, the contract SLA applies. This is a Sprint 3 configuration item once the base SLA framework is stable."],
    ],
    col_widths_in=[3.0, 6.4],
)
doc.page_break()

# =============================================================================
# 6. Sprint Retro Template
# =============================================================================
doc.h1("Sprint Retro Template")
doc.para(
    "Run the sprint retro in the last 30 minutes of the sprint demo session, after the demo "
    "questions are complete. Keep it fast — this is a team alignment exercise, not a post-mortem. "
    "Capture the output in the Decision Log."
)

doc.table(
    headers=["Category", "Question", "Notes / Capture Here"],
    rows=[
        ["What worked", "Which workshop sessions were most productive? What did the customer respond to best?", ""],
        ["What worked", "Which ECS pre-fills were accepted without major revision?", ""],
        ["What did not work", "Where did the workshops lose momentum or go sideways?", ""],
        ["What did not work", "Which customer participants were missing or disengaged? Does this need to be escalated?", ""],
        ["Decisions deferred", "Which Sprint 1 decisions are still outstanding? (List with owner and deadline)", ""],
        ["Governed exceptions", "How many items went to the Governed Exceptions log? (Target: ≤ 3 per sprint)", ""],
        ["Sprint 2 readiness", "Is the customer ready for Sprint 2 (Catalog and Employee Center)? What blockers exist?", ""],
        ["ECS team learning", "What would we do differently if we ran Sprint 1 again on this engagement?", ""],
    ],
    col_widths_in=[1.6, 4.0, 3.8],
)

doc.para(
    "If the Governed Exceptions log has more than 3 items from Sprint 1 Incident, flag this "
    "to the Engagement Manager before Sprint 2 begins. The Customization Council must clear "
    "the backlog before the volume becomes unmanageable. Reference INT-TBV-08 "
    "(Engagement Course-Correction Playbook) if the exception count signals a deeper "
    "OOTB resistance pattern."
)

doc.save(OUT)
print(f"INT-FG-02 built → {OUT}")
