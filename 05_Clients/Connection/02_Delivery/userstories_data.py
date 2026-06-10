# Connection user-story data. add(module, short, role, want, benefit, ac[list], points, priority, note)
MODMETA = {
 # module: dict(sheet, abbr, sprint, role)
 "Platform Foundation": dict(sheet="app",abbr="PF",sprint="Sprint 1",role="Solution Architect / Technical Consultant"),
 "CSDM": dict(sheet="app",abbr="CSDM",sprint="Sprint 1",role="Solution Architect"),
 "CMDB": dict(sheet="app",abbr="CMDB",sprint="Sprint 2",role="Solution Architect / Technical Consultant"),
 "Discovery": dict(sheet="app",abbr="DISC",sprint="Sprint 2",role="Technical Consultant"),
 "Incident": dict(sheet="app",abbr="INC",sprint="Sprint 3",role="Process Consultant / Technical Consultant"),
 "Major Incident": dict(sheet="app",abbr="MIM",sprint="Sprint 3",role="Process Consultant"),
 "Problem": dict(sheet="app",abbr="PRB",sprint="Sprint 3",role="Process Consultant"),
 "Change": dict(sheet="app",abbr="CHG",sprint="Sprint 4",role="Process Consultant / Technical Consultant"),
 "Service Catalog": dict(sheet="app",abbr="SCR",sprint="Sprint 4",role="Process Consultant / Technical Consultant"),
 "Knowledge": dict(sheet="app",abbr="KM",sprint="Sprint 5",role="Process Consultant"),
 "Employee Center": dict(sheet="app",abbr="EC",sprint="Sprint 5",role="Process Consultant / Technical Consultant"),
 "Virtual Agent": dict(sheet="app",abbr="VA",sprint="Sprint 5",role="Technical Consultant"),
 "Predictive Intelligence": dict(sheet="app",abbr="PI",sprint="Sprint 5",role="Solution Architect"),
 "HAM": dict(sheet="app",abbr="HAM",sprint="Sprint 6",role="Solution Architect / Technical Consultant"),
 "Performance Analytics": dict(sheet="app",abbr="PA",sprint="Sprint 6",role="Solution Architect"),
 "Integrations": dict(sheet="int",abbr="INT",sprint="Sprint 3",role="Solution Architect / Technical Consultant"),
 "Service Graph Connectors": dict(sheet="int",abbr="SGC",sprint="Sprint 4",role="Solution Architect / Technical Consultant"),
 "Vonage CTI & Interactions": dict(sheet="int",abbr="CTI",sprint="Sprint 4",role="Solution Architect / Technical Consultant"),
}
STORIES=[]
def add(module,short,role,want,benefit,ac,points=3,priority="3 - Moderate",note="OOTB-first: configure within the Rule of Three; any delta routes to the Customization Council."):
    STORIES.append(dict(module=module,short=short,role=role,want=want,benefit=benefit,ac=ac,points=points,priority=priority,note=note))

# ---------------- Platform Foundation ----------------
m="Platform Foundation"
add(m,"Configure sub-production and production instances","platform administrator","sub-production and production instances stood up with a naming standard and test-data approach","environments are governed, consistent, and ready for build and a clean cutover",
 ["Given the dedicated instances are provisioned, When naming standards are applied, Then sub-prod and prod follow the agreed naming convention with ECS admin access.",
  "Given the move off domain separation, When the instances are configured, Then no domain-separation artifacts are carried into the new instances.",
  "Given a test-data approach is agreed, When build begins, Then sub-prod holds representative Connection data (not Lorem ipsum) for demos."],5,"1 - Critical")
add(m,"Configure AD/LDAP user import and ongoing sync","platform administrator","users imported from Active Directory via an OOTB scheduled import with ongoing sync","user records stay current without manual maintenance",
 ["Given AD/LDAP connectivity, When the OOTB scheduled import runs, Then in-scope users are created/updated with required attributes.",
  "Given the sync schedule, When a user is disabled in AD, Then the ServiceNow record reflects the change on the next run.",
  "Given coalesce rules, When the import runs twice, Then no duplicate user records are created."],3,"1 - Critical")
add(m,"Load the OOTB location hierarchy","platform administrator","the location hierarchy (site, building, floor) loaded using OOTB structures","assignment, routing, and asset placement resolve to correct locations",
 ["Given the location source data, When loaded, Then the site/building/floor hierarchy matches the agreed structure.",
  "Given a user with a location, When records are created, Then the location reference resolves correctly.",
  "Given OOTB location tables, When loaded, Then no custom location tables are introduced."],3)
add(m,"Configure groups and roles at go-live","platform administrator","OOTB roles and assignment groups configured with least-privilege membership","day-one access is correct and upgrade-safe",
 ["Given the agreed group/role model, When configured, Then OOTB roles (itil, admin, catalog_admin, asset, approver_user) are assigned via group membership.",
  "Given least privilege, When a member is added, Then they receive only the roles their group grants.",
  "Given role review, When audited, Then no custom roles exist without a documented business need."],3,"2 - High")
add(m,"Configure business hour schedules and holiday calendars","platform administrator","OOTB business-hour schedules and holiday calendars per in-scope process area","SLAs and escalations compute against correct working time",
 ["Given the agreed schedules, When configured, Then each process area references the correct OOTB schedule.",
  "Given a holiday, When an SLA spans it, Then elapsed time excludes non-working hours.",
  "Given OOTB schedules, When built, Then no scripted time calculations are introduced."],2)
add(m,"Configure outbound and inbound email","platform administrator","OOTB outbound SMTP relay and inbound mailboxes/actions configured","notifications send and inbound email creates/updates records",
 ["Given SMTP relay details, When configured, Then test notifications deliver to recipients.",
  "Given an inbound mailbox, When an email arrives, Then the OOTB inbound action creates/updates the correct record.",
  "Given email config, When reviewed, Then no custom mail scripts beyond OOTB inbound actions are used."],3)
add(m,"Deploy and configure the MID Server(s)","platform administrator","MID Server(s) deployed with credentials and network paths verified","Discovery and integrations can reach in-scope targets",
 ["Given MID Server host(s), When installed, Then they show Up and validated in ServiceNow.",
  "Given credentials in the vault, When a test probe runs, Then it connects without hard-coded credentials.",
  "Given placement, When reviewed, Then MID count/placement covers all in-scope subnets and integrations."],3,"2 - High")
add(m,"Establish platform health baseline KPIs","platform administrator","baseline platform-health KPIs configured and tracked","platform health is visible from go-live",
 ["Given the agreed KPIs, When configured, Then a baseline health view is available to the platform team.",
  "Given OOTB instance scan / health, When run, Then results are captured as the Phase 1 baseline.",
  "Given the baseline, When Hypercare begins, Then health is trended against it."],2)

# ---------------- CSDM ----------------
m="CSDM"
add(m,"Set CSDM adoption scope to the foundation tier for Phase 1","solution architect","CSDM adoption scoped to the foundation/design tiers appropriate for Phase 1","we build a healthy, right-sized service model without over-engineering",
 ["Given the CSDM workshop decision, When scope is set, Then Foundation and Design domains are in scope and deeper tiers are deferred with rationale.",
  "Given CSDM 5.0, When applied, Then OOTB CSDM tables are used with no custom service tables.",
  "Given the scope, When documented, Then it is recorded in the Architecture & CSDM Alignment document."],5,"1 - Critical")
add(m,"Load the Business Application inventory","solution architect","the Business Application inventory loaded into OOTB CSDM tables","services have an accurate top-level anchor for mapping",
 ["Given the agreed inventory, When loaded, Then Business Application records exist with owners.",
  "Given coalesce keys, When loaded twice, Then no duplicates are created.",
  "Given OOTB tables, When loaded, Then cmdb_ci_business_app is used without extension."],3,"2 - High")
