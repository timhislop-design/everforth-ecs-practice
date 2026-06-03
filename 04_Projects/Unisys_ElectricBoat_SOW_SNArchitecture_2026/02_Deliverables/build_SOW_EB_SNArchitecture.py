"""
Build script: ECS Unisys Electric Boat SN Architecture Services SOW
Output: SOW_Unisys_ElectricBoat_SNArchitecture_2026.docx
"""
import sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

OUT = os.path.join(HERE, "SOW_Unisys_ElectricBoat_SNArchitecture_2026.docx")

doc = EcsDocument(meta=DocMeta(
    eyebrow="CLIENT · STATEMENT OF WORK",
    title="ServiceNow Architecture Services\nStatement of Work",
    subtitle="High Availability Environment Rebuild — Electric Boat / General Dynamics",
    audience="Unisys · Electric Boat (General Dynamics)",
    companion_to="Unisys – Electric Boat ServiceNow Support Services SOW (O&M)",
    doc_id="SOW-EB-001",
    version="1.0",
    status="Draft",
    running_header_label="Client · SN Architecture Services SOW",
    footer_left="ECS Federal · ServiceNow Practice · Confidential",
))

doc.add_cover_page()
doc.page_break()

# ── 1. EXECUTIVE OVERVIEW ────────────────────────────────────────────────────
doc.h1("Executive Overview", numbered=True)
doc.para(
    "Everforth ECS Federal ((ECS)) is engaged as a subcontractor to Unisys in support of "
    "Unisys's prime contract with Electric Boat (EB), a subsidiary of General Dynamics. As "
    "part of that engagement, Electric Boat operates an on-premise installation of ServiceNow "
    "that Unisys is contractually obligated to manage and maintain."
)
doc.para(
    "The current ServiceNow environment lacks sufficient compute capacity—processing power and "
    "RAM—and has no reliability redundancy across its environment tiers. This creates operational "
    "risk and, under the terms of Unisys's contract renewal with Electric Boat, now creates a "
    "contractual compliance risk: EB's renewed contract requires 99.99% uptime (fewer than 53 "
    "minutes of downtime per year across all tiers)."
)
doc.para(
    "This Statement of Work defines the services ECS will perform to design, build, and migrate "
    "Electric Boat's ServiceNow environment to a new, high-availability architecture across all "
    "tiers (PROD, UAT, and DEV), spanning two data centers with global load balancing, RaptorDB "
    "Professional database infrastructure, and automated database failover. Post-migration "
    "operational support is governed under a separate Unisys–Electric Boat ServiceNow Support "
    "Services agreement and is explicitly outside the scope of this engagement."
)

# ── 2. REQUESTED ARCHITECTURE ────────────────────────────────────────────────
doc.h1("Requested Architecture", numbered=True)
doc.para(
    "The following architecture has been specified by Unisys and Electric Boat to meet the "
    "99.99% uptime contractual requirement. ECS will deliver against these specifications "
    "across three environment tiers."
)

doc.h2("PROD Environment")
doc.bullet("Expand application node hosts by two (2) in PROD")
doc.bullet(
    "Final configuration: two (2) application servers in DataCenter 1 and two (2) application "
    "servers in DataCenter 2, providing both single-site and cross-site high availability"
)
doc.bullet("Leverage Global Server Load Balancing (GSLB) on F5s for application nodes")
doc.bullet(
    "GSLB provides a VIP in each data center, managing traffic in an active/passive fashion "
    "to deliver single-site and cross-site high availability"
)
doc.bullet("Migrate MariaDB to RaptorDB, targeting RaptorDB Professional")
doc.bullet(
    "Database placement: Primary, Replica, and Witness servers in DataCenter 1; two (2) "
    "Replica servers in DataCenter 2 — providing both single-site and cross-site HA"
)
doc.bullet("Leverage GSLB on F5s for database tier")
doc.bullet(
    "Implement automated high availability for databases beyond simple replication, per "
    "ServiceNow KB2407699 — using repmgr or Patroni (Distributed Configuration Store)"
)
doc.bullet("Two (2) Predictive Intelligence Servers — listed as an optional line item")

