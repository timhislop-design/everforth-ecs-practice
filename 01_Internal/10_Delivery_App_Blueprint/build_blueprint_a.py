"""
build_blueprint_a.py — ECS Delivery Intelligence Platform Blueprint A (Custom App)
Rebuilt with canonical ECS Federal branding via ecs_template.py
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
OUT  = os.path.join(HERE, "ECS_DeliveryApp_Blueprint_A_CustomApp_INTERNAL.docx")

doc = EcsDocument(
    meta=DocMeta(
        eyebrow="INTERNAL · ARCHITECTURAL BLUEPRINT — FOR REVIEW WITH DIRECTOR OF TECHNICAL SERVICES",
        title="ECS Delivery Intelligence Platform\nBlueprint A — Full Custom Application",
        subtitle="ServiceNow Scoped Application Architecture · Living Delivery Platform · Role-Based Portal · Native Module Integration",
        audience="Director of Technical Services (Shawn), Senior Director, Lead Developer",
        companion_to="Blueprint B (Table Extends) · Executive Briefing A · Arch Rationale · Project Plan xlsx",
        doc_id="INT-DA-BP-A",
        version="1.0 Draft",
        status="For Architecture Review",
        confidentiality="Internal Use Only · Confidential",
        running_header_label="Internal · Blueprint A — Full Custom Application",
    ),
    logo_path=LOGO,
)

doc.add_cover_page()
doc.page_break()

# ── 1. EXECUTIVE SUMMARY ────────────────────────────────────────────────────
doc.h1("Executive Summary")
doc.para(
    "This blueprint defines the architecture for the ECS Delivery Intelligence Platform — a ServiceNow scoped "
    "application built and owned by Everforth that transforms how we deliver, measure, and demonstrate value "
    "during every ECS OOTB engagement."
)
doc.para(
    "The platform replaces disconnected spreadsheets, static documents, and manual status updates with a "
    "living, record-driven system that surfaces real sprint health, customer transparency, and delivery "
    "accountability — all inside the ServiceNow instance the customer is already using. It is not a document "
    "repository. It is an operational platform that treats delivery methodology the same way ServiceNow treats "
    "IT operations: as structured data, governed workflow, and measurable outcomes."
)
doc.callout(
    "Strategic Intent: Every ECS engagement leaves the customer with two things — a configured ServiceNow "
    "platform and a delivery audit trail they can show their leadership. The app is the proof that we operate "
    "the way we say we do."
)
doc.table(
    headers=["Dimension", "This Blueprint"],
    rows=[
        ["Application Type",   "ServiceNow Scoped Application — custom tables, custom portal, native module integration"],
        ["Deployment Model",   "Installed on customer instance per engagement; portable as update set or Store app"],
        ["Target Audience",    "Everforth consultants (internal) + customer stakeholders (portal-only access)"],
        ["Data Strategy",      "Custom tables + native Agile, SPM, Knowledge, Catalog table integration"],
        ["Dashboard Approach", "Performance Analytics (PA) + native platform reporting for health scoring"],
        ["Commercial Path",    "Engagement deliverable initially; ServiceNow Store ISV app as the long-term target"],
        ["Review Decision",    "Full custom vs. Table Extends (Blueprint B) — to be resolved with Director of Technical Services"],
    ],
    col_widths_in=[2.0, 7.36],
)

# ── 2. VISION ───────────────────────────────────────────────────────────────
doc.h1("Vision — What We Are Building")
doc.para(
    "The ECS Delivery Intelligence Platform is the operational backbone of every engagement. It gives three "
    "groups exactly what they need, in one place, without anyone updating a spreadsheet."
)
doc.h2("2.1  The Consultant Experience")
doc.para(
    "A consultant arriving at Sprint 3 should not have to open five documents to understand where the "
    "engagement stands. They log in, see their role-based landing page, and find: what is due this sprint, "
    "what decisions are open, where the health indicators are yellow, and what methodology content applies "
    "to today's work. The app is their guided workflow, not a filing cabinet."
)
doc.h2("2.2  The Delivery Manager Experience")
doc.para(
    "The delivery manager stops filling in RAG status spreadsheets. Instead, they review a dashboard that "
    "calculates health from real data: sprint completion rate from Agile, milestone variance from SPM, open "
    "risk count from the risk register, SLA compliance from ITSM. When a sponsor asks 'how are we doing?' "
    "the answer is a live URL, not a PowerPoint exported last Thursday."
)
doc.h2("2.3  The Customer Stakeholder Experience")
doc.para(
    "The customer project sponsor and process owners get portal-only access to a view designed for them. "
    "They see what is coming this sprint, what decisions they need to make, what the current health score is, "
    "and a summary of completed work. They do not see consultant internal notes, tooling configuration, or "
    "anything that is not relevant to their role. This level of transparency builds trust and reduces the "
    "noise of weekly status emails."
)
doc.callout(
    "What replaces the spreadsheets: Sprint health trackers become PA dashboards reading from Agile sprint "
    "records. Risk logs become structured Risk/Issue records with workflow. Decision trackers become Decision "
    "records tied to sprint gates. Project milestone trackers become SPM milestone views. None of these "
    "require manual updates — they derive from work already being done in the platform."
)

# ── 3. APPLICATION ARCHITECTURE OVERVIEW ─────────────────────────────────────
doc.h1("Application Architecture Overview")
doc.para(
    "The application is built as a ServiceNow scoped application using standard Studio-based development. "
    "It is self-contained within its own application scope, which means it can be packaged as an update set "
    "and installed on any customer instance without polluting the global scope. The architecture has four layers."
)
doc.table(
    headers=["Layer", "What It Contains", "ServiceNow Technology"],
    rows=[
        ["Data Layer",         "Engagement records, health metrics, risks, decisions, milestones, methodology content", "Custom scoped tables + extensions of native tables"],
        ["Integration Layer",  "Real-time reads from Agile (stories/sprints), SPM (milestones/projects), ITSM, KB", "GlideRecord queries, Table API, PA data sources"],
        ["Logic Layer",        "Health scoring engine, gate pass/fail logic, escalation rules, notification triggers", "Business Rules, Flow Designer, Scheduled Jobs"],
        ["Presentation Layer", "Role-based Service Portal pages, PA dashboards, Virtual Agent topics", "Service Portal, Performance Analytics, NLU/VA"],
    ],
    col_widths_in=[1.8, 4.2, 3.36],
)
doc.h2("3.1  Scoped Application Identity")
doc.table(
    headers=["Property", "Value"],
    rows=[
        ["Application Name",   "ECS Delivery Intelligence Platform"],
        ["Application Scope",  "x_everforth_ecs_dip"],
        ["Vendor",             "Everforth"],
        ["Version",            "1.0.0 (initial engagement deliverable)"],
        ["Deployment Method",  "Update Set or ServiceNow Store (ISV path)"],
        ["Target Instance",    "Customer instance — installed per engagement"],
        ["Access Model",       "Role-based: ecs_consultant, ecs_delivery_mgr, ecs_customer_viewer"],
    ],
    col_widths_in=[2.0, 7.36],
)
doc.h2("3.2  Key Design Principles")
doc.bullet("Platform-native: use ServiceNow capabilities first, custom code only when necessary")
doc.bullet("Record-driven: every status, health metric, and decision is a record, not a cell in a spreadsheet")
doc.bullet("Role-aware: every view is filtered and scoped to the logged-in user's role and engagement")
doc.bullet("Portable: the app installs on any instance with no external dependencies")
doc.bullet("Auditable: all state changes are tracked in the ServiceNow audit log automatically")
doc.bullet("Extensible: new workstreams (HAM, SAM, CMDB) can be added as configuration, not code changes")

# ── 4. CUSTOM DATA MODEL ─────────────────────────────────────────────────────
doc.h1("Custom Data Model")
doc.para(
    "The following custom tables form the core data layer. All are created within the x_everforth_ecs_dip "
    "application scope. Each table uses ServiceNow's standard audit, ACL, and workflow capabilities automatically."
)
doc.h2("4.1  Core Custom Tables")
doc.h3("ECS Engagement [x_everforth_ecs_dip_engagement]")
doc.para("The master record for each customer engagement. One per implementation. All other records relate back to this.")
doc.table(
    headers=["Field", "Type", "Purpose"],
    rows=[
        ["Engagement Name",  "String",                  "Customer name + engagement identifier"],
        ["Customer Account", "Reference → Account",     "Links to CRM/customer record"],
        ["Start Date",       "Date",                    "Engagement kick-off date"],
        ["Target Go-Live",   "Date",                    "Planned go-live date"],
        ["Current Phase",    "Choice",                  "Sprint 0, Sprint 1–6, Hypercare"],
        ["Overall Health",   "Calculated",              "Derived: red/yellow/green from health score"],
        ["Health Score",     "Integer",                 "0–100, calculated by scheduled job"],
        ["Delivery Manager", "Reference → User",        "Everforth DM assigned to engagement"],
        ["Lead Architect",   "Reference → User",        "Everforth architect"],
        ["Executive Sponsor","Reference → User",        "Customer sponsor (portal access)"],
        ["SPM Project",      "Reference → pm_project",  "Links to Strategic Portfolio Mgmt record"],
        ["Agile Backlog",    "Reference → rm_sprint_backlog", "Links to Agile backlog for this engagement"],
    ],
    col_widths_in=[2.0, 2.0, 5.36],
)
doc.h3("Sprint Gate [x_everforth_ecs_dip_sprint_gate]")
doc.para("One record per sprint per engagement. Tracks gate criteria and pass/fail status.")
doc.table(
    headers=["Field", "Type", "Purpose"],
    rows=[
        ["Engagement",        "Reference → Engagement", "Parent engagement"],
        ["Sprint Number",     "Choice (0–6, Hypercare)", "Which sprint"],
        ["Sprint Start",      "Date",                   "Actual start date"],
        ["Sprint End",        "Date",                   "Actual end date"],
        ["Gate Status",       "Choice",                 "Open, At Risk, Passed, Failed"],
        ["Stories Committed", "Integer",                "Pulled from Agile at sprint start"],
        ["Stories Completed", "Calculated",             "Live count from Agile"],
        ["Velocity %",        "Calculated",             "Completed ÷ Committed × 100"],
        ["Open Risks",        "Calculated",             "Count of open Risk records for this sprint"],
        ["Open Decisions",    "Calculated",             "Count of open Decision records"],
        ["Gate Sign-Off",     "Reference → User",       "Customer sign-off on gate"],
        ["Sign-Off Date",     "Date",                   "When gate was approved"],
        ["Notes",             "Journal",                "Delivery manager notes"],
    ],
    col_widths_in=[2.0, 2.0, 5.36],
)
doc.h3("Risk & Issue [x_everforth_ecs_dip_risk]")
doc.table(
    headers=["Field", "Type", "Purpose"],
    rows=[
        ["Title",            "String",                   "Short description of risk or issue"],
        ["Type",             "Choice: Risk / Issue",     "Distinguishes proactive vs. active"],
        ["Sprint Gate",      "Reference → Sprint Gate",  "Which sprint this was raised in"],
        ["Engagement",       "Reference → Engagement",   "Parent engagement"],
        ["Probability",      "Choice: Low/Med/High",     "For risks only"],
        ["Impact",           "Choice: Low/Med/High",     "Severity if realized"],
        ["Owner",            "Reference → User",         "Who is resolving it"],
        ["Status",           "Choice",                   "Open, Mitigated, Closed, Escalated"],
        ["Mitigation Plan",  "String",                   "Documented mitigation steps"],
        ["Due Date",         "Date",                     "Target resolution date"],
    ],
    col_widths_in=[2.0, 2.0, 5.36],
)
doc.h3("Decision Record [x_everforth_ecs_dip_decision]")
doc.table(
    headers=["Field", "Type", "Purpose"],
    rows=[
        ["Decision Required",  "String",                   "What needs to be decided"],
        ["Workstream",         "Choice",                   "ITSM, Catalog, CMDB, HAM, VA, etc."],
        ["Sprint Gate",        "Reference → Sprint Gate",  "Sprint in which decision is needed"],
        ["Decision Owner",     "Reference → User",         "Customer stakeholder who must decide"],
        ["Options Presented",  "String",                   "OOTB option vs. alternatives offered"],
        ["Decision Made",      "String",                   "Recorded outcome"],
        ["Status",             "Choice",                   "Open, Decided, Deferred, Escalated"],
        ["Impact if Deferred", "String",                   "What delays if not resolved"],
        ["Date Decided",       "Date",                     "When the decision was made"],
    ],
    col_widths_in=[2.0, 2.0, 5.36],
)
doc.h3("Methodology Content [x_everforth_ecs_dip_content]")
doc.para(
    "Stores methodology articles, how-to guides, and accelerator pack references. Rendered through the "
    "role-based portal. Tagged by role, sprint phase, and workstream so the right content surfaces automatically."
)
doc.table(
    headers=["Field", "Type", "Purpose"],
    rows=[
        ["Title",             "String",         "Content title"],
        ["Content Type",      "Choice",         "How-To Guide, Accelerator Pack, Decision Guide, Workshop Pre-Read, Cheatsheet"],
        ["Workstream",        "Choice (multi)", "Which workstreams this applies to"],
        ["Applicable Sprint", "Choice (multi)", "Sprint 0, 1, 2, 3, 4, 5, 6"],
        ["Target Role",       "Choice (multi)", "Delivery Manager, Architect, Consultant, Customer Sponsor, Process Owner"],
        ["Audience",          "Choice",         "Internal / Customer / Both"],
        ["Body",              "HTML",           "Rich text content"],
        ["Attachment",        "Attachment",     "Link to source docx/xlsx in this pack"],
        ["Version",           "String",         "Content version for change tracking"],
    ],
    col_widths_in=[2.0, 2.0, 5.36],
)

# ── 5. ROLE FRAMEWORK ───────────────────────────────────────────────────────
doc.h1("Role Framework")
doc.para(
    "The application defines distinct roles that control access, portal views, and notification behaviour. "
    "Roles are granted at the engagement level, not globally, so consultants only see the engagements they "
    "are assigned to."
)
doc.h2("5.1  Internal Roles (Everforth Staff)")
doc.table(
    headers=["Role", "SNow Role Name", "What They See & Can Do"],
    rows=[
        ["Practice Leader",  "ecs_practice_leader",  "All engagements, practice-level health roll-up, benchmarking across customers, content management"],
        ["Delivery Manager", "ecs_delivery_mgr",     "Their engagements: full edit on Sprint Gates, Risks, Decisions; health dashboard; customer portal preview"],
        ["Lead Architect",   "ecs_architect",        "Their engagements: technical decision records, workstream health, how-to content for their workstreams"],
        ["Consultant",       "ecs_consultant",       "Their sprint tasks, relevant methodology content filtered by sprint and workstream, read on sprint health"],
    ],
    col_widths_in=[1.8, 2.2, 5.36],
)
doc.h2("5.2  Customer Roles (Portal Access Only)")
doc.table(
    headers=["Role", "SNow Role Name", "What They See & Can Do"],
    rows=[
        ["Executive Sponsor", "ecs_customer_sponsor",  "Engagement health summary, milestone status, sprint gate approvals, escalated risks — executive view"],
        ["Project Owner",     "ecs_customer_pm",       "Sprint-level detail, decision records requiring their input, risk log, upcoming commitments"],
        ["Process Owner",     "ecs_customer_process",  "Workstream-specific content, decisions in their area, workshop pre-read materials for their process"],
        ["End User",          "ecs_customer_user",     "Read-only: sprint schedule, upcoming changes, knowledge articles relevant to their role"],
    ],
    col_widths_in=[1.8, 2.2, 5.36],
)
doc.callout(
    "Licensing note: Customer roles are portal-only. They require a ServiceNow Requester or Customer Portal "
    "license, not a full platform seat. This is the lowest-cost access tier. Confirm specific entitlement "
    "with the customer's ServiceNow contract before assigning portal roles."
)

# ── 6. ROLE-BASED PORTAL DESIGN ──────────────────────────────────────────────
doc.h1("Role-Based Portal Design")
doc.para(
    "The portal is the face of the platform. Each role sees a different landing page — same underlying data, "
    "different filters and emphasis. All portal pages are built on ServiceNow's Service Portal framework."
)
doc.h2("6.1  Consultant Landing Page")
doc.bullet("Current sprint banner: sprint number, start/end dates, velocity % updated in real time")
doc.bullet("My open tasks: stories assigned to me from the Agile board, filtered to this sprint")
doc.bullet("My content: methodology guides, how-to docs, cheatsheets — filtered by my role and current sprint")
doc.bullet("Open decisions: decisions in my workstream needing input, with a direct link to the decision record")
doc.bullet("Quick access: accelerator pack templates for the current workstream and sprint")
doc.h2("6.2  Delivery Manager Dashboard")
doc.bullet("Engagement health card: overall health score (0–100) with RAG indicator, trend vs. last sprint")
doc.bullet("Sprint gate status: all six gates shown as a visual timeline with pass/at-risk/open status")
doc.bullet("Risk & issue summary: count by status and severity, oldest open risk highlighted")
doc.bullet("Decision tracker: count of open decisions, overdue decisions flagged in red")
doc.bullet("Velocity chart: committed vs. completed stories per sprint (PA chart from Agile data)")
doc.bullet("Customer portal preview: toggle to see exactly what the sponsor sees before they log in")
doc.bullet("Quick actions: add risk, add decision, trigger gate sign-off request")
doc.h2("6.3  Customer Sponsor View")
doc.bullet("Engagement progress: visual timeline showing which sprint we are in and what is coming")
doc.bullet("Health score: plain-language summary — 'Engagement is on track' or 'One item needs your attention'")
doc.bullet("Decisions awaiting your input: prominent call-to-action for any pending decision records")
doc.bullet("Completed this sprint: bullet summary of what was delivered (auto-generated from closed stories)")
doc.bullet("Upcoming commitments: what the customer team needs to provide in the next sprint")
doc.bullet("Gate approval: one-click approval when the sprint gate sign-off is requested")
doc.h2("6.4  Customer Process Owner View")
doc.bullet("My workstream health: ITSM, CMDB, HAM, Catalog — filtered to their area only")
doc.bullet("Workshop pre-reads: documents relevant to upcoming workshops surfaced automatically by sprint")
doc.bullet("Decisions in my area: any open decisions tagged to their workstream")
doc.bullet("Knowledge articles: OOTB methodology articles relevant to their process")
doc.bullet("What's been built: completed work items tagged to their workstream, readable summary")

# ── 7. LIVING PROJECT HEALTH ──────────────────────────────────────────────────
doc.h1("Living Project Health — Replacing the Spreadsheets")
doc.para(
    "This section maps every recurring manual spreadsheet to its replacement record type and explains how "
    "the health score is calculated automatically from real data."
)
doc.h2("7.1  Spreadsheet-to-Record Mapping")
doc.table(
    headers=["Current Spreadsheet", "Replaced By", "Data Source"],
    rows=[
        ["Weekly RAG Status Report",   "Engagement Health Card (portal)", "Calculated from sprint velocity, risk count, open decisions, milestone variance"],
        ["Sprint Tracking Worksheet",  "Sprint Gate record + Agile board", "Stories committed/completed live from Agile Development module"],
        ["Risk & Issue Log",           "Risk/Issue records with workflow", "Created in app, status tracked in ServiceNow audit log"],
        ["Decision Log",               "Decision records tied to sprint gates", "Workflow sends reminders to decision owner; escalates on due date"],
        ["Milestone Tracker",          "SPM Project milestones", "Milestones defined in Strategic Portfolio Management, linked to engagement"],
        ["Velocity Chart",             "PA chart: stories by sprint", "Performance Analytics reads Agile story records directly"],
        ["Customer Readiness Checklist","Sprint Gate criteria records", "Gate pass/fail criteria defined as records; sign-off triggers approval workflow"],
        ["Project Health Summary",     "Health Score (0–100) on Engagement", "Scheduled job recalculates nightly: velocity (40%) + risks (30%) + decisions (20%) + milestone (10%)"],
    ],
    col_widths_in=[2.2, 2.4, 4.76],
)
doc.h2("7.2  Health Score Calculation")
doc.para("The Engagement Health Score is recalculated nightly by a scheduled job. The score drives the RAG indicator shown to all roles.")
doc.table(
    headers=["Component", "Weight", "Calculation Logic"],
    rows=[
        ["Sprint Velocity",   "40%", "Average story completion rate across all sprints to date. 100% = full weight."],
        ["Risk Posture",      "30%", "Starts at full score, deducted for open high risks (−15 each), open medium risks (−5 each)."],
        ["Decision Latency",  "20%", "Deducted for decisions overdue by more than 5 days (−10 each) or escalated (−15 each)."],
        ["Milestone Variance","10%", "SPM milestone date variance. No variance = full weight; each week late = −5 points."],
        ["RAG Threshold",     "N/A", "Green ≥ 80 | Yellow 60–79 | Red < 60"],
    ],
    col_widths_in=[2.0, 0.8, 6.56],
)
doc.h2("7.3  Audit Trail")
doc.para(
    "Because every health indicator derives from ServiceNow records, the audit trail is automatic. Every risk "
    "status change, decision update, story completion, and gate sign-off is recorded in the ServiceNow audit "
    "log with timestamp and user. At engagement close, the complete delivery history is available for internal "
    "review, post-engagement analysis, and customer handoff. No manual documentation required."
)

# ── 8. NATIVE MODULE INTEGRATION ─────────────────────────────────────────────
doc.h1("Native Module Integration")
doc.para(
    "The platform does not replicate functionality that ServiceNow already provides. It reads from native "
    "modules and surfaces their data in a delivery context."
)
doc.table(
    headers=["Module", "What We Read", "How We Use It"],
    rows=[
        ["Agile Development (rm_story, rm_sprint)", "Stories, sprints, backlog, velocity", "Sprint Gate auto-populates committed/completed counts. Velocity chart on DM dashboard. Story list on consultant landing page."],
        ["Strategic Portfolio Management (pm_project, pm_milestone)", "Project milestones, task completion, resource allocation", "Milestone records linked to Engagement. Variance drives 10% of health score. Sponsor sees milestone timeline on portal."],
        ["ITSM (incident, problem, change_request)", "Open tickets against the customer instance", "Included in health scoring during Hypercare. Incident volume shown on customer sponsor view as 'platform stability' indicator."],
        ["Knowledge Base (kb_knowledge)", "OOTB methodology articles we have published", "Methodology Content table references KB articles. Portal surfaces relevant articles by role and sprint. VA uses KB as answer source."],
        ["Service Catalog (sc_cat_item)", "Catalog items built during delivery", "Completed catalog items shown on 'what we built' view. Count tracked as a delivery metric per sprint."],
        ["Performance Analytics (pa_job, pa_widget)", "Live PA data for dashboard widgets", "All health trend charts use PA widgets embedded in the Service Portal. No static screenshots."],
        ["Virtual Agent (va_topic, NLU model)", "Conversation topics for guidance", "VA topics answer 'what do I need to do in Sprint 3?' and route to content, decisions, or risk records."],
    ],
    col_widths_in=[2.4, 2.0, 5.0],
)
doc.callout(
    "PA Licensing note: Performance Analytics (PA) is a separately licensed ServiceNow product. If a customer "
    "does not have PA, health trend charts fall back to native platform reporting and list views. Core health "
    "scoring is unaffected — it runs from calculated fields, not PA. Confirm PA availability during Sprint 0 discovery."
)

# ── 9. SERVICENOW STORE PATH ──────────────────────────────────────────────────
doc.h1("ServiceNow Store Path")
doc.para(
    "Publishing to the ServiceNow Store is the preferred long-term commercial model. This section outlines "
    "requirements, timeline, and what must be decided before committing to the Store path."
)
doc.h2("9.1  ISV Program Requirements")
doc.bullet("Everforth must be enrolled in the ServiceNow Technology Partner Program (or ISV program)")
doc.bullet("Application must pass automated ATF (Automated Testing Framework) test suite — minimum 80% coverage")
doc.bullet("Application must pass ServiceNow security review — no hardcoded credentials, scoped ACLs, no global scope writes")
doc.bullet("Application must meet Now Platform UX standards for Store listing")
doc.bullet("Version control via ServiceNow Studio source control (GitHub integration recommended)")
doc.bullet("Formal support model must be documented (SLA for defect resolution)")
doc.h2("9.2  Certification Timeline Estimate")
doc.table(
    headers=["Phase", "Estimated Duration", "Key Activities"],
    rows=[
        ["Partner enrollment",       "4–6 weeks",  "Complete ISV/Technology Partner application, legal review of partner agreement"],
        ["v1.0 development on PDI",  "8–12 weeks", "Build on Personal Developer Instance, write ATF tests, internal QA"],
        ["Pre-certification scan",   "2 weeks",    "Run ServiceNow's internal scanner, fix flagged issues"],
        ["ServiceNow security review","4–6 weeks", "ServiceNow team reviews app; typical 1–2 remediation cycles"],
        ["Store listing & launch",   "2–3 weeks",  "Write listing, screenshots, pricing, submit for approval"],
        ["Total",                    "20–29 weeks","Parallel with engagement delivery work; not a blocker for first use"],
    ],
    col_widths_in=[2.4, 1.6, 5.36],
)
doc.h2("9.3  Near-Term Distribution (Pre-Store)")
doc.para(
    "While the Store certification process runs, the application is distributed as an update set installed "
    "directly on each customer instance by the delivery team during Sprint 0. This requires no partner "
    "program enrollment and can begin immediately. The update set approach has one constraint: updates to "
    "the app must be manually pushed to each customer instance. Plan for a quarterly update cadence per engagement."
)

# ── 10. IMPLEMENTATION SEQUENCE ──────────────────────────────────────────────
doc.h1("Implementation Sequence")
doc.para(
    "The platform is built in four phases. The first phase produces a usable v0.5 that can be installed "
    "on the next engagement. Each phase adds capability without breaking what was built before."
)
doc.table(
    headers=["Phase", "Duration", "Deliverables", "Milestone"],
    rows=[
        ["Phase 1 — Foundation",     "4–5 weeks", "App scope, all custom tables, basic CRUD UI, role setup, update set packaging, Engagement + Sprint Gate records", "v0.5: installable on first real engagement"],
        ["Phase 2 — Portal & Health","4–5 weeks", "Service Portal pages for all roles, health score calculation, Risk and Decision records, basic list/form views, portal access for customers", "v0.7: usable by customer stakeholders"],
        ["Phase 3 — Integrations",   "3–4 weeks", "Agile and SPM live integration, velocity chart, milestone linking, Virtual Agent topics for content discovery, PA widgets for DM dashboard", "v0.9: replaces all spreadsheets"],
        ["Phase 4 — Content & Polish","3–4 weeks","Methodology Content table populated from existing collateral, content tagging by role/sprint/workstream, Store prep, ATF test suite, documentation", "v1.0: Store-ready, commercially distributable"],
    ],
    col_widths_in=[2.2, 0.9, 4.0, 2.26],
)
doc.h2("10.1  Resource Model")
doc.table(
    headers=["Role", "Phase 1", "Phase 2", "Phase 3", "Phase 4"],
    rows=[
        ["Lead Architect / App Developer",   "Full",     "Full",     "Full",     "Part"],
        ["Delivery Manager",                  "Part",     "Part",     "Part",     "Full"],
        ["Content / Methodology Owner",       "Advisory", "Advisory", "Part",     "Full"],
        ["QA / ATF Engineer",                 "—",        "Part",     "Part",     "Full"],
        ["Practice Leader (review/sign-off)", "Milestone","Milestone","Milestone","Milestone"],
    ],
    col_widths_in=[3.0, 1.59, 1.59, 1.59, 1.59],
)

# ── 11. TRADE-OFFS VS. BLUEPRINT B ───────────────────────────────────────────
doc.h1("Trade-Offs vs. Blueprint B (Table Extends)")
doc.table(
    headers=["Dimension", "Blueprint A (Custom App)", "Blueprint B (Table Extends)"],
    rows=[
        ["Custom Table SKU",       "Requires App Engine or custom table entitlement on customer instance", "Avoids custom tables — uses native table extensions only"],
        ["Data Model Control",     "Full control — fields, relationships, UI exactly as designed", "Constrained by native table structure; workarounds needed for some fields"],
        ["Development Complexity", "Higher — full scoped app development, Studio, ATF", "Lower — mostly configuration, field additions, portal page building"],
        ["Store Path",             "Clean — scoped apps with custom tables are the Store standard", "Messier — extensions of native tables create upgrade risk on customer instance"],
        ["Upgrade Risk",           "Low — scoped app is isolated from platform upgrades", "Medium — extended fields can be affected by ServiceNow version upgrades"],
        ["Build Timeline",         "16–18 weeks to v1.0", "10–12 weeks to equivalent functionality"],
        ["Long-term Scalability",  "High — designed to grow with engagement portfolio", "Medium — native table extensions have field limits and governance constraints"],
        ["Commercial Packaging",   "Clearly packageable as standalone product", "Harder to package — extensions are embedded in customer's native tables"],
        ["Best For",               "Strategic product investment; Store listing; multi-customer scale", "Fast first engagement use; customers without App Engine SKU; lower initial investment"],
    ],
    col_widths_in=[2.2, 3.5, 3.66],
)

# ── 12. DECISION POINTS FOR DIRECTOR OF TECHNICAL SERVICES ──────────────────
doc.h1("Decision Points for Director of Technical Services Review")
doc.para(
    "The following decisions should be resolved in the architecture review session before development begins. "
    "Each has a recommended default if there is no strong reason to deviate."
)
doc.table(
    headers=["Decision", "Options", "Recommended Default", "Implication"],
    rows=[
        ["App vs. Extends",            "Blueprint A or Blueprint B", "Blueprint A", "Higher investment, stronger long-term product; review against timeline and resource constraints"],
        ["Store vs. Update Set",       "ServiceNow Store ISV or update set", "Update Set first, Store by Q4 2026", "Update set allows immediate use; Store runs in parallel"],
        ["PA Required?",               "Full PA or native reporting fallback", "Native reporting fallback as default; PA as premium", "Ensures app works on all customer instances regardless of PA SKU"],
        ["Write vs. Read-Only on Agile","Create stories from app, or read only", "Read-only initially", "Write access to Agile increases complexity; defer to Phase 3 if at all"],
        ["Content Hosting",            "App's own Content table or reference existing KB", "Own Content table", "Own table gives full control; KB reference reduces duplication but depends on KB being set up"],
        ["Multi-Engagement Support",   "One instance per engagement or shared Everforth instance", "Customer instance per engagement", "Avoids multi-tenancy and licensing complexity"],
    ],
    col_widths_in=[1.8, 2.2, 2.0, 3.36],
)
doc.callout(
    "Recommended outcome of review: Confirm Blueprint A or B. If A — assign a lead developer and begin Phase 1 "
    "scope. If B — begin table extension mapping against a PDI within two weeks. Either way, methodology "
    "content loading (populating the Content table from existing collateral) should start in parallel "
    "immediately — it is path-independent."
)

# ── 13. NEXT STEPS ───────────────────────────────────────────────────────────
doc.h1("Next Steps")
doc.table(
    headers=["Action", "Owner", "Timeline"],
    rows=[
        ["Review Blueprint A and Blueprint B with Director of Technical Services", "Senior Director + Shawn", "This week"],
        ["Decision: Custom App vs. Table Extends approach", "Senior Director + Shawn", "End of review session"],
        ["Decision: ServiceNow Store ISV enrollment — initiate or defer", "Senior Director + Practice Mgr", "2 weeks post-decision"],
        ["Assign lead developer / architect for Phase 1", "Senior Director", "1 week post-decision"],
        ["Provision PDI (Personal Developer Instance) for development", "Shawn / Architecture team", "1 week post-decision"],
        ["Begin Phase 1 — App scope, tables, role definitions", "Lead Developer", "Week following PDI provisioning"],
        ["Begin methodology content loading in parallel (path-independent)", "Delivery Manager / Practice", "Start immediately — does not require app decision"],
        ["Draft go-to-market one-pager for sales team", "Senior Director", "Following architecture decision"],
    ],
    col_widths_in=[4.0, 2.5, 2.86],
)

doc.save(OUT)
print(f"Saved: {OUT}")