add(m,"Structure the service taxonomy mapped to OOTB CSDM tables","solution architect","a service taxonomy (Business/Application/Technical service) mapped to OOTB CSDM tables","services are classified consistently for maps and reporting",
 ["Given the taxonomy decision, When configured, Then the hierarchy maps Business Application to Application Service to Technical Service via OOTB tables.",
  "Given a sample service, When classified, Then it resolves cleanly through the hierarchy.",
  "Given the taxonomy, When reviewed, Then it requires no custom classification fields."],5,"2 - High")
add(m,"Assign Application Service ownership","solution architect","Application Service owners, managers, and support groups assigned via OOTB fields","accountability for each service is explicit and operational",
 ["Given the ownership model, When assigned, Then each in-scope Application Service has owner, manager, and support group populated.",
  "Given an unowned service, When validated, Then it is flagged before sign-off.",
  "Given OOTB service fields, When used, Then no custom ownership fields are added."],3)
add(m,"Model service relationships to the agreed depth","solution architect","service relationships modeled using OOTB relationship types to the agreed depth","service maps are accurate without unbounded sprawl",
 ["Given the depth decision, When relationships are built, Then OOTB relationship types are used to the agreed number of tiers.",
  "Given a sample service, When mapped, Then upstream/downstream dependencies render correctly.",
  "Given the model, When reviewed, Then no custom relationship types are introduced."],3)
add(m,"Align CSDM with CMDB to create accurate service maps","solution architect","CSDM service definitions aligned to CMDB CIs to produce accurate service maps","change impact and incident context are trustworthy",
 ["Given CMDB CIs, When linked to services, Then service maps render with correct CI membership.",
  "Given a CI change, When impact is assessed, Then dependent services are identified.",
  "Given alignment, When validated, Then no orphaned services or CIs remain in scope."],5,"2 - High")
add(m,"Link CSDM services to the Service Catalog","solution architect","CSDM services connected to catalog items where applicable","requests carry service context for routing and reporting",
 ["Given in-scope catalog items, When associated to services, Then the service reference is populated.",
  "Given a request, When created, Then the related service is visible.",
  "Given the link, When reviewed, Then it uses OOTB service references."],2)
add(m,"Enable CSDM service maps for Change impact assessment","solution architect","CSDM service maps usable in Change for impact assessment","CAB sees affected services and CIs for each change",
 ["Given a change tied to a CI, When assessed, Then affected services display from the service map.",
  "Given a high-impact service, When a change targets it, Then risk reflects the impact.",
  "Given the integration, When validated, Then it uses OOTB change-CMDB relationships."],3)

# ---------------- CMDB ----------------
m="CMDB"
add(m,"Define in-scope CI classes for go-live","CMDB manager","the in-scope CI classes defined in OOTB CMDB Studio with deferred classes documented","the CMDB is populated to a useful, bounded scope at go-live",
 ["Given the class decision, When configured, Then in-scope CI classes exist with mandatory attributes defined in CMDB Studio.",
  "Given deferred classes, When documented, Then they are recorded with rationale for a later phase.",
  "Given OOTB classes, When used, Then no custom CI tables are created without Council approval."],3,"1 - Critical")
add(m,"Set the CMDB scope boundary","CMDB manager","the CMDB scope boundary defined for systems and networks","Discovery and connectors populate only in-scope CIs",
 ["Given the boundary decision, When applied, Then in-scope systems/networks are documented and out-of-scope excluded.",
  "Given a discovered out-of-scope CI, When ingested, Then it is filtered or flagged per the boundary.",
  "Given the boundary, When reviewed, Then it aligns with the Architecture & CSDM Alignment document."],3,"2 - High")
add(m,"Configure CI relationship types and maintenance","CMDB manager","OOTB CI relationship types configured with a maintenance approach","service maps and impact analysis stay accurate over time",
 ["Given the relationship decision, When configured, Then OOTB types (Runs on, Depends on, Hosted on) are used.",
  "Given automated sources, When data loads, Then relationships are maintained by Discovery/SGC, not manual edits.",
  "Given the model, When reviewed, Then no custom relationship types exist without business need."],3)
add(m,"Set CMDB health targets","CMDB manager","CMDB Health thresholds set for completeness, compliance, and correctness","CMDB quality is measurable and sufficient for AI ROI and risk scoring",
 ["Given the target decision, When configured, Then OOTB CMDB Health metrics use the agreed thresholds.",
  "Given the first data load, When scored, Then a health baseline is captured.",
  "Given thresholds, When breached, Then the dashboard surfaces the gap."],3,"2 - High")
add(m,"Define the source of record per CI class","CMDB manager","an authoritative source of record set per CI class (Discovery, connector, or manual)","CI data conflicts resolve predictably",
 ["Given the source decision, When configured, Then IRE rules name the authoritative source per class.",
  "Given overlapping sources, When data loads, Then the authoritative source wins per the rules.",
  "Given the mapping, When documented, Then it is recorded for operations."],3,"2 - High")
add(m,"Configure CI lifecycle states and retired-CI management","CMDB manager","OOTB CI lifecycle states configured with a retired-CI process","stale and retired CIs are managed, not deleted ad hoc",
 ["Given the lifecycle decision, When configured, Then OOTB states (Installed, In Maintenance, Retired) are used.",
  "Given a stale CI, When the policy runs, Then it is flagged inactive per the agreed window (deletion deferred to manual review).",
  "Given states, When reviewed, Then no custom lifecycle scripting is introduced."],2)
add(m,"Assign CI ownership","CMDB manager","CI ownership assigned via OOTB CI record fields with an operational definition","accountability for CIs is clear",
 ["Given the ownership model, When applied, Then in-scope CIs have owner/stewardship populated.",
  "Given an unowned CI, When validated, Then it is flagged before sign-off.",
  "Given OOTB fields, When used, Then no custom ownership fields are added."],2)
add(m,"Integrate CMDB with Change and Incident","CMDB manager","CMDB CI context available to Change and Incident","change risk scoring and incident context use CI data",
 ["Given a change tied to a CI, When created, Then affected CIs/services display.",
  "Given an incident on a CI, When created, Then related CI context is visible.",
  "Given the integration, When validated, Then it uses OOTB CMDB relationships."],3,"2 - High")

# ---------------- Discovery ----------------
m="Discovery"
add(m,"Plan MID Server count and placement for Discovery","Discovery engineer","MID Servers sized and placed for Discovery coverage","all in-scope subnets are reachable for Discovery",
 ["Given the subnet inventory, When MID placement is planned, Then every in-scope subnet has a reachable MID Server.",
  "Given a MID Server, When validated, Then it passes connectivity tests to sample targets.",
  "Given existing MID infrastructure, When reused, Then it is leveraged where it meets best practice."],3,"2 - High")
add(m,"Define Discovery IP ranges and subnets","Discovery engineer","Discovery IP ranges and subnets configured in OOTB Discovery Schedules","Discovery scans the right scope and nothing out of bounds",
 ["Given the in-scope ranges, When configured, Then Discovery Schedules target only those ranges.",
  "Given out-of-scope ranges (lab/test), When excluded, Then they are not scanned.",
  "Given schedules, When reviewed, Then they use OOTB schedule configuration."],2)
add(m,"Activate OOTB Discovery patterns for in-scope classes","Discovery engineer","OOTB Discovery patterns activated for in-scope CI classes","CIs are discovered without custom patterns",
 ["Given in-scope classes, When patterns are activated, Then OOTB patterns (Windows, Linux, VMware, network) populate them.",
  "Given a custom pattern need, When identified, Then it routes to the Customization Council.",
  "Given a test run, When executed, Then sample CIs populate with expected attributes."],3,"2 - High")
