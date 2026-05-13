"""
build_blueprint_b.py — ECS Delivery Intelligence Platform Blueprint B (Table Extends)
Rebuilt with canonical ECS Federal branding via ecs_template.py
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
OUT  = os.path.join(HERE, "ECS_DeliveryApp_Blueprint_B_TableExtends_INTERNAL.docx")

doc = EcsDocument(
    meta=DocMeta(
        eyebrow="INTERNAL · ARCHITECTURAL BLUEPRINT — FOR REVIEW WITH DIRECTOR OF TECHNICAL SERVICES",
        title="ECS Delivery Intelligence Platform\nBlueprint B — Table Extends Approach",
        subtitle="Native Platform Extension Architecture · Lower SKU Dependency · Faster to Deploy · Constrained by Native Structure",
        audience="Director of Technical Services (Shawn), Senior Director, Lead Developer",
        companion_to="Blueprint A (Custom App) · Executive Briefing B · Arch Rationale · Project Plan xlsx",
        doc_id="INT-DA-BP-B",
        version="1.0 Draft",
        status="For Architecture Review",
        confidentiality="Internal Use Only · Confidential",
        running_header_label="Internal · Blueprint B — Table Extends Approach",
    ),
    logo_path=LOGO,
)

doc.add_cover_page()
doc.page_break()

# ── 1. EXECUTIVE SUMMARY ────────────────────────────────────────────────────
doc.h1("Executive Summary")
doc.para(
    "This blueprint defines an alternative architecture for the ECS Delivery Intelligence Platform that "
    "achieves the same functional goals as Blueprint A — role-based portal, living health dashboards, native "
    "module integration, structured delivery data — but does so by extending ServiceNow's existing native "
    "tables rather than creating new custom tables in a scoped application."
)
doc.para(
    "Blueprint B trades architectural purity for speed and lower SKU friction. It can be deployed to a "
    "customer instance faster, does not require App Engine licensing, and can be built with "
    "configuration-first techniques that reduce development complexity. The trade-off is a less clean "
    "commercial packaging path and greater exposure to upgrade risk when ServiceNow releases new platform versions."
)
doc.callout(
    "Key distinction from Blueprint A: Blueprint B does not create new custom tables. It adds fields to "
    "native tables (Task, Project, Knowledge, Group), builds portal pages on top of those extensions, and "
    "wires health scoring through calculated fields and scheduled jobs that read from native records. The "
    "delivery intelligence lives inside the platform's existing structure."
)
doc.table(
    headers=["Dimension", "This Blueprint"],
    rows=[
        ["Application Type",   "Table extensions + scoped UI/Portal only; no new custom base tables"],
        ["Deployment Model",   "Update set of field extensions, portal pages, business rules — smaller footprint than Blueprint A"],
        ["Target Audience",    "Same roles as Blueprint A: Everforth consultants + customer stakeholders (portal-only)"],
        ["Data Strategy",      "Extend native tables: Task, pm_project, kb_knowledge, sys_user_group, rm_story"],
        ["Dashboard Approach", "Native platform reporting + optional PA widgets; same health score logic as Blueprint A"],
        ["Commercial Path",    "Engagement deliverable; Store path is harder — extended tables are messier to package"],
        ["Key Advantage",      "Faster to build (10–12 weeks), no App Engine SKU needed, lower customer licensing risk"],
        ["Key Constraint",     "Native table field limits, upgrade exposure, harder to package as standalone commercial product"],
    ],
    col_widths_in=[2.0, 7.36],
)

# ── 2. ARCHITECTURE PHILOSOPHY ───────────────────────────────────────────────
doc.h1("Architecture Philosophy — Extend, Do Not Build")
doc.para(
    "ServiceNow's platform is built around a small number of powerful base tables that everything else "
    "extends from. The Task table [task] is the foundation of virtually all work records — incidents, "
    "changes, requests, stories, project tasks. The Project table [pm_project] underpins SPM. Knowledge "
    "[kb_knowledge] underpins the knowledge base."
)
doc.para(
    "Blueprint B leverages this extensibility model deliberately. Rather than defining what an 'Engagement' "
    "or 'Sprint Gate' is from scratch, we extend existing concepts: a Sprint Gate is a Project Task with "
    "additional fields. A Risk Record is a task-extended record in the existing Risk Management module. "
    "A Decision is a catalog task with added metadata. Methodology content is a Knowledge Article with "
    "additional categorization fields."
)
doc.callout(
    "Design constraint to hold: Every field added to a native table must be prefixed with the application "
    "scope (u_ecs_ or x_everforth_ecs_) and documented in the extension registry. Undocumented field "
    "additions are the primary cause of upgrade conflicts. Discipline here is non-negotiable."
)

# ── 3. TABLE EXTENSION STRATEGY ──────────────────────────────────────────────
doc.h1("Table Extension Strategy")
doc.para(
    "The following native tables are extended. Each extension adds only the fields necessary to support "
    "delivery intelligence — no redundant fields that duplicate native functionality."
)
doc.h2("3.1  Extending pm_project — The Engagement Record")
doc.para(
    "ServiceNow's Strategic Portfolio Management project table becomes the Engagement record. A project is "
    "created per engagement and extended with ECS-specific fields. This gives us SPM's native milestone, "
    "resource, and portfolio capabilities for free."
)
doc.table(
    headers=["Extended Field", "Type", "Purpose"],
    rows=[
        ["u_ecs_engagement_type",  "Choice",             "ECS OOTB / HAM-Only / SAM-Only / Custom scope"],
        ["u_ecs_health_score",     "Integer",            "0–100, calculated by scheduled job"],
        ["u_ecs_health_indicator", "Choice",             "Red / Yellow / Green — derived from health score"],
        ["u_ecs_current_sprint",   "Choice",             "Sprint 0 through Sprint 6, Hypercare"],
        ["u_ecs_delivery_manager", "Reference → User",   "Everforth DM assigned"],
        ["u_ecs_lead_architect",   "Reference → User",   "Everforth architect"],
        ["u_ecs_customer_sponsor", "Reference → User",   "Customer executive sponsor (gets portal access)"],
        ["u_ecs_agile_backlog",    "Reference → rm_sprint_backlog", "Links project to Agile backlog"],
        ["u_ecs_portal_active",    "Boolean",            "Whether customer portal view is live for this engagement"],
    ],
    col_widths_in=[2.6, 1.6, 5.16],
)
doc.h2("3.2  Extending pm_project_task — Sprint Gates")
doc.para(
    "SPM's project task table is extended to represent Sprint Gates. One project task record per sprint, "
    "typed as a gate checkpoint."
)
doc.table(
    headers=["Extended Field", "Type", "Purpose"],
    rows=[
        ["u_ecs_task_type",         "Choice",            "Sprint Gate / Milestone / Action Item — filters gate records from normal tasks"],
        ["u_ecs_sprint_number",     "Choice (0–6)",      "Which sprint this gate applies to"],
        ["u_ecs_stories_committed", "Integer",           "Captured at sprint start from Agile module"],
        ["u_ecs_stories_completed", "Calculated Int",    "Live GlideRecord count from Agile stories for this sprint"],
        ["u_ecs_velocity_pct",      "Calculated Dec",    "Completed ÷ Committed × 100"],
        ["u_ecs_open_risks",        "Calculated Int",    "Count of open risk records for this sprint"],
        ["u_ecs_open_decisions",    "Calculated Int",    "Count of open decision records for this sprint"],
        ["u_ecs_gate_status",       "Choice",            "Open / At Risk / Passed / Failed"],
        ["u_ecs_signoff_user",      "Reference → User",  "Customer sign-off on gate completion"],
        ["u_ecs_signoff_date",      "Date",              "When gate was formally approved"],
    ],
    col_widths_in=[2.6, 1.6, 5.16],
)
doc.h2("3.3  Extending sn_risk_risk — Risk & Issue Register")
doc.para(
    "ServiceNow's native Risk Management table [sn_risk_risk] is extended to capture delivery-specific "
    "risks and issues. If the customer does not have GRC Risk Management licensed, a lightweight fallback "
    "extends the base Task table instead."
)
doc.table(
    headers=["Extended Field", "Type", "Purpose"],
    rows=[
        ["u_ecs_risk_type",    "Choice: Risk/Issue",          "Distinguishes proactive risk from active issue"],
        ["u_ecs_engagement",   "Reference → pm_project",      "Links risk to the engagement"],
        ["u_ecs_sprint_gate",  "Reference → pm_project_task", "Sprint in which risk was raised"],
        ["u_ecs_workstream",   "Choice",                      "ITSM, CMDB, HAM, Catalog, VA, Platform, etc."],
        ["u_ecs_health_impact","Choice: Low/Med/High",         "How this risk affects the health score"],
    ],
    col_widths_in=[2.6, 1.6, 5.16],
)
doc.h2("3.4  Extending kb_knowledge — Methodology Content")
doc.para(
    "The Knowledge Base table is extended to tag existing articles and new methodology content with "
    "delivery-specific metadata. This surfaces the right article on the right portal page for the right "
    "role without creating a separate content system."
)
doc.table(
    headers=["Extended Field", "Type", "Purpose"],
    rows=[
        ["u_ecs_content_type",      "Choice",         "How-To Guide / Accelerator Pack / Decision Guide / Workshop Pre-Read / Cheatsheet"],
        ["u_ecs_target_role",       "Choice (multi)", "Delivery Manager / Architect / Consultant / Customer Sponsor / Process Owner"],
        ["u_ecs_applicable_sprint", "Choice (multi)", "Sprint 0 / 1 / 2 / 3 / 4 / 5 / 6 / Hypercare"],
        ["u_ecs_workstream",        "Choice (multi)", "Which workstreams this content applies to"],
        ["u_ecs_audience",          "Choice",         "Internal / Customer / Both"],
        ["u_ecs_ecs_content",       "Boolean",        "Flags article as ECS delivery content — used to filter portal displays"],
    ],
    col_widths_in=[2.6, 1.6, 5.16],
)
doc.h2("3.5  Decision Records — Extending sc_task")
doc.para(
    "Decisions that need customer input are captured as Catalog Tasks extended with decision-specific fields. "
    "This gives us native approval workflow, due dates, and assignment without building a custom table."
)
doc.table(
    headers=["Extended Field", "Type", "Purpose"],
    rows=[
        ["u_ecs_decision_type",      "Boolean (flag)",              "Marks this catalog task as an ECS Decision record"],
        ["u_ecs_engagement",         "Reference → pm_project",      "Links to engagement"],
        ["u_ecs_sprint_gate",        "Reference → pm_project_task", "Sprint when decision is needed"],
        ["u_ecs_workstream",         "Choice",                      "Which workstream is affected"],
        ["u_ecs_options_presented",  "String",                      "OOTB vs. alternatives documented"],
        ["u_ecs_decision_made",      "String",                      "Recorded outcome once decided"],
        ["u_ecs_impact_if_deferred", "String",                      "What delays if not resolved by due date"],
    ],
    col_widths_in=[2.6, 1.6, 5.16],
)

# ── 4. ROLE FRAMEWORK ───────────────────────────────────────────────────────
doc.h1("Role Framework")
doc.para(
    "The role framework is identical to Blueprint A. Roles are defined within the scoped application scope "
    "to control portal access, field visibility, and notifications. The difference is that ACLs restrict "
    "access to fields on native tables rather than entirely separate tables."
)
doc.h2("4.1  Internal Roles (Everforth Staff)")
doc.table(
    headers=["Role", "SNow Role Name", "What They See & Can Do"],
    rows=[
        ["Practice Leader",  "x_everforth_ecs_dip.practice_leader", "All engagements (pm_project filtered by u_ecs flag), practice health roll-up, content management"],
        ["Delivery Manager", "x_everforth_ecs_dip.delivery_mgr",    "Their engagements: sprint gate edits, risk/decision management, health dashboard, customer portal preview"],
        ["Lead Architect",   "x_everforth_ecs_dip.architect",       "Their engagements: technical decisions, workstream health, KB content for their workstreams"],
        ["Consultant",       "x_everforth_ecs_dip.consultant",      "Their sprint tasks from Agile, relevant KB content filtered by sprint and workstream"],
    ],
    col_widths_in=[1.8, 2.8, 4.76],
)
doc.h2("4.2  Customer Roles (Portal Access Only)")
doc.table(
    headers=["Role", "SNow Role Name", "What They See & Can Do"],
    rows=[
        ["Executive Sponsor","x_everforth_ecs_dip.customer_sponsor",  "Health summary, milestone timeline, gate approvals, escalated risks and decisions"],
        ["Project Owner",    "x_everforth_ecs_dip.customer_pm",       "Sprint-level detail, all decisions requiring input, risk log, upcoming commitments"],
        ["Process Owner",    "x_everforth_ecs_dip.customer_process",  "Workstream-scoped content, decisions in their area, workshop pre-reads for their process"],
        ["End User",         "x_everforth_ecs_dip.customer_user",     "Read-only: sprint schedule, upcoming changes, relevant knowledge articles"],
    ],
    col_widths_in=[1.8, 2.8, 4.76],
)
doc.callout(
    "ACL strategy for Blueprint B: Because extended fields live on native tables, ACLs must be written "
    "carefully to avoid granting broader native table access than intended. Each ECS field should have its "
    "own ACL condition checking for the u_ecs_ prefix and the user's ECS role. Portal widget data queries "
    "must use addQuery() conditions to scope results to the current engagement. This is more ACL management "
    "overhead than Blueprint A's scoped tables."
)

# ── 5. ROLE-BASED PORTAL DESIGN ──────────────────────────────────────────────
doc.h1("Role-Based Portal Design")
doc.para(
    "The portal experience is functionally identical to Blueprint A. All role-based landing pages are built "
    "on the Service Portal framework. The difference is that portal widgets query extended native tables "
    "rather than custom tables. From the user's perspective, the experience is the same."
)
doc.h2("5.1  Portal Pages")
doc.table(
    headers=["Page", "Audience", "Primary Data Source"],
    rows=[
        ["Engagement Overview",   "Delivery Manager",       "pm_project with u_ecs_ extensions — health score, sprint gate summary, risk/decision counts"],
        ["Sprint Health Dashboard","Delivery Manager",       "pm_project_task (sprint gates) + rm_story (Agile stories) + PA charts"],
        ["Consultant Home",        "Consultant",             "rm_story filtered to user, kb_knowledge filtered by u_ecs_applicable_sprint and user's workstream"],
        ["Sponsor View",           "Customer Sponsor",       "pm_project health card, pm_milestone list, sc_task decisions awaiting approval"],
        ["Project Owner View",     "Customer PM",            "pm_project_task sprint gates, sn_risk_risk open items, sc_task open decisions"],
        ["Process Owner View",     "Customer Process Owner", "kb_knowledge filtered by u_ecs_workstream and u_ecs_audience=Customer, sc_task decisions in their workstream"],
        ["Practice Roll-Up",       "Practice Leader",        "Aggregate across all pm_projects flagged as ECS engagements — portfolio health view"],
    ],
    col_widths_in=[2.0, 2.0, 5.36],
)
doc.h2("5.2  Key Widget Types")
doc.bullet("Engagement health card: reads u_ecs_health_score and u_ecs_health_indicator from pm_project")
doc.bullet("Sprint gate timeline: reads pm_project_task records filtered by u_ecs_task_type='Sprint Gate'")
doc.bullet("Velocity chart: reads rm_story records for the linked agile backlog — completed vs. committed per sprint")
doc.bullet("Risk summary: reads sn_risk_risk records filtered by u_ecs_engagement reference")
doc.bullet("Decision tracker: reads sc_task records filtered by u_ecs_decision_type=true and engagement")
doc.bullet("Content browser: reads kb_knowledge filtered by u_ecs_ecs_content=true and role/sprint/workstream tags")
doc.bullet("Gate approval button: triggers approval workflow on the sprint gate project task record")

# ── 6. LIVING PROJECT HEALTH ──────────────────────────────────────────────────
doc.h1("Living Project Health — Same Outcome, Native Data")
doc.para(
    "The health scoring logic is identical to Blueprint A. A scheduled job runs nightly and writes the "
    "calculated score to u_ecs_health_score on the pm_project record. The difference is that all source "
    "data comes from queries against native tables rather than custom tables."
)
doc.h2("6.1  Health Score Calculation (Scheduled Job)")
doc.table(
    headers=["Component", "Weight", "Data Source", "Calculation"],
    rows=[
        ["Sprint Velocity",   "40%", "rm_story where sprint = current sprint and backlog = engagement backlog", "Completed stories ÷ committed stories × 100"],
        ["Risk Posture",      "30%", "sn_risk_risk where u_ecs_engagement = this project and state = Open", "Start 100; −15 per high risk, −5 per medium risk"],
        ["Decision Latency",  "20%", "sc_task where u_ecs_decision_type=true, u_ecs_engagement = this project", "−10 per overdue decision, −15 per escalated decision"],
        ["Milestone Variance","10%", "pm_milestone where project = this project", "Days late × −5 per week of variance"],
        ["RAG Threshold",     "N/A", "u_ecs_health_score on pm_project", "Green ≥ 80 | Yellow 60–79 | Red < 60"],
    ],
    col_widths_in=[1.7, 0.7, 3.0, 3.96],
)
doc.h2("6.2  Spreadsheet-to-Record Mapping")
doc.table(
    headers=["Current Spreadsheet", "Blueprint B Replacement", "Native Table"],
    rows=[
        ["Weekly RAG Status",       "Health card on portal — auto-calculated",       "pm_project (u_ecs_health_score)"],
        ["Sprint Tracking Worksheet","Sprint Gate project task + Agile board",        "pm_project_task + rm_story"],
        ["Risk & Issue Log",        "Extended sn_risk_risk records",                 "sn_risk_risk (u_ecs_ fields)"],
        ["Decision Log",            "Extended sc_task decision records",             "sc_task (u_ecs_decision_type)"],
        ["Milestone Tracker",       "Native SPM milestones on the project",          "pm_milestone"],
        ["Velocity Chart",          "PA chart or native report on rm_story",         "rm_story"],
        ["Project Health Summary",  "Engagement health card on Sponsor portal",      "pm_project (u_ecs_health_score, u_ecs_health_indicator)"],
    ],
    col_widths_in=[2.2, 2.8, 4.36],
)

# ── 7. SKU IMPLICATIONS ───────────────────────────────────────────────────────
doc.h1("SKU Implications")
doc.para(
    "A core advantage of Blueprint B is that it avoids requiring the App Engine SKU on the customer instance. "
    "The following table maps each capability to its licensing requirement."
)
doc.table(
    headers=["Capability", "Required SKU", "Notes"],
    rows=[
        ["Table field extensions (u_ecs_ fields)", "Base Platform", "Adding fields to native tables is standard platform capability — no additional SKU"],
        ["Service Portal pages",                   "Base Platform", "Portal framework is included in all ServiceNow platform licenses"],
        ["Business Rules / Scheduled Jobs",        "Base Platform", "Standard scripting capability — no additional SKU"],
        ["Flow Designer workflows",                "Base Platform", "Flow Designer is included in all current platform versions"],
        ["Agile Development integration",          "ITSM or SPM",  "Agile module may require ITSM Pro or SPM license — confirm with customer contract"],
        ["SPM Project & Milestones",               "SPM",          "Strategic Portfolio Management requires SPM license or equivalent PPM entitlement"],
        ["Risk Management (sn_risk_risk)",         "GRC",          "If customer does not have GRC, fall back to extending Task table for risk records"],
        ["Performance Analytics widgets",          "PA",           "Optional — fall back to native reports if PA not licensed"],
        ["Virtual Agent topics",                   "VA / ITSM Pro","Virtual Agent requires VA SKU or ITSM Professional — confirm before building VA topics"],
        ["App Engine (custom tables)",             "NOT REQUIRED", "Blueprint B's key advantage — no App Engine SKU needed"],
    ],
    col_widths_in=[2.8, 1.4, 5.16],
)
doc.callout(
    "Minimum viable baseline for Blueprint B: Base Platform + SPM + ITSM. These three are almost always "
    "present in any ECS customer engagement. Blueprint B can be deployed on this baseline without any "
    "additional licensing conversation. VA and PA are additive enhancements if the customer has them."
)

# ── 8. NATIVE MODULE INTEGRATION ─────────────────────────────────────────────
doc.h1("Native Module Integration")
doc.para(
    "Integration approach is the same as Blueprint A. The platform reads from native modules and surfaces "
    "their data in a delivery context. Because Blueprint B extends native tables, some integrations are "
    "even simpler — no cross-scope queries needed."
)
doc.table(
    headers=["Module", "Integration Approach", "Blueprint B Advantage vs. A"],
    rows=[
        ["Agile Development",        "GlideRecord query on rm_story filtered by backlog reference stored on pm_project extension", "Slightly simpler — no cross-scope reference; backlog linked directly to native project record"],
        ["SPM Milestones",           "Native pm_milestone records on the engagement project — no extension needed", "Direct native access — milestones already on the project, no mapping required"],
        ["ITSM (incidents/changes)", "GlideRecord query on incident and change_request during Hypercare phase", "Same as Blueprint A — read-only query, no scope issues"],
        ["Knowledge Base",           "Extended kb_knowledge table — content tagged in-place with u_ecs_ fields", "Simpler — articles live in native KB, no separate content sync needed"],
        ["Risk Management",          "Extended sn_risk_risk or task fallback — native GRC workflow available if licensed", "May gain native GRC workflow for free if customer has GRC licensed"],
        ["Virtual Agent",            "VA topics query extended tables using same field filters as portal widgets", "Same complexity as Blueprint A — VA scripting is table-agnostic"],
    ],
    col_widths_in=[2.0, 3.5, 3.86],
)

# ── 9. IMPLEMENTATION SEQUENCE ───────────────────────────────────────────────
doc.h1("Implementation Sequence")
doc.para(
    "Blueprint B has a shorter build timeline than Blueprint A. The primary reason is that configuration "
    "of existing tables and portal pages is faster than standing up a full scoped application from scratch."
)
doc.table(
    headers=["Phase", "Duration", "Deliverables", "Milestone"],
    rows=[
        ["Phase 1 — Extensions & Roles",      "2–3 weeks", "All u_ecs_ field extensions on native tables, scoped roles and ACLs, engagement project type configuration, update set packaging", "v0.5: extensions installed, records can be created in native tables"],
        ["Phase 2 — Portal & Health",          "3–4 weeks", "Service Portal pages for all roles, health score scheduled job, risk and decision records functioning, portal customer access", "v0.7: fully functional for internal use; customer portal live"],
        ["Phase 3 — Integrations",             "2–3 weeks", "Agile velocity chart, SPM milestone integration, Knowledge Base content tagging, Virtual Agent topics", "v0.9: replaces all spreadsheets; methodology content surfacing correctly"],
        ["Phase 4 — Content & Hardening",      "2–3 weeks", "Methodology content loaded into KB with u_ecs_ tags, ACL audit, upgrade-risk assessment of all extensions, documentation", "v1.0: production-ready for all engagements"],
    ],
    col_widths_in=[2.2, 0.9, 4.0, 2.26],
)
doc.h2("9.1  Comparison to Blueprint A")
doc.table(
    headers=["Factor", "Blueprint A", "Blueprint B"],
    rows=[
        ["Build timeline to v1.0",   "16–18 weeks",                                        "10–12 weeks"],
        ["Developer profile needed", "ServiceNow app developer (Studio)",                   "ServiceNow configurator / mid-level developer"],
        ["App Engine SKU required",  "Yes — customer must have it",                         "No — base platform sufficient"],
        ["Store packaging",          "Clean — scoped app is Store-ready",                   "Complex — native extensions are messy to package"],
        ["Upgrade risk",             "Low — scoped app isolated",                           "Medium — field extensions can conflict with upgrades"],
        ["Data model control",       "Full — all tables designed for this",                  "Constrained — working within native table limits"],
        ["Long-term commercial potential","High — clean product story",                     "Lower — harder to position as a standalone product"],
        ["Right choice when",        "Strategic product; Store is the goal",                "Fast first use; customer lacks App Engine SKU"],
    ],
    col_widths_in=[2.4, 3.4, 3.56],
)

# ── 10. UPGRADE RISK MANAGEMENT ──────────────────────────────────────────────
doc.h1("Upgrade Risk Management")
doc.para(
    "Blueprint B's primary architectural risk is that field extensions on native tables can be affected "
    "by ServiceNow's biannual platform upgrades. This section defines how to manage that risk so it does "
    "not become a customer problem."
)
doc.h2("10.1  Risk Mitigation Practices")
doc.bullet("Maintain a formal Extension Registry document listing every u_ecs_ field, the native table it extends, its type, and its purpose")
doc.bullet("After every ServiceNow upgrade (now twice yearly), run a regression test against all ECS portal pages and health score calculations before customer is notified of upgrade")
doc.bullet("Keep all ECS fields in a dedicated update set so they can be reapplied cleanly if an upgrade conflicts")
doc.bullet("Avoid extending tables that ServiceNow actively redesigns frequently — prefer stable tables like pm_project over rapidly evolving ones like sn_hr_case")
doc.bullet("Document fallback behaviour for each integration: if a native table changes structure, what does the health score do? Defaults should degrade gracefully, not error")
doc.h2("10.2  Tables Assessed as Stable vs. Higher Risk")
doc.table(
    headers=["Table", "Stability Assessment", "Basis"],
    rows=[
        ["pm_project",      "Stable",  "SPM table — changes are additive, not structural, in recent upgrade history"],
        ["pm_project_task", "Stable",  "Same lineage as pm_project — low structural change risk"],
        ["kb_knowledge",    "Stable",  "Knowledge table has been structurally stable for multiple major versions"],
        ["sn_risk_risk",    "Medium",  "GRC module evolves more frequently — monitor upgrade notes"],
        ["sc_task",         "Stable",  "Catalog task table is foundational — rarely restructured"],
        ["rm_story",        "Medium",  "Agile module has seen more active development — test post-upgrade"],
    ],
    col_widths_in=[2.0, 1.8, 5.56],
)

# ── 11. DECISION POINTS FOR DIRECTOR OF TECHNICAL SERVICES ──────────────────
doc.h1("Decision Points for Director of Technical Services Review")
doc.para(
    "The following decisions are specific to Blueprint B and should be resolved in the architecture review session."
)
doc.table(
    headers=["Decision", "Options", "Recommended Default", "Implication"],
    rows=[
        ["Risk table: GRC or Task fallback", "Extend sn_risk_risk or extend Task", "sn_risk_risk if GRC licensed; Task fallback otherwise", "Confirm GRC licensing during Sprint 0 — drive consistent approach across all engagements"],
        ["Decision record: sc_task or custom", "Extend sc_task or Request Catalog Item", "Extend sc_task", "Catalog Item approach gives nicer UI but adds catalog complexity; sc_task is simpler"],
        ["Content in KB or separate category", "Tag existing KB or new KB category", "New KB category tagged u_ecs_ecs_content=true", "Separate category keeps methodology content distinct from operational KB"],
        ["PA fallback strategy", "Native reports or PA if licensed", "Native reports with PA as upgrade if customer has it", "Design portal widgets to work without PA; use PA widget variants if available"],
        ["Store path: attempt or skip", "Pursue Store eventually or remain update set", "Remain update set for Blueprint B; revisit if customer demand warrants", "Blueprint B is harder to certify for the Store — set expectations accordingly"],
        ["Upgrade regression ownership", "Everforth or customer-managed", "Everforth-managed as part of support", "Need a defined support offer if we own upgrade regression; adds ongoing service commitment"],
    ],
    col_widths_in=[2.0, 1.8, 2.0, 3.56],
)
doc.callout(
    "Recommended review outcome: If speed to first deployment and SKU flexibility are the priority, choose "
    "Blueprint B for the first engagement and use learnings to inform whether Blueprint A is worth the "
    "additional investment. Blueprint B is not a permanent compromise — it can be rebuilt as a full custom "
    "app once the data model and portal design are proven in the field."
)

# ── 12. NEXT STEPS ───────────────────────────────────────────────────────────
doc.h1("Next Steps")
doc.table(
    headers=["Action", "Owner", "Timeline"],
    rows=[
        ["Review Blueprint A and Blueprint B with Director of Technical Services", "Senior Director + Shawn", "This week"],
        ["Decision: Blueprint A (Custom App) vs. Blueprint B (Table Extends)", "Senior Director + Shawn", "End of review session"],
        ["If Blueprint B selected: provision PDI and begin extension mapping", "Shawn / Architecture team", "1 week post-decision"],
        ["If Blueprint B selected: confirm GRC licensing on first target customer", "Delivery Manager", "During Sprint 0 discovery of first engagement"],
        ["Draft Extension Registry document — catalog all u_ecs_ fields", "Lead Developer", "Phase 1, Week 1"],
        ["Define upgrade regression test plan", "Lead Developer + Shawn", "Phase 1, Week 2"],
        ["Begin KB category and content tagging (path-independent)", "Delivery Manager / Practice", "Start immediately — does not require architecture decision"],
        ["Draft portal wireframes for review with practice team", "Delivery Manager + Architect", "Phase 2, Week 1"],
        ["Draft go-to-market one-pager for sales team", "Senior Director", "Following architecture decision"],
    ],
    col_widths_in=[4.0, 2.5, 2.86],
)

doc.save(OUT)
print(f"Saved: {OUT}")
