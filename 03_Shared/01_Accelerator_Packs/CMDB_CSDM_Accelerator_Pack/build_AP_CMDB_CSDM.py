"""
Build AP — CMDB-CSDM Accelerator Pack
6 xlsx workbooks + 1 README docx, branded to the canonical ECS standard.

Scope: CSDM taxonomy layers, CI class selection, business/technical service definitions,
service-CI relationships, and CMDB governance baseline.

Sprint alignment: Month 1 — Sprint 1 (CSDM definition) and Sprint 2 (CMDB normalization).
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
TEMPLATES = os.path.join(REPO, "03_Shared", "00_Templates_and_Branding")
sys.path.insert(0, TEMPLATES)

from accelerator_pack_builder import TabContent, build_workbook
from ecs_template import EcsDocument, DocMeta

PACK_NAME = "CMDB-CSDM Accelerator Pack"

# =============================================================================
# WORKBOOK 1 — CSDM Service Taxonomy
# =============================================================================
wb1 = TabContent(
    workbook_title="01 — CSDM Service Taxonomy",
    pack_name=PACK_NAME,
    purpose="Defines the four-layer CSDM service taxonomy the customer will implement in ServiceNow: Foundational Data, Managed Objects, Business Applications, and Business Services. This workbook establishes the vocabulary and hierarchy that underpins every downstream CMDB, Catalog, and AI feature in the engagement.",
    who_fills="Customer-side: Enterprise Architect or IT Service Management Owner, working with the CIO/IT Director to confirm Business Service naming. ECS SA facilitates the first workshop; customer confirms the taxonomy in Weeks 1-2 of Sprint 1.",
    sprint_window="Sprint 1, Weeks 1–2",
    estimated_effort="4–6 hours across two workshops for a typical mid-market customer",
    related_workbooks=["02 CI Class Selection", "03 Business Service Definitions", "04 Technical Services & Apps", "Foundation Data Pack"],
    success_criteria=[
        "All four CSDM layers are named and the customer team understands how they relate.",
        "A complete list of Business Services is agreed, signed off by the IT Director or CIO.",
        "The service owner for each Business Service is identified by name and role.",
        "The mapping from Business Services down to Technical Services is drafted (can be refined in Sprint 2).",
        "OOTB CSDM domain is chosen (IT, HR, Facilities, or scoped subset) and agreed.",
    ],
    process_decisions=[
        ("Which CSDM domains are in scope for this engagement?",
         "IT domain only. Scope CSDM to the IT service portfolio. HR, Facilities, and Legal domains can be added in a future phase without restructuring what is built here.",
         "Including multiple domains in Sprint 1 adds 3–5 weeks of taxonomy work and delays every downstream build. The OOTB CSDM model is designed to layer on new domains incrementally."),
        ("Should we use ServiceNow's OOTB CSDM service classifications or define custom ones?",
         "Use OOTB CSDM classifications: Business Service, Technical Service, Application Service, and the standard supporting objects. Do not create custom CI classes to represent service layers.",
         "Custom service classification tables require upgrade maintenance and block PI and Virtual Agent from recognising service context. The OOTB model is the AI-readable contract."),
        ("How many levels of Business Service hierarchy are appropriate?",
         "Two levels maximum: primary Business Services (e.g., Email, ERP, HR Systems) and sub-services where operationally meaningful. Do not model every application as a top-level Business Service.",
         "Customers who model 80+ Business Services cannot maintain ownership, SLA assignment, or service health dashboards. A well-scoped OOTB CSDM has 10–25 Business Services for a mid-market IT portfolio."),
        ("Who owns a Business Service record in ServiceNow?",
         "A single named IT manager is the service owner. The IT Director or CIO approves the full list. Service ownership is a governance decision, not a technical one — resolve it before configuration.",
         "Shared ownership or committee ownership means nobody responds when the service health degrades. ServiceNow requires a single owner field on the Business Service record for assignment and escalation."),
        ("How should legacy application names map to the CSDM service model?",
         "Map legacy applications to Application Services under the appropriate Technical Service. Keep the legacy name in the 'alias' or 'short description' field rather than as the primary CI name.",
         "Legacy names are tribal knowledge. OOTB CSDM names services by what they deliver to the business, not by the product that happens to deliver it. The alias field preserves findability."),
        ("Should we model services we don't fully manage (e.g., SaaS vendors)?",
         "Yes, but as External Service records with the vendor as service owner. Do not skip SaaS services — they appear in incidents, requests, and outage communications regardless of who manages them.",
         "Omitting vendor-managed services creates orphaned incidents and breaks the service map. The External Service classification in OOTB CSDM handles this without requiring CI-level discovery of the vendor environment."),
    ],
    dependencies=[
        ("Foundation Data Pack — Departments and Business Units completed", "Required", "Customer IT Director", "End of Sprint 0", "Business Service ownership maps to Departments. Incomplete department data means service owners cannot be named."),
        ("ITSM Design Workshop outputs — service categories agreed", "Required", "ECS SA + Customer ITSM Owner", "Sprint 1 Wk 1", "Incident and Request categories must align with the Business Service taxonomy. Misalignment here causes rework in Sprints 3–4."),
        ("CIO/IT Director available for Business Service approval session", "Required", "Customer Project Sponsor", "Sprint 1 Wk 2", "Business Service names and owners must be approved by a business stakeholder, not just IT ops."),
        ("Existing CMDB or asset register for application inventory", "Recommended", "Customer IT Ops", "Sprint 1 Wk 1", "Even a partial existing list of applications shortens the taxonomy workshop by 2–3 hours."),
        ("Vendor list for SaaS/external services", "Recommended", "Customer Procurement", "Sprint 1 Wk 2", "Needed to populate External Service records and identify which services have no discovery data."),
    ],
    config_sections=[
        ("CSDM Domain Scope", [
            ("In-scope domain(s)", "IT", "Start with IT only. Expand to HR/Facilities in a future phase.", True),
            ("CSDM version targeting", "CSDM 4.0 (Vancouver+)", "Align to the ServiceNow version in use. CSDM 4.0 is the default from Vancouver onward.", False),
            ("Service classification model", "OOTB: Business Service > Technical Service > Application Service", "Do not create custom tables.", False),
        ]),
        ("Business Service Naming Standards", [
            ("Naming convention", "[Service Verb] + [Business Object] e.g., 'Deliver Email', 'Support ERP'", "Keep names outcome-oriented, not technology-oriented.", False),
            ("Maximum number of top-level Business Services (target)", "10–25", "More than 25 requires a service portfolio manager to maintain.", True),
            ("Sub-service levels allowed", "2 maximum", "Three or more levels become unmaintainable.", False),
            ("Service owner field", "Single named individual (not a group)", "Use the 'service owner' field on Business Service CI.", False),
        ]),
        ("External / Vendor Services", [
            ("Model vendor-managed SaaS?", "Yes — as External Service CI type", "Examples: Microsoft 365, Salesforce, Workday.", False),
            ("Discovery required for External Services?", "No — manually maintained records acceptable at MVP", "External Services are excluded from Discovery reconciliation rules.", False),
        ]),
    ],
    raci_rows=[
        ("Facilitate CSDM taxonomy workshop", "R/A", "C", "ECS SA runs the workshops; customer provides the business knowledge."),
        ("Define and name Business Services", "C", "R/A", "Customer IT Director owns the service list; ECS advises on OOTB best practice."),
        ("Assign service owners to each Business Service", "I", "R/A", "Pure customer governance decision."),
        ("Map legacy applications to CSDM Application Services", "R", "C", "ECS SA leads mapping; customer confirms names and technology ownership."),
        ("Identify External / Vendor services", "C", "R", "Customer procurement leads; ECS advises on CI classification."),
        ("Load Business Service CIs into ServiceNow", "R/A", "I", "ECS SA performs the configuration."),
        ("Validate service hierarchy in ServiceNow Service Map", "R", "A", "ECS validates technically; customer approves visually."),
        ("Approve final CSDM taxonomy", "I", "R/A", "Customer IT Director or CIO formally approves."),
    ],
    consultant_guide_sections=[
        ("Workshop approach", "Run two 90-minute workshops in Sprint 1 Week 1. Workshop 1 is top-down: start with the CSDM model diagram, then ask the customer to list everything IT delivers to the business (not the tools — the outcomes). Workshop 2 maps those outcomes to OOTB CSDM classifications and identifies the service owner for each. A miro/whiteboard is more effective than spreadsheet-first for workshop 1."),
        ("Common drift patterns to watch for", "Customers frequently try to model every application as a Business Service (too granular) or define Business Services so broadly they have no operational meaning ('All of IT'). Push for the middle ground: a Business Service should map to a distinct SLA, a distinct service owner, and at least one identifiable user population. If you can't name those three things, the service definition isn't ready."),
        ("CSDM readiness check before Sprint 2", "By end of Sprint 1, the following must be locked: (1) Business Service list approved by IT Director, (2) service owner for each, (3) top-level Technical Service groupings (e.g., Infrastructure, End User Computing, Applications), (4) the Application Service list derived from the existing application inventory. If any of these are missing, Sprint 2 CMDB normalization will lack an anchor and the Discovery team will load CIs with no service relationship."),
        ("Handling resistance to OOTB naming", "Customers often want to preserve legacy tool names as Business Service names. The counter-argument: 'The CSDM model names services by what the business receives, not the product that delivers it. When we move platforms in the future, the service name stays stable even when the underlying technology changes. Your users search for email, not Exchange.' This usually resolves the objection."),
    ],
    adoption_rows=[
        ("We have a different service model from our legacy ITSM tool — can we mirror it?",
         "Implement OOTB CSDM service classifications. Migrate the legacy hierarchy into the new taxonomy during Sprint 1 workshops.",
         "OOTB CSDM is the data contract for PI, Virtual Agent, Service Health, and CMDB health. A custom taxonomy breaks all of these and requires upgrade maintenance.",
         "'Your legacy model was designed for your previous tool, not for AI-powered service management. CSDM lets Virtual Agent understand which service is affected when a user reports a problem — that only works with the standard model. Let's map your existing services into CSDM; the names can stay the same even when the structure is standardized.'",
         "Only if the customer has a mature service portfolio management practice and an enterprise architect who will own the taxonomy for 3+ years. Extremely rare at mid-market."),
        ("We want every application to be a separate Business Service for reporting",
         "Application-level reporting belongs on Application Service CIs, not Business Services. Business Services roll up to executive dashboards; application detail stays at the Technical/Application tier.",
         "Forty Business Services means forty SLA definitions, forty service owners, and forty health dashboards. No customer team can maintain that. OOTB reporting surfaces application data from the lower CSDM tiers without elevating everything to Business Service.",
         "'Business Services are the C-suite view — what IT delivers to the business. Applications are the operational view — what IT teams manage. We can report on both independently without mixing the layers. Let me show you how the OOTB service health dashboard rolls application health up to business service health.'",
         "If the customer has a formal service catalogue managed at application level with SLAs per application, a hybrid model can be considered — but discuss with Practice Lead first."),
        ("We don't want to define service owners — IT is collectively responsible",
         "Assign a single named owner to each Business Service. This is a ServiceNow platform requirement for SLA escalation, Major Incident routing, and service health alerting.",
         "Collective ownership means nobody responds. The OOTB Service Health and Major Incident Management modules both require a single accountable owner for escalation. Without it, P1 alerts go unanswered.",
         "'Service ownership doesn't mean one person does all the work — it means one person is accountable for the service being healthy. We're not changing how your team is organized; we're giving the platform a single escalation point so that when a major incident hits, there's no confusion about who to call.'",
         "Never. This is a ServiceNow platform requirement, not an ECS preference."),
    ],
    snmap_sections=[
        ("Primary CMDB Tables", [
            ("Business Service", "cmdb_ci_service", "The top-level service classification in CSDM. Represents what IT delivers to the business."),
            ("Technical Service", "cmdb_ci_service_technical", "Mid-tier service — groups the technical components that support a Business Service."),
            ("Application Service", "cmdb_ci_appl", "Represents a deployable application or software service, mapped to Technical Service."),
            ("External Service", "cmdb_ci_service_auto", "Vendor-managed / SaaS services. Not populated by Discovery."),
        ]),
        ("Key Fields to Configure", [
            ("service_classification", "Business Service / Technical Service / Application Service / External Service", "Set on every Service CI to enable CSDM layer filtering."),
            ("owned_by", "Named individual (sys_user)", "Single service owner. Required for health dashboard and escalation."),
            ("support_group", "Assignment group", "Operational support group, distinct from the business owner."),
            ("operational_status", "1 = Operational (default for MVP)", "Set all live services to Operational before Sprint 2 discovery begins."),
        ]),
        ("OOTB Features Leveraged", [
            ("Service Map", "Now Platform > CMDB > Service Mapping", "Visualises service-to-CI relationships. Requires Service Mapping licence or Discovery."),
            ("CMDB Health Dashboard", "CMDB > CMDB Health", "Monitors completeness and staleness. Configure after CI classes are selected (Workbook 02)."),
            ("Dependency Views", "CMDB > CI Relationships", "OOTB graph view of service dependencies. No customisation needed."),
        ]),
    ],
)

# =============================================================================
# WORKBOOK 2 — CI Class Selection
# =============================================================================
wb2 = TabContent(
    workbook_title="02 — CI Class Selection",
    pack_name=PACK_NAME,
    purpose="Defines which OOTB CMDB CI classes the customer will activate at MVP, what data quality standards apply to each class, and which classes are explicitly out of scope. Keeping CI class scope narrow at MVP is the single most important CMDB governance decision — it determines whether the CMDB becomes a trusted asset or a noise source.",
    who_fills="Customer-side: IT Operations Manager and the team responsible for the infrastructure environment (server, endpoint, network). ECS SA facilitates the scoping discussion and recommends the MVP class list based on Discovery data availability.",
    sprint_window="Sprint 1 Week 2 — Sprint 2 Week 1",
    estimated_effort="3–4 hours (one scoping workshop + customer review of recommended class list)",
    related_workbooks=["01 CSDM Service Taxonomy", "05 Service-CI Relationships", "06 CMDB Governance Baseline", "Foundation Data Pack"],
    success_criteria=[
        "MVP CI class list is agreed and documented — typically 5–8 classes for a mid-market engagement.",
        "Each in-scope CI class has a named data steward responsible for quality.",
        "Out-of-scope CI classes are explicitly listed and the rationale recorded.",
        "Minimum mandatory attributes for each in-scope CI class are defined.",
        "Discovery source for each CI class (SCCM, Intune, Agent, manual) is confirmed.",
    ],
    process_decisions=[
        ("Which CI classes are in scope at MVP?",
         "Recommended MVP class set: cmdb_ci_computer (workstations/laptops), cmdb_ci_server (on-prem servers), cmdb_ci_appl (installed applications), cmdb_ci_service / cmdb_ci_service_technical (CSDM services from Workbook 01), cmdb_ci_network_adapter (populated by Discovery automatically). Add only if Discovery data confirms reliable population.",
         "Every CI class you activate is a data quality commitment. A CMDB with 6 clean classes is more valuable than one with 30 partially-populated classes. Start with what Discovery can reliably populate and expand sprint-by-sprint."),
        ("Should we include network devices (switches, routers, firewalls) at MVP?",
         "Exclude from MVP unless a Network Discovery licence and SNMP credentials are ready. Network devices can be added in Phase 2 without restructuring the MVP CMDB.",
         "Network devices require SNMP community strings, device credentials, and a pattern library. Without these, Discovery creates stub records with no meaningful attributes — which is worse than no record."),
        ("Should we track virtual machines separately from physical servers?",
         "Yes. Use cmdb_ci_vm_instance for VMs and cmdb_ci_server for physical. Both classes are OOTB and Discovery populates them correctly when VMware/Hyper-V credentials are available.",
         "Mixing VMs and physical servers in a single class breaks capacity reporting and service impact analysis. The OOTB separation is the right model."),
        ("Should we include cloud resources (AWS EC2, Azure VMs) at MVP?",
         "Include only if the Cloud Provisioning and Governance plugin is licensed. Use cmdb_ci_vm_instance with the cloud_service_account relationship. If not licensed, defer to Phase 2.",
         "Manually maintained cloud CIs become stale within weeks. The OOTB Cloud Management integration is the only reliable source for cloud CI data. Without the licence, do not attempt cloud CIs at MVP."),
        ("How do we handle legacy CI records from the previous ITSM tool?",
         "Do not migrate legacy CI records. Run Discovery first; then reconcile what Discovery found against the legacy export. Retire any CI not confirmed by Discovery within 90 days.",
         "Legacy CI data is typically 30–60% stale. Migrating it pollutes the CMDB before Discovery has a chance to establish a clean baseline. Discovery-first is the only way to start with trusted data."),
        ("What is the minimum set of attributes required on every CI record?",
         "Mandatory for all CI classes: Name, Class, Operational Status, Managed By (assignment group), and the relationship to at least one CSDM service (from Workbook 05). Class-specific mandatories: see Configuration Data tab.",
         "CI records with no service relationship are invisible to service impact analysis. Records with no managed-by group are orphaned. These two attributes are the minimum for a CMDB that actually works in incident management."),
    ],
    dependencies=[
        ("CSDM Service Taxonomy (Workbook 01) completed", "Required", "ECS SA + Customer EA", "Sprint 1 Wk 2", "CI classes must be mappable to CSDM services. Without the service taxonomy, relationships cannot be defined."),
        ("Discovery scope confirmed — IP ranges, credentials, MID Server location", "Required", "Customer IT Ops + ECS Architect", "Sprint 1 Wk 2", "CI class selection drives Discovery pattern requirements. Unconfirmed scope means some classes cannot be reliably populated."),
        ("SCCM/Intune Service Graph Connector credentials and instance access", "Required", "Customer IT Ops", "Sprint 2 Wk 1", "SGC is the primary source for cmdb_ci_computer and installed applications (cmdb_ci_appl)."),
        ("VMware vCenter credentials (if virtualised environment)", "Recommended", "Customer Infrastructure Lead", "Sprint 2 Wk 1", "Required to populate cmdb_ci_vm_instance and host relationships."),
        ("Legacy CMDB or asset register export (for reconciliation reference)", "Recommended", "Customer IT Ops", "Sprint 1 Wk 2", "Used to cross-check Discovery results, not to migrate into ServiceNow."),
    ],
    config_sections=[
        ("MVP CI Class List", [
            ("cmdb_ci_computer", "In scope", "Workstations, laptops. Primary source: SCCM/Intune SGC.", False),
            ("cmdb_ci_server", "In scope", "On-prem physical servers. Primary source: Discovery (agent or agentless).", False),
            ("cmdb_ci_vm_instance", "In scope if VMware/Hyper-V credentials available", "Virtual machines. Primary source: Discovery VMware extension.", True),
            ("cmdb_ci_appl", "In scope (limited to managed applications)", "Installed software. Populated by SCCM SGC. Scope to managed apps only — not every detected binary.", False),
            ("cmdb_ci_network_adapter", "In scope (auto-populated by Discovery)", "Network interfaces. Discovery creates these automatically as part of computer/server discovery.", False),
            ("cmdb_ci_network_gear", "Out of scope at MVP", "Network devices. Defer until SNMP credentials and Network Discovery are confirmed.", False),
            ("cmdb_ci_cloud_*", "Out of scope at MVP unless Cloud Provisioning licensed", "Cloud resources. Defer unless the licence is confirmed.", True),
            ("cmdb_ci_database", "Out of scope at MVP", "Database instances. Add in Phase 2 with Application Discovery patterns.", False),
        ]),
        ("Mandatory CI Attributes (all classes)", [
            ("name", "Required — populated by Discovery", "Must be unique within class.", False),
            ("sys_class_name", "Required — set by Discovery automatically", "Must match OOTB class hierarchy.", False),
            ("operational_status", "Required — default to 1 (Operational)", "Stale/retired CIs must be set to Retired within 90 days of confirmation.", False),
            ("assignment_group", "Required — data steward group", "Every CI must have a managed-by group. Use assignment groups from Foundation Data Pack.", True),
            ("Service relationship (cmdb_rel_ci)", "Required — at least one CSDM service", "Link to a Business Service, Technical Service, or Application Service from Workbook 01.", True),
        ]),
        ("Mandatory Attributes — cmdb_ci_computer", [
            ("serial_number", "Required — from SCCM/Intune", "Must match physical label or BIOS serial.", False),
            ("os", "Required — from Discovery", "Operating System name and version.", False),
            ("last_discovered", "Required — auto-populated", "Must be within 30 days to be considered current.", False),
            ("u_asset_tag or asset_tag", "Required — from Foundation Data Pack", "Link to HAM asset record if HAM is in scope.", True),
        ]),
        ("Mandatory Attributes — cmdb_ci_server", [
            ("serial_number", "Required", "From Discovery or manual entry for physical servers.", False),
            ("os", "Required — from Discovery", "", False),
            ("ip_address / ip_addresses", "Required — from Discovery", "Primary IP; multiple IPs via related list.", False),
            ("location", "Required", "Must match a Location record from Foundation Data Pack.", True),
        ]),
    ],
    raci_rows=[
        ("Facilitate CI class scoping workshop", "R/A", "C", "ECS SA runs the workshop; customer confirms environment details."),
        ("Confirm Discovery scope (IP ranges, credentials)", "C", "R/A", "Customer IT Ops owns network access; ECS advises on Discovery configuration."),
        ("Define mandatory attributes per CI class", "R/A", "C", "ECS SA defines the OOTB-aligned mandatory set; customer confirms."),
        ("Assign CI data stewards per class", "I", "R/A", "Customer IT Ops assigns stewards by class."),
        ("Configure Discovery patterns for in-scope classes", "R/A", "I", "ECS Architect configures Discovery; IT Ops provides credentials."),
        ("Configure SCCM/Intune Service Graph Connectors", "R/A", "C", "ECS Architect configures; customer provides connector credentials."),
        ("Validate first Discovery run results vs. in-scope class list", "R", "C", "ECS validates class coverage; customer confirms asset counts are plausible."),
        ("Document out-of-scope class rationale", "R/A", "I", "ECS SA documents rationale for the project record."),
    ],
    consultant_guide_sections=[
        ("The scoping conversation", "The CI class scoping workshop is the highest-leverage CMDB conversation in the engagement. The goal is to get the customer to commit to a narrow, clean scope rather than a broad, aspirational one. Open with: 'Every CI class you include is a data quality commitment. I'd rather have you start with 5 classes that are 95% accurate than 20 classes that are 60% accurate. We can add classes in Phase 2. What can we not go live without?' This reframe usually cuts the initial class list by half."),
        ("Discovery credential dependency", "The single biggest CMDB sprint risk is credential delays. In Sprint 1 Week 2, confirm: (1) MID Server is deployed and reaching the target subnets, (2) admin credentials for Windows/Linux discovery are in the credential store, (3) SCCM/Intune API credentials for the SGC are available. If any of these are missing at the start of Sprint 2, escalate immediately — this is a project risk, not a configuration problem."),
        ("Handling the 'we need everything' response", "Customers frequently ask to track everything from printers to coffee machines in the CMDB. The counter-argument is not 'the platform can't do it' — it can. The counter-argument is: 'Every CI class requires a data steward who keeps it accurate. Who is the steward for printers, and how will they know when a printer is retired?' This question usually resolves the scope inflation."),
        ("Legacy data migration anti-pattern", "Do not agree to migrate legacy CI data even if the customer insists it will 'save time'. Legacy CMDB data is almost always inaccurate and creates false positives in Discovery reconciliation. The correct sequence is: Discovery runs and creates authoritative records; then the customer compares to the legacy export and confirms what Discovery missed. Anything Discovery can't find within 90 days is out of scope."),
    ],
    adoption_rows=[
        ("We have 200 CI classes in our legacy CMDB and need them all",
         "Activate only the OOTB MVP class set. Legacy class specialisations belong in CI attributes, not separate classes.",
         "Custom CI classes require upgrade maintenance and break Discovery reconciliation rules. OOTB CI classes cover the meaningful distinctions. Use attributes for sub-types.",
         "'Your legacy system may have needed separate classes to compensate for limited attribute support. ServiceNow handles sub-types through attributes and CI relationships — you get the same reporting without the maintenance overhead of custom class tables.'",
         "Only if the customer has a unique CI type with no OOTB class equivalent AND a named data steward. Escalate to Practice Lead before agreeing."),
        ("We want to migrate our existing 50,000 CI records on day one",
         "Run Discovery first. Use the legacy export for reconciliation reference only. Do not load stale data.",
         "Discovery-first ensures the CMDB starts with verified, current data. Loading 50,000 stale records creates noise that undermines trust in the CMDB from day one.",
         "'Imagine going live with a CMDB where every record is accurate because Discovery verified it. That's more valuable than a CMDB with 50,000 records where 30% are out of date. We'll run Discovery first, then use your legacy export to catch anything Discovery missed — you get the best of both.'",
         "Never for bulk migration. Manual entry of a small set of strategic CIs (critical servers not reachable by Discovery) is acceptable."),
        ("We want to track every software installation, not just managed applications",
         "Scope cmdb_ci_appl to managed applications (those with a maintenance or licence obligation). All detections are available via the Software Asset Management module without polluting the CMDB.",
         "Tracking every detected binary in the CMDB creates millions of CI records that nobody maintains. SAM has its own normalised software library for this purpose.",
         "'Discovery will find every installed binary — that data lives in the SAM software normalisation layer where it belongs. The CMDB Application CI should represent managed applications your team is responsible for, not every utility that's ever been installed on a laptop.'",
         "Only if the customer has a specific compliance requirement to audit every binary installation. Rare and should be managed in SAM, not CMDB."),
    ],
    snmap_sections=[
        ("Core CI Tables", [
            ("cmdb_ci_computer", "Computer CI", "Workstations, laptops — populated via SCCM/Intune SGC."),
            ("cmdb_ci_server", "Server CI", "Physical on-prem servers — populated via Discovery."),
            ("cmdb_ci_vm_instance", "Virtual Machine Instance", "VMs — populated via Discovery with vCenter credentials."),
            ("cmdb_ci_appl", "Application", "Managed software installations — populated via SCCM SGC."),
            ("cmdb_ci_network_adapter", "Network Adapter", "Auto-populated by Discovery as part of computer/server patterns."),
        ]),
        ("Key OOTB Identification Rules", [
            ("IRE — Computer", "Serial number + OS + CPU", "OOTB identification rule. Do not modify without Discovery Architect review."),
            ("IRE — Server", "Serial number + name", "Fallback to IP if serial unavailable (physical only)."),
            ("IRE — VM", "VM UUID (from hypervisor)", "VM UUID is the authoritative identifier. Never use hostname alone."),
        ]),
        ("Discovery Sources", [
            ("Service Graph Connector — SCCM", "IntegrationHub > SCCM SGC", "Populates computer CIs and installed application CIs."),
            ("Service Graph Connector — Intune", "IntegrationHub > Intune SGC", "Populates modern-managed endpoint CIs. Complements SCCM SGC."),
            ("Discovery (agentless)", "Discovery > Discovery Schedules", "Populates server CIs, VM instances, network adapters."),
        ]),
    ],
)

# =============================================================================
# WORKBOOK 3 — Business Service Definitions
# =============================================================================
wb3 = TabContent(
    workbook_title="03 — Business Service Definitions",
    pack_name=PACK_NAME,
    purpose="Captures the full definition of each Business Service the customer will register in ServiceNow, including service name, owner, support group, SLA targets, user population, and the upstream Technical Services that support it. This is the customer-completed record set that ECS uses to load Business Service CIs in Sprint 1.",
    who_fills="Customer-side: IT Service Management Owner or Service Portfolio Manager, with sign-off from IT Director or CIO. One row per Business Service. ECS provides the template; customer populates. ECS SA reviews for CSDM compliance before loading.",
    sprint_window="Sprint 1 Weeks 1–2 (draft), confirmed by end of Sprint 1",
    estimated_effort="2–4 hours for a typical 10–20 Business Service portfolio",
    related_workbooks=["01 CSDM Service Taxonomy", "04 Technical Services & Apps", "05 Service-CI Relationships", "Foundation Data Pack — Groups"],
    success_criteria=[
        "Every Business Service has a name, owner (named individual), support group, and operational status.",
        "SLA targets (availability % and response time) are defined or confirmed as TBD for Phase 2.",
        "Each Business Service is linked to at least one Technical Service (can be draft).",
        "The IT Director or CIO has reviewed and signed off the list.",
        "No duplicate Business Service names exist in the list.",
    ],
    process_decisions=[
        ("How do we handle services that are partially outsourced?",
         "Define the Business Service from the user's perspective (what IT delivers) regardless of who delivers it. The support group can be an external vendor group. Mark the service as 'External Provider' in the service classification.",
         "The user experiences a Business Service outage whether IT or a vendor caused it. The service record must exist to track incidents and SLAs end-to-end."),
        ("Should Business Services have SLAs defined at this stage or deferred?",
         "Capture SLA targets now even if aspirational — 99.9% availability, 4-hour response for P2. SLAs can be refined in Sprint 3 when the SLA module is configured. Having a placeholder prevents the field from being skipped entirely.",
         "SLA fields left blank at Sprint 1 are rarely filled in later. A placeholder forces the service owner conversation about what 'good' looks like before configuration begins."),
        ("What if we don't know the user population size?",
         "Estimate in tiers: <100 users, 100-500 users, 500-2000 users, >2000 users. Exact counts are not required at this stage.",
         "User population drives incident priority matrix, capacity planning, and service health alerting. Even a rough tier is better than no data."),
        ("How should we handle services that are being decommissioned in the next 12 months?",
         "Create the Business Service record with operational_status = 'Retiring'. This ensures incidents during the retirement period are tracked correctly and the service is excluded from new SLA commitments.",
         "Omitting retiring services means incidents against them are uncategorised. OOTB operational_status = Retiring handles this cleanly without requiring a custom field."),
    ],
    dependencies=[
        ("CSDM Service Taxonomy (Workbook 01) approved", "Required", "Customer IT Director", "Sprint 1 Wk 1", "Business Service names must align with the agreed taxonomy."),
        ("Foundation Data Pack — Groups (assignment groups) loaded", "Required", "ECS SA", "Sprint 0", "Support groups must exist in ServiceNow before Business Service CIs are created."),
        ("Foundation Data Pack — Users (for service owners) loaded", "Required", "ECS SA", "Sprint 0", "Service owners must be active user records in ServiceNow."),
        ("SLA targets reviewed by IT Director", "Recommended", "Customer IT Director", "Sprint 1 Wk 2", "Even draft SLA targets require business stakeholder input."),
    ],
    config_sections=[
        ("Business Service Template Fields", [
            ("Service Name", "[Customer to complete]", "Follow naming convention from Workbook 01.", True),
            ("Service Description", "[Customer to complete — 1-2 sentences]", "What does this service deliver to the business? Not how.", True),
            ("Service Owner (named individual)", "[Customer to complete]", "Must be an active user in ServiceNow.", True),
            ("Support Group", "[Customer to complete]", "Must be an existing assignment group.", True),
            ("Operational Status", "1 — Operational (default) / 5 — Retiring", "Set Retiring for services being decommissioned.", True),
            ("SLA — Availability Target (%)", "[Customer to complete or TBD]", "e.g., 99.9%. Leave TBD if not yet agreed.", True),
            ("SLA — P2 Response Time", "[Customer to complete or TBD]", "e.g., 4 hours. Used in Sprint 3 SLA configuration.", True),
            ("User Population Tier", "[<100 / 100-500 / 500-2000 / >2000]", "Rough estimate is acceptable.", True),
            ("Service Classification", "Business Service (OOTB)", "Do not change. Set by ECS during CI load.", False),
            ("Primary Technical Service(s) supporting this", "[Customer to complete — link to Workbook 04 rows]", "Can be draft — confirm in Sprint 2.", True),
        ]),
    ],
    raci_rows=[
        ("Provide Business Service template and instructions", "R/A", "I", "ECS SA distributes this workbook."),
        ("Complete Business Service definitions (one row per service)", "I", "R/A", "Customer ITSM Owner fills; IT Director approves."),
        ("Review definitions for CSDM compliance", "R/A", "C", "ECS SA validates names, classifications, and relationships."),
        ("Load Business Service CIs into ServiceNow", "R/A", "I", "ECS SA performs the CI load after customer sign-off."),
        ("Validate loaded CIs in ServiceNow", "R", "A", "ECS validates technically; customer confirms data is correct."),
        ("Obtain IT Director sign-off on final Business Service list", "I", "R/A", "Customer-side governance step."),
    ],
    consultant_guide_sections=[
        ("The service definition interview", "If the customer is struggling to complete Workbook 03 independently, run a 60-minute service definition interview. Ask for each service: (1) Who calls the helpdesk when this is down? (2) What does 'down' mean for this service? (3) Who do you call at 2am if it's down? (4) How long can the business tolerate it being down? These four questions populate service owner, definition, support group, and SLA target respectively."),
        ("Service owner resistance", "The most common blocker is naming a service owner. IT directors sometimes resist because they don't want to make managers 'accountable' for service health. Frame it as: 'We need someone who gets the first call from the business when this service is impacted. That's the owner — not someone who fixes it, just someone who orchestrates the response.' This usually resolves the resistance."),
        ("Validation before CI load", "Before loading Business Service CIs, validate: (1) no duplicate names, (2) all support groups exist in ServiceNow, (3) all service owners are active users, (4) operational_status is explicitly set (not blank). A missing operational_status defaults to null, which breaks the CMDB Health dashboard filter for active services."),
    ],
    adoption_rows=[
        ("Our service definitions from the old ITSM tool are fine — can we just import them?",
         "Review the legacy definitions against CSDM compliance criteria, then load only compliant records as new Business Service CIs.",
         "Legacy service definitions are often formatted as categories or queues, not CSDM Business Services. Importing them without review creates misclassified CIs that break service health and PI.",
         "'We'll start from your legacy list as a reference — it's much faster than starting from scratch. The review step just ensures each record is structured the way ServiceNow expects so that service health, Virtual Agent, and reporting all work correctly from day one.'",
         "If the legacy system is ServiceNow and the definitions are already CSDM-compliant, a direct import is acceptable after validation."),
    ],
    snmap_sections=[
        ("Target Table", [
            ("Business Service CI", "cmdb_ci_service", "One record per Business Service. Loaded via import set or direct creation."),
            ("Service Relationship", "cmdb_rel_ci", "Links Business Service to Technical Service CIs."),
            ("SLA Definition (reference)", "contract_sla", "SLA records configured in Sprint 3; reference the service name from this workbook."),
        ]),
        ("Key Fields", [
            ("name", "Service name from this workbook", ""),
            ("service_classification", "Business Service", "Set by ECS during load."),
            ("owned_by", "Service owner sys_user record", ""),
            ("support_group", "Assignment group sys_id", ""),
            ("operational_status", "1 = Operational, 5 = Retiring", ""),
            ("u_sla_availability_target", "Custom field or notes field", "If not using formal SLA module in Sprint 1, capture in notes."),
        ]),
    ],
)

# =============================================================================
# WORKBOOK 4 — Technical Services & Applications
# =============================================================================
wb4 = TabContent(
    workbook_title="04 — Technical Services & Applications",
    pack_name=PACK_NAME,
    purpose="Defines the Technical Service and Application Service CIs that underpin each Business Service. Technical Services group the infrastructure and software components that together deliver a Business Service. This workbook drives the CMDB relationship layer that enables service impact analysis, Major Incident routing, and CMDB health scoring.",
    who_fills="Customer-side: Infrastructure Lead and Application Owners, facilitated by ECS SA. One row per Technical Service or Application Service. Can be completed iteratively as Discovery data becomes available in Sprint 2.",
    sprint_window="Sprint 1 Week 2 (draft structure) — Sprint 2 Week 2 (confirmed after first Discovery run)",
    estimated_effort="3–5 hours. Draft in Sprint 1; refine after Discovery in Sprint 2.",
    related_workbooks=["01 CSDM Service Taxonomy", "03 Business Service Definitions", "05 Service-CI Relationships", "02 CI Class Selection"],
    success_criteria=[
        "Every Business Service from Workbook 03 has at least one Technical Service mapped to it.",
        "Key managed applications (from cmdb_ci_appl scope in Workbook 02) are represented as Application Service CIs.",
        "Technical Service CIs are loaded in ServiceNow before Sprint 2 Discovery runs.",
        "Discovery-identified CIs can be related to Technical Services within Sprint 2.",
    ],
    process_decisions=[
        ("How granular should Technical Services be?",
         "Group by infrastructure domain: one Technical Service per logical infrastructure grouping (e.g., 'Windows Server Infrastructure', 'Network Core', 'Microsoft 365 Platform'). Avoid one Technical Service per physical server.",
         "A Technical Service per physical server creates maintenance overhead that destroys CMDB health scores. The correct level of granularity is: 'What group of CIs would I notify if this Technical Service were degraded?'"),
        ("Should application servers and their applications be separate Technical Services?",
         "Yes. Create one Technical Service for the server infrastructure tier and a separate Application Service CI for each managed application. Relate the Application Service to both the server Technical Service and the Business Service it supports.",
         "The CSDM model separates infrastructure from application for a reason: different teams manage them, they have different maintenance windows, and they fail independently. Mixing them breaks service impact analysis."),
        ("How do we handle shared infrastructure (e.g., a server that supports multiple Business Services)?",
         "The shared server CI is related to a Technical Service. That Technical Service is then related to multiple Business Services. The server CI is related to the Technical Service once — not duplicated per Business Service.",
         "OOTB relationship modelling handles fan-out naturally. Duplicating CIs to represent shared infrastructure creates orphaned duplicates after Discovery reconciliation."),
        ("Do we need Technical Service CIs before Discovery runs?",
         "Yes. Create the Technical Service CIs manually in Sprint 1 so that Discovery-found CIs can be related to them in Sprint 2. An empty service hierarchy means Discovery-found CIs have no service context.",
         "CIs without service relationships are invisible to service impact analysis. Creating the Technical Service shells early means Sprint 2 Discovery produces immediately useful data."),
    ],
    dependencies=[
        ("Business Service Definitions (Workbook 03) approved", "Required", "Customer IT Director", "Sprint 1 Wk 2", "Technical Services must link upward to approved Business Services."),
        ("CI Class Selection (Workbook 02) confirmed", "Required", "ECS SA + Customer IT Ops", "Sprint 1 Wk 2", "Technical Service scope is bounded by the agreed CI classes."),
        ("First Discovery run results", "Recommended", "ECS Architect", "Sprint 2 Wk 1", "Discovery results allow Technical Services to be validated against actual CI population."),
        ("Application inventory (spreadsheet or legacy CMDB export)", "Recommended", "Customer App Owners", "Sprint 1 Wk 2", "Needed to identify Application Service CIs before Discovery finds them."),
    ],
    config_sections=[
        ("Technical Service Template Fields", [
            ("Technical Service Name", "[Customer to complete]", "Format: [Domain] + 'Infrastructure' e.g., 'Windows Server Infrastructure'.", True),
            ("Description", "[Customer to complete]", "What infrastructure components does this service group?", True),
            ("Support Group", "[Customer to complete]", "The team responsible for this infrastructure domain.", True),
            ("Parent Business Service(s)", "[Customer to complete — link to Workbook 03 rows]", "One or more Business Services this Technical Service supports.", True),
            ("Operational Status", "1 — Operational", "", False),
        ]),
        ("Application Service Template Fields", [
            ("Application Name", "[Customer to complete]", "The managed application name. Use the business name, not the executable name.", True),
            ("Application Version (if fixed)", "[Customer to complete or 'multi-version']", "", True),
            ("Application Owner / Team", "[Customer to complete]", "The team responsible for the application.", True),
            ("Parent Technical Service", "[Customer to complete — link above]", "The infrastructure domain this application runs on.", True),
            ("Parent Business Service", "[Customer to complete — link to Workbook 03]", "The Business Service this application supports.", True),
        ]),
    ],
    raci_rows=[
        ("Draft Technical Service list (infrastructure domains)", "R/A", "C", "ECS SA drafts based on CSDM taxonomy; customer confirms infrastructure groupings."),
        ("Identify managed Application Services", "C", "R/A", "Customer Application Owners list managed apps; ECS validates against CSDM model."),
        ("Load Technical Service CIs into ServiceNow", "R/A", "I", "ECS SA loads before Sprint 2 Discovery begins."),
        ("Load Application Service CIs into ServiceNow", "R/A", "C", "ECS SA loads after customer confirms list."),
        ("Relate Technical Services to Business Services", "R/A", "C", "ECS SA configures relationships; customer validates in dependency view."),
        ("Validate Technical Service coverage after Discovery", "R", "C", "ECS SA validates that Discovery-found CIs map to Technical Services."),
    ],
    consultant_guide_sections=[
        ("Creating Technical Service shells before Discovery", "The most important sequencing decision is loading Technical Service CI shells before Discovery runs. Without them, Discovery-found CIs have no service context and the CMDB health score starts low. Create 5–10 Technical Service CIs manually in Sprint 1 Week 2. These are just shell records with a name, description, and support group — Discovery fills in the CI relationships later."),
        ("Application Service scoping", "Not every installed application should be an Application Service CI. Scope Application Services to applications that: (a) have a named owner, (b) have or should have an SLA, or (c) appear in incidents frequently enough to benefit from service impact analysis. Rule of thumb: if nobody would notice it was missing from the CMDB, it shouldn't be an Application Service CI."),
        ("The relationship between Application Services and SAM", "Application Service CIs in the CMDB represent managed applications at the service level. SAM's software normalisation covers installed binaries at the asset level. These are complementary, not overlapping. An Application Service CI for 'Microsoft SQL Server' represents the managed database service; SAM tracks every SQL Server installation across the fleet. Don't conflate them."),
    ],
    adoption_rows=[
        ("We want a separate Technical Service for every physical server",
         "Group servers into Technical Services by infrastructure domain. One Technical Service per server defeats the purpose of service-level modelling.",
         "Service impact analysis requires service-level groupings, not CI-level CIs at the top of the hierarchy. Grouping by domain means one incident can correctly flag the Technical Service as degraded without requiring manual correlation across 200 individual server CIs.",
         "'If we create one Technical Service per server, you'd have hundreds of services to maintain and monitor. What you actually want to know is: is my Windows server infrastructure healthy? That's one Technical Service that covers all your Windows servers — and when one fails, the service health rolls up automatically.'",
         "Only for strategically critical single servers (e.g., a legacy mainframe with no peers). Discuss with Practice Lead."),
    ],
    snmap_sections=[
        ("Target Tables", [
            ("Technical Service CI", "cmdb_ci_service_technical", "One record per infrastructure domain group."),
            ("Application Service CI", "cmdb_ci_appl", "One record per managed application."),
            ("Service Relationship", "cmdb_rel_ci", "Links: Application Service → Technical Service → Business Service."),
        ]),
        ("Relationship Types", [
            ("Depends on", "cmdb_rel_type: Depends on::Used by", "Application Service depends on Technical Service."),
            ("Hosted on", "cmdb_rel_type: Hosted on::Hosts", "Application Service hosted on server CI."),
            ("Runs on", "cmdb_rel_type: Runs on::Runs", "Server CI runs on VM Instance CI."),
        ]),
    ],
)

# =============================================================================
# WORKBOOK 5 — Service-CI Relationships
# =============================================================================
wb5 = TabContent(
    workbook_title="05 — Service-CI Relationships",
    pack_name=PACK_NAME,
    purpose="Defines the relationship mappings between Discovery-found CI records and the CSDM service hierarchy. This workbook drives the service impact analysis capability: when a CI is marked as impacted in an incident, ServiceNow automatically identifies which services are affected. Completing this workbook is what transforms a list of CIs into a functioning service map.",
    who_fills="ECS SA leads the mapping exercise using Discovery results. Customer Infrastructure Lead and Application Owners validate. Complete in Sprint 2 after first Discovery run.",
    sprint_window="Sprint 2 Weeks 1–2",
    estimated_effort="4–6 hours (initial mapping from Discovery results); ongoing as Discovery finds new CIs",
    related_workbooks=["02 CI Class Selection", "04 Technical Services & Apps", "03 Business Service Definitions"],
    success_criteria=[
        "Every CI in the in-scope classes (Workbook 02) is related to at least one CSDM service.",
        "The CMDB relationship graph shows a complete chain from Business Service to CI for each Business Service.",
        "Service Map view in ServiceNow is navigable without broken relationships.",
        "CMDB Health — Relationship completeness score is above 80% for in-scope CI classes.",
    ],
    process_decisions=[
        ("Should every CI be related to a service or only critical CIs?",
         "Every CI in the agreed in-scope class list must have at least one service relationship. CIs with no service relationship do not contribute to service impact analysis and reduce the CMDB health score.",
         "The OOTB CMDB health dashboard flags 'orphaned CIs' (no service relationship) as a health problem. Orphaned CIs are also invisible to Virtual Agent and Predictive Intelligence service context. A CI without a service relationship is a CI with no value."),
        ("Can a CI be related to multiple services?",
         "Yes. A shared infrastructure CI (e.g., a core network switch) should be related to all services that depend on it. Use the 'Depends on' relationship type. There is no limit on the number of service relationships per CI.",
         "Shared infrastructure by definition supports multiple services. Artificially limiting relationships to one service creates incorrect service impact analysis during outages."),
        ("How should we handle CIs discovered but not in the agreed class scope?",
         "Do not create service relationships for out-of-scope CI classes. Mark these CIs as 'Out of scope — pending Phase 2' in the notes field and set operational_status to 'Non-operational' if they should not appear in service impact analysis.",
         "Creating service relationships for out-of-scope CIs expands the maintenance commitment beyond what was agreed. Keep the scope boundary clean."),
        ("What is the process for newly discovered CIs after Sprint 2?",
         "Establish a monthly CI relationship review. New CIs found by Discovery are automatically created; ECS configures an IRE reconciliation rule that assigns new CIs to the correct Technical Service based on subnet/naming pattern. Customer IT Ops reviews and confirms monthly.",
         "Discovery runs continuously after Sprint 2. Without a process for relating new CIs to services, the CMDB degrades over time regardless of how well it started."),
    ],
    dependencies=[
        ("First Discovery run completed and CI records created", "Required", "ECS Architect", "Sprint 2 Wk 1", "Cannot map relationships until CIs exist."),
        ("Technical Service and Application Service CIs loaded (Workbook 04)", "Required", "ECS SA", "Sprint 1 Wk 2", "Service shells must exist before relationships can be created."),
        ("Business Service CIs loaded (Workbook 03)", "Required", "ECS SA", "Sprint 1 Wk 2", "Required for the full relationship chain."),
        ("Network diagram or infrastructure topology document", "Recommended", "Customer Infrastructure Lead", "Sprint 2 Wk 1", "Helps identify which CIs support which Technical Services when Discovery data is ambiguous."),
    ],
    config_sections=[
        ("Relationship Mapping Matrix", [
            ("Business Service → Technical Service relationship type", "Used by::Depends on", "OOTB relationship type. Do not create custom types.", False),
            ("Technical Service → Server/VM CI relationship type", "Used by::Depends on", "", False),
            ("Application Service → Server CI relationship type", "Hosted on::Hosts", "Use 'Hosted on' for application-to-server relationships.", False),
            ("CI → CI relationship (peer)", "Connected to::Connected to", "Use for network/dependency peer relationships.", False),
        ]),
        ("IRE Auto-Relationship Rules (recommended)", [
            ("cmdb_ci_computer → 'End User Computing' Technical Service", "Subnet match or AD OU match", "Configure IRE rule to auto-relate endpoint CIs to the EUC Technical Service.", False),
            ("cmdb_ci_server → 'Windows Server Infrastructure' or 'Linux Infrastructure'", "OS attribute match", "Auto-relate servers to the appropriate infrastructure Technical Service by OS.", False),
            ("cmdb_ci_appl → Application Service CI", "Application name match", "Match installed application CIs to Application Service CIs by normalised name.", True),
        ]),
    ],
    raci_rows=[
        ("Map Discovery-found CIs to Technical Services", "R/A", "C", "ECS SA leads mapping; customer confirms infrastructure groupings."),
        ("Configure IRE auto-relationship rules", "R/A", "I", "ECS Architect configures IRE; this is a technical configuration step."),
        ("Validate service map completeness (relationship view)", "R", "A", "ECS validates technically; customer confirms service map is meaningful."),
        ("Review and confirm orphaned CI list", "R", "A", "ECS identifies orphans; customer decides classification."),
        ("Establish monthly CI relationship review process", "C", "R/A", "Customer IT Ops owns the ongoing review; ECS advises on tooling."),
        ("Document relationship standards for future CI types", "R/A", "I", "ECS SA documents the relationship standards for customer runbook."),
    ],
    consultant_guide_sections=[
        ("IRE auto-relationship rules", "The most efficient way to relate hundreds of CIs to services is through IRE (Identification and Reconciliation Engine) relationship rules. Configure rules that automatically relate CIs to services based on observable attributes (subnet, OS, application name). This means every new CI found by Discovery is automatically placed in the service hierarchy without manual intervention. Spend an extra hour in Sprint 2 getting IRE rules right — it saves 10+ hours of manual mapping and prevents CMDB drift."),
        ("Service Map walkthrough with the customer", "Before Sprint 2 ends, run a 30-minute Service Map walkthrough with the IT Operations Lead. Show them: (1) a Business Service and its downstream Technical Services, (2) click into a Technical Service and show the CI list, (3) simulate a CI outage and show the service impact pop-up. This walkthrough converts CMDB sceptics. The visual payoff of a complete service map is the most effective tool for sustaining customer engagement with CMDB data quality."),
        ("Orphaned CI triage", "After the first Discovery run, export the list of CIs with no service relationship (CMDB Health report — orphaned CIs). Work through this list with the customer in Sprint 2 Week 2: most orphaned CIs either belong to an existing Technical Service (easy fix) or are out-of-scope CIs that Discovery found but shouldn't be tracked (set operational_status = Non-operational). Aim for zero orphaned in-scope CIs before Sprint 2 closes."),
    ],
    adoption_rows=[
        ("We want to manually maintain all CI-to-service relationships",
         "Configure IRE auto-relationship rules for relationship maintenance. Manual-only maintenance degrades within 60 days as Discovery continuously finds and creates new CI records.",
         "IRE auto-relationship rules are OOTB functionality specifically designed for this purpose. Manual maintenance of CI relationships is not scalable and is the leading cause of CMDB health degradation.",
         "'Manual relationship maintenance works for the first sprint, but Discovery runs every day and creates new CIs constantly. IRE rules mean every new CI is automatically placed in the right service — you only need to review exceptions, not manage every individual record.'",
         "Only for very small, static environments (<100 CIs total). Still document the process so it can be automated later."),
    ],
    snmap_sections=[
        ("Relationship Table", [
            ("cmdb_rel_ci", "CI Relationship", "All CI-to-CI and CI-to-Service relationships. Primary relationship table."),
            ("cmdb_rel_type", "CI Relationship Type", "OOTB relationship types. 'Depends on::Used by' and 'Hosted on::Hosts' are most commonly used."),
        ]),
        ("IRE Configuration", [
            ("IRE Rule", "Identification Rules > Relationship Rules", "Configure in CMDB > Identification/Reconciliation > Relationship Rules."),
            ("Pattern match", "Attribute-based (subnet, OS, app name)", "Use existing CI attributes to drive automatic relationship assignment."),
        ]),
        ("OOTB Reporting", [
            ("Service Map", "CMDB > Dependency Views > Services", "Visual service map driven by cmdb_rel_ci."),
            ("CMDB Health — Relationship completeness", "CMDB > CMDB Health Dashboard", "Measures % of in-scope CIs with at least one service relationship."),
            ("Orphaned CI report", "CMDB > CMDB Health > Orphaned CIs", "CIs with no service relationship. Target: 0 for in-scope classes."),
        ]),
    ],
)

# =============================================================================
# WORKBOOK 6 — CMDB Governance Baseline
# =============================================================================
wb6 = TabContent(
    workbook_title="06 — CMDB Governance Baseline",
    pack_name=PACK_NAME,
    purpose="Establishes the governance framework for the CMDB: data steward assignments, staleness thresholds, CMDB health KPIs, the review cadence, and the process for adding new CI classes post-MVP. Without a governance baseline, even a well-configured CMDB degrades within 3–6 months of go-live.",
    who_fills="ECS SA drafts the framework with the customer IT Operations Manager. The IT Director approves the KPI targets. Finalised before Sprint 2 ends so governance is in place when Discovery runs continuously.",
    sprint_window="Sprint 2 Weeks 1–2 (draft) — confirmed by end of Sprint 2",
    estimated_effort="2–3 hours (one governance workshop with IT Ops Manager and IT Director)",
    related_workbooks=["02 CI Class Selection", "05 Service-CI Relationships", "Foundation Data Pack — Groups"],
    success_criteria=[
        "A named data steward is assigned to each in-scope CI class.",
        "Staleness thresholds (last_discovered > N days = stale) are defined per CI class.",
        "CMDB Health KPI targets are agreed and baselined.",
        "A CMDB governance review cadence (monthly recommended) is scheduled and has an owner.",
        "The process for requesting new CI classes post-MVP is documented.",
    ],
    process_decisions=[
        ("What staleness threshold should apply to Discovery-managed CIs?",
         "30 days for computer and server CIs (Discovery runs at least weekly). 90 days for manually maintained CIs. CIs not updated within the threshold are flagged as stale and should be reviewed for retirement.",
         "The OOTB CMDB Health dashboard uses the last_discovered date to calculate staleness. A 30-day threshold for Discovery-managed CIs is standard — it allows for Discovery interruptions without false positives."),
        ("Who is the CMDB data steward for each CI class?",
         "Assign a named individual from the IT Ops team to each in-scope CI class. The steward is responsible for reviewing CMDB Health reports monthly and actioning stale or orphaned CIs.",
         "Without named stewards, CMDB health reports generate alerts that nobody acts on. The steward role is operational, not technical — it requires 1–2 hours per month per class."),
        ("What CMDB Health score targets should we commit to?",
         "Completeness: 85%+ for mandatory attributes on in-scope CI classes. Relationship completeness: 80%+ for in-scope classes. Staleness: <5% of CIs stale at any given time. These are Sprint 2 targets; aim for 90%+ by Sprint 6.",
         "These targets are OOTB CMDB Health dashboard metrics. Starting at 85% gives realistic headroom for the first Discovery pass while still requiring a functional CMDB."),
        ("How should new CI classes be added after MVP?",
         "Any new CI class must go through a governance request: (1) business case (why is this needed?), (2) data source confirmed (how will it be populated?), (3) named data steward assigned, (4) CMDB impact assessed (does this require new Discovery patterns?). Approved by IT Director or IT Operations Manager.",
         "Ad-hoc CI class additions are the primary source of CMDB sprawl. A lightweight governance gate prevents low-value classes from being added without a data source."),
        ("What happens to a CI that Discovery cannot find for 90+ days?",
         "Flag for retirement review. The data steward reviews: is the asset still deployed? If yes, investigate why Discovery cannot find it (credential issue, subnet exclusion). If no, retire the CI record. Never auto-delete — always human review first.",
         "Auto-deleting CIs creates audit risk and breaks incident history. The OOTB retire workflow preserves the record and its history while removing it from active service impact analysis."),
    ],
    dependencies=[
        ("CI Class Selection (Workbook 02) confirmed", "Required", "ECS SA + Customer", "Sprint 1 Wk 2", "Governance applies to agreed CI classes only."),
        ("First Discovery run completed", "Required", "ECS Architect", "Sprint 2 Wk 1", "Baseline CMDB Health score requires CI data."),
        ("Foundation Data Pack — Groups (data steward groups) loaded", "Required", "ECS SA", "Sprint 0", "Steward assignment groups must exist."),
        ("IT Director available for KPI target approval", "Required", "Customer Project Sponsor", "Sprint 2 Wk 2", "KPI targets require business stakeholder sign-off."),
    ],
    config_sections=[
        ("Data Steward Assignments", [
            ("cmdb_ci_computer — Data Steward", "[Customer to complete — name and group]", "Typically the End User Computing team lead.", True),
            ("cmdb_ci_server — Data Steward", "[Customer to complete — name and group]", "Typically the Server/Infrastructure team lead.", True),
            ("cmdb_ci_vm_instance — Data Steward", "[Customer to complete]", "May be the same as server steward if same team manages VMs.", True),
            ("cmdb_ci_appl — Data Steward", "[Customer to complete]", "Application owners team or ITSM team.", True),
            ("CSDM Service CIs — Data Steward", "[Customer to complete]", "ITSM Process Owner. Responsible for service record accuracy.", True),
        ]),
        ("Staleness Thresholds", [
            ("cmdb_ci_computer — staleness threshold", "30 days (Discovery-managed)", "CMDB Health flags as stale if last_discovered > 30 days.", False),
            ("cmdb_ci_server — staleness threshold", "30 days (Discovery-managed)", "", False),
            ("cmdb_ci_vm_instance — staleness threshold", "30 days (Discovery-managed)", "", False),
            ("cmdb_ci_appl — staleness threshold", "30 days (SGC-managed)", "", False),
            ("CSDM Service CIs — staleness threshold", "90 days (manually maintained)", "Service records do not have a last_discovered date. Review quarterly.", False),
        ]),
        ("CMDB Health KPI Targets", [
            ("Mandatory attribute completeness (in-scope classes)", "85% by end Sprint 2 / 90%+ by Sprint 6", "", True),
            ("Relationship completeness (CIs with ≥1 service relationship)", "80% by end Sprint 2 / 90%+ by Sprint 6", "", True),
            ("Staleness rate (% of CIs stale)", "< 5% at any time", "", True),
            ("Orphaned CI rate (% with no service relationship)", "< 5% at any time", "", True),
        ]),
        ("Governance Review Cadence", [
            ("CMDB Health review frequency", "Monthly", "Data stewards review CMDB Health dashboard and action stale/orphaned CIs.", False),
            ("Governance review owner", "[Customer to complete — name and role]", "IT Operations Manager recommended.", True),
            ("New CI class request process", "Business case → data source confirmed → steward assigned → IT Director approval", "Document in customer runbook. ECS SA to provide runbook template.", False),
            ("CI retirement review process", "Flagged by CMDB Health → steward reviews → retires or investigates Discovery gap", "Use OOTB Retire workflow. Do not delete CI records.", False),
        ]),
    ],
    raci_rows=[
        ("Draft CMDB governance framework", "R/A", "C", "ECS SA drafts; customer reviews and confirms ownership commitments."),
        ("Assign CI class data stewards", "I", "R/A", "Customer IT Operations Manager assigns stewards."),
        ("Configure CMDB Health KPI thresholds in ServiceNow", "R/A", "I", "ECS SA configures CMDB Health dashboard targets."),
        ("Obtain IT Director approval of KPI targets", "I", "R/A", "Customer governance step."),
        ("Document CI retirement process in customer runbook", "R/A", "I", "ECS SA documents; hands off to IT Ops at end of engagement."),
        ("Conduct first monthly CMDB health review (post go-live)", "C", "R/A", "Customer IT Ops runs monthly reviews; ECS advises for first 2 cycles."),
        ("Review and action stale CI reports", "I", "R/A", "Customer data stewards action stale CIs monthly."),
    ],
    consultant_guide_sections=[
        ("Why governance must be in place before go-live", "CMDB governance is the unsexy deliverable that determines whether the CMDB is still useful 12 months after go-live. Every engagement that skips this step ends up with a CMDB re-scope engagement 18 months later. Use the governance workshop to get the customer to name specific people (not just roles) who will run the monthly health review. If no name can be attached, the governance framework is aspirational, not operational."),
        ("CMDB Health dashboard configuration", "Configure the CMDB Health dashboard in Sprint 2 with the agreed KPI targets. Set the staleness rules, mandatory attribute checks, and relationship completeness rules. Schedule the Health Score Calculation job to run daily. Show the customer the dashboard before Sprint 2 ends — they need to see a score, even if it's 70%, to understand what they're managing toward."),
        ("The retirement process is critical", "The single most common cause of CMDB health degradation after go-live is retired assets that were never retired in ServiceNow. Configure the retirement workflow to be triggered by: (a) the CMDB Health stale CI report, (b) the HAM asset disposition process (if HAM is in scope), and (c) an offboarding checklist item. Three triggers means CIs are retired when any of the three processes runs — reducing the chance of orphaned records."),
        ("Handoff preparation", "By the end of Sprint 6, the CMDB governance runbook must be handed to the customer IT Ops team. The runbook should cover: how to run the monthly health review, how to action stale CIs, how to request a new CI class, and how to retire a CI. This is not a technical document — write it for the IT Ops Manager who has never configured ServiceNow."),
    ],
    adoption_rows=[
        ("We don't need a formal governance process — our team will just keep it updated",
         "Implement the formal monthly CMDB Health review with named stewards and documented process.",
         "Informal governance works for 2–3 months after go-live when the engagement is fresh. It fails when team members change, when priorities shift, or when Discovery starts finding CIs from a new subnet that nobody remembers to relate to a service.",
         "'Formal governance doesn't mean bureaucracy — it means a 30-minute monthly meeting where someone looks at the CMDB Health dashboard and actions anything that's red. Without that scheduled touchpoint, CMDB health problems accumulate invisibly until they're large enough to break incident management.'",
         "Only for very small teams (<5 IT staff) with a genuinely stable environment. Still document the informal process."),
        ("We want to add CI classes whenever we need them",
         "Implement the CI class governance gate: business case, data source, steward, approval.",
         "Ad-hoc CI class additions without data sources create stub CI records that immediately become stale. The governance gate is 15 minutes of overhead per request — far less than the cleanup cost of an ungoverned CMDB.",
         "'The governance gate isn't about slowing you down — it's about making sure every CI class you add is actually maintained. The question we ask is simple: how will these CIs stay accurate after we add them? If that question has a clear answer, approval takes minutes.'",
         "The governance gate is non-negotiable. Simplify it for small teams, but never eliminate it."),
    ],
    snmap_sections=[
        ("CMDB Health Configuration", [
            ("CMDB Health dashboard", "CMDB > CMDB Health", "Configure KPI targets, staleness rules, and mandatory attribute checks here."),
            ("Health Score Calculation job", "CMDB > Health Calculation Job", "Schedule to run daily. Results feed the CMDB Health dashboard."),
            ("Staleness rule", "CMDB Health > Staleness Rules", "Configure per CI class with agreed thresholds from this workbook."),
        ]),
        ("CI Lifecycle Management", [
            ("Retire workflow", "CMDB > CI Lifecycle > Retire", "OOTB workflow for retiring CIs. Preserves record and history."),
            ("operational_status field", "cmdb_ci.operational_status", "1=Operational, 2=Non-Operational, 3=Repair in Progress, 6=End of Life, 7=Installed, 8=Retired. Use Retired (8) for decommissioned CIs."),
        ]),
    ],
)


# =============================================================================
# README — 00_README_CMDB_CSDM_Pack.docx
# =============================================================================
def build_readme(out_path):
    doc = EcsDocument(
        meta=DocMeta(
            eyebrow="ACCELERATOR PACK",
            title="CMDB-CSDM\nAccelerator Pack",
            subtitle="CSDM taxonomy, CI class selection, and CMDB governance for the OOTB-first ServiceNow engagement",
            org="ECS Federal · ServiceNow Practice",
            audience="Customer Project Sponsor, Enterprise Architect, IT Operations Manager, and named CMDB Data Stewards",
            companion_to="Foundation Data Pack · ITSM Accelerator Pack · Integration Accelerator Pack",
            doc_id="AP-CMDB-CSDM",
            version="1.0",
            status="Released",
            confidentiality="Shared — for the recipient and their organisation",
            running_header_label="CMDB-CSDM Accelerator Pack · ECS Federal",
        )
    )
    doc.add_cover_page()
    doc.add_page_break()

    doc.h1("What This Pack Is", numbered=False)
    doc.para(
        "This Accelerator Pack contains six workbooks that together define and govern the "
        "ServiceNow CMDB and Common Service Data Model (CSDM) for your engagement. The scope "
        "is deliberately focused on the minimum needed to make the CMDB trustworthy and useful "
        "from day one: a clean service taxonomy, a scoped CI class list, and a governance "
        "framework that keeps it accurate after go-live."
    )
    doc.para(
        "CSDM is the framework that connects configuration items (the things IT manages) to "
        "business services (the outcomes IT delivers). Without CSDM, your CMDB is a list of "
        "assets. With CSDM, it is a live map of how IT infrastructure supports business "
        "operations — the data model that powers service impact analysis, Virtual Agent service "
        "context, Predictive Intelligence, and CMDB Health dashboards."
    )
    doc.para(
        "The six workbooks follow a structured sequence: define the service taxonomy first "
        "(Workbook 01), agree which CI classes to track (Workbook 02), define the specific "
        "services (Workbooks 03 and 04), map the relationships (Workbook 05), and establish "
        "governance (Workbook 06). Do not skip workbooks or reverse the sequence — each one "
        "is a prerequisite for the next."
    )

    doc.h1("The Six Workbooks", numbered=False)
    doc.table(
        headers=["#", "Workbook", "What It Captures", "Customer Owner", "Sprint Window"],
        rows=[
            ["01", "CSDM Service Taxonomy", "Four-layer CSDM model — Foundational, Managed, Business, Application tiers; scope and naming standards", "Enterprise Architect / ITSM Owner", "Sprint 1, Wks 1–2"],
            ["02", "CI Class Selection", "MVP CI classes, mandatory attributes, Discovery sources, and out-of-scope rationale", "IT Operations Manager", "Sprint 1 Wk 2 – Sprint 2 Wk 1"],
            ["03", "Business Service Definitions", "One row per Business Service: name, owner, support group, SLA targets, user population", "ITSM Owner / IT Director", "Sprint 1 Wks 1–2"],
            ["04", "Technical Services & Applications", "Technical Service groupings and Application Service CIs that underpin each Business Service", "Infrastructure Lead / App Owners", "Sprint 1 Wk 2 – Sprint 2 Wk 2"],
            ["05", "Service-CI Relationships", "CI-to-service relationship matrix; IRE auto-relationship rules; orphaned CI triage", "ECS SA + IT Ops Lead", "Sprint 2 Wks 1–2"],
            ["06", "CMDB Governance Baseline", "Data steward assignments, staleness thresholds, CMDB Health KPI targets, review cadence", "IT Operations Manager", "Sprint 2 Wks 1–2"],
        ]
    )
    doc.para(
        "Each workbook contains eight tabs that mirror the ECS standard Accelerator Pack structure: "
        "Instructions (start here); Process Decisions (workshop questions with ECS OOTB recommendations "
        "pre-filled); Dependencies (prerequisites); Configuration Data (the OOTB-aligned values used "
        "to configure ServiceNow); R&R (RACI matrix); Consultant Guide (internal ECS reference); "
        "Adoption vs Re-engineering (OOTB defence language for common pushback scenarios); and "
        "ServiceNow Mapping (target tables and OOTB features). Customers focus on Instructions, "
        "Process Decisions, and Configuration Data. ECS consultants use all eight tabs."
    )

    doc.h1("Sprint Alignment", numbered=False)
    doc.para(
        "This pack spans Month 1 of the 18-week engagement — Sprint 1 (CSDM definition and "
        "validation) and Sprint 2 (Discovery initiation and CMDB normalisation). The Foundation "
        "Data Pack must be completed before this pack can begin: users, groups, locations, and "
        "departments must exist in ServiceNow before Business Service owners and data stewards "
        "can be assigned."
    )
    doc.para(
        "By the end of Sprint 2, the following must be in place: Business Service CIs loaded and "
        "approved, Technical Service CIs loaded, first Discovery run complete with CIs related to "
        "services, CMDB Health dashboard baselined, and the governance framework operational with "
        "named stewards. These are the prerequisites for the ITSM sprint builds (Sprints 3–4) "
        "where incident, problem, and change management all reference service data from this pack."
    )

    doc.h1("OOTB-First Principles", numbered=False)
    doc.para(
        "The ECS OOTB-first approach requires three commitments on CMDB and CSDM:"
    )
    doc.para(
        "First, use OOTB CSDM classifications — Business Service, Technical Service, Application "
        "Service, External Service. Do not create custom CI classes to represent service layers. "
        "Custom service tables require upgrade maintenance and block Predictive Intelligence and "
        "Virtual Agent from understanding service context."
    )
    doc.para(
        "Second, Discovery-first data sourcing. Do not migrate legacy CI records. Run Discovery, "
        "validate the results, and retire anything Discovery cannot confirm within 90 days. A "
        "small, accurate CMDB is more valuable than a large, inaccurate one."
    )
    doc.para(
        "Third, narrow MVP scope. Activate 5–8 CI classes at MVP. Add classes in subsequent "
        "phases with a governance gate. Every CI class you activate is a data quality commitment — "
        "staff it accordingly."
    )

    doc.h1("Completing This Pack Accurately and On Time", numbered=False)
    doc.para(
        "Completing Workbooks 01–04 accurately before Sprint 2 begins directly determines how much "
        "of Sprint 2 is spent on configuration versus data gathering. Workbooks 05 and 06 must be "
        "complete before Sprint 3 begins — incident management, problem management, and service "
        "request all depend on the service map and CI relationships established in this pack."
    )
    doc.para(
        "The IT Director or CIO must approve the Business Service list in Workbook 03 before ECS "
        "loads any service CIs. This is a governance requirement, not a formality. Service ownership "
        "decisions made incorrectly in Sprint 1 propagate through SLA assignment, major incident "
        "escalation, and service health alerting for the life of the platform."
    )

    doc.save(out_path)
    print(f"README saved: {out_path}")


# =============================================================================
# Build all files
# =============================================================================
if __name__ == "__main__":
    OUT = HERE

    print("Building CMDB-CSDM Accelerator Pack...")

    workbooks = [
        (wb1, "01_csdm_service_taxonomy.xlsx"),
        (wb2, "02_ci_class_selection.xlsx"),
        (wb3, "03_business_service_definitions.xlsx"),
        (wb4, "04_technical_services_and_apps.xlsx"),
        (wb5, "05_service_ci_relationships.xlsx"),
        (wb6, "06_cmdb_governance_baseline.xlsx"),
    ]

    for content, fname in workbooks:
        path = os.path.join(OUT, fname)
        build_workbook(content, path)
        print(f"  ✓ {fname}")

    build_readme(os.path.join(OUT, "00_README_CMDB_CSDM_Pack.docx"))

    print("\nCMDB-CSDM Accelerator Pack complete.")
    print(f"Output: {OUT}")