add(m,"Configure Discovery credentials in the vault","Discovery engineer","Discovery credentials stored in the OOTB Credential Vault","Discovery authenticates securely without hard-coded secrets",
 ["Given credential records, When stored, Then they reside in the OOTB Credential store.",
  "Given a probe, When it runs, Then it uses vaulted credentials only.",
  "Given access, When reviewed, Then least-privilege service accounts are used."],2,"2 - High")
add(m,"Set the Discovery schedule and maintenance windows","Discovery engineer","Discovery schedule frequency, timing, and maintenance-window exclusions configured","Discovery runs predictably without impacting operations",
 ["Given the cadence decision, When configured, Then schedules run at the agreed frequency/timing.",
  "Given maintenance windows, When set, Then Discovery excludes them.",
  "Given OOTB scheduling, When used, Then no custom scheduling logic is introduced."],2)
add(m,"Configure IRE reconciliation and duplicate handling","Discovery engineer","IRE identification and reconciliation rules configured to prevent duplicate CIs","CMDB stays clean across multiple data sources",
 ["Given IRE rules, When data loads from multiple sources, Then CIs are matched and reconciled, not duplicated.",
  "Given a potential duplicate, When ingested, Then IRE identifies the existing CI.",
  "Given the rules, When reviewed, Then they use OOTB IRE configuration."],3,"2 - High")
add(m,"Decide and configure cloud Discovery (if in scope)","Discovery engineer","cloud Discovery activated for agreed providers (or formally deferred)","cloud CIs are captured if required for Phase 1",
 ["Given the cloud decision, When made, Then cloud Discovery is activated for named providers or deferred with rationale.",
  "Given activation, When configured, Then OOTB cloud Discovery uses service-account credentials.",
  "Given a test run, When executed, Then sample cloud CIs populate."],2)
add(m,"Verify the CMDB after the first Discovery run","Discovery engineer","a CMDB verification process executed after the first Discovery run","Discovery results are trusted before downstream use",
 ["Given the first full run, When complete, Then a sample of CIs is validated against source-of-truth.",
  "Given verification, When gaps are found, Then they are logged and remediated before sign-off.",
  "Given results, When validated, Then CMDB Health meets the agreed baseline."],3)

# ---------------- Incident ----------------
m="Incident"
add(m,"Configure incident priority via OOTB Impact x Urgency","service desk manager","incident priority driven by the OOTB 5-level Impact x Urgency matrix","priority is consistent and requires no scripting",
 ["Given the priority decision, When configured, Then the OOTB Impact x Urgency matrix yields the 5 priority levels.",
  "Given an incident, When impact and urgency are set, Then priority calculates automatically.",
  "Given the matrix, When reviewed, Then no custom priority script is used."],3,"1 - Critical")
add(m,"Configure incident categories and subcategories","service desk manager","incident category/subcategory taxonomy configured","incidents are classified for routing and reporting",
 ["Given the taxonomy decision, When configured, Then agreed categories/subcategories exist as OOTB choices.",
  "Given a new incident, When categorized, Then the subcategory list filters to the category.",
  "Given the taxonomy, When reviewed, Then it stays a routing taxonomy (service context lives on the CI)."],2)
add(m,"Adopt the OOTB incident lifecycle states","service desk manager","the OOTB incident lifecycle states adopted","the process is upgrade-safe with no custom states",
 ["Given the lifecycle decision, When configured, Then OOTB states are used with On Hold reasons.",
  "Given a custom-state request, When raised, Then it routes to the Customization Council.",
  "Given the lifecycle, When validated, Then state transitions follow OOTB rules."],3,"2 - High")
add(m,"Activate in-scope incident intake channels","service desk manager","the agreed intake channels activated (Employee Center, email, Virtual Agent, phone/CTI)","users can raise incidents through approved channels at go-live",
 ["Given the channel decision, When activated, Then each agreed channel creates incidents correctly.",
  "Given a phone call, When handled, Then an Interaction can spawn an incident (see CTI stories).",
  "Given channels, When reviewed, Then they use OOTB intake."],3,"2 - High")
add(m,"Configure incident SLAs by priority","service desk manager","response and resolution SLA targets configured by priority with schedules","commitments are tracked and breaches are visible",
 ["Given the SLA decision, When configured, Then OOTB SLA definitions set response/resolution targets per priority.",
  "Given a business schedule, When applied, Then SLA elapsed time respects working hours.",
  "Given an at-risk SLA, When approaching breach, Then it surfaces on the workspace/dashboards."],3,"2 - High")
add(m,"Configure incident routing/assignment","service desk manager","incidents routed to the correct support group via OOTB assignment rules","tickets reach the right team without manual triage",
 ["Given assignment rules, When an incident is categorized, Then it routes to the correct group.",
  "Given an unmatched incident, When created, Then it lands in a defined catch-all group.",
  "Given rules, When reviewed, Then they use OOTB assignment (Decision Tables/conditions), not custom code."],3)
add(m,"Configure Major Incident escalation from Incident","service desk manager","the criteria and action to escalate an incident to a Major Incident","major incidents are declared consistently",
 ["Given the escalation decision, When configured, Then qualifying incidents can be promoted to Major Incident.",
  "Given a P1 meeting criteria, When promoted, Then the MIM process engages (see MIM stories).",
  "Given promotion, When validated, Then it uses the OOTB MIM trigger."],2,"2 - High")
add(m,"Configure incident notifications","service desk manager","notifications configured across the incident lifecycle","stakeholders are informed at the right moments",
 ["Given the notification decision, When configured, Then OOTB notifications fire on the agreed events.",
  "Given an assignment, When made, Then the assignee is notified.",
  "Given notifications, When reviewed, Then OOTB notification records are used."],2)
add(m,"Connect Predictive Intelligence and Knowledge to Incident","service desk manager","PI categorization/assignment and KB suggestions surfaced in Incident","agents resolve faster with AI and knowledge support",
 ["Given PI enabled, When an incident is created, Then category/assignment predictions surface for agent review.",
  "Given KB integration, When working an incident, Then relevant articles are suggested.",
  "Given the integration, When validated, Then it uses OOTB PI and KB features (see PI/KM stories)."],3)

# ---------------- Major Incident ----------------
m="Major Incident"
add(m,"Define major incident criteria","major incident coordinator","major-incident criteria defined and frozen before plugin activation","major incidents are declared consistently without MIM fatigue",
 ["Given the criteria decision, When configured, Then OOTB MIM criteria (priority/impact/EM/manual) reflect the agreement.",
  "Given an incident meeting criteria, When evaluated, Then it qualifies for major-incident declaration.",
  "Given the criteria, When frozen, Then changes route to governance."],3,"1 - Critical")
add(m,"Configure MIM team roles","major incident coordinator","OOTB MIM roles configured (coordinator, technical lead, comms lead, exec sponsor)","accountability in a major incident is clear",
 ["Given the role decision, When configured, Then OOTB MIM roles exist with named (or draft) holders.",
  "Given a major incident, When declared, Then the coordinator owns the record.",
  "Given roles, When reviewed, Then OOTB role structure is used."],2,"2 - High")
add(m,"Configure stakeholder communication templates","communications lead","stakeholder communication templates configured for major incidents","comms are timely, consistent, and approved",
 ["Given the comms decision, When configured, Then templates exist per communication type (subject/body/audience).",
  "Given a major incident, When comms are sent, Then a template populates the message.",
  "Given templates, When reviewed, Then OOTB notification/template features are used."],2)
add(m,"Configure major-incident SLAs","major incident coordinator","SLAs specific to major incidents configured","MIM response/restore times are tracked distinctly",
 ["Given the MIM SLA decision, When configured, Then OOTB SLAs track major-incident response/restore.",
  "Given a major incident, When active, Then the MIM SLA clock runs.",
  "Given SLAs, When validated, Then they use OOTB SLA definitions."],2)
