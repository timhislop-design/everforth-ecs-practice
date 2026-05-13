"""
Build INT-AR-04 and INT-AR-05 — Event Management Adopt-vs-Re-engineer Cheatsheets
INT-AR-04: Event Management (alert sources, rules, promotion, CI correlation)
INT-AR-05: AIOps and Advanced Correlation (ML noise reduction, storm management, remediation)
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta


def build_cheatsheet(meta_kwargs, intro, table_rows, objections, footer_note, out_path):
    doc = EcsDocument(meta=DocMeta(**meta_kwargs), logo_path=LOGO)
    doc.add_cover_page()
    doc.page_break()

    doc.h1("How to Use This Cheatsheet", numbered=False)
    doc.para(intro)

    doc.callout(
        "Governance rule: Any item pattern flagged for Re-engineer goes into the Engagement "
        "Governance Triage Log before any scope commitment. No custom build without Delivery "
        "Manager review and customer sign-off."
    )

    doc.page_break()

    doc.h1("Pattern Decision Table")
    doc.para(
        "For each pattern encountered during Event Management discovery or workshops, call Adopt "
        "or flag for Re-engineer using the decision rule in the rightmost column. The Adopt path "
        "is the default — shift the burden of proof to the exception."
    )

    doc.table(
        headers=["Customer Pattern", "OOTB Adopt Path", "Re-engineer Trigger", "Decision Rule"],
        rows=table_rows,
        col_widths_in=[2.0, 2.2, 2.2, 2.96],
    )

    doc.page_break()

    doc.h1("Common Objections — Consulting Response")
    doc.para(
        "These objections surface in nearly every Event Management engagement. "
        "Use the responses below verbatim or adapt to the customer's language."
    )

    doc.table(
        headers=["Objection", "Consulting Response"],
        rows=objections,
        col_widths_in=[4.0, 5.36],
    )

    doc.page_break()
    doc.h1("Field Notes", numbered=False)
    doc.para(footer_note)

    doc.save(out_path)
    print(f"  Built → {out_path}")


# =============================================================================
# INT-AR-04 — Event Management
# =============================================================================
build_cheatsheet(
    meta_kwargs=dict(
        eyebrow="INTERNAL · ADOPT-VS-RE-ENGINEER CHEATSHEET",
        title="INT-AR-04\nEvent Management",
        subtitle="Pattern decision table for event sources, alert rules, CI correlation, and alert-to-incident promotion",
        audience="ECS Lead Consultant, Solution Architect",
        companion_to="AP-08 Event Management Foundations Pack · INT-FG-02 Sprint 1 Incident Facilitator Guide",
        doc_id="INT-AR-04",
        version="1.0",
        status="Released",
        running_header_label="Internal · Adopt-vs-Re-engineer · Event Management",
    ),
    intro=(
        "Use this cheatsheet during Event Management discovery and Sprint 0-1 configuration sessions. "
        "Every pattern listed here has appeared in at least three prior ECS engagements. "
        "The Adopt path is the OOTB answer. The Re-engineer trigger is the narrow set of circumstances "
        "where OOTB genuinely cannot meet the requirement. Most of the time, the customer's resistance "
        "to the Adopt path is familiarity bias, not a genuine OOTB limitation."
    ),
    table_rows=[
        # Alert Sources
        ("Customer wants to send pre-correlated alerts from the monitoring tool directly (not raw events).",
         "Send raw events to em_event. ServiceNow Event Management correlation engine produces the alert layer from raw events.",
         "Re-engineer: never. Pre-correlated input bypasses the em_event table, breaking the correlation engine, CI correlation, and the CMDB-backed alert lifecycle.",
         "Adopt always. If the monitoring tool cannot send raw events, configure it to send raw before the connector build. Pre-correlated input is an architecture error, not a configuration choice."),
        ("Customer wants one service account for all monitoring tool connectors.",
         "Dedicate one service account per monitoring tool source (svc_em_[tool]). OOTB audit trails per source depend on this.",
         "Re-engineer: never. Shared credentials across sources make audit trails meaningless and create a single point of credential failure.",
         "Adopt always. Customer IT security may resist creating multiple accounts — explain the audit trail requirement."),
        ("Customer wants to route events from a SaaS monitoring tool (e.g., Datadog) without a MID Server.",
         "Direct REST push from Datadog to ServiceNow em_event REST API endpoint. No MID Server required for cloud-to-cloud.",
         "Re-engineer: not applicable. Direct REST is OOTB — this is the right architecture for cloud-native sources.",
         "Adopt always for cloud-native tools with direct internet access to ServiceNow."),
        # Event Rules
        ("Customer wants to add custom columns to the em_event table for tool-specific metadata.",
         "Use the OOTB additional_info (JSON) field on em_event. Tool-specific metadata is stored as JSON and surfaced via transform rules.",
         "Re-engineer if: the metadata requires indexed database queries for performance-sensitive reporting (extremely rare). Even then, promote to em_alert, not em_event.",
         "Adopt for all metadata that does not require indexed querying. Never add columns to em_event — it is a high-volume transient table and schema changes degrade index performance."),
        ("Customer wants to suppress all events during maintenance windows globally.",
         "Use OOTB em_maintenance_schedule: suppress by CI + time window, not globally by time. All other events process normally.",
         "Re-engineer if: customer has a contractual requirement for zero alert generation during defined maintenance periods (e.g., change freeze windows). Even then, scope the suppression to specific CIs, not globally.",
         "Adopt for most cases. Global time-based suppression hides real incidents during maintenance windows. Suppress selectively by CI + window."),
        ("Customer wants event rules to be different per environment (prod vs. non-prod).",
         "Use CI attribute filtering in OOTB event rules: check cmdb_ci.environment and apply different rule logic within the same rule set.",
         "Re-engineer: never. Separate rule sets per environment double maintenance burden and cause rules to drift out of sync over time.",
         "Adopt always. Environment-aware filtering within a single rule set is more maintainable than separate rule sets."),
        # CI Correlation
        ("Customer's monitoring tool identifies CIs by a custom tag or property not in the CMDB.",
         "Add the custom identifier as a CI attribute and configure a CI Identifier Rule to lookup by that attribute. OOTB CI identifier rules support any cmdb_ci attribute.",
         "Re-engineer if: the identifier is too dynamic or transient to store reliably in the CMDB (e.g., rotating container IDs). In that case, use additional_info for metadata and accept lower correlation rates for dynamic infrastructure.",
         "Adopt if the identifier is stable enough to store in the CMDB. Flag dynamic infrastructure as a Phase 2 Discovery/cloud connector item."),
        ("Customer wants Event Management to auto-create CMDB CIs when an event arrives for an unknown node.",
         "Route uncorrelated events to the Event Triage assignment group. Use Discovery or import to add missing CIs from the triage queue analysis.",
         "Re-engineer: never. Auto-creating CIs from event data produces low-quality records with no ownership, no lifecycle data, and no relationships.",
         "Adopt always. The triage queue is the safety net and the CMDB improvement driver. Show customers the triage-to-CMDB improvement loop."),
        # Alert Promotion
        ("Customer wants every alert to auto-create an incident, including Severity 4 and 5.",
         "Use the OOTB operator workspace for Severity 4-5 alerts. Operators review and manually promote if warranted. Auto-promote Severity 1-2 only.",
         "Re-engineer if: regulatory requirement mandates an ITSM record for every alert. Even then, route low-severity auto-promotions to a dedicated low-priority queue.",
         "Adopt for all cases without a regulatory mandate. Auto-promoting Severity 4-5 fills the incident queue with non-actionable records within hours."),
        ("Customer wants auto-resolved incidents to reach Closed state immediately (not Resolved).",
         "Auto-resolve to Resolved state (state = 6). Closed state (state = 7) requires closure confirmation. Resolved is the correct landing state for auto-resolution.",
         "Re-engineer if: customer has explicitly removed the closure confirmation step from their Incident workflow AND has a named owner for the resulting audit gap.",
         "Adopt for all standard deployments. Closed without closure confirmation is a governance risk. Resolved is correct and operationally appropriate."),
    ],
    objections=[
        ("'Our monitoring tool already correlates alerts. Why does ServiceNow need to do it again?'",
         "ServiceNow correlates alerts across all tools into a single operator view, links them to CMDB CIs, and drives automated incident creation — none of which the individual monitoring tool can do across the full stack. The monitoring tool is excellent at detecting issues in its domain. ServiceNow is where all those domains meet. Keep both — each does what it is best at."),
        ("'We will lose visibility during maintenance windows if ServiceNow suppresses events.'",
         "We are not suppressing globally — we are suppressing by CI and by window. Every CI that is not in a confirmed maintenance window continues to generate alerts normally. The only events suppressed are the ones you have explicitly told us are expected. Unexpected events during maintenance windows still produce alerts."),
        ("'CI correlation is too complex — our monitoring tool uses hostnames that don't match CMDB names.'",
         "This is the most common CI correlation challenge, and OOTB CI Identifier Rules handle it. We configure a secondary identifier rule that matches the monitoring tool's hostname format to the CMDB attribute that stores it (fqdn, asset_tag, or a custom attribute). The gap analysis report shows us exactly which hostnames are failing correlation — that is our CMDB remediation list for Phase 2."),
        ("'If we auto-promote every Severity 3 alert, the incident queue will be flooded.'",
         "That is why we use the 15-minute delay rule for Severity 3: auto-promote only if the alert is still open and unacknowledged after 15 minutes. An operator who sees a Severity 3 alert and acknowledges it within 15 minutes has decided it does not need an incident yet — and the system agrees. The auto-promotion is the safety net for alerts that fall through the cracks."),
        ("'We need to track which monitoring tool created each alert for reporting.'",
         "The source field on em_alert is populated automatically from the event source configuration. Every alert has a source field that identifies the monitoring tool. OOTB Incident dashboards can be filtered or grouped by source. No custom development required."),
    ],
    footer_note=(
        "Key reference: AP-08 Event Management Foundations Accelerator Pack — workbooks 01 through 06 "
        "contain the detailed configuration decisions for every pattern in this table. "
        "When a pattern falls to Re-engineer, document it in the Engagement Governance Triage Log "
        "(INT-TBV-03) with the business justification and the scope impact estimate before any "
        "configuration work begins."
    ),
    out_path=os.path.join(HERE, "INT-AR-04_Event_Management_Cheatsheet_INTERNAL.docx"),
)


# =============================================================================
# INT-AR-05 — AIOps and Advanced Correlation
# =============================================================================
build_cheatsheet(
    meta_kwargs=dict(
        eyebrow="INTERNAL · ADOPT-VS-RE-ENGINEER CHEATSHEET",
        title="INT-AR-05\nAIOps and Advanced Correlation",
        subtitle="Pattern decision table for ML noise reduction, storm management, advanced correlation, and runbook automation",
        audience="ECS Lead Consultant, Solution Architect",
        companion_to="AP-09 Event Management Realization Pack · INT-AR-04 Event Management Cheatsheet",
        doc_id="INT-AR-05",
        version="1.0",
        status="Released",
        running_header_label="Internal · Adopt-vs-Re-engineer · AIOps and Advanced Correlation",
    ),
    intro=(
        "Use this cheatsheet during Event Management Realization workshops (Sprint 3-5) and AIOps "
        "design sessions. These patterns surface after the Foundations implementation is working "
        "and the customer is pushing for advanced capabilities. "
        "The OOTB AIOps and correlation features are more capable than most customers realize — "
        "the Adopt path almost always meets the requirement without custom development."
    ),
    table_rows=[
        # AIOps
        ("Customer wants AIOps to auto-resolve alerts without operator review.",
         "Use AIOps for noise reduction recommendations and human-in-the-loop promotion decisions. Auto-resolution comes from monitoring tool recovery events (OOTB alert closure rules), not the ML model.",
         "Re-engineer: never. ML models make mistakes, especially early in training. Auto-resolving on ML recommendations without human review creates invisible gaps where real incidents are suppressed.",
         "Adopt always. AIOps makes operators faster, not optional. Frame it as 10-second decisions instead of 2-minute investigations."),
        ("Customer wants to train the AIOps model on historical data from their old monitoring system.",
         "AIOps trains on em_event and em_alert data from the ServiceNow instance. 30-day production training period is required.",
         "Re-engineer: never. External monitoring data lacks the CMDB correlation, severity mapping, and source attribution that the ML model requires.",
         "Adopt always. Position the 30-day training period as an advantage: the model learns the new platform architecture, not the legacy system's patterns."),
        ("Customer wants custom ML algorithms to replace ServiceNow's AIOps model.",
         "Use the OOTB AIOps model with sensitivity tuning. The OOTB model is trained on ServiceNow's global event dataset and fine-tuned on the customer's own data.",
         "Re-engineer: only if the customer has a documented and proven custom ML algorithm that outperforms the OOTB model on their data. Requires a scoped integration project.",
         "Adopt for all standard deployments. Custom ML is a Phase 3+ investment and requires dedicated data science resources to maintain."),
        # Storm Management
        ("Customer wants to auto-close all alerts during a storm and start fresh after recovery.",
         "Use the OOTB storm parent alert model: individual alerts are linked to the storm parent but retained. After the storm, the triage queue and post-incident review use this data.",
         "Re-engineer: never. Auto-closing storm alerts destroys the post-incident audit trail and hides alerts for issues that did not self-resolve.",
         "Adopt always. The storm parent model is the right architecture. Demonstrate how the workspace de-clutters during a storm without closing individual alerts."),
        ("Customer wants a single global storm detection rule for all sources.",
         "Create one OOTB correlation rule per major event source with independently tuned thresholds. Network tools have different baseline volumes than application tools.",
         "Re-engineer: never. A global rule with a single threshold produces either excessive false positives for low-volume sources or missed detections for high-volume sources.",
         "Adopt per-source rules always. Separate rules with per-source thresholds are more accurate and independently tunable without affecting other sources."),
        ("Customer wants to suppress ALL events during a storm, including Severity 1.",
         "Suppress Severity 4-5 only during a storm window. Severity 1-3 continue as individual alerts linked to the storm parent.",
         "Re-engineer: never. Suppressing Severity 1-3 during a storm creates a window of complete blindness for P1 incidents that start during the storm.",
         "Adopt always. Severity 1-3 suppression during a storm is never acceptable. If the customer insists, escalate to Delivery Manager and document the risk in writing."),
        # Advanced Correlation
        ("Customer wants one correlation rule to group all multi-source incidents.",
         "Build one OOTB correlation rule per incident pattern (e.g., network cascade, database overload, storage failure). Per-pattern rules are more accurate than a global rule.",
         "Re-engineer: never. A single global rule groups unrelated incidents, destroying operator confidence within weeks.",
         "Adopt per-pattern rules always. Use the incident pattern interview (INT-FG-02) to identify the top 3-5 patterns before building rules."),
        ("Customer wants ML-based advanced correlation before 30 days of production data.",
         "Use OOTB rule-based correlation during the training period. ML correlation activates naturally once the AIOps model has sufficient data.",
         "Re-engineer: never. ML correlation on insufficient training data produces incorrect groupings that are worse than no correlation.",
         "Adopt rule-based correlation first. Transition to ML correlation naturally — do not force it early."),
        # Remediation
        ("Customer wants auto-remediation without any human approval step.",
         "Use OOTB RBA with approval-tier framework: low-risk actions (cache flush, log rotation) auto-execute; medium/high-risk actions (service restart, VM reboot) require operator approval.",
         "Re-engineer: only for low-risk, well-understood, fully reversible actions with a documented rollback plan and a named owner for failure review.",
         "Adopt the approval tier framework always. Document the specific approval tier for each action type in the Triage Log. Zero-approval for destructive actions is not acceptable."),
        ("Customer wants to trigger remediation from their monitoring tool directly.",
         "Trigger all remediation through ServiceNow RBA. OOTB RBA provides the ITSM record linkage, audit trail, and approval workflow that monitoring tool-triggered remediation bypasses.",
         "Re-engineer: never. Monitoring tool-triggered remediation is invisible to the ITSM system and creates a parallel, unaudited automation program.",
         "Adopt always. Runbook Automation through ServiceNow is the architecture. Monitoring tools detect; ServiceNow orchestrates."),
    ],
    objections=[
        ("'We have been using AIOps marketing numbers (80% noise reduction from day 1) to justify this project.'",
         "Reset expectations before go-live, not after. The realistic trajectory is 10-15% at day 30, 30% at day 60, 50%+ at day 90 with active operator feedback. Show customers the maturity curve now and let them re-calibrate their stakeholder messaging. Discovering the gap at day 30 is a trust crisis; discovering it before go-live is a planning conversation."),
        ("'Why can't the monitoring tool trigger the remediation directly? It already knows the fix.'",
         "The monitoring tool triggers the detection. ServiceNow orchestrates the response. The monitoring tool does not know whether the same CI already has an open incident, whether an approval is required by policy, or whether the fix should be logged in the audit trail. ServiceNow knows all of those things — and OOTB RBA gives you the orchestration layer without writing custom integration code."),
        ("'We want to see 95% noise reduction before we go live.'",
         "Noise reduction is a function of model maturity — it requires production data that does not exist yet. The right gate for go-live is a clean Foundations implementation with correct CI correlation, severity mapping, and suppression rules. Noise reduction is what grows from that foundation over the first 90 days. Holding go-live hostage to a metric that requires go-live data is a logical trap."),
        ("'Our team runs remediation scripts manually today. Why would we change that?'",
         "Manual scripts have no audit trail, no approval governance, and no ITSM record linkage. They work fine when the same person runs them every time and never makes a mistake under pressure. RBA gives you the same scripts with an approval step before they run, a work note on the incident after they run, and a metric on whether they worked. The scripts stay the same — the governance improves."),
        ("'We want to group all alerts from the same time period into one parent, regardless of source.'",
         "Time-based grouping without a shared root cause produces parent alerts that mix completely unrelated incidents — a server CPU alert and a network switch alert that happened to occur in the same 10-minute window are not related just because they are close in time. OOTB correlation uses CI relationship and source patterns to identify genuine groupings. Time is a condition, not a sufficient criterion."),
    ],
    footer_note=(
        "Key reference: AP-09 Event Management Realization Accelerator Pack — workbooks 02 through 06 "
        "contain the detailed configuration for every Realization pattern in this table. "
        "AIOps and advanced correlation decisions escalated to Re-engineer require Delivery Manager "
        "review, scope impact documentation in INT-TBV-03, and customer sign-off before any "
        "custom development begins. The OOTB answer should always be demonstrated first."
    ),
    out_path=os.path.join(HERE, "INT-AR-05_AIOps_Advanced_Correlation_Cheatsheet_INTERNAL.docx"),
)

print("INT-AR-04 and INT-AR-05 complete.")
