"""
Build INT-HT-02 — Incident Management How-To Consultant Guide
Internal audience — mirrors INT-HT-16 (HAM) structure.
Sections: OOTB Capabilities, Two-Phase Approach, OOTB Defense, Demo Flow, UAT Scenarios, Post-Go-Live Ownership.
Companion to: INT-FG-02, INT-DS-01
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

OUT = os.path.join(HERE, "Incident_Management_How-To_Consultant_Guide_INTERNAL.docx")

doc = EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL · DISCIPLINE HOW-TO GUIDE",
    title="Incident Management\nConsultant How-To Guide",
    subtitle="OOTB capabilities, configuration playbook, OOTB defense language, demo flow, UAT scenarios, and post-go-live ownership for ServiceNow Incident Management",
    audience="ECS Lead Consultant, Solution Architect",
    companion_to="INT-FG-02 Sprint 1 Incident Facilitator Guide · INT-DS-01 Incident Demo Script · ITSM Accelerator Pack",
    doc_id="INT-HT-02",
    version="1.0",
    status="Released",
    running_header_label="Internal · Incident Management How-To Consultant Guide",
), logo_path=LOGO)

doc.add_cover_page()
doc.page_break()

# =============================================================================
# 1. What This Guide Is For
# =============================================================================
doc.h1("What This Guide Is For", numbered=False)
doc.para(
    "This guide is the ECS practitioner's reference for configuring, defending, and operating "
    "OOTB ServiceNow Incident Management. Use it alongside the Sprint 1 Incident Facilitator "
    "Guide (INT-FG-02) for workshop preparation and alongside the Incident Demo Script (INT-DS-01) "
    "for demo preparation. It is the discipline-specific depth behind the sprint-level guidance."
)
doc.para(
    "Incident Management is the highest-traffic module in every ServiceNow ITSM deployment. "
    "It is also the module where customers have the most pre-existing opinions, the most "
    "accumulated technical debt in their legacy system, and the strongest resistance to change. "
    "This guide gives you the configuration knowledge to build it correctly and the conversation "
    "language to defend what you have built."
)
doc.page_break()

# =============================================================================
# 1. OOTB Capabilities
# =============================================================================
doc.h1("OOTB Incident Management Capabilities")
doc.para(
    "ServiceNow OOTB Incident Management includes more capability than most customers realize "
    "before they see a properly configured instance. Demonstrating the full OOTB capability "
    "set before any customization conversation is the single most effective technique for "
    "reducing the governed exceptions log."
)

doc.h2("Core Workflow Engine")
doc.table(
    headers=["Capability", "What It Does", "Configuration Required"],
    rows=[
        ["State Lifecycle Management", "New → In Progress → On Hold → Resolved → Closed with mandatory fields at each transition (e.g., resolution summary required to Resolve)", "Mandatory fields per state configured via UI Policy or Business Rule"],
        ["Priority Lookup Rules", "Calculates Incident Priority from Impact × Urgency matrix automatically on creation and update. Supports VIP caller elevation and category-based overrides.", "Configure via Incident > Administration > Priority Lookup Rules"],
        ["Assignment Lookup Rules", "Auto-assigns to the correct group based on category, subcategory, and location. No analyst decision required for routing.", "Configure via Incident > Administration > Assignment Lookup Rules"],
        ["SLA Engine", "Response SLA (clock starts on creation) and Resolution SLA (clock stops on Resolved). Supports per-priority, per-category, and per-contract SLA definitions.", "SLA Definitions + SLA Workflow conditions; linked to Incident via SLA module"],
        ["On Hold with Hold Reason", "Suspends the SLA clock during customer wait or vendor hold. Hold Reason field distinguishes Pending Customer from Pending Vendor without custom states.", "OOTB On Hold state + Hold Reason field; no custom development"],
        ["Closure Code Requirements", "Mandates a closure code and resolution summary before the Incident can move to Closed state.", "Mandatory field on Closed transition via UI Policy"],
        ["Duplicate Detection", "Identifies similar open Incidents and suggests merge before a new Incident is submitted.", "OOTB similar Incident suggestions; configure sensitivity threshold"],
    ],
    col_widths_in=[2.0, 4.2, 3.2],
)

doc.h2("Major Incident Management")
doc.table(
    headers=["Capability", "What It Does", "Configuration Required"],
    rows=[
        ["Major Incident Declaration", "P1 Incidents can be declared Major Incidents, activating the Major Incident workflow: dedicated workspace, named Major Incident Manager (MIM), task model for parallel workstreams.", "Major Incident module configuration; MIM role assignment"],
        ["Stakeholder Communication Templates", "Automated stakeholder updates at configurable intervals (e.g., every 30 minutes during a Major Incident). Pre-built templates that the MIM can send with one click.", "Email notification templates for Major Incident state changes"],
        ["Communication Plan", "OOTB Communication Plan tracks who has been notified, when, and with what update — visible to all responders.", "Communication Plan configuration within the Major Incident workspace"],
        ["Post-Incident Review (PIR) Task", "Auto-creates a PIR task linked to the closed Major Incident. PIR drives Problem Management creation.", "PIR task Business Rule on Major Incident closure"],
        ["Timeline View", "Visual timeline of all Incident updates, state changes, and communications during a Major Incident — used for the post-incident review.", "OOTB; no configuration required"],
    ],
    col_widths_in=[2.0, 4.2, 3.2],
)

doc.h2("Reporting and Analytics")
doc.table(
    headers=["Capability", "What It Does"],
    rows=[
        ["OOTB Incident Dashboards", "Category by volume, priority distribution, SLA compliance rate, MTTR trend, assignment group workload. All OOTB; no custom report development."],
        ["Performance Analytics Indicators", "OOTB PA indicators for Incident volume, MTTR, SLA compliance, and reopen rate. Trend data available from day one."],
        ["Incident Reopen Rate", "OOTB metric tracking incidents that move from Resolved back to In Progress — the most reliable measure of resolution quality."],
        ["Category-by-SLA Compliance Report", "Cross-tab of category against SLA compliance rate. Immediately reveals which categories have SLA problems and which assignment groups are the bottleneck."],
    ],
    col_widths_in=[2.5, 6.9],
)
doc.page_break()

# =============================================================================
# 2. Two-Phase Configuration Approach
# =============================================================================
doc.h1("Two-Phase Configuration Approach")
doc.para(
    "Incident Management configuration follows the same two-phase model as every OOTB-first "
    "discipline: Phase 1 (Sprint 1) builds the baseline with OOTB capabilities and customer data. "
    "Phase 2 (post-go-live) adds the governed enhancements that the customer genuinely needs "
    "after seeing Phase 1 working in production."
)

doc.h2("Phase 1 — Sprint 1 Baseline (Weeks 3-4)")
doc.table(
    headers=["Configuration Item", "Approach", "Owner", "Sprint Timing"],
    rows=[
        ["Incident category taxonomy", "OOTB taxonomy with customer-agreed categories (max 5 top-level, max 8 sub-categories each)", "ECS SA after Workshop 1", "Week 3"],
        ["Priority Lookup Rules", "OOTB 4-tier matrix (P1/P2/P3/P4) with VIP elevation. Import from ITSM Accelerator Pack tab 01.", "ECS SA after Workshop 2", "Week 3"],
        ["Assignment Lookup Rules", "Category → assignment group mapping from Foundation Data Pack groups. Import from ITSM Accelerator Pack tab 01.", "ECS SA after Workshop 2", "Week 3"],
        ["SLA definitions", "Per-priority SLA targets agreed in Sprint 1 Platform. Link to Incident via SLA module.", "ECS SA after Workshop 2", "Week 3-4"],
        ["Notification templates", "OOTB templates with customer branding: Incident Assigned, Incident Resolved, SLA Breach Warning.", "ECS SA", "Week 4"],
        ["Closure code list", "Customer-agreed closure codes (target: 6-10 codes). Mandatory on Closed transition.", "ECS SA after Workshop 1", "Week 3"],
        ["Major Incident workflow", "OOTB Major Incident configuration with named MIM role and stakeholder notification templates.", "ECS SA", "Week 4"],
        ["UAT scenario execution", "All 5 standard UAT scenarios from Section 5 of this guide", "ECS Lead + Customer", "Week 4"],
    ],
    col_widths_in=[2.2, 4.0, 1.6, 1.6],
)

doc.h2("Phase 2 — Post-Go-Live Enhancements")
doc.table(
    headers=["Enhancement", "Trigger", "Approach"],
    rows=[
        ["Contract-based SLA differentiation", "Customer has multiple customer contracts with different SLA targets", "OOTB Contract SLA condition on SLA Definition; no custom code"],
        ["Skills-based agent routing", "Volume data shows significant variation in incident types by agent (90+ days of data)", "OOTB Skill Assignment in Agent Workspace; requires agent skill profiles"],
        ["Predictive Intelligence — category classification", "Category mis-classification rate > 15% from PA report", "OOTB Predictive Intelligence category classification model; requires 30+ days of labeled data"],
        ["Virtual Agent Incident deflection", "Sprint 5 VA configuration; Incident creation from VA topic", "OOTB VA Incident creation topic; no custom development"],
        ["Watch list and stakeholder notifications", "Customer request for role-based stakeholder subscriptions to Incident updates", "OOTB Incident Watch List field; add stakeholders, configure notification rules"],
        ["Expanded closure code taxonomy", "Post-go-live analysis shows closure code gaps or high 'Other' usage", "Add missing codes; quarterly review cadence recommended"],
    ],
    col_widths_in=[2.4, 2.8, 4.2],
)
doc.page_break()

# =============================================================================
# 3. OOTB Defense Language
# =============================================================================
doc.h1("OOTB Defense Language")
doc.para(
    "These are the most common requests for Incident Management customization and the "
    "ECS-recommended responses. The goal is to understand the underlying need and show how "
    "OOTB meets it before escalating to the Customization Council."
)

defense_items = [
    ("'We need a custom state: Pending Approval'",
     "The need is to pause the SLA clock and track incidents waiting for management approval before resolution.",
     "Use the OOTB On Hold state with a Hold Reason of 'Pending Approval'. The SLA clock pauses on On Hold. A report filtered by Hold Reason = Pending Approval shows all incidents in this state. Mandatory fields on the On Hold transition can require the analyst to document who the approval is pending from.",
     "Never. Add to the Customization Council agenda only if the customer needs On Hold sub-states with different SLA behaviors — which the Hold Reason field handles without customization."),
    ("'We need more than 4 priority levels — we use 7 today'",
     "The need is to differentiate urgency between incidents that all have the same business impact but different response urgency profiles.",
     "Map their 7 levels to the 4-tier OOTB matrix: Critical and Urgent both map to P1 (response in 1 hour regardless). High maps to P2. Medium maps to P3. Low and Informational both map to P4. The distinction between Critical and Urgent in the old system is almost always about notification routing, not SLA — which OOTB handles via notification rules, not priority levels.",
     "Escalate to Customization Council only if the customer has a contractual obligation to support more than 4 priority levels in reporting. Even then, Priority Lookup Rules with custom conditions can produce the right behavior."),
    ("'We need to auto-create incidents from emails without a Service Desk agent touching them'",
     "The need is to reduce Service Desk workload for high-volume, low-complexity Incident submissions.",
     "OOTB Inbound Email Actions create Incidents from email automatically. The email subject populates short_description; the body populates description. Category, assignment group, and priority can be set by email parsing rules. This is OOTB — no custom development.",
     "Inbound Email Actions are OOTB. Walk through the configuration in the demo if this is a customer requirement."),
    ("'We want Incident records to be read-only once they are Closed — no one should be able to edit them'",
     "The need is audit integrity — closed Incidents should not be modified.",
     "OOTB: Access Control Rules (ACLs) can restrict write access on Incident records in Closed state to sys_admin only. This is an ACL configuration — no custom code. Existing ACLs in the base system should be reviewed first to avoid overwriting platform controls.",
     "ACL-based read-only on Closed is OOTB-supportable configuration. Bring to Customization Council only if the customer wants something more granular (e.g., read-only except for certain fields or roles)."),
    ("'We need a dedicated queue for walk-in requests versus phone calls versus self-service submissions'",
     "The need is to track the channel of submission for reporting and workload management.",
     "Use the OOTB Contact Type field on the Incident record: Phone, Email, Self-Service, Walk-In, Chat. Reports can be filtered by Contact Type. Assignment rules can prioritize based on Contact Type if needed.",
     "Contact Type is an OOTB field. No customization needed. Show the field in the demo."),
]

for title, need, ootb_response, escalation in defense_items:
    doc.h2(title)
    doc.table(
        headers=["Element", "Detail"],
        rows=[
            ["Underlying need", need],
            ["OOTB response", ootb_response],
            ["When to escalate", escalation],
        ],
        col_widths_in=[1.8, 7.6],
    )

doc.page_break()

# =============================================================================
# 4. Demo Flow (4 Acts)
# =============================================================================
doc.h1("Demo Flow (4 Acts)")
doc.para(
    "This is the high-level demo structure. The full click-by-click script is in INT-DS-01. "
    "Use this summary to brief ECS team members who need to understand the demo arc "
    "without reading the full script."
)

doc.h2("Act 1 — Incident Creation and Auto-Routing (10 minutes)")
doc.para(
    "Scenario: A network team member reports that a core switch is intermittently dropping packets. "
    "Show: self-service portal Incident creation (analyst fills category: Network, subcategory: "
    "Connectivity, urgency: High). System auto-calculates Priority 2. Assignment Lookup Rule routes "
    "to Network Operations group. SLA clock starts. Notification sent to Network Operations group manager. "
    "Key message: 'The analyst made one decision — what type of problem this is. The system made every "
    "other routing decision automatically.'"
)

doc.h2("Act 2 — Priority Escalation and SLA Management (8 minutes)")
doc.para(
    "Scenario: The network outage escalates — two additional offices are now affected and a VIP executive "
    "is impacted. Show: Priority escalation to P1 via manual override (log the override reason). VIP flag "
    "on the executive's user record triggers automatic P1 elevation for subsequent incidents from the same "
    "caller. SLA breach warning notification fires when the P1 response SLA is approaching breach. "
    "Key message: 'The SLA engine is working for you, not just tracking failure. The breach warning gives "
    "the team time to escalate before the SLA is missed.'"
)

doc.h2("Act 3 — Major Incident Declaration and Communication (10 minutes)")
doc.para(
    "Scenario: The network outage is declared a Major Incident. Show: Major Incident declaration checkbox "
    "on the P1 Incident. Major Incident Manager role assigned. Stakeholder communication plan activated. "
    "30-minute update notification template sent to IT leadership. Timeline view showing all responder "
    "actions in sequence. Key message: 'When you need command-and-control during a P1, the Major Incident "
    "workspace is already built. You are not doing this in a group chat and a shared spreadsheet.'"
)

doc.h2("Act 4 — Resolution, Closure, and Reporting (7 minutes)")
doc.para(
    "Scenario: The network issue is resolved. Show: Resolution state transition with mandatory resolution "
    "summary and closure code (Root Cause: Hardware Failure). Caller notification sent automatically. "
    "Post-Incident Review task auto-created. Jump to the OOTB Incident dashboard: SLA compliance rate, "
    "category-by-volume chart, MTTR trend. Key message: 'From the moment the Incident was created to the "
    "PIR task being assigned, the system guided every step. Your team spent zero time on process management "
    "and 100% of their time on fixing the problem.'"
)
doc.page_break()

# =============================================================================
# 5. UAT Scenarios
# =============================================================================
doc.h1("UAT Scenarios")
doc.para(
    "Run all five UAT scenarios with customer participants before the sprint demo. "
    "UAT is not the demo — UAT is the quality gate. Confirm each scenario passes before "
    "the sprint demo date. If a scenario fails, fix the configuration and re-test. "
    "Do not bring an untested scenario to the sprint demo."
)

doc.table(
    headers=["#", "Scenario", "Steps", "Pass Criteria"],
    rows=[
        ["1", "Standard Incident — auto-routing and SLA",
         "1. Log Incident: Category=Network, Subcategory=Connectivity, Impact=2, Urgency=2.\n2. Submit.\n3. Observe priority, assignment group, SLA.",
         "Priority = P2 (per matrix). Assignment group = Network Operations (per Assignment Rule). Response SLA clock running. Assignee notification sent within 60 seconds."],
        ["2", "VIP caller priority elevation",
         "1. Log Incident on behalf of a VIP-flagged user: same category, same urgency.\n2. Submit.\n3. Observe priority.",
         "Priority = P1 automatically (VIP elevation rule). No manual override required."],
        ["3", "On Hold — SLA pause",
         "1. Set an open Incident to On Hold. Hold Reason = Pending Customer.\n2. Wait 2 minutes.\n3. Return to In Progress.",
         "SLA clock pauses when state = On Hold. Clock resumes when state returns to In Progress. Total hold time visible in SLA record."],
        ["4", "Mandatory closure fields",
         "1. Attempt to close an Incident without entering a resolution summary.\n2. Attempt to close without selecting a closure code.\n3. Enter both fields. Close.",
         "System blocks closure without resolution summary (UI Policy error message). System blocks closure without closure code. Closure succeeds when both fields are populated."],
        ["5", "Major Incident declaration",
         "1. Create a P1 Incident. 2. Check the Major Incident checkbox. 3. Assign a Major Incident Manager. 4. Open the Major Incident workspace.",
         "Major Incident workspace opens with timeline, communication plan, and task model visible. MIM receives notification. Stakeholder communication template available for one-click sending."],
    ],
    col_widths_in=[0.4, 1.8, 3.4, 3.8],
)
doc.page_break()

# =============================================================================
# 6. Post-Go-Live Ownership
# =============================================================================
doc.h1("Post-Go-Live Ownership")
doc.para(
    "Incident Management is a living configuration. The handover to the customer admin team "
    "must include the knowledge to maintain and tune it, not just to operate it."
)

doc.h2("What the Customer Admin Team Owns")
doc.table(
    headers=["Item", "Frequency", "Tool/Location", "Training Required"],
    rows=[
        ["Category taxonomy review and updates", "Quarterly", "Incident > Administration > Categories", "Yes — guide admin through adding/removing categories and sub-categories"],
        ["Assignment Lookup Rule updates", "As org structure changes", "Incident > Administration > Assignment Lookup Rules", "Yes — demonstrate how to add a new rule and test it"],
        ["Priority Lookup Rule tuning", "Quarterly (after reviewing override rate report)", "Incident > Administration > Priority Lookup Rules", "Yes — demonstrate condition logic and Impact/Urgency matrix"],
        ["Closure code list maintenance", "Semi-annually", "Incident > Administration > Choice Lists (closed_code field)", "Yes — show the Choice List editor"],
        ["Notification template updates", "As needed (e.g., org name or logo change)", "System Notification > Email > Notifications", "Yes — demonstrate HTML template editing"],
        ["SLA definition review", "Annually or when SLA targets change contractually", "SLA > SLA Definitions", "Yes — demonstrate SLA condition and schedule linking"],
        ["Category mis-categorization report review", "Monthly", "PA Dashboard > Incident Category-by-SLA Compliance", "Show admin how to filter the report and identify outliers"],
        ["Priority override rate review", "Monthly", "Custom report on Incident audit log", "ECS to build the override report before handover"],
    ],
    col_widths_in=[2.4, 1.4, 2.4, 3.2],
)

doc.h2("Escalation Criteria — When to Call ECS")
doc.para(
    "The customer admin team should handle routine maintenance without ECS involvement. "
    "The following conditions warrant re-engaging ECS:"
)
doc.table(
    headers=["Condition", "Threshold", "Action"],
    rows=[
        ["Incident SLA compliance rate", "< 70% for any priority level at 60 days", "ECS audit of Priority Lookup Rules and assignment rules; may indicate category or routing misconfiguration"],
        ["Category mis-categorization rate", "> 20% of incidents changed category after creation", "ECS audit of category taxonomy and Assignment Lookup Rules"],
        ["Priority override rate", "> 15% of incidents have priority manually overridden", "ECS review of Priority Lookup Rules; may indicate the matrix does not reflect actual customer urgency patterns"],
        ["Closure code 'Other' usage", "> 25% of closed incidents using 'Other' closure code", "ECS review of closure code list; missing codes are driving analyst workarounds"],
        ["Major Incident declaration rate", "0 declarations in 90 days despite P1 incidents occurring", "Indicates MIM role is not being used; ECS coaching session on Major Incident process"],
    ],
    col_widths_in=[2.6, 2.0, 4.8],
)

doc.h2("Knowledge Transfer Checklist")
doc.table(
    headers=["#", "Knowledge Area", "Transferred?", "Recipient"],
    rows=[
        ["1", "Category taxonomy administration (add/remove/rename)", "☐", ""],
        ["2", "Assignment Lookup Rule configuration", "☐", ""],
        ["3", "Priority Lookup Rule configuration and testing", "☐", ""],
        ["4", "SLA Definition linking and condition configuration", "☐", ""],
        ["5", "Closure code list administration", "☐", ""],
        ["6", "Notification template editing", "☐", ""],
        ["7", "Major Incident process and workspace navigation", "☐", ""],
        ["8", "OOTB Incident dashboards and PA indicator access", "☐", ""],
        ["9", "Priority override and mis-categorization reports", "☐", ""],
        ["10", "Escalation criteria — when to re-engage ECS", "☐", ""],
    ],
    col_widths_in=[0.4, 4.4, 1.4, 3.2],
)

doc.save(OUT)
print(f"INT-HT-02 built → {OUT}")