add(m,"Configure the Post-Incident Review (PIR) process","major incident coordinator","the OOTB PIR workflow configured","every major incident drives learning and follow-up",
 ["Given the PIR decision, When configured, Then a PIR is generated/required after a major incident.",
  "Given a closed major incident, When PIR runs, Then actions are captured and tracked.",
  "Given PIR, When reviewed, Then it uses OOTB PIR capability."],2)
add(m,"Configure Event Management trigger to MIM (alignment note)","major incident coordinator","the EM-to-MIM promotion threshold aligned (EM is later-phase)","if/when EM is enabled, promotion is consistent",
 ["Given EM is out of Phase 1 scope, When documented, Then the EM-to-MIM threshold is recorded for a later phase.",
  "Given manual/priority criteria, When used now, Then MIM does not depend on EM in Phase 1.",
  "Given alignment, When validated, Then no EM customization is built in Phase 1."],1,"4 - Low")
add(m,"Decide war-room tooling integration (Teams/Zoom/Slack)","major incident coordinator","a decision on war-room tooling integration for major incidents","collaboration during a major incident is effective",
 ["Given the tooling decision, When made, Then either an OOTB collaboration integration is used or it is deferred with rationale.",
  "Given a custom integration request, When raised, Then it routes to the Customization Council.",
  "Given the decision, When documented, Then it is recorded in the Triage Log if a deviation."],2)

# ---------------- Problem ----------------
m="Problem"
add(m,"Adopt the OOTB problem lifecycle","problem manager","the OOTB problem lifecycle states adopted","the process is upgrade-safe with no custom states",
 ["Given the lifecycle decision, When configured, Then OOTB problem states and On Hold reasons are used.",
  "Given a custom-state request, When raised, Then it routes to the Customization Council.",
  "Given the lifecycle, When validated, Then transitions follow OOTB rules."],3,"2 - High")
add(m,"Align problem categories to the incident taxonomy","problem manager","problem categories aligned to the incident taxonomy","trends connect cleanly from incident to problem",
 ["Given the taxonomy decision, When configured, Then problem categories mirror the incident taxonomy.",
  "Given a problem from incidents, When categorized, Then categories are consistent.",
  "Given alignment, When reviewed, Then OOTB category choices are used."],2)
add(m,"Configure the Known Error Database (KEDB)","problem manager","the KEDB configured so known errors and workarounds are surfaced","agents resolve repeat issues faster",
 ["Given the KEDB decision, When configured, Then known errors/workarounds are captured on problem records.",
  "Given an incident matching a known error, When worked, Then the workaround is discoverable.",
  "Given KEDB, When reviewed, Then OOTB known-error capability is used."],3,"2 - High")
add(m,"Configure problem assignment and Problem Manager role","problem manager","problem assignment rules and the Problem Manager role configured","problems are owned and driven to root cause",
 ["Given the assignment decision, When configured, Then problems route by category/CI/support group.",
  "Given the Problem Manager role, When assigned, Then ownership is clear.",
  "Given rules, When reviewed, Then OOTB assignment is used."],2)
add(m,"Configure problem SLAs and KPIs","problem manager","SLA targets and KPIs for problem investigation configured","investigation progress is measurable",
 ["Given the SLA/KPI decision, When configured, Then time-to-root-cause and time-to-resolution are tracked.",
  "Given a problem, When active, Then the relevant SLA runs.",
  "Given KPIs, When reviewed, Then OOTB PA indicators support them."],2)
add(m,"Configure problem notifications","problem manager","notifications configured across the problem lifecycle","stakeholders stay informed",
 ["Given the notification decision, When configured, Then OOTB notifications fire on agreed events.",
  "Given a root cause found, When recorded, Then stakeholders are notified.",
  "Given notifications, When reviewed, Then OOTB records are used."],1)
add(m,"Link Problem to Change","problem manager","problems linked to change requests for permanent fixes","fixes are delivered through governed change",
 ["Given a problem needing a fix, When raised, Then a change can be created/linked from the problem.",
  "Given the linked change, When progressed, Then the problem reflects fix status.",
  "Given the link, When validated, Then OOTB problem-change relationships are used."],2)
add(m,"Connect Predictive Intelligence to Problem","problem manager","PI similarity/clustering surfaced to support problem identification","recurring incident patterns become problems sooner",
 ["Given PI enabled, When incidents cluster, Then candidate problems are surfaced for review.",
  "Given a cluster, When reviewed, Then a problem can be created from it.",
  "Given the integration, When validated, Then OOTB PI features are used (see PI stories)."],2)

# ---------------- Change ----------------
m="Change"
add(m,"Adopt the 3 OOTB change types","change manager","the OOTB change types (Normal, Standard, Emergency) adopted","change is governed with proven, upgrade-safe types",
 ["Given the type decision, When configured, Then Normal, Standard, and Emergency are active with their OOTB workflows.",
  "Given a change, When created, Then the type drives the correct approval path.",
  "Given the types, When reviewed, Then no custom change types are introduced."],3,"1 - Critical")
add(m,"Adopt the OOTB change lifecycle states","change manager","the OOTB change lifecycle states adopted","the process stays upgrade-safe",
 ["Given the lifecycle decision, When configured, Then OOTB change states are used.",
  "Given a custom-state request, When raised, Then it routes to the Customization Council.",
  "Given the lifecycle, When validated, Then transitions follow OOTB rules."],2,"2 - High")
add(m,"Configure CI-driven change risk scoring","change manager","change risk calculated using OOTB risk assessment with thresholds that trigger CAB","risk-appropriate changes get the right scrutiny",
 ["Given the risk decision, When configured, Then the OOTB risk questionnaire/conditions produce a risk score.",
  "Given a CI-tied change, When assessed, Then CMDB context informs the risk.",
  "Given thresholds, When exceeded, Then the change is routed to CAB."],5,"1 - Critical")
add(m,"Stand up the CAB Workbench","change manager","the OOTB CAB Workbench configured for the agreed CAB structure","CAB reviews are efficient and consistent",
 ["Given the CAB decision, When configured, Then the CAB Workbench reflects the meeting cadence and membership.",
  "Given non-standard changes, When scheduled, Then they appear on the CAB agenda.",
  "Given the workbench, When validated, Then OOTB CAB capability is used."],3,"2 - High")
add(m,"Configure the Standard Change Catalog","change manager","2-3 well-defined standard change templates configured with template approvers","low-risk repeatable changes are pre-approved and fast",
 ["Given the standard-change decision, When configured, Then the agreed templates exist in the Standard Change Catalog.",
  "Given a standard change, When raised from a template, Then it follows the pre-approved path.",
  "Given templates, When created, Then template approval is governed."],3,"2 - High")
add(m,"Configure change approvals and sequence","change manager","change approval policies and sequence configured","the right approvers act in the right order",
 ["Given the approval decision, When configured, Then OOTB Approval Definitions route by type/risk.",
  "Given a change, When submitted, Then approvals occur in the agreed sequence.",
  "Given approvals, When reviewed, Then OOTB approval engine is used (no custom code)."],3)
add(m,"Configure change conflict detection and blackout windows","change manager","OOTB conflict detection and blackout/maintenance windows configured","conflicting or risky-timed changes are caught",
 ["Given the schedule decision, When configured, Then OOTB conflict detection flags overlapping changes on shared CIs.",
  "Given a blackout window, When a change targets it, Then it is flagged.",
  "Given the config, When validated, Then OOTB change schedule features are used."],3)
add(m,"Configure change notifications","change manager","notifications configured across the change lifecycle","stakeholders are informed at approvals and implementation",
 ["Given the notification decision, When configured, Then OOTB notifications fire on agreed events.",
  "Given an approval request, When raised, Then approvers are notified.",
  "Given notifications, When reviewed, Then OOTB records are used."],2)
