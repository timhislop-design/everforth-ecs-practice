"""
Build AP-08 — Event Management Foundations Accelerator Pack
6 xlsx workbooks + 1 README docx, branded to the canonical ECS standard.

Workbooks:
  01_event_sources.xlsx           — which monitoring tools will feed ServiceNow
  02_event_rules_baseline.xlsx    — OOTB event rules (dedup, filtering, classification)
  03_alert_promotion_rules.xlsx   — when and how alerts become incidents
  04_ci_correlation_mapping.xlsx  — which CIs are monitored and how they map
  05_mid_server_configuration.xlsx — MID Server setup and connector baseline
  06_operator_workspace_setup.xlsx — alert views, ownership, thresholds
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
TEMPLATES = os.path.join(REPO, "03_Shared", "00_Templates_and_Branding")
sys.path.insert(0, TEMPLATES)

from accelerator_pack_builder import TabContent, build_workbook
from ecs_template import EcsDocument, DocMeta

PACK_NAME = "Event Management Foundations Accelerator Pack"
OUT = HERE


# =============================================================================
# WORKBOOK 1 — Event Sources
# =============================================================================
wb1 = TabContent(
    workbook_title="01 — Event Sources",
    pack_name=PACK_NAME,
    purpose="Defines every monitoring tool that will send events into ServiceNow Event Management at MVP. The event source list is the foundation of the entire Event Management program — every downstream rule, alert, and incident traces back to a source.",
    who_fills="Customer-side: IT Operations lead working with the monitoring/tooling team. ECS facilitates the source prioritisation workshop in Sprint 0.",
    sprint_window="Sprint 0, Week 1–2",
    estimated_effort="4–6 hours including source inventory and connector validation",
    related_workbooks=["02 Event Rules Baseline", "05 MID Server Configuration", "Foundation Data Pack — CIs"],
    success_criteria=[
        "Every active monitoring tool sending event data is listed with a named owner and the data volume estimate.",
        "Source priority (P1 = feeds alerts that could become P1 incidents, P2 = operational, P3 = informational) is assigned to all sources.",
        "MID Server connector type is confirmed for each source (REST, JDBC, Email, custom connector).",
        "Sources with duplicate coverage (e.g., two tools monitoring the same CI) are flagged for consolidation discussion.",
        "Out-of-scope sources (decommission planned within 12 months) are excluded with a note.",
    ],
    process_decisions=[
        ("Which monitoring tools are in scope at MVP?",
         "Start with the tools that generate P1/P2 alert noise today — typically 2–4 tools covering infrastructure, network, and application tiers. Add others in Phase 2.",
         "Customers who onboard every monitoring tool at once overwhelm the event rules build and produce an alert flood that operators ignore. Focus on the tools that matter most for SLA compliance first."),
        ("How will each source authenticate to ServiceNow?",
         "Use REST API (sys_import_set or em_event table endpoint) with a dedicated service account per source. OAuth where the tool supports it.",
         "Shared credentials across sources make audit trails useless and create a single point of credential failure. One service account per source is the OOTB best practice and a security baseline requirement."),
        ("Will sources send raw events or pre-correlated alerts?",
         "Send raw events. ServiceNow Event Management's correlation engine produces the alert layer — pre-correlating in the monitoring tool duplicates logic and prevents ServiceNow from applying its own correlation rules.",
         "Pre-correlated input bypasses the em_event table entirely and arrives as an alert, which means the source's correlation logic overrides ServiceNow's. This breaks the unified operator view and makes the CMDB correlation step meaningless."),
        ("What event volume (events/minute) is expected per source at peak?",
         "Document peak volume per source. Any source exceeding 1,000 events/minute requires dedicated MID Server capacity planning.",
         "Under-provisioned MID Servers are the most common cause of event lag, which delays alert creation, which delays incident creation, which triggers SLA breaches. Volume numbers must be captured now."),
        ("How are out-of-hours events handled — same rules or suppressed?",
         "Use OOTB Event Management maintenance windows (em_maintenance_schedule) to suppress known maintenance events. All other events follow standard rules regardless of time of day.",
         "Time-based suppression at the source level is a trap — it hides real incidents during maintenance windows. Suppress selectively by CI + window, not globally by time."),
        ("What is the retention policy for raw events in the em_event table?",
         "OOTB default is 7 days for raw events and 30 days for alerts. Accept the defaults at MVP; revisit after observing actual volume.",
         "Custom retention is frequently requested but rarely necessary at MVP. The em_event table growth is manageable at default settings for most customers."),
        ("Will the monitoring tools be integrated via MID Server or direct REST?",
         "MID Server for on-premises monitoring tools; direct REST for cloud-native tools that can reach the ServiceNow instance. Hybrid is common and OOTB-supported.",
         "Forcing all sources through MID Server when direct REST is available adds unnecessary latency and a single MID Server becomes a bottleneck. Use the right connector for the source topology."),
        ("Are there SIEM or log aggregation tools (e.g., Splunk) that should also feed events?",
         "Include SIEM/log aggregation tools that generate actionable operational alerts. Exclude log streams that are informational only — these inflate event volume without actionable signal.",
         "Splunk and similar tools can send thousands of informational events per minute. Without pre-filtering at the source, the em_event table fills with noise and operator confidence collapses."),
    ],
    dependencies=[
        ("MID Server installed and registered to ServiceNow instance", "Pending", "ECS", "Sprint 0, Wk 1", "Required before any monitoring tool can send events via MID Server connector"),
        ("Event Management plugin (com.glideapp.itom.snac) activated", "Pending", "ECS", "Sprint 0, Wk 1", "Foundation for all Event Management tables and rules"),
        ("Monitoring tool admin credentials provided for connector configuration", "Pending", "Customer", "Sprint 0, Wk 2", "One set of read-only credentials per tool; ECS will configure the connector"),
        ("Network firewall rules opened: monitoring tool → MID Server → ServiceNow", "Pending", "Customer", "Sprint 0, Wk 1", "ECS to provide port requirements; Customer networking team to execute"),
        ("CMDB CI baseline loaded (Foundation Data Pack)", "Pending", "ECS + Customer", "Sprint 0, Wk 1", "CI correlation requires CIs to exist in the CMDB; cannot correlate events to phantom CIs"),
        ("Peak event volume estimate provided per monitoring tool", "Pending", "Customer", "Sprint 0, Wk 2", "Required for MID Server sizing; ask the monitoring team's ops lead"),
    ],
    config_sections=[
        ("Event Source Registry", [
            ("Total event sources at MVP", "TBD", "Customer to confirm after source inventory workshop", True),
            ("Source naming convention", "TOOL_TIER (e.g., DYNATRACE_APP, SOLARWINDS_NET)", "Consistent naming required — used as source field in em_event and in alert grouping", False),
            ("Primary event table", "em_event", "OOTB; do not redirect to custom table", False),
            ("Source classification field", "source (string)", "Populated by the monitoring tool connector; drives rule filtering", False),
        ]),
        ("Connector Types", [
            ("Dynatrace", "REST API (OOTB Dynatrace connector)", "Supported natively in Event Management; configure in MID Server Extensions", False),
            ("SolarWinds", "REST API via MID Server", "Use the OOTB SolarWinds connector from the ServiceNow Store", False),
            ("Nagios / Icinga", "JDBC or REST via MID Server", "Legacy Nagios uses JDBC polling; Icinga 2 supports REST push", False),
            ("Splunk", "REST push (Splunk Add-on for ServiceNow)", "Customer installs the Splunk add-on; ECS configures the ServiceNow-side receiver", False),
            ("Prometheus / Alertmanager", "REST push via Alertmanager webhook", "Alertmanager sends JSON to em_event REST endpoint; no MID Server required if cloud-to-cloud", False),
            ("Custom / proprietary tool", "JDBC polling or REST via MID Server", "ECS builds a custom connector using the Event Management scripted connector framework", False),
        ]),
        ("Service Account Configuration", [
            ("Service account naming convention", "svc_em_[tool] (e.g., svc_em_dynatrace)", "One dedicated account per source for audit traceability", False),
            ("Required ServiceNow role", "evt_mgmt_integration", "OOTB role; do not grant admin or itil to event integration accounts", False),
            ("Password rotation policy", "90-day rotation; ECS notified 2 weeks before rotation", "Customer to confirm rotation schedule aligns with connector reconfiguration window", True),
        ]),
        ("Volume and Capacity Baseline", [
            ("Expected peak events/minute — all sources combined", "TBD", "Customer to provide; drives MID Server sizing and event retention planning", True),
            ("MID Server CPU/memory recommendation (< 5k events/min)", "4 vCPU / 8 GB RAM", "OOTB recommendation for standard deployments", False),
            ("MID Server CPU/memory recommendation (5k–20k events/min)", "8 vCPU / 16 GB RAM", "Scale MID Server before going live; cannot resize mid-sprint without downtime", False),
            ("High-availability MID Server (> 20k events/min or SLA-critical)", "Clustered MID Servers (2+ nodes)", "Requires MID Server cluster configuration; plan for this in Sprint 0 if volume warrants", False),
        ]),
    ],
    raci_rows=[
        ("Event source inventory (which tools are in scope)", "C", "R", "Customer IT Ops lead owns the list; ECS validates for connector feasibility"),
        ("Source priority classification (P1/P2/P3)", "R", "C", "ECS facilitates; customer confirms based on SLA exposure per tier"),
        ("Monitoring tool credential provisioning", "I", "R", "Customer security team provisions; ECS receives and configures"),
        ("Network firewall rule changes (tool → MID Server → SN)", "I", "R", "Customer networking team owns; ECS provides port specs"),
        ("MID Server connector configuration", "R", "I", "ECS configures each connector; customer validates data flow in the event log"),
        ("Service account creation in ServiceNow", "R", "I", "ECS creates; customer IT security to approve/audit"),
        ("Volume estimation and MID Server sizing sign-off", "R", "C", "ECS sizes based on customer data; customer confirms acceptable risk"),
        ("Out-of-scope source documentation (decommission list)", "C", "R", "Customer owns decommission timeline; ECS documents exclusion rationale"),
    ],
    consultant_guide_sections=[
        ("Event Management Architecture Overview",
         "ServiceNow Event Management sits between monitoring tools and ITSM. The flow is: monitoring tool → em_event (raw event) → event rules (dedup/filter/classify) → em_alert (correlated alert) → alert promotion → incident. Every decision in this workbook affects every stage of that flow. Do not skip the source inventory — trying to build event rules without knowing the sources is like building assignment rules without knowing the groups."),
        ("MID Server Sizing — The Number Customers Get Wrong",
         "Ask for peak events/minute from the monitoring team, not average. Events are not evenly distributed — a network storm, a failed patch, or a cloud region failure can generate 10× the normal volume in under 60 seconds. MID Server queue depth is finite; if it fills, events are dropped silently. There is no dead-letter queue in the OOTB architecture. Size for peak + 20% headroom."),
        ("Common Source Inventory Mistakes",
         "Three patterns that create downstream problems: (1) listing monitoring tools that are decommissioning within 6 months as in-scope — wastes connector build time and creates rule tech debt; (2) including informational log streams alongside operational monitoring — floods the em_event table and destroys operator confidence; (3) missing the SIEM because 'Splunk is log management, not monitoring' — if Splunk generates actionable alerts, it belongs in scope."),
        ("Sprint 0 Sequencing Note",
         "Get the source list locked by end of Sprint 0 Week 1. The event rules workbook (02) cannot be built without a confirmed source list because rules are keyed to the source field. One week of source inventory slippage equals one week of rule-building slippage equals one week of alert configuration slippage. This is the critical path item in Event Management Foundations."),
        ("Connector Validation Checkpoint",
         "Before Sprint 1: validate each connector by sending a test event and confirming it appears in the em_event table. Use the Event Management > Events list view. If a test event does not appear within 60 seconds, the connector is misconfigured — do not proceed to event rules until all sources are validated. A misconfigured source discovered during alert testing costs 3× as long to diagnose."),
    ],
    adoption_rows=[
        ("'We already have alert management in our monitoring tool — why do we need ServiceNow to do it again?'",
         "ServiceNow correlates alerts from all tools into a single operator view, links them to CMDB CIs, and drives automated incident creation — none of which the individual monitoring tool can do across the full stack.",
         "Unified operator experience, CMDB-backed correlation, and SLA-linked incident automation are impossible from a single monitoring tool silo.",
         "'Your monitoring tool is excellent at detecting issues in its domain. ServiceNow is where all those domains meet — it's the single pane of glass your operators use to see the full picture and drive incidents.'",
         "Never for the core flow. Custom dashboards in the monitoring tool for tier-specific views are fine alongside ServiceNow, not instead of it."),
        ("'We want to keep incidents in our legacy ITSM tool and just use ServiceNow for events.'",
         "Event Management's alert promotion creates incidents natively in ServiceNow. Sending promoted alerts to an external ITSM requires custom integration and breaks the OOTB SLA, assignment, and notification chain.",
         "OOTB alert promotion to ServiceNow Incident is a first-class feature. External integration is a custom build that introduces latency and breaks the closed-loop workflow.",
         "'The alert-to-incident promotion is where the ROI lives — automated creation, CMDB-backed assignment, SLA clock starts on promotion. Routing to an external tool means building all of that again outside the platform.'",
         "Only if contractually required and the external ITSM has a ServiceNow-certified integration. Even then, plan for significant limitations."),
        ("'Can we customize the em_event table to add fields specific to our monitoring tools?'",
         "Use the OOTB additional_info (JSON) field on em_event for tool-specific metadata. Do not add columns to em_event — it is a high-volume staging table and schema changes affect indexing and performance.",
         "em_event is a transient staging table, not a record of system. Custom columns on a high-volume transient table create index bloat and performance risk.",
         "'The additional_info field is purpose-built for exactly this — tool-specific metadata that the correlation rules and alert tabs can surface without touching the core schema.'",
         "Never add columns to em_event. If metadata must persist beyond the event, promote it to the alert or incident record via a transform rule."),
        ("'We want event rules to auto-close incidents when the monitoring tool sends a recovery event.'",
         "Use OOTB Alert Closure Rules (em_alert_state_rule) to close alerts on recovery, which then triggers incident resolution via the alert-incident binding. This is fully OOTB.",
         "Auto-resolution is a high-ROI OOTB feature that reduces MTTR and operator burden. It is explicitly in scope for Foundations.",
         "'Good news — this is exactly what OOTB alert closure rules are designed for. We configure the recovery event pattern and the resolution state together in workbook 03.'",
         "No customisation needed. This is a configuration exercise, not a development exercise."),
    ],
    snmap_sections=[
        ("Core Tables", [
            ("Raw event table", "em_event", "High-volume transient table; 7-day default retention"),
            ("Alert table", "em_alert", "Correlated alerts; 30-day default retention; drives the operator workspace"),
            ("Event source table", "em_source", "Registry of configured event sources"),
            ("Maintenance schedule table", "em_maintenance_schedule", "Suppression windows tied to CIs and sources"),
            ("Alert state rule table", "em_alert_state_rule", "Drives alert lifecycle (open → flapping → closed → resolved)"),
        ]),
        ("Key Fields — em_event", [
            ("source", "String — monitoring tool identifier", "Must match the registered em_source name; drives all event rules"),
            ("node", "String — hostname or IP of affected CI", "Used for CMDB CI lookup/correlation; must match ci_identifier strategy"),
            ("type", "String — event category from the tool", "e.g., 'CPU', 'Disk', 'Network'; used in event rule matching"),
            ("severity", "Integer 1–5 (1=Critical)", "OOTB severity scale; monitoring tool severity must be mapped to this scale"),
            ("description", "String", "Alert and incident short description is derived from this field"),
            ("additional_info", "JSON string", "Tool-specific metadata; surfaced in alert tabs via transform; no schema change needed"),
            ("message_key", "String", "Deduplication key; events with the same message_key update the existing alert rather than creating a new one"),
        ]),
        ("OOTB Features Used", [
            ("Event Management Workspace", "Operator-facing unified alert view", "OOTB; no configuration required beyond alert rules"),
            ("Event Correlation Rules", "Groups related alerts into a parent alert", "OOTB scripted rules engine; configured in workbook 02"),
            ("Alert Promotion to Incident", "Auto-creates incident from alert on threshold breach", "Configured in workbook 03; OOTB promotion template"),
            ("MID Server Event Connectors", "Tool-specific data adapters (Dynatrace, SolarWinds, etc.)", "Installed from ServiceNow Store or MID Server Extensions"),
            ("CI Correlation (CMDB lookup)", "Links em_event.node to cmdb_ci.name/ip_address", "Configured via CI Identifier Rules; requires clean CMDB"),
        ]),
    ],
)

# =============================================================================
# WORKBOOK 2 — Event Rules Baseline
# =============================================================================
wb2 = TabContent(
    workbook_title="02 — Event Rules Baseline",
    pack_name=PACK_NAME,
    purpose="Defines the OOTB event rules that filter, deduplicate, classify, and correlate raw events into actionable alerts. Event rules are the intelligence layer between raw monitoring data and the operator-facing alert queue.",
    who_fills="ECS Solution Architect (primary). Customer Monitoring/IT Ops lead validates rule logic against tool-specific event formats in Sprint 0 Week 2.",
    sprint_window="Sprint 0, Week 2 — Sprint 1, Week 1",
    estimated_effort="8–12 hours including rule design, testing, and validation per source",
    related_workbooks=["01 Event Sources", "03 Alert Promotion Rules", "04 CI Correlation Mapping"],
    success_criteria=[
        "At least one deduplication rule (message_key strategy) is defined per event source.",
        "Severity mapping from each monitoring tool's scale to ServiceNow's 1–5 scale is documented and configured.",
        "Noise suppression rules for known informational events (e.g., heartbeat, low-severity disk warnings) are in place.",
        "CI correlation rules are configured and tested with sample events from each source.",
        "Event flood protection (max events/minute threshold) is configured per source.",
        "All rules are documented in this workbook with the ServiceNow rule name for cross-reference.",
    ],
    process_decisions=[
        ("Message key strategy — how will duplicate events be identified?",
         "Use source + node + type as the message_key composite. Events with the same key update the existing alert rather than creating a new one.",
         "Without a dedup strategy, a single monitoring tool can create hundreds of duplicate alerts in minutes during an incident. The message_key is the single most important Event Management configuration decision."),
        ("Severity mapping — how does each tool's severity scale map to ServiceNow's 1–5?",
         "Document the mapping per tool. Most tools use Critical/Major/Minor/Warning/Info — map directly to ServiceNow's 1/2/3/4/5. Tool-specific numeric scales (0–10, etc.) require a transform rule.",
         "Mismatched severity mapping is the most common cause of P1 incidents being created from P3 events, or P1 events being deprioritised. This must be confirmed with the monitoring team for each source."),
        ("What events should be suppressed entirely (never reach an alert)?",
         "Suppress: heartbeat/keep-alive events, scheduled maintenance events, events from decommissioned CIs, events below the agreed noise threshold (e.g., disk > 70% but < 80% on non-production CIs).",
         "The goal is zero-noise for known non-actionable events. Operators who see a noisy queue start ignoring it — and then miss real incidents. Every suppression rule should have a named business justification."),
        ("How will correlated alerts be grouped — by CI, by service, or by event type?",
         "Group by affected service (OOTB Business Service correlation) where service maps exist; fall back to CI grouping. Do not group by event type alone — a CPU and a disk event on the same CI during the same incident should be one alert, not two.",
         "Service-level grouping produces the most useful operator view. CI-level grouping is a good default when service maps are not yet built. Type-level grouping almost always creates more noise, not less."),
        ("What is the alert flapping threshold?",
         "Default OOTB: an alert flaps if it opens and closes more than 3 times in 15 minutes. Accept this default at MVP.",
         "Flapping detection prevents auto-resolution from triggering on transient recovery events (common with network monitoring). The default threshold works for most customers; tune after 30 days of production data."),
        ("Will event rules be version-controlled or managed only in ServiceNow?",
         "Document all rules in this workbook. Export the event rule configuration via Update Set at the end of Sprint 0. Store the Update Set in the project SharePoint/repo.",
         "Event rules are configuration, not code, and therefore not source-controlled by default. The Update Set export is the closest equivalent and must be done before go-live."),
    ],
    dependencies=[
        ("Event sources confirmed and connectors validated (workbook 01)", "Pending", "ECS", "Sprint 0, Wk 2", "Cannot write source-specific rules without confirmed source names and event formats"),
        ("Sample raw event payload provided per source (JSON/XML export)", "Pending", "Customer", "Sprint 0, Wk 2", "ECS needs sample payloads to validate field mapping; 10–20 representative events per source"),
        ("Severity scale documentation from each monitoring tool", "Pending", "Customer", "Sprint 0, Wk 2", "Native severity values (e.g., Dynatrace: AVAILABILITY, ERROR, SLOWDOWN) must be mapped to ServiceNow 1–5"),
        ("List of known informational / heartbeat event types per tool", "Pending", "Customer", "Sprint 0, Wk 2", "Required to build suppression rules; customer monitoring team holds this knowledge"),
        ("CMDB CI baseline loaded for CI correlation testing", "Pending", "ECS", "Sprint 0, Wk 1", "CI correlation rules cannot be tested without CIs in the CMDB"),
        ("Event Management plugin activated and em_event table accessible", "Pending", "ECS", "Sprint 0, Wk 1", "Event rules are configured in the Event Management module — cannot proceed without plugin"),
    ],
    config_sections=[
        ("Deduplication Rules (Message Key Strategy)", [
            ("Composite key fields", "source + node + type", "OOTB default; adjust if tool sends unique identifiers that are more precise", False),
            ("Message key field on em_event", "message_key", "Populated by the event connector transform; must be set before events reach the rules engine", False),
            ("Duplicate suppression window", "60 minutes (OOTB default)", "Events with the same message_key within 60 min update the existing alert; after 60 min a new alert is created", False),
        ]),
        ("Severity Mapping", [
            ("Dynatrace → ServiceNow", "AVAILABILITY=1, ERROR=2, SLOWDOWN=3, RESOURCE_CONTENTION=3, CUSTOM_ALERT=4, INFO=5", "Customer to confirm; Dynatrace event severity varies by monitor type", True),
            ("SolarWinds → ServiceNow", "Critical=1, High=2, Medium=3, Low=4, Informational=5", "Standard SolarWinds severity mapping; confirm against customer SolarWinds alert policies", True),
            ("Nagios / Icinga → ServiceNow", "CRITICAL=1, WARNING=3, UNKNOWN=4, OK=5 (recovery)", "OK state triggers recovery event; used by alert closure rules in workbook 03", True),
            ("Custom/Proprietary tool", "Customer to document", "ECS will build a transform rule based on the documented mapping", True),
        ]),
        ("Suppression Rules", [
            ("Heartbeat / keep-alive events", "Suppress if type = 'heartbeat' OR type = 'keepalive'", "Populate with customer-specific heartbeat event type names from each source", True),
            ("Scheduled maintenance events", "Suppress via em_maintenance_schedule (CI + time window)", "ECS configures; customer provides the maintenance calendar", False),
            ("Below-threshold disk events (non-production)", "Suppress if type = 'disk' AND severity >= 4 AND node NOT IN production CI list", "Customer to confirm non-production CI identification strategy", True),
            ("Decommissioned CI events", "Suppress if CMDB CI status = 'Retired' or CI not found", "Handled by CI correlation rule — events for unknown CIs can be suppressed or routed to a triage alert", False),
        ]),
        ("Correlation Rules", [
            ("Service-level grouping rule", "Group alerts sharing the same business service (cmdb_ci_service) within 10 minutes", "Requires Business Service map to be configured; falls back to CI grouping if service map is absent", False),
            ("CI-level grouping rule", "Group alerts sharing the same CI within 5 minutes", "Default fallback; effective when service maps are not yet built", False),
            ("Storm detection rule", "If > 50 alerts from the same source within 5 minutes, create a single 'Event Storm' parent alert", "Prevents alert flood from overwhelming the operator queue during mass outages", False),
            ("Flapping threshold", "3 open/close cycles within 15 minutes (OOTB default)", "Accept at MVP; tune after 30 days of production data", False),
        ]),
    ],
    raci_rows=[
        ("Message key strategy definition", "R", "C", "ECS designs based on source event structure; customer confirms accuracy"),
        ("Sample event payload provision", "I", "R", "Customer monitoring team provides raw event samples; ECS uses for rule testing"),
        ("Severity scale documentation and mapping approval", "R", "C", "ECS drafts mapping; customer monitoring lead confirms against tool-specific definitions"),
        ("Suppression rule list (heartbeat, maintenance, below-threshold)", "C", "R", "Customer defines what is non-actionable; ECS configures the rules"),
        ("Correlation rule design and configuration", "R", "I", "ECS owns the correlation logic design; customer validates in UAT"),
        ("Event rule testing with live or simulated events", "R", "C", "ECS executes; customer provides test event scenarios and validates outcomes"),
        ("Rule documentation and Update Set export", "R", "I", "ECS documents and exports; stored in project repository"),
        ("Storm detection threshold calibration (post-go-live)", "R", "C", "ECS recommends based on 30-day data; customer approves threshold change"),
    ],
    consultant_guide_sections=[
        ("Event Rules Architecture",
         "There are three layers of rules in ServiceNow Event Management: (1) Event Transform Rules — shape the raw event payload into the em_event record (field mapping, severity translation, message_key population); (2) Event Management Rules — filter, suppress, or classify events before they become alerts; (3) Correlation Rules — group related alerts into a parent alert. Build in this order. Trying to build correlation rules before the lower layers are right is the single most common implementation mistake."),
        ("Message Key — The Most Important Single Configuration Decision",
         "The message_key is what prevents an alert flood. If two events have the same message_key, ServiceNow updates the existing alert instead of creating a new one. If message_key is empty or wrong, every event creates a new alert. For most monitoring tools, source + node + type is the right composite key. For tools that generate unique alert IDs (e.g., Dynatrace problem IDs), use the tool's native ID as the message_key — it is already unique and already deduplicates at the tool level."),
        ("Severity Mapping — Do Not Skip the Workshop",
         "Every monitoring tool uses a different severity vocabulary. Dynatrace uses AVAILABILITY and SLOWDOWN. SolarWinds uses numeric levels. Nagios uses CRITICAL/WARNING/UNKNOWN/OK. Mapping these to ServiceNow's 1–5 scale sounds trivial but takes a full working session with the customer's monitoring team to get right. The consequence of getting it wrong is P1 incidents from P4 events (noise → operator fatigue) or P1 events that arrive as P4 (missed incidents → SLA breach). Do not skip this session."),
        ("Suppression Rules — Start Narrow, Expand",
         "Start with the obvious suppression candidates: heartbeats, scheduled maintenance, known informational events. Do not try to suppress everything the customer thinks is noise on day one — you will suppress real incidents. Build the suppression list from 30 days of production event data in Phase 2 after operators have had time to identify the true noise patterns. The MVP suppression list should cover known non-actionable event types only."),
        ("Testing Protocol",
         "Test each rule type in sequence: (1) send a synthetic event and confirm it appears in em_event; (2) send a duplicate event and confirm the existing alert is updated, not a new one created; (3) send a suppressed event type and confirm it does not produce an alert; (4) send events from two sources for the same CI within 5 minutes and confirm correlation grouping. Document all test results in this workbook."),
    ],
    adoption_rows=[
        ("'We want to build custom event processing rules in a script.'",
         "Use OOTB Event Management Rules (em_event_rule) with condition filters and transform scripts. The scripted rule framework handles 95% of custom logic without leaving the OOTB architecture.",
         "Custom scripts outside the em_event_rule framework bypass the audit trail, cannot be exported as Update Sets, and break in platform upgrades.",
         "'The event rule framework has a full scripting engine built in — you can express almost any logic there without going outside the platform. Show me what the custom script needs to do and we will build it inside the rule.'",
         "Only if the logic genuinely cannot be expressed in the event rule framework — which is rare. Document the justification if customisation is truly needed."),
        ("'Can we just use Transform Maps to process events instead of Event Management rules?'",
         "Use Event Management Rules (em_event_rule), not Transform Maps. Transform Maps process imported records; Event Management Rules process the live event stream. They are different pipelines.",
         "Transform Maps do not have access to the alert lifecycle, the correlation engine, or the CI lookup. Using them for event processing produces a fragmented architecture that cannot be maintained.",
         "'Transform Maps are the right tool for import sets and data loads — not for the live event stream. Event Management rules are the OOTB home for this logic and give you the operator workspace integration for free.'",
         "Never. This is an architecture boundary, not a preference."),
        ("'We need event rules that are different per environment (prod vs. non-prod).'",
         "Use OOTB CI attribute filtering in event rules: check the CI's environment attribute (cmdb_ci.environment) and apply different rule logic. No separate rule sets required.",
         "Separate rule sets per environment double the maintenance burden and cause rules to drift out of sync. Environment-aware filtering within a single rule set is the OOTB best practice.",
         "'The event rule condition builder can filter on any CI attribute, including environment. One rule, environment-aware logic — you get the right behaviour in both environments without doubling the rule count.'",
         "Only if the customer insists on separate rule sets AND has a named owner responsible for keeping both in sync. Document the dual-maintenance risk."),
    ],
    snmap_sections=[
        ("Core Event Rule Tables", [
            ("Event transform rule table", "em_event_rule", "Drives field mapping, severity translation, and message_key population from raw event payload"),
            ("Correlation rule table", "em_correlation_rule", "Groups related em_alert records into a parent alert"),
            ("Message key rule table", "em_message_key_rule", "Defines which fields compose the deduplication key per source"),
            ("Maintenance schedule table", "em_maintenance_schedule", "Suppression windows by CI and/or source"),
            ("Alert state rule table", "em_alert_state_rule", "Drives flapping detection and alert lifecycle transitions"),
        ]),
        ("Key Event Rule Fields", [
            ("Source filter (em_event_rule.source)", "Restricts rule to events from a specific monitoring tool", "Must match the em_source.name exactly"),
            ("Condition (em_event_rule.condition)", "JavaScript condition evaluated against the em_event record", "Full GlideRecord API available within the condition script"),
            ("Transform script (em_event_rule.script)", "JavaScript transform applied to the em_event before alert creation", "Used for severity mapping, field enrichment, CI lookup customisation"),
            ("Priority / order (em_event_rule.order)", "Numeric execution order; lower = first", "Plan rule order carefully — later rules can override earlier transforms"),
        ]),
        ("OOTB Features Used", [
            ("Event Management Rules engine", "Core event processing pipeline", "Handles filter, transform, dedup, and classification"),
            ("CI Identifier Rules", "Resolves em_event.node to a CMDB CI", "Configured separately; required for correlation and alert-to-incident assignment"),
            ("Business Service Correlation", "Groups alerts by affected business service", "Requires Business Service map; delivers the highest-value operator view"),
            ("Alert Flapping Detection", "Detects transient open/close cycling", "OOTB; configured via em_alert_state_rule"),
        ]),
    ],
)

# =============================================================================
# WORKBOOK 3 — Alert Promotion Rules
# =============================================================================
wb3 = TabContent(
    workbook_title="03 — Alert Promotion Rules",
    pack_name=PACK_NAME,
    purpose="Defines when and how alerts automatically promote to incidents. Alert promotion is the ROI moment of Event Management — it replaces manual operator triage with a rules-driven, CMDB-backed incident creation workflow.",
    who_fills="ECS Solution Architect with the Service Desk Manager and IT Operations lead. Promotion thresholds must be jointly agreed — over-promoting creates noise, under-promoting defeats the purpose.",
    sprint_window="Sprint 1, Week 1–2",
    estimated_effort="6–8 hours including threshold design, ITSM field mapping, and test promotion runs",
    related_workbooks=["02 Event Rules Baseline", "04 CI Correlation Mapping"],
    success_criteria=[
        "Promotion criteria (severity level + duration + CI tier) are agreed and documented for all alert types.",
        "Incident field mapping from alert to incident is confirmed (category, subcategory, assignment group, priority).",
        "Auto-resolution rules (recovery event closes alert and resolves incident) are configured and tested.",
        "Incident deduplication (do not create a second incident if one is already open for the same CI + alert) is configured.",
        "Non-promotion scenarios (informational alerts, non-production CIs) are explicitly documented.",
        "Promotion rules are tested end-to-end with synthetic events before go-live.",
    ],
    process_decisions=[
        ("What severity level triggers automatic incident promotion?",
         "Severity 1 (Critical) and Severity 2 (Major) alerts auto-promote. Severity 3 (Minor) promotes only if the alert is open for more than 15 minutes without operator acknowledgement. Severity 4–5 never auto-promote.",
         "Promoting only Severity 1–2 at MVP keeps the incident queue clean. Adding the 15-minute rule for Severity 3 catches unattended medium alerts without flooding the queue with every minor event."),
        ("Should non-production CI alerts ever auto-promote to incidents?",
         "No. Non-production alerts route to a dedicated 'Event Triage' assignment group for manual review. They do not auto-create incidents.",
         "Auto-promoting non-production alerts is the fastest path to operator fatigue. Non-production systems can generate high event volumes during deployments, testing, and patch cycles."),
        ("What incident fields are populated by the promotion rule?",
         "OOTB promotion populates: short_description (from alert.name), description (from alert.description + event details), category/subcategory (from CI class), assignment_group (from CI support group via CMDB), priority (from alert severity), cmdb_ci (from alert.cmdb_ci).",
         "Mapping assignment_group from the CMDB support group is the highest-value promotion field — it routes the incident to the right team automatically without dispatcher intervention."),
        ("What happens when the monitoring tool sends a recovery event?",
         "Recovery event closes the alert. If the incident is still open (not yet resolved by the team), an auto-resolution work note is added and the incident is moved to 'Resolved' with resolution code 'Auto-Resolved by Event Management'.",
         "Auto-resolution is the OOTB feature that closes the loop and reduces MTTR. Do not disable it — it is the most visible ROI metric for Event Management."),
        ("How should duplicate incidents be handled (same CI alerts multiple times before resolution)?",
         "Use OOTB alert-incident binding: if an open incident already exists for the alert's CI, the new alert is linked to the existing incident as a related alert, not promoted to a new incident.",
         "Without duplicate detection, a network storm can create hundreds of incidents for the same CI in minutes. The OOTB binding table (em_alert_task_alert) manages this natively."),
        ("What is the escalation path if an auto-promoted incident is not acknowledged within SLA?",
         "Use standard Incident Management SLA with escalation rules. Event Management promotion does not change the incident SLA workflow — the promoted incident is a standard incident from that point forward.",
         "Do not build a separate escalation path for Event Management incidents. The Incident SLA module handles this correctly for all incidents regardless of origin."),
    ],
    dependencies=[
        ("Event rules baseline configured (workbook 02)", "Pending", "ECS", "Sprint 0, Wk 2", "Promotion rules require alerts to exist; alerts require event rules to be configured first"),
        ("CI support group mapping in CMDB confirmed", "Pending", "Customer + ECS", "Sprint 0, Wk 2", "Assignment group on promoted incidents derives from CMDB CI support_group; must be populated before promotion testing"),
        ("Incident category/subcategory taxonomy agreed (from Incident Management workstream)", "Pending", "Customer", "Sprint 0, Wk 2", "Event Management promotion must map to the agreed incident taxonomy; cannot differ from manually created incidents"),
        ("Non-production CI list confirmed (for non-promotion rule)", "Pending", "Customer", "Sprint 0, Wk 2", "ECS needs the list or CMDB attribute to identify non-production CIs accurately"),
        ("Recovery event type identified per monitoring tool", "Pending", "Customer", "Sprint 0, Wk 2", "Each tool sends recovery differently (Nagios: OK state, Dynatrace: RESOLVED event type); must be confirmed per source"),
    ],
    config_sections=[
        ("Promotion Thresholds", [
            ("Severity 1 (Critical) — auto-promote?", "Yes — immediate on alert creation", "No delay for Critical alerts; the monitoring tool has already determined this is critical", False),
            ("Severity 2 (Major) — auto-promote?", "Yes — immediate on alert creation", "Same logic as Severity 1; Major events have a material service impact", False),
            ("Severity 3 (Minor) — auto-promote?", "Yes — after 15 minutes without acknowledgement", "15-minute window gives operators a chance to review before the system promotes", True),
            ("Severity 4–5 — auto-promote?", "No", "Informational and low-severity alerts do not auto-create incidents at MVP", False),
            ("Non-production CI — auto-promote?", "No — route to Event Triage group for manual review", "Customer to confirm non-production identification attribute (e.g., cmdb_ci.environment = 'Development')", True),
        ]),
        ("Incident Field Mapping", [
            ("short_description", "Derived from alert.name (auto-populated by OOTB promotion template)", "ECS to validate the resulting format matches incident standards", False),
            ("category", "Derived from CI class (cmdb_ci.sys_class_name → category mapping)", "Customer to confirm category taxonomy aligns with Incident Management configuration", True),
            ("subcategory", "Derived from alert event type", "Customer to confirm subcategory mapping per event type", True),
            ("assignment_group", "Derived from CMDB CI support_group field", "Requires support_group to be populated on all in-scope CIs; ECS to validate coverage during CI correlation workbook", False),
            ("priority", "Derived from alert.severity (1=Critical → Priority 1, etc.)", "Consistent with OOTB priority matrix; customer to confirm alignment with Incident Management SLA tiers", False),
            ("cmdb_ci", "Direct link from alert.cmdb_ci (set during CI correlation)", "Requires CI correlation to be working correctly; auto-populates CMDB field on the incident", False),
        ]),
        ("Auto-Resolution Configuration", [
            ("Recovery event type — Nagios/Icinga", "OK", "When Nagios sends OK severity event, OOTB closure rule closes the alert", False),
            ("Recovery event type — Dynatrace", "Event type = RESOLVED (or severity drops to INFO)", "Customer to confirm Dynatrace recovery signal; varies by monitor type", True),
            ("Recovery event type — SolarWinds", "Status = Up or severity = Clear", "Customer to confirm SolarWinds clear/recovery event type name", True),
            ("Incident auto-resolution state", "Resolved (state = 6) with resolution code 'Auto-Resolved'", "Work note added to incident before resolution so the team can see the auto-resolution event", False),
            ("Auto-resolution suppression (critical incidents)", "Do not auto-resolve if incident priority = 1 and caller is VIP group", "Customer to confirm if any incident class should be excluded from auto-resolution", True),
        ]),
        ("Duplicate Detection", [
            ("Alert-incident binding", "OOTB em_alert_task_alert table", "If an open incident exists for the CI, new alert is linked as a related alert, not promoted to a new incident", False),
            ("Open incident lookback window", "Any incident in 'New' or 'In Progress' state for the same CI", "OOTB logic; does not consider incidents in 'Resolved' or 'Closed' state as active", False),
            ("Storm deduplication (>10 alerts from same source in 5 min)", "Route to a single parent 'Event Storm' incident via correlation rule", "Configured in workbook 02 (storm detection rule); referenced here for promotion linkage", False),
        ]),
    ],
    raci_rows=[
        ("Promotion threshold decisions (severity levels, delays)", "R", "C", "ECS facilitates threshold workshop; customer Service Desk Manager and IT Ops lead approve"),
        ("Incident field mapping to agreed ITSM taxonomy", "R", "C", "ECS maps; customer confirms alignment with Incident Management configuration"),
        ("Non-production CI identification and non-promotion rule", "C", "R", "Customer defines non-production boundary; ECS configures the rule"),
        ("Recovery event type confirmation per monitoring tool", "I", "R", "Customer monitoring team confirms; ECS configures the closure rule"),
        ("Auto-resolution configuration and exclusion list", "R", "C", "ECS configures; customer approves exclusion criteria (e.g., P1 VIP incidents)"),
        ("End-to-end promotion testing (synthetic events → incidents)", "R", "C", "ECS executes test runs; customer validates incident quality and assignment accuracy"),
        ("Promotion rule documentation", "R", "I", "ECS documents in this workbook; customer retains for operational runbook"),
    ],
    consultant_guide_sections=[
        ("Why Promotion Rules Are the Hardest Conversation",
         "Every customer wants to auto-promote everything and auto-resolve everything. The tension is: over-promotion trains operators to ignore the incident queue; under-promotion means the team is still manually triaging events. The right threshold is almost always narrower than the customer initially wants. Use production data from the monitoring tools to show current alert volume by severity — that conversation resets expectations faster than any presentation."),
        ("CMDB Support Group Coverage Is the Hidden Dependency",
         "Alert promotion maps the assignment_group from the CMDB CI's support_group field. If support_group is empty on a CI, the promoted incident has no assignment group — it lands in the unassigned queue and defeats the whole purpose. Before Sprint 1 promotion testing, run a report: how many in-scope CIs have an empty support_group? That gap must be closed before go-live."),
        ("Auto-Resolution Is the Metric Customers Will Measure",
         "Track: (1) how many incidents were auto-resolved via Event Management, (2) what percentage of those were legitimate resolutions vs. false positives (monitoring tool said OK but the issue wasn't really fixed). This ratio is what you show in the Sprint demo. A 90%+ legitimate auto-resolution rate is the benchmark for a well-tuned system. Early on, expect 70–80% — it improves as the event rules tighten."),
        ("Testing Sequence",
         "Before go-live: (1) synthetic critical event → confirm alert created → confirm incident created with correct assignment group and category; (2) synthetic recovery event → confirm alert closes → confirm incident resolves with auto-resolution note; (3) second critical event for same CI while incident is open → confirm new alert links to existing incident, not a new one; (4) non-production CI event → confirm no incident is created."),
    ],
    adoption_rows=[
        ("'We want every alert to create an incident — even informational ones.'",
         "Use the OOTB operator workspace for informational alerts; only Critical/Major auto-create incidents. Operators review informational alerts manually and promote if warranted.",
         "Auto-promoting informational alerts fills the incident queue with non-actionable records within hours. Operator confidence collapses and the team starts closing incidents without reading them.",
         "'Let's show you the operator workspace — informational alerts are visible there and a single click promotes to an incident if the operator decides it warrants one. You get full visibility without the queue flood.'",
         "Only if a regulatory requirement mandates an incident record for every event. Even then, use a separate low-priority incident queue with a dedicated assignment group."),
        ("'We want the auto-resolved incident to be Closed, not Resolved.'",
         "Use Resolved (state = 6) for auto-resolution. Closed (state = 7) requires a closure code and caller confirmation in most Incident Management configurations.",
         "OOTB incident workflow requires closure confirmation before reaching Closed state. Bypassing this breaks the Incident SLA closure metric and creates audit gaps.",
         "'Resolved is the right landing state — it signals the monitoring tool confirmed the issue is cleared, the team can review and formally close after confirming there is no follow-up action. Closed without that review step is a governance risk.'",
         "Only if the customer has explicitly removed the closure confirmation step from their Incident workflow AND has a named owner for the audit gap."),
    ],
    snmap_sections=[
        ("Core Promotion Tables", [
            ("Alert promotion rule table", "em_alert_task_rule", "Defines conditions for alert-to-incident promotion"),
            ("Alert-incident binding table", "em_alert_task_alert", "Links alerts to their promoted incidents; drives deduplication"),
            ("Promotion template table", "em_alert_task_template", "Defines default field values for promoted incidents"),
            ("Alert closure rule table", "em_alert_state_rule", "Drives auto-resolution when recovery event arrives"),
        ]),
        ("Key Promotion Fields", [
            ("em_alert.cmdb_ci", "CI linked to the alert (from CI correlation)", "Drives assignment_group, category, and location on the promoted incident"),
            ("em_alert.severity", "1–5 scale (from event rules)", "Primary promotion threshold condition"),
            ("em_alert.state", "Open / Flapping / Closed / Resolved", "Promotion only fires when state = Open; closed/resolved alerts do not re-promote"),
            ("em_alert.task", "Reference to promoted incident (task table)", "Set by the promotion engine; used for deduplication lookup"),
        ]),
        ("OOTB Features Used", [
            ("Alert Promotion Rules", "Conditions and templates for incident creation", "Configured via Event Management > Alert Management > Promotion Rules"),
            ("Alert-Incident Binding", "Deduplication and related-alert linking", "OOTB em_alert_task_alert; no custom code required"),
            ("Alert Closure Rules", "Auto-resolution on recovery event", "Configured via Event Management > Alert Management > Alert State Rules"),
            ("CI Support Group Lookup", "Auto-assignment via CMDB", "Requires CMDB support_group field to be populated on all in-scope CIs"),
        ]),
    ],
)

# =============================================================================
# WORKBOOK 4 — CI Correlation Mapping
# =============================================================================
wb4 = TabContent(
    workbook_title="04 — CI Correlation Mapping",
    pack_name=PACK_NAME,
    purpose="Documents how events from monitoring tools are correlated to CMDB Configuration Items. CI correlation is the bridge between the monitoring world (hostnames, IPs, DNS names) and the ServiceNow CMDB. Without it, alert promotion, auto-assignment, and service impact analysis all fail.",
    who_fills="ECS Solution Architect (primary), with customer CMDB owner validating CI naming conventions and coverage.",
    sprint_window="Sprint 0, Week 2 — Sprint 1, Week 1",
    estimated_effort="6–10 hours including CI identifier rule design, CMDB gap analysis, and correlation testing",
    related_workbooks=["01 Event Sources", "02 Event Rules Baseline", "Foundation Data Pack — CIs"],
    success_criteria=[
        "CI identifier rules are configured for each event source's naming convention (hostname, IP, FQDN, custom tag).",
        "Coverage report shows CI correlation rate ≥ 85% for in-scope monitoring sources at go-live.",
        "Uncorrelated event handling is defined (route to triage queue, not discard).",
        "Business Service maps are either built or explicitly deferred to Phase 2 with a named owner.",
        "CMDB gap analysis (CIs monitored but not in CMDB) is completed and remediation is planned.",
    ],
    process_decisions=[
        ("How does each monitoring tool identify the affected CI — hostname, IP, FQDN, or custom tag?",
         "Document the node field value format per source. Map to the corresponding CMDB attribute (name, ip_address, fqdn, asset_tag).",
         "CI identifier rules match the em_event.node value to a CMDB CI attribute. If the format does not match, correlation fails silently — events are recorded but no CI is linked, which breaks promotion and assignment."),
        ("What is the target CI correlation coverage rate at go-live?",
         "85% or higher. Events without a CI correlation are routed to an 'Uncorrelated Events' assignment group, not discarded.",
         "100% correlation at go-live is rarely achievable because monitoring tools often know about CIs that are not yet in the CMDB. 85% is a realistic MVP target; drive toward 95%+ by end of Phase 2."),
        ("What happens to events that cannot be correlated to a CI?",
         "Route to a designated 'Event Triage' assignment group. Do not discard — uncorrelated events may represent CIs that should be in the CMDB but are not.",
         "Discarding uncorrelated events hides CMDB gaps and means real incidents are never raised for those CIs. The triage queue is the safety net and the CMDB improvement driver."),
        ("Are Business Service maps in scope for Foundations?",
         "Defer Business Service maps to Phase 2 unless a service map already exists in the CMDB. CI-level correlation is the MVP foundation.",
         "Building accurate Business Service maps requires a mature CMDB and stakeholder investment in service topology documentation. Forcing it in Foundations delays go-live without commensurate value."),
        ("How will dynamic infrastructure CIs (cloud VMs, containers, auto-scaled instances) be handled?",
         "Use ServiceNow Discovery or a cloud connector to keep dynamic CI records current. Event Management CI correlation depends on CMDB accuracy for dynamic infrastructure.",
         "Dynamic infrastructure is where CI correlation most commonly fails — a VM spun up after the last Discovery run does not exist in the CMDB. The Discovery workstream must be coordinated with Event Management if cloud or containerised infrastructure is in scope."),
    ],
    dependencies=[
        ("CMDB CI baseline loaded with name, ip_address, and fqdn attributes populated", "Pending", "ECS + Customer", "Sprint 0, Wk 1", "CI correlation requires CI records to exist and have populated identifier attributes"),
        ("Event sources confirmed with node field format documented (workbook 01)", "Pending", "ECS", "Sprint 0, Wk 2", "Cannot configure CI identifier rules without knowing how each tool identifies CIs"),
        ("Business Service map decision made (in scope vs. deferred)", "Pending", "Customer", "Sprint 0, Wk 2", "Service map scope affects correlation rule design; must be decided before Sprint 1"),
        ("Discovery / cloud connector scope confirmed (for dynamic CIs)", "Pending", "Customer + ECS", "Sprint 0, Wk 2", "Dynamic CI coverage must be understood before go-live; gaps mean uncorrelated events for cloud workloads"),
    ],
    config_sections=[
        ("CI Identifier Rules", [
            ("Primary identifier — hostname", "em_event.node → cmdb_ci.name (case-insensitive)", "Works for most on-premises servers; hostname must match exactly", False),
            ("Secondary identifier — IP address", "em_event.node → cmdb_ci.ip_address", "Fallback if hostname match fails; requires IP to be populated on the CI record", False),
            ("Tertiary identifier — FQDN", "em_event.node → cmdb_ci.fqdn", "Used by tools that send fully qualified domain names; common for network devices", False),
            ("Tool-specific tag mapping", "Customer to document", "Some tools (e.g., Dynatrace entity IDs) require a custom attribute on the CI; ECS configures the lookup", True),
            ("Match failure behaviour", "Route to Event Triage assignment group; do not discard", "Uncorrelated events are logged and visible for CMDB remediation", False),
        ]),
        ("CMDB Coverage Baseline", [
            ("In-scope CI count (monitored by at least one source)", "TBD", "Customer to provide or ECS to derive from monitoring tool export", True),
            ("CI records with name populated", "TBD%", "ECS to run CMDB report; target 100% for in-scope CIs", False),
            ("CI records with ip_address populated", "TBD%", "Target 90%+ for servers; lower acceptable for non-IP-addressable CIs", True),
            ("CI records with fqdn populated", "TBD%", "Required for sources that send FQDN; ECS to report coverage", True),
            ("CI records with support_group populated", "TBD%", "Required for auto-assignment on promoted incidents; target 95%+", True),
            ("Target correlation rate at go-live", "≥ 85%", "Track weekly after go-live; drive toward 95%+ by end of Phase 2", False),
        ]),
        ("Business Service Map (Phase 2 Target)", [
            ("Business Service map scope", "Deferred to Phase 2 (unless existing map available)", "If a service map exists, ECS will validate and link to Event Management correlation rules", True),
            ("Phase 2 target service count", "TBD", "Customer to identify top 5–10 services for Phase 2 mapping", True),
            ("Service map source", "Manual mapping or Discovery-derived", "Discovery-derived maps are more accurate but require Discovery to be mature first", True),
        ]),
    ],
    raci_rows=[
        ("Node field format documentation per monitoring tool", "C", "R", "Customer monitoring team documents; ECS uses for identifier rule design"),
        ("CI identifier rule configuration", "R", "I", "ECS configures all CI identifier rules; customer validates in testing"),
        ("CMDB CI coverage gap analysis", "R", "C", "ECS runs the report; customer CMDB owner reviews and confirms remediation plan"),
        ("CMDB attribute population (name, ip, fqdn, support_group)", "C", "R", "Customer CMDB team populates; ECS validates coverage rate"),
        ("Event Triage group creation and staffing", "I", "R", "Customer defines the triage group and assigns members; ECS configures the routing rule"),
        ("Business Service map scope decision (Foundations vs. Phase 2)", "C", "R", "Customer decides; ECS documents the decision and Phase 2 plan"),
        ("CI correlation rate validation (≥ 85% checkpoint)", "R", "C", "ECS measures from em_event data; customer reviews and approves go-live readiness"),
    ],
    consultant_guide_sections=[
        ("CI Correlation Is the Hidden Critical Path Item",
         "CI identifier rules sound simple, but the reality is that monitoring tools and the CMDB evolved independently and use different naming conventions. Dynatrace uses its own entity IDs. SolarWinds uses Node Names that may or may not match the CMDB hostname. Network devices are often in the CMDB by their management IP, not their hostname. Spend an hour with both the monitoring team and the CMDB team together in the same room — it surfaces the naming gaps faster than any analysis."),
        ("The 85% Target and What to Do About the Other 15%",
         "The uncorrelated 15% at go-live is not a failure — it is a CMDB improvement backlog. Every uncorrelated event is evidence of a CI that should be in the CMDB. Track uncorrelated events in the triage queue for 4 weeks, then run a report: what are the top 20 uncorrelated node values? Those become the CMDB remediation list for Phase 2. Show this to the customer as the virtuous cycle: better events → better CMDB → better correlation → better events."),
        ("Dynamic Infrastructure Warning",
         "If the customer runs significant cloud or containerised workloads, CI correlation for those assets requires a real-time Discovery or cloud connector — not a periodic CMDB snapshot. A VM that spins up after the last Discovery run does not exist in the CMDB. Events from that VM are uncorrelated. If the VM hosts a critical service, that means Event Management is blind to it. Flag this explicitly with the customer and ensure the Discovery workstream is coordinated."),
        ("Support Group Coverage Is Mandatory, Not Optional",
         "At least 95% of in-scope CIs must have a support_group populated before go-live. This is not a nice-to-have. An incident promoted from an Event Management alert with no assignment group lands in an unassigned queue and is indistinguishable from a manually created incident with a data entry error. Run the coverage report early in Sprint 0 and give the customer time to remediate."),
    ],
    adoption_rows=[
        ("'Our monitoring tool knows about CIs that are not in the CMDB — can Event Management create CIs automatically?'",
         "No. Event Management correlates events to existing CMDB CIs; it does not create new CI records. Use Discovery or manual import to add missing CIs to the CMDB.",
         "Auto-creating CIs from event data produces low-quality CMDB records with no ownership, no relationships, and no lifecycle data. The CMDB degrades faster than it grows.",
         "'What Event Management can do is show you exactly which node values are failing correlation — that is your missing CI list. Discovery or a quick import fills those gaps properly with full CMDB attributes.'",
         "Never. This is an architectural boundary."),
        ("'Can we skip CI correlation and just use event metadata for incident assignment?'",
         "Use CI correlation and derive assignment from the CMDB. Event metadata routing requires custom scripting and produces brittle assignment logic that breaks when tool configurations change.",
         "CMDB-based assignment is maintainable by the customer's CMDB team without ECS involvement. Metadata-based routing requires a developer to update scripts every time the monitoring tool changes its event format.",
         "'The CMDB approach is self-maintaining — update the support_group on the CI record and the assignment changes everywhere automatically. Let me show you why that is worth the upfront CI coverage work.'",
         "Only if the CMDB is genuinely too immature to populate support_group in time for go-live. Even then, plan to migrate to CMDB-based routing in Phase 2."),
    ],
    snmap_sections=[
        ("CI Identifier Tables", [
            ("CI identifier rule table", "em_ci_identifier_rule", "Defines how em_event.node maps to a CMDB CI; evaluated in priority order"),
            ("CI identifier type table", "em_ci_identifier_type", "Defines the CMDB attribute used for lookup (name, ip_address, fqdn, etc.)"),
            ("Uncorrelated event log", "em_event (where cmdb_ci is empty)", "Used for CMDB gap analysis; query this table weekly in the first 30 days"),
        ]),
        ("Key CI Attributes Required for Correlation", [
            ("cmdb_ci.name", "Primary identifier; must match em_event.node for hostname-based sources", "Case-insensitive match; partial match not supported in OOTB rules"),
            ("cmdb_ci.ip_address", "Secondary identifier for IP-based sources", "IPv4 only in base OOTB; IPv6 requires custom rule"),
            ("cmdb_ci.fqdn", "Tertiary identifier for FQDN-based sources", "Must be fully qualified (e.g., server01.domain.com, not server01)"),
            ("cmdb_ci.support_group", "Required for auto-assignment on promoted incidents", "Must be a valid sys_user_group reference; free-text not supported"),
            ("cmdb_ci.environment", "Used for non-production suppression rule", "Values: Production, Development, Test, Staging; customer to confirm taxonomy"),
        ]),
        ("OOTB Features Used", [
            ("CI Identifier Rules", "Core CI correlation engine", "Configured via Event Management > Administration > CI Identifier Rules"),
            ("Event Triage Assignment Group", "Routing destination for uncorrelated events", "Standard assignment group; created via User Administration > Groups"),
            ("Business Service Map (Phase 2)", "Service-level alert grouping", "Configured via Service Mapping or manual map builder; deferred from Foundations"),
        ]),
    ],
)

# =============================================================================
# WORKBOOK 5 — MID Server Configuration
# =============================================================================
wb5 = TabContent(
    workbook_title="05 — MID Server Configuration",
    pack_name=PACK_NAME,
    purpose="Documents the MID Server installation, configuration, and connector setup that enables on-premises monitoring tools to send events to ServiceNow. The MID Server is the on-premises bridge between customer-side monitoring tools and the ServiceNow cloud instance.",
    who_fills="ECS Solution Architect with customer infrastructure team. MID Server sizing and network configuration require the customer's infrastructure and networking teams.",
    sprint_window="Sprint 0, Week 1",
    estimated_effort="4–8 hours including installation, validation, and connector configuration",
    related_workbooks=["01 Event Sources"],
    success_criteria=[
        "MID Server is installed, registered, and validated (green status in ServiceNow).",
        "All required firewall ports are open and confirmed by the customer networking team.",
        "Each monitoring tool connector is configured and has successfully sent at least one test event.",
        "MID Server sizing is confirmed as adequate for peak event volume.",
        "MID Server HA configuration is in place if required by event volume or SLA.",
    ],
    process_decisions=[
        ("Where will the MID Server be hosted — on-premises server or cloud VM?",
         "On-premises server in the customer's data center, close to the monitoring tools. If the customer runs monitoring tools in a cloud VPC, the MID Server can be a cloud VM in the same VPC.",
         "Network latency between the MID Server and the monitoring tools directly affects event timeliness. Host the MID Server as close to the monitoring tools as possible."),
        ("How many MID Servers are needed?",
         "One MID Server for < 5,000 events/minute. Two or more (clustered) for higher volumes or HA requirements.",
         "A single MID Server is the correct starting point for most customers. Add a second for redundancy only if the SLA for event processing is critical."),
        ("What OS and Java version?",
         "OOTB supported: Windows Server 2016/2019/2022 or RHEL 7/8/9 / Ubuntu 20.04+. Java: OpenJDK 11 (bundled with MID Server installer — do not use a separate JDK).",
         "Using a non-bundled JDK is the most common MID Server installation mistake. Always use the JDK bundled with the ServiceNow MID Server installer."),
        ("Will the MID Server be managed by the customer or ECS?",
         "Customer infrastructure team manages the host OS; ECS configures the MID Server application and connectors. Patching cadence must be agreed: ServiceNow MID Server upgrades are released with every platform upgrade.",
         "MID Server version must match the ServiceNow instance version. If the customer upgrades the instance without upgrading the MID Server, connectors stop working. Set up the auto-upgrade setting in the MID Server configuration."),
    ],
    dependencies=[
        ("Server hardware/VM provisioned for MID Server", "Pending", "Customer", "Sprint 0, Wk 1", "Minimum spec: 4 vCPU / 8 GB RAM / 50 GB disk for standard deployments"),
        ("Firewall rules opened: MID Server → ServiceNow (443/HTTPS outbound)", "Pending", "Customer", "Sprint 0, Wk 1", "MID Server initiates outbound connection to ServiceNow; no inbound rules required from ServiceNow"),
        ("Firewall rules opened: Monitoring tools → MID Server (tool-specific ports)", "Pending", "Customer", "Sprint 0, Wk 1", "ECS to provide port list per monitoring tool connector"),
        ("ServiceNow MID Server user account created with mid_server role", "Pending", "ECS", "Sprint 0, Wk 1", "Required for MID Server registration; dedicated account per MID Server"),
        ("MID Server installer downloaded from ServiceNow instance", "Pending", "ECS", "Sprint 0, Wk 1", "Download from ServiceNow > MID Server > Downloads; version must match instance version"),
    ],
    config_sections=[
        ("MID Server Installation", [
            ("Host OS", "Customer to confirm", "Windows Server 2019/2022 recommended; RHEL 8/9 also supported", True),
            ("Java version", "Bundled OpenJDK 11 (included with installer)", "Do NOT install a separate JDK; always use the bundled version", False),
            ("MID Server service account (OS level)", "svc_midserver (local or domain)", "Minimal OS permissions: read/write to MID Server install directory only", False),
            ("MID Server ServiceNow account", "svc_mid_[environment] with mid_server role", "One account per MID Server; do not share credentials across MID Servers", False),
            ("Auto-upgrade enabled", "Yes", "Ensures MID Server version stays in sync with ServiceNow upgrades automatically", False),
            ("Install directory", "C:\\ServiceNow\\MID (Windows) or /opt/servicenow/mid (Linux)", "Consistent naming for all MID Servers in the environment", False),
        ]),
        ("Network Configuration", [
            ("MID Server → ServiceNow (outbound)", "TCP 443 (HTTPS)", "MID Server initiates; no inbound connection from ServiceNow required", False),
            ("Monitoring tool → MID Server (inbound)", "Tool-specific; see connector documentation", "Customer networking team to open per the port list ECS provides", True),
            ("MID Server → Monitoring tool (outbound polling, if applicable)", "Tool-specific; JDBC tools require outbound from MID Server", "Required only for polling-based connectors (JDBC, SNMP); push-based connectors do not require this", False),
            ("Proxy server required?", "Customer to confirm", "If MID Server reaches ServiceNow via proxy, configure proxy settings in config.xml", True),
        ]),
        ("Connector Configuration", [
            ("Dynatrace connector", "OOTB Dynatrace connector (ServiceNow Store)", "Configure in MID Server > Extensions; requires Dynatrace API token", False),
            ("SolarWinds connector", "OOTB SolarWinds connector (ServiceNow Store)", "Requires SolarWinds Orion REST API enabled and a read-only API credential", False),
            ("Nagios / Icinga connector", "JDBC polling or Nagios Event Broker plugin", "Confirm connector type based on Nagios version; Icinga 2 supports REST push", False),
            ("Custom connector", "MID Server scripted connector (EventSource application)", "ECS builds using the OOTB EventSource framework; documented in Consultant Guide tab", False),
        ]),
    ],
    raci_rows=[
        ("Server/VM provisioning for MID Server", "I", "R", "Customer infrastructure team provisions; ECS provides minimum spec"),
        ("Firewall rule implementation", "I", "R", "Customer networking team executes; ECS provides port specifications"),
        ("MID Server installation and registration", "R", "I", "ECS installs and registers; customer infrastructure team validates OS-level access"),
        ("ServiceNow MID Server user account creation", "R", "I", "ECS creates the ServiceNow account; customer IT security to approve"),
        ("Monitoring tool connector configuration", "R", "C", "ECS configures each connector; customer monitoring team validates data flow"),
        ("MID Server validation (green status + test event)", "R", "C", "ECS validates; customer confirms test events appear in em_event table"),
        ("Auto-upgrade configuration", "R", "I", "ECS configures; customer infrastructure team informed of upgrade behaviour"),
        ("Ongoing MID Server host OS maintenance (patching, monitoring)", "I", "R", "Customer infrastructure team owns OS-level maintenance; ECS owns the MID Server application"),
    ],
    consultant_guide_sections=[
        ("MID Server Is Sprint 0 Day 1",
         "Nothing in Event Management works without the MID Server being up, registered, and green. Treat it as the first task in Sprint 0, before event rules, before alert configuration, before anything. If the customer's networking or infrastructure team is slow, this becomes the critical path blocker for the entire Event Management workstream."),
        ("The Bundled JDK Rule",
         "It sounds like a trivial implementation detail, but customers who install their own JDK instead of the bundled one account for a disproportionate share of MID Server issues. The bundled JDK is tested by ServiceNow against the platform version. Separately installed JDKs drift in patch version and create intermittent TLS and SSL handshake failures that are hard to diagnose. Enforce this rule at installation time."),
        ("Auto-Upgrade Is Not Optional",
         "The MID Server must stay in sync with the ServiceNow instance version. If auto-upgrade is disabled and the customer upgrades the instance, the MID Server stops processing events silently — no error in the UI, just an empty em_event table. Turn on auto-upgrade and verify it is working before go-live."),
        ("Connector Validation Protocol",
         "After configuring each connector: (1) send a test event from the monitoring tool (most tools have a 'send test alert' button); (2) immediately check Event Management > Events in ServiceNow; (3) the test event should appear within 60 seconds. If it does not appear, check: MID Server status (green?), firewall rules (is the port open?), connector credentials (are they valid?), em_event source field (does it match the expected source name?). Do not proceed to event rules until all connectors are validated."),
    ],
    adoption_rows=[
        ("'Can we skip the MID Server and send events directly from monitoring tools via REST?'",
         "Yes for cloud-native tools that can reach the ServiceNow instance directly (direct REST to the em_event endpoint). No for on-premises monitoring tools that cannot reach ServiceNow directly.",
         "Direct REST is valid for cloud-to-cloud. On-premises tools behind a firewall cannot typically reach ServiceNow directly — the MID Server bridges the gap.",
         "'If the tool can reach ServiceNow directly, absolutely — we will configure direct REST and skip the MID Server for that source. Let us check the network topology for each tool and use the right connector for each one.'",
         "Yes, for cloud-native sources with direct internet access to ServiceNow. Document which sources use direct REST vs. MID Server."),
        ("'We want to install the MID Server on the same server as the monitoring tool.'",
         "Avoid collocating the MID Server with the monitoring tool. The MID Server is a JVM process that competes for CPU and memory, which can impact monitoring tool performance during event storms.",
         "During a network storm or major outage, the monitoring tool generates maximum event volume at exactly the same time as the MID Server is most stressed. Collocated deployments fail at the worst possible moment.",
         "'We strongly recommend a dedicated host — even a small VM. The MID Server and the monitoring tool both spike under load at the same time, which is when you least want resource contention.'",
         "Only if a dedicated host is genuinely impossible. Document the risk and add MID Server host resource monitoring to the monitoring tool's own alert scope."),
    ],
    snmap_sections=[
        ("MID Server Tables", [
            ("MID Server table", "ecc_agent", "Registry of registered MID Servers and their status"),
            ("MID Server parameter table", "ecc_agent_ext", "Configuration parameters per MID Server (proxy, auto-upgrade, etc.)"),
            ("MID Server queue (inbound)", "ecc_queue (queue = input)", "Events from monitoring tools arrive here before processing"),
            ("MID Server queue (outbound)", "ecc_queue (queue = output)", "Commands sent from ServiceNow to MID Server"),
        ]),
        ("Key MID Server Configuration Files", [
            ("config.xml", "Primary MID Server configuration file", "Contains ServiceNow instance URL, credentials, proxy settings, and extension configurations"),
            ("wrapper.conf", "JVM heap settings", "Default heap: -Xmx512m; increase to -Xmx2048m for high-volume deployments"),
            ("extensions/ directory", "Connector extension files", "Monitoring tool connectors installed as extension JARs or scripts in this directory"),
        ]),
        ("OOTB Features Used", [
            ("MID Server Extensions", "Monitoring tool connectors", "Installed from ServiceNow Store or MID Server Extensions module"),
            ("MID Server Cluster", "HA configuration for high-volume deployments", "Configured via MID Server cluster properties; load balances event processing across nodes"),
            ("Auto-Upgrade", "Keeps MID Server version in sync with instance", "Configured via ecc_agent_ext parameter 'mid.auto_upgrade.enabled'"),
        ]),
    ],
)

# =============================================================================
# WORKBOOK 6 — Operator Workspace Setup
# =============================================================================
wb6 = TabContent(
    workbook_title="06 — Operator Workspace Setup",
    pack_name=PACK_NAME,
    purpose="Defines the Event Management Operator Workspace configuration — alert views, ownership assignment, notification rules, and the daily operational workflow for the team who will manage alerts post-go-live.",
    who_fills="ECS Solution Architect with the Service Desk Manager and designated Event Management operators. Workspace configuration must be validated by the actual operators, not only by management.",
    sprint_window="Sprint 1, Week 2 — Sprint 2, Week 1 (validated in UAT)",
    estimated_effort="4–6 hours including workspace configuration, view design, and operator walkthrough",
    related_workbooks=["03 Alert Promotion Rules", "04 CI Correlation Mapping"],
    success_criteria=[
        "Operator Workspace is accessible to all designated operators with the correct role assignment.",
        "Alert views are configured with the agreed filter sets (by priority, by assignment group, by service).",
        "Alert ownership and escalation workflow is defined and documented.",
        "Notification rules (alert created, alert severity changed, alert promoted) are configured and tested.",
        "Operators have completed a 60-minute walkthrough of the workspace before go-live.",
        "A daily operational runbook is produced from this workbook for the operators to reference.",
    ],
    process_decisions=[
        ("Who are the designated Event Management operators at go-live?",
         "Identify by name. Minimum: one primary operator per shift (or on-call rotation) and a named backup. Do not rely on a generic 'monitoring team' — unnamed operators are no operators.",
         "The most common Event Management go-live failure is having the workspace configured correctly but no one accountable for watching it. Name the operators before go-live, not after."),
        ("What alert views are needed?",
         "Three OOTB views at minimum: (1) All Open Alerts (by severity); (2) My Assignment Group Alerts; (3) Unacknowledged Critical/Major Alerts. Add service-level views if Business Service maps are in scope.",
         "Avoid creating more than 5–6 views at MVP — operators who cannot decide which view to use default to none of them."),
        ("What is the alert acknowledgement SLA?",
         "Critical (Severity 1): acknowledge within 5 minutes. Major (Severity 2): acknowledge within 15 minutes. Minor (Severity 3): acknowledge within 60 minutes.",
         "Acknowledgement SLA drives the flapping/escalation thresholds in workbook 02. The values must be consistent across both workbooks."),
        ("How will operators be notified of new Critical/Major alerts outside business hours?",
         "Use OOTB Event Management notification rules to send email and/or SMS on Severity 1/2 alert creation. Integrate with on-call roster (PagerDuty, OpsGenie, or ServiceNow On-Call) if available.",
         "Email alone is insufficient for out-of-hours critical alerts. Confirm the on-call notification mechanism before go-live."),
        ("Will operators use the OOTB Event Management Workspace or the classic Alerts list?",
         "OOTB Event Management Workspace (Event Management > Workspace). The classic Alerts list view is retained for administrative purposes but operators should work from the Workspace.",
         "The Workspace provides the operator-centric view with grouped alerts, CI context, and one-click incident promotion. The classic list view is for configuration and reporting, not for daily operations."),
    ],
    dependencies=[
        ("Alert promotion rules configured (workbook 03)", "Pending", "ECS", "Sprint 1, Wk 1", "Workspace shows promoted incidents alongside alerts; requires promotion to be working"),
        ("Operator user accounts created with evt_mgmt_operator role", "Pending", "ECS + Customer", "Sprint 1, Wk 2", "Operators need evt_mgmt_operator role; Service Desk Manager needs evt_mgmt_admin"),
        ("On-call roster / notification integration confirmed (PagerDuty, OpsGenie, etc.)", "Pending", "Customer", "Sprint 1, Wk 2", "Required for out-of-hours critical alert notifications; customer to confirm tooling"),
        ("Alert views agreed with designated operators", "Pending", "ECS + Customer", "Sprint 1, Wk 2", "Views must be designed with the actual operators, not only management"),
    ],
    config_sections=[
        ("Role Assignment", [
            ("Event Management operator role", "evt_mgmt_operator", "All designated operators receive this role; grants access to Workspace and alert acknowledgement", False),
            ("Event Management admin role", "evt_mgmt_admin", "Service Desk Manager and ECS; grants access to rule configuration and workspace administration", False),
            ("Event Management integration role", "evt_mgmt_integration", "Monitoring tool service accounts only; no human users should have this role", False),
            ("Designated operators at go-live", "Customer to name", "List all named operators before go-live; unnamed = no coverage", True),
        ]),
        ("Alert Views", [
            ("View 1 — All Open Alerts (by severity)", "Filter: state = Open, sorted by severity ASC, then created DESC", "Default view; shows the most critical unresolved alerts first", False),
            ("View 2 — My Assignment Group", "Filter: assignment_group IN (current user's groups), state = Open", "Operator-specific view; each operator sees only their team's alerts", False),
            ("View 3 — Unacknowledged Critical/Major", "Filter: severity IN (1,2), acknowledged = false, state = Open", "Escalation view; used by the Service Desk Manager to identify missed critical alerts", False),
            ("View 4 — Service-Level (Phase 2)", "Filter: business_service = [service name]", "Deferred until Business Service maps are built in Phase 2", False),
        ]),
        ("Notification Rules", [
            ("Critical alert created", "Email + on-call notification to primary operator and backup within 60 seconds of alert creation", "Severity 1 only; immediate notification regardless of time of day", False),
            ("Major alert created (business hours)", "Email to assignment group within 2 minutes of alert creation", "Severity 2 during business hours; on-call notification outside business hours", False),
            ("Alert unacknowledged at SLA breach", "Escalation email to Service Desk Manager + on-call backup", "Drives escalation without manual monitoring of the workspace", False),
            ("Alert auto-resolved", "Work note on linked incident + email to incident assignee", "Closes the loop for the incident team; confirms the monitoring tool sent a recovery signal", False),
            ("On-call integration (if applicable)", "Customer to confirm: PagerDuty, OpsGenie, or ServiceNow On-Call", "ECS configures the integration based on customer's on-call tooling", True),
        ]),
        ("Acknowledgement SLA", [
            ("Severity 1 (Critical) acknowledgement window", "5 minutes", "Triggers escalation notification if not acknowledged within 5 minutes", False),
            ("Severity 2 (Major) acknowledgement window", "15 minutes", "Consistent with Incident SLA Priority 2 response time", False),
            ("Severity 3 (Minor) acknowledgement window", "60 minutes", "Lower urgency; operators review at next check-in", False),
        ]),
    ],
    raci_rows=[
        ("Operator identification and role assignment", "I", "R", "Customer Service Desk Manager names operators; ECS assigns roles in ServiceNow"),
        ("Alert view design (agreed with operators)", "R", "C", "ECS designs initial views; operators validate and request adjustments"),
        ("Notification rule configuration", "R", "C", "ECS configures; customer confirms notification recipients and on-call integration"),
        ("On-call integration setup (PagerDuty, OpsGenie, etc.)", "C", "R", "Customer owns on-call tooling; ECS provides the ServiceNow webhook configuration"),
        ("Acknowledgement SLA definition", "C", "R", "Customer Service Desk Manager defines SLA targets; ECS configures the escalation rules"),
        ("Operator walkthrough and workspace training", "R", "I", "ECS leads the 60-minute walkthrough; all designated operators must attend"),
        ("Post-go-live workspace optimisation (30-day review)", "R", "C", "ECS reviews view usage and notification noise at 30 days; customer approves adjustments"),
    ],
    consultant_guide_sections=[
        ("The Workspace Is Where Adoption Lives or Dies",
         "A technically perfect Event Management implementation fails if operators do not use the workspace. The workspace training session is not optional — it is the moment where the operators either adopt the tool or find workarounds (usually: keep using their old monitoring tool dashboards). Spend time in the workspace with the operators before go-live. Let them configure their own views. Answer the 'why would I use this instead of what I already have?' question honestly."),
        ("Alert Fatigue Is the Enemy",
         "The workspace must show operators only what they need to act on. If the default view has 500 open alerts, operators will ignore the workspace. The acknowledgement SLA, the suppression rules (workbook 02), and the promotion thresholds (workbook 03) all contribute to alert fatigue. Run a 2-week pilot with real events before go-live and count: how many alerts are in the operator's view at any given time? Target < 20 open, unacknowledged alerts in the primary view at any given time during normal operations."),
        ("Named Operators Before Go-Live",
         "This seems obvious but frequently gets deferred. 'The monitoring team will handle it' is not a named operator. Get the Service Desk Manager to name the primary operator and backup per shift, assign the evt_mgmt_operator role to those individuals, and confirm they have completed the workspace walkthrough. Document this in the Operator Runbook."),
        ("Operator Runbook",
         "Produce a 2-page daily operations runbook from this workbook before go-live. Contents: (1) how to log into the Workspace; (2) which view to check first; (3) how to acknowledge an alert; (4) how to manually promote an alert to an incident; (5) how to handle an alert storm; (6) who to escalate to if the workspace is down. The runbook lives in the project SharePoint alongside the workbook."),
    ],
    adoption_rows=[
        ("'We will keep using our monitoring tool dashboards and only use ServiceNow for incidents.'",
         "Use the Event Management Workspace as the primary operational view. Monitoring tool dashboards are still available for tool-specific deep-dive, but the ServiceNow workspace is the single pane of glass for cross-tool operations.",
         "If operators continue to live in the monitoring tool dashboards, the alert acknowledgement and escalation workflow breaks. The workspace provides the cross-tool view that no individual monitoring tool can provide.",
         "'Your monitoring tool dashboards are excellent for deep-diving into a specific tool's metrics — keep them. The ServiceNow workspace gives you the view across all of your tools together, which is the view you need when something is actually on fire.'",
         "Only if the customer has a single monitoring tool and does not expect to add more. Even then, the workspace provides the incident linkage that the monitoring tool cannot."),
        ("'Can we build a custom portal for our operators instead of using the OOTB workspace?'",
         "Use the OOTB Event Management Workspace. It receives ServiceNow product investment with every release. Custom portals become orphaned after the first platform upgrade.",
         "Custom portals require ongoing maintenance as the Event Management data model evolves. The OOTB workspace gains new features (AI-assisted correlation, topology maps, etc.) in every release — custom portals miss all of it.",
         "'The OOTB workspace has come a long way — let me show you the current version. If there is something specific it cannot do, we can look at whether it is on the roadmap before we decide to build around it.'",
         "Only if there is a documented accessibility requirement the OOTB workspace cannot meet. Even then, consider Service Portal as a lighter alternative to a fully custom portal."),
    ],
    snmap_sections=[
        ("Workspace Tables", [
            ("Operator workspace configuration", "em_workspace_config", "Defines workspace layout, available widgets, and default view"),
            ("Alert view table", "em_alert_view", "Custom alert filter views accessible from the workspace"),
            ("Notification rule table", "sysevent_email_action (for email) + em_notification_rule", "Event Management-specific notification rules; reference via em_alert event triggers"),
        ]),
        ("Required Roles", [
            ("evt_mgmt_operator", "Alert acknowledgement, manual promotion, workspace access", "Assign to all designated Event Management operators"),
            ("evt_mgmt_admin", "Workspace administration, view management, rule access", "Assign to Service Desk Manager and ECS during implementation"),
            ("evt_mgmt_integration", "Event ingestion only (monitoring tool service accounts)", "No human users; monitoring tool service accounts only"),
        ]),
        ("OOTB Features Used", [
            ("Event Management Workspace", "Primary operator interface for alert management", "Event Management > Workspace; mobile-accessible via the ServiceNow mobile app"),
            ("Alert Acknowledgement", "Marks an alert as being reviewed by an operator", "Stops the acknowledgement SLA escalation timer"),
            ("Manual Incident Promotion", "One-click promotion from alert to incident within the Workspace", "Available for Severity 3–5 alerts not covered by auto-promotion rules"),
            ("Workspace Notification Rules", "Real-time notifications for alert lifecycle events", "Configured via Event Management > Administration > Notification Rules"),
        ]),
    ],
)


# =============================================================================
# README docx
# =============================================================================
def build_readme():
    meta = DocMeta(
        eyebrow="ECS Federal · ServiceNow Practice",
        title="Event Management Foundations\nAccelerator Pack",
        subtitle="AP-08 — Sprint 0–1 Configuration Workbooks",
        audience="Internal · Shared with Customer",
        version="1.0",
        doc_id="AP-08",
        companion_to="AP-09 Event Management Realization Pack · INT-HT-18 How-To Guide (pending) · CLT-WP-Event Workshop Pre-Read (pending)",
    )
    doc = EcsDocument(meta)

    doc.h1("About This Pack")
    doc.para(
        "The Event Management Foundations Accelerator Pack contains six Excel workbooks that guide the "
        "ECS team and the customer through every configuration decision required to stand up ServiceNow "
        "Event Management at MVP. Each workbook maps to a discrete configuration layer — from event "
        "sources and MID Server through event rules, CI correlation, alert promotion, and the operator "
        "workspace — following the same eight-tab structure used across all ECS accelerator packs."
    )

    doc.h1("Pack Contents")
    doc.table(
        headers=["#", "Workbook", "Primary Owner", "Sprint Window"],
        rows=[
            ["01", "Event Sources", "ECS + Customer IT Ops", "Sprint 0, Wk 1–2"],
            ["02", "Event Rules Baseline", "ECS Solution Architect", "Sprint 0, Wk 2 – Sprint 1, Wk 1"],
            ["03", "Alert Promotion Rules", "ECS + Service Desk Manager", "Sprint 1, Wk 1–2"],
            ["04", "CI Correlation Mapping", "ECS + Customer CMDB Owner", "Sprint 0, Wk 2 – Sprint 1, Wk 1"],
            ["05", "MID Server Configuration", "ECS + Customer Infrastructure", "Sprint 0, Wk 1"],
            ["06", "Operator Workspace Setup", "ECS + Designated Operators", "Sprint 1, Wk 2 – Sprint 2, Wk 1"],
        ]
    )

    doc.h1("Non-Negotiable Prerequisites")
    doc.para(
        "Event Management Foundations has four hard dependencies that must be confirmed before Sprint 0 "
        "begins. Without all four, the workstream stalls immediately."
    )
    doc.table(
        headers=["#", "Prerequisite", "Owner", "What Happens Without It"],
        rows=[
            ["1", "Event Management plugin activated (com.glideapp.itom.snac)", "ECS", "All Event Management tables and rules are unavailable"],
            ["2", "MID Server provisioned and network ports confirmed open", "Customer Infra + ECS", "No monitoring tool can send events to ServiceNow"],
            ["3", "CMDB CI baseline loaded (Foundation Data Pack)", "ECS + Customer", "CI correlation fails; all events are uncorrelated"],
            ["4", "Monitoring tool admin credentials for connector config", "Customer Security", "MID Server connectors cannot authenticate to the monitoring tools"],
        ]
    )

    doc.h1("How to Use These Workbooks")
    doc.para(
        "Start with workbook 05 (MID Server Configuration) and workbook 01 (Event Sources) in parallel — "
        "these are Sprint 0 Week 1 activities and are on the critical path. Workbook 04 (CI Correlation) "
        "runs in parallel with workbook 02 (Event Rules) because CI identifier rules and event rules are "
        "independent configuration tracks. Workbook 03 (Alert Promotion) depends on event rules being "
        "stable. Workbook 06 (Operator Workspace) is the final layer, configured in Sprint 1 Week 2 "
        "and validated in UAT."
    )
    doc.para(
        "Each workbook follows the standard eight-tab structure: Instructions → Process Decisions → "
        "Dependencies → Configuration Data → Roles & Responsibilities → Consultant Guide → "
        "Adoption vs Re-engineering → ServiceNow Mapping. The yellow-shaded cells in Configuration "
        "Data are the customer's inputs; all other cells are ECS-owned."
    )

    doc.h1("Companion Artifacts")
    doc.para(
        "This pack pairs with AP-09 (Event Management Realization Accelerator Pack), which covers the "
        "advanced configuration layer: service impact analysis, topology maps, event storm management, "
        "and AIOps integration. The internal consultant guide (INT-HT-18) and the customer-facing "
        "workshop pre-read are produced in the same build window as this pack."
    )

    doc.h1("Metrics to Track at Go-Live")
    doc.table(
        headers=["Metric", "Target", "Source"],
        rows=[
            ["CI correlation rate", "≥ 85%", "em_event where cmdb_ci is empty / total events"],
            ["Alert-to-incident promotion rate (Sev 1/2)", "100%", "em_alert where severity IN (1,2) and task IS NOT NULL"],
            ["Auto-resolution rate", "≥ 70% of promoted incidents", "Incidents resolved with resolution_code = 'Auto-Resolved'"],
            ["Alert acknowledgement within SLA", "≥ 90%", "em_alert where acknowledged within SLA window"],
            ["Mean time to alert (event → alert)", "< 60 seconds", "em_alert.opened_at − em_event.created"],
        ]
    )

    out_path = os.path.join(OUT, "00_README_Event_Management_Foundations_Pack.docx")
    doc.save(out_path)
    print(f"  README → {out_path}")


# =============================================================================
# BUILD
# =============================================================================
if __name__ == "__main__":
    print("Building AP-08 — Event Management Foundations Accelerator Pack")
    print("="*65)

    workbooks = [
        (wb1, "01_event_sources.xlsx"),
        (wb2, "02_event_rules_baseline.xlsx"),
        (wb3, "03_alert_promotion_rules.xlsx"),
        (wb4, "04_ci_correlation_mapping.xlsx"),
        (wb5, "05_mid_server_configuration.xlsx"),
        (wb6, "06_operator_workspace_setup.xlsx"),
    ]

    for content, filename in workbooks:
        path = os.path.join(OUT, filename)
        build_workbook(content, path)
        print(f"  ✓ {filename}")

    build_readme()
    print("  ✓ 00_README_Event_Management_Foundations_Pack.docx")
    print("="*65)
    print("AP-08 complete — 6 workbooks + 1 README built.")