doc.h2("UAT Environment")
doc.bullet("Expand application node hosts by one (1) in UAT")
doc.bullet(
    "Final configuration: two (2) application servers in DataCenter 1 and two (2) application "
    "servers in DataCenter 2"
)
doc.bullet("Leverage GSLB on F5s for application nodes — active/passive VIP per data center")
doc.bullet("Provides cross-site high availability")
doc.bullet("Migrate MariaDB to RaptorDB, targeting RaptorDB Professional")
doc.bullet(
    "Database placement: Primary and Witness servers in DataCenter 1; one (1) Replica server "
    "in DataCenter 2"
)
doc.bullet("Leverage GSLB on F5s for database tier")
doc.bullet(
    "Implement automated high availability for databases per ServiceNow KB2407699 "
    "(repmgr or Patroni)"
)
doc.bullet("Two (2) Predictive Intelligence Servers — optional line item")

doc.h2("DEV Environment")
doc.bullet("Migrate MariaDB to RaptorDB, targeting RaptorDB Professional")
doc.bullet("Database placement: Primary server in DataCenter 1. No replicas.")
doc.bullet("Two (2) Predictive Intelligence Servers — optional line item")

doc.h2("Architectural Overview")
doc.para(
    "The combined architecture delivers three tiers of availability protection: in-site high "
    "availability within each data center, cross-site high availability across DataCenter 1 and "
    "DataCenter 2, and cold/warm-site disaster recovery capability. F5 GSLB is the traffic "
    "management layer for both application and database tiers. RaptorDB Professional with "
    "repmgr or Patroni provides automated database failover that exceeds the capability of "
    "simple replication, satisfying the uptime requirement without reliance on manual "
    "intervention."
)
doc.callout(
    "Target Uptime SLA: 99.99% — fewer than 53 minutes of unplanned downtime per year. "
    "This is a contractual commitment between Unisys and Electric Boat. This architecture "
    "is designed to meet that requirement."
)

# ── 3. SCOPE OF SERVICES ─────────────────────────────────────────────────────
doc.h1("Scope of Services", numbered=True)
doc.para(
    "ECS will provide the following services under this Statement of Work. All work will be "
    "performed remotely unless travel is explicitly requested and approved in writing by Unisys."
)

doc.h2("Architecture Design and Documentation")
doc.bullet("Document the current-state ServiceNow architecture across all environment tiers")
doc.bullet(
    "Design the target-state high availability architecture in alignment with the specifications "
    "in Section 2"
)
doc.bullet(
    "Produce architecture diagrams and supporting documentation for Unisys and EB review "
    "and approval prior to build"
)
doc.bullet("Identify and document required infrastructure dependencies (F5, server provisioning, network)")

doc.h2("Environment Build — DEV, UAT, PROD")
doc.bullet("Build new ServiceNow environments in the specified sequence: DEV first, UAT second, PROD last")
doc.bullet("Configure RaptorDB Professional across all tiers per the architecture specification")
doc.bullet("Coordinate with EB infrastructure teams on F5 GSLB configuration")
doc.bullet(
    "Configure repmgr or Patroni for automated database high availability per ServiceNow "
    "KB2407699 guidance"
)
doc.bullet("Configure application node distribution across DataCenter 1 and DataCenter 2")
doc.bullet("Install and configure Predictive Intelligence servers (optional — if authorized)")

doc.h2("Testing")
doc.bullet("Unit and integration testing throughout the build of each environment tier")
doc.bullet("Failover testing — simulated single-site and cross-site failure scenarios")
doc.bullet(
    "Performance validation — confirm resource capacity meets current load and projected growth"
)
doc.bullet("Coordinate User Acceptance Testing (UAT) with EB stakeholders prior to PROD migration")

doc.h2("Migration")
doc.bullet("Develop and document a migration plan for each environment tier")
doc.bullet("Execute migration from legacy environment to new architecture")
doc.bullet(
    "Coordinate Change Advisory Board (CAB) approval through Unisys and EB change management "
    "process prior to PROD migration execution"
)
doc.bullet("Validate post-migration system health across all tiers")
doc.bullet("Confirm go-live readiness with Unisys and EB stakeholders")

doc.h2("Project Management and Communication")
doc.bullet("Provide weekly status reports to Unisys")
doc.bullet("Maintain a project schedule and issue/risk log")
doc.bullet("Facilitate regular coordination calls with Unisys and EB stakeholders")
doc.bullet(
    "Manage ECS internal team coordination, task assignment, and quality assurance "
    "throughout the engagement"
)