add(m,"Connect Predictive Intelligence/Now Assist to Change (alignment)","change manager","the PI/Now Assist hooks for Change documented (Now Assist later-phase)","Change is ready for AI assistance without Phase 1 customization",
 ["Given Now Assist is later-phase, When documented, Then the Change hooks are recorded for a future phase.",
  "Given PI in Phase 1, When applicable, Then only OOTB PI features are used.",
  "Given alignment, When validated, Then no AI customization is built in Phase 1."],1,"4 - Low")

# ---------------- Service Catalog ----------------
m="Service Catalog"
add(m,"Define and bound the Phase 1 catalog item list","catalog manager","the top 10-15 highest-impact items plus 2-3 generic catch-all items defined","value is delivered without unbounded catalog scope",
 ["Given the item decision, When configured, Then the agreed 10-15 items plus 2-3 catch-all items are in scope.",
  "Given prioritization, When applied, Then items are ranked by impact and bounded for Phase 1.",
  "Given existing items, When reused, Then only those without technical debt are leveraged."],5,"1 - Critical")
add(m,"Design catalog variables and variable sets","catalog manager","variables designed using shared variable sets where appropriate","catalog items are consistent and maintainable",
 ["Given the variable decision, When configured, Then shared variable sets are used for common fields.",
  "Given an item, When built, Then item-level variables are used only where unique.",
  "Given the design, When reviewed, Then no scripted client logic beyond UI Policies is used."],3,"2 - High")
add(m,"Configure the catalog approval model","catalog manager","the approval model configured (who approves what; auto vs manual)","requests are approved appropriately and quickly",
 ["Given the approval decision, When configured, Then OOTB approval rules trigger by item type or cost threshold.",
  "Given a low-cost item, When ordered, Then it follows the agreed auto/manual path.",
  "Given approvals, When reviewed, Then OOTB approval engine is used."],3,"2 - High")
add(m,"Structure catalog fulfillment tasks","catalog manager","fulfillment tasks structured for common request types","fulfillment teams have clear, repeatable work",
 ["Given the fulfillment decision, When configured, Then OOTB fulfillment task templates exist for common items.",
  "Given a request, When approved, Then fulfillment tasks generate to the right groups.",
  "Given the model, When reviewed, Then OOTB workflow/flow is used."],3)
add(m,"Configure catalog request SLAs","catalog manager","SLAs configured for catalog requests","request commitments are defined and tracked",
 ["Given the SLA decision, When configured, Then OOTB SLAs track request fulfillment by item/type.",
  "Given a request, When active, Then the SLA clock runs against the schedule.",
  "Given SLAs, When reviewed, Then OOTB SLA definitions are used."],2)
add(m,"Configure catalog categorization for AI and reporting","catalog manager","catalog taxonomy configured to support AI and reporting","requests classify cleanly for analytics and automation",
 ["Given the taxonomy decision, When configured, Then categories support reporting and future AI.",
  "Given an item, When categorized, Then it resolves to the agreed taxonomy.",
  "Given the taxonomy, When reviewed, Then OOTB category structures are used."],2)
add(m,"Define the catalog post-launch governance model","catalog manager","a governance model for catalog item retirement and additions","the catalog stays healthy after go-live",
 ["Given the governance decision, When documented, Then an item review/retirement process is defined.",
  "Given a new-item request post-launch, When raised, Then it follows the governance path.",
  "Given the model, When handed over, Then it is captured in the Admin Guide."],2)
add(m,"Define catalog performance measurement (30/60/90)","catalog manager","catalog performance measures defined for 30/60/90 days","success is measurable after launch",
 ["Given the measurement decision, When configured, Then PA indicators track request volume, cycle time, and satisfaction.",
  "Given the 30/60/90 cadence, When reviewed, Then results are reported.",
  "Given measures, When reviewed, Then OOTB PA is used."],2)

# ---------------- Knowledge ----------------
m="Knowledge"
add(m,"Configure knowledge bases and access model","knowledge manager","the agreed knowledge bases created with an access model per KB","content is organized and access-appropriate",
 ["Given the KB decision, When configured, Then the agreed KBs exist with OOTB access controls (public/authenticated/role-based).",
  "Given a user, When they browse, Then they see only KBs they are entitled to.",
  "Given KBs, When reviewed, Then OOTB KB records are used."],3,"2 - High")
add(m,"Configure the article lifecycle workflow","knowledge manager","the article lifecycle configured (OOTB review workflow or direct publish per KB)","articles are governed appropriately",
 ["Given the lifecycle decision, When configured, Then the agreed workflow (1-stage/2-stage or direct) is active per KB.",
  "Given an article, When submitted, Then it follows the configured workflow.",
  "Given the workflow, When reviewed, Then OOTB article workflow is used."],2)
add(m,"Define knowledge ownership and authorship","knowledge manager","KB Owner/Manager roles and an authorship model assigned","accountability for content is clear",
 ["Given the ownership decision, When configured, Then each KB has Owner and Manager assigned via OOTB roles.",
  "Given a new article, When created, Then the author/owner is captured.",
  "Given roles, When reviewed, Then OOTB KB roles are used."],2)
add(m,"Activate article templates","knowledge manager","the agreed article templates activated","articles are consistent and easy to author",
 ["Given the template decision, When configured, Then templates (How-To, FAQ, Policy, Resolution) are available.",
  "Given an author, When creating an article, Then they can select a template.",
  "Given templates, When reviewed, Then OOTB template capability is used."],1)
add(m,"Configure article feedback capture","knowledge manager","article feedback (useful/not, comments, flagging) enabled and actioned","content quality improves from user input",
 ["Given the feedback decision, When configured, Then OOTB feedback is enabled on articles.",
  "Given negative feedback, When submitted, Then it flags the article for review.",
  "Given feedback, When reviewed, Then OOTB feedback features are used."],1)
add(m,"Integrate Knowledge with Virtual Agent and Employee Center search","knowledge manager","knowledge surfaced through VA and Employee Center / AI Search","users self-serve and deflect tickets",
 ["Given the integration decision, When configured, Then articles surface in EC search and VA responses.",
  "Given a user query, When searched, Then relevant articles are returned.",
  "Given integration, When validated, Then OOTB AI Search/VA-KB features are used."],3,"2 - High")
add(m,"Define knowledge governance KPIs and review","knowledge manager","KM governance KPIs and a monthly review owner defined","knowledge stays current and valuable",
 ["Given the governance decision, When configured, Then KPIs (usage, freshness, feedback) are tracked.",
  "Given the monthly review, When scheduled, Then an owner is named.",
  "Given KPIs, When reviewed, Then OOTB PA/KM reporting is used."],2)
add(m,"Plan and execute initial knowledge content seeding","knowledge manager","baseline content ported from the legacy platform for go-live","users have useful content on day one",
 ["Given the seeding plan, When executed, Then the agreed baseline articles are ported and reviewed.",
  "Given ported articles, When validated, Then they meet the article standard before publish.",
  "Given seeding, When complete, Then KBs are populated for go-live."],3,"2 - High")

# ---------------- Employee Center ----------------
m="Employee Center"
add(m,"Configure Employee Center topic categories and owners","EC product owner","the launch topic categories configured with named owners","employees find services in a clear structure",
 ["Given the topic decision, When configured, Then the agreed categories (IT, HR, Facilities, Finance...) exist with owners.",
  "Given a category, When browsed, Then it surfaces the right content and items.",
  "Given topics, When reviewed, Then OOTB taxonomy is used."],3,"2 - High")
add(m,"Apply Connection branding via the OOTB theme engine","EC product owner","Connection branding/theming applied within OOTB limits","the portal feels like Connection without custom UI",
 ["Given the branding decision, When applied, Then OOTB theming (logo, colors, layout) reflects Connection branding.",
  "Given a full-custom-UI request, When raised, Then it routes to the Customization Council.",
  "Given branding, When reviewed, Then the OOTB theme engine is used (no custom portal UI)."],3,"2 - High")
