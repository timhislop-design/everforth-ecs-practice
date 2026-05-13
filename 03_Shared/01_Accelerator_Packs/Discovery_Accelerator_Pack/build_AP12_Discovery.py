"""
Build AP-12 — Discovery Accelerator Pack
6 xlsx workbooks + 1 README docx

Sprint alignment: Month 1 Sprint 2 — Discovery initiation and CMDB normalization.
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
TEMPLATES = os.path.join(REPO, "03_Shared", "00_Templates_and_Branding")
sys.path.insert(0, TEMPLATES)
from accelerator_pack_builder import TabContent, build_workbook
from ecs_template import EcsDocument, DocMeta

PACK_NAME = "Discovery Accelerator Pack"

wb1 = TabContent(
    workbook_title="01 — Discovery Scope & IP Ranges",
    pack_name=PACK_NAME,
    purpose="Defines the Discovery scope: which IP ranges are in scope, which subnets are excluded, and the phasing strategy for rolling Discovery across the environment. Scope decisions made here directly control what CI data populates in Sprint 2 and what remains out of scope for Phase 2.",
    who_fills="Customer-side: Network/Infrastructure Lead provides IP range documentation. IT Operations Manager approves the scope. ECS Architect reviews for Discovery feasibility.",
    sprint_window="Sprint 1 Week 2 — Sprint 2 Week 1",
    estimated_effort="2–3 hours to gather and document network topology",
    related_workbooks=["02 MID Server Configuration", "03 Credential Management", "CMDB-CSDM Pack — CI Class Selection"],
    success_criteria=[
        "All in-scope IP ranges are documented with CIDR notation.",
        "Excluded subnets are listed with rationale (DMZ, OT networks, etc.).",
        "Phase 1 vs Phase 2 scope boundary is agreed.",
        "Estimated device count per subnet is provided.",
        "Network team has confirmed Discovery traffic is permitted on in-scope ranges.",
    ],
    process_decisions=[
        ("Should we discover everything on the network or a scoped subset?",
         "Start with a scoped subset: corporate LAN subnets housing servers and workstations managed by IT. Exclude DMZ, OT/SCADA, guest Wi-Fi, and printer networks from Phase 1.",
         "Discovering everything creates thousands of stub CI records for unmanaged devices. A scoped approach produces accurate data for the CIs that matter and avoids polluting the CMDB with noise."),
        ("How should we handle cloud-hosted resources in the Discovery scope?",
         "Exclude cloud resources from IP-range Discovery. Use Service Graph Connectors or Cloud Management for cloud CIs. IP-range Discovery was designed for on-prem networks.",
         "IP-range Discovery of cloud VPCs requires VPN connectivity and produces unreliable results. OOTB SGCs (AWS, Azure) are the authoritative source for cloud CIs."),
        ("What happens to devices Discovery finds but that are not in the agreed CI class scope?",
         "Discovery finds them but IRE rules prevent CI creation for out-of-scope classes. Configure IRE to skip creation for out-of-scope classes rather than creating stub records.",
         "Stub records for out-of-scope devices (printers, phones, IoT) are harder to clean up than preventing their creation. Configure IRE exclusion rules before the first Discovery run."),
        ("How often should Discovery run?",
         "Weekly for servers and workstations. Daily for critical infrastructure CIs. SGC syncs can run more frequently (every 4–6 hours for SCCM/Intune). Do not run Discovery continuously — it generates significant network traffic.",
         "Weekly Discovery provides a 7-day staleness window which is within the 30-day threshold. Daily runs are reserved for environments with high CI turnover (e.g., VDI pools)."),
    ],
    dependencies=[
        ("Network topology document (IP ranges, VLANs, subnets)", "Required", "Customer Network Lead", "Sprint 1 Wk 2", "Cannot scope Discovery without network documentation."),
        ("Network team approval for Discovery traffic on in-scope subnets", "Required", "Customer Network Lead", "Sprint 1 Wk 2", "Discovery generates ICMP, WMI, SSH, and SNMP traffic. Security team must approve."),
        ("CMDB-CSDM CI Class Selection (Workbook 02) confirmed", "Required", "ECS SA", "Sprint 1 Wk 2", "Discovery scope must align with agreed CI classes."),
    ],
    config_sections=[
        ("In-Scope IP Ranges", [
            ("Corporate LAN — servers", "[Customer: CIDR notation, e.g. 10.10.0.0/24]", "Primary server subnet.", True),
            ("Corporate LAN — workstations", "[Customer: CIDR notation]", "End-user device subnets.", True),
            ("DMZ", "Excluded — Phase 2 if required", "DMZ devices require separate credential set and security approval.", False),
            ("Guest Wi-Fi", "Excluded permanently", "Guest devices are not IT-managed and should not appear in CMDB.", False),
            ("OT/SCADA networks", "Excluded permanently", "OT networks must never be scanned without explicit OT team approval.", False),
            ("Cloud (AWS/Azure)", "Excluded — use SGC instead", "Handled by Service Graph Connectors, not IP-range Discovery.", False),
        ]),
        ("Phasing", [
            ("Phase 1 (Sprint 2)", "[Customer: list subnets]", "Start with server subnet; add workstation subnet after first validation.", True),
            ("Phase 2 (post-Sprint 2)", "[Customer: list subnets]", "Remaining in-scope subnets after Phase 1 is validated.", True),
            ("Estimated device count — Phase 1", "[Customer: estimate]", "Used to size MID Server and validate Discovery results.", True),
        ]),
    ],
    raci_rows=[
        ("Provide IP range and network topology documentation", "I", "R/A", "Customer Network Lead."),
        ("Approve Discovery traffic on in-scope subnets", "I", "R/A", "Customer Network/Security team."),
        ("Configure Discovery scope in ServiceNow", "R/A", "I", "ECS Architect."),
        ("Validate first Discovery run — device counts plausible", "R", "A", "ECS validates; customer confirms counts."),
    ],
    consultant_guide_sections=[
        ("Scope conversation", "The most common scope mistake is including too many subnets in Phase 1. Start with the server subnet only. A successful server Discovery in week 1 builds confidence. Workstation Discovery can be added in week 2 once credentials and MID Server are validated."),
        ("OT/SCADA boundary", "Never agree to discover OT networks without explicit sign-off from both the OT team and the CISO. OT equipment (PLCs, SCADA controllers) can be destabilized by network scanning. This is a safety issue, not just a scope issue."),
    ],
    adoption_rows=[
        ("We want to discover everything — all subnets, all devices",
         "Phase 1 scope to managed IT subnets. Phase 2 expands after validation.",
         "Discovering everything in Sprint 2 creates thousands of CI records for unmanaged devices before governance is in place. Scope creep at Discovery is CMDB health debt.",
         "'Discovering everything at once means your first CMDB report will be full of printers, phones, and IoT devices that nobody is responsible for. Let's start with what IT manages, prove the model works, then expand. You get a trusted CMDB faster with a narrower start.'",
         "Never expand scope without confirming governance (data steward, staleness process) is in place."),
    ],
    snmap_sections=[
        ("Discovery Configuration", [
            ("Discovery Schedule", "Discovery > Discovery Schedules", "One schedule per phase. Set IP ranges, frequency, and MID Server."),
            ("Discovery Status", "Discovery > Discovery Status", "Monitor active Discovery runs and errors here."),
            ("Excluded IP Ranges", "Discovery > Exclusion Lists", "Configure excluded subnets before the first Discovery run."),
        ]),
    ],
)

wb2 = TabContent(
    workbook_title="02 — MID Server Configuration",
    pack_name=PACK_NAME,
    purpose="Defines the MID Server deployment plan: server sizing, placement, Windows vs Linux, redundancy, and validation requirements. The MID Server is the single point of failure for Discovery — getting it right in Sprint 1 prevents Discovery failures throughout the engagement.",
    who_fills="ECS Architect designs the MID Server plan; customer Infrastructure team provisions the VM and network access.",
    sprint_window="Sprint 1 Weeks 1–2 (must be deployed before Sprint 2 Discovery runs)",
    estimated_effort="4–8 hours for VM provisioning and MID Server installation/validation",
    related_workbooks=["01 Discovery Scope", "03 Credential Management"],
    success_criteria=[
        "MID Server VM is provisioned and meets sizing requirements.",
        "MID Server is installed, registered, and validated (green status in ServiceNow).",
        "MID Server can reach all in-scope IP ranges from its network position.",
        "MID Server has outbound HTTPS access to the ServiceNow instance.",
        "Redundant MID Server (or failover plan) is documented.",
    ],
    process_decisions=[
        ("Windows or Linux MID Server?",
         "Windows MID Server if the environment is predominantly Windows (enables WMI Discovery natively). Linux MID Server for Linux-heavy environments. Use Windows as the default for mixed environments.",
         "WMI discovery of Windows servers and workstations requires the MID Server to be on a Windows host with domain access. A Linux MID Server can still discover Windows targets via WMI but requires additional credential configuration."),
        ("How many MID Servers are needed?",
         "One MID Server per network segment that is not reachable from a single point. Minimum one for the corporate LAN. Add a second for redundancy if the environment has >500 managed devices.",
         "A single MID Server is sufficient for most mid-market environments. Redundancy is a Phase 2 consideration unless the customer has a high-availability requirement."),
        ("Where should the MID Server be placed on the network?",
         "On the corporate LAN with visibility to all in-scope subnets. The MID Server must be able to reach target devices on WMI (port 135/445), SSH (port 22), and SNMP (port 161) as applicable.",
         "A MID Server that cannot reach target subnets produces no Discovery data. Validate network reachability before the MID Server is installed — not after."),
        ("What are the minimum VM sizing requirements?",
         "Minimum: 4 vCPU, 8 GB RAM, 100 GB disk. Recommended for >500 devices: 8 vCPU, 16 GB RAM, 200 GB disk. Run on a dedicated VM — do not co-locate with other workloads.",
         "Under-resourced MID Servers are the most common cause of slow or incomplete Discovery runs. The MID Server processes probe results locally before sending to ServiceNow."),
    ],
    dependencies=[
        ("VM provisioned per sizing requirements", "Required", "Customer Infrastructure Lead", "Sprint 1 Wk 1", "MID Server software cannot be installed until the VM is ready."),
        ("ServiceNow instance URL and MID Server credentials", "Required", "ECS Architect", "Sprint 1 Wk 1", "Required to register the MID Server with the instance."),
        ("Network firewall rules allowing MID Server traffic to in-scope subnets", "Required", "Customer Network Lead", "Sprint 1 Wk 1", "Without firewall rules, Discovery probes cannot reach target devices."),
        ("Outbound HTTPS (443) from MID Server to ServiceNow instance URL", "Required", "Customer Network Lead", "Sprint 1 Wk 1", "MID Server communicates results to ServiceNow via HTTPS."),
    ],
    config_sections=[
        ("MID Server Specification", [
            ("MID Server hostname", "[Customer to complete]", "", True),
            ("Operating system", "[Windows Server 2019/2022 recommended]", "", True),
            ("vCPU", "[4 minimum / 8 recommended]", "", True),
            ("RAM (GB)", "[8 minimum / 16 recommended]", "", True),
            ("Disk (GB)", "[100 minimum / 200 recommended]", "", True),
            ("Network location", "[Corporate LAN segment with visibility to in-scope subnets]", "", True),
            ("MID Server service account", "[Customer to complete — domain service account]", "Requires local admin on MID Server host. Domain admin not required.", True),
            ("Redundant MID Server planned?", "[Yes / No / Phase 2]", "", True),
        ]),
        ("Validation Checklist", [
            ("MID Server status in ServiceNow", "Up (green)", "Check Discovery > MID Servers.", False),
            ("Test probe to server subnet — responds", "Pass", "Run test Discovery against one known server IP.", False),
            ("Test probe to workstation subnet — responds", "Pass", "Run after server subnet is validated.", False),
            ("Outbound HTTPS to instance confirmed", "Pass", "MID Server logs show no connection errors.", False),
        ]),
    ],
    raci_rows=[
        ("Provision MID Server VM", "C", "R/A", "Customer Infrastructure Lead provisions the VM."),
        ("Install and register MID Server software", "R/A", "C", "ECS Architect installs; customer provides access."),
        ("Configure firewall rules for Discovery traffic", "C", "R/A", "Customer Network Lead configures firewall."),
        ("Validate MID Server and run test probe", "R/A", "C", "ECS Architect validates; customer IT Ops confirms."),
    ],
    consultant_guide_sections=[
        ("MID Server is the critical path item", "The MID Server must be deployed and validated before any Discovery configuration begins. If the MID Server is delayed, Sprint 2 Discovery is delayed. Escalate immediately if VM provisioning is not started by Sprint 1 Week 1. This is the most common Sprint 2 delay and it is always caused by late VM provisioning."),
        ("Service account permissions", "The MID Server service account needs local administrator rights on the MID Server host to install and run as a Windows service. It does NOT need domain admin rights. Many customers confuse these — clarify early to avoid a security team rejection of a 'domain admin request'."),
    ],
    adoption_rows=[
        ("We want to use an existing server rather than provisioning a new VM",
         "Provision a dedicated VM. Do not co-locate the MID Server with production workloads.",
         "Co-located MID Servers compete for CPU and memory during Discovery runs, causing both Discovery and the host workload to perform poorly. A dedicated VM is the OOTB recommendation and is required for supportability.",
         "'The MID Server has CPU and memory spikes during Discovery runs. If it is sharing a host with your SQL Server, both services will be impacted during those spikes. A dedicated VM costs almost nothing in a virtualised environment and eliminates the risk.'",
         "Never co-locate. If resource constraints are severe, reduce MID Server sizing rather than co-locating."),
    ],
    snmap_sections=[
        ("MID Server Management", [
            ("MID Server record", "ecc_agent", "Registered MID Servers appear here."),
            ("MID Server status", "Discovery > MID Servers", "Must show 'Up' before Discovery schedules run."),
            ("MID Server logs", "ECC Queue > Output (filter by MID Server)", "Review for connection errors after installation."),
        ]),
    ],
)

wb3 = TabContent(
    workbook_title="03 — Credential Management",
    pack_name=PACK_NAME,
    purpose="Defines the Discovery credential strategy: which credential types are needed, how they are stored in ServiceNow, and what permissions each credential requires. Credential gaps are the primary cause of incomplete Discovery — a CI that cannot be authenticated produces only a stub record with no meaningful attributes.",
    who_fills="Customer-side: IT Operations Lead and Active Directory admin provide credentials. ECS Architect configures the credential store in ServiceNow.",
    sprint_window="Sprint 1 Week 2 (must be ready before Sprint 2 Discovery runs)",
    estimated_effort="2–4 hours to gather credentials and configure credential store",
    related_workbooks=["01 Discovery Scope", "02 MID Server Configuration"],
    success_criteria=[
        "Windows/WMI credentials are stored in ServiceNow credential store and validated.",
        "Linux/SSH credentials are stored and validated (if Linux hosts are in scope).",
        "SCCM/Intune API credentials are stored for SGC configuration.",
        "VMware vCenter credentials are stored (if virtualised environment).",
        "Credential rotation plan is documented.",
    ],
    process_decisions=[
        ("Should Discovery use a dedicated service account or existing admin accounts?",
         "Dedicated Discovery service account with the minimum permissions required. Never use a named admin account for Discovery — it ties Discovery availability to an individual's account status.",
         "Named admin accounts get disabled when the person leaves, locked when the password expires, and audited in ways that create noise. A dedicated service account with a documented rotation schedule is the OOTB best practice."),
        ("What permissions does the Windows Discovery account need?",
         "Local administrator on target Windows devices (for WMI access). Domain-joined — member of the local Administrators group via GPO, not a domain admin. Specifically needs: WMI namespace access, Remote Registry access, and Service Control Manager access.",
         "Domain admin for Discovery is the most common over-privilege request from customers. WMI Discovery does not require domain admin. Document the exact permissions to support the security team's approval process."),
        ("How should credentials be stored and secured in ServiceNow?",
         "Use the OOTB Credential Store (Discovery > Credentials). Passwords are encrypted at rest using the instance encryption key. Do not store credentials in Discovery schedule notes or configuration fields.",
         "The OOTB Credential Store is the only security-compliant method for storing Discovery credentials in ServiceNow. Any other storage method creates an audit finding."),
        ("How often should Discovery credentials be rotated?",
         "Align to the organisation's password policy — typically every 90 days. Configure a calendar reminder for the ECS SA and the customer IT Ops Lead. ServiceNow must be updated on each rotation.",
         "Expired Discovery credentials cause Discovery to fail silently — CIs are not updated but no alert is generated unless CMDB Health staleness rules are in place. A rotation calendar prevents this."),
    ],
    dependencies=[
        ("Active Directory service account created with minimum permissions", "Required", "Customer AD Admin", "Sprint 1 Wk 2", ""),
        ("Linux service account with SSH key (if Linux in scope)", "Required", "Customer Linux Admin", "Sprint 1 Wk 2", "SSH key authentication is preferred over password for Linux Discovery."),
        ("VMware vCenter read-only account (if virtualised)", "Required", "Customer VMware Admin", "Sprint 1 Wk 2", ""),
        ("SCCM API account for Service Graph Connector", "Required", "Customer SCCM Admin", "Sprint 1 Wk 2", ""),
        ("Intune API credentials (Azure AD app registration)", "Required", "Customer Azure Admin", "Sprint 1 Wk 2", "Intune SGC uses OAuth — requires Azure AD app registration with Device.Read.All permission."),
    ],
    config_sections=[
        ("Credential Store Entries", [
            ("Windows/WMI credential name", "ECS_Discovery_Windows", "Named in ServiceNow Credential Store.", False),
            ("Windows account format", "DOMAIN\\svc_discovery (or svc_discovery@domain.com)", "", True),
            ("Linux/SSH credential type", "SSH Private Key (preferred) or Username/Password", "", True),
            ("VMware credential name", "ECS_Discovery_VMware", "Read-only vCenter account.", False),
            ("SCCM SGC credential", "ECS_SGC_SCCM", "SCCM service account with Read access to SCCM WMI namespace.", False),
            ("Intune SGC credential", "ECS_SGC_Intune", "Azure AD app registration — Client ID, Client Secret, Tenant ID.", False),
        ]),
        ("Minimum Permission Requirements", [
            ("Windows Discovery — required groups/permissions", "Local Administrators (via GPO); WMI namespace root\\cimv2 read; Remote Registry read", "", False),
            ("Linux Discovery — required permissions", "SSH login; sudo for specific commands (lshw, dmidecode, ifconfig)", "", False),
            ("VMware vCenter — required role", "Read-Only (OOTB vCenter role)", "", False),
            ("SCCM — required permissions", "Read access to SMS WMI namespace; Collection Read", "", False),
            ("Intune Azure AD app — required API permissions", "Device.Read.All; DeviceManagementManagedDevices.Read.All", "", False),
        ]),
        ("Credential Rotation", [
            ("Rotation frequency", "[Customer to complete — align to password policy]", "", True),
            ("Rotation owner", "[Customer to complete]", "IT Ops Lead or AD Admin.", True),
            ("ServiceNow update process", "Update credential in Discovery > Credentials > [credential record]", "ECS SA or customer admin updates the record on each rotation.", False),
        ]),
    ],
    raci_rows=[
        ("Create Discovery service accounts with minimum permissions", "C", "R/A", "Customer AD/Linux/VMware admins create accounts."),
        ("Configure credentials in ServiceNow Credential Store", "R/A", "I", "ECS Architect configures the Credential Store."),
        ("Test credential against target devices", "R/A", "C", "ECS Architect tests; customer confirms access is correct."),
        ("Document credential rotation calendar", "R/A", "C", "ECS SA documents; customer IT Ops owns ongoing rotation."),
        ("Configure Intune Azure AD app registration", "C", "R/A", "Customer Azure Admin creates the app registration."),
    ],
    consultant_guide_sections=[
        ("The domain admin pushback", "Security teams sometimes push back on providing any account for Discovery, asking for justification of each permission. Prepare a one-page permission justification document: WMI requires Local Admin on the target because Microsoft's WMI security model does not support a 'WMI read-only' role. Remote Registry is needed for software inventory. Service Control Manager is needed for service state. Having this document ready prevents a 2-week security review delay."),
        ("SSH key vs password for Linux", "Always request SSH key authentication for Linux Discovery, not a password. SSH keys are more secure, do not expire, and are easier to audit. If the customer insists on password authentication, configure the credential with the password and document the rotation requirement. Key rotation for SSH keys is still recommended annually."),
    ],
    adoption_rows=[
        ("We don't want to give Discovery full local admin — can we use a limited account?",
         "Local admin is the minimum required for WMI Discovery on Windows. There is no lower-privilege option for full Discovery.",
         "WMI's security model requires local admin for remote access. Microsoft does not provide a 'WMI read-only' role. The account is dedicated to Discovery and monitored — it cannot be used interactively.",
         "'The local admin requirement is a Microsoft constraint, not an ECS choice. The Discovery account cannot log in interactively, cannot make changes — it only reads data via WMI. Your SIEM will show it as a service account with read activity only. We document this for your audit record.'",
         "If the security team absolutely refuses local admin, Discovery can run with limited scope using SNMP (network devices) and agent-based discovery (ServiceNow agent installed on each device). Both produce inferior data compared to WMI Discovery."),
    ],
    snmap_sections=[
        ("Credential Configuration", [
            ("Credential Store", "Discovery > Credentials", "All Discovery credentials stored here. Encrypted at rest."),
            ("Credential Affinity", "Discovery > Credential Affinity", "Map specific credentials to specific IP ranges for multi-credential environments."),
        ]),
    ],
)

wb4 = TabContent(
    workbook_title="04 — Discovery Schedules & Patterns",
    pack_name=PACK_NAME,
    purpose="Defines the Discovery schedule configuration: schedule names, IP ranges, MID Server assignment, frequency, and the Discovery patterns activated for each in-scope CI class. Pattern selection determines what attributes are collected — activating unnecessary patterns wastes MID Server resources and slows Discovery.",
    who_fills="ECS Architect completes this workbook based on decisions from Workbooks 01–03. Customer IT Ops reviews the schedule plan and confirms frequency is acceptable.",
    sprint_window="Sprint 2 Week 1",
    estimated_effort="2–3 hours to configure schedules and validate patterns in non-prod",
    related_workbooks=["01 Discovery Scope", "02 MID Server Configuration", "03 Credential Management"],
    success_criteria=[
        "At least one Discovery schedule is configured and validated for in-scope subnets.",
        "Only required Discovery patterns are activated (no pattern sprawl).",
        "First Discovery run completes without critical errors.",
        "CI counts from first run are within expected range (validated against network team estimate).",
        "Discovery log is reviewed and any authentication failures are documented.",
    ],
    process_decisions=[
        ("Should we use Quick Discovery or full Horizontal Discovery?",
         "Horizontal Discovery for the primary run (discovers full CI attributes). Quick Discovery for validation checks only — it identifies what devices are on the network but does not collect full attribute data.",
         "Horizontal Discovery is the OOTB pattern that populates CI attributes. Quick Discovery is a reconnaissance tool, not a data collection tool. Many customers confuse them — only Horizontal Discovery populates CIs."),
        ("Which Discovery patterns should be activated at MVP?",
         "Activate only: Windows OS pattern (for servers and workstations), Linux OS pattern (if Linux in scope), VMware Infrastructure pattern (if virtualised), Software (Installed) pattern (for cmdb_ci_appl population via Discovery). Deactivate: Network Gear, Storage, Printer patterns unless those classes are in scope.",
         "Every activated pattern runs on every device in scope. Activating Network Gear patterns on a workstation subnet generates thousands of failed probes. Pattern selection must match CI class scope from the CMDB-CSDM pack."),
        ("How should Discovery handle devices that fail authentication?",
         "Log authentication failures in Discovery Status. Review weekly — authentication failures mean a device was found on the network but credentials did not work. These are either out-of-scope devices or a credential issue. Do not create CI records for devices that fail all authentication attempts.",
         "Authentication failure logs are the most useful diagnostic tool for Discovery health. Review them after every Discovery run in the first 4 weeks to confirm credential coverage is complete."),
    ],
    dependencies=[
        ("MID Server validated (Workbook 02)", "Required", "ECS Architect", "Sprint 2 Wk 1", ""),
        ("Credentials configured (Workbook 03)", "Required", "ECS Architect", "Sprint 2 Wk 1", ""),
        ("Discovery scope confirmed (Workbook 01)", "Required", "Customer + ECS", "Sprint 1 Wk 2", ""),
    ],
    config_sections=[
        ("Discovery Schedules", [
            ("Schedule 1 — Name", "ECS_Phase1_Servers", "", False),
            ("Schedule 1 — IP range", "[Server subnet CIDR from Workbook 01]", "", True),
            ("Schedule 1 — Frequency", "Weekly (Sunday 02:00 AM)", "Run during low-traffic period.", False),
            ("Schedule 1 — MID Server", "[MID Server hostname from Workbook 02]", "", True),
            ("Schedule 2 — Name", "ECS_Phase1_Workstations", "", False),
            ("Schedule 2 — IP range", "[Workstation subnet CIDR]", "", True),
            ("Schedule 2 — Frequency", "Weekly (Saturday 23:00)", "Run after server schedule completes.", False),
        ]),
        ("Activated Patterns (MVP)", [
            ("Windows OS — Horizontal", "Active", "Populates cmdb_ci_server, cmdb_ci_computer, cmdb_ci_network_adapter.", False),
            ("Linux OS — Horizontal", "Active if Linux in scope / Inactive otherwise", "", True),
            ("VMware Infrastructure", "Active if VMware in scope / Inactive otherwise", "Populates cmdb_ci_vm_instance.", True),
            ("Software (Installed)", "Active", "Populates cmdb_ci_appl from installed software inventory.", False),
            ("Network Gear", "Inactive — Phase 2", "Activate only if network devices are in CI class scope.", False),
            ("Storage", "Inactive — Phase 2", "", False),
            ("Printer", "Inactive — permanently excluded", "Printers are not in scope.", False),
        ]),
    ],
    raci_rows=[
        ("Configure Discovery schedules in ServiceNow", "R/A", "I", "ECS Architect."),
        ("Activate/deactivate Discovery patterns per scope", "R/A", "I", "ECS Architect."),
        ("Run first Discovery and review results", "R/A", "C", "ECS Architect runs; customer IT Ops reviews device counts."),
        ("Review authentication failure log", "R/A", "C", "ECS reviews; customer confirms out-of-scope devices."),
    ],
    consultant_guide_sections=[
        ("First Discovery run review", "After the first Discovery run, export and review: (1) CI count by class — does it match the customer's estimate? (2) Authentication failure list — any in-scope devices that failed? (3) Pattern probe errors — any patterns that found no targets? This 30-minute review after the first run is the most valuable time investment in the Discovery sprint."),
    ],
    adoption_rows=[
        ("We want Discovery to run continuously (always-on)",
         "Schedule Discovery weekly. Continuous Discovery is not an OOTB option and would generate excessive network traffic.",
         "Continuous Discovery would generate WMI and SSH connections on every device every few minutes. This creates significant network overhead and is not supported by ServiceNow.",
         "'Weekly Discovery gives you a 7-day staleness window — which is well within the 30-day threshold. If you need faster updates for specific critical servers, we can run a daily schedule targeting just those servers by IP. That gives you the freshness where it matters without the overhead everywhere.'",
         "Daily schedule for critical infrastructure is acceptable. Never continuous."),
    ],
    snmap_sections=[
        ("Discovery Configuration Tables", [
            ("Discovery Schedule", "discovery_schedule", "One record per Discovery schedule."),
            ("Discovery Status", "discovery_status", "Tracks active and completed Discovery runs."),
            ("Discovery Log", "discovery_log", "Authentication failures, probe errors, CI creation events."),
            ("ECC Queue", "ecc_queue", "MID Server probe results queue. Review for errors during first run."),
        ]),
    ],
)

wb5 = TabContent(
    workbook_title="05 — Service Graph Connector Configuration",
    pack_name=PACK_NAME,
    purpose="Defines the configuration for SCCM and Intune Service Graph Connectors — the primary data source for endpoint CI data (cmdb_ci_computer) and installed application CIs (cmdb_ci_appl). SGC is preferred over agentless Discovery for endpoints because SCCM/Intune data is more comprehensive and more reliable than WMI probes on roaming devices.",
    who_fills="ECS Architect configures SGC; customer SCCM/Intune admins provide API credentials and validate device counts after the first sync.",
    sprint_window="Sprint 2 Weeks 1–2",
    estimated_effort="4–6 hours per connector for initial configuration and validation",
    related_workbooks=["03 Credential Management", "CMDB-CSDM Pack — CI Class Selection"],
    success_criteria=[
        "SCCM SGC is installed, configured, and first sync completed successfully.",
        "Intune SGC is installed, configured, and first sync completed successfully.",
        "CI count from SGC syncs matches SCCM/Intune device inventory (within 5% tolerance).",
        "Duplicate CI prevention rules (IRE) are validated — SGC and Discovery do not create duplicates.",
        "Sync schedule is configured and documented.",
    ],
    process_decisions=[
        ("Should we use SCCM SGC, Intune SGC, or both?",
         "Both if the environment uses both management platforms. SCCM for domain-joined managed workstations; Intune for modern-managed (Azure AD joined) devices. They use different identifiers — configure both and rely on IRE deduplication.",
         "Environments moving from SCCM to Intune frequently have devices managed by both simultaneously. Using both SGCs ensures complete coverage during the transition period."),
        ("Should SGC replace Discovery for endpoints or complement it?",
         "SGC is the primary source for endpoint CIs. Agentless Discovery is the primary source for servers. Do not run both on the same device — IRE will deduplicate, but the redundant data creates probe noise.",
         "SGC produces richer endpoint data than WMI Discovery because SCCM/Intune already collect comprehensive hardware inventory. Using SGC for endpoints and Discovery for servers divides the data collection work by the tool best suited for each CI type."),
        ("How frequently should SGC syncs run?",
         "Every 4–6 hours for SCCM (incremental sync — only changed devices). Daily full sync as a baseline. Intune SGC can run more frequently as it uses a lightweight Microsoft Graph API call.",
         "Frequent incremental syncs keep endpoint CIs current without the overhead of full syncs. A 4-hour window means endpoint CIs are at most 4 hours stale — well within the 30-day staleness threshold."),
    ],
    dependencies=[
        ("SCCM API credentials configured (Workbook 03)", "Required", "Customer SCCM Admin", "Sprint 2 Wk 1", ""),
        ("Intune Azure AD app registration (Workbook 03)", "Required", "Customer Azure Admin", "Sprint 2 Wk 1", ""),
        ("IntegrationHub licence confirmed", "Required", "ECS Architect", "Sprint 1", "SGCs require IntegrationHub. Confirm licence before configuring."),
        ("MID Server validated (Workbook 02)", "Required", "ECS Architect", "Sprint 2 Wk 1", "SGC runs through the MID Server."),
    ],
    config_sections=[
        ("SCCM SGC Configuration", [
            ("SCCM site server hostname", "[Customer to complete]", "", True),
            ("SCCM WMI namespace", "root\\SMS\\site_[site code]", "Replace [site code] with customer's SCCM site code.", True),
            ("SCCM sync frequency", "Incremental: every 4 hours / Full: daily at 01:00", "", False),
            ("SCCM CI classes populated", "cmdb_ci_computer, cmdb_ci_appl (managed software), cmdb_ci_network_adapter", "", False),
            ("MID Server for SCCM SGC", "[MID Server hostname from Workbook 02]", "", True),
        ]),
        ("Intune SGC Configuration", [
            ("Azure AD Tenant ID", "[Customer to complete]", "", True),
            ("Azure AD App Client ID", "[Customer to complete]", "", True),
            ("Intune sync frequency", "Every 6 hours", "", False),
            ("Intune CI classes populated", "cmdb_ci_computer (modern-managed devices)", "", False),
            ("IRE deduplication key between SCCM and Intune", "Serial number + OS", "IRE uses serial number to deduplicate CIs found by both SGCs.", False),
        ]),
        ("IRE Deduplication Rules", [
            ("Deduplication between SCCM SGC and Discovery", "Active — serial number + hostname", "IRE prevents duplicate CI creation when both sources find the same device.", False),
            ("Deduplication between SCCM and Intune SGC", "Active — serial number + OS", "", False),
            ("Source priority (in case of conflict)", "SCCM > Intune > Discovery", "SCCM data takes precedence for domain-joined devices.", False),
        ]),
    ],
    raci_rows=[
        ("Provide SCCM site server details and WMI namespace", "I", "R/A", "Customer SCCM Admin."),
        ("Create Azure AD app registration for Intune SGC", "C", "R/A", "Customer Azure Admin."),
        ("Install and configure SCCM SGC in ServiceNow", "R/A", "I", "ECS Architect."),
        ("Install and configure Intune SGC in ServiceNow", "R/A", "I", "ECS Architect."),
        ("Validate first SGC sync — CI counts match SCCM/Intune inventory", "R", "A", "ECS validates counts; customer SCCM/Intune admin confirms source counts."),
        ("Configure IRE deduplication rules", "R/A", "I", "ECS Architect."),
    ],
    consultant_guide_sections=[
        ("SGC vs. Discovery for endpoints", "The most important sequencing decision: configure SCCM/Intune SGC before running Discovery on workstation subnets. If Discovery runs first and creates computer CIs, SGC will create duplicates that IRE must resolve. SGC first means Discovery can be scoped to server-only subnets and the workstation CI data comes entirely from the more reliable SCCM/Intune source."),
        ("IntegrationHub licence check", "SGCs require IntegrationHub. Confirm this licence is active before Sprint 2 begins. IntegrationHub licensing issues are a common Sprint 2 blocker that ECS cannot resolve without customer involvement with their ServiceNow account team."),
    ],
    adoption_rows=[
        ("We want to use SCCM/Intune data but keep Discovery running on workstations too",
         "Use SGC as the primary source for endpoints. Exclude workstation subnets from Discovery schedules.",
         "Running both on the same devices creates IRE merge conflicts and doubles the data collection overhead. SGC data from SCCM is more complete than WMI Discovery for endpoints.",
         "'SCCM already has everything Discovery would find — and more. Hardware inventory, installed software, patch status. Running Discovery on top of SCCM data is duplicate work. We'll use SCCM for endpoints and Discovery for servers — each tool doing what it does best.'",
         "Only if the customer has specific servers that must come from SGC rather than Discovery. Design with ECS Architect."),
    ],
    snmap_sections=[
        ("SGC Tables", [
            ("SGC Data Source", "sn_disco_datasource", "Registered SGC data sources."),
            ("SGC Transform Map", "sys_transform_map", "Maps SCCM/Intune data to ServiceNow CI fields."),
            ("IntegrationHub Flow", "Flow Designer > SGC Flows", "Orchestrates the SGC sync process."),
        ]),
    ],
)

wb6 = TabContent(
    workbook_title="06 — Reconciliation & IRE Rules",
    pack_name=PACK_NAME,
    purpose="Defines the Identification and Reconciliation Engine (IRE) rules that prevent duplicate CI creation and control which data source wins when multiple sources report conflicting attribute values. IRE is the governance layer that keeps the CMDB accurate when Discovery, SCCM SGC, and Intune SGC all run simultaneously.",
    who_fills="ECS Architect designs the IRE rules; customer validates the deduplication results after first Discovery + SGC runs.",
    sprint_window="Sprint 2 Weeks 1–2 (configure before first combined Discovery + SGC run)",
    estimated_effort="3–4 hours to configure and validate IRE rules",
    related_workbooks=["04 Discovery Schedules", "05 SGC Configuration"],
    success_criteria=[
        "IRE identification rules are configured for each in-scope CI class.",
        "No duplicate CI records exist after combined Discovery + SGC run.",
        "Source precedence rules are configured (which data source wins conflicts).",
        "IRE auto-relationship rules are configured (links CIs to CSDM services).",
        "IRE reconciliation log is reviewed and any conflicts are resolved.",
    ],
    process_decisions=[
        ("What should be the primary CI identifier for Windows computers?",
         "Serial number as the primary identifier, with hostname as a secondary fallback. Never use IP address as a CI identifier — IP addresses change.",
         "Serial numbers are stable hardware identifiers that do not change when devices are reimaged, renamed, or moved. IP addresses change with DHCP and network moves. A serial-number-based IRE rule prevents duplicate CIs when a device appears in multiple data sources."),
        ("Which data source should win when attributes conflict?",
         "SCCM SGC wins for endpoint attributes (hardware, OS, software). Discovery wins for server attributes (IP, services, running processes). Intune SGC wins for modern management attributes (compliance state, MDM enrollment). Configure source precedence per CI class.",
         "Without explicit source precedence, IRE uses a first-in rule that produces unpredictable results when sources conflict. Explicit precedence ensures the most authoritative source always wins for each attribute type."),
        ("Should IRE auto-create new CI classes when Discovery finds unexpected device types?",
         "No. Configure IRE to only create CI records for the agreed in-scope classes. For out-of-scope device types, IRE should log the discovery without creating a CI record.",
         "Auto-creating CI records for out-of-scope classes undermines the MVP scope boundary agreed in the CMDB-CSDM pack. IRE class restrictions are the enforcement mechanism for the CI class governance gate."),
    ],
    dependencies=[
        ("CI Class Selection (CMDB-CSDM Workbook 02) confirmed", "Required", "ECS SA", "Sprint 1 Wk 2", "IRE rules are scoped to agreed CI classes."),
        ("Discovery schedules configured (Workbook 04)", "Required", "ECS Architect", "Sprint 2 Wk 1", ""),
        ("SGC configured (Workbook 05)", "Required", "ECS Architect", "Sprint 2 Wk 1", ""),
    ],
    config_sections=[
        ("Identification Rules per CI Class", [
            ("cmdb_ci_computer — primary identifier", "Serial number (serial_number)", "Fallback: hostname + OS + MAC address.", False),
            ("cmdb_ci_server — primary identifier", "Serial number; fallback: hostname + IP", "", False),
            ("cmdb_ci_vm_instance — primary identifier", "VM UUID (vm_inst_uuid from hypervisor)", "Never use hostname alone for VMs.", False),
            ("cmdb_ci_appl — primary identifier", "Application name + version + host CI sys_id", "", False),
        ]),
        ("Source Precedence Rules", [
            ("Endpoint CIs (cmdb_ci_computer) — source priority", "SCCM SGC > Intune SGC > Discovery", "", False),
            ("Server CIs (cmdb_ci_server) — source priority", "Discovery > manual", "", False),
            ("VM CIs (cmdb_ci_vm_instance) — source priority", "VMware Discovery > manual", "", False),
            ("Application CIs (cmdb_ci_appl) — source priority", "SCCM SGC > Discovery Software pattern", "", False),
        ]),
        ("Auto-Relationship Rules", [
            ("cmdb_ci_computer → End User Computing Technical Service", "Subnet or OU match", "Configured per CMDB-CSDM Service-CI Relationships workbook.", False),
            ("cmdb_ci_server → Server Infrastructure Technical Service", "OS attribute match", "", False),
            ("New CI class auto-creation", "Disabled for out-of-scope classes", "IRE will log but not create records for out-of-scope CI types.", False),
        ]),
    ],
    raci_rows=[
        ("Design IRE identification rules per CI class", "R/A", "I", "ECS Architect."),
        ("Configure source precedence rules", "R/A", "I", "ECS Architect."),
        ("Configure auto-relationship rules", "R/A", "I", "ECS Architect."),
        ("Review IRE reconciliation log after first combined run", "R/A", "C", "ECS reviews; customer validates deduplication results."),
        ("Resolve any IRE conflicts from first run", "R/A", "C", "ECS resolves technical conflicts; customer confirms correct data source.", ),
    ],
    consultant_guide_sections=[
        ("IRE is not optional", "Some customers ask to defer IRE configuration until after Discovery runs. Never agree — running Discovery without IRE configured creates duplicate CIs that are extremely difficult to clean up after the fact. IRE must be configured before the first Discovery run and the first SGC sync."),
        ("Post-run reconciliation review", "After the first combined Discovery + SGC run, export the IRE reconciliation log and look for: (1) duplicate matches resolved — confirm the right record was kept, (2) unresolved duplicates — investigate and resolve manually, (3) out-of-scope CI types found — confirm they were not created. This review takes 1 hour and is the most important quality gate in the Discovery sprint."),
    ],
    adoption_rows=[
        ("We want to migrate all our legacy CI records first, then run Discovery",
         "Run Discovery first. Use legacy data as a reconciliation reference, not a migration source.",
         "Migrating legacy CIs before Discovery creates a polluted baseline that IRE must reconcile against. Discovery-first means every CI is authoritative from day one.",
         "'Your legacy data has value as a checklist — we use it to confirm Discovery found everything. But if we load it into ServiceNow first, Discovery creates duplicates and IRE has to choose which one to keep. Starting clean and validating against your legacy list gives you a trustworthy CMDB from day one.'",
         "Never migrate legacy CIs as a bulk load. Small, strategic manual entries (critical servers not reachable by Discovery) are acceptable with documented rationale."),
    ],
    snmap_sections=[
        ("IRE Tables", [
            ("Identification Rule", "cmdb_identifier_entry", "Defines the CI identifier per class."),
            ("Source Precedence", "cmdb_source_precedence", "Controls which data source wins per attribute."),
            ("Reconciliation Log", "cmdb_reconciliation_log", "Logs all IRE decisions for audit."),
        ]),
    ],
)

def build_readme(out_path):
    doc = EcsDocument(meta=DocMeta(
        eyebrow="ACCELERATOR PACK", title="Discovery\nAccelerator Pack",
        subtitle="MID Server, Discovery scope, credential management, SGC, and IRE configuration for OOTB-first CMDB population",
        org="ECS Federal · ServiceNow Practice",
        audience="Customer IT Operations Manager, Infrastructure Lead, and Network/AD Administrators",
        companion_to="CMDB-CSDM Accelerator Pack · Integration Accelerator Pack",
        doc_id="AP-12", version="1.0", status="Released",
        confidentiality="Shared — for the recipient and their organisation",
        running_header_label="Discovery Accelerator Pack · ECS Federal",
    ))
    doc.add_cover_page(); doc.add_page_break()
    doc.h1("What This Pack Is", numbered=False)
    doc.para("This Accelerator Pack covers the complete Discovery and Service Graph Connector configuration for the OOTB-first ServiceNow engagement. Discovery is the automated mechanism that populates and maintains the CMDB — without it, CI data is manual, stale, and untrustworthy within months of go-live.")
    doc.para("The six workbooks address the full Discovery implementation sequence: scope and IP range definition (Workbook 01), MID Server deployment (Workbook 02), credential management (Workbook 03), Discovery schedule and pattern configuration (Workbook 04), SCCM and Intune Service Graph Connector setup (Workbook 05), and the Identification and Reconciliation Engine rules that prevent duplicates (Workbook 06).")
    doc.h1("The Six Workbooks", numbered=False)
    doc.table(headers=["#", "Workbook", "What It Covers", "Owner", "Sprint"],
        rows=[
            ["01", "Discovery Scope & IP Ranges", "In-scope subnets, exclusions, phasing strategy, device count estimates", "Customer Network Lead", "Sprint 1 Wk 2"],
            ["02", "MID Server Configuration", "VM sizing, placement, installation, firewall rules, validation", "ECS Architect + Customer Infra", "Sprint 1 Wks 1–2"],
            ["03", "Credential Management", "Service accounts, minimum permissions, Credential Store, rotation plan", "ECS Architect + Customer AD/Azure Admin", "Sprint 1 Wk 2"],
            ["04", "Discovery Schedules & Patterns", "Schedule configuration, pattern activation, first run validation", "ECS Architect", "Sprint 2 Wk 1"],
            ["05", "SGC Configuration", "SCCM and Intune SGC setup, sync frequency, IRE deduplication", "ECS Architect + Customer SCCM/Azure Admin", "Sprint 2 Wks 1–2"],
            ["06", "Reconciliation & IRE Rules", "Identification rules, source precedence, auto-relationships, reconciliation review", "ECS Architect", "Sprint 2 Wks 1–2"],
        ])
    doc.h1("Sprint Alignment", numbered=False)
    doc.para("Discovery spans Sprint 1 (preparation) and Sprint 2 (execution). MID Server and credentials must be ready by the end of Sprint 1 — these are the critical path items. If either is delayed, Sprint 2 Discovery is delayed, which delays the CMDB-CSDM relationship mapping and the service impact analysis capability.")
    doc.save(out_path); print(f"README saved: {out_path}")

if __name__ == "__main__":
    OUT = HERE
    print("Building Discovery Accelerator Pack...")
    for content, fname in [(wb1,"01_discovery_scope.xlsx"),(wb2,"02_mid_server_config.xlsx"),(wb3,"03_credential_management.xlsx"),(wb4,"04_discovery_schedules.xlsx"),(wb5,"05_sgc_configuration.xlsx"),(wb6,"06_ire_reconciliation.xlsx")]:
        build_workbook(content, os.path.join(OUT, fname)); print(f"  ✓ {fname}")
    build_readme(os.path.join(OUT, "00_README_Discovery_Pack.docx"))
    print("\nDiscovery Accelerator Pack complete.")
