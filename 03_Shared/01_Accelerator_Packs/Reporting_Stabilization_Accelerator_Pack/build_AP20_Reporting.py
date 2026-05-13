"""
build_AP20_Reporting.py -- AP-20 Reporting & Stabilization Accelerator Pack
Covers: OOTB report catalog, stabilization checklist, customer admin
training plan, engagement handover, and Phase 2 readiness.
Sprint window: Month 3 (Sprint 6) -- engagement close
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "03_Shared", "00_Templates_and_Branding"))
from accelerator_pack_builder import TabContent, build_workbook
from ecs_template import EcsDocument, DocMeta

PACK_DIR = HERE
PACK_NAME = "Reporting & Stabilization Accelerator Pack"

wb1 = TabContent(
    workbook_title="01 -- OOTB Report Catalog",
    pack_name=PACK_NAME,
    purpose="Document the OOTB ServiceNow reports configured and shared with customer stakeholders as part of the 18-week engagement close. Covers ITSM, CMDB, Catalog, and HAM/SAM operational reports.",
    who_fills="ECS Consultant documents all reports configured during the engagement. Customer Process Owners confirm they can access and run each report.",
    sprint_window="Sprint 6 -- all reports confirmed by Week 12",
    estimated_effort="3-4 hours to document, configure, and share reports",
    related_workbooks=["AP-19 Performance Analytics", "02 Stabilization Checklist"],
    success_criteria=[
        "All go-live reports documented with table, filter, and audience.",
        "Reports shared to correct roles (not individual users).",
        "Each Process Owner can locate and run their reports independently.",
        "Report groups created for each audience (IT Director, IT Manager, Service Desk).",
        "No custom scripted reports created -- OOTB report builder only.",
    ],
    process_decisions=[
        ("Should reports be shared to individual users or roles?",
         "Roles only. Never share to individual users in production.",
         "User-level sharing requires manual maintenance as people change roles. Role-based sharing is self-maintaining."),
        ("Should a report catalog document be provided to the customer?",
         "Yes -- this workbook IS the report catalog. Customer receives it as part of Sprint 6 handover.",
         "A documented report catalog prevents the common post-engagement question: where is the report for X?"),
        ("Should reports be organized into report groups?",
         "Yes -- create three OOTB report groups: IT Leadership, IT Operations, Service Desk. Each group contains the reports for that audience.",
         "Report groups allow users to find their reports without searching. OOTB report group configuration takes 30 minutes."),
        ("Should any scheduled report deliveries be configured?",
         "Yes -- weekly email delivery of the Incident Summary Report to IT Manager. Monthly delivery of SLA Report to IT Director.",
         "Scheduled delivery ensures leaders see key reports even if they do not log into ServiceNow regularly."),
    ],
    dependencies=[
        ("All ITSM processes active and generating data", "Required", "ECS", "Sprint 4 close", "Reports require source data."),
        ("Roles confirmed for all report audiences", "Required", "Customer", "Sprint 6 Wk 1", "Reports shared to roles -- roles must exist."),
        ("CMDB, Catalog, HAM data populated", "Recommended", "ECS", "Sprint 5 close", "Operational reports for CMDB and HAM require populated data."),
    ],
    config_sections=[
        ("ITSM Reports", [
            ("Incident Summary (Weekly)", "Table: incident. Filter: opened_at > last 7 days. Group by: category, assignment group. Audience: IT Manager.", "Share to IT Manager role. Schedule: every Monday 8am.", False),
            ("Open Incidents by Priority", "Table: incident. Filter: state != Closed. Group by: priority. Audience: IT Manager, Service Desk Manager.", "Share to IT Manager and Service Desk Manager roles.", False),
            ("SLA Compliance Monthly", "Table: task_sla. Filter: stage = completed, sys_created_on > last 30 days. Metric: % met. Audience: IT Director.", "Share to IT Director role. Schedule: last day of month.", False),
            ("Incidents Resolved Without Reassignment (FCR)", "Table: incident. Filter: reassignment_count = 0, state = Closed. Group by: assignment group. Audience: IT Manager.", "Approximates FCR rate. Share to IT Manager role.", False),
            ("Aging Open Incidents (>5 days)", "Table: incident. Filter: state != Closed, sys_created_on < 5 days ago. Order by: opened_at asc. Audience: Service Desk Manager.", "Identifies tickets at risk of SLA breach.", False),
        ]),
        ("CMDB Reports", [
            ("CI Count by Class", "Table: cmdb_ci. Group by: sys_class_name. Audience: IT Manager.", "Provides CMDB population summary.", False),
            ("CIs Discovered in Last 30 Days", "Table: cmdb_ci. Filter: sys_created_on > last 30 days. Group by: sys_class_name. Audience: IT Manager.", "Validates Discovery is running and producing results.", False),
            ("Stale CIs (no Discovery update in 60 days)", "Table: cmdb_ci. Filter: last_discovered < 60 days ago. Audience: CMDB Admin.", "Identifies CIs that may need Discovery schedule review.", False),
        ]),
        ("Service Catalog Reports", [
            ("Catalog Item Requests (Monthly)", "Table: sc_request. Filter: opened_at > last 30 days. Group by: cat_item. Audience: IT Manager.", "Shows most-requested catalog items -- informs catalog optimization.", False),
            ("Open Requests by Fulfillment Group", "Table: sc_req_item. Filter: state != Closed. Group by: assignment group. Audience: IT Manager.", "Identifies fulfillment backlog by team.", False),
        ]),
        ("HAM/SAM Reports (if in scope)", [
            ("Hardware Asset Inventory", "Table: alm_hardware. Group by: model category, location. Audience: IT Asset Manager.", "Full hardware asset count by model and location.", False),
            ("Assets Due for Refresh (next 90 days)", "Table: alm_hardware. Filter: retire_date < 90 days from now. Audience: IT Asset Manager.", "Informs procurement planning.", False),
            ("Software License Compliance Summary", "Table: alm_license. Group by: publisher. Metric: compliance status. Audience: IT Director, SAM Manager.", "If SAM is in scope -- license compliance overview.", False),
        ]),
        ("Report Groups & Delivery", [
            ("Report Group: IT Leadership", "Reports: SLA Compliance Monthly, Incident Summary Weekly, Software License Compliance. Share to: IT Director role.", "Group created in Reports > View > Groups", False),
            ("Report Group: IT Operations", "Reports: Open Incidents by Priority, Catalog Item Requests, CI Count by Class. Share to: IT Manager role.", "", False),
            ("Report Group: Service Desk", "Reports: Aging Open Incidents, Open Requests by Fulfillment Group, FCR. Share to: Service Desk Manager role.", "", False),
            ("Scheduled delivery: Incident Summary", "Every Monday 8am local time -- to IT Manager role via email", "OOTB scheduled report -- confirm email domain is allowlisted", True),
            ("Scheduled delivery: SLA Report", "Last business day of month -- to IT Director role via email", "Confirm email domain and delivery time", True),
        ]),
    ],
    raci_rows=[
        ("Configure and share OOTB reports", "R/A", "I", "ECS Consultant."),
        ("Create report groups", "R/A", "I", "ECS Consultant."),
        ("Configure scheduled report delivery", "R/A", "Confirm email addresses", "ECS configures; Customer IT Manager confirms recipients."),
        ("UAT -- each Process Owner runs their reports independently", "R (facilitate)", "A (perform)", "ECS facilitates; each owner must run reports without ECS assistance."),
        ("Document report catalog in this workbook", "R/A", "Review + sign off", "ECS documents; Customer PM reviews and signs off."),
    ],
    consultant_guide_sections=[
        ("Role-sharing discipline", "Never share a report to an individual user. Role-based sharing is the only acceptable pattern. If a stakeholder says 'I need this report but I do not have the role,' the correct answer is 'we add you to the role' not 'we share the report directly to you.' This keeps report governance clean."),
        ("Scheduled report email domain", "Before configuring scheduled report delivery, confirm with the Customer IT team that the ServiceNow email sender domain is allowlisted in their email gateway. Reports scheduled to deliver to blocked domains silently fail -- no error, no delivery. Test with a single report first."),
        ("Report catalog as handover artifact", "This workbook is one of the most used handover documents. Customers reference it for months after the engagement. Ensure every report is documented with: table name, filter conditions, group by, and who has access. A report without documentation is a mystery six months later."),
    ],
    adoption_rows=[
        ("Build us custom scripted reports",
         "OOTB report builder covers all 18-week reporting needs.",
         "Scripted reports require JavaScript, are fragile across upgrades, and are not supportable by the customer post-engagement.",
         "The OOTB report builder can answer every question in your report catalog without a single line of code. Scripted reports are a maintenance liability -- they break on upgrades and require developer involvement to fix. Every report we build is OOTB and can be maintained by your team in ServiceNow's built-in interface.",
         "If a requirement genuinely cannot be met with OOTB reporting -- document it as a Phase 2 custom development item with effort estimate."),
    ],
    snmap_sections=[
        ("Reports", [
            ("sys_report", "Report record -- table, filter, display, chart type", "sys_report"),
            ("sys_report_group", "Report group -- container for organizing reports by audience", "sys_report_group"),
            ("sys_report_schedule", "Scheduled delivery record -- frequency, recipients, format", "sys_report_schedule"),
        ]),
    ],
)

wb2 = TabContent(
    workbook_title="02 -- Stabilization Checklist",
    pack_name=PACK_NAME,
    purpose="Provide the definitive go/no-go stabilization checklist covering all 18-week workstreams. Each item must be confirmed before ECS transitions from delivery to hypercare and handover.",
    who_fills="ECS PM leads. One responsible party per checklist item -- either ECS or Customer. Items marked red block handover.",
    sprint_window="Sprint 6 -- checklist complete by Week 12",
    estimated_effort="3-4 hours with ECS PM and Customer PM",
    related_workbooks=["All Accelerator Pack workbooks", "04 Handover & Sign-Off"],
    success_criteria=[
        "All checklist items green or formally accepted as known exceptions.",
        "No red items that are not acknowledged by Customer PM in writing.",
        "ECS PM and Customer PM have reviewed checklist together.",
        "Known exceptions documented with remediation plan and owner.",
    ],
    process_decisions=[
        ("What happens if a stabilization item is not complete at Sprint 6?",
         "Item is documented as a known exception with: (1) description of gap, (2) impact, (3) remediation owner, (4) remediation deadline.",
         "Known exceptions with documented plans are acceptable. Undiscovered gaps after handover are not. All gaps must be surfaced and acknowledged before sign-off."),
        ("Who has final authority to declare stabilization complete?",
         "Customer IT Director signs the stabilization sign-off. ECS PM countersigns.",
         "Both parties must agree. ECS cannot declare stabilization without Customer IT Director sign-off."),
    ],
    dependencies=[
        ("All sprint deliverables complete per AP workbooks", "Required", "ECS + Customer", "Sprint 6 Wk 2", "Each AP workbook has its own UAT sign-off -- those must be complete before stabilization."),
    ],
    config_sections=[
        ("Foundation & Data (Month 1)", [
            ("Foundation data loaded: users, locations, departments, groups", "Confirm", "AP-01 Foundation Pack", True),
            ("Assignment rules active and tested", "Confirm", "AP-01", True),
            ("SLA schedules configured and generating SLA records", "Confirm", "AP-01", True),
            ("AD/SSO integration tested (users can log in)", "Confirm", "AP-03 Integration Pack", True),
            ("SCCM or Intune SGC syncing CIs to CMDB", "Confirm", "AP-03 + AP-12", True),
        ]),
        ("CMDB & Discovery (Month 1-2)", [
            ("CSDM service taxonomy approved and populated", "Confirm", "AP-10/11 CMDB Pack", True),
            ("Discovery running on schedule, CI count plausible", "Confirm", "AP-12 Discovery Pack", True),
            ("IRE deduplication rules tested -- no duplicate CIs", "Confirm", "AP-12", True),
            ("MID Server health green (all MID Servers up)", "Confirm", "AP-12", True),
            ("CMDB governance baseline reviewed with CMDB Admin", "Confirm", "AP-10/11", True),
        ]),
        ("ITSM Processes (Month 2)", [
            ("Incident management: creation, routing, SLA, closure tested", "Confirm", "AP-02 ITSM Pack", True),
            ("Major incident process tested with P1 scenario", "Confirm", "AP-02", True),
            ("Problem management: creation, RCA, known error process tested", "Confirm", "AP-02", True),
            ("Change management: standard, normal, emergency flows tested", "Confirm", "AP-02", True),
            ("Service request fulfillment: at least 5 catalog items tested end-to-end", "Confirm", "AP-CAT + AP-02", True),
        ]),
        ("AI & Self-Service (Month 3)", [
            ("Predictive Intelligence: all 3 models active and producing suggestions", "Confirm", "AP-17 PI Pack", True),
            ("Knowledge Base: published articles in at least 2 KBs", "Confirm", "AP-13 Knowledge Pack", True),
            ("Employee Center: live and accessible to all employees", "Confirm", "AP-15 EC Pack", True),
            ("Virtual Agent: all 6 go-live topics passing UAT", "Confirm", "AP-16 VA Pack", True),
            ("Now Assist: 3 skills active and agent-facing", "Confirm", "AP-18 Now Assist Pack", True),
        ]),
        ("Analytics & Reporting (Month 3)", [
            ("PA dashboards: 3 OOTB dashboards live and owners have access", "Confirm", "AP-19 PA Pack", True),
            ("PA data collection confirmed running (check last run)", "Confirm", "AP-19", True),
            ("OOTB reports: all report catalog items accessible to owners", "Confirm", "AP-20 (this pack)", True),
            ("Scheduled report delivery tested for at least 1 report", "Confirm", "AP-20", True),
        ]),
        ("Handover Readiness", [
            ("Customer Admin named and trained for each workstream", "Confirm", "AP-20 WB3", True),
            ("All AP workbook UAT sign-offs complete", "Confirm", "All AP workbooks", True),
            ("Known exceptions documented with remediation plans", "Confirm", "This workbook", True),
            ("Customer IT Director available for sign-off meeting", "Confirm", "Customer PM", True),
        ]),
    ],
    raci_rows=[
        ("Complete stabilization checklist with ECS PM", "R/A", "Joint completion", "ECS PM leads; Customer PM confirms each item."),
        ("Document known exceptions", "R/A", "A (acknowledge in writing)", "ECS documents; Customer PM signs acknowledgment."),
        ("Schedule stabilization sign-off meeting", "R", "A", "ECS PM schedules; Customer IT Director attends."),
        ("Sign stabilization sign-off document", "R (countersign)", "A (primary sign)", "Customer IT Director signs first; ECS PM countersigns."),
    ],
    consultant_guide_sections=[
        ("Known exception handling", "A known exception is not a failure -- it is a documented risk with a plan. Every complex engagement has 2-5 known exceptions at Sprint 6. The failure mode is undocumented exceptions that surface post-handover. Use this checklist to find them all, document them, and get Customer PM acknowledgment in writing."),
        ("Red item escalation", "If a checklist item is red and the customer wants to proceed to handover anyway, get it in writing. The Customer IT Director must sign an exception acknowledgment that states: the gap, the risk, the remediation owner, and the deadline. This protects ECS and gives the customer accountability for the remediation."),
        ("Checklist meeting facilitation", "Run the stabilization checklist review as a joint meeting with ECS PM and Customer PM. Go line by line. For each item, ask: 'Can you confirm this is done?' If the customer cannot confirm, mark it yellow (needs verification) or red (not done). Do not mark anything green based on assumption."),
    ],
    adoption_rows=[
        ("Skip the stabilization checklist -- we trust everything is working",
         "Stabilization checklist is mandatory before sign-off.",
         "Undiscovered gaps surface as post-handover support requests. The checklist protects both ECS and the customer.",
         "The stabilization checklist is the final quality gate. It takes 3-4 hours and has found real issues in every engagement -- a misconfigured SLA, a MID Server that went offline, a report that was not shared to the right role. Those issues are easy to fix before handover and expensive to fix after. We do the checklist.",
         "Non-negotiable -- stabilization checklist is required before sign-off."),
    ],
    snmap_sections=[
        ("Reference Tables", [
            ("All workstream tables", "Each checklist item references the primary ServiceNow table and AP workbook", "See individual AP workbooks for table references"),
            ("Incident, problem, change", "Core ITSM tables -- tested in stabilization check", "incident, problem, change_request"),
            ("cmdb_ci", "CMDB health check -- CI count, Discovery last run", "cmdb_ci"),
        ]),
    ],
)

wb3 = TabContent(
    workbook_title="03 -- Customer Admin Training Plan",
    pack_name=PACK_NAME,
    purpose="Define the training plan, schedule, and competency checklist for all Customer Administrators who will own ServiceNow workstreams post-engagement.",
    who_fills="ECS PM and Customer PM jointly plan. ECS Consultants deliver training. Customer Admins complete competency checklist.",
    sprint_window="Sprint 6 -- all admin training complete by Week 12",
    estimated_effort="Training delivery: 2-4 hours per admin (varies by workstream). Planning: 2 hours.",
    related_workbooks=["02 Stabilization Checklist", "04 Handover & Sign-Off"],
    success_criteria=[
        "One named admin per workstream confirmed and trained.",
        "Each admin has completed their competency checklist independently.",
        "All admins have correct ServiceNow roles and can perform their tasks without ECS assistance.",
        "Escalation path documented for each admin (who to call if stuck).",
    ],
    process_decisions=[
        ("Should training be delivered individually or in a group?",
         "Workstream-specific training delivered individually or in small groups (2-3 admins max per session).",
         "Group training with mixed workstreams reduces depth. Each admin should receive hands-on training in their specific area."),
        ("Should training be recorded?",
         "Yes -- record each training session in the ServiceNow instance (screen recording) and share the recording link with the admin.",
         "Recordings are the post-engagement support safety net. An admin who is stuck 3 months after handover can replay the training session."),
        ("What is the escalation path after ECS handover?",
         "Tier 1: Customer admin self-service (documentation + recordings). Tier 2: ServiceNow Community and documentation. Tier 3: ServiceNow Support (customer must have a support contract).",
         "Document the escalation path explicitly. Admins who do not know where to escalate call ECS -- which is billable T&M post-engagement."),
    ],
    dependencies=[
        ("Customer Admins named for each workstream", "Required", "Customer", "Sprint 6 Wk 1", "Cannot schedule training without named admins."),
        ("Instances stable (not in active configuration change)", "Required", "ECS", "Sprint 6 Wk 1", "Training on an unstable instance is counterproductive."),
    ],
    config_sections=[
        ("Admin Training Schedule", [
            ("ITSM Process Admin", "2 hours -- incident, request, change, problem configuration and reporting", "Customer: [Name]. ECS: [Consultant name]. Sprint 6 Wk 1.", True),
            ("CMDB / Discovery Admin", "3 hours -- Discovery schedule management, IRE rule review, CI governance, MID Server health", "Customer: [Name]. ECS: [Consultant name]. Sprint 6 Wk 1.", True),
            ("Service Catalog Admin", "2 hours -- catalog item maintenance, category management, fulfillment workflow updates", "Customer: [Name]. ECS: [Consultant name]. Sprint 6 Wk 1.", True),
            ("Knowledge Base Admin", "1.5 hours -- article lifecycle, KB structure, access control, search optimization", "Customer: [Name]. ECS: [Consultant name]. Sprint 6 Wk 2.", True),
            ("Employee Center Admin", "1.5 hours -- portal page management, widget configuration, topic taxonomy updates", "Customer: [Name]. ECS: [Consultant name]. Sprint 6 Wk 2.", True),
            ("Virtual Agent Admin", "2 hours -- topic management, utterance tuning, NLU analytics, Phase 2 topic builds", "Customer: [Name]. ECS: [Consultant name]. Sprint 6 Wk 2.", True),
            ("PI / Now Assist Admin", "1.5 hours -- model monitoring, accuracy review, Now Assist skill management", "Customer: [Name]. ECS: [Consultant name]. Sprint 6 Wk 2.", True),
            ("PA / Reporting Admin", "1.5 hours -- dashboard management, indicator thresholds, report sharing, scheduled delivery", "Customer: [Name]. ECS: [Consultant name]. Sprint 6 Wk 2.", True),
            ("HAM / SAM Admin (if in scope)", "2 hours -- asset lifecycle, stockroom management, software reconciliation", "Customer: [Name]. ECS: [Consultant name]. Sprint 6 Wk 1.", True),
        ]),
        ("Competency Checklist (per admin)", [
            ("Admin can navigate to their primary configuration area without ECS guidance", "Pass / Fail", "Assessed during training session", True),
            ("Admin can perform their top 3 routine tasks independently", "Pass / Fail", "ECS observes -- admin performs without prompting", True),
            ("Admin can locate relevant OOTB documentation (ServiceNow Docs, Community)", "Pass / Fail", "Admin demonstrates search during session", True),
            ("Admin has confirmed access to all required ServiceNow roles", "Pass / Fail", "ECS verifies roles in instance", True),
            ("Admin has received training recording link", "Pass / Fail", "ECS shares recording within 24 hours of session", True),
        ]),
        ("Escalation Path", [
            ("Tier 1 (self-service)", "Admin review of training recording + AP workbook documentation", "Available immediately post-engagement", False),
            ("Tier 2 (community)", "ServiceNow Community (community.servicenow.com) and Now Learning", "Free access with customer's ServiceNow account", False),
            ("Tier 3 (ServiceNow Support)", "Customer opens support case via Now Support portal", "Requires active ServiceNow support contract -- customer must confirm", True),
            ("Post-engagement ECS support", "T&M engagement -- contact ECS PM to scope", "Not included in 18-week engagement; billable separately", False),
        ]),
    ],
    raci_rows=[
        ("Name admins for each workstream", "I", "R/A", "Customer IT Director names admins before Sprint 6 Wk 1."),
        ("Schedule and deliver admin training sessions", "R/A", "Attend + complete competency checklist", "ECS delivers; Customer Admins participate."),
        ("Record and share training sessions", "R/A", "I", "ECS records and shares links within 24 hours."),
        ("Verify admin roles in ServiceNow", "R/A", "I", "ECS verifies; Customer Admin confirms access."),
        ("Complete competency checklist", "R (observe)", "A (perform)", "Each admin must perform tasks independently."),
    ],
    consultant_guide_sections=[
        ("Training scheduling", "Book all admin training in Sprint 6 Week 1-2. Do not push training to the final week -- if an admin fails the competency checklist, there is no time to remediate. Two weeks of buffer allows a re-session if needed."),
        ("Competency pass criteria", "An admin passes competency when they can perform their top 3 tasks without being prompted or corrected by ECS. 'I saw you click the wrong menu but then self-correct' is a pass. 'I had to tell you where to go' is a fail requiring another session."),
        ("Escalation path documentation", "The escalation path documentation is the most important artifact for preventing post-engagement support calls from becoming T&M disputes. Be explicit: ECS is not included in the escalation path after handover. ServiceNow Support is Tier 3. Any ECS involvement post-engagement is billable. Get Customer PM acknowledgment of this in the handover sign-off."),
    ],
    adoption_rows=[
        ("We do not have time for training in Sprint 6",
         "Admin training is mandatory -- schedule it in Sprint 6 Week 1, not Week 2.",
         "Untrained admins make configuration changes that break processes. The cost of undoing a bad admin change is higher than 2 hours of training.",
         "Admin training is how we hand over the keys. Without it, the customer owns a ServiceNow instance they cannot maintain. We have seen customers change a single SLA configuration incorrectly and break ticket routing for 200 users. Two hours of training prevents that. We schedule it in Week 1 of Sprint 6 so we have buffer if anyone needs a second session.",
         "Non-negotiable -- admin training is required before handover sign-off."),
    ],
    snmap_sections=[
        ("Admin Roles", [
            ("itil", "ITSM process user role -- incident, request, change, problem management", "sys_user_role"),
            ("cmdb_admin", "CMDB admin -- CI class management, IRE rules, Discovery schedule", "sys_user_role"),
            ("catalog_admin", "Service Catalog admin -- item, category, workflow management", "sys_user_role"),
            ("knowledge_admin", "Knowledge Base admin -- KB structure, article lifecycle, access control", "sys_user_role"),
            ("pa_admin", "Performance Analytics admin -- indicators, thresholds, dashboard sharing", "sys_user_role"),
            ("ml_admin", "Predictive Intelligence admin -- model management, accuracy monitoring", "sys_user_role"),
            ("sn_now_assist.admin", "Now Assist admin -- skill management, content filtering", "sys_user_role"),
        ]),
    ],
)

wb4 = TabContent(
    workbook_title="04 -- Engagement Handover & Sign-Off",
    pack_name=PACK_NAME,
    purpose="Define the formal handover process, sign-off documentation, and transition from ECS delivery to customer-owned operations at the close of the 18-week engagement.",
    who_fills="ECS PM prepares. Customer IT Director and Customer PM sign. ECS PM countersigns.",
    sprint_window="Sprint 6 -- handover complete by end of Week 12",
    estimated_effort="2-3 hours for handover meeting and sign-off documentation",
    related_workbooks=["02 Stabilization Checklist", "03 Admin Training Plan", "05 Phase 2 Readiness"],
    success_criteria=[
        "Stabilization checklist fully green (or known exceptions documented and signed).",
        "All admin training complete with competency sign-offs.",
        "Handover meeting held with Customer IT Director, Customer PM, and ECS PM.",
        "Sign-off document executed by Customer IT Director and ECS PM.",
        "Hypercare period terms confirmed (2 weeks post-sign-off).",
    ],
    process_decisions=[
        ("What does formal handover mean for this engagement?",
         "Handover means: (1) stabilization checklist complete, (2) admin training complete, (3) Customer IT Director signs the engagement completion document, (4) ECS transitions to hypercare mode (2 weeks).",
         "Handover does not mean ECS disappears. Hypercare provides a 2-week buffer for post-launch issues."),
        ("What is included in the 2-week hypercare period?",
         "ECS available for: configuration corrections, SLA/routing troubleshooting, admin guidance on routine tasks. NOT included: new feature builds, new catalog items, new integrations.",
         "Hypercare scope boundaries protect both ECS and the customer from scope creep."),
        ("What happens to open work at handover?",
         "All open items are documented in the known exceptions log and assigned to Customer owners with deadlines. No open ECS-owned items at handover.",
         "ECS must close or formally transfer every open item before sign-off. Handover with open ECS-owned items is not a handover."),
    ],
    dependencies=[
        ("Stabilization checklist complete (WB2)", "Required", "ECS PM", "Sprint 6 Wk 2", "Cannot hand over without stabilization confirmed."),
        ("All admin training complete (WB3)", "Required", "ECS PM", "Sprint 6 Wk 2", "Cannot hand over without trained admins."),
        ("Customer IT Director availability for sign-off meeting", "Required", "Customer PM", "Sprint 6 Wk 2", "Sign-off requires IT Director presence."),
    ],
    config_sections=[
        ("Handover Meeting Agenda", [
            ("Agenda Item 1: Engagement summary (15 min)", "ECS PM presents what was delivered -- AP workbooks, systems live, KPI baselines set", "Slide deck reference: ECS Engagement Summary presentation", False),
            ("Agenda Item 2: Stabilization checklist review (20 min)", "Review green/yellow/red items. Discuss any known exceptions.", "ECS PM leads; Customer PM confirms", False),
            ("Agenda Item 3: Admin training confirmation (10 min)", "Confirm each admin has passed competency checklist", "ECS PM presents admin training summary", False),
            ("Agenda Item 4: Hypercare scope and boundaries (10 min)", "Confirm what is and is not covered in 2-week hypercare", "ECS PM presents hypercare terms", False),
            ("Agenda Item 5: Phase 2 roadmap preview (10 min)", "ECS PM presents Phase 2 opportunities based on engagement learnings", "Reference AP-20 WB5 Phase 2 Readiness", False),
            ("Agenda Item 6: Sign-off (5 min)", "Customer IT Director and ECS PM execute sign-off document", "Physical or DocuSign signature required", False),
        ]),
        ("Sign-Off Document Contents", [
            ("Engagement scope summary", "List of all AP workbooks delivered and accepted", "ECS PM prepares", False),
            ("Systems live at handover", "List of all ServiceNow modules active with go-live dates", "ECS PM prepares", False),
            ("Known exceptions log", "All outstanding items with owner and deadline", "ECS PM + Customer PM jointly prepare", True),
            ("Hypercare period", "Start date, end date, scope, and out-of-scope items", "2 weeks from sign-off date", False),
            ("Customer IT Director signature", "[Customer IT Director name and date]", "Required for handover to be valid", True),
            ("ECS PM countersignature", "[ECS PM name and date]", "ECS PM countersigns after Customer IT Director", False),
        ]),
        ("Post-Handover Contacts", [
            ("Customer primary contact post-handover", "[Customer IT Director name, email, phone]", "For post-engagement T&M engagement", True),
            ("ECS primary contact post-handover", "[ECS PM name, email]", "For Phase 2 scoping and T&M", False),
            ("ServiceNow Support", "support.servicenow.com -- customer must have active support contract", "Customer to confirm support contract is active", True),
        ]),
    ],
    raci_rows=[
        ("Prepare handover meeting agenda and presentation", "R/A", "I", "ECS PM."),
        ("Prepare sign-off document", "R/A", "Review", "ECS PM prepares; Customer PM reviews draft."),
        ("Host handover meeting", "R (host)", "A (attend)", "ECS PM hosts; Customer IT Director + PM attend."),
        ("Execute sign-off document", "R (countersign)", "A (primary sign)", "Customer IT Director signs first."),
        ("Transition to hypercare mode", "R/A", "I", "ECS PM notifies team of hypercare start date."),
    ],
    consultant_guide_sections=[
        ("Sign-off meeting tone", "The handover meeting should feel like a graduation, not a checkout. Open with a summary of what was built together -- the systems live, the KPIs achieved, the admins trained. End with the Phase 2 roadmap preview. The customer should leave feeling accomplished and equipped, not abandoned."),
        ("Known exceptions handling", "If there are known exceptions, present them with their remediation plans and owners. Frame it as: 'Here is what is complete, here is what has a plan.' Never present an exception without a plan. A gap with a plan is a managed risk. A gap without a plan is a failure."),
        ("Hypercare enforcement", "In the first week of hypercare, you will receive requests for new features, new catalog items, and new reports. These are out of scope. Respond to every one with: 'This is a great Phase 2 item -- I will add it to the Phase 2 backlog we will review at [date].' Do not say no -- say 'Phase 2.' The Phase 2 backlog is the most valuable sales document for the next engagement."),
    ],
    adoption_rows=[
        ("We are not ready to sign off -- there are too many open items",
         "Document all open items as known exceptions with plans. Sign off on the engagement with the exception log attached.",
         "Waiting for zero open items before sign-off means the engagement never ends. Known exceptions with plans are the OOTB pattern for complex deployments.",
         "No complex engagement finishes with zero open items. The question is whether each open item has a clear owner, a clear deadline, and a clear remediation plan. If yes, we sign off with the exception log attached -- both parties are on record about what is outstanding. If no, we spend the next hour making sure every item has an owner and a date.",
         "If Customer IT Director refuses to sign with documented exceptions -- escalate to ECS Practice Lead."),
    ],
    snmap_sections=[
        ("Handover Reference", [
            ("ServiceNow Support portal", "support.servicenow.com -- customer submits support cases here", "External: support.servicenow.com"),
            ("ServiceNow Community", "community.servicenow.com -- admin self-service resource", "External: community.servicenow.com"),
            ("Now Learning", "nowlearning.servicenow.com -- training courses for admins", "External: nowlearning.servicenow.com"),
        ]),
    ],
)

wb5 = TabContent(
    workbook_title="05 -- Phase 2 Readiness Assessment",
    pack_name=PACK_NAME,
    purpose="Document the Phase 2 opportunity backlog based on 18-week engagement learnings, deferred items, and new capabilities identified during delivery. Provides the foundation for the next ECS engagement proposal.",
    who_fills="ECS PM compiles based on deferred items logged across all AP workbooks. Customer PM reviews and prioritizes.",
    sprint_window="Sprint 6 -- Phase 2 assessment presented at handover meeting",
    estimated_effort="2-3 hours to compile deferred items from all AP workbooks",
    related_workbooks=["All AP workbooks (Adoption vs. Re-engineering tabs)", "04 Handover & Sign-Off"],
    success_criteria=[
        "All deferred items from AP workbooks compiled into Phase 2 backlog.",
        "Phase 2 items prioritized by customer value (High/Medium/Low).",
        "Indicative effort estimate provided for top 5 Phase 2 items.",
        "Customer PM has reviewed and ranked Phase 2 priorities.",
        "Phase 2 backlog shared with customer as a leave-behind document.",
    ],
    process_decisions=[
        ("How should Phase 2 items be prioritized?",
         "Business value to the customer (High/Medium/Low). High = operational pain point or significant efficiency gain. Medium = nice to have. Low = theoretical benefit.",
         "Customer-facing prioritization drives the next engagement scope. ECS should not unilaterally rank Phase 2 items -- the customer prioritizes based on their operational needs."),
        ("Should Phase 2 include items not on the original blueprint?",
         "Yes -- capture any new requirements that emerged during the 18-week engagement.",
         "Delivery always surfaces requirements that were not in the original scope. These are the highest-value Phase 2 items because they are based on real operational experience, not pre-engagement assumptions."),
        ("Should ECS provide a proposal for Phase 2 at the handover meeting?",
         "No -- provide the Phase 2 backlog and indicative estimates only. Formal proposal is a separate sales activity.",
         "Mixing delivery handover with sales creates awkwardness and potential conflict of interest. The backlog is a gift to the customer; the proposal comes separately."),
    ],
    dependencies=[
        ("All AP workbook Adoption vs. Re-engineering tabs reviewed", "Required", "ECS PM", "Sprint 6 Wk 2", "Every deferred item from every AP workbook is a Phase 2 candidate."),
    ],
    config_sections=[
        ("Phase 2 Backlog -- AI & Self-Service", [
            ("VA: Teams/Slack channel integration", "High", "2-3 sprints. Requires Azure AD app registration and bot configuration.", False),
            ("VA: Topic library expansion (7-15 additional topics)", "High", "1-2 sprints per 5 topics. Data-driven from unhandled intent report.", False),
            ("PI: Agent-level Assignment Intelligence", "Medium", "1 sprint. Requires 6+ months of group-level accuracy baseline.", False),
            ("PI: Predictive Fields (custom field prediction)", "Medium", "1-2 sprints. Each custom field is a separate ML Solution.", False),
            ("Now Assist: GenAI for Change (change assessment)", "Medium", "1 sprint. Requires mature Change Management process.", False),
            ("Now Assist: AI Search corpus expansion (SharePoint connector)", "High", "2-3 sprints. Requires SharePoint Online connector and content governance.", False),
            ("Now Assist: Auto-generation mode (all skills)", "Low", "1 sprint. Enable after 90-day on-demand baseline proven.", False),
        ]),
        ("Phase 2 Backlog -- ITSM & Platform", [
            ("ITSM: CSM (Customer Service Management) for external-facing requests", "Medium", "4-6 sprints. Significant scope -- separate engagement.", False),
            ("Catalog: Additional catalog items (beyond go-live set)", "High", "0.5 sprint per 10 items. Customer-driven -- use unmet request data.", False),
            ("Integration: ACD handoff for VA (Genesys/Five9)", "Low", "3-4 sprints. Requires ACD vendor engagement and middleware.", False),
            ("CMDB: Cloud CIs via AWS/Azure SGC", "High", "1-2 sprints. OOTB SGC connectors -- high value if cloud-heavy environment.", False),
            ("Event Management: Alert consolidation and correlation", "Medium", "3-4 sprints. Was descoped from 18-week engagement.", False),
        ]),
        ("Phase 2 Backlog -- Analytics & Reporting", [
            ("PA: Custom indicator library (FCR by team, SLA by category)", "High", "1-2 sprints. Builds on 6-month OOTB baseline.", False),
            ("PA: Department-level dashboards (HR, Finance, Facilities)", "Medium", "1 sprint per department. Requires ITSM usage data per department.", False),
            ("PA: AI-assisted forecasting with Now Assist", "Low", "2-3 sprints. Requires 12+ months of PA trend data.", False),
            ("Reporting: SharePoint / Power BI integration", "Medium", "2-3 sprints. Requires Power BI connector and data governance review.", False),
        ]),
        ("Phase 2 Effort Estimates (Top 5 by Customer Priority)", [
            ("Priority 1 (Customer to complete)", "[Item name]", "[Indicative sprints]", True),
            ("Priority 2 (Customer to complete)", "[Item name]", "[Indicative sprints]", True),
            ("Priority 3 (Customer to complete)", "[Item name]", "[Indicative sprints]", True),
            ("Priority 4 (Customer to complete)", "[Item name]", "[Indicative sprints]", True),
            ("Priority 5 (Customer to complete)", "[Item name]", "[Indicative sprints]", True),
        ]),
    ],
    raci_rows=[
        ("Compile deferred items from all AP workbooks", "R/A", "I", "ECS PM compiles Phase 2 backlog."),
        ("Add new requirements surfaced during delivery", "R/A", "I", "ECS Consultants contribute workstream-specific items."),
        ("Prioritize Phase 2 backlog (High/Medium/Low)", "I (facilitate)", "R/A (decide)", "Customer PM prioritizes with ECS PM facilitation."),
        ("Present Phase 2 backlog at handover meeting", "R/A", "Receive", "ECS PM presents; Customer PM takes as leave-behind."),
        ("Formal Phase 2 proposal", "N/A (separate sales activity)", "N/A", "Formal proposal is separate from handover -- do not conflate."),
    ],
    consultant_guide_sections=[
        ("Phase 2 backlog as sales asset", "The Phase 2 backlog is the most valuable sales document that comes out of an 18-week engagement. It is grounded in real experience with the customer's environment, real operational pain points, and real deferred requirements. Every item on the backlog is a justified opportunity. Share it generously -- the customer views it as a roadmap, ECS views it as a pipeline."),
        ("Prioritization facilitation", "When facilitating Phase 2 prioritization, ask: 'Which of these items, if delivered, would most improve your team's daily operations?' This is more productive than asking 'which do you want most' -- operational pain drives honest prioritization. The IT Director's top priority is almost always different from the Service Desk Manager's. Capture both perspectives."),
        ("Indicative estimates", "Indicative estimates are ranges, not commitments. 'This is a 2-3 sprint item' gives the customer enough to budget-plan without creating a contractual obligation. Always include the caveat: 'These estimates assume an OOTB-first approach. Custom development would add scope.'"),
    ],
    adoption_rows=[
        ("We want to start Phase 2 immediately -- skip the stabilization period",
         "2-week stabilization period is required before Phase 2 begins.",
         "Starting Phase 2 configuration before the go-live platform stabilizes introduces dependency risks and makes defect isolation nearly impossible.",
         "The 2-week stabilization period is when we watch the live data and confirm everything is working as designed. Starting Phase 2 during this window means we might be building on top of a misconfiguration that has not surfaced yet. Two weeks is a small investment to ensure Phase 2 is built on a solid foundation.",
         "Phase 2 begins after 2-week stabilization hypercare period closes."),
    ],
    snmap_sections=[
        ("Phase 2 Reference", [
            ("All AP workbook Adoption vs. Re-engineering tabs", "Source of all deferred items -- compile from each workbook", "See individual AP workbooks"),
            ("ServiceNow Product Roadmap", "docs.servicenow.com -- future OOTB capabilities to include in Phase 2 planning", "External: docs.servicenow.com"),
        ]),
    ],
)

def build_readme():
    meta = DocMeta(
        eyebrow="ACCELERATOR PACK",
        title="Reporting & Stabilization\nAccelerator Pack",
        subtitle="OOTB Reports, Stabilization Checklist, Admin Training, Handover & Phase 2 Readiness",
        doc_id="AP-20",
        version="1.0",
        status="Released",
        audience="ECS PM (Internal) + Customer IT Director / Customer PM (shared workbooks)",
        running_header_label="Reporting & Stabilization Accelerator Pack · ECS Federal",
        confidentiality="Internal Use Only · Confidential",
    )
    doc = EcsDocument(meta=meta)
    doc.add_cover_page()
    doc.h1("Pack Overview")
    doc.para(
        "AP-20 closes the 18-week ECS OOTB engagement. It covers the OOTB report catalog "
        "built during delivery, the definitive stabilization checklist across all workstreams, "
        "the customer admin training plan, formal engagement handover and sign-off, and the "
        "Phase 2 opportunity backlog. This pack is the final deliverable of every ECS OOTB "
        "engagement and the bridge to the next phase of the customer relationship."
    )
    doc.h1("Workbook Inventory")
    doc.table(
        headers=["#", "Workbook", "Owner", "Sprint"],
        rows=[
            ("WB1", "OOTB Report Catalog", "ECS Consultant", "Sprint 6"),
            ("WB2", "Stabilization Checklist", "ECS PM + Customer PM", "Sprint 6"),
            ("WB3", "Customer Admin Training Plan", "ECS PM + Customer PM", "Sprint 6"),
            ("WB4", "Engagement Handover & Sign-Off", "ECS PM + Customer IT Director", "Sprint 6"),
            ("WB5", "Phase 2 Readiness Assessment", "ECS PM + Customer PM", "Sprint 6"),
        ],
    )
    doc.h1("Key Principles for Engagement Close")
    doc.para(
        "Stabilization is mandatory before handover -- the checklist (WB2) is the gate. "
        "Admin training (WB3) must be complete before sign-off -- no untrained admins at handover. "
        "Known exceptions are acceptable with documented remediation plans and Customer IT Director acknowledgment. "
        "Hypercare (2 weeks) covers corrections to existing configuration only -- new builds are Phase 2. "
        "Phase 2 backlog (WB5) is built from every deferred item logged in the Adoption vs. Re-engineering "
        "tabs of all AP workbooks -- compile it before the handover meeting."
    )
    out = os.path.join(PACK_DIR, "00_README_Reporting_Stabilization_Pack.docx")
    doc.save(out)
    print(f"README saved: {out}")

if __name__ == "__main__":
    print("Building Reporting & Stabilization Accelerator Pack...")
    workbooks = [
        ("01_ootb_report_catalog.xlsx", wb1),
        ("02_stabilization_checklist.xlsx", wb2),
        ("03_admin_training_plan.xlsx", wb3),
        ("04_handover_signoff.xlsx", wb4),
        ("05_phase2_readiness.xlsx", wb5),
    ]
    for filename, content in workbooks:
        build_workbook(content, os.path.join(PACK_DIR, filename))
        print(f"  check {filename}")
    build_readme()
    print("Reporting & Stabilization Accelerator Pack complete.")