add(m,"Curate the home page and promoted items","EC product owner","home page promoted items and banners curated","employees see the most relevant services first",
 ["Given the curation decision, When configured, Then promoted items/banners reflect the agreed priorities.",
  "Given a launch, When viewed, Then the home page surfaces top services.",
  "Given curation, When reviewed, Then OOTB promoted-content features are used."],2)
add(m,"Configure Employee Center search","EC product owner","search configured with synonyms, promoted results, and relevance tuning","users find answers quickly",
 ["Given the search decision, When configured, Then synonyms and promoted results are set.",
  "Given a query, When searched, Then relevant results (KB, catalog) return.",
  "Given search, When reviewed, Then OOTB search config (no custom indexing) is used."],3,"2 - High")
add(m,"Surface knowledge in Employee Center","EC product owner","in-scope knowledge surfaced through Employee Center","self-service deflects tickets",
 ["Given the content decision, When configured, Then the agreed KBs surface in EC.",
  "Given a topic, When browsed, Then related articles display.",
  "Given surfacing, When validated, Then OOTB KB-EC integration is used."],2)
add(m,"Define Employee Center migration from the existing portal","EC product owner","the migration approach from the existing intranet/portal defined","the transition is clean for users",
 ["Given the migration decision, When documented, Then in-scope content/links to migrate are listed.",
  "Given go-live, When cutover, Then the agreed redirect/migration plan is followed.",
  "Given migration, When validated, Then OOTB EC replaces the prior self-service path."],2)
add(m,"Integrate Virtual Agent into Employee Center","EC product owner","Virtual Agent embedded in Employee Center for the in-scope conversations","users get conversational self-service",
 ["Given the VA decision, When configured, Then the OOTB VA launcher is available in EC.",
  "Given a user, When they open VA, Then in-scope topics are available.",
  "Given integration, When validated, Then OOTB EC-VA integration is used (see VA stories)."],2)
add(m,"Define Employee Center adoption measurement","EC product owner","adoption metrics defined for Employee Center","success and deflection are measurable",
 ["Given the metric decision, When configured, Then PA tracks visits, self-service rate, and deflection.",
  "Given launch, When reviewed, Then adoption is reported.",
  "Given metrics, When reviewed, Then OOTB PA is used."],2)

# ---------------- Virtual Agent ----------------
m="Virtual Agent"
add(m,"Activate the 5 baseline Virtual Agent topics","VA administrator","the 5 baseline VA topics activated and configured","users get conversational self-service at go-live",
 ["Given the topic decision, When configured, Then 5 baseline OOTB topics (e.g., incident, catalog, RITM status, KB search, password reset) are active.",
  "Given a user, When they invoke a topic, Then the conversation completes successfully.",
  "Given topics, When reviewed, Then OOTB VA topics are used (no NLU model rebuild)."],3,"2 - High")
add(m,"Configure NLU vs menu-driven matching","VA administrator","the matching approach configured (OOTB NLU intent matching or menu-driven)","users are understood and routed correctly",
 ["Given the matching decision, When configured, Then the agreed approach is active.",
  "Given a user utterance, When matched, Then the correct topic launches.",
  "Given utterances, When added, Then custom utterances extend OOTB NLU without a model rebuild."],3)
add(m,"Configure VA live-agent escalation","VA administrator","escalation from VA to a live agent configured to the right teams","users reach a human when self-service cannot help",
 ["Given the escalation decision, When configured, Then OOTB live-agent handoff routes to the agreed teams.",
  "Given a failed self-service, When escalated, Then the conversation/context transfers.",
  "Given escalation, When validated, Then OOTB Connect/Advanced Work Assignment is used."],3,"2 - High")
add(m,"Activate VA channels for go-live","VA administrator","the agreed VA channels activated (Employee Center; others as scoped)","users access VA where they work",
 ["Given the channel decision, When configured, Then VA is active in the agreed channels.",
  "Given a channel, When used, Then VA responds correctly.",
  "Given channels, When reviewed, Then OOTB channel configuration is used."],2)
add(m,"Configure VA authentication","VA administrator","authentication within VA sessions configured","personalized, secure self-service is possible",
 ["Given the auth decision, When configured, Then authenticated VA sessions identify the user.",
  "Given an authenticated user, When they ask about their tickets, Then VA returns their records.",
  "Given auth, When validated, Then OOTB VA authentication is used."],2)
add(m,"Integrate VA with the Service Catalog","VA administrator","VA connected to the catalog for request fulfillment","users can order in-scope items conversationally",
 ["Given the integration decision, When configured, Then VA can submit agreed catalog requests.",
  "Given a user, When ordering via VA, Then a request is created correctly.",
  "Given integration, When validated, Then OOTB VA-catalog topics are used."],2)
add(m,"Document Now Assist enhancement for VA (later-phase)","VA administrator","the Now Assist enhancements for VA documented for a later phase","VA is ready for GenAI without Phase 1 customization",
 ["Given Now Assist is later-phase, When documented, Then the enhancement plan is recorded.",
  "Given Phase 1, When delivered, Then only OOTB VA is configured.",
  "Given alignment, When validated, Then no GenAI customization is built in Phase 1."],1,"4 - Low")
add(m,"Define VA performance measurement and governance","VA administrator","VA performance metrics and governance defined","VA effectiveness is measured and improved",
 ["Given the metric decision, When configured, Then PA tracks containment, escalation, and satisfaction.",
  "Given launch, When reviewed, Then VA performance is reported.",
  "Given governance, When defined, Then a review owner is named."],2)

# ---------------- Predictive Intelligence ----------------
m="Predictive Intelligence"
add(m,"Select and activate the PI use cases","platform owner","the agreed PI use cases activated for Phase 1","AI assists where data supports it, without over-reach",
 ["Given the use-case decision, When configured, Then OOTB PI solutions (e.g., categorization, assignment, similarity) are activated for the agreed scope.",
  "Given an out-of-scope use case, When requested, Then it is deferred with rationale.",
  "Given activation, When validated, Then only OOTB PI capabilities are used (no custom ML)."],3,"2 - High")
add(m,"Assess training data quality and volume","platform owner","training data quality and volume assessed before model training","models are trained on sufficient, clean data",
 ["Given the data assessment, When complete, Then volume/quality is documented per use case.",
  "Given insufficient data, When found, Then the use case is deferred or scoped down.",
  "Given filters, When applied, Then training data uses OOTB training filters."],3,"2 - High")
add(m,"Set PI confidence thresholds","platform owner","confidence thresholds set for auto-population vs agent review","predictions help without eroding trust",
 ["Given the threshold decision, When configured, Then high-confidence predictions auto-populate and lower-confidence ones surface for review.",
  "Given a prediction, When below threshold, Then the agent confirms.",
  "Given thresholds, When validated, Then OOTB PI configuration is used."],2)
add(m,"Configure similar-incident surfacing","platform owner","similar-incident matching configured and surfaced to agents","agents resolve faster using prior resolutions",
 ["Given the similarity decision, When configured, Then OOTB similarity surfaces related incidents/resolutions.",
  "Given an incident, When worked, Then similar incidents display.",
  "Given the config, When validated, Then OOTB PI similarity is used."],2)
add(m,"Decide and configure incident clustering","platform owner","incident clustering activated (or deferred) with a reviewer named","recurring patterns become problems sooner",
 ["Given the clustering decision, When made, Then clustering is activated with a named reviewer or deferred with rationale.",
  "Given a cluster alert, When raised, Then the reviewer triages it.",
  "Given the config, When validated, Then OOTB clustering is used."],2)
add(m,"Define PI model governance","platform owner","PI model ownership, training cadence, and monitoring defined","models stay accurate and accountable",
 ["Given the governance decision, When documented, Then owners, retrain cadence, and monitoring are defined.",
  "Given model drift, When detected, Then the retrain process triggers.",
  "Given governance, When handed over, Then it is captured in the Admin Guide."],2)