doc.h2("Out of Scope")
doc.bullet(
    "Ongoing operational support and managed services — governed under the separate "
    "Unisys–Electric Boat ServiceNow Support Services agreement"
)
doc.bullet(
    "ServiceNow platform licensing — Electric Boat's responsibility as the licensed customer"
)
doc.bullet(
    "Physical infrastructure provisioning (servers, networking equipment, data center "
    "facilities) — Electric Boat's responsibility"
)
doc.bullet("Travel costs — excluded unless requested and approved in writing by Unisys")
doc.bullet("Customization or functional configuration of ServiceNow modules beyond the architecture scope")

# ── 4. PROJECT APPROACH AND TIMELINE ─────────────────────────────────────────
doc.h1("Project Approach and Timeline", numbered=True)
doc.para(
    "This engagement is planned for fourteen (14) weeks, with a ceiling of sixteen (16) weeks "
    "to accommodate infrastructure provisioning dependencies outside ECS's control. The "
    "sequencing prioritizes DEV first to validate the build approach before applying it to "
    "UAT and PROD."
)

doc.h2("Month 1 — Discovery, Architecture, and Preparation (Weeks 1–4)")
doc.bullet("Conduct project kickoff with Unisys and EB stakeholders")
doc.bullet("Identify and confirm SME contacts, points of contact, and escalation paths")
doc.bullet("Document current-state architecture across PROD, UAT, and DEV")
doc.bullet("Design and document target-state architecture; obtain Unisys and EB approval")
doc.bullet("Verify and validate access to all required environments and infrastructure")
doc.bullet("Coordinate with EB to confirm server provisioning timelines and F5 access")
doc.bullet("Initiate the Unisys/EB Change Management process for planned environment work")
doc.bullet("Prepare detailed build runbooks for each environment tier")

doc.h2("Month 2 — Environment Build (Weeks 5–10)")
doc.bullet("Build DEV environment first: RaptorDB migration, PI server configuration, validation")
doc.bullet("Build UAT environment: app node expansion, RaptorDB, GSLB configuration, F5 coordination")
doc.bullet("Conduct integration and failover testing in DEV and UAT")
doc.bullet("Coordinate UAT sign-off with EB stakeholders")
doc.bullet("Begin PROD environment build in parallel with UAT validation")
doc.bullet("Ongoing status reporting and stakeholder coordination throughout")

doc.h2("Month 3 — PROD Finalization, Migration, and Go-Live (Weeks 11–14)")
doc.bullet("Finalize PROD environment build and testing")
doc.bullet("Conduct PROD failover and performance validation")
doc.bullet("Develop and review detailed migration plan with Unisys and EB")
doc.bullet("Obtain CAB approval for production migration through Unisys/EB change process")
doc.bullet("Execute production migration during approved change window")
doc.bullet("Validate post-migration system health and confirm 99.99% uptime architecture is operational")
doc.bullet("Conduct project closeout with Unisys and EB; transfer documentation package")

# ── 5. ROLES AND RESPONSIBILITIES ────────────────────────────────────────────
doc.h1("Roles and Responsibilities", numbered=True)

doc.h2("Everforth ECS Federal")
doc.para("ECS is responsible for delivery of all services defined in Section 3, including:")
doc.bullet("All architecture design, build, testing, and migration activities")
doc.bullet("Project management, scheduling, status reporting, and internal team coordination")
doc.bullet("Documentation of architecture, migration plans, and test results")
doc.bullet(
    "Coordination with Unisys on change management, escalations, and contract-level decisions"
)
doc.bullet("Technical quality assurance across all environment tiers")

doc.h2("Unisys")
doc.para("As the prime contractor, Unisys is responsible for:")
doc.bullet(
    "Contract and relationship management with Electric Boat — ECS escalates to Unisys "
    "for all customer-level decisions and approvals"
)
doc.bullet("Coordination of EB stakeholder and SME availability for architecture review, testing, and go-live")
doc.bullet(
    "Escalation of issues requiring EB action (infrastructure provisioning, change approvals, "
    "access requests)"
)
doc.bullet("Review and approval of ECS status reports, architecture documentation, and migration plans")
doc.bullet("Contractual coordination of the Unisys/EB change management process")

