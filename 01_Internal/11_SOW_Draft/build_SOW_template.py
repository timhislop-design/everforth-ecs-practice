# -*- coding: utf-8 -*-
"""
Build ECS OOTB-First SOW Template
Generic Statement of Work template for the ECS OOTB-First / Modernizing the Core engagement.
Based on the Connection engagement as the reference model; all customer-specific content replaced
with bracketed placeholders so consultants can adapt per engagement.

Audience: Client (shared with customer at SOW stage)
Doc ID: CLT-SOW-01
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

OUT = os.path.join(HERE, "ECS_OOTB_SOW_Template_CLIENT.docx")
LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")

d = EcsDocument(logo_path=LOGO, meta=DocMeta(
    eyebrow="STATEMENT OF WORK · MODERNIZING THE CORE",
    title="Statement of Work\nServiceNow OOTB-First Reimplementation",
    subtitle="Modernizing the Core — Ensuring AI Realization and Optimizing Long-Term Value",
    audience="[Customer Organization] · ECS Federal — ServiceNow Practice",
    companion_to="ECS Consultant Handbook (INT-CH-01) · Accelerator Pack Suite · Sprint Workbooks",
    doc_id="CLT-SOW-01",
    version="1.0",
    status="Template — Adapt Per Engagement",
    running_header_label="Statement of Work · OOTB-First Reimplementation",
    footer_left="ECS Federal · ServiceNow Practice  ·  Confidential",
))

# ── COVER ────────────────────────────────────────────────────────────────────
d.add_cover_page()

d.callout(
    "HOW TO USE THIS TEMPLATE: Replace every bracketed placeholder — [Customer Name], "
    "[X weeks], [dollar amount], etc. — with engagement-specific content before sending "
    "to the customer. Sections marked ‘INTERNAL NOTE’ must be removed from the "
    "customer-facing version. Pricing and payment schedule are in Section 12 and must be "
    "completed by the Engagement Manager and reviewed by Practice Lead prior to issuance."
)

d.para(
    "This Statement of Work (SOW) also serves as the Project Charter for the engagement. "
    "It defines the scope, delivery approach, customer responsibilities, governance model, "
    "and contractual guardrails that govern the ECS Federal ServiceNow reimplementation "
    "engagement with [Customer Organization]. Upon execution, this document is binding on "
    "both parties and supersedes any prior proposals, presentations, or correspondence "
    "related to the same scope of work."
)

# ── TABLE OF CONTENTS PLACEHOLDER ────────────────────────────────────────────
d.page_break()

# ── 1. EXECUTIVE SUMMARY ─────────────────────────────────────────────────────
d.h1("Executive Summary")
d.para(
    "[Customer Organization] has initiated a strategic ServiceNow reimplementation designed to "
    "exit a [describe current state — e.g., highly customized legacy environment / domain-separated "
    "instance / aging implementation] and establish a modern, AI-ready platform foundation. "
    "ECS Federal will lead this engagement under an OOTB-First delivery discipline — standing up "
    "proven ServiceNow baseline capability before any deviation is considered — so that [Customer "
    "Organization] lands on a platform that is architecturally ready for Now Assist, Agentic "
    "Agents, Predictive Intelligence, and the Workflow Data Fabric."
)
d.para(
    "This [X]-week Phase 1 delivery focuses on modernizing ITSM Core processes and standing up a "
    "modern Employee Center with Virtual Agent and AI Search to drive ticket deflection and improve "
    "the overall employee experience. A foundational Sprint 0 precedes the build sprints and is "
    "dedicated to alignment, governance setup, and accelerator pack data collection. Delivery "
    "follows an iterative Agile methodology with two-week sprints."
)
d.para(
    "A critical success factor for this engagement is alignment to Common Service Data Model "
    "(CSDM) best practices from day one, ensuring a healthy CMDB that can support CI-based change "
    "risk scoring and provide the clean data required for AI ROI. Key outcomes will be tracked "
    "via Platform Analytics, focusing on operational improvements including MTTR, SLA attainment, "
    "and change success rates."
)

d.h2("Core Project Goals")
d.bullet("Adopt OOTB processes as the default, leading with ServiceNow best practices before making iterative adjustments.")
d.bullet("Modernize Change Management and CMDB alignment to CSDM standards, enabling CI-based risk scoring.")
d.bullet("Deliver a modern Employee Center with Virtual Agent, AI Search, and a curated Knowledge Base.")
d.bullet("Enable Platform Analytics and Predictive Intelligence to achieve measurable operational ROI.")
d.bullet("Establish strict governance to intake, triage, and prioritize platform requests based on business need.")
d.bullet("Ensure all purchased SKUs are actively configured and delivering value within the engagement scope.")
d.bullet("[Add customer-specific goal: e.g., exit domain separation / consolidate instances / etc.]")

d.h2("Current State and Pain Points")
d.para(
    "The following pain points, identified during pre-engagement discovery with [Customer "
    "Organization], form the basis for the scope and sequencing decisions in this SOW:"
)
d.bullet("Technical debt and accumulated customization that limits AI adoption and upgrade flexibility.")
d.bullet("Low OOTB adoption resulting in process inefficiencies, complexity, and limited scalability.")
d.bullet("[Customer-specific blocker, e.g., domain separation / aging integrations / portal confusion].")
d.bullet("User experience gaps: employees uncertain where or how to request services.")
d.bullet("CMDB health issues preventing AI ROI — CI data quality insufficient for risk scoring or automation.")
d.bullet("Underutilized license SKUs — purchased capabilities not yet configured or delivering value.")

# ── 2. SCOPE OF SERVICES ─────────────────────────────────────────────────────
d.page_break()
d.h1("Phase 1: In-Scope Applications and Integrations")
d.para(
    "The following capabilities are in scope for Phase 1. Each capability is selected because it "
    "delivers immediate operational value and serves as a prerequisite for the AI capabilities "
    "[Customer Organization] will leverage in subsequent phases."
)

d.h2("ITSM Core")
d.bullet("Interactions, Incident Management, Request Management, Knowledge Management.")
d.bullet("Change Management including CAB Workbench and [2–3] well-defined standard changes.")
d.bullet("Problem Management and Major Incident Management.")
d.bullet("Service Operations Workspace.")

d.h2("Service Catalog")
d.bullet(
    "Top [10–15] most impactful existing catalog items with clearly defined activities, "
    "workflows, and approvals. Existing catalog configurations are leveraged where they do not "
    "introduce technical debt."
)
d.bullet(
    "[2–3] of the Phase 1 catalog items are designed to be generic enough to capture services "
    "that do not yet have a dedicated workflow, ensuring no user community is left without a "
    "service path. Directed workflows for those services are delivered in later phases."
)

d.h2("Employee Experience")
d.bullet("Employee Center portal.")
d.bullet("Virtual Agent with [X] baseline topic configurations.")
d.bullet("AI Search configuration and knowledge base integration.")
d.bullet("Knowledge Management curation and baseline article set.")

d.h2("Platform Baselines")
d.bullet("Subscription Management — configured as a platform-level baseline for license visibility.")
d.bullet("Security Center — baseline posture visibility from day one.")
d.bullet("Flow Designer, Predictive Intelligence, Task Intelligence.")
d.bullet("Platform Analytics, Data Visualization, Benchmarks.")

d.h2("CMDB and CSDM")
d.bullet("Foundational alignment to CSDM best practices.")
d.bullet("CMDB and CI relationship standards established.")
d.bullet("Discovery and Service Graph Connectors for [SCCM / Intune / other — list specifically].")
d.bullet("Current Discovery configuration leveraged where it does not introduce technical debt.")

d.h2("Hardware Asset Management (HAM)")
d.bullet("Stockrooms and HAM foundational configuration to ensure CSDM alignment in Phase 1.")

d.h2("Integrations")
d.bullet("Active Directory (AD) and Single Sign-On (SSO) — current configuration leveraged where aligned to best practices.")
d.bullet("[List any additional integration specifically — every integration not listed here is Out of Scope].")

d.callout(
    "AI ALIGNMENT NOTE: Each capability above is selected because it both delivers immediate "
    "operational value and is a prerequisite for AI capabilities [Customer Organization] has "
    "invested in. The OOTB foundation established in Phase 1 is the architectural requirement "
    "for Now Assist, Agentic Agents, and the Workflow Data Fabric."
)

# ── 3. TECHNICAL APPROACH ─────────────────────────────────────────────────────
d.page_break()
d.h1("Technical Approach: The OOTB-First Framework")
d.para(
    "The goal of this engagement is to make customization the exception rather than the default. "
    "Every in-scope application build begins with a demonstration of out-of-the-box ServiceNow "
    "functionality. Any delta between the baseline and a user story requirement must be justified "
    "by a documented business necessity, scoped to budget, and signed off by the Project Sponsor "
    "before ECS proceeds with configuration."
)
d.para(
    "An acceptable threshold for deviating from OOTB is qualitative: a delta is acceptable only "
    "when it is (a) tied to a documented business outcome, (b) cannot be met by configuration of "
    "an OOTB capability, and (c) signed off by the Project Sponsor. ECS will proactively present "
    "the OOTB alternative in every case before a deviation is considered."
)

d.h2("The Rule of Three")
d.para(
    "If a requirement cannot be met by (1) Configuration, (2) UI Policy, or (3) Flow Designer, "
    "it is treated as a Customization. Customizations require a separate technical review, a "
    "formal impact assessment against scope and budget, and Project Sponsor approval before work begins."
)

d.h2("Definition of Done")
d.para("A user story is considered Done when:")
d.bullet("All acceptance criteria in the user story have been met and validated by the Product Owner.")
d.bullet("The configuration adheres to the Rule of Three unless a Customization has been approved by the Project Sponsor.")
d.bullet("The configuration is documented in the relevant design artifact and the sprint workbook is updated.")

d.h2("MVP Mindset")
d.para(
    "To complete this engagement within the [X]-week timeline and achieve a Go-Live at week [16], "
    "ECS and [Customer Organization] will maintain an MVP mindset: delivering a baseline "
    "implementation for all in-scope applications while capturing secondary and enhancement "
    "requirements in the backlog for the Phase 2 roadmap. This keeps the initial implementation "
    "clean and the timeline protected."
)

d.h2("Low-Code / No-Code Governance")
d.para(
    "ServiceNow configuration will prioritize Flow Designer, Decision Tables, and UI Builder over "
    "custom Script Includes or Jelly/Angular modifications. Any request that requires scripted "
    "solutions is subject to the Rule of Three review and may require a PCR."
)

d.h2("Upgradeability Scorecard")
d.para(
    "Every configuration decision is assessed for its impact on future ServiceNow upgrades. If a "
    "request creates a Skipped Record risk for the next ServiceNow family version, it is "
    "automatically flagged for the Governance Triage Log and brought to the Customization Council "
    "for disposition."
)

d.h2("Intelligent Reuse: Accelerating Delivery Without Compromising OOTB")
d.para(
    "A pragmatic accelerator for the delivery timeline is the intelligent reuse of [Customer "
    "Organization]’s existing platform investments where they align with the OOTB pattern. "
    "ECS and [Customer Organization]’s technical leadership will assess current configurations "
    "and port them to the new instance where doing so does not introduce technical debt."
)
d.bullet(
    "Integration configurations (AD/SSO, Discovery, SCCM/Intune): ECS reviews current integration "
    "designs with [Customer Organization] SMEs and ports the working configuration where it aligns "
    "to current best practices."
)
d.bullet(
    "Service Catalog items: Existing items using OOTB workflow patterns and standard form variables "
    "are ported and adapted. Items relying on custom Script Includes or non-standard data models "
    "are rebuilt against the OOTB pattern."
)
d.bullet(
    "Knowledge articles: KM articles are curated and ported as a baseline for the new KM instance "
    "and Virtual Agent / AI Search content. Stale, redundant, or off-pattern articles are retired "
    "rather than ported."
)
d.callout("The principle: reuse what aligns to OOTB; rebuild what does not. This accelerates delivery while preserving the OOTB-first discipline that makes the platform AI-ready.")

# ── 4. DELIVERY APPROACH ─────────────────────────────────────────────────────
d.page_break()
d.h1("Delivery Approach and Engagement Model")

d.h2("Workshop Model")
d.para(
    "The engagement is anchored by a structured, Just-in-Time workshop approach that grounds every "
    "design decision in standard ServiceNow OOTB capability before any deviation is considered. "
    "Workshops are deliberately short, outcome-oriented sessions where the platform demonstrates "
    "the work first, and the conversation focuses on the narrow set of decisions [Customer "
    "Organization] actually needs to make."
)
d.para("Workshops are organized into five tiers, each tied directly to the active sprint backlog:")
d.bullet("Accelerator Pack Workshops: Capture foundational core data required to execute the build (CSDM, CMDB classes, locations, groups, assignment rules, catalog taxonomy, reference datasets).")
d.bullet("CSDM Workshops: Establish the Common Service Data Model foundation that every downstream workstream depends on.")
d.bullet("Process Design Workshops: One per in-scope ITSM process — demonstrate OOTB capability, identify the minimal set of decisions, and close with documented decisions before the sprint begins.")
d.bullet("Employee Experience Workshops: Employee Center structure, Virtual Agent topic design, Knowledge Management taxonomy, and AI Search configuration.")
d.bullet("Validation Workshops: UAT facilitation, stakeholder sign-off, and go-live readiness review.")

d.h2("Sprint Sequencing")
d.table(
    headers=["Sprint", "Phase", "Focus Areas"],
    rows=[
        ["Sprint 0", "Initiate & Plan", "Project kickoff, governance setup, environment provisioning, Accelerator Pack data collection, CSDM alignment workshop"],
        ["Sprint 1", "Execute — Month 1", "Platform architecture, CSDM validation, ITSM design workshops, Discovery / Service Graph Connectors initiation"],
        ["Sprint 2", "Execute — Month 1", "CMDB normalization, ITSM Core configuration begins (Incident, Problem), integration review"],
        ["Sprint 3", "Execute — Month 2", "ITSM Core build (Incident, Problem, Request), SLA and assignment rule configuration"],
        ["Sprint 4", "Execute — Month 2", "Change Management and CAB, first set of high-priority catalog items developed"],
        ["Sprint 5", "Execute — Month 3", "Employee Center, Virtual Agent, Knowledge Management, Platform Analytics"],
        ["Sprint 6", "Execute — Month 3", "HAM foundations, remaining catalog items (totaling [13–15]), environment stabilization"],
        ["Sprint 7/8", "Deliver — Month 4", "UAT, Knowledge Transfer, production cutover, Hypercare"],
    ]
)

# ── 5. CUSTOMER RESPONSIBILITIES ─────────────────────────────────────────────
d.page_break()
d.h1("Customer Responsibilities and Dependencies")
d.para(
    "The successful delivery of this engagement within the agreed timeline depends on active, "
    "timely participation from [Customer Organization]. The following responsibilities are not "
    "optional elements of the engagement — they are structural dependencies that gate ECS’s "
    "ability to build, validate, and deliver on schedule. ECS will provide reasonable advance "
    "notice of each dependency so [Customer Organization] can plan accordingly."
)

d.h2("Sprint 0 / Pre-Build Dependencies (Required by Week [X])")
d.bullet("Completed Accelerator Pack workbooks for Foundation Data (users, locations, departments, groups, assignment rules, schedules, SLAs) — ECS will provide templates.")
d.bullet("SSO/AD configuration details and access to a technical SME for integration review.")
d.bullet("Provisioned development and test environments with admin-level ECS access.")
d.bullet("Named Product Owner with authority to make acceptance decisions on behalf of [Customer Organization].")
d.bullet("Named SMEs per process area — at minimum: ITSM, Catalog, CMDB/Discovery, Employee Experience.")
d.bullet("Executive Sponsor confirmed and available for governance cadence (bi-weekly, 45 minutes).")

d.h2("Ongoing Engagement Responsibilities")
d.bullet("SME availability for workshops and validation sessions as scheduled by ECS — minimum [X] hours per sprint per process area.")
d.bullet("User story acceptance decisions within [3] business days of demo delivery; delays beyond this window may push stories to the next sprint.")
d.bullet("Governance Triage Log review and disposition within [5] business days of ECS submission.")
d.bullet("Data quality ownership: [Customer Organization] is responsible for the accuracy and completeness of data loaded via Accelerator Pack workbooks.")
d.bullet("Change Advisory Board participation: [Customer Organization] CAB members to be available for Change Management configuration workshops in Sprint 4.")
d.bullet("UAT execution: [Customer Organization] assigns and makes available testers with sufficient platform knowledge to execute UAT scenarios within the defined UAT window.")
d.bullet("Training and adoption: [Customer Organization] is responsible for end-user communication, change management, and adoption activities beyond the train-the-trainer sessions delivered by ECS.")

d.callout(
    "ECS will flag any approaching dependency milestone at least [5] business days in advance. "
    "If a dependency is at risk, ECS and [Customer Organization] will jointly assess the timeline "
    "impact and document it in the sprint workbook before it becomes a delay."
)

# ── 6. OUT OF SCOPE ──────────────────────────────────────────────────────────
d.page_break()
d.h1("Out of Scope")
d.para(
    "The following items are explicitly excluded from the Phase 1 scope of this SOW. Requirements "
    "in any of these categories that emerge during the engagement will be captured in the "
    "Governance Triage Log and may be addressed through a Project Change Request or deferred to "
    "a subsequent phase."
)
d.bullet("Any ServiceNow application or module not listed in Section 2.")
d.bullet("Custom scripting, modification of protected baseline objects, or creation of custom tables outside of Project Sponsor–approved deviations.")
d.bullet("Any third-party integration not explicitly named in Section 2.")
d.bullet("Data migration of historical incident, change, or request records (data migration scope, if applicable, is addressed separately).")
d.bullet("End-user training delivery beyond train-the-trainer and admin knowledge transfer sessions.")
d.bullet("ServiceNow licensing procurement or license advisory (ECS will surface licensing observations but does not act as a licensing agent).")
d.bullet("Ongoing platform administration, break-fix, or managed services after the Hypercare period.")
d.bullet("Phase 2, Phase 3, or roadmap capabilities identified in Section [X] of this SOW — those phases require a separate SOW.")
d.bullet("[Any customer-specific exclusion, e.g., portal redesign, legacy system decommission, etc.]")

# ── 7. ASSUMPTIONS ────────────────────────────────────────────────────────────
d.h1("Assumptions")
d.para(
    "This SOW and the associated timeline are based on the following assumptions. If any "
    "assumption proves incorrect or changes during the engagement, ECS will assess the impact "
    "and may initiate a PCR discussion."
)
d.bullet("[Customer Organization] will have a clean [net-new / dedicated] ServiceNow instance provisioned and ECS-accessible by the start of Sprint 0.")
d.bullet("ECS has been granted admin-level access to all development and test environments required for this engagement.")
d.bullet("The ServiceNow version targeted for this implementation is [Washington / Xanadu / Vancouver — specify] or later.")
d.bullet("All [Customer Organization] SMEs named for this engagement have authority to make design decisions within their process area, subject to Product Owner acceptance.")
d.bullet("The [X] catalog items in scope have been prioritized and the top [10–15] are identified and agreed upon by [Customer Organization] prior to Sprint 2.")
d.bullet("Discovery and Service Graph Connector configurations from the existing instance are accessible for review by ECS and [Customer Organization] SMEs during Sprint 1.")
d.bullet("ECS will operate under a [fixed-fee / time-and-materials] model as defined in Section 12. Additional scope is addressed via PCR, not change to the base fee.")

# ── 8. GUARDRAILS AND PCR TRIGGERS ───────────────────────────────────────────
d.page_break()
d.h1("Project Guardrails and PCR Process")
d.para(
    "ECS and [Customer Organization] share a mutual interest in protecting the timeline, the "
    "agreed budget, and the OOTB-first discipline that makes Phase 1 valuable. The guardrails "
    "and Project Change Request (PCR) process below are designed to surface impacts early, "
    "preserve transparency, and give both parties the information needed to make sound decisions "
    "— not to create friction or assign blame. When a trigger is reached, ECS will raise it "
    "as a conversation first and a formal PCR only if the impact cannot be absorbed within the "
    "current sprint plan."
)

d.h2("Scope Boundary Definitions")
d.para(
    "The OOTB Baseline defines the scope specifically as the implementation and configuration of "
    "out-of-the-box ServiceNow functionality as defined by ServiceNow Product Documentation for "
    "all in-scope applications listed in Section 2."
)
d.table(
    headers=["Term", "Definition"],
    rows=[
        ["OOTB Configuration", "Use of standard ServiceNow fields, tables, workflows, UI policies, and Flow Designer without modification of baseline objects."],
        ["Governed Deviation", "A delta from OOTB that has been reviewed by the Customization Council, documented in the Governance Triage Log, and approved by the Project Sponsor."],
        ["Customization", "Any requirement that cannot be met by Configuration, UI Policy, or Flow Designer alone. Triggers mandatory technical review and Project Sponsor approval before work begins."],
        ["Structural Deviation", "Use of custom tables instead of standard CI classes, or modification of core platform objects. Requires Project Sponsor approval and automatic escalation to the Customization Council."],
        ["Project Change Request (PCR)", "A formal document initiated by ECS that describes a scope, timeline, or resource impact and proposes a resolution. Both parties must sign a PCR before ECS proceeds with out-of-scope work."],
    ]
)

d.h2("PCR Triggers: Customer-Initiated Scope Changes")
d.para(
    "The following conditions, when initiated by [Customer Organization], will trigger a PCR "
    "discussion. ECS will document the trigger in writing within [2] business days of "
    "identification and schedule a PCR conversation within [3] business days."
)
d.bullet(
    "Requirements beyond the OOTB Baseline: Any requirement that necessitates custom scripting, "
    "modification of protected baseline objects, or creation of custom tables not listed in "
    "Section 2. ECS will present the OOTB alternative before raising the PCR."
)
d.bullet(
    "Expansion of in-scope catalog items: Requests to add catalog items beyond the agreed "
    "[–10–15] items will be assessed for sprint capacity impact. Items that displace "
    "agreed-scope work require a PCR."
)
d.bullet(
    "Addition of in-scope applications or integrations: Any application, module, or integration "
    "not listed in Section 2. No work begins on out-of-scope items without an executed PCR."
)
d.bullet(
    "Process redesign requests: Requests to redesign an existing OOTB process beyond the "
    "configuration decisions captured in workshops. Redesign typically signals a Customization "
    "and triggers the Rule of Three review."
)
d.bullet(
    "Significant volume increases: Material increases in the number of user stories, locations, "
    "groups, assignment rules, or catalog taxonomy entries beyond what was baselined in the "
    "Accelerator Packs."
)

d.h2("PCR Triggers: Schedule and Dependency Impacts")
d.para(
    "The following conditions, regardless of which party initiates them, may trigger a PCR for "
    "timeline extension. ECS’s obligation is to flag the risk as soon as it is identified "
    "and to work collaboratively on mitigation before formalizing a PCR."
)

d.bullet(
    "Accelerator Pack data not delivered on time: Foundation Data workbooks (users, locations, "
    "groups, SLAs, assignment rules) are required by Sprint 0 to enable build. If completed "
    "workbooks are not received within [5] business days of the agreed delivery date, ECS will "
    "document the delay and assess the timeline impact. Delays that push build start beyond "
    "Sprint 1 Week 1 may result in a PCR for timeline and/or fee adjustment."
)
d.bullet(
    "SME unavailability: If a named SME is unavailable for a scheduled workshop or validation "
    "session and no qualified substitute is provided with [2] business days’ notice, ECS "
    "will reschedule the session. If repeated unavailability (defined as [2] or more missed "
    "sessions in a single sprint) causes sprint goals to slip, ECS will initiate a PCR discussion."
)
d.bullet(
    "Decision delays: User story acceptance decisions are expected within [3] business days of "
    "demo delivery. Governance Triage Log dispositions are expected within [5] business days of "
    "ECS submission. Decisions outstanding beyond these windows will be documented in the sprint "
    "workbook; accumulated delays that affect the sprint plan trigger a PCR conversation."
)
d.bullet(
    "Environment or access delays: If provisioned environments or admin credentials are not "
    "available as committed and ECS is blocked from building for more than [3] consecutive "
    "business days, ECS will document the blockage and assess timeline impact. Sustained "
    "blockage may result in a PCR."
)
d.bullet(
    "Third-party vendor delays: If a third-party vendor (e.g., AD/SSO provider, SCCM/Intune "
    "administrator) required for an in-scope integration is not available within the sprint "
    "window, ECS will document the dependency and may adjust sprint sequencing. If the delay "
    "affects the critical path, a PCR will be initiated."
)
d.bullet(
    "Executive Sponsor escalation hold: If a governance decision requires Executive Sponsor "
    "input and that input is not received within [5] business days of escalation, ECS will "
    "document the hold and assess downstream impact."
)

d.callout(
    "GUARDRAIL PRINCIPLE: A PCR is not a penalty. It is a shared acknowledgment that "
    "circumstances have changed and that ECS and [Customer Organization] need to agree on "
    "how to proceed. ECS will always present mitigation options alongside a PCR trigger — "
    "the goal is a decision, not a dispute."
)

d.h2("PCR Process")
d.para("When a PCR trigger is reached, the following process applies:")
d.table(
    headers=["Step", "Owner", "Timeframe", "Action"],
    rows=[
        ["1. Identify", "ECS", "Within 2 business days of trigger", "ECS documents the trigger, the impact assessment, and the proposed resolution in a PCR document."],
        ["2. Notify", "ECS", "Within 1 business day of Step 1", "ECS delivers the PCR document to [Customer Organization] Project Sponsor and Product Owner."],
        ["3. Review", "Both parties", "Within 3 business days of receipt", "[Customer Organization] reviews the PCR and may request a working session to discuss."],
        ["4. Decide", "Customer Sponsor", "Within 5 business days of receipt", "Customer Sponsor approves, modifies, or rejects the PCR in writing."],
        ["5. Execute", "ECS", "Upon PCR execution", "ECS proceeds with the approved scope/timeline change. No out-of-scope work begins before PCR execution."],
    ]
)
d.para(
    "PCRs that involve additional fees are subject to the same review and approval process. "
    "ECS will not invoice for PCR-related work until the PCR is executed by both parties."
)

d.h2("Governance Triage Log")
d.para(
    "All scope deviation requests, open questions, and deferred requirements are captured in "
    "the Governance Triage Log, a living artifact maintained by ECS and reviewed at each "
    "bi-weekly Sponsor Sync. The Log tracks the deviation, its business rationale, scope impact, "
    "and disposition (deferred to Phase 2 / approved as Governed Deviation / escalated for PCR). "
    "The Log is a feature of this engagement, not a warning sign — it is how both parties "
    "protect the baseline and the customer’s legitimate requirements simultaneously."
)

# ── 9. TESTING AND ACCEPTANCE ─────────────────────────────────────────────────
d.page_break()
d.h1("Testing and Acceptance")

d.h2("Testing Approach")
d.para(
    "ECS follows a continuous testing model throughout the build sprints, with formal User "
    "Acceptance Testing (UAT) conducted in Sprint [7]. Testing phases include:"
)
d.bullet("Unit Testing: ECS consultants validate each configuration against user story acceptance criteria before sprint demo.")
d.bullet("Sprint Demo Validation: Product Owner reviews configured capability at the end of each sprint and provides formal acceptance or identifies defects for the next sprint.")
d.bullet("Integration Testing: ECS validates end-to-end data flows across integrated systems in Sprint [6–7].")
d.bullet("UAT: [Customer Organization] executes test scenarios against a defined UAT script in the test environment. ECS provides the UAT script and facilitates sessions.")
d.bullet("Regression Testing: ECS performs regression validation prior to production cutover.")

d.h2("Acceptance Criteria")
d.para(
    "A configuration is accepted when the Product Owner confirms, in writing or via the sprint "
    "workbook, that all user story acceptance criteria have been met. Defects identified during "
    "sprint demos are classified as:"
)
d.bullet("P1 (Blocker): Prevents core process execution. ECS resolves within the sprint.")
d.bullet("P2 (Critical): Significant impact to user experience or process; ECS resolves in the next sprint.")
d.bullet("P3 (Enhancement): Desirable improvement not required for go-live. Captured in the Phase 2 backlog.")
d.para(
    "Go-live readiness requires [Customer Organization] sign-off on all P1 and P2 defects as "
    "resolved and written acceptance of the UAT results by the Product Owner and Executive Sponsor."
)

# ── 10. OCM AND TRAINING ──────────────────────────────────────────────────────
d.h1("Organizational Change Management and Training")
d.para(
    "ECS’s delivery scope includes the following knowledge transfer and enablement activities. "
    "Broader organizational change management, end-user communication, and adoption campaigns "
    "are [Customer Organization]’s responsibility."
)
d.bullet("Admin Knowledge Transfer (KT): [X] sessions covering platform administration, update set management, and OOTB governance principles.")
d.bullet("Train-the-Trainer sessions: [X] sessions per process area enabling [Customer Organization]’s designated trainers to deliver end-user training.")
d.bullet("Process documentation: ECS delivers design documentation per sprint. [Customer Organization] is responsible for translating these into internal procedures and training materials.")
d.bullet("Hypercare support: ECS provides [X] weeks of Hypercare support post go-live, available during business hours for production issues classified P1 or P2.")

# ── 11. GOVERNANCE MODEL ──────────────────────────────────────────────────────
d.page_break()
d.h1("Engagement Governance")

d.h2("Governance Cadence")
d.table(
    headers=["Cadence", "Participants", "Frequency", "Purpose"],
    rows=[
        ["Daily Stand-up", "ECS delivery team + [Customer] Product Owner", "Daily (15 min)", "Sprint progress, blockers, and dependency flags."],
        ["Sprint Review / Demo", "ECS + [Customer] Product Owner + Process SMEs", "Bi-weekly (end of sprint)", "Demo of completed stories; formal acceptance or defect logging."],
        ["Sprint Retrospective", "ECS delivery team + [Customer] Product Owner", "Bi-weekly (end of sprint)", "Process improvement and sprint planning."],
        ["Bi-Weekly Sponsor Sync", "ECS Engagement Manager + [Customer] Executive Sponsor", "Bi-weekly (45 min)", "Schedule health, Governance Triage Log review, PCR decisions."],
        ["Steering Committee", "ECS Practice Lead + [Customer] Sponsor + Stakeholders", "Monthly", "Program-level decisions, risk review, roadmap alignment."],
    ]
)

d.h2("Roles and Responsibilities")
d.table(
    headers=["Role", "Party", "Responsibilities"],
    rows=[
        ["Engagement Manager", "ECS", "Day-to-day delivery oversight, sprint planning, PCR management, Sponsor Sync facilitation."],
        ["Solution Architect", "ECS", "Technical design authority, OOTB-first discipline, architecture decisions, Customization Council chair."],
        ["Process Consultants", "ECS", "Workshop facilitation, configuration, user story delivery, sprint workbook maintenance."],
        ["Executive Sponsor", "[Customer]", "PCR approval authority, escalation resolution, program-level decisions, go-live sign-off."],
        ["Product Owner", "[Customer]", "User story acceptance, sprint backlog prioritization, Governance Triage Log dispositions."],
        ["Process SMEs", "[Customer]", "Subject matter input in workshops, UAT execution, knowledge transfer participation."],
        ["Platform Administrator", "[Customer]", "Environment provisioning, access management, post-go-live administration."],
    ]
)

# ── 12. TIMELINE AND PRICING ──────────────────────────────────────────────────
d.page_break()
d.h1("Timeline and Pricing")

d.h2("Phase 1 Timeline")
d.table(
    headers=["Phase", "Weeks", "Key Milestone"],
    rows=[
        ["Sprint 0: Initiate & Plan", "Week 1–2", "Kickoff, governance established, Accelerator Pack data collected, environments provisioned."],
        ["Month 1: Foundation & Discovery", "Weeks 3–6", "Platform architecture, CSDM, ITSM design, Discovery/Connectors initiated."],
        ["Month 2: Core Build", "Weeks 7–10", "ITSM Core, Change Management, first catalog items."],
        ["Month 3: Advanced Features", "Weeks 11–14", "Employee Experience, HAM, remaining catalog items, environment stabilization."],
        ["Month 4: Validation & Go-Live", "Weeks 15–18", "UAT, Knowledge Transfer, cutover, Hypercare begins."],
        ["Hypercare", "Weeks 19–[X]", "[X]-week post-go-live support window."],
    ]
)

d.h2("Phase 1 Pricing")
d.callout("INTERNAL NOTE (REMOVE BEFORE SENDING): Complete the pricing table below with the Engagement Manager and Practice Lead before issuing this SOW. All figures require Practice Lead sign-off.")
d.table(
    headers=["Item", "Description", "Fee"],
    rows=[
        ["Phase 1 Fixed Fee", "Delivery of all in-scope capabilities as defined in Section 2, including Sprint 0 through Hypercare.", "$[Amount]"],
        ["Travel and Expenses", "Estimated travel for on-site workshops ([X] trips of [X] days each). Actuals billed as incurred.", "$[Estimate]"],
        ["Out-of-Scope / PCR Work", "Billed at the agreed blended rate of $[Rate]/hour upon executed PCR.", "As incurred"],
        ["Phase 1 Total (Estimated)", "", "$[Total]"],
    ]
)

d.h2("Payment Schedule")
d.table(
    headers=["Milestone", "Payment", "Trigger"],
    rows=[
        ["Contract Execution", "[X]%", "Upon execution of this SOW."],
        ["Sprint 0 Complete", "[X]%", "Upon written acceptance of Sprint 0 deliverables."],
        ["Month 1 Complete", "[X]%", "Upon written acceptance of Sprint 1–2 deliverables."],
        ["Month 2 Complete", "[X]%", "Upon written acceptance of Sprint 3–4 deliverables."],
        ["Month 3 Complete", "[X]%", "Upon written acceptance of Sprint 5–6 deliverables."],
        ["Go-Live", "[X]%", "Upon execution of production cutover and written go-live acceptance."],
    ]
)

# ── 13. LONG-TERM ROADMAP ────────────────────────────────────────────────────
d.page_break()
d.h1("Long-Term Roadmap: Beyond Phase 1")
d.para(
    "Phase 1 delivers the OOTB baseline that unlocks [Customer Organization]’s full "
    "ServiceNow investment. The following phases are not in scope for this SOW and will be "
    "addressed in separate engagements, but are summarized here to provide [Customer "
    "Organization]’s leadership with a view of the full value trajectory."
)

d.h2("Phase 2: Baseline Expansion and Enhanced User Experience")
d.bullet("Expanded Service Catalog: Additional catalog items and directed workflows for services captured in the Phase 1 generic workflow buckets.")
d.bullet("Enhanced Virtual Agent: Additional topic coverage and integration with backend systems.")
d.bullet("Broader HAM Realization: Full asset lifecycle, procurement integration, and disposal workflows.")
d.bullet("Governed Deviations Backlog: Triage Log items deferred from Phase 1 assessed for implementation.")

d.h2("Phase 3: ITOM and Intelligence")
d.bullet("Event Management foundations and AIOps integration.")
d.bullet("Service Mapping and Business Service topology.")
d.bullet("Advanced Predictive Intelligence models and Task Intelligence tuning.")
d.bullet("Now Assist and Agentic Agents activation.")

d.h2("Phase 4 and Beyond: Full AI Realization")
d.bullet("Workflow Data Fabric integration.")
d.bullet("Cross-domain automation and orchestration.")
d.bullet("Continuous platform optimization and innovation cadence.")
d.callout(
    "Each phase builds directly on the OOTB foundation established in Phase 1. Skipping or "
    "compromising the baseline in Phase 1 creates rework in every subsequent phase. "
    "The investment in OOTB discipline now is the investment in AI realization later."
)

# ── 14. TERMS AND CONDITIONS ─────────────────────────────────────────────────
d.page_break()
d.h1("Terms and Conditions")

d.h2("Term of Engagement")
d.para(
    "This SOW is effective upon execution by both parties and remains in effect through the "
    "completion of the Hypercare period, unless earlier terminated in accordance with this Section."
)

d.h2("Termination for Convenience")
d.para(
    "Either party may terminate this SOW for convenience upon [30] days’ written notice. "
    "In the event of termination by [Customer Organization] for convenience, [Customer "
    "Organization] shall pay ECS for all work completed through the termination date, plus "
    "reasonable wind-down costs not to exceed [X]% of the remaining contract value."
)

d.h2("Termination for Cause")
d.para(
    "Either party may terminate this SOW for material breach upon [15] days’ written notice "
    "if the breaching party fails to cure the breach within the notice period. ECS’s "
    "liability for termination for cause shall not exceed fees paid for the relevant work "
    "product that gave rise to the breach."
)

d.h2("Intellectual Property")
d.para(
    "ECS retains ownership of all methodologies, accelerator frameworks, templates, and "
    "reusable intellectual property developed by ECS prior to or independently of this "
    "engagement. All customer-specific configurations, design documents, and deliverables "
    "produced exclusively for [Customer Organization] under this SOW are owned by "
    "[Customer Organization] upon full payment of all fees due."
)

d.h2("Confidentiality")
d.para(
    "Both parties agree to maintain the confidentiality of the other’s non-public "
    "information disclosed in connection with this engagement for a period of [3] years "
    "following the expiration or termination of this SOW, consistent with the terms of "
    "any Master Services Agreement (MSA) or Non-Disclosure Agreement (NDA) between the parties."
)

d.h2("Limitation of Liability")
d.para(
    "ECS’s total liability under this SOW shall not exceed the total fees paid by "
    "[Customer Organization] in the [3] months preceding the event giving rise to the claim. "
    "Neither party shall be liable for indirect, incidental, or consequential damages."
)

d.h2("Governing Law")
d.para(
    "This SOW is governed by the laws of the State of [State], without regard to conflict "
    "of law principles. Any disputes shall be resolved in accordance with the dispute "
    "resolution provisions of the parties’ MSA, or, absent an MSA, by binding arbitration "
    "in [City, State]."
)

d.h2("Order of Precedence")
d.para(
    "In the event of conflict between this SOW and any Master Services Agreement between "
    "the parties, the MSA shall take precedence except with respect to the specific scope, "
    "timeline, and pricing defined herein."
)

# ── 15. SIGNATURE BLOCK ───────────────────────────────────────────────────────
d.page_break()
d.h1("Signature Block")
d.para(
    "By signing below, both parties agree to the terms, scope, and conditions set forth in "
    "this Statement of Work."
)

d.table(
    headers=["ECS Federal", "[Customer Organization]"],
    rows=[
        ["Signature: ________________________", "Signature: ________________________"],
        ["Name: ____________________________", "Name: ____________________________"],
        ["Title: ____________________________", "Title: ____________________________"],
        ["Date: _____________________________", "Date: _____________________________"],
    ]
)

d.para("") # spacing
d.para(
    "Project Sponsor Acknowledgment ([Customer Organization]) — The Project Sponsor named below "
    "confirms their availability and authority as described in Section 5 and Section 8 of this SOW."
)
d.table(
    headers=["Project Sponsor Acknowledgment"],
    rows=[
        ["Signature: ________________________"],
        ["Name: ____________________________"],
        ["Title: ____________________________"],
        ["Date: _____________________________"],
    ]
)

# ── 16. ACRONYMS ─────────────────────────────────────────────────────────────
d.page_break()
d.h1("Acronyms", numbered=False)
d.table(
    headers=["Acronym", "Definition"],
    rows=[
        ["AD", "Active Directory"],
        ["CAB", "Change Advisory Board"],
        ["CI", "Configuration Item"],
        ["CMDB", "Configuration Management Database"],
        ["CSDM", "Common Service Data Model"],
        ["ECS", "Everforth Consulting Services"],
        ["HAM", "Hardware Asset Management"],
        ["ITSM", "IT Service Management"],
        ["KM", "Knowledge Management"],
        ["KT", "Knowledge Transfer"],
        ["MSA", "Master Services Agreement"],
        ["MTTR", "Mean Time to Resolution"],
        ["MVP", "Minimum Viable Platform"],
        ["NDA", "Non-Disclosure Agreement"],
        ["OCM", "Organizational Change Management"],
        ["OOTB", "Out of the Box"],
        ["PA", "Platform Analytics"],
        ["PCR", "Project Change Request"],
        ["PI", "Predictive Intelligence"],
        ["SAM", "Software Asset Management"],
        ["SCCM", "System Center Configuration Manager (Microsoft)"],
        ["SLA", "Service Level Agreement"],
        ["SME", "Subject Matter Expert"],
        ["SOW", "Statement of Work"],
        ["SSO", "Single Sign-On"],
        ["UAT", "User Acceptance Testing"],
        ["VA", "Virtual Agent"],
    ]
)


d.save(OUT)
print(f"Saved: {OUT}")