# ---------------- HAM ----------------
m="HAM"
add(m,"Configure asset classes and models for go-live","asset manager","the in-scope asset classes and models configured","hardware assets are tracked consistently",
 ["Given the class decision, When configured, Then OOTB asset classes/models reflect the in-scope hardware.",
  "Given an asset, When created, Then it maps to the correct class/model.",
  "Given the config, When reviewed, Then OOTB HAM tables are used."],3,"2 - High")
add(m,"Configure asset lifecycle states and transitions","asset manager","OOTB asset lifecycle states and valid transitions configured","asset status reflects reality through its life",
 ["Given the lifecycle decision, When configured, Then OOTB states and transitions are active.",
  "Given an asset, When it moves stages, Then only valid transitions are allowed.",
  "Given the config, When reviewed, Then no custom lifecycle scripting is added."],2)
add(m,"Configure stockrooms","asset manager","the agreed stockrooms configured with managers","asset inventory is organized and owned",
 ["Given the stockroom decision, When configured, Then the agreed stockrooms exist with managers.",
  "Given an asset receipt, When recorded, Then it lands in the correct stockroom.",
  "Given stockrooms, When reviewed, Then OOTB stockroom capability is used."],2)
add(m,"Activate the agreed IMAC workflows","asset manager","the in-scope IMAC (install/move/add/change) workflows activated","asset moves are governed",
 ["Given the IMAC decision, When configured, Then the agreed workflows are active at the agreed scope.",
  "Given an asset move, When initiated, Then the workflow drives the tasks.",
  "Given workflows, When reviewed, Then OOTB asset workflows are used."],2)
add(m,"Configure the asset intake process","asset manager","the asset intake process (purchase order to stockroom) configured","new assets enter the system cleanly",
 ["Given the intake decision, When configured, Then assets flow from receipt to stockroom via OOTB process.",
  "Given a received asset, When intaken, Then it is recorded with required attributes.",
  "Given intake, When reviewed, Then OOTB intake is used."],2)
add(m,"Configure asset retirement and disposal","asset manager","the asset retirement and disposal process configured","end-of-life assets are handled and recorded",
 ["Given the disposal decision, When configured, Then OOTB retirement/disposal steps are active with disposal vendors.",
  "Given a retired asset, When disposed, Then the record reflects disposal and compliance.",
  "Given the process, When reviewed, Then OOTB capability is used."],2)
add(m,"Define the asset ownership model","asset manager","the asset ownership model defined (user, department, or cost center)","assets roll up to the right accountability",
 ["Given the ownership decision, When configured, Then assets carry the agreed ownership dimension.",
  "Given an asset, When assigned, Then ownership resolves correctly.",
  "Given OOTB fields, When used, Then no custom ownership fields are added."],2)
add(m,"Link HAM assets to CMDB CIs","asset manager","assets linked to CMDB CIs with a clear management boundary","asset and CI data stay aligned for CSDM",
 ["Given the link decision, When configured, Then in-scope assets relate to their CMDB CIs.",
  "Given an asset/CI pair, When viewed, Then the asset-vs-CI managed attributes are clear.",
  "Given the link, When validated, Then OOTB asset-CI relationship is used."],3,"2 - High")

# ---------------- Performance Analytics ----------------
m="Performance Analytics"
add(m,"Activate the baseline OOTB indicators","analytics lead","the agreed OOTB PA indicators activated for go-live","operational performance is measured from day one",
 ["Given the indicator decision, When configured, Then OOTB indicators (MTTR, SLA attainment, change success...) are active.",
  "Given the first collection, When run, Then indicators populate with data.",
  "Given indicators, When reviewed, Then OOTB content packs are used."],3,"2 - High")
add(m,"Configure breakdown dimensions","analytics lead","breakdown dimensions configured for indicator segmentation","metrics can be sliced by the dimensions that matter",
 ["Given the breakdown decision, When configured, Then indicators segment by the agreed dimensions (group, category, priority).",
  "Given an indicator, When viewed, Then breakdowns render correctly.",
  "Given breakdowns, When reviewed, Then OOTB breakdown sources are used."],2)
add(m,"Build the agreed scorecards","analytics lead","scorecards built for the agreed audiences","leaders and teams see the metrics they need",
 ["Given the scorecard decision, When configured, Then scorecards exist per audience.",
  "Given an audience, When they open a scorecard, Then it shows their indicators.",
  "Given scorecards, When reviewed, Then OOTB PA is used."],2)
add(m,"Set indicator thresholds (green/yellow/red)","analytics lead","thresholds set for each indicator","performance status is visible at a glance",
 ["Given the threshold decision, When configured, Then each indicator has green/yellow/red bands.",
  "Given a breach, When it occurs, Then the indicator shows the correct status.",
  "Given thresholds, When reviewed, Then OOTB threshold config is used."],1)
add(m,"Configure the data collection cadence","analytics lead","data collection jobs scheduled at the agreed cadence","metrics are timely and consistent",
 ["Given the cadence decision, When configured, Then collection jobs run at the agreed times.",
  "Given a job, When it runs, Then it completes without errors.",
  "Given jobs, When reviewed, Then OOTB PA jobs are used."],1)
add(m,"Publish dashboards with the right access","analytics lead","PA dashboards published with role-based access","the right people see the right dashboards",
 ["Given the access decision, When configured, Then dashboards are shared per role.",
  "Given a user, When they open a dashboard, Then they see only what they are entitled to.",
  "Given publishing, When reviewed, Then OOTB sharing/ACLs are used."],2)
add(m,"Decide trending and forecasting activation","analytics lead","trending/forecasting activated at the agreed horizon (or deferred)","leaders can see direction, not just current state",
 ["Given the forecasting decision, When made, Then trending/forecasting is activated at the agreed horizon or deferred.",
  "Given an indicator, When forecast, Then the projection renders.",
  "Given the config, When validated, Then OOTB PA forecasting is used."],2)
add(m,"Migrate or retire Classic Reports","analytics lead","in-scope Classic Reports migrated to PA or retired","reporting consolidates on PA without clutter",
 ["Given the migration decision, When made, Then each in-scope Classic Report is migrated to PA or retired with rationale.",
  "Given a migrated report, When validated, Then the PA equivalent matches.",
  "Given the work, When reviewed, Then OOTB PA/reporting is used."],2)

# ---------------- Integrations ----------------
m="Integrations"
add(m,"Configure Active Directory / Entra ID user sync","integration engineer","AD/Entra ID user synchronization configured via OOTB scheduled import","user data stays accurate from the authoritative source",
 ["Given AD/Entra connectivity, When the OOTB import runs, Then in-scope users sync with required attributes.",
  "Given coalesce rules, When the import repeats, Then no duplicates are created.",
  "Given the integration, When validated, Then OOTB LDAP/Graph import is used (no custom sync code)."],3,"1 - Critical")
add(m,"Configure SSO (SAML 2.0 / OIDC)","integration engineer","SSO configured with the Connection IdP using OOTB SAML 2.0 (or OIDC)","users authenticate securely via single sign-on",
 ["Given IdP metadata, When configured, Then OOTB SSO authenticates users against the Connection IdP.",
  "Given a login, When SSO completes, Then the user lands authenticated.",
  "Given SSO, When validated, Then OOTB multi-provider SSO is used."],3,"1 - Critical")
add(m,"Configure the SCCM / MECM Service Graph Connector","integration engineer","the SCCM/MECM connector configured to populate CMDB","client/server CI data flows from SCCM into a CSDM-aligned CMDB",
 ["Given SCCM connection details, When configured, Then the OOTB SGC for SCCM connects and tests successfully.",
  "Given a scheduled import, When run, Then in-scope CIs populate per the class mapping.",
  "Given the connector, When validated, Then OOTB SGC is used (no custom JDBC pipeline)."],5,"2 - High")