doc.h2("Electric Boat / General Dynamics")
doc.para("Electric Boat is responsible for infrastructure ownership and organizational coordination, including:")
doc.bullet(
    "Timely provisioning of servers, network infrastructure, and data center resources "
    "required to support the build timeline"
)
doc.bullet(
    "F5 configuration support — EB infrastructure teams own the F5 appliances and must "
    "coordinate GSLB configuration with ECS"
)
doc.bullet("SME availability for architecture review, UAT sign-off, and migration go-live approval")
doc.bullet("CAB process — Electric Boat's change advisory process governs all PROD environment changes")
doc.bullet("ServiceNow platform licensing and license management")
doc.bullet(
    "Maintaining supported ServiceNow versions on all tiers throughout the engagement"
)

# ── 6. PROJECT RESOURCES ─────────────────────────────────────────────────────
doc.h1("Project Resources", numbered=True)
doc.para(
    "ECS will staff the following roles for the duration of this engagement. All resources "
    "are remote unless otherwise agreed."
)
doc.table(
    headers=["Role", "Responsibilities"],
    rows=[
        [
            "Engagement Manager",
            "Project management, scheduling, stakeholder communication, status reporting, "
            "risk and issue management, ECS team coordination"
        ],
        [
            "Business Analyst",
            "Architecture documentation, testing coordination, requirements capture, "
            "migration plan documentation, general BA support"
        ],
        [
            "Platform Architect",
            "Lead architect responsible for target-state design, build execution, "
            "RaptorDB and GSLB configuration, failover design and validation"
        ],
        [
            "Developer",
            "General configuration support, build assistance, peer testing, "
            "post-migration validation support"
        ],
    ]
)

# ── 7. DEPENDENCIES ───────────────────────────────────────────────────────────
doc.h1("Dependencies", numbered=True)
doc.para(
    "The following dependencies are outside ECS's direct control and represent the primary "
    "schedule risk for this engagement. ECS will flag these early and track them throughout."
)
doc.bullet(
    "Infrastructure provisioning timeline — server provisioning and data center readiness "
    "are owned by Electric Boat. Delays in provisioning will directly impact the build schedule."
)
doc.bullet(
    "F5 GSLB configuration — Electric Boat's infrastructure team must be available and "
    "responsive to support F5 configuration in both data centers."
)
doc.bullet(
    "SME availability — EB subject matter experts must be available for architecture review, "
    "UAT validation, and go-live approval windows. Scheduling conflicts will delay milestones."
)
doc.bullet(
    "Change Advisory Board (CAB) process — PROD migration requires CAB approval through "
    "Unisys and EB's change management process. CAB cadence and lead times are EB-controlled."
)
doc.bullet(
    "Access and credentials — ECS requires timely access to all environment tiers, "
    "infrastructure management systems, and relevant tooling. Delayed access provisioning "
    "will impact the Month 1 preparation phase."
)
doc.bullet(
    "Unisys coordination — as the prime, Unisys must be available to facilitate EB "
    "communication and escalate decisions in a timely manner."
)

# ── 8. ASSUMPTIONS ────────────────────────────────────────────────────────────
doc.h1("Assumptions", numbered=True)
doc.para("This Statement of Work is based on the following assumptions:")
doc.bullet("Electric Boat maintains supported ServiceNow versions on all environment tiers throughout the engagement.")
doc.bullet(
    "All work will be performed remotely. Travel is not included in the pricing below. "
    "If travel is required, it will be mutually agreed in writing and billed as a "
    "pass-through expense at cost."
)
doc.bullet(
    "EB-owned infrastructure (servers, data center facilities, F5 appliances, networking) "
    "will be provisioned and accessible within the timelines required to support the build schedule."
)
doc.bullet(
    "Unisys will coordinate EB stakeholder and SME availability; ECS does not have a direct "
    "contractual relationship with Electric Boat."
)
doc.bullet(
    "Pricing is based on T&M at a blended rate. Hours are estimated; actual hours billed "
    "will reflect work performed."
)
doc.bullet(
    "Post-environment operational support (monitoring, break/fix, managed services) is "
    "explicitly out of scope and is governed by the separate "
    "Unisys–Electric Boat ServiceNow Support Services agreement."
)
doc.bullet(
    "ServiceNow licensing, including any incremental licenses required for RaptorDB Professional "
    "or Predictive Intelligence, is Electric Boat's responsibility."
)
doc.bullet(
    "The Predictive Intelligence Server component in each environment tier is treated as an "
    "optional scope item and priced separately. Inclusion requires written authorization from Unisys."
)
doc.bullet(
    "ECS's scope is limited to the architecture, build, and migration work defined in this SOW. "
    "Functional configuration changes, module implementations, or enhancements to ServiceNow "
    "capabilities are out of scope."
)

