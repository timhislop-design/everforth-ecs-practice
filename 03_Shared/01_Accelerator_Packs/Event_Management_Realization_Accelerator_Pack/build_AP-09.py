"""
Build AP-09 — Event Management Realization Accelerator Pack
8 xlsx workbooks + 1 README docx.

Workbooks:
  01_service_health_maps.xlsx         — Business Service maps, health scoring, topology
  02_storm_management.xlsx            — Event storm detection, flood control, at-scale dedup
  03_aiops_integration.xlsx           — ML-based noise reduction, predictive correlation
  04_alert_intelligence.xlsx          — OOTB alert classification, similar alert suggestions
  05_remediation_workflows.xlsx       — Auto-remediation, runbook automation triggers
  06_advanced_correlation.xlsx        — Multi-source parent-child alert chains
  07_analytics_and_kpis.xlsx          — PA dashboards, event management KPIs
  08_hypercare_and_maturity.xlsx      — 30/60/90-day tuning, operator maturity framework
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
TEMPLATES = os.path.join(REPO, "03_Shared", "00_Templates_and_Branding")
sys.path.insert(0, TEMPLATES)

from accelerator_pack_builder import TabContent, build_workbook
from ecs_template import EcsDocument, DocMeta

PACK_NAME = "Event Management Realization Accelerator Pack"
OUT = HERE


# =============================================================================
# WORKBOOK 1 — Service Health Maps
# =============================================================================
wb1 = TabContent(
    workbook_title="01 — Service Health Maps",
    pack_name=PACK_NAME,
    purpose=(
        "Defines the Business Service map configuration that enables service-level alert grouping, "
        "service health scoring, and stakeholder-facing health dashboards. Service Health Maps are "
        "the bridge between CI-level event noise and business-outcome reporting."
    ),
    who_fills=(
        "ECS Solution Architect with customer Service Owners and CMDB team. "
        "Service scope and CI membership must be confirmed by the service owner, not ECS alone."
    ),
    sprint_window="Sprint 3–4 (after CI correlation rate ≥ 85% from AP-08)",
    estimated_effort="8–12 hours including service scoping, map build, and health score calibration",
    related_workbooks=["AP-08 Workbook 04 — CI Correlation Mapping", "CMDB CSDM Pack", "Foundation Data Pack"],
    success_criteria=[
        "Top 10 business services have confirmed CI membership and a named service owner.",
        "Service Health Score thresholds (Operational / Degraded / Critical) are agreed and configured.",
        "Service health dashboard is accessible to service owners with no custom development.",
        "Alert grouping by business service is working: related CI alerts roll up to the service-level parent.",
        "At least one end-to-end service impact scenario is tested (CI alert → service health change → stakeholder notification).",
    ],
    process_decisions=[
        ("Which business services are in scope for Phase 1 health maps?",
         "Start with the 5–10 services that are most sensitive to IT events — typically services that are covered by SLAs, have executive sponsors, or have the highest incident volume. Build maps for others in Phase 2.",
         "Mapping every service at once overwhelms the workshop and produces low-quality maps. The first 5–10 maps, done well, build the template for everything that follows."),
        ("What is the health scoring model — availability only, or a composite score?",
         "OOTB Service Health uses a composite model: critical CIs degrade health more than non-critical CIs, and the number of degraded CIs relative to total CI count drives the health percentage. Accept the OOTB model at MVP.",
         "Custom health scoring algorithms are rarely needed and create upgrade risk. The OOTB model is transparent, configurable, and defensible to stakeholders."),
        ("Should service health trigger notifications to business stakeholders?",
         "Yes — configure OOTB service health notifications to the service owner email when health drops below the Degraded threshold. Do not notify on every CI alert, only on service health state changes.",
         "Notifying stakeholders on every CI alert trains them to ignore notifications. Notify on service health state change only — this is the signal that matters to the business."),
        ("How will dynamic CIs (cloud VMs, containers) affect service health accuracy?",
         "Use Discovery / cloud connector to keep CI membership current. Flag dynamic services explicitly — health scores for services with high CI churn are less reliable until Discovery is mature.",
         "A service map that references deleted or spun-up CIs not yet in the CMDB produces misleading health scores. Coordinate with the Discovery workstream before enabling health maps for cloud-heavy services."),
        ("Will service maps be manually maintained or Discovery-derived?",
         "Manual maps for the first 5–10 services at MVP (fastest to deliver). Discovery-derived maps for Phase 2 once Discovery is tuned to the service topology.",
         "Discovery-derived maps are more accurate and self-maintaining but require a mature Discovery implementation. Manual maps are the right MVP trade-off."),
        ("What is the health score threshold for Degraded and Critical states?",
         "Degraded: health score < 80%. Critical: health score < 50%. These are OOTB defaults and work well for most customers at MVP. Calibrate after 30 days of production data.",
         "The right thresholds depend on service criticality and CI count. A service with 2 CIs where 1 fails hits 50% immediately; a service with 20 CIs where 2 fail is at 90%. Confirm thresholds per service, not globally."),
    ],
    dependencies=[
        ("CI correlation rate ≥ 85% (AP-08, Workbook 04)", "Pending", "ECS", "Before Sprint 3", "Service maps are only meaningful if the CI correlation is reliable"),
        ("Business services identified and named in CMDB (cmdb_ci_service)", "Pending", "Customer + ECS", "Sprint 2, Wk 2", "Service map build requires CI service records to exist in the CMDB"),
        ("CI membership list per service confirmed by service owner", "Pending", "Customer", "Sprint 3, Wk 1", "Service owner must approve CI scope — do not build maps without this sign-off"),
        ("OOTB Service Mapping plugin activated (com.sn_sm)", "Pending", "ECS", "Sprint 2, Wk 2", "Service Mapping plugin is required for automated topology discovery in Phase 2"),
        ("Alert grouping by service tested and validated (AP-08, Workbook 02)", "Pending", "ECS", "Sprint 2", "Correlation rules from AP-08 must be working before service-level grouping is testable"),
    ],
    config_sections=[
        ("Business Service Registry", [
            ("Service 1 — name and owner", "TBD", "Customer Service Owner to confirm", True),
            ("Service 2 — name and owner", "TBD", "Customer Service Owner to confirm", True),
            ("Service 3 — name and owner", "TBD", "Customer Service Owner to confirm", True),
            ("Service 4 — name and owner", "TBD", "Customer Service Owner to confirm", True),
            ("Service 5 — name and owner", "TBD", "Customer Service Owner to confirm", True),
            ("Additional services (Phase 2)", "TBD", "Defer to Phase 2 after MVP maps are validated", True),
        ]),
        ("Health Score Configuration", [
            ("Health score model", "OOTB composite model (CI count × CI criticality weight)", "Accept OOTB at MVP; custom model requires development and upgrade testing", False),
            ("Degraded threshold", "< 80% health score", "Service owner and Service Desk Manager to confirm; adjust per service if needed", True),
            ("Critical threshold", "< 50% health score", "Service owner and Service Desk Manager to confirm; triggers stakeholder notification", True),
            ("CI criticality weighting", "OOTB: critical CIs weighted 2× non-critical", "Requires CI criticality attribute to be populated on in-scope CIs", False),
            ("Health score refresh interval", "Every 5 minutes (OOTB default)", "Accept OOTB; reducing interval increases system load", False),
        ]),
        ("Notification Configuration", [
            ("Degraded → notification target", "Service owner email", "Customer to confirm service owner email per service", True),
            ("Critical → notification target", "Service owner + IT Manager + on-call operator", "Ensure on-call integration is configured (AP-08, Workbook 06)", True),
            ("Notification on health improvement (recovery)", "Yes — notify service owner when health returns to Operational", "Closes the communication loop for stakeholders", False),
            ("Notification rate limiting", "One notification per state change; suppress repeats within 30 minutes", "Prevents notification storms during prolonged degradation", False),
        ]),
    ],
    raci_rows=[
        ("Business service scope (which services get maps first)", "C", "R", "Customer CIO/IT Manager decides priority; ECS documents and builds"),
        ("CI membership confirmation per service", "I", "R", "Service owner signs off on which CIs belong to their service"),
        ("Service map build in CMDB", "R", "C", "ECS builds the map; service owner validates CI coverage"),
        ("Health score threshold calibration", "R", "C", "ECS configures OOTB thresholds; service owner approves for their service"),
        ("Stakeholder notification list per service", "I", "R", "Service owner provides the list; ECS configures the notification rule"),
        ("End-to-end service health scenario testing", "R", "C", "ECS executes test; service owner validates the health dashboard response"),
        ("Post-go-live health score tuning (30-day review)", "R", "C", "ECS reviews with 30 days of data; service owner approves threshold changes"),
    ],
    consultant_guide_sections=[
        ("Service Maps Are About Business Conversations, Not Technology",
         "The service health map build is the moment where IT and the business start speaking the same language. A CI alert means nothing to a service owner; 'your CRM service is at 60% health' means something. Run the service scoping session with the service owner present, not just the CMDB team — the service owner knows what matters to the business, the CMDB team knows what is technically connected. You need both."),
        ("The CI Criticality Attribute Problem",
         "The OOTB health score model weights critical CIs more heavily. But most customers have never populated the cmdb_ci.criticality attribute. Before the service map build, run a report: what percentage of in-scope CIs have criticality populated? If it is less than 50%, the weighting model produces misleading results. In that case, configure the health model without criticality weighting until the attribute is populated in Phase 2."),
        ("Manual vs Discovery-Derived Maps",
         "Manual maps take 30–60 minutes per service and are immediately accurate — the service owner names the CIs. Discovery-derived maps take days to tune but automatically update when the service topology changes. At MVP, manual maps for the top 5–10 services are the right trade-off. Start the Discovery tuning conversation early so Phase 2 maps can be derived rather than maintained."),
        ("The Health Dashboard Is a Stakeholder Management Tool",
         "Show the health dashboard to the IT leadership team before go-live. Not for approval — for socialization. Stakeholders who see the dashboard before a real incident are far less likely to panic when they see a 60% health score during an actual event. The first time should not be during a crisis."),
    ],
    adoption_rows=[
        ("'We want a custom health scoring algorithm that weights our most critical services differently.'",
         "Use the OOTB CI criticality weighting plus per-service threshold configuration to model service criticality. No custom code required.",
         "Custom scoring algorithms require scripting, survive platform upgrades poorly, and are difficult for customer admins to maintain.",
         "'The OOTB model gives you two levers: CI criticality weighting and per-service thresholds. Let me show you how those two combined handle the differentiation you are looking for without writing a single line of code.'",
         "Only if the customer's service criticality model genuinely cannot be expressed through CI criticality + threshold tuning. Document the business case before building."),
        ("'Can we integrate the health dashboard with our executive reporting portal?'",
         "Use the OOTB Performance Analytics integration for ServiceNow data export. Service health scores are PA indicators and can be exposed via the PA API.",
         "Custom portal integrations require ongoing maintenance as the ServiceNow data model evolves. The PA API is stable and version-controlled.",
         "'The PA API is the right integration point — health scores are already PA indicators and the API is documented and stable. That is a Phase 2 integration item; let us get the maps right first.'",
         "Yes — PA API export is OOTB and supportable. Scope this as a Phase 2 integration item."),
    ],
    snmap_sections=[
        ("Service Map Tables", [
            ("Business Service table", "cmdb_ci_service", "Parent record for each business service; linked to CI members via service_ci relationship"),
            ("Service CI relationship table", "service_ci", "Maps CIs to services; drives health score calculation"),
            ("Service health score table", "cmdb_service_health", "Stores current and historical health scores per service"),
            ("Service health notification rule", "em_service_health_notification_rule", "Drives stakeholder alerts on health state change"),
        ]),
        ("Key Configuration Points", [
            ("Service health scoring", "Configured via Service Mapping > Service Health", "Threshold sliders for Degraded and Critical in the service health configuration"),
            ("CI criticality weighting", "cmdb_ci.criticality attribute (1=Critical, 2=High, 3=Medium, 4=Low)", "Must be populated on in-scope CIs for weighting to be meaningful"),
            ("Service health dashboard", "OOTB Service Health dashboard in Event Management Workspace", "No custom development; add service widgets from the OOTB widget library"),
        ]),
        ("OOTB Features Used", [
            ("Service Mapping plugin (com.sn_sm)", "Automated service topology discovery", "Required for Discovery-derived maps in Phase 2"),
            ("Service Health Score", "Composite CI-based health calculation", "OOTB; no custom development; configured via Service Mapping admin"),
            ("Service Health Notifications", "Stakeholder alerts on health state change", "Configured via Event Management notification rules"),
            ("Performance Analytics — Service Health Indicators", "Long-term health trend reporting", "Health scores are PA indicators out of the box; enable PA collection for trend reporting"),
        ]),
    ],
)


# =============================================================================
# WORKBOOK 2 — Storm Management
# =============================================================================
wb2 = TabContent(
    workbook_title="02 — Storm Management",
    pack_name=PACK_NAME,
    purpose=(
        "Defines the configuration for detecting, containing, and recovering from event storms — "
        "periods of massively elevated event volume triggered by major outages, failed patches, or "
        "network events. Storm management is the difference between Event Management surviving a P1 "
        "incident and becoming part of the problem."
    ),
    who_fills=(
        "ECS Solution Architect. Storm management is primarily an ECS-owned configuration track. "
        "Customer IT Ops lead validates storm thresholds against historical incident data."
    ),
    sprint_window="Sprint 3–4 (after baseline event rules are stable from AP-08)",
    estimated_effort="6–8 hours including threshold design, storm simulation, and recovery testing",
    related_workbooks=["AP-08 Workbook 02 — Event Rules Baseline", "AP-09 Workbook 01 — Service Health Maps"],
    success_criteria=[
        "Storm detection rule is configured with agreed thresholds (events/minute per source).",
        "Storm parent alert creation is working — a single parent alert represents the storm, not hundreds of individual alerts.",
        "Storm suppression is in place: during a storm, low-severity alerts from the storm source are suppressed.",
        "Storm notification to the Service Desk Manager is configured and tested.",
        "Storm recovery procedure is documented in the Operator Runbook.",
        "A storm simulation test has been executed successfully before go-live.",
    ],
    process_decisions=[
        ("What event volume threshold defines a storm?",
         "≥ 100 events per minute from a single source within a 5-minute window. This is above the 99th percentile of normal operations for most customers.",
         "Setting the threshold too low creates false storm alerts during legitimate high-activity periods (e.g., patching). Setting it too high means a real storm is not detected until the queue is already overwhelmed. 100 events/minute is the right starting point; tune after 30 days of production data."),
        ("Should low-severity events be suppressed during a storm?",
         "Yes — suppress Severity 4–5 events from the storm source during the storm window. Severity 1–3 events continue to be processed as alerts.",
         "During a storm, Severity 4–5 events are almost always noise caused by the root-cause event propagating. Suppressing them keeps the operator workspace actionable."),
        ("How is the storm resolved — automatic or operator-confirmed?",
         "Automatic: when event volume drops below the storm threshold for 10 consecutive minutes, the storm alert closes and suppression ends. Operator receives a recovery notification.",
         "Requiring operator confirmation to close a storm alert creates additional toil during an already stressful incident. Automatic closure with a notification is the right balance."),
        ("Should storm events from non-production sources be handled differently?",
         "Yes — non-production storms route to the Event Triage group, not the production operator queue. Do not suppress — non-production storms can mask real events if suppressed entirely.",
         "Non-production patching and deployment activities regularly generate event storms. Routing them to a separate triage queue keeps the production operator view clean without losing visibility."),
        ("What happens to the individual alerts created before the storm was detected?",
         "The storm correlation rule retroactively links alerts created in the storm window to the parent storm alert. Individual alerts are not deleted but are de-emphasized in the operator workspace.",
         "Retroactive linkage is the OOTB behaviour. It is more transparent than deleting pre-storm alerts and preserves the audit trail."),
        ("What is the storm notification list?",
         "Service Desk Manager + on-call IT Manager. Storm notifications are high-priority and sent via email and on-call system (PagerDuty/OpsGenie if configured).",
         "Storm notifications are a management escalation, not an operator task. Notify management so they can communicate to stakeholders and authorize additional resources."),
    ],
    dependencies=[
        ("Event rules baseline stable and validated in production (AP-08, Workbook 02)", "Pending", "ECS", "Before Sprint 3", "Storm detection builds on top of the baseline event rules; unstable rules produce false storm triggers"),
        ("Historical event volume data by source (peak events/minute)", "Pending", "Customer", "Sprint 2, Wk 2", "Required to calibrate storm thresholds; use the monitoring tool's own metrics if em_event history is unavailable"),
        ("On-call notification integration configured (AP-08, Workbook 06)", "Pending", "ECS", "Sprint 2", "Storm notifications route through the on-call system; must be working before storm management is tested"),
        ("Storm simulation approval from customer IT Manager", "Pending", "Customer", "Sprint 3, Wk 2", "Storm simulation requires generating high event volume in the test environment; customer IT Manager must approve"),
    ],
    config_sections=[
        ("Storm Detection Thresholds", [
            ("Storm volume threshold (events/minute)", "100 events/minute from a single source in a 5-minute window", "Customer IT Ops lead to validate against historical peak event data", True),
            ("Storm detection window", "5 minutes", "OOTB correlation rule window; accept at MVP", False),
            ("Storm recovery window", "10 consecutive minutes below threshold", "Automatic closure condition; adjust if storms are naturally intermittent in the customer environment", True),
            ("Non-production storm threshold", "Same threshold; route to Event Triage group instead of operator queue", "Different routing, same detection logic", False),
        ]),
        ("Storm Correlation Rule", [
            ("Rule name", "EM Storm Detection — [Source Name]", "Create one rule per major event source to allow per-source threshold tuning", False),
            ("Parent alert name pattern", "EVENT STORM — [Source] — [Timestamp]", "Consistent naming makes storm alerts immediately recognizable in the operator workspace", False),
            ("Severity of storm parent alert", "Severity 1 (Critical)", "Storm parent alert is always Critical regardless of the severity of individual storm alerts", False),
            ("Storm alert assignment group", "Event Management Operators (production) or Event Triage (non-production)", "Route to the group with authority to coordinate the storm response", True),
        ]),
        ("Suppression Configuration During Storm", [
            ("Suppress Severity 4–5 events during storm", "Yes — suppress from the storm source for the duration of the storm window", "Prevents noise from overwhelming the operator workspace while the storm parent alert is active", False),
            ("Continue processing Severity 1–3 events during storm", "Yes — all high-severity events continue as individual alerts linked to the storm parent", "High-severity events during a storm may have different root causes; do not suppress", False),
            ("Suppression auto-lift on storm recovery", "Yes — suppression ends when storm alert closes", "Automatic; no operator action required to re-enable suppression after recovery", False),
        ]),
        ("Notification Configuration", [
            ("Storm detected — notification targets", "Service Desk Manager + on-call IT Manager", "Customer to confirm names and email/on-call IDs", True),
            ("Storm recovery — notification targets", "Same as storm detected list", "Recovery notification closes the communication loop", False),
            ("Notification channel", "Email + on-call system (PagerDuty/OpsGenie)", "Customer to confirm on-call system; ECS configures the ServiceNow-side webhook", True),
        ]),
    ],
    raci_rows=[
        ("Storm threshold calibration", "R", "C", "ECS designs based on historical volume data; IT Ops lead approves"),
        ("Storm simulation test authorization", "I", "R", "Customer IT Manager must approve; ECS executes the test"),
        ("Storm simulation execution", "R", "C", "ECS generates synthetic storm events; customer validates workspace behavior"),
        ("Non-production storm routing decision", "C", "R", "Customer decides triage group staffing; ECS configures routing"),
        ("Storm notification list confirmation", "I", "R", "Customer Service Desk Manager confirms notification targets"),
        ("Operator Runbook — storm recovery procedure", "R", "I", "ECS writes the storm recovery procedure; customer operators review and confirm"),
        ("Post-go-live threshold tuning (30-day review)", "R", "C", "ECS recommends threshold adjustments based on production storm data; customer approves"),
    ],
    consultant_guide_sections=[
        ("Why Storm Management Is a Phase 2 Item",
         "Storm management requires knowing what 'normal' looks like before you can define 'storm.' You cannot calibrate storm thresholds without production event data. AP-08 runs in Sprint 0–1 to establish the event flow; AP-09 storm management runs in Sprint 3–4 after 4–6 weeks of production data. Do not try to configure storm management before the baseline is stable — you will set the wrong thresholds and spend days chasing false positives."),
        ("Storm Simulation — Do It Before Go-Live",
         "A storm simulation (generating 100–500 synthetic events per minute in the test environment) is the only way to validate that storm detection, parent alert creation, suppression, and recovery all work correctly under load. Run the simulation in the test environment with the designated operators watching the workspace. This is also the best operator training exercise — there is no substitute for seeing the workspace behavior under a real storm scenario."),
        ("The False Positive Problem",
         "If the storm threshold is set too low (e.g., 20 events/minute), legitimate patching windows, deployment pipelines, and batch job completions will trigger false storm alerts. The operators will start ignoring storm notifications within 2 weeks. Always calibrate against historical peak event data and set the threshold at the 99th percentile + 50% headroom. If that data is unavailable, start high and tune down after 30 days."),
        ("Per-Source Storm Rules",
         "Create separate storm detection rules per major event source rather than one global rule. Network monitoring tools have different 'normal' volumes than application monitoring tools. A global threshold that is right for the network tool is often wrong for the application tool. Per-source rules allow independent tuning without affecting other sources."),
    ],
    adoption_rows=[
        ("'We want to auto-close all alerts during a storm and start fresh after recovery.'",
         "Use the OOTB storm parent alert model: individual alerts are linked to the storm parent but not closed. After the storm, operators review linked alerts and close manually or wait for the monitoring tool's recovery events to auto-close them.",
         "Auto-closing alerts during a storm destroys the audit trail and means that alerts for issues that did not self-resolve (root cause of the storm) are also closed. This is an invisible gap until the next incident review.",
         "'The storm parent model is designed exactly for this — it de-clutters the operator workspace during the storm without destroying the record of what happened. After the storm, everything is still there for the post-incident review.'",
         "Never auto-close alerts during a storm. The post-incident review depends on that data."),
        ("'We want storm suppression to apply to ALL events, not just Severity 4–5.'",
         "Suppress Severity 4–5 only. Severity 1–3 events during a storm continue as individual alerts linked to the storm parent.",
         "Suppressing all events during a storm means that a separate P1 event occurring during the storm window will not create an alert or promote an incident. The storm becomes a window of complete blindness.",
         "'Suppressing Severity 1–3 during a storm means a different P1 event that starts during the storm is invisible. That is the most dangerous gap we can create. Keep high-severity events flowing — the storm parent keeps the workspace organized.'",
         "Never suppress Severity 1–3 events during a storm."),
    ],
    snmap_sections=[
        ("Storm Management Tables", [
            ("Correlation rule table", "em_correlation_rule", "Storm detection is implemented as an OOTB correlation rule with high-volume conditions"),
            ("Parent alert table", "em_alert (where is_parent = true)", "Storm parent alerts are standard em_alert records flagged as parent"),
            ("Alert-to-parent linkage", "em_alert.parent_alert", "Links individual storm alerts to the storm parent alert"),
            ("Suppression rule table", "em_event_rule (suppression type)", "Storm suppression implemented as event rules activated when storm parent is open"),
        ]),
        ("OOTB Features Used", [
            ("Correlation Rule — Storm Detection", "High-volume threshold detection per source", "Configured via Event Management > Administration > Correlation Rules"),
            ("Parent Alert Creation", "Single parent alert representing the storm", "OOTB correlation rule output; no custom development"),
            ("Alert Suppression During Storm", "Low-severity event suppression while storm is active", "Event rule with condition on storm parent alert existence"),
            ("Storm Auto-Recovery", "Storm parent closes automatically when volume drops", "Configured via the correlation rule recovery condition"),
        ]),
    ],
)


# =============================================================================
# WORKBOOK 3 — AIOps Integration
# =============================================================================
wb3 = TabContent(
    workbook_title="03 — AIOps Integration",
    pack_name=PACK_NAME,
    purpose=(
        "Defines the configuration for ServiceNow's OOTB AIOps capabilities within Event Management: "
        "ML-based noise reduction, anomaly detection, and predictive event correlation. "
        "AIOps features are available with the Health Log Analytics and Predictive AIOps licenses "
        "and activate automatically once the event data volume is sufficient for ML training."
    ),
    who_fills=(
        "ECS Solution Architect (primary). Customer IT Manager confirms license scope "
        "and data retention requirements for ML training."
    ),
    sprint_window="Sprint 4–5 (after ≥ 30 days of production event data)",
    estimated_effort="6–10 hours including ML model activation, training validation, and initial results review",
    related_workbooks=["AP-08 Workbook 02 — Event Rules Baseline", "AP-09 Workbook 01 — Service Health Maps", "AP-09 Workbook 04 — Alert Intelligence"],
    success_criteria=[
        "AIOps license scope is confirmed and the required plugins are activated.",
        "ML training data volume requirement is met (minimum 30 days of clean event data).",
        "Anomaly Detection is enabled for at least the top 3 CI classes by event volume.",
        "Noise reduction rate is measured: target ≥ 30% reduction in actionable alerts after 60 days.",
        "Operators understand ML-generated recommendations and can act on them in the workspace.",
        "AIOps performance dashboard is accessible to the Service Desk Manager.",
    ],
    process_decisions=[
        ("Are Health Log Analytics and/or Predictive AIOps licenses in scope?",
         "Confirm with the customer's ServiceNow license agreement. Health Log Analytics drives anomaly detection and noise reduction; Predictive AIOps drives predictive correlation and root cause suggestions.",
         "AIOps features require specific licenses that may not be included in the base Event Management license. Confirm before spending time on AIOps configuration."),
        ("What is the minimum clean event data volume for ML training?",
         "30 days of production event data with ≥ 85% CI correlation rate. ML models trained on low-quality or uncorrelated event data produce unreliable results.",
         "Starting ML training before the event baseline is clean is the most common AIOps implementation mistake. The model learns the noise as signal and noise reduction goes negative — more alerts, not fewer."),
        ("Which CI classes should be prioritized for anomaly detection?",
         "Start with the CI classes that generate the highest event volume and have the cleanest CMDB data: typically servers (cmdb_ci_server), network gear (cmdb_ci_netgear), and databases (cmdb_ci_database).",
         "Anomaly detection accuracy improves with event volume per CI class. Starting with high-volume CI classes provides the fastest feedback loop for model quality."),
        ("How will operators interact with ML-generated alert recommendations?",
         "OOTB — ML recommendations appear in the Event Management Workspace as 'Suggested Actions' on alerts. Operators can accept or dismiss recommendations. Acceptance feedback improves the model.",
         "Operators who understand that their feedback (accept/dismiss) trains the model are more likely to engage with recommendations consistently. Include this in the operator walkthrough."),
        ("What noise reduction target is realistic at 60 days?",
         "30% reduction in actionable alerts at 60 days is a realistic and measurable target for a well-configured implementation. 50%+ is achievable at 90 days with active operator feedback.",
         "Promising unrealistic noise reduction numbers (80%+ within 30 days) sets up the implementation for a perception failure. Set conservative targets and exceed them."),
    ],
    dependencies=[
        ("Minimum 30 days of clean production event data with ≥ 85% CI correlation", "Pending", "ECS", "Sprint 4 start", "ML model cannot train on low-quality data; this is a hard dependency"),
        ("Health Log Analytics and/or Predictive AIOps license confirmed", "Pending", "Customer", "Sprint 3, Wk 1", "AIOps features are license-gated; confirm before configuration begins"),
        ("OOTB AIOps plugins activated (com.snc.health_log_analytics, com.snc.predictive_aiops)", "Pending", "ECS", "Sprint 4, Wk 1", "Plugins must be activated before AIOps configuration is accessible"),
        ("Operator walkthrough completed and operators trained on ML recommendations", "Pending", "ECS", "Sprint 5, Wk 1", "Operators must understand ML suggestions before go-live; untrained operators ignore or override all recommendations"),
    ],
    config_sections=[
        ("License and Plugin Scope", [
            ("Health Log Analytics license", "Confirm with customer license team", "Drives anomaly detection and ML-based noise reduction", True),
            ("Predictive AIOps license", "Confirm with customer license team", "Drives predictive correlation and root cause suggestions", True),
            ("Health Log Analytics plugin", "com.snc.health_log_analytics", "Must be activated before anomaly detection configuration", False),
            ("Predictive AIOps plugin", "com.snc.predictive_aiops", "Must be activated before predictive correlation configuration", False),
        ]),
        ("ML Training Configuration", [
            ("Minimum training data period", "30 days of production event data", "Do not activate ML features before this threshold is met", False),
            ("Training data CI correlation requirement", "≥ 85% CI correlation rate during training period", "Uncorrelated events are noise to the ML model; low correlation = poor model quality", False),
            ("ML model retraining schedule", "Weekly automatic retraining (OOTB default)", "Accept OOTB; manual retraining available via the AIOps administration interface", False),
            ("Training data scope", "All in-scope CI classes from the event sources defined in AP-08, Workbook 01", "Do not limit training data scope unless event volume is extremely high (>1M events/day)", False),
        ]),
        ("Anomaly Detection Configuration", [
            ("Priority CI class 1", "cmdb_ci_server (servers)", "Highest event volume in most environments; best training data for the model", False),
            ("Priority CI class 2", "cmdb_ci_netgear (network)", "Second-highest event volume; network events drive a high proportion of P1 incidents", False),
            ("Priority CI class 3", "cmdb_ci_database (databases)", "Database events are high-impact; anomaly detection here has the highest business value", False),
            ("Additional CI classes (Phase 2)", "Customer to identify based on 30-day event data analysis", "Expand anomaly detection after MVP model quality is validated", True),
            ("Anomaly detection sensitivity", "Medium (OOTB default)", "Accept at MVP; tune after 60 days of feedback from operators", False),
        ]),
        ("AIOps Performance Metrics", [
            ("Baseline actionable alert count (pre-AIOps)", "TBD — measure in the 30-day pre-AIOps period", "ECS to report from em_alert data before AIOps activation", False),
            ("Target noise reduction at 60 days", "≥ 30% reduction in actionable alerts", "Report via PA indicator; ECS to build the measurement dashboard", False),
            ("Target noise reduction at 90 days", "≥ 50% reduction in actionable alerts", "Achievable with active operator feedback loop", False),
            ("Operator recommendation acceptance rate target", "≥ 70%", "High acceptance rate indicates model quality and operator trust", False),
        ]),
    ],
    raci_rows=[
        ("License scope confirmation", "I", "R", "Customer IT Manager confirms with ServiceNow account team"),
        ("AIOps plugin activation", "R", "I", "ECS activates plugins; customer IT Manager approves"),
        ("ML training period monitoring (data quality)", "R", "C", "ECS monitors CI correlation rate and event volume during training period"),
        ("Anomaly detection CI class prioritization", "R", "C", "ECS recommends based on event volume data; customer IT Ops lead approves"),
        ("Operator walkthrough — ML recommendation workflow", "R", "I", "ECS delivers the walkthrough; all designated operators attend"),
        ("Noise reduction measurement and reporting", "R", "C", "ECS builds the PA measurement dashboard; customer IT Manager reviews monthly"),
        ("Model sensitivity tuning (60-day review)", "R", "C", "ECS recommends adjustments based on operator feedback data; customer approves"),
    ],
    consultant_guide_sections=[
        ("Set Expectations Before You Start",
         "AIOps is the most oversold feature in Event Management. Customer expectations after seeing vendor marketing are often 80%+ noise reduction within 30 days. The realistic trajectory: 0% at day 0 (model training), 10–15% at day 30 (early model), 30% at day 60 (calibrated model), 50%+ at day 90 (operator feedback incorporated). Show customers the maturity curve before activation, not after they are disappointed by early results."),
        ("Clean Data Is the Only Variable That Matters",
         "Every AIOps implementation that fails does so because of dirty training data. Uncorrelated events, misconfigured severity mappings, and suppressed events that should have flowed through the model all corrupt the training set. Before activating AIOps, run a 30-day data quality audit: CI correlation rate, severity distribution, event volume per source. If the data is clean, AIOps works. If it is not, AIOps makes things worse."),
        ("Operator Feedback Is Not Optional",
         "The ML model improves based on operator accept/dismiss feedback on recommendations. An implementation where operators never interact with recommendations produces a static model that does not improve. Build the feedback expectation into the operator runbook: 'Review and respond to ML suggestions every time you acknowledge an alert. This trains the model.' Include the acceptance rate metric in the weekly management report."),
        ("When to Defer AIOps",
         "If the customer's event volume is less than 50,000 events/week, the ML model has insufficient training data to produce reliable results. In this case, defer AIOps to Phase 2 and focus on OOTB correlation rules for noise reduction in Foundations. Do not activate AIOps features for the sake of demonstrating them — a poorly-trained model destroys operator confidence faster than any configuration error."),
    ],
    adoption_rows=[
        ("'We want AIOps to automatically resolve alerts without operator review.'",
         "Use AIOps for noise reduction recommendations and human-in-the-loop alert promotion decisions. Auto-resolution of alerts should come from monitoring tool recovery events (AP-08, Workbook 03), not from the ML model.",
         "ML models make mistakes, especially in the early training period. Auto-resolving alerts based on ML recommendations without operator review creates invisible gaps where real incidents are suppressed.",
         "'AIOps makes your operators faster, not optional. The recommendation workflow puts the right information in front of the operator so they can make the right decision in 10 seconds instead of 2 minutes. That is the ROI.'",
         "Only after ≥ 90 days of validated model performance AND operator agreement AND a defined exception process. Document the risk explicitly."),
        ("'Can we train the AIOps model on data from our old monitoring system before we go live on ServiceNow?'",
         "No. AIOps trains on em_event and em_alert data from the ServiceNow instance. Historical data from external monitoring systems cannot be imported in a form the model can use.",
         "The ML model requires the full em_event record structure including CMDB correlation, severity mapping, and source attribution. External monitoring data lacks these attributes.",
         "'The 30-day training period is actually an advantage — it means the model learns your environment as it exists on the new platform, not as it existed in the old system. The old system's patterns may not reflect the new architecture.'",
         "Never. This is an architectural boundary of the ML platform."),
    ],
    snmap_sections=[
        ("AIOps Tables and Features", [
            ("Anomaly detection results", "ml_anomaly_detection_result", "Stores ML-generated anomaly scores per CI per time window"),
            ("AIOps alert enrichment", "em_alert (aiops_* fields)", "ML-generated fields appended to em_alert records by the AIOps engine"),
            ("Operator feedback table", "ml_operator_feedback", "Stores accept/dismiss feedback from operators; drives model retraining"),
            ("AIOps administration", "Predictive AIOps > Administration", "Model management, retraining schedule, sensitivity configuration"),
        ]),
        ("OOTB AIOps Features in Event Management", [
            ("Anomaly Detection", "CI-level event anomaly scoring", "Identifies when a CI's event pattern deviates from its historical baseline"),
            ("Noise Reduction", "ML-based suppression of low-signal events", "Reduces actionable alert volume by identifying historically non-actionable events"),
            ("Predictive Correlation", "Cross-source alert grouping based on historical patterns", "Groups alerts that have historically co-occurred before a P1 incident"),
            ("Root Cause Suggestions", "ML-suggested probable root cause CI", "Surfaces in the operator workspace; improves with operator feedback"),
        ]),
    ],
)


# =============================================================================
# WORKBOOK 4 — Alert Intelligence
# =============================================================================
wb4 = TabContent(
    workbook_title="04 — Alert Intelligence",
    pack_name=PACK_NAME,
    purpose=(
        "Defines the OOTB alert classification, similar alert suggestions, and alert enrichment "
        "configuration that makes the operator workspace intelligent rather than just a list of alerts. "
        "Alert intelligence features reduce mean-time-to-diagnose by surfacing relevant context "
        "alongside each alert without requiring operator research."
    ),
    who_fills=(
        "ECS Solution Architect. Customer IT Ops lead validates that suggested similar alerts "
        "and enrichment data match operational reality."
    ),
    sprint_window="Sprint 3–4",
    estimated_effort="4–6 hours including enrichment configuration, similar alert testing, and workspace validation",
    related_workbooks=["AP-08 Workbook 02 — Event Rules Baseline", "AP-09 Workbook 03 — AIOps Integration"],
    success_criteria=[
        "Alert enrichment fields (affected service, CI owner, recent changes) are populated on all Severity 1–3 alerts.",
        "Similar alert suggestions are surfaced in the workspace for at least 70% of alert types.",
        "Alert classification (category/subcategory) is automatically derived from CI class and event type.",
        "Related incident history is accessible from the alert without navigating away from the workspace.",
        "Alert enrichment does not degrade workspace performance (load time < 3 seconds for the alert detail view).",
    ],
    process_decisions=[
        ("What contextual information should be displayed on an alert in the workspace?",
         "OOTB: affected CI, CI owner, assigned support group, affected business service, recent changes to the CI (last 72 hours from Change Management), open incidents for the CI, and similar historical alerts. Accept the OOTB default; add custom fields in Phase 2 if needed.",
         "Enrichment data must be available without operator navigation. If the operator needs to open 3 separate records to gather context, the workspace is not faster than the old way of working."),
        ("Should recent change data be shown on alerts to help diagnose change-induced incidents?",
         "Yes — show the last 5 approved changes to the affected CI in the last 72 hours. This is OOTB via the Change Management integration in the Event Management Workspace.",
         "Change-induced incidents account for a significant percentage of P1 events. Surfacing recent changes on the alert reduces mean-time-to-diagnose for this category from hours to seconds."),
        ("How will similar alert suggestions be generated — rule-based or ML-based?",
         "Rule-based at MVP (OOTB: alerts from the same source with the same event type and CI class are similar). ML-based similarity activates automatically once AIOps training data is sufficient (see Workbook 03).",
         "Rule-based similar alerts work immediately with no training period. ML-based similarity is more accurate but requires 30+ days of data. Start with rule-based and transition to ML-based naturally as the AIOps model matures."),
        ("Should alert classification (category/subcategory) be auto-populated?",
         "Yes — derive category from CI class (cmdb_ci.sys_class_name) and subcategory from alert event type. This ensures consistent classification and accurate reporting without manual operator input.",
         "Manual alert classification by operators is inconsistent and low-quality. Operators under time pressure skip classification fields. Auto-classification is the only way to get clean category data at scale."),
    ],
    dependencies=[
        ("CI class mapping to incident category/subcategory agreed (from ITSM workstream)", "Pending", "Customer", "Sprint 2, Wk 2", "Alert auto-classification must align with the Incident category taxonomy"),
        ("Change Management integration confirmed working (CHG → Event alert context)", "Pending", "ECS", "Sprint 3, Wk 1", "Recent changes appear on the alert only if the CHG integration is configured"),
        ("Alert correlation rate ≥ 85% (AP-08, Workbook 04)", "Pending", "ECS", "Before Sprint 3", "Similar alert suggestions require alerts to be correlated to CIs; uncorrelated alerts have no similar alert context"),
    ],
    config_sections=[
        ("Alert Enrichment Fields", [
            ("Affected CI — name, class, environment", "Auto-populated from em_alert.cmdb_ci", "Requires CI correlation to be working", False),
            ("CI owner (support group)", "Auto-populated from cmdb_ci.support_group", "Requires support_group to be populated on all in-scope CIs", False),
            ("Affected business service", "Auto-populated from service_ci relationship", "Requires service maps to be built (AP-09, Workbook 01)", False),
            ("Recent changes to CI (last 72 hours)", "OOTB Change Management integration — last 5 approved changes", "Configured via Event Management > Administration > External Data Sources", False),
            ("Open incidents for CI", "Auto-populated from em_alert_task_alert binding", "Shows linked incidents and any open incidents for the same CI", False),
        ]),
        ("Alert Classification", [
            ("Category mapping — cmdb_ci_server", "Category: Hardware", "ECS to confirm against agreed incident taxonomy", True),
            ("Category mapping — cmdb_ci_netgear", "Category: Network", "ECS to confirm against agreed incident taxonomy", True),
            ("Category mapping — cmdb_ci_database", "Category: Database", "ECS to confirm against agreed incident taxonomy", True),
            ("Category mapping — cmdb_ci_application", "Category: Software", "ECS to confirm against agreed incident taxonomy", True),
            ("Subcategory mapping — event type 'CPU'", "Subcategory: Performance", "ECS to document full event type to subcategory mapping", False),
            ("Subcategory mapping — event type 'Disk'", "Subcategory: Availability", "ECS to document full event type to subcategory mapping", False),
            ("Subcategory mapping — event type 'Network'", "Subcategory: Connectivity", "ECS to document full event type to subcategory mapping", False),
        ]),
        ("Similar Alert Configuration", [
            ("Rule-based similarity criteria", "Same source + same event type + same CI class within 24 hours", "OOTB; no configuration required beyond enabling the similar alert widget in the workspace", False),
            ("Similar alert lookback window", "24 hours (OOTB default)", "Extend to 72 hours for low-frequency, high-impact alert types if needed", False),
            ("Maximum similar alerts displayed", "10 (OOTB default)", "Accept at MVP; operators overwhelmed by too many similar alerts start ignoring them", False),
            ("ML-based similarity (post-AIOps)", "Activates automatically when AIOps model is trained", "See Workbook 03; ML similarity replaces rule-based when model is ready", False),
        ]),
    ],
    raci_rows=[
        ("Alert enrichment field selection", "R", "C", "ECS selects from OOTB available fields; IT Ops lead validates usefulness"),
        ("CI class to incident category mapping", "R", "C", "ECS maps based on ITSM taxonomy; customer confirms alignment"),
        ("Similar alert configuration", "R", "I", "ECS configures; operators validate suggestions match their intuition during UAT"),
        ("Change Management integration for alert context", "R", "C", "ECS configures the integration; Change Manager confirms change data is appearing correctly"),
        ("Workspace performance validation (< 3 second load)", "R", "I", "ECS validates; alerts if enrichment queries are degrading performance"),
    ],
    consultant_guide_sections=[
        ("Enrichment vs Performance Trade-Off",
         "Every enrichment field on an alert requires an additional database lookup when the alert is opened. Three to five enrichment fields is the sweet spot — enough context to diagnose without degrading workspace performance. Test workspace alert open time with all enrichment fields active before go-live. If load time exceeds 3 seconds, remove the lowest-value enrichment field, not the highest-value one."),
        ("The Change Management Integration ROI",
         "The single highest-value enrichment field is recent changes to the affected CI. Studies across ITSM implementations consistently show that 20–40% of P1 incidents are change-induced. Surfacing recent changes on the alert eliminates the most common time-wasting investigative step (Did someone change something recently?). This field alone reduces MTTR meaningfully and is easy to demonstrate to the IT Manager."),
        ("Auto-Classification Is Non-Negotiable",
         "Manual alert classification produces data that is too inconsistent for meaningful reporting. After 90 days of manually classified alerts, the category distribution will reflect which operators were working at the time, not the actual alert mix. Auto-classification from CI class + event type produces consistent data from day one. The data quality compounds over time — at 12 months, the category trends are meaningful for capacity planning and problem management."),
    ],
    adoption_rows=[
        ("'We want custom enrichment data from our CMDB that is not in the standard alert view.'",
         "Use the OOTB alert workspace customization to add custom CI attributes to the alert enrichment panel. Most CMDB attributes can be surfaced without custom development.",
         "Custom development for enrichment fields is rarely needed because the OOTB workspace customization supports attribute-level field addition from any related table.",
         "'Show me which CMDB field you want — most of them can be added through the workspace configuration without writing code. Let us check what is available before we scope a development item.'",
         "Only if the field requires a complex calculation or multi-table join that the workspace field configuration cannot handle."),
    ],
    snmap_sections=[
        ("Alert Intelligence Tables", [
            ("Similar alert relationship table", "em_alert_similar_alert", "Links similar alerts for workspace display"),
            ("Alert enrichment configuration", "em_workspace_config (enrichment section)", "Defines which enrichment fields appear in the alert detail panel"),
            ("Alert classification rules", "em_event_rule (classification transform)", "Auto-populates category/subcategory on the alert from CI class and event type"),
        ]),
        ("OOTB Features Used", [
            ("Alert Enrichment Panel", "Contextual data panel in the Event Management Workspace alert detail", "Configured via workspace administration; no custom development"),
            ("Similar Alerts Widget", "Shows historically similar alerts alongside the current alert", "OOTB workspace widget; enabled in workspace configuration"),
            ("Recent Changes Widget", "Shows last 5 approved changes to the affected CI", "Requires Change Management integration; configured via External Data Sources"),
        ]),
    ],
)


# =============================================================================
# WORKBOOK 5 — Remediation Workflows
# =============================================================================
wb5 = TabContent(
    workbook_title="05 — Remediation Workflows",
    pack_name=PACK_NAME,
    purpose=(
        "Defines the auto-remediation and runbook automation configuration that allows ServiceNow "
        "to automatically respond to known event patterns without operator intervention. "
        "Remediation workflows close the loop from detection to resolution for the most common "
        "alert types, reducing MTTR and operator toil."
    ),
    who_fills=(
        "ECS Solution Architect with customer IT Ops lead and system administrators. "
        "Remediation actions must be approved and tested by the customer's operations team before activation."
    ),
    sprint_window="Sprint 4–5 (after alert promotion and auto-resolution are stable from AP-08)",
    estimated_effort="8–12 hours including runbook design, automation scripting, and approval testing",
    related_workbooks=["AP-08 Workbook 03 — Alert Promotion Rules", "AP-09 Workbook 04 — Alert Intelligence"],
    success_criteria=[
        "Top 5 auto-remediation scenarios are identified, approved, and tested.",
        "Runbook Automation (RBA) workflows are configured for each approved scenario.",
        "Human-in-the-loop approval step is in place for all destructive remediation actions (restart, failover).",
        "Remediation success/failure is logged on the linked incident record.",
        "Failed remediation triggers operator notification and escalation.",
        "Remediation effectiveness rate (successful auto-remediation / total attempts) is measured and reported.",
    ],
    process_decisions=[
        ("Which alert types are candidates for auto-remediation?",
         "Start with the 5 most common, well-understood, low-risk remediation actions: disk cleanup scripts, service restart, cache flush, connection pool reset, and scheduled job re-trigger. Never auto-remediate actions that could cause data loss or extended downtime without human approval.",
         "The right candidates are: high-frequency, well-understood root cause, known remediation that works > 90% of the time, and low blast radius if the remediation fails. Start there."),
        ("What approval workflow is required before executing a remediation action?",
         "OOTB: Service Restart and above require a named approver (on-call operator or Service Desk Manager) to confirm via the mobile app or email before the RBA workflow executes. Low-risk actions (cache flush, log rotation) can execute without approval.",
         "Never configure auto-remediation without a defined approval tier for each action type. The customer's operations team must own the approval list — ECS cannot approve production remediation actions."),
        ("How will remediation success or failure be measured?",
         "Log remediation attempt, action taken, result (success/failure), and duration on the linked incident work note. Failed remediations trigger operator notification and are flagged for post-incident review.",
         "Remediation logging is the only way to measure effectiveness and justify the RBA investment. It is also the audit trail that demonstrates due diligence when a remediation fails."),
        ("What happens if a remediation action fails?",
         "Notify the on-call operator immediately with the failure detail. Escalate the linked incident to Priority 1 if the remediation failure indicates the issue is worse than initially assessed.",
         "Unnoticed remediation failures leave the system in an ambiguous state — the alert closed but the issue was not resolved. The failure notification must be immediate and must go to someone with authority to escalate."),
        ("Will MID Server be used for on-premises remediation, or is there a direct API?",
         "MID Server for on-premises actions (Windows restart, Linux service control). Direct REST API for cloud-hosted services that expose a management API.",
         "This mirrors the event source decision from AP-08, Workbook 01. The same topology that applies to event sources applies to remediation actions."),
    ],
    dependencies=[
        ("Alert promotion and auto-resolution working correctly (AP-08, Workbook 03)", "Pending", "ECS", "Before Sprint 4", "Remediation workflows trigger from promoted alerts; unstable promotion = unreliable remediation triggers"),
        ("Runbook Automation plugin activated (com.snc.runbook_automation)", "Pending", "ECS", "Sprint 4, Wk 1", "RBA workflows require the RBA plugin; activate before remediation design sessions"),
        ("Customer operations team to approve the remediation candidate list", "Pending", "Customer IT Ops Lead", "Sprint 3, Wk 2", "ECS cannot define which remediation actions are safe to auto-execute; customer operations team must own this list"),
        ("Test environment with representative CIs available for remediation testing", "Pending", "Customer", "Sprint 4, Wk 1", "All remediation workflows must be tested in the test environment before production activation; customer to confirm test CI availability"),
        ("MID Server configured (AP-08, Workbook 05) for on-premises remediation", "Pending", "ECS", "Sprint 0", "On-premises remediation requires an active MID Server; same MID Server as event source collection"),
    ],
    config_sections=[
        ("Approved Remediation Scenarios", [
            ("Scenario 1 — Disk space cleanup", "Action: Run disk cleanup script via MID Server. Approval: None (automated). Scope: Non-production CIs only at MVP.", "Safe to automate; low blast radius; high frequency", True),
            ("Scenario 2 — Application service restart", "Action: Restart named Windows/Linux service via MID Server. Approval: On-call operator via mobile app. Scope: Non-critical services only.", "Requires approval; service restart can cause brief downtime", True),
            ("Scenario 3 — Cache flush", "Action: API call to application cache flush endpoint. Approval: None (automated). Scope: Designated caching services only.", "Safe to automate; cache flush is stateless and reversible", True),
            ("Scenario 4 — Connection pool reset", "Action: API call to application server connection pool reset. Approval: On-call operator. Scope: Database connection pools.", "Requires approval; brief connection disruption during reset", True),
            ("Scenario 5 — Scheduled job re-trigger", "Action: API call to scheduler to re-trigger failed job. Approval: None (automated). Scope: Idempotent scheduled jobs only.", "Safe to automate only for idempotent jobs; customer must confirm idempotency", True),
        ]),
        ("Approval Workflow Configuration", [
            ("Low-risk actions (no approval)", "Cache flush, log rotation, disk cleanup, idempotent job re-trigger", "ECS to validate that each no-approval action meets the low-risk criteria", False),
            ("Standard approval actions", "Service restart, connection pool reset, process kill", "On-call operator approves via ServiceNow mobile app or email within 5 minutes", False),
            ("Elevated approval actions", "VM reboot, failover, network config change", "On-call operator + Service Desk Manager both must approve; 10-minute window", False),
            ("Approval escalation if no response", "Escalate to backup approver; if still no response after 15 min, notify IT Manager and abort remediation", "Remediation must not execute if approval window expires; safe default is abort", False),
        ]),
        ("Remediation Logging", [
            ("Work note on linked incident — attempt", "Logged when remediation action is triggered: action name, target CI, timestamp", "Automatic via RBA workflow; no manual step required", False),
            ("Work note on linked incident — result", "Logged when action completes: success/failure, duration, output (first 500 characters)", "Automatic via RBA workflow output step", False),
            ("Remediation failure alert", "Notify on-call operator immediately; upgrade incident priority if severity warrants", "ECS to configure the failure notification in the RBA workflow", False),
            ("Remediation effectiveness dashboard", "PA indicator: successful remediations / total attempts per scenario, weekly", "ECS to build the measurement dashboard in Sprint 5", False),
        ]),
    ],
    raci_rows=[
        ("Remediation candidate list approval", "I", "R", "Customer IT Ops Lead defines and approves; ECS documents"),
        ("Approval tier assignment per action type", "R", "C", "ECS drafts the tier structure; customer IT Manager approves"),
        ("RBA workflow build", "R", "I", "ECS builds in ServiceNow; customer operations team reviews the workflow logic"),
        ("Remediation testing in test environment", "R", "C", "ECS executes test scenarios; customer operations team validates results"),
        ("Production activation approval", "I", "R", "Customer IT Manager signs off on production activation for each scenario"),
        ("Remediation effectiveness measurement", "R", "C", "ECS builds the PA dashboard; customer IT Manager reviews monthly"),
        ("Failed remediation post-incident review", "R", "C", "ECS leads the review for failed remediations; customer operations team attends"),
    ],
    consultant_guide_sections=[
        ("Start Small and Build Trust",
         "The fastest path to a failed auto-remediation program is automating too much too soon. Start with the safest, most understood, most reversible actions. Build the operator's trust that the automation works and does not cause harm. After 30 days of successful automated remediations, the operator team will come to ECS asking for more automation — that is the right time to expand scope."),
        ("The Approval Workflow Is the Governance Framework",
         "The approval workflow is what makes auto-remediation safe. Every destructive action (restart, reset, reboot) must have a human approval step. The approval step is also a coaching opportunity — the on-call operator who approves a restart learns when it is appropriate and why, which builds institutional knowledge. Design the approval workflow with the customer's ops team, not for them."),
        ("Measure Everything",
         "The RBA program justification depends on data. Track: how many remediations were attempted, how many succeeded, how much time was saved per successful remediation (use the MTTR delta), and how many failed and why. Show this data monthly to the IT Manager. A program that resolves 50 incidents per month automatically, each saving 30 minutes of operator time, is easy to defend and easy to expand."),
        ("The MID Server Is the Remediation Bridge",
         "On-premises remediation depends on the MID Server being healthy. A MID Server that is under load from event processing will also be slow to execute remediation scripts. If event volume is high and remediation response time is slow, consider a dedicated MID Server for remediation workflows separate from the event source MID Server."),
    ],
    adoption_rows=[
        ("'We want to auto-remediate VM reboots without approval.'",
         "VM reboots require explicit operator approval. Place this in the elevated approval tier with dual sign-off.",
         "An auto-rebooted VM that was serving active user sessions causes an outage, not a remediation. The blast radius is too large for zero-approval automation.",
         "'A VM reboot is a calculated risk — sometimes the right call, sometimes not. The approval step takes 2 minutes and gives the operator the context to make the right decision. That 2 minutes is worth it.'",
         "Never. VM reboots require approval regardless of the customer's confidence level."),
        ("'Can we trigger remediation from our monitoring tool directly rather than through ServiceNow?'",
         "Trigger remediation through ServiceNow RBA only. Monitoring tool-triggered remediation bypasses the ITSM record linkage, audit trail, and approval workflow.",
         "Monitoring tool-triggered remediation is invisible to the ITSM system. There is no incident record, no approval audit, no effectiveness measurement. It also creates two parallel remediation programs that quickly become inconsistent.",
         "'Running remediation through ServiceNow means every action is linked to an incident, approved by the right person, and tracked for effectiveness. Your monitoring tool is great at detecting the issue — ServiceNow is where the response is orchestrated.'",
         "Never. Remediation must flow through the ITSM platform for auditability and governance."),
    ],
    snmap_sections=[
        ("Runbook Automation Tables", [
            ("RBA workflow table", "rba_workflow", "Defines the automated workflow steps, conditions, and approvals"),
            ("RBA execution history", "rba_activity_execution", "Logs every RBA execution attempt, outcome, and duration"),
            ("MID Server command table", "ecc_queue (RBA commands)", "RBA commands to on-premises systems route through the ecc_queue to the MID Server"),
        ]),
        ("OOTB Features Used", [
            ("Runbook Automation (RBA)", "ServiceNow's orchestration engine for automated IT actions", "Available via the Orchestration license; confirm license scope with customer"),
            ("MID Server Script Execution", "Executes scripts and commands on on-premises systems via MID Server", "Uses the PowerShell or SSH activity packs in RBA"),
            ("REST API Activity", "Calls external REST APIs for cloud-hosted service remediation", "OOTB REST activity in RBA; no custom development required"),
            ("Approval Workflow", "Human-in-the-loop approval before destructive remediation actions", "Standard ServiceNow approval workflow integrated into the RBA execution chain"),
        ]),
    ],
)


# =============================================================================
# WORKBOOK 6 — Advanced Correlation
# =============================================================================
wb6 = TabContent(
    workbook_title="06 — Advanced Correlation",
    pack_name=PACK_NAME,
    purpose=(
        "Defines multi-source, multi-tier advanced correlation rules that group alerts from "
        "different monitoring tools and different CI classes into unified parent alerts representing "
        "a single business event. Advanced correlation is the configuration that produces "
        "the 'single view of an incident' that operators need to diagnose complex, cross-domain outages."
    ),
    who_fills=(
        "ECS Solution Architect. Advanced correlation rules are ECS-owned configuration. "
        "Customer IT Ops lead validates that correlation groupings match operational experience."
    ),
    sprint_window="Sprint 3–4 (after Foundations event rules are stable)",
    estimated_effort="8–10 hours including rule design, cross-source testing, and parent alert validation",
    related_workbooks=["AP-08 Workbook 02 — Event Rules Baseline", "AP-09 Workbook 01 — Service Health Maps"],
    success_criteria=[
        "At least 3 multi-source correlation scenarios are configured and tested.",
        "Parent alert correctly aggregates child alerts from at least 2 different event sources.",
        "Cross-CI-class correlation (e.g., network alert + server alert = related) is working for the top 3 incident patterns.",
        "Parent alert severity reflects the highest child alert severity (not an average).",
        "Operator workspace correctly shows the parent-child hierarchy without requiring navigation.",
    ],
    process_decisions=[
        ("What are the most common multi-source incident patterns in this environment?",
         "Interview the IT Ops team: 'When a P1 incident happens, which monitoring tools typically all fire at the same time?' The most common patterns are: network switch failure → server alerts + application alerts from the same segment; database overload → application alerts + end-user experience alerts; storage failure → VM alerts + application alerts.",
         "Advanced correlation rules must be built from real incident patterns, not from theoretical alert taxonomy. The IT Ops team holds this knowledge."),
        ("What correlation window should be used for multi-source rules?",
         "10 minutes is the OOTB default and works for most infrastructure-layer incidents. Application-layer incidents (where the root cause takes time to cascade) may need a 20–30 minute window.",
         "A correlation window that is too short misses the cascade; too long creates false groupings. Use the customer's historical incident timeline data to calibrate — how long does it typically take for a root cause to produce alerts across all affected tools?"),
        ("How should parent alert severity be determined?",
         "Parent alert severity = highest severity among child alerts. Do not average. One Severity 1 child in a group makes the parent Severity 1.",
         "Averaging severity hides the true impact. A parent alert at Severity 3 (average of 1 and 5) does not promote to an incident. The correct answer is always: if any child is Severity 1, the parent is Severity 1."),
        ("Should advanced correlation rules replace or supplement the basic CI-level grouping from AP-08?",
         "Supplement. Advanced correlation rules are additive — they create higher-level parent alerts that group lower-level CI alerts. The CI-level grouping from AP-08 continues to function.",
         "Removing CI-level grouping in favour of advanced correlation is risky because advanced rules may miss alerts that do not match the multi-source pattern. Both layers working together produces the best operator experience."),
    ],
    dependencies=[
        ("CI-level correlation rules working (AP-08, Workbook 02)", "Pending", "ECS", "Before Sprint 3", "Advanced correlation builds on top of CI-level grouping; must be stable first"),
        ("Event sources confirmed and validated for all in-scope monitoring tools (AP-08, Workbook 01)", "Pending", "ECS", "Sprint 1", "Cross-source correlation requires all sources to be sending events reliably"),
        ("IT Ops team historical incident pattern interview completed", "Pending", "ECS", "Sprint 3, Wk 1", "Advanced correlation rules must be designed from real incident patterns; interview is a prerequisite"),
    ],
    config_sections=[
        ("Multi-Source Correlation Scenarios", [
            ("Scenario A: Network switch failure cascade", "Triggers: SolarWinds network alert (switch) + Dynatrace application alerts (servers in the same segment) within 10 minutes. Parent: 'Network Segment Impact — [Switch CI]'.", "Customer to confirm which network segments have the highest P1 exposure", True),
            ("Scenario B: Database overload cascade", "Triggers: Database monitoring alert (disk/CPU/connections) + application performance alert (response time degradation) within 20 minutes. Parent: 'Database Impact — [DB CI]'.", "20-minute window to account for application layer cascade lag", True),
            ("Scenario C: Storage failure cascade", "Triggers: Storage monitoring alert + VM alerts (same datastore) + application availability alerts within 15 minutes. Parent: 'Storage Impact — [Storage CI]'.", "Customer to confirm which datastores host the highest-priority VMs", True),
            ("Additional scenarios (Phase 2)", "Customer IT Ops to identify from post-incident reviews", "Build additional scenarios from 30-day production incident data analysis", True),
        ]),
        ("Correlation Rule Configuration", [
            ("Default correlation window", "10 minutes", "Adjust per scenario; see individual scenario notes above", False),
            ("Parent alert naming convention", "[Pattern Name] — [Root Cause CI] — [Timestamp]", "Consistent naming makes parent alerts immediately recognizable", False),
            ("Parent alert severity rule", "Severity = MAX(child alert severities)", "Never average; highest child severity = parent severity", False),
            ("Maximum child alerts per parent", "50 (OOTB default)", "Cap prevents a single parent alert from aggregating an entire storm; storm detection handles high-volume events", False),
        ]),
    ],
    raci_rows=[
        ("Incident pattern interview with IT Ops team", "R", "C", "ECS leads the interview; IT Ops team provides real incident examples"),
        ("Multi-source correlation scenario design", "R", "C", "ECS designs based on interview findings; IT Ops lead validates"),
        ("Advanced correlation rule configuration", "R", "I", "ECS configures; customer validates in UAT"),
        ("Cross-source correlation testing", "R", "C", "ECS generates synthetic multi-source events; IT Ops validates parent alert grouping"),
        ("Post-go-live rule tuning (30-day review)", "R", "C", "ECS adjusts correlation windows based on production data; customer approves"),
    ],
    consultant_guide_sections=[
        ("The Incident Pattern Interview Is Essential",
         "Do not design advanced correlation rules from theoretical alert taxonomy. Sit with the IT Ops team and ask: 'Walk me through the last three P1 incidents. Which monitoring tools fired? In what order? How long after the root cause did each tool fire?' That conversation produces more useful correlation rule designs than any documentation."),
        ("Test With Real Alert Sequences, Not Individual Events",
         "Advanced correlation testing requires generating a sequence of synthetic events from different sources within the correlation window. Send a network alert from SolarWinds, then application alerts from Dynatrace 3 minutes later, then watch the workspace. If the parent alert does not appear, the correlation rule is wrong. This cannot be tested with a single synthetic event."),
        ("The Window Calibration Problem",
         "The correlation window must be wide enough to catch the cascade but narrow enough to avoid false groupings. If the window is 30 minutes, two unrelated incidents that happen 25 minutes apart will be incorrectly grouped. Use historical incident timeline data to set the window at 1.5× the observed cascade lag. If cascade lag varies widely, use a narrow window and accept that some correlations will be missed — false positives are worse than missed correlations."),
    ],
    adoption_rows=[
        ("'We want one correlation rule that catches every multi-source incident pattern.'",
         "Build separate correlation rules per scenario. One global rule produces false groupings that destroy operator confidence within 2 weeks.",
         "A global correlation rule that catches 'any two alerts from any source within 30 minutes' will group completely unrelated incidents. Every incorrect grouping requires operator time to undo and reduces trust in the system.",
         "'Separate rules per scenario give you the accuracy to justify the workflow change. A wrong correlation is worse than no correlation — your operators will turn the feature off if it groups unrelated incidents.'",
         "Never. Per-scenario rules are non-negotiable for quality."),
    ],
    snmap_sections=[
        ("Advanced Correlation Tables", [
            ("Correlation rule table", "em_correlation_rule", "Advanced multi-source rules; same table as basic CI-level rules, additional conditions"),
            ("Parent-child alert linkage", "em_alert.parent_alert", "All child alerts reference the parent alert sys_id"),
            ("Correlation event table", "em_correlation_event", "Logs which events contributed to each correlation rule evaluation"),
        ]),
        ("OOTB Features Used", [
            ("Multi-Source Correlation Rules", "Cross-source alert grouping based on CI relationship and time window", "Configured via Event Management > Administration > Correlation Rules; supports scripted conditions"),
            ("Parent Alert Hierarchy", "Visual parent-child alert grouping in the Operator Workspace", "OOTB workspace feature; no custom development"),
        ]),
    ],
)


# =============================================================================
# WORKBOOK 7 — Analytics and KPIs
# =============================================================================
wb7 = TabContent(
    workbook_title="07 — Analytics and KPIs",
    pack_name=PACK_NAME,
    purpose=(
        "Defines the Performance Analytics dashboards, KPI indicators, and reporting structure "
        "for Event Management. Analytics is what transforms Event Management from an operational "
        "tool into a strategic platform — it is the evidence base for continuous improvement, "
        "capacity planning, and stakeholder reporting."
    ),
    who_fills=(
        "ECS Solution Architect with Service Desk Manager. "
        "KPI targets must be approved by the IT Manager before dashboard publication."
    ),
    sprint_window="Sprint 4–5",
    estimated_effort="6–8 hours including indicator design, dashboard build, and management walkthrough",
    related_workbooks=["AP-09 Workbook 03 — AIOps Integration", "AP-09 Workbook 05 — Remediation Workflows"],
    success_criteria=[
        "Event Management PA dashboard is accessible to the Service Desk Manager and IT Manager.",
        "Core KPI indicators are collecting data and trending correctly.",
        "Weekly automated report is scheduled and tested.",
        "KPI targets are agreed, documented, and visible on the dashboard.",
        "Management walkthrough of the dashboard is completed before go-live.",
    ],
    process_decisions=[
        ("Who is the primary audience for the Event Management analytics dashboard?",
         "Two audiences: (1) Service Desk Manager — operational dashboard updated daily; (2) IT Manager — executive summary dashboard updated weekly. Build both separately rather than combining into one.",
         "A single dashboard serving both audiences satisfies neither. The Service Desk Manager needs granular operational data; the IT Manager needs trend summaries and KPI traffic lights. Separate dashboards serve both audiences correctly."),
        ("What are the three most important KPIs to track?",
         "CI correlation rate (measures CMDB quality and event coverage), alert-to-incident promotion rate for Severity 1/2 (measures Event Management reliability), and MTTR delta (measures the business value of Event Management automation).",
         "These three KPIs tell the full story: correlation rate = data quality, promotion rate = system reliability, MTTR delta = business impact. Every other metric is secondary to these three."),
        ("How frequently should the analytics data be collected?",
         "Hourly collection for operational indicators (alert volume, promotion rate). Daily collection for trend indicators (CI correlation rate, MTTR). Weekly calculation for executive summary indicators.",
         "Over-collecting analytics data degrades instance performance. Hourly is the right collection interval for operational data; daily is sufficient for trend data."),
    ],
    dependencies=[
        ("Performance Analytics plugin activated and baseline PA configured", "Pending", "ECS", "Sprint 3", "PA must be active and collecting before Event Management indicators can be built"),
        ("30 days of production Event Management data for baseline measurement", "Pending", "ECS", "Sprint 4", "KPI baselines require production data; cannot set meaningful targets without a baseline"),
        ("IT Manager approval on KPI targets", "Pending", "Customer", "Sprint 5, Wk 1", "Dashboard KPI targets must be IT Manager-approved before publication"),
    ],
    config_sections=[
        ("Core KPI Indicators", [
            ("CI correlation rate", "Target: ≥ 85% at go-live; ≥ 95% by 90 days. Calculation: correlated alerts / total alerts.", "Measures CMDB quality and event source coverage", False),
            ("Alert-to-incident promotion rate (Sev 1/2)", "Target: 100%. Calculation: promoted incidents / total Sev 1-2 alerts.", "Measures Event Management reliability for critical alerts", False),
            ("Auto-resolution rate", "Target: ≥ 70% of promoted incidents. Calculation: auto-resolved incidents / total promoted incidents.", "Measures monitoring tool recovery signal quality and alert closure rule accuracy", False),
            ("Mean time to alert (event → alert)", "Target: < 60 seconds. Calculation: em_alert.opened_at − em_event.created (median).", "Measures MID Server and event processing performance", False),
            ("Alert acknowledgement within SLA", "Target: ≥ 90%. Calculation: alerts acknowledged within SLA window / total alerts.", "Measures operator responsiveness; drives workspace and staffing decisions", False),
            ("Noise reduction rate (post-AIOps)", "Target: ≥ 30% at 60 days. Calculation: (baseline alert volume − current alert volume) / baseline.", "Measures AIOps effectiveness; report only after AIOps is activated", False),
            ("Remediation success rate (if RBA in scope)", "Target: ≥ 85%. Calculation: successful remediations / total attempts.", "Measures RBA reliability; report per remediation scenario", False),
        ]),
        ("Dashboard Configuration", [
            ("Operational dashboard (Service Desk Manager)", "Daily updated; includes: open alerts by severity, SLA compliance heat map, top 5 CI types by alert volume, promotion rate gauge, current AIOps noise reduction", "Service Desk Manager to confirm required widgets during UAT", True),
            ("Executive dashboard (IT Manager)", "Weekly updated; includes: KPI traffic light (target vs actual), MTTR trend, 4-week alert volume trend, top 5 unresolved alerts, AIOps ROI (alerts auto-resolved × avg MTTR)", "IT Manager to confirm dashboard scope before Sprint 5 build", True),
            ("Automated weekly report", "Email to IT Manager every Monday 7:00 AM with PA data export", "ECS to configure the scheduled PA report; confirm recipient list", True),
        ]),
    ],
    raci_rows=[
        ("KPI target agreement", "R", "C", "ECS proposes targets based on industry benchmarks; IT Manager approves"),
        ("PA indicator configuration", "R", "I", "ECS builds; customer validates data accuracy"),
        ("Dashboard build (operational and executive)", "R", "C", "ECS builds; Service Desk Manager and IT Manager review and confirm layout"),
        ("Management dashboard walkthrough", "R", "I", "ECS leads the walkthrough; Service Desk Manager and IT Manager attend"),
        ("Weekly report scheduling", "R", "C", "ECS configures; IT Manager confirms recipient list and format"),
        ("Monthly KPI review cadence (post go-live)", "R", "C", "ECS leads the monthly review; IT Manager owns the KPI target adjustment decisions"),
    ],
    consultant_guide_sections=[
        ("The MTTR Delta Is the Business Case",
         "The single most compelling metric for Event Management ROI is the MTTR delta — the difference in mean time to resolve incidents that were auto-promoted vs. incidents that were manually created. Measure this at 30 and 60 days. A 20% MTTR reduction for Event Management-promoted incidents translates directly into reduced business impact time and is the most persuasive evidence for continuing investment."),
        ("Build the Baseline Before Go-Live",
         "Measure the current MTTR, alert volume, and incident creation time from the legacy system or manual process before Event Management goes live. Without a baseline, the post-go-live metrics have no reference point and the improvement cannot be quantified. The baseline measurement takes 30 minutes in the old system and saves months of 'we think it got better' conversations."),
        ("Weekly Reports Build Stakeholder Confidence",
         "The weekly automated report to the IT Manager is the most important relationship-maintenance activity in the post-go-live period. It shows the system is working, shows improvement over time, and proactively surfaces issues before they become escalations. Schedule the first report for Day 7 post-go-live, not Day 30."),
    ],
    adoption_rows=[
        ("'We want custom reports that are not available in the OOTB PA dashboard.'",
         "Use PA report builder for custom views; export to PDF or email schedule for distribution. Most Event Management metrics are already PA indicators.",
         "Custom reporting development is rarely needed because PA's report builder handles most custom metric views without code.",
         "'Show me the specific report format you need — PA report builder handles most custom views in configuration, not code. Let us try that first before scoping a development item.'",
         "Only if the metric requires a calculation that PA's formula builder cannot express."),
    ],
    snmap_sections=[
        ("PA Event Management Indicators", [
            ("OOTB EM indicators", "em_alert, em_event, task tables", "Performance Analytics > Indicator Sources for Event Management tables"),
            ("Custom indicator source", "PA Indicator Source builder", "For custom KPI calculations not available in OOTB indicators"),
        ]),
        ("OOTB Features Used", [
            ("Performance Analytics", "KPI collection, trending, and dashboard reporting", "Core PA license required; Event Management indicators available OOTB"),
            ("Scheduled Reports", "Automated email distribution of PA dashboard data", "Configured via Performance Analytics > Scheduled Data Collections + Reports"),
        ]),
    ],
)


# =============================================================================
# WORKBOOK 8 — Hypercare and Maturity
# =============================================================================
wb8 = TabContent(
    workbook_title="08 — Hypercare and Maturity",
    pack_name=PACK_NAME,
    purpose=(
        "Defines the 30/60/90-day hypercare activities, tuning checkpoints, and operator maturity "
        "framework for Event Management post-go-live. Hypercare is where the Event Management program "
        "moves from 'working' to 'optimized.' Without a structured hypercare plan, the program "
        "stabilizes at 70% of its potential and the tuning never happens."
    ),
    who_fills=(
        "ECS Delivery Manager with Service Desk Manager and IT Manager. "
        "Hypercare is a joint accountability between ECS and the customer."
    ),
    sprint_window="Go-Live + 90 days (Hypercare period)",
    estimated_effort="2–4 hours per checkpoint (3 checkpoints = 6–12 hours total ECS effort)",
    related_workbooks=["All AP-08 and AP-09 workbooks", "AP-09 Workbook 07 — Analytics and KPIs"],
    success_criteria=[
        "30-day checkpoint: all KPIs are measured and compared to targets; top 3 tuning actions identified.",
        "60-day checkpoint: AIOps noise reduction ≥ 30%; correlation rate ≥ 90%; all P1/P2 alerts auto-promoting.",
        "90-day checkpoint: operator maturity assessment completed; Phase 2 scope agreed.",
        "Customer operations team can manage and tune Event Management without ECS support for routine operations.",
        "Phase 2 scope document is agreed by IT Manager at the 90-day checkpoint.",
    ],
    process_decisions=[
        ("Who owns Event Management operations after go-live?",
         "Designate a named ServiceNow Platform Admin or Event Management Admin who owns day-to-day rule maintenance, operator onboarding, and threshold tuning. This person should have the evt_mgmt_admin role and has completed ECS's operator certification process.",
         "Without a named owner, Event Management configurations drift as team members change. The admin designation must happen before go-live, not after the first configuration problem."),
        ("What is the criteria for escalating from hypercare to a formal ECS engagement?",
         "Escalate if: CI correlation rate < 75% at 60 days, more than 3 auto-remediation failures per week, more than 5 false storm alerts per week, or operator workspace load time > 5 seconds.",
         "Clear escalation criteria prevent both under-escalation (problems that fester) and over-escalation (ECS involvement for issues the customer admin can resolve). These thresholds are the trigger for a formal post-go-live assessment."),
        ("What does the Phase 2 scope include?",
         "Standard Phase 2 candidates: Service Mapping for Discovery-derived service maps, AIOps advanced noise reduction, additional remediation scenarios, SIEM integration (Splunk/QRadar), and capacity planning automation.",
         "Phase 2 scope is defined at the 90-day checkpoint using actual production data — not speculative requirements from pre-go-live workshops. Production data always reveals the most valuable next investments."),
    ],
    dependencies=[
        ("All AP-08 and AP-09 workbooks completed and validated in UAT", "Pending", "ECS", "Before Go-Live", "Hypercare assumes all Foundations and Realization configurations are in place"),
        ("Named Event Management Admin designated and trained", "Pending", "Customer", "Go-Live", "Admin must be in place before hypercare begins"),
        ("PA dashboards live and KPI baselines established (Workbook 07)", "Pending", "ECS", "Go-Live", "Hypercare checkpoint measurements depend on PA dashboards being operational"),
    ],
    config_sections=[
        ("30-Day Hypercare Checkpoint", [
            ("KPI measurement", "Compare CI correlation rate, promotion rate, auto-resolution rate, and alert acknowledgement rate against go-live targets", "ECS to pull from PA dashboard; present to Service Desk Manager", False),
            ("Top 3 tuning actions", "Identify the 3 highest-impact tuning actions from the first 30 days of production data", "Common actions: adjust storm thresholds, fix CI correlation gaps, tune suppression rules", False),
            ("Operator feedback review", "Review operator feedback on similar alert suggestions and ML recommendations", "High dismiss rates indicate poor model quality or irrelevant suggestions", False),
            ("MID Server health check", "Confirm MID Server queue depth < 1,000, no event lag, and auto-upgrade confirmed working", "MID Server issues that were manageable in testing often surface at production volume", False),
        ]),
        ("60-Day Hypercare Checkpoint", [
            ("AIOps noise reduction measurement", "Target: ≥ 30% reduction vs. go-live baseline", "If < 30%, review ML training data quality and operator feedback rates", False),
            ("CI correlation rate target", "Target: ≥ 90%", "Identify and remediate top 20 uncorrelated node values from the Event Triage queue", False),
            ("Advanced correlation validation", "Confirm multi-source correlation rules are grouping correctly; review false positive rate", "Target: < 10% false positive rate (parent alerts that should not have been grouped)", False),
            ("Operator maturity pulse check", "Survey designated operators: 'Is the workspace your primary alert management tool?' Target: 100% yes.", "If operators are still using monitoring tool dashboards as primary, the workspace adoption has failed; identify the obstacle", True),
        ]),
        ("90-Day Checkpoint and Phase 2 Planning", [
            ("Full KPI review", "Compare all 7 core KPIs against targets; identify sustained gaps vs. met targets", "Present to IT Manager as the Event Management program report card", False),
            ("Operator maturity assessment", "Can the designated admin manage rules, tune thresholds, and onboard new operators without ECS support?", "If not, plan an ECS admin coaching session before formal ECS engagement ends", False),
            ("Phase 2 scope agreement", "Based on 90 days of production data, agree the Phase 2 scope with IT Manager", "Phase 2 candidates: Service Mapping, advanced AIOps, additional RBA scenarios, SIEM integration", True),
            ("Formal ECS engagement closeout", "Document what was built, what is operating, and what Phase 2 will add; sign off with IT Manager", "This document is the foundation for the Phase 2 SOW", False),
        ]),
    ],
    raci_rows=[
        ("30-day checkpoint facilitation", "R", "C", "ECS leads; Service Desk Manager and designated admin attend"),
        ("KPI data pull for checkpoints", "R", "I", "ECS pulls from PA dashboard; customer reviews"),
        ("Tuning actions implementation", "R", "C", "ECS implements agreed tuning actions; customer admin observes for knowledge transfer"),
        ("Operator maturity pulse check (survey)", "R", "I", "ECS administers and reports; Service Desk Manager reviews results"),
        ("Phase 2 scope definition", "R", "C", "ECS drafts based on production data; IT Manager approves scope"),
        ("Formal engagement closeout sign-off", "C", "R", "Customer IT Manager signs off; ECS prepares the closeout document"),
        ("Ongoing Event Management administration post-closeout", "I", "R", "Customer designated admin owns; ECS available for Phase 2 engagement"),
    ],
    consultant_guide_sections=[
        ("The 90-Day Window Is Everything",
         "Event Management programs that are not actively managed in the first 90 days stabilize at 60–70% of their potential. The suppression rules never get tuned. The correlation windows never get calibrated. The AIOps model never gets enough operator feedback. Schedule the 30/60/90-day checkpoints before go-live, not after. Put them in the project plan as deliverables, not optional check-ins."),
        ("The Named Admin Is the Program",
         "The designated Event Management admin is the difference between a program that evolves and one that fossilizes. Find this person before go-live. Give them the evt_mgmt_admin role. Walk them through every rule, every threshold, every workflow. The training session is not optional — it is the knowledge transfer that makes the program sustainable."),
        ("Phase 2 Is Sold at the 90-Day Checkpoint",
         "The 90-day checkpoint is the best time to scope Phase 2. The customer has 90 days of production data and can see exactly what is working and what is not. ECS has the credibility of a successful go-live. The IT Manager is engaged with the program results. This is the natural moment to say: 'Based on what we have built and what we can see in the data, here is what Phase 2 should include.'"),
        ("Document the Escalation Criteria Explicitly",
         "Before go-live, get written agreement from the IT Manager on the escalation criteria (the thresholds above). This protects both ECS and the customer. When the 30-day checkpoint shows CI correlation at 78%, there is no ambiguity — it is below the 75% escalation threshold, a formal review is triggered, and ECS is engaged. Without agreed escalation criteria, every sub-target measurement becomes a negotiation."),
    ],
    adoption_rows=[
        ("'We do not need the 90-day hypercare structure — our team will manage it.'",
         "Engage in the three checkpoint structure regardless of the customer's confidence level. Checkpoints are lightweight (2 hours each) and the data they produce is essential for Phase 2 scoping.",
         "Every Event Management program that skips hypercare checkpoints has the same outcome: the program is declared successful at go-live and then quietly ignored until a major incident reveals the gaps.",
         "'The checkpoints take 2 hours each and give you 90 days of trend data for the Phase 2 conversation. That data is worth more than the 6 hours — it is what makes Phase 2 a no-brainer approval.'",
         "Only if the customer is a highly mature ServiceNow shop with an existing admin team and proven self-sufficiency on other platform areas."),
    ],
    snmap_sections=[
        ("Hypercare Measurement Sources", [
            ("CI correlation rate", "PA indicator on em_alert table", "Correlated alerts / total alerts; trend weekly"),
            ("Alert promotion rate", "PA indicator on em_alert + task tables", "Promoted incidents / Sev 1-2 alerts; trend weekly"),
            ("Operator feedback rate", "ml_operator_feedback table", "Accept + dismiss counts; ratio is model quality indicator"),
            ("MID Server queue depth", "ecc_queue count (input queue)", "Monitor daily; alert if > 1,000 during non-storm periods"),
        ]),
        ("OOTB Tuning Capabilities", [
            ("Correlation window adjustment", "em_correlation_rule.time_window", "Adjust per rule; requires ECS or designated admin"),
            ("Storm threshold adjustment", "em_correlation_rule.count_threshold", "Increase if false storm alerts; decrease if real storms are missed"),
            ("Suppression rule expansion", "em_event_rule (suppression type)", "Add new suppression rules from Event Triage queue analysis"),
            ("AIOps sensitivity tuning", "Predictive AIOps > Administration > Sensitivity", "Reduce sensitivity if too many false positives; increase if too many misses"),
        ]),
    ],
)


# =============================================================================
# README docx
# =============================================================================
def build_readme():
    meta = DocMeta(
        eyebrow="ECS Federal · ServiceNow Practice",
        title="Event Management Realization\nAccelerator Pack",
        subtitle="AP-09 — Sprint 3–5 Advanced Configuration Workbooks",
        audience="Internal · Shared with Customer",
        version="1.0",
        doc_id="AP-09",
        companion_to="AP-08 Event Management Foundations Pack · INT-HT-18 How-To Guide (pending) · CLT-WP-Event Workshop Pre-Read",
    )
    doc = EcsDocument(meta)

    doc.h1("About This Pack")
    doc.para(
        "The Event Management Realization Accelerator Pack contains eight Excel workbooks that guide "
        "the ECS team and the customer through the advanced configuration required to move from a "
        "working Event Management Foundations implementation to a fully optimized, intelligent, and "
        "self-improving event operations program. This pack is the complement to AP-08 "
        "(Event Management Foundations) and is sequenced for Sprint 3–5 and the 90-day hypercare window."
    )

    doc.h1("Pack Contents")
    doc.table(
        headers=["#", "Workbook", "Primary Owner", "Sprint / Phase"],
        rows=[
            ["01", "Service Health Maps", "ECS + Customer Service Owners", "Sprint 3–4"],
            ["02", "Storm Management", "ECS Solution Architect", "Sprint 3–4"],
            ["03", "AIOps Integration", "ECS SA + Customer IT Manager", "Sprint 4–5"],
            ["04", "Alert Intelligence", "ECS Solution Architect", "Sprint 3–4"],
            ["05", "Remediation Workflows", "ECS + Customer IT Ops Lead", "Sprint 4–5"],
            ["06", "Advanced Correlation", "ECS Solution Architect", "Sprint 3–4"],
            ["07", "Analytics and KPIs", "ECS + Service Desk Manager", "Sprint 4–5"],
            ["08", "Hypercare and Maturity", "ECS Delivery Manager", "Go-Live + 90 days"],
        ]
    )

    doc.h1("Sequencing This Pack")
    doc.para(
        "AP-09 runs after AP-08 (Foundations) is stable in production. The recommended sequence within "
        "this pack: start Workbooks 01 (Service Health Maps) and 06 (Advanced Correlation) in Sprint 3 "
        "once CI correlation rate exceeds 85%. Workbooks 02 (Storm Management) and 04 (Alert Intelligence) "
        "follow in Sprint 3–4. Workbooks 03 (AIOps) and 05 (Remediation Workflows) require 30 days of "
        "production data and activate in Sprint 4–5. Workbooks 07 (Analytics) and 08 (Hypercare) run "
        "concurrently with the rest of Sprint 4–5 and continue through the 90-day post-go-live window."
    )

    doc.h1("Prerequisites from AP-08")
    doc.table(
        headers=["Prerequisite", "Target", "Risk If Not Met"],
        rows=[
            ["CI correlation rate", "≥ 85%", "Service health maps and AIOps produce inaccurate results"],
            ["Alert promotion working for Sev 1/2", "100%", "Storm management and advanced correlation cannot be tested reliably"],
            ["MID Server stable (no queue backlog)", "Queue depth < 100 during normal ops", "Remediation workflows time out; event processing lag masks correlation accuracy"],
            ["30 days of clean production event data", "Required for AIOps training", "AIOps activation produces worse results than no AIOps"],
        ]
    )

    doc.h1("KPI Progression Targets")
    doc.table(
        headers=["KPI", "Go-Live", "30 Days", "60 Days", "90 Days"],
        rows=[
            ["CI correlation rate", "≥ 85%", "≥ 88%", "≥ 92%", "≥ 95%"],
            ["Alert-to-incident promotion (Sev 1/2)", "100%", "100%", "100%", "100%"],
            ["Auto-resolution rate", "≥ 60%", "≥ 65%", "≥ 70%", "≥ 75%"],
            ["AIOps noise reduction", "N/A (training)", "10–15%", "≥ 30%", "≥ 50%"],
            ["Operator acknowledgement within SLA", "≥ 80%", "≥ 85%", "≥ 90%", "≥ 93%"],
            ["Remediation success rate", "≥ 80%", "≥ 85%", "≥ 88%", "≥ 90%"],
        ]
    )

    doc.h1("Phase 2 Scope Candidates")
    doc.para(
        "The 90-day hypercare checkpoint (Workbook 08) is the right time to scope Phase 2. "
        "Common Phase 2 investments — all informed by 90 days of production Event Management data — "
        "include: Discovery-derived Business Service maps (replacing manual maps from Workbook 01), "
        "SIEM integration (Splunk or QRadar feeding events into ServiceNow), expanded RBA remediation "
        "scenarios for cloud workloads, and Performance Analytics capacity planning dashboards that "
        "correlate event volume trends with CI lifecycle planning."
    )

    out_path = os.path.join(OUT, "00_README_Event_Management_Realization_Pack.docx")
    doc.save(out_path)
    print(f"  README → {out_path}")


# =============================================================================
# BUILD
# =============================================================================
if __name__ == "__main__":
    print("Building AP-09 — Event Management Realization Accelerator Pack")
    print("=" * 65)

    workbooks = [
        (wb1, "01_service_health_maps.xlsx"),
        (wb2, "02_storm_management.xlsx"),
        (wb3, "03_aiops_integration.xlsx"),
        (wb4, "04_alert_intelligence.xlsx"),
        (wb5, "05_remediation_workflows.xlsx"),
        (wb6, "06_advanced_correlation.xlsx"),
        (wb7, "07_analytics_and_kpis.xlsx"),
        (wb8, "08_hypercare_and_maturity.xlsx"),
    ]

    for content, filename in workbooks:
        path = os.path.join(OUT, filename)
        build_workbook(content, path)
        print(f"  ✓ {filename}")

    build_readme()
    print("  ✓ 00_README_Event_Management_Realization_Pack.docx")
    print("=" * 65)
    print("AP-09 complete — 8 workbooks + 1 README built.")
