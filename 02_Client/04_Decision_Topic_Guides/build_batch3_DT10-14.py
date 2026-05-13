"""Build CLT-DT-10 through CLT-DT-14."""
from dtg_builder import build_dtg

GUIDES = [

# ═══════════════════════════════════════════════════════════════════════════════
# CLT-DT-10  CMDB Class Selection
# ═══════════════════════════════════════════════════════════════════════════════
{
"doc_id": "CLT-DT-10",
"filename": "CMDB_Class_Selection_Decision_Guide_CLIENT.docx",
"short_name": "CMDB Class Selection",
"signal_subject": "your CMDB configuration",
"title": "CMDB Class Selection",
"subtitle": "A decision guide for choosing which configuration items to track, at what depth, and in what sequence",
"audience": "CMDB Owners, IT Operations, Infrastructure Teams, Asset Managers",
"companion_to": "CMDB Workshop Pre-Read · Discovery Pre-Read · HAM Pre-Read",
"how_to_use_paras": [
    "The CMDB is only as useful as the decisions made about its scope. An over-scoped CMDB — one "
    "that attempts to track every device, application, and network component from day one — "
    "produces high volume, low quality data that nobody trusts. An under-scoped CMDB leaves "
    "gaps that downstream processes (Incident routing, Change risk scoring, HAM lifecycle tracking) "
    "cannot fill. The right scope is the one where every CI class you track is actively used "
    "by at least one process.",
    "This guide walks through the four decisions that define your CMDB architecture: which CI "
    "classes to populate, how much attribute depth each class needs, how CI relationships are "
    "captured, and who governs the data quality over time.",
    "Read this alongside the Discovery Phasing guide. Discovery is the primary mechanism for "
    "populating CMDB automatically — the CI classes you select here will shape which Discovery "
    "patterns and Service Graph Connectors need to be configured.",
],
"why_matters": [
    {"h2": "Incident and Change accuracy depend on CI data quality",
     "body": "When an incident references a CI, ServiceNow can automatically calculate business "
             "impact (which services are affected), identify related open changes (is there a "
             "maintenance window that explains this?), and route the ticket to the CI owner. "
             "When the CI does not exist, or exists with stale data, none of those capabilities "
             "function. CI data quality is a prerequisite for the higher-value Incident and "
             "Change workflows — not an optional enrichment."},
    {"h2": "HAM lifecycle tracking lives in the CMDB",
     "body": "Hardware Asset Management tracks assets as Configuration Items. The lifecycle "
             "states (Ordered, Received, In Stock, Deployed, Retired) and the relationships "
             "(this laptop is assigned to this user, connected to this network) are CMDB data. "
             "The quality of your HAM implementation is therefore bounded by the quality of "
             "your CMDB for the hardware CI classes."},
    {"h2": "AI capabilities use CI context for smarter recommendations",
     "body": "Predictive Intelligence uses CI data as a routing signal — the same issue on a "
             "P1-critical server is routed differently than the same issue on a developer "
             "workstation. Change risk assessment uses CI criticality classification to calculate "
             "blast radius. The richer and more accurate your CI data, the more context AI "
             "capabilities have for making relevant recommendations."},
],
"signals": [
    {"h2": "CI records are created but never updated",
     "body": "A CMDB full of CI records with last-modified dates from the initial import is "
             "a CMDB that reflects the past, not the present. Static CMDB data is worse than "
             "no CMDB data in some respects — it creates false confidence. The moment CI data "
             "stops being current, it stops being trustworthy for process automation."},
    {"h2": "CI classes were selected without a process consumer in mind",
     "body": "The most common CMDB scope error is tracking CI classes because they exist in "
             "the data model, not because any process uses them. A CI class with no process "
             "consuming it — no Incident routing based on it, no Change risk assessment using "
             "it, no HAM lifecycle connected to it — is configuration overhead with no return."},
    {"h2": "CMDB health score is below 70%",
     "body": "ServiceNow's CMDB Health dashboard provides a data quality score across "
             "completeness, staleness, and orphaned record dimensions. A score below 70% "
             "indicates that a significant portion of CI records have missing mandatory attributes, "
             "stale data, or no relationship connections — and should trigger a scoping and "
             "governance review."},
],
"decisions": [
    {"label": "Which CI classes will you populate in Phase 1?",
     "body": "Select CI classes based on the processes that will use them, not based on "
             "infrastructure completeness. The Phase 1 recommendation: Server (for Incident "
             "and Change routing), Application (for CSDM service mapping), and Hardware Asset "
             "for end-user computing (for HAM). Add network, cloud, and database CI classes "
             "in subsequent phases as Discovery coverage grows.",
     "questions": [
         "Which Incident routing decisions need CI context to be more accurate?",
         "Which Change types need CI criticality data for risk scoring?",
         "Is HAM in scope? If so, which hardware CI classes need to be populated?",
     ],
     "landing": "Start with 3–5 CI classes tied to specific process consumers. Each additional "
                "class requires a named owner and a data population plan before it goes live."},
    {"label": "What attribute depth is required for each class?",
     "body": "Each CI class has dozens of possible attributes. Only a fraction of those attributes "
             "are actively used by processes. Populating attributes that no process reads is "
             "configuration overhead. For each CI class in scope, define the minimum attribute "
             "set needed by the processes that consume it — and make those mandatory. "
             "Leave optional attributes optional.",
     "questions": [
         "For Server CIs: which attributes are used by Incident routing, Change risk, and CMDB health reporting?",
         "For Hardware CIs: which attributes are needed for HAM lifecycle tracking and asset audit?",
         "Are there compliance or audit requirements that mandate specific CI attributes?",
     ]},
    {"label": "How will CI relationships be captured?",
     "body": "CI relationships — 'this server runs this application,' 'this application depends "
             "on this database' — are what turn a CI inventory into a service dependency map. "
             "Relationships can be populated automatically by Discovery and Service Graph "
             "Connectors, or manually for high-priority CIs where automated discovery is "
             "not yet configured.",
     "questions": [
         "Are the relationships most important for your Incident and Change processes discoverable automatically?",
         "Is there a manual relationship definition process for the critical CIs that cannot be auto-discovered?",
         "Is CSDM being built concurrently — and will service relationships be defined at the CSDM layer?",
     ]},
    {"label": "Who governs CMDB data quality, and what is the review cadence?",
     "body": "CMDB data quality requires active governance — someone reviews the CMDB Health "
             "score, investigates staleness flags, and approves new CI class additions. Without "
             "a named owner and a review schedule, CMDB data drifts from current state within "
             "3–6 months of go-live. The workshop will assign ownership and define the minimum "
             "governance cadence.",
     "questions": [
         "Who is the named CMDB owner post-go-live?",
         "How frequently will the CMDB Health dashboard be reviewed?",
         "What is the process for requesting a new CI class or a new mandatory attribute?",
     ]},
],
"good_rows": [
    ["Every populated CI class is consumed by at least one active process", "CI classes populated because they exist in the data model, not because any process uses them"],
    ["CI records updated automatically by Discovery or Service Graph Connectors", "CI records created at import and never updated — data is a historical snapshot"],
    ["CMDB Health score above 80% — completeness, staleness, and orphan metrics green", "CMDB Health below 70% — systematic data quality issues across multiple dimensions"],
    ["Mandatory attributes defined per class based on process consumer requirements", "All attributes optional — CMDB records have inconsistent completeness"],
    ["Named CMDB owner reviews health monthly and closes gaps", "CMDB owned by everyone and no one — health score not reviewed"],
    ["CI class scope expands only when a new process consumer is identified", "CI classes added without a consuming process — scope grows without quality following"],
],
"patterns": [
    {"label": "Pattern A — Three CI classes, high fidelity",
     "body": "A federal agency limited Phase 1 CMDB scope to three CI classes: Server, "
             "Business Application (for CSDM), and Computer (for HAM). Every CI in those "
             "three classes had a defined set of mandatory attributes, a Discovery pattern "
             "populating them automatically, and a named owner per class. CMDB Health score "
             "was 88% at 90 days post-go-live. The agency resisted requests to expand scope "
             "in Phase 1 and had a working, trusted CMDB foundation when Phase 2 began."},
    {"label": "Pattern B — CI relationship manual seeding for critical systems",
     "body": "A healthcare organization had 12 mission-critical applications that needed "
             "service relationship mapping before Discovery was fully configured. They ran "
             "a two-week manual seeding exercise: an architect walked through each critical "
             "application and manually documented its dependencies on servers, databases, "
             "and network components. Those 12 application service maps were then available "
             "for Incident impact calculation and Change risk scoring immediately at go-live, "
             "before automated discovery was complete."},
    {"label": "Pattern C — CMDB Health as a standing dashboard item",
     "body": "A technology company added CMDB Health score to their weekly IT operations "
             "review dashboard — alongside Incident SLA compliance and Change success rate. "
             "The visibility created accountability: when the staleness metric dropped below "
             "75% in month three, the conversation happened immediately rather than being "
             "discovered in an audit. The root cause (a Discovery schedule gap) was fixed "
             "within the same week it was flagged."},
],
"workshop_para": (
    "The workshop will map your process areas to CI class requirements, define the mandatory "
    "attribute set for each class in scope, review the Discovery and Service Graph Connector "
    "configuration plan against the class selection, and assign data governance ownership. "
    "The output is a CMDB scope document with a phased expansion roadmap."
),
"need_bullets": [
    "Current infrastructure inventory (spreadsheet, existing CMDB export, or architecture diagram)",
    "List of process areas in scope — Incident, Change, HAM — to map CI class requirements",
    "Discovery deployment plan if already underway (MID Server locations, scan scope)",
    "Cloud environment inventory (AWS accounts, Azure subscriptions) for Service Graph Connector planning",
],
"questions": [
    "Do you have an existing CMDB? If so, what is the current record count and health score?",
    "Which process decisions most urgently need CI data — Incident routing, Change risk, HAM?",
    "Is your infrastructure primarily on-premises, cloud, or hybrid?",
    "Who currently owns infrastructure inventory in your organization?",
    "Are there CI classes you know you need but are not sure how to populate?",
],
"xrefs": [
    ["CMDB Workshop Pre-Read", "Background reading for the CMDB workshop session", "02_Client/05_Workshop_Pre-Reads/"],
    ["Discovery Phasing Decision Guide", "Discovery populates CMDB CIs automatically — the two designs are linked", "02_Client/04_Decision_Topic_Guides/"],
    ["CSDM Workshop Pre-Read", "CSDM service hierarchy builds on CMDB CI data — understand the sequencing", "02_Client/05_Workshop_Pre-Reads/"],
],
},

# ═══════════════════════════════════════════════════════════════════════════════
# CLT-DT-11  Discovery Phasing
# ═══════════════════════════════════════════════════════════════════════════════
{
"doc_id": "CLT-DT-11",
"filename": "Discovery_Phasing_Decision_Guide_CLIENT.docx",
"short_name": "Discovery Phasing",
"signal_subject": "your Discovery deployment",
"title": "Discovery Phasing",
"subtitle": "A decision guide for rolling out automated infrastructure scanning in the right sequence",
"audience": "CMDB Owners, Infrastructure Teams, Network Teams, Security Teams",
"companion_to": "Discovery Workshop Pre-Read · CMDB Class Selection Decision Guide",
"how_to_use_paras": [
    "Discovery is the ServiceNow capability that scans your network infrastructure and populates "
    "your CMDB automatically. A well-phased Discovery deployment produces a trusted CMDB that "
    "stays current with your environment. A poorly sequenced deployment produces CI sprawl — "
    "thousands of CIs that nobody owns, many that are duplicates, and a CMDB that teams quickly "
    "learn not to rely on.",
    "The key insight is that Discovery scope and CMDB class selection must be designed together. "
    "There is no point scanning everything in your network if you have not decided which CI "
    "classes to populate and which mandatory attributes to enforce. Discovery without a "
    "defined CMDB target produces noise.",
    "This guide walks through the four Discovery phasing decisions: which network zones to "
    "scan first, where to place MID Servers, how to scope credentials, and how to govern "
    "the reconciliation process that prevents duplicate CIs from accumulating.",
],
"why_matters": [
    {"h2": "Manual CMDB maintenance is not sustainable",
     "body": "Every organization that attempts to maintain a CMDB manually discovers the same "
             "thing: the data is accurate at go-live and increasingly inaccurate thereafter. "
             "Servers are commissioned and decommissioned. Software is installed and removed. "
             "Network topology changes. Manual processes cannot keep pace with a dynamic "
             "infrastructure. Discovery makes CMDB maintenance an automated process — changes "
             "are detected and recorded on the scan schedule without manual intervention."},
    {"h2": "Discovery phase decisions determine CMDB data quality from the start",
     "body": "If Discovery is configured to scan too broadly too early — before CI class "
             "definitions and mandatory attributes are finalized — the initial scan produces "
             "CIs that do not match the target schema. Cleaning up a large set of incorrectly "
             "structured CIs is a significant rework effort. Starting narrow and expanding "
             "as the CI model matures avoids that cleanup."},
    {"h2": "Security teams need to be part of the Discovery planning conversation",
     "body": "Discovery scans produce network traffic and require authentication credentials "
             "stored in ServiceNow. Some organizations have security policies that restrict "
             "scanning traffic, require firewall rule changes, or mandate specific credential "
             "handling processes. Discovering these constraints after MID Servers are deployed "
             "delays the Discovery timeline. Security alignment is a phase-one task, not an "
             "afterthought."},
],
"signals": [
    {"h2": "CMDB contains large numbers of orphaned or duplicate CIs",
     "body": "Orphaned CIs (no relationships, no process connections) and duplicate CIs (the "
             "same device discovered multiple times from different scan sources) are the most "
             "common signs of a Discovery deployment that expanded faster than the CMDB "
             "governance could keep up with. Both are prevention problems — the Identification "
             "and Reconciliation Engine (IRE) prevents duplicates when correctly configured, "
             "and class scope decisions prevent orphans."},
    {"h2": "Discovery schedules run but CMDB updates do not happen",
     "body": "When Discovery scans complete but CI records are not updated, the cause is usually "
             "credential failure (Discovery cannot authenticate to the device) or a pattern "
             "mismatch (the device type is not recognized by the configured Discovery patterns). "
             "Both are solvable, but they require active monitoring of Discovery logs — "
             "a governance activity that needs an owner."},
],
"decisions": [
    {"label": "Which network zones and infrastructure segments to scan in Phase 1?",
     "body": "Prioritize the network zones that host the CIs most critical to your Phase 1 "
             "process areas. If Incident routing on critical servers is the Phase 1 use case, "
             "start with the data center segments hosting those servers. If HAM is Phase 1, "
             "start with the network segments where end-user endpoints are registered.",
     "questions": [
         "Which network segments host the infrastructure most critical to your Phase 1 process areas?",
         "Are there segments that should be excluded — air-gapped networks, classified environments, OT/ICS?",
         "What cloud environments (AWS VPCs, Azure VNets) are in scope, and do they require cloud-native Discovery?",
     ],
     "landing": "Phase 1: scan the 2–3 segments most relevant to your in-scope process areas. "
                "Add segments in subsequent phases as the CI governance model matures."},
    {"label": "Where to place MID Servers?",
     "body": "A MID Server must be reachable from the devices it scans and must have outbound "
             "access to the ServiceNow instance. The number of MID Servers needed depends on "
             "your network topology: each segment separated by a firewall typically needs its "
             "own MID Server. Cloud environments use cloud-native Discovery rather than "
             "MID Servers in most cases.",
     "questions": [
         "How many distinct network segments separated by firewalls are in scope?",
         "Is there a standard server or VM that can host a MID Server in each required segment?",
         "What are the outbound firewall requirements for MID Server to ServiceNow communication?",
     ]},
    {"label": "What credentials should Discovery use, and how are they managed?",
     "body": "Discovery requires service account credentials to authenticate against discovered "
             "devices (SSH for Linux, WMI for Windows, SNMP for network devices). These "
             "credentials are stored in the ServiceNow Credential Store. The design decision "
             "is scope: should one credential set cover all devices, or should credentials "
             "be scoped by device type or network zone?",
     "questions": [
         "Are there separate service accounts for different environments (production vs. development)?",
         "What is the process for provisioning service accounts in your organization?",
         "Are there network devices that require SNMP community strings rather than standard authentication?",
     ]},
    {"label": "How will CI reconciliation prevent duplicates?",
     "body": "The Identification and Reconciliation Engine (IRE) uses defined rules to match "
             "newly discovered CIs against existing CMDB records and prevent duplicates. "
             "The default IRE configuration works well for most environments, but organizations "
             "with multiple data sources (Discovery + Intune + manual import) need to review "
             "the reconciliation rules to ensure the right source wins when records conflict.",
     "questions": [
         "Will multiple sources populate the same CI class (e.g., both Discovery and Intune for endpoints)?",
         "Should Discovery data win over manually entered data when there is a conflict?",
         "Is there a process for reviewing and resolving IRE conflicts that require human judgment?",
     ]},
],
"good_rows": [
    ["Discovery scope matches CMDB class scope — only scanning what will be tracked", "Discovery scanning everything — producing CIs in classes that no process uses"],
    ["MID Servers deployed in all required network segments before scans begin", "MID Servers covering only some segments — gaps in CMDB coverage"],
    ["IRE configured and duplicate rate below 2%", "Duplicate CIs accumulating without a reconciliation process to address them"],
    ["Discovery logs monitored weekly — credential and pattern failures investigated", "Discovery runs complete but failures are not monitored or addressed"],
    ["Credentials managed in ServiceNow Credential Store with rotation process defined", "Credentials hardcoded in Discovery configuration — rotation is manual and error-prone"],
    ["Phase expansion criteria defined — new segments added when CI governance is proven", "Discovery expanded to new segments before existing scope is governed and stable"],
],
"patterns": [
    {"label": "Pattern A — Starting with critical server segment only",
     "body": "A federal agency limited Phase 1 Discovery to one network segment: the data center "
             "hosting their 40 most critical servers. Discovery was configured, credential "
             "provisioning was completed, and IRE rules were validated before any other segment "
             "was added. At 90 days post-go-live, that segment's CI data was 94% accurate. "
             "The agency added three more segments in Phase 2, using the Phase 1 configuration "
             "as a validated template."},
    {"label": "Pattern B — Cloud-native Discovery for Azure environment",
     "body": "A technology company with a primarily Azure-hosted infrastructure used the Azure "
             "Service Graph Connector rather than MID Server-based Discovery for their cloud "
             "resources. The connector populated Azure VM, App Service, and SQL Database CIs "
             "automatically. On-premises equipment used MID Server-based Discovery. The two "
             "populations were kept in separate CI subclasses to allow different attribute "
             "requirements and ownership models."},
    {"label": "Pattern C — Security review as a Phase 0 activity",
     "body": "A healthcare organization built a Discovery security review into Phase 0 of "
             "their engagement — four weeks before MID Server deployment. The security team "
             "reviewed the Discovery traffic patterns, approved the firewall rule changes "
             "required for MID Server connectivity, and documented the credential provisioning "
             "process. By the time MID Servers were deployed, every security requirement was "
             "already met. Organizations that skip this step typically experience 3–6 week "
             "delays when security review happens after deployment."},
],
"workshop_para": (
    "The workshop will map your infrastructure environment to the Discovery phase plan: "
    "which segments to scan first, where MID Servers will be deployed, what credentials "
    "are needed and how they will be provisioned, and how the IRE will be configured for "
    "your multi-source environment. We will also define the Discovery log monitoring process "
    "and the phase expansion criteria."
),
"need_bullets": [
    "Network topology diagram and IP range documentation for in-scope segments",
    "Server and platform inventory for the segments in scope for Phase 1",
    "Firewall policy or ACL documentation to assess MID Server connectivity requirements",
    "Cloud environment details (AWS accounts, Azure subscriptions, VPC/VNet listings)",
    "Service account provisioning process and contacts",
],
"questions": [
    "Do you have network segmentation documentation — VLANs, subnets, and firewall boundaries?",
    "How many distinct network zones separated by firewalls are in scope for Phase 1?",
    "Are there segments that must be excluded from Discovery for security or compliance reasons?",
    "What service account provisioning process exists, and how long does it typically take?",
    "Are there existing MID Servers in your environment, or will this be a fresh deployment?",
],
"xrefs": [
    ["Discovery Workshop Pre-Read", "Background reading for the Discovery workshop session", "02_Client/05_Workshop_Pre-Reads/"],
    ["CMDB Class Selection Decision Guide", "CI class scope determines what Discovery populates — design the two together", "02_Client/04_Decision_Topic_Guides/"],
    ["Service Graph Connectors Workshop Pre-Read", "Service Graph Connectors complement Discovery for cloud and third-party tools", "02_Client/05_Workshop_Pre-Reads/"],
],
},

# ═══════════════════════════════════════════════════════════════════════════════
# CLT-DT-12  Integration Prioritization
# ═══════════════════════════════════════════════════════════════════════════════
{
"doc_id": "CLT-DT-12",
"filename": "Integration_Prioritization_Decision_Guide_CLIENT.docx",
"short_name": "Integration Prioritization",
"signal_subject": "your integration roadmap",
"title": "Integration\nPrioritization",
"subtitle": "A decision guide for choosing which integrations to build first and how to build them sustainably",
"audience": "IT Leadership, Integration Architects, Platform Owners, Process Owners",
"companion_to": "Platform Foundation Workshop Pre-Read · Service Graph Connectors Pre-Read",
"how_to_use_paras": [
    "Every ServiceNow implementation involves integrations — connections to Active Directory, "
    "cloud platforms, monitoring tools, HR systems, asset management tools, and more. The "
    "question is never whether to integrate but which integrations to build first, how to "
    "build them in a way that is maintainable, and which integrations can be served by "
    "ServiceNow's pre-built connectors rather than custom development.",
    "Integration decisions have a disproportionate impact on project timeline. A single "
    "complex integration that is scoped incorrectly or assigned to an unavailable technical "
    "resource can consume weeks of the sprint. The prioritization decisions in this guide "
    "are designed to protect the timeline by sequencing integrations from highest-value "
    "and lowest-complexity to highest-value and highest-complexity — and deferring "
    "everything else.",
    "ServiceNow's pre-built connector ecosystem covers a significant portion of enterprise "
    "integration needs — often without any custom development. Reviewing the connector "
    "catalog before committing to custom integration is always the right first step.",
],
"why_matters": [
    {"h2": "Foundation integrations unlock every downstream process area",
     "body": "Active Directory and Entra ID integration is the single most foundational: "
             "it populates the user directory that every other ServiceNow process depends on. "
             "SSO integration determines how users authenticate. SCCM or Intune integration "
             "feeds asset data to HAM. These foundation integrations have no process-area "
             "prerequisites — they should be the first integrations built, regardless of "
             "the order of other sprint work."},
    {"h2": "Custom integrations create maintenance debt",
     "body": "Every custom integration is a code artifact that must be maintained across "
             "ServiceNow upgrades, API changes in the source system, and organizational "
             "changes. Pre-built connectors are maintained by ServiceNow and updated with "
             "each platform release. The ratio of custom-to-connector integrations is "
             "a useful technical debt metric — an engagement that ends with 12 custom "
             "integrations and 2 connectors has more maintenance risk than one that ends "
             "with 4 custom integrations and 10 connectors."},
    {"h2": "Integration scope creep is the most common sprint timeline risk",
     "body": "Integrations are the most common source of sprint scope expansion during "
             "an ITSM implementation. A data feed that 'should be simple' reveals API "
             "authentication requirements, data quality issues, or source system access "
             "restrictions that each add days to the timeline. Prioritizing integrations "
             "explicitly — and freezing scope once the sprint begins — is the most effective "
             "mitigation."},
],
"signals": [
    {"h2": "Integration requests arrive throughout the engagement without prioritization",
     "body": "When integration requests are added to the backlog as they are identified — "
             "rather than prioritized at the start — the integration scope expands continuously. "
             "By mid-engagement, the integration list has grown beyond what the sprint schedule "
             "can absorb, and decisions about what to defer happen under time pressure "
             "rather than strategically."},
    {"h2": "Custom development is proposed for integrations that have pre-built connectors",
     "body": "AWS, Azure, Intune, Active Directory, Okta, Qualys, and dozens of other platforms "
             "have ServiceNow-certified connectors that require no custom development. "
             "When custom development is proposed for any of these, the first question "
             "should be: does a certified connector already exist?"},
],
"decisions": [
    {"label": "Which integrations are required for Sprint 1 go-live?",
     "body": "Identify the integrations without which the core platform cannot function: "
             "user directory sync (AD/Entra), SSO authentication, and email for notifications. "
             "These are non-negotiable Sprint 1 requirements. Everything else should be "
             "evaluated against sprint capacity and deferred if necessary.",
     "questions": [
         "Which systems must be integrated before any ServiceNow user can log in and work?",
         "Is SSO already configured in a prior ServiceNow environment, or does it need to be built from scratch?",
         "Which integrations feed data that downstream sprint work depends on?",
     ],
     "landing": "Sprint 1 integration scope: AD/Entra sync, SSO, email notifications. Everything else "
                "is Sprint 2 or later."},
    {"label": "Connector vs. custom integration — which approach for each in-scope integration?",
     "body": "For every integration on the list, the first question is: does a ServiceNow-certified "
             "connector exist? Certified connectors for SCCM, Intune, AWS, Azure, Okta, Qualys, "
             "and others eliminate custom development. If a connector exists and meets the "
             "requirement, the connector is the answer — the cost comparison (connector "
             "configuration vs. custom development and maintenance) is never close.",
     "questions": [
         "What is the source system for each integration — does a ServiceNow connector exist?",
         "For integrations without a connector: what is the source system API, and who owns it?",
         "Are there integration requirements that connectors cannot meet — and if so, why?",
     ]},
    {"label": "What is the data flow direction and volume for each integration?",
     "body": "Each integration has a direction (ServiceNow reads from source, ServiceNow writes "
             "to target, or bidirectional) and a volume (how many records, how frequently). "
             "High-volume, high-frequency bidirectional integrations are the highest-risk "
             "scope items. Defining direction and volume before development begins prevents "
             "the most common integration scope surprises.",
     "questions": [
         "For each integration: does ServiceNow need to read, write, or both?",
         "What is the expected record volume — hundreds, thousands, millions?",
         "What is the required synchronization frequency — real-time, hourly, daily?",
     ]},
    {"label": "Who owns each integration post-go-live?",
     "body": "Every integration needs a named owner: the person responsible when the source "
             "system changes its API, when the integration fails, or when the data quality "
             "degrades. Integrations without named owners accumulate silently until a failure "
             "makes them visible. The workshop will assign ownership for every in-scope "
             "integration.",
     "questions": [
         "Who owns the source system for each integration — and have they been engaged?",
         "Who on the IT side is responsible for monitoring integration health?",
         "What is the process for updating an integration when the source system changes?",
     ]},
],
"good_rows": [
    ["Foundation integrations (AD, SSO, email) built in Sprint 1", "Foundation integrations deferred — subsequent sprints blocked by missing user data"],
    ["Certified connectors used wherever available", "Custom development built for integrations that have certified connectors"],
    ["Integration scope frozen at sprint start — additions require change control", "Integration requests added throughout the sprint — scope grows continuously"],
    ["Named owner for every integration with a monitoring process", "Integrations running without an owner — failures discovered only when a process breaks"],
    ["Data direction and volume documented before development begins", "Volume and direction assumptions discovered during development — timeline surprises"],
    ["Integration health included in operational monitoring dashboard", "Integrations not monitored — silently degrading data quality"],
],
"patterns": [
    {"label": "Pattern A — Connector-first audit saving 8 weeks of development",
     "body": "A technology company entered implementation planning with a list of 14 integrations "
             "flagged for custom development. An ECS connector audit found that 8 of the 14 "
             "had certified ServiceNow connectors: Intune, AWS, Azure, Okta, Qualys, and three "
             "others. Switching from custom development to connector configuration saved an "
             "estimated 8 weeks of development time and eliminated 8 custom code artifacts "
             "from the ongoing maintenance burden."},
    {"label": "Pattern B — Integration scope freeze protecting sprint timelines",
     "body": "A federal agency implemented a formal integration scope freeze: any integration "
             "not on the approved Phase 1 list required a written change request reviewed by "
             "the steering committee. Three change requests were submitted during the "
             "engagement; two were deferred to Phase 2, one was approved with a corresponding "
             "scope reduction elsewhere. No sprint timeline was exceeded. Agencies without "
             "this process averaged 2.3 weeks of timeline extension per sprint."},
    {"label": "Pattern C — SCCM integration as a HAM data foundation",
     "body": "A healthcare organization used the ServiceNow SCCM connector to populate endpoint "
             "CIs with hardware inventory data. The connector sync ran nightly and updated "
             "Computer CI records with installed software, hardware configuration, and last-seen "
             "date. HAM lifecycle tracking for 12,000 endpoints was available from day one "
             "without any custom development, and asset audit accuracy improved from 68% "
             "to 94% in the first quarter."},
],
"workshop_para": (
    "The workshop will produce a prioritized integration list with a connector vs. custom "
    "classification for each item, data direction and volume estimates, named owners, and "
    "a sprint assignment for each integration. We will also review the integration scope "
    "against sprint capacity and make explicit decisions about what to defer."
),
"need_bullets": [
    "Complete list of systems that need to connect to ServiceNow — in any direction",
    "For each system: technical contacts who own the source API or data feed",
    "Existing integration documentation if any integrations have been built previously",
    "SSO and identity provider configuration details (AD, Entra ID, SAML)",
],
"questions": [
    "What systems need to connect to ServiceNow, and do you have a list of them?",
    "Is Active Directory or Entra ID the primary identity source for your environment?",
    "Are there integrations your team considers mandatory for go-live?",
    "Who are the technical owners of the key source systems (SCCM, cloud platforms, monitoring tools)?",
    "Have you done any ServiceNow integration work before — are there existing integration patterns or tools in use?",
],
"xrefs": [
    ["Platform Foundation Workshop Pre-Read", "Foundation integrations (AD, SSO) are covered in the Platform Foundation sprint", "02_Client/05_Workshop_Pre-Reads/"],
    ["Service Graph Connectors Workshop Pre-Read", "Service Graph Connectors are pre-built integrations for CMDB population", "02_Client/05_Workshop_Pre-Reads/"],
    ["HAM Workshop Pre-Read", "SCCM and Intune integrations feed HAM asset data", "02_Client/05_Workshop_Pre-Reads/"],
],
},

# ═══════════════════════════════════════════════════════════════════════════════
# CLT-DT-13  Custom-vs-OOTB Decision Framework
# ═══════════════════════════════════════════════════════════════════════════════
{
"doc_id": "CLT-DT-13",
"filename": "Custom_vs_OOTB_Decision_Framework_CLIENT.docx",
"short_name": "Custom vs. OOTB",
"signal_subject": "your approach to customization decisions",
"title": "Custom vs. OOTB\nDecision Framework",
"subtitle": "A customer-facing guide to understanding how customization decisions are made — and why the default is always the platform",
"audience": "Project Sponsors, IT Leadership, Process Owners, Service Owners, Change Advisory Board",
"companion_to": "18-Week OOTB-First Journey Overview · Technical Debt Elimination Roadmap",
"how_to_use_paras": [
    "At some point in the engagement, your team will encounter a requirement that the "
    "ServiceNow out-of-the-box configuration does not address exactly as described. "
    "This is a normal part of every implementation. What distinguishes this engagement "
    "from a conventional implementation is how those moments are handled — and this guide "
    "gives you the framework your team and ours will use when they arise.",
    "The framework is not a prohibition on customization. It is a structured way of ensuring "
    "that every customization decision is deliberate, documented, and made with full "
    "awareness of the long-term cost it carries. Some requirements genuinely require "
    "customization. Many that initially appear to require it do not — they can be met "
    "by the OOTB platform when the requirement is examined more carefully.",
    "Understanding this framework before the workshops begin means your team can participate "
    "in the decision as a full partner — not as someone receiving a recommendation they "
    "do not have context to evaluate.",
],
"why_matters": [
    {"h2": "Every customization is a liability, not just an asset",
     "body": "Customization delivers a capability. It also creates a maintenance obligation: "
             "the customization must be tested with every ServiceNow upgrade, maintained when "
             "business requirements change, and documented so future team members can understand "
             "it. An organization with 500 customizations has 500 maintenance obligations. "
             "An organization with 50 has 50. The difference compounds across every upgrade "
             "cycle and every personnel change."},
    {"h2": "OOTB capabilities evolve — customizations do not",
     "body": "ServiceNow releases new platform capabilities three times per year. OOTB "
             "configurations receive those capabilities automatically. Customizations either "
             "block the new capability from activating, require code changes to accommodate "
             "it, or are rendered redundant when the OOTB platform catches up. Every "
             "customization is a bet that the capability gap it addresses will not be closed "
             "by the platform in the next 12–18 months. That bet has a poor historical track record."},
    {"h2": "The Governance Triage Log captures requirements that are not lost",
     "body": "Requirements that do not meet the customization threshold are not discarded — "
             "they are entered into the Governance Triage Log. The log ensures that "
             "legitimate business requirements that do not warrant customization today have "
             "a documented home and a path to resolution in a future phase. No business "
             "requirement is ignored. Some are deferred with documented reasoning."},
],
"signals": [
    {"h2": "Customization requests are increasing as the engagement progresses",
     "body": "A gradual increase in customization requests across sprint reviews is a normal "
             "pattern — requirements become more specific as the platform becomes more real. "
             "An accelerating increase, however, is a signal that requirements are not being "
             "challenged against OOTB capabilities early enough, or that the initial "
             "discovery process did not surface the full requirement set."},
    {"h2": "Customization decisions are made informally without documentation",
     "body": "When customization decisions are made in meetings without a formal record, "
             "two things happen: the reasoning is lost (future team members do not know "
             "why the customization exists) and accountability is diffused (no one owns "
             "the decision). The customization council and triage log exist to prevent both."},
],
"decisions": [
    {"label": "Is the requirement a genuine gap or a preference?",
     "body": "The first question for any customization request is: is the OOTB platform "
             "genuinely incapable of meeting this requirement, or is the OOTB capability "
             "simply different from how the team has done things before? "
             "Preference-based customization — 'we prefer the old interface,' 'we are used "
             "to this field being here' — is the largest driver of unnecessary customization. "
             "It is also the most socially difficult category to address, because the "
             "preference is real even when the gap is not.",
     "questions": [
         "Can the OOTB platform meet the underlying business need, even if the approach differs?",
         "Has the team seen the OOTB capability demonstrated — or is the gap assumption based on the current tool?",
         "Would the preference require customization, or can it be addressed through configuration?",
     ],
     "landing": "Configuration (changing field values, adjusting workflows, modifying layouts) is "
                "always the first option. Customization (modifying platform code or schema) is "
                "the last resort."},
    {"label": "If a genuine gap, what is the total cost of customization?",
     "body": "When a requirement genuinely cannot be met by OOTB configuration, the "
             "customization decision requires a full cost assessment: initial development "
             "cost, testing cost per upgrade cycle, documentation cost, and the opportunity "
             "cost of the developer time not spent on other work. The comparison is between "
             "the cost of the customization and the cost of adapting the business process "
             "to the OOTB capability.",
     "questions": [
         "What is the estimated development and testing effort for this customization?",
         "How many ServiceNow upgrades will this customization require testing across its lifetime?",
         "What is the business cost of adopting the OOTB approach — retraining, process change, or genuinely missing capability?",
     ]},
    {"label": "Who has authority to approve a customization?",
     "body": "Customization approvals require a named decision-maker with authority to "
             "commit the associated maintenance obligation on behalf of the organization. "
             "In this engagement, that authority sits with the Customization Council — "
             "a standing group that reviews customization requests against the OOTB-first "
             "criteria and approves, defers, or rejects them with documented reasoning.",
     "questions": [
         "Who are the Customization Council members for this engagement?",
         "What is the review cadence — how quickly can a customization request receive a decision?",
         "Is there a fast-track process for urgent customization requests?",
     ]},
    {"label": "How will deferred requirements be managed in the Governance Triage Log?",
     "body": "Requirements that are deferred — not customized now, but not permanently excluded — "
             "are entered in the Governance Triage Log with the original requirement, the "
             "deferral reasoning, and a review trigger (e.g., 'revisit if this requirement "
             "affects more than 50 users' or 'revisit in Phase 2 when CSDM data is mature'). "
             "The log is reviewed quarterly.",
     "questions": [
         "Who owns the Governance Triage Log — the ECS engagement manager, the customer process owner?",
         "How frequently will the log be reviewed with the steering committee?",
         "What criteria trigger a deferred item being promoted to active consideration?",
     ]},
],
"good_rows": [
    ["Every customization decision documented with business requirement, cost assessment, and approver", "Customizations added informally without documentation or approval record"],
    ["OOTB demonstration precedes every customization discussion", "Customization requested before OOTB capability has been shown to the stakeholder"],
    ["Governance Triage Log maintained and reviewed quarterly", "Requirements not meeting customization criteria are simply dropped with no tracking"],
    ["Customization count tracked as an engagement health metric", "Customization volume not monitored — scope creep is invisible until the backlog is full"],
    ["Configuration distinguished from customization — each treated with appropriate governance", "All platform changes treated identically — no distinction between configuration and code modification"],
    ["Customization council reviews requests within a defined SLA", "Customization requests queue without a decision process — delay accumulates"],
],
"patterns": [
    {"label": "Pattern A — OOTB demonstration resolving 70% of customization requests",
     "body": "A federal agency entered Sprint 1 with 22 customization requests in the backlog. "
             "ECS ran a structured OOTB demonstration for each request: showing the stakeholder "
             "how the OOTB platform addressed their underlying requirement, even if the approach "
             "differed from the legacy system. After demonstrations, 15 of the 22 requests "
             "were withdrawn — the stakeholders concluded the OOTB approach was acceptable. "
             "The remaining 7 went to the Customization Council, of which 4 were approved "
             "and 3 were deferred to Phase 2."},
    {"label": "Pattern B — Governance Triage Log as a steering committee standing item",
     "body": "A technology company added the Governance Triage Log as a standing agenda item "
             "at every steering committee meeting. Each session reviewed new log entries, "
             "confirmed deferral reasoning, and checked whether any deferred items had "
             "reached their review trigger. This practice kept the log visible and prevented "
             "the common failure mode where deferred requirements are forgotten and resurface "
             "as escalations late in the engagement."},
    {"label": "Pattern C — Phase 2 clearing 80% of the triage log",
     "body": "A healthcare organization entered Phase 2 with 18 items in the Governance Triage "
             "Log. Reviewing the log at Phase 2 kickoff, they found that 14 of the 18 "
             "requirements had been addressed by Phase 1 OOTB capabilities that stakeholders "
             "had not yet seen demonstrated. Three more were addressed by a ServiceNow "
             "platform update that had released in the interim. One required a Phase 2 "
             "customization — reviewed and approved by the council."},
],
"workshop_para": (
    "This is not a standalone workshop — the Custom-vs-OOTB framework applies continuously "
    "across all workshops. In Sprint 0, we will establish the Customization Council, define the "
    "decision criteria, and initialize the Governance Triage Log. In each subsequent sprint, "
    "requirements that surface as potential customization requests will be processed through "
    "the framework before any development work begins."
),
"need_bullets": [
    "List of requirements your team has already identified as 'probably needing customization' — the council will review these first",
    "Named Customization Council members (typically: IT leadership, process owner, ECS engagement manager)",
    "Existing customization inventory from your current ServiceNow environment (if one exists)",
    "Any requirements derived from contractual or compliance obligations that might be non-negotiable",
],
"questions": [
    "Are there requirements you have already identified that you believe require customization?",
    "Who in your organization has authority to approve a customization decision?",
    "Do you have an existing ServiceNow environment with customizations that will carry forward?",
    "Are there business processes that you believe cannot change to accommodate OOTB — and why?",
    "What is your organization's history with software customization — has technical debt been a problem before?",
],
"xrefs": [
    ["18-Week OOTB-First Journey Overview Deck", "The engagement model that this framework supports — shared in the kickoff briefing", "02_Client/01_Engagement_Overview/"],
    ["Technical Debt Elimination Roadmap Decision Guide", "The forward-looking companion — how to address existing customization debt", "02_Client/04_Decision_Topic_Guides/"],
    ["Change Management Workshop Pre-Read", "Change governance model connects to customization council governance", "02_Client/05_Workshop_Pre-Reads/"],
],
},

# ═══════════════════════════════════════════════════════════════════════════════
# CLT-DT-14  Technical Debt Elimination Roadmap
# ═══════════════════════════════════════════════════════════════════════════════
{
"doc_id": "CLT-DT-14",
"filename": "Technical_Debt_Elimination_Roadmap_Decision_Guide_CLIENT.docx",
"short_name": "Technical Debt Elimination Roadmap",
"signal_subject": "your technical debt reduction approach",
"title": "Technical Debt Elimination\nRoadmap",
"subtitle": "A decision guide for sequencing the reduction of accumulated customization and configuration debt",
"audience": "IT Leadership, Project Sponsors, Platform Owners, Process Owners, Enterprise Architects",
"companion_to": "Custom vs. OOTB Decision Framework · 18-Week OOTB-First Journey Overview",
"how_to_use_paras": [
    "Technical debt in a ServiceNow environment accumulates in predictable ways: customizations "
    "built for requirements that have since changed, configurations tuned for a process that no "
    "longer operates that way, integrations built when no connector existed and never replaced "
    "when one became available. This debt is invisible until it becomes expensive — and it "
    "becomes expensive when upgrades are delayed, when new capabilities cannot be activated, "
    "or when the platform team is spending more time on maintenance than on new value.",
    "This engagement is organized around preventing new debt from accumulating. But most "
    "organizations also arrive with existing debt — a legacy of customizations, workarounds, "
    "and configurations that served their purpose at the time but now constrain the platform's "
    "ability to deliver AI value.",
    "This guide helps you think about that existing debt: how to classify it, how to sequence "
    "its elimination, and how to govern future requests to prevent the cycle from repeating. "
    "It pairs with the Custom-vs-OOTB Decision Framework, which governs new requests. "
    "Together, the two guides define a complete technical debt management posture.",
],
"why_matters": [
    {"h2": "Technical debt blocks AI realization",
     "body": "ServiceNow's AI capabilities — Predictive Intelligence, Now Assist, Virtual Agent "
             "with generative answers — require a clean, OOTB-aligned data and process foundation "
             "to deliver value. Customizations that modify the data model create fields that AI "
             "capabilities do not know about. Custom workflows that bypass OOTB processes create "
             "data gaps that AI cannot bridge. The most direct path to AI realization is reducing "
             "the customization surface that sits between your data and the AI layer."},
    {"h2": "Upgrade velocity is inversely proportional to customization volume",
     "body": "Every customization adds testing scope to every ServiceNow upgrade. Organizations "
             "with high customization volumes upgrade less frequently — falling behind on platform "
             "capabilities, security patches, and the AI features that require current releases. "
             "Reducing the customization count is not just a technical improvement; it is a "
             "strategic investment in staying current with a platform that releases three times "
             "per year."},
    {"h2": "Debt elimination creates capacity for new value delivery",
     "body": "Platform teams that spend 70% of their capacity maintaining customizations have "
             "30% available for new capabilities. Teams that reduce their customization "
             "maintenance burden to 30% of capacity have 70% available for value delivery. "
             "The ROI calculation for debt elimination is straightforward — the question is "
             "the sequencing: which debt to eliminate first, and in what phases."},
],
"signals": [
    {"h2": "Upgrade testing takes more than 4 weeks",
     "body": "If your ServiceNow upgrade testing cycle routinely exceeds four weeks, the "
             "customization volume has reached a level that makes staying current with the "
             "platform difficult. Four weeks of testing per upgrade, three upgrades per year, "
             "means 12 weeks — 25% of your team's annual capacity — consumed by upgrade "
             "testing alone."},
    {"h2": "New platform capabilities cannot be activated without code changes",
     "body": "When a new ServiceNow capability requires modifications to existing customizations "
             "before it can be activated, that is a direct cost of technical debt. The more "
             "customizations that block new capabilities, the more each platform release "
             "requires remediation work before the organization can benefit from it."},
    {"h2": "Customization documentation is sparse or missing",
     "body": "Customizations without documentation are a succession risk: when the person "
             "who built them leaves, the organization loses the ability to maintain them. "
             "Undocumented customizations are also harder to evaluate for elimination — "
             "nobody knows what removing them would break."},
],
"decisions": [
    {"label": "How to classify existing technical debt by elimination priority",
     "body": "Not all debt is equally urgent to eliminate. A classification framework for "
             "existing customizations: Tier 1 — blocks AI capabilities or upgrade testing "
             "(eliminate in Phase 1 or Phase 2), Tier 2 — adds maintenance burden but does "
             "not block new capabilities (eliminate on natural refresh cycle), Tier 3 — "
             "low impact, low maintenance cost (document and monitor, do not prioritize "
             "for elimination unless capacity allows).",
     "questions": [
         "Do you have an inventory of your current ServiceNow customizations?",
         "Which customizations have been identified as blocking upgrades or new capabilities?",
         "Are there customizations that no longer serve their original purpose — requirements that have changed?",
     ],
     "landing": "Most organizations find that 20–30% of their customizations are Tier 1 (block "
                "AI or upgrade capability), 40–50% are Tier 2 (maintenance burden only), and "
                "20–30% are Tier 3 (low impact). The Tier 1 inventory is the Phase 2 elimination roadmap."},
    {"label": "Parallel vs. sequential approach — eliminate while building, or after stabilizing?",
     "body": "Some debt elimination work can happen in parallel with the Phase 1 OOTB baseline "
             "build — replacing a custom integration with a certified connector, for example. "
             "Other debt elimination requires the new baseline to be stable first — replacing "
             "a custom workflow with an OOTB workflow that depends on the new category structure "
             "being in place. The workshop will identify which debt items can be eliminated "
             "in parallel and which are Phase 2.",
     "questions": [
         "Are there customizations that can be retired as soon as the OOTB replacement is configured — without waiting for go-live?",
         "Are there customizations whose replacement depends on Phase 1 process design decisions being final?",
     ]},
    {"label": "What governance prevents new debt from accumulating?",
     "body": "Debt elimination without a prevention mechanism produces a debt cycle: new "
             "customizations accumulate at the same rate that old ones are eliminated. "
             "The Custom-vs-OOTB Decision Framework and Customization Council established "
             "in Sprint 0 are the prevention mechanism. The debt elimination roadmap and "
             "the prevention governance need to be designed as a system.",
     "questions": [
         "Is the Customization Council operational — have members been named and the process defined?",
         "Is customization volume being tracked as a platform health metric?",
         "Is there a target customization count the organization is aiming for at the end of the engagement?",
     ]},
    {"label": "How will debt elimination progress be reported to leadership?",
     "body": "Technical debt elimination is a multi-phase effort. Leadership visibility into "
             "progress — specifically the reduction in customization count and the corresponding "
             "reduction in upgrade testing time — is what sustains organizational commitment "
             "to the effort across multiple phases.",
     "questions": [
         "Which leadership audience needs visibility into debt elimination progress?",
         "What metrics will demonstrate debt reduction value — customization count, upgrade test time, maintenance hours?",
         "How frequently should debt elimination progress be reported?",
     ]},
],
"good_rows": [
    ["Customization inventory exists with classification by elimination priority", "No customization inventory — debt volume is unknown"],
    ["Tier 1 (AI-blocking) customizations on a Phase 2 elimination roadmap", "AI-blocking customizations not prioritized — AI capability activation deferred indefinitely"],
    ["Upgrade testing time decreasing quarter-over-quarter as debt is eliminated", "Upgrade testing time constant or increasing — debt is accumulating faster than it is being eliminated"],
    ["Custom-vs-OOTB framework preventing new debt accumulation", "New customizations added at the same rate that old ones are eliminated — no net progress"],
    ["Debt elimination metrics in leadership reporting", "Debt elimination progress not tracked — leadership does not have visibility into the effort"],
    ["Documentation produced for every remaining customization", "Customizations running without documentation — succession and maintenance risk"],
],
"patterns": [
    {"label": "Pattern A — Customization inventory as Phase 1 deliverable",
     "body": "A federal agency made a complete customization inventory a Sprint 0 deliverable "
             "— completed before the Phase 1 build began. The inventory classified each of "
             "their 340 customizations by type, business owner, and elimination priority. "
             "Tier 1 analysis showed that 42 customizations were blocking specific AI "
             "capabilities. Those 42 became the Phase 2 elimination roadmap. By the end "
             "of Phase 2, the platform had eliminated all 42 Tier 1 items, reducing upgrade "
             "testing time from 6 weeks to 3 weeks per release."},
    {"label": "Pattern B — Parallel elimination of custom integrations",
     "body": "A technology company identified during integration prioritization that 6 of their "
             "custom integrations had certified connector equivalents. They configured the "
             "connectors in parallel with the Phase 1 build and retired the custom integrations "
             "at go-live — not in a separate phase. Eliminating 6 custom integrations at "
             "go-live rather than deferring them to Phase 2 reduced the Phase 2 backlog and "
             "provided immediate upgrade testing relief."},
    {"label": "Pattern C — Debt metric in quarterly business review",
     "body": "A healthcare organization added three metrics to their quarterly IT business "
             "review: total customization count, Tier 1 customization count, and upgrade "
             "testing duration. Over four quarters, total customization count dropped from "
             "290 to 210, Tier 1 count dropped from 38 to 12, and upgrade testing duration "
             "dropped from 5 weeks to 2.5 weeks. The metrics kept debt elimination on the "
             "leadership agenda and provided a clear narrative for the platform investment."},
],
"workshop_para": (
    "The debt elimination roadmap is built across two conversations: Sprint 0 (customization "
    "inventory and Tier 1 identification) and Phase 2 kickoff (sequenced elimination plan "
    "with sprint assignments). In Sprint 0, we will review your existing customization list, "
    "apply the three-tier classification, and identify the Tier 1 items that become the "
    "Phase 2 priority. The elimination work happens in Phase 2, after the OOTB baseline "
    "is stable and the replacement configurations are proven."
),
"need_bullets": [
    "Customization inventory from your current ServiceNow environment — update set history, custom tables, custom scripts",
    "Upgrade test plan from the last upgrade cycle (shows which customizations required remediation)",
    "List of ServiceNow capabilities your team has been unable to activate — these are Tier 1 debt candidates",
    "Business owner for each major customization area — they will need to validate elimination feasibility",
],
"questions": [
    "Do you have an inventory of your current ServiceNow customizations?",
    "Are there specific AI capabilities (Now Assist, Predictive Intelligence, Virtual Agent) that you have been unable to activate due to customization conflicts?",
    "How long does your current ServiceNow upgrade testing cycle take?",
    "Are there customizations that you already know should be retired but have not had capacity to address?",
    "What leadership audience needs to see technical debt elimination progress?",
],
"xrefs": [
    ["Custom vs. OOTB Decision Framework", "The companion guide — prevents new debt while this guide addresses existing debt", "02_Client/04_Decision_Topic_Guides/"],
    ["18-Week OOTB-First Journey Overview", "The engagement model that frames the debt elimination approach", "02_Client/01_Engagement_Overview/"],
    ["Now Assist/GenAI Workshop Pre-Read", "AI capability activation is the primary value driver for Tier 1 debt elimination", "02_Client/05_Workshop_Pre-Reads/"],
],
},

]  # end GUIDES

if __name__ == "__main__":
    print(f"\nBuilding {len(GUIDES)} Decision Topic Guides (batch 3: DT-10 to DT-14)...\n")
    for g in GUIDES:
        build_dtg(g)
    print(f"\n✅  Batch 3 complete.\n")