# ── 9. PRICING ────────────────────────────────────────────────────────────────
doc.h1("Pricing", numbered=True)

doc.h2("Pricing Structure")
doc.para(
    "This engagement is priced as a Time and Materials (T&M) contract. ECS will bill "
    "at a blended hourly rate for all resources assigned to this engagement. Actual hours "
    "billed will reflect work performed; the estimate below represents the projected total "
    "for the fourteen (14) week base engagement."
)

doc.table(
    headers=["Description", "Detail"],
    rows=[
        ["Contract Type", "Time and Materials (T&M)"],
        ["Blended Hourly Rate", "$215.00 per hour"],
        ["Estimated Total Hours", "2,325 hours"],
        ["Estimated Total Cost", "$499,875"],
        ["Base Engagement Duration", "14 weeks (16-week ceiling)"],
        ["Travel", "Excluded — billed as pass-through if required and approved"],
        ["Optional: Predictive Intelligence Servers", "To be quoted separately upon written authorization"],
    ]
)

doc.para(
    "The estimated total reflects ECS's projection for the full engagement across all "
    "four roles (Engagement Manager, Business Analyst, Platform Architect, Developer) "
    "over fourteen weeks. Hours may be reallocated across roles as needed to respond to "
    "schedule conditions, provided the blended rate and total hours remain within the "
    "ceiling."
)
doc.callout(
    "Not-to-Exceed Authorization: Unless otherwise agreed in writing, ECS will not exceed "
    "$499,875 without prior written approval from Unisys. ECS will notify Unisys when "
    "cumulative billings reach 80% of the authorized ceiling."
)

# ── 10. PAYMENT TERMS ─────────────────────────────────────────────────────────
doc.h1("Payment Terms", numbered=True)

doc.h2("Invoicing")
doc.para(
    "Everforth ECS shall invoice Unisys monthly in arrears based on hours worked in the "
    "preceding month. Payment terms are net thirty (30) days from invoice date. Late payments "
    "shall accrue interest at the lesser of 1.5% per month or the maximum rate permitted by law."
)

doc.h2("Suspension for Non-Payment")
doc.para(
    "Everforth ECS may suspend services upon ten (10) business days' written notice for any "
    "invoiced amount more than thirty (30) days past due. Service Level commitments shall be "
    "suspended during any period of non-payment. Such suspension shall not constitute a breach "
    "by Everforth ECS."
)

doc.h2("Engagement Extension")
doc.para(
    "If the engagement is extended beyond the initial ceiling term, fees shall be subject to "
    "renegotiation. Any extension must be authorized in writing by Unisys prior to ECS "
    "performing additional work."
)

doc.h2("Taxes")
doc.para(
    "Fees are exclusive of all applicable taxes other than taxes on Everforth ECS's net income."
)

# ── 11. SUMMARY ───────────────────────────────────────────────────────────────
doc.h1("Summary", numbered=True)
doc.para(
    "This Statement of Work defines the scope, approach, responsibilities, and commercial "
    "terms under which Everforth ECS Federal will deliver ServiceNow architecture services "
    "to support Unisys's contractual obligations to Electric Boat / General Dynamics."
)
doc.para(
    "ECS will design and build a high-availability ServiceNow environment across three tiers "
    "(DEV, UAT, PROD) spanning two data centers, migrating from the current MariaDB installation "
    "to RaptorDB Professional with automated failover, deploying application node redundancy, "
    "and implementing F5 Global Server Load Balancing. The result will be an architecture "
    "capable of meeting Electric Boat's 99.99% uptime contractual requirement."
)
doc.para(
    "Post-migration operational support is explicitly out of scope and is governed by the "
    "separate Unisys–Electric Boat ServiceNow Support Services agreement."
)
doc.callout(
    "This document is a draft Statement of Work provided for discussion and review. It does "
    "not constitute a binding commitment. All terms, including pricing, are subject to "
    "revision until a mutually executed SOW is in place. In the event of conflict between "
    "this document and any executed agreement, the executed agreement shall control."
)

doc.save(OUT)
print(f"Written: {OUT}")