add(m,"Configure the Microsoft Intune connector","integration engineer","the Intune connector configured to populate mobile/endpoint CI data","Intune-managed devices appear in the CMDB",
 ["Given Intune/Graph credentials, When configured, Then the OOTB Intune connector connects and tests successfully.",
  "Given a scheduled import, When run, Then in-scope devices populate.",
  "Given the connector, When validated, Then OOTB connector is used."],3,"2 - High")
add(m,"Map AD groups to ServiceNow groups and roles","integration engineer","AD group-to-ServiceNow group/role mapping configured","access derives from directory membership",
 ["Given the group mapping, When configured, Then AD groups sync to the agreed ServiceNow groups/roles.",
  "Given a membership change in AD, When synced, Then ServiceNow membership updates.",
  "Given mapping, When validated, Then OOTB group import is used."],3,"2 - High")
add(m,"Configure email integration","integration engineer","outbound SMTP relay and inbound mailboxes/actions configured","notifications send and inbound email creates/updates records",
 ["Given relay/mailbox details, When configured, Then outbound notifications deliver and inbound actions process mail.",
  "Given an inbound email, When received, Then the correct record is created/updated.",
  "Given email, When validated, Then OOTB email and inbound actions are used."],2)
add(m,"Configure integration health monitoring","integration engineer","integration health monitoring configured for all connectors","integration failures are detected early",
 ["Given the monitoring decision, When configured, Then connector run status and failures are visible.",
  "Given a failed import, When it occurs, Then it surfaces to the platform team.",
  "Given monitoring, When validated, Then OOTB integration logs/dashboards are used."],2)
add(m,"Confirm certificate and security requirements","integration engineer","certificate and security requirements satisfied for all integrations","integrations meet Connection security standards",
 ["Given security requirements, When applied, Then certificates and credentials meet Connection standards (vaulted, least-privilege).",
  "Given a connection, When established, Then it uses approved encryption.",
  "Given security, When reviewed, Then no secrets are hard-coded."],2,"2 - High")

# ---------------- Service Graph Connectors ----------------
m="Service Graph Connectors"
add(m,"Activate the in-scope Service Graph Connectors","integration engineer","the agreed Service Graph Connectors (SCCM, Intune) activated","authoritative CI data flows into the CMDB",
 ["Given the connector decision, When activated, Then SCCM and Intune SGCs are live for the agreed scope.",
  "Given activation, When run, Then in-scope CIs populate.",
  "Given connectors, When validated, Then OOTB SGC apps are used."],3,"2 - High")
add(m,"Set the source of record per CI class across connectors","integration engineer","an authoritative source of record set per CI class where connectors and Discovery overlap","CI conflicts resolve predictably",
 ["Given overlap, When IRE rules are set, Then the authoritative source wins per class.",
  "Given a CI from two sources, When ingested, Then it reconciles to one record.",
  "Given the rules, When validated, Then OOTB IRE is used."],3,"2 - High")
add(m,"Configure connector sync frequency","integration engineer","each connector's sync frequency configured","CI freshness matches operational need without overload",
 ["Given the cadence decision, When configured, Then each connector runs at the agreed frequency.",
  "Given a run, When complete, Then data is current within the agreed window.",
  "Given schedules, When validated, Then OOTB scheduling is used."],1)
add(m,"Map source attributes to ServiceNow CI fields","integration engineer","connector source fields mapped to OOTB CI fields","CI attributes are accurate and normalized",
 ["Given the mapping decision, When configured, Then source fields map to OOTB CI fields.",
  "Given a CI, When imported, Then key attributes populate correctly.",
  "Given mapping, When validated, Then OOTB connector mapping is used."],2)
add(m,"Configure Content Library normalization","integration engineer","OOTB Content/Context Service normalization configured","hardware/software names are normalized to prevent sprawl",
 ["Given the normalization decision, When configured, Then OOTB normalization standardizes product names.",
  "Given inconsistent source names, When imported, Then they normalize.",
  "Given normalization, When validated, Then OOTB Content Library is used."],2)
add(m,"Define the deduplication strategy across connectors","integration engineer","a deduplication strategy configured to prevent CI proliferation","the CMDB stays clean as connectors expand it",
 ["Given the dedup decision, When configured, Then IRE prevents duplicate CIs across connectors.",
  "Given a duplicate candidate, When ingested, Then it matches the existing CI.",
  "Given the strategy, When validated, Then OOTB IRE is used."],3,"2 - High")
add(m,"Configure connector health monitoring and escalation","integration engineer","connector health monitoring with escalation configured","connector failures are caught and escalated",
 ["Given the monitoring decision, When configured, Then connector health is visible with escalation on failure.",
  "Given a failed run, When it occurs, Then escalation triggers.",
  "Given monitoring, When validated, Then OOTB monitoring is used."],2)
add(m,"Validate the expanded CMDB before sprint close","integration engineer","the connector-expanded CMDB validated before sprint close","downstream processes trust the CI data",
 ["Given the connectors live, When validation runs, Then a sample of CIs is checked against source.",
  "Given gaps, When found, Then they are logged and remediated before close.",
  "Given validation, When complete, Then CMDB Health meets the agreed target."],2)

# ---------------- Vonage CTI & Interactions ----------------
m="Vonage CTI & Interactions"
add(m,"Install and configure the OOTB OpenFrame softphone","CTI engineer","OpenFrame configured to host the Vonage softphone in the workspace","agents have a CTI softphone without a separate app",
 ["Given OpenFrame activated, When configured, Then the Vonage softphone loads in the Agent/SO Workspace.",
  "Given an agent, When they log in, Then the softphone is available with the right roles.",
  "Given OpenFrame, When validated, Then OOTB OpenFrame + the Vonage adapter are used (no custom softphone)."],3,"2 - High")
add(m,"Map agents to Vonage extensions","CTI engineer","agents mapped to Vonage extensions/agent IDs","calls route to the correct ServiceNow agent",
 ["Given the agent mapping, When configured, Then each agent maps to their Vonage extension.",
  "Given an inbound call, When routed, Then it reaches the mapped agent.",
  "Given mapping, When validated, Then OOTB CTI mapping is used."],2)
add(m,"Configure inbound screen-pop and caller matching","CTI engineer","inbound screen-pop configured to open an Interaction with caller match","agents get caller context automatically",
 ["Given an inbound call, When it rings, Then an Interaction opens with the caller matched by phone number.",
  "Given no match, When the call arrives, Then a guest Interaction opens.",
  "Given matching, When validated, Then OOTB CTI/Interaction config is used (no scripted screen-pop)."],3,"2 - High")
add(m,"Configure Interaction to Incident/Request creation","CTI engineer","agents able to create or link an Incident/Request from the Interaction","calls convert to the right ITSM record",
 ["Given an Interaction, When the agent acts, Then they create or link an Incident or Request via OOTB actions.",
  "Given the created record, When saved, Then interaction_related_record links it to the Interaction.",
  "Given the flow, When validated, Then OOTB Interaction relationships are used."],3,"2 - High")
add(m,"Map Vonage queues to assignment groups","CTI engineer","Vonage queues/skills mapped to ServiceNow assignment groups","routing context carries from telephony to ITSM",
 ["Given the queue mapping, When configured, Then Vonage queues map to the agreed assignment groups.",
  "Given a queued call, When handled, Then the Interaction/record reflects the routing context.",
  "Given mapping, When validated, Then OOTB configuration is used."],2)
add(m,"Port the legacy Vonage configuration","CTI engineer","the legacy Vonage integration ported onto OOTB OpenFrame + connector","parity with the legacy phone experience without custom middleware",
 ["Given the legacy inventory, When reviewed, Then config is rebuilt OOTB and bespoke middleware is not ported.",
  "Given a custom legacy script, When found, Then it is evaluated vs OOTB and routed to Council if needed.",
  "Given parity testing, When run, Then inbound call to screen-pop to Incident/Request matches the legacy experience."],3,"2 - High")
