"""
build_AP19_PA.py -- AP-19 Performance Analytics Accelerator Pack
Covers: OOTB PA scope, indicator library, dashboard design,
scorecard configuration, and governance cadence.
Sprint window: Month 3 (Sprint 6)
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "03_Shared", "00_Templates_and_Branding"))
from accelerator_pack_builder import TabContent, build_workbook
from ecs_template import EcsDocument, DocMeta

PACK_DIR = HERE
PACK_NAME = "Performance Analytics Accelerator Pack"

wb1 = TabContent(
    workbook_title="01 -- PA Scope & Dashboard Inventory",
    pack_name=PACK_NAME,
    purpose="Define which OOTB Performance Analytics dashboards to activate, which audiences they serve, and the governance model for ongoing dashboard ownership.",
    who_fills="ECS Consultant leads. Customer IT Director and Process Owners confirm dashboard priorities.",
    sprint_window="Sprint 6 -- scope confirmed by Week 11",
    estimated_effort="2-3 hours with Customer IT Director and Process Owners",
    related_workbooks=["02 Indicator Library", "03 Dashboard Design", "04 Scorecard Configuration", "AP-20 Reporting & Stabilization"],
    success_criteria=[
        "OOTB dashboard inventory agreed for go-live.",
        "Dashboard owners named (one owner per dashboard).",
        "Audience confirmed for each dashboard (executive, manager, agent).",
        "PA license entitlement confirmed.",
        "Review cadence agreed (daily, weekly, monthly per dashboard).",
    ],
    process_decisions=[
        ("Which OOTB PA dashboards should be activated at go-live?",
         "Three OOTB dashboards: ITSM Executive Overview, Incident Management, and Service Desk Performance.",
         "These three cover the primary audiences (executive, manager, agent team lead) and use OOTB indicators that are already populated by ITSM data. No custom indicators needed for go-live."),
        ("Should custom PA indicators be built in Sprint 6?",
         "No custom indicators in 18-week scope. OOTB indicators only.",
         "Custom indicators require data collection activation, breakdowns, and threshold configuration -- each adds sprint scope. OOTB indicators are pre-configured and immediately populated."),
        ("Who owns each dashboard post-go-live?",
         "One named owner per dashboard. Owner is responsible for monthly review and keeping widgets current.",
         "Unowned dashboards become stale within 90 days. Named ownership drives accountability."),
        ("Should dashboards be on a fixed refresh schedule?",
         "Yes -- OOTB PA runs on nightly collection jobs. Executive dashboard refreshes daily; Incident and Service Desk dashboards refresh every 4 hours (OOTB default).",
         "Real-time refresh is not OOTB for PA indicators. Near-real-time (every 4 hours) is the correct expectation."),
    ],
    dependencies=[
        ("PA license confirmed (Performance Analytics Premium or included)", "Required", "Customer", "Before Sprint 6", "PA dashboards require license entitlement."),
        ("ITSM processes active (incidents, requests, changes)", "Required", "ECS", "Sprint 4 close", "PA indicators source from incident, request, and change tables."),
        ("Data collection jobs activated", "Required", "ECS", "Sprint 6 Wk 1", "PA data collection must be activated for each indicator to begin populating."),
    ],
    config_sections=[
        ("OOTB Dashboard Inventory", [
            ("ITSM Executive Overview", "Activate Sprint 6 Wk 1", "Audience: IT Director / CIO. KPIs: SLA compliance, open incidents by priority, resolution trends.", False),
            ("Incident Management Dashboard", "Activate Sprint 6 Wk 1", "Audience: IT Manager, Service Desk Manager. KPIs: volume, MTTR, backlog, first-call resolution.", False),
            ("Service Desk Performance", "Activate Sprint 6 Wk 1", "Audience: Service Desk Team Lead. KPIs: agent workload, reassignment rate, resolution by group.", False),
            ("Change Management Dashboard", "Activate Sprint 6 Wk 2 (if Change is in scope)", "Activate only if Change Management is active in the instance.", False),
            ("Custom dashboards", "Defer to Phase 2", "All custom indicator and dashboard builds are post-stabilization scope.", False),
        ]),
        ("Dashboard Ownership", [
            ("ITSM Executive Overview owner", "[Customer: IT Director name]", "Must have PA Viewer role minimum", True),
            ("Incident Management Dashboard owner", "[Customer: IT Manager name]", "Must have PA Viewer role minimum", True),
            ("Service Desk Performance owner", "[Customer: Service Desk Manager name]", "Must have PA Viewer role minimum", True),
        ]),
        ("Refresh & Collection", [
            ("Data collection schedule", "Nightly for daily indicators; every 4 hours for operational indicators (OOTB)", "Do not change collection frequency in 18-week scope", False),
            ("Historical data backfill", "OOTB PA collects from activation date forward -- no backfill", "Communicate to customer: dashboards will be sparse for first 2-4 weeks", False),
        ]),
    ],
    raci_rows=[
        ("Confirm PA license entitlement", "I", "R/A", "Customer IT Director."),
        ("Activate OOTB dashboards in instance", "R/A", "I", "ECS Consultant."),
        ("Activate data collection jobs", "R/A", "I", "ECS Consultant."),
        ("Name dashboard owners", "I", "R/A", "Customer IT Director."),
        ("Grant PA Viewer roles to owners", "R/A", "Provide user list", "ECS grants roles; Customer names users."),
        ("Communicate 2-4 week data ramp-up to leadership", "I", "R/A", "Customer IT Director sets expectations."),
    ],
    consultant_guide_sections=[
        ("Data ramp-up expectation", "PA indicators collect data from the activation date forward. Dashboards will appear sparse or empty for the first 2-4 weeks. Set this expectation explicitly with the IT Director before activating. A dashboard with 2 weeks of data looks broken -- frame it as 'the meter is running, data is accumulating daily.'"),
        ("Backfill workaround", "If the customer needs historical context immediately: OOTB Reports can show historical data from before PA activation. Build an OOTB report for the most important executive metric (e.g., monthly incident volume for the past 6 months) and pin it alongside the PA dashboard. This bridges the ramp-up period."),
        ("Dashboard vs. report distinction", "PA dashboards show trends and KPIs over time. OOTB Reports show snapshots and lists. Customers often confuse the two. Frame PA as 'the trend story' and OOTB Reports as 'the detail behind it.' Both are needed."),
    ],
    adoption_rows=[
        ("Build us a custom executive scorecard with 20 indicators",
         "3 OOTB dashboards at go-live; custom scorecard in Phase 2.",
         "20 custom indicators require data collection activation, breakdown configuration, and threshold tuning -- each indicator adds days of scope.",
         "Three OOTB dashboards give the IT Director, Service Desk Manager, and Team Lead exactly what they need on day 1. The data starts accumulating immediately. At the 90-day review, we have real data to design a custom scorecard around what actually matters to your leadership -- not what we guessed would matter before go-live.",
         "Phase 2 -- after 90 days of OOTB data establishes baseline."),
    ],
    snmap_sections=[
        ("Performance Analytics Core", [
            ("pa_dashboard", "PA Dashboard record -- OOTB dashboard configurations", "pa_dashboard"),
            ("pa_indicator", "PA Indicator record -- each KPI metric", "pa_indicator"),
            ("pa_collection", "Data collection job -- scheduled to run per indicator", "pa_collection"),
            ("PA Viewer role", "pa_viewer -- grants read access to PA dashboards", "sys_user_role"),
        ]),
    ],
)

wb2 = TabContent(
    workbook_title="02 -- OOTB Indicator Library",
    pack_name=PACK_NAME,
    purpose="Document the OOTB PA indicators activated for go-live across ITSM, with their data sources, collection frequency, and target thresholds.",
    who_fills="ECS Consultant confirms indicators active. Customer Process Owners set threshold targets.",
    sprint_window="Sprint 6 -- indicators active and collecting by Week 11",
    estimated_effort="3-4 hours including indicator activation and threshold configuration",
    related_workbooks=["01 PA Scope", "03 Dashboard Design", "AP-02 ITSM Pack"],
    success_criteria=[
        "All OOTB go-live indicators activated and collecting data.",
        "Threshold targets set for each indicator (green/yellow/red).",
        "Process Owners have confirmed targets are aligned to SLAs.",
        "Indicator collection verified -- data visible in at least one dashboard widget.",
    ],
    process_decisions=[
        ("Should thresholds be set at go-live or after data accumulates?",
         "Set indicative thresholds at go-live based on SLAs. Revise after 30 days of real data.",
         "Empty thresholds mean all indicators show gray -- no signal. SLA-based thresholds give a starting point that can be refined with actual performance data."),
        ("Should indicators be broken down by assignment group?",
         "Yes for Incident Volume and MTTR -- broken down by assignment group is the most actionable view.",
         "Group-level breakdown lets managers see which teams are struggling without building custom indicators."),
    ],
    dependencies=[
        ("ITSM processes generating data", "Required", "ECS", "Sprint 4 close", "PA indicators only collect data if source tables have records."),
        ("SLA definitions confirmed (AP-01 Foundation Data)", "Required", "ECS + Customer", "Sprint 1 close", "SLA targets inform PA indicator thresholds."),
    ],
    config_sections=[
        ("Incident Indicators", [
            ("Incident Volume (daily)", "OOTB -- count of incidents created per day", "Collection: daily. Breakdown: by priority, by category.", False),
            ("Open Incident Backlog", "OOTB -- count of open incidents at time of collection", "Collection: every 4 hours. Threshold: green <100, yellow 100-150, red >150", True),
            ("Mean Time to Resolve (MTTR)", "OOTB -- average hours from creation to resolution", "Collection: daily. Threshold set to SLA target", True),
            ("SLA Compliance %", "OOTB -- % of incidents resolved within SLA", "Collection: daily. Target: green >90%, yellow 80-90%, red <80%", True),
            ("First Call Resolution Rate", "OOTB -- % of incidents resolved without reassignment", "Collection: daily. Target: green >70%, yellow 55-70%, red <55%", True),
            ("Reassignment Count", "OOTB -- average reassignments per incident", "Collection: daily. Target: green <1.5, yellow 1.5-2.5, red >2.5", True),
        ]),
        ("Service Request Indicators", [
            ("Request Volume (daily)", "OOTB -- count of service requests created per day", "Collection: daily.", False),
            ("Request MTTR", "OOTB -- average hours from request to fulfillment", "Collection: daily. Threshold: set to catalog item SLA", True),
            ("Open Request Backlog", "OOTB -- open requests pending fulfillment", "Collection: every 4 hours.", False),
        ]),
        ("Change Indicators (if in scope)", [
            ("Change Volume (weekly)", "OOTB -- count of changes by type (Standard, Normal, Emergency)", "Collection: weekly.", False),
            ("Change Success Rate", "OOTB -- % of changes with no associated incident post-implementation", "Collection: weekly. Target: green >95%", True),
        ]),
    ],
    raci_rows=[
        ("Activate OOTB indicators and data collection jobs", "R/A", "I", "ECS Consultant."),
        ("Set green/yellow/red thresholds", "R (propose)", "A (approve)", "ECS proposes SLA-based thresholds; Customer Process Owner approves."),
        ("Verify data collection running", "R/A", "I", "ECS verifies collection job execution logs."),
        ("Review and adjust thresholds at 30-day review", "R (advise)", "A (decide)", "Customer IT Manager decides threshold adjustments."),
    ],
    consultant_guide_sections=[
        ("Threshold-setting conversation", "Use SLAs as the anchor for initial thresholds. If the SLA for incident resolution is 8 hours, set the MTTR green threshold at 7 hours (buffer). Yellow at 8-10 hours. Red above 10. This directly links the PA indicator to the contractual commitment the customer has already agreed to."),
        ("Sparse data in first 30 days", "Inform Process Owners that indicators need 2-4 weeks of data before trends are meaningful. In the first week, charts will show single data points -- that is expected. Coach them to look at the raw numbers, not the trend line, for the first month."),
        ("Collection job verification", "After activating each indicator, navigate to PA > Data Collector and confirm the collection job shows a successful last run. A collection job that never ran is silent -- it does not error, it just produces no data. Always verify."),
    ],
    adoption_rows=[
        ("We want real-time dashboards",
         "Near-real-time (every 4 hours) for operational indicators; daily for trend indicators.",
         "True real-time PA requires event-driven collection not available in OOTB PA. OOTB Reports can provide snapshot data that is more current.",
         "PA is designed for trend analysis, not live monitoring. For real-time operational monitoring -- who is working what right now -- OOTB Reports with auto-refresh is the correct tool. PA shows you the trend story; Reports show you the current state. Both are in ServiceNow, both are OOTB.",
         "Never -- real-time PA is not an OOTB capability."),
    ],
    snmap_sections=[
        ("Indicators", [
            ("pa_indicator", "Each KPI metric -- source table, collection frequency, breakdown", "pa_indicator"),
            ("pa_target", "Threshold record -- green/yellow/red values per indicator", "pa_target"),
            ("pa_collection", "Collection job -- scheduled data collection per indicator", "pa_collection"),
            ("incident, sc_request", "Source tables for ITSM indicators", "incident, sc_request, change_request"),
        ]),
    ],
)

wb3 = TabContent(
    workbook_title="03 -- Dashboard Design & Layout",
    pack_name=PACK_NAME,
    purpose="Document the widget layout, audience, and refresh settings for each OOTB PA dashboard activated at go-live.",
    who_fills="ECS Consultant configures OOTB layouts. Dashboard owners review and approve during UAT.",
    sprint_window="Sprint 6 -- dashboards configured and approved by Week 12",
    estimated_effort="4-5 hours including widget configuration and owner UAT",
    related_workbooks=["01 PA Scope", "02 Indicator Library"],
    success_criteria=[
        "All three OOTB dashboards configured with correct widgets.",
        "Each dashboard owner has approved the layout.",
        "Dashboards accessible to correct roles (Viewer for owners).",
        "Sharing settings confirmed (individual vs. group access).",
    ],
    process_decisions=[
        ("Should dashboards be shared with specific users or roles?",
         "Share with roles (IT Director role, Service Desk Manager role). Do not share to all users.",
         "Role-based sharing ensures dashboards reach the right audience as the organization grows. User-level sharing requires manual updates when people change roles."),
        ("Should executive dashboard include a traffic light summary?",
         "Yes -- OOTB PA supports a KPI summary widget with green/yellow/red status. Include it as the first widget on the executive dashboard.",
         "Traffic light summary gives the IT Director a 5-second health check without reading all charts. It is the highest-value widget on the executive dashboard."),
        ("Should dashboards be set as homepage for dashboard owners?",
         "Recommend setting the relevant PA dashboard as homepage for each named owner.",
         "Homepage setting ensures the dashboard is the first thing owners see on login -- maximizing the chance they review it daily."),
    ],
    dependencies=[
        ("OOTB indicators active (WB2)", "Required", "ECS", "Sprint 6 Wk 1", "Dashboard widgets require active indicators."),
        ("Dashboard owners named (WB1)", "Required", "Customer", "Sprint 6 Wk 1", "Cannot configure sharing without named owners."),
        ("PA Viewer roles granted", "Required", "ECS", "Sprint 6 Wk 1", "Owners need PA Viewer role to access dashboards."),
    ],
    config_sections=[
        ("ITSM Executive Overview -- Widget Layout", [
            ("Widget 1: SLA Compliance Traffic Light", "KPI summary -- green/yellow/red for SLA compliance", "Position: top left, full width. OOTB pa_kpi_summary widget", False),
            ("Widget 2: Incident Volume Trend (30 days)", "Line chart -- daily incident volume", "Position: left column. OOTB pa_chart widget", False),
            ("Widget 3: Open Incidents by Priority", "Bar chart -- P1/P2/P3/P4 open count", "Position: right column. OOTB pa_chart widget", False),
            ("Widget 4: MTTR Trend (30 days)", "Line chart -- average resolution time daily", "Position: bottom left. OOTB pa_chart widget", False),
            ("Widget 5: SLA Compliance % (30 days)", "Line chart -- daily SLA compliance %", "Position: bottom right. OOTB pa_chart widget", False),
        ]),
        ("Incident Management Dashboard -- Widget Layout", [
            ("Widget 1: Open Backlog Scorecard", "Single number -- current open incidents", "OOTB pa_scorecard widget", False),
            ("Widget 2: Incidents by Assignment Group", "Bar chart -- volume and backlog by group", "OOTB pa_breakdown widget", False),
            ("Widget 3: First Call Resolution Rate", "Gauge -- FCR % vs. 70% target", "OOTB pa_gauge widget", False),
            ("Widget 4: Reassignment Rate Trend", "Line chart -- average reassignments per incident", "OOTB pa_chart widget", False),
            ("Widget 5: MTTR by Category", "Bar chart -- resolution time by incident category", "OOTB pa_breakdown widget", False),
        ]),
        ("Service Desk Performance -- Widget Layout", [
            ("Widget 1: Agent Workload Distribution", "Bar chart -- open incidents per agent", "OOTB pa_breakdown widget", False),
            ("Widget 2: Incidents Resolved Today", "Single number scorecard", "OOTB pa_scorecard widget", False),
            ("Widget 3: FCR Rate by Agent", "Table -- FCR % per agent for current week", "OOTB pa_breakdown widget", False),
            ("Widget 4: Volume vs. Capacity Trend", "Line chart -- daily volume vs. team average handle capacity", "OOTB pa_chart widget", False),
        ]),
        ("Access & Sharing", [
            ("ITSM Executive Overview -- shared to", "IT Director role (itil_admin or custom IT Director role)", "Customer to confirm role name", True),
            ("Incident Management -- shared to", "IT Manager role", "Customer to confirm role name", True),
            ("Service Desk Performance -- shared to", "Service Desk Manager role", "Customer to confirm role name", True),
            ("Set as homepage", "Recommend for all three named owners", "Customer owners confirm preference", True),
        ]),
    ],
    raci_rows=[
        ("Configure OOTB widget layout for each dashboard", "R/A", "I", "ECS Consultant."),
        ("Configure sharing and role assignments", "R/A", "Provide role names", "ECS configures; Customer confirms roles."),
        ("Dashboard owner UAT", "R (facilitate)", "A (approve)", "ECS facilitates; each owner approves their dashboard."),
        ("Set homepage for dashboard owners", "R/A", "Confirm preference", "ECS sets with owner consent."),
    ],
    consultant_guide_sections=[
        ("Layout simplicity rule", "Each OOTB dashboard should have 4-6 widgets maximum. More widgets = cognitive overload = dashboard is ignored. The rule is: every widget must answer a question the owner asks at least weekly. If they cannot name the question, remove the widget."),
        ("UAT with owners", "Sit with each dashboard owner for 30 minutes. Walk through their dashboard and ask: 'What question does each widget answer?' If they struggle, simplify. Dashboards that owners understand are dashboards they use. Dashboards that impress but confuse are dashboards that get abandoned."),
        ("Traffic light widget", "The traffic light (KPI summary) widget is the most impactful single widget on the executive dashboard. It converts a complex dashboard into a 3-second health check. Always lead with it. The IT Director will see it on homepage load and know immediately if ITSM is healthy."),
    ],
    adoption_rows=[
        ("Add 15 widgets to the executive dashboard to show everything",
         "4-6 widgets maximum; curate relentlessly.",
         "15 widgets on a single dashboard produces scroll fatigue and information overload. IT Directors stop reviewing overpacked dashboards within 2 weeks.",
         "We curate these dashboards based on one principle: what does the IT Director look at first thing Monday morning? That is the dashboard. Everything else is available in OOTB Reports for drill-down. Five focused widgets that answer five important questions will be used every day. Fifteen widgets that try to show everything will be ignored by week 3.",
         "Never -- widget discipline is a governance principle, not a constraint."),
    ],
    snmap_sections=[
        ("Dashboard Widgets", [
            ("pa_dashboard", "Dashboard container record", "pa_dashboard"),
            ("pa_widget", "Individual widget on a dashboard -- chart, scorecard, KPI summary", "pa_widget"),
            ("pa_chart_widget", "Chart widget -- line, bar, gauge types", "pa_chart_widget"),
            ("pa_scorecard_widget", "Single-number scorecard widget", "pa_scorecard_widget"),
        ]),
    ],
)

wb4 = TabContent(
    workbook_title="04 -- Scorecard Configuration",
    pack_name=PACK_NAME,
    purpose="Configure the OOTB PA Scorecard for IT leadership to provide a single-page view of ITSM health against KPI targets.",
    who_fills="ECS Consultant configures OOTB scorecard. Customer IT Director reviews and approves.",
    sprint_window="Sprint 6 -- scorecard configured and published by Week 12",
    estimated_effort="3 hours including scorecard configuration and IT Director review",
    related_workbooks=["01 PA Scope", "02 Indicator Library", "03 Dashboard Design"],
    success_criteria=[
        "OOTB PA Scorecard published and accessible to IT Director.",
        "All go-live indicators included in scorecard.",
        "Green/yellow/red thresholds set and approved.",
        "Scorecard scheduled for monthly review in recurring calendar invite.",
    ],
    process_decisions=[
        ("Should the scorecard be a separate artifact or embedded in the executive dashboard?",
         "Separate OOTB PA Scorecard document, linked from the executive dashboard.",
         "The OOTB Scorecard is a formatted, printable KPI summary. It serves a different purpose than a live dashboard -- it is for leadership reviews, board presentations, and monthly reporting."),
        ("How often should the scorecard be formally reviewed?",
         "Monthly -- scheduled recurring review with IT Director and ECS PM during engagement; Customer-owned monthly review post-engagement.",
         "Monthly cadence matches typical IT leadership review cycles."),
        ("Should the scorecard include trend direction indicators?",
         "Yes -- OOTB PA Scorecard shows trend arrow (up/down/flat) alongside each KPI value.",
         "Trend direction tells the story faster than a raw number. 'SLA compliance 88% (down from 92%)' is more meaningful than just '88%.'"),
    ],
    dependencies=[
        ("OOTB indicators active with thresholds set (WB2)", "Required", "ECS", "Sprint 6 Wk 1", "Scorecard pulls from active indicators."),
        ("At least 2 weeks of collected data", "Required", "ECS", "Sprint 6 Wk 2", "Scorecard trends are not meaningful without at least 2 data points."),
    ],
    config_sections=[
        ("Scorecard Structure", [
            ("Scorecard name", "ITSM Monthly Health Scorecard", "", False),
            ("KPI 1: SLA Compliance %", "Target: 90%. Trend: vs. prior month.", "Green >90%, Yellow 80-90%, Red <80%", True),
            ("KPI 2: Mean Time to Resolve", "Target: [Customer SLA hours]. Trend: vs. prior month.", "Green at target, Yellow 10% over, Red 20% over", True),
            ("KPI 3: First Call Resolution Rate", "Target: 70%. Trend: vs. prior month.", "Green >70%, Yellow 55-70%, Red <55%", True),
            ("KPI 4: Incident Volume (monthly)", "No target -- trend only. Shows workload change.", "Used for capacity planning context", False),
            ("KPI 5: Open Backlog at Month End", "Target: <100. Trend: vs. prior month end.", "Green <100, Yellow 100-150, Red >150", True),
        ]),
        ("Scorecard Governance", [
            ("Scorecard owner", "[Customer: IT Director name]", "Owner reviews and distributes monthly", True),
            ("Monthly review cadence", "Last Friday of each month -- recurring calendar invite", "ECS PM schedules for engagement period; Customer PM owns post-engagement", False),
            ("Distribution", "IT Director + Customer PM + ECS PM (during engagement)", "Customer to confirm distribution list post-engagement", True),
        ]),
    ],
    raci_rows=[
        ("Configure OOTB PA Scorecard", "R/A", "I", "ECS Consultant."),
        ("Set thresholds on scorecard KPIs", "R (propose)", "A (approve)", "ECS proposes; IT Director approves."),
        ("Schedule monthly review calendar invite", "R", "A", "ECS PM schedules during engagement; Customer PM takes over."),
        ("Distribute monthly scorecard", "N/A (during engagement: ECS)", "R/A (post-engagement)", "Customer IT Director distributes post-handover."),
    ],
    consultant_guide_sections=[
        ("Scorecard timing", "Do not publish the scorecard until at least 2 weeks of data have collected. A scorecard with 3 data points is misleading. Present the scorecard at the 30-day review meeting -- by then there is enough data to show meaningful trends."),
        ("Trend arrow language", "Coach the IT Director on trend arrows: a down arrow on MTTR is good (resolving faster). A down arrow on SLA compliance is bad. The direction of good is context-dependent. Include a legend note on the scorecard: 'For MTTR: lower is better. For SLA Compliance: higher is better.'"),
        ("Executive presentation use", "The OOTB Scorecard is PDF-exportable. Confirm the IT Director knows how to export it. Many customers use this as a one-page insert in their monthly IT leadership report. That visibility is excellent for demonstrating the value of the ServiceNow deployment."),
    ],
    adoption_rows=[
        ("We want a scorecard with 25 KPIs for the CIO",
         "5 KPIs at go-live; expand to 10 at 90-day review based on data.",
         "25 KPIs without baseline data are 25 numbers without context. Five focused KPIs that the IT Director understands and can act on are more valuable than 25 that require explanation.",
         "We start with five KPIs that connect directly to your SLAs and operations. At the 90-day review, we have real performance data and we know which additional metrics would be meaningful. Building a 25-KPI scorecard before you have baseline data means you are measuring things without knowing what good looks like.",
         "Phase 2 -- expand scorecard after 90-day baseline established."),
    ],
    snmap_sections=[
        ("Scorecard", [
            ("pa_scorecard", "PA Scorecard record -- collection of indicators formatted for review", "pa_scorecard"),
            ("pa_target", "Threshold target per indicator -- drives green/yellow/red color", "pa_target"),
            ("pa_score", "Individual score record per collection period", "pa_score"),
        ]),
    ],
)

wb5 = TabContent(
    workbook_title="05 -- PA Governance & Review Cadence",
    pack_name=PACK_NAME,
    purpose="Establish the ongoing governance model, review cadence, and continuous improvement process for Performance Analytics post-go-live.",
    who_fills="ECS PM and Customer PM jointly complete. Dashboard owners commit to review cadence.",
    sprint_window="Sprint 6 -- governance model finalized before handover at Week 12",
    estimated_effort="2 hours with Customer PM and dashboard owners",
    related_workbooks=["01 PA Scope", "03 Dashboard Design", "04 Scorecard", "AP-20 Reporting & Stabilization"],
    success_criteria=[
        "Dashboard owners committed to review cadence.",
        "Monthly scorecard review scheduled (recurring).",
        "Dashboard modification governance agreed (who can change what).",
        "Phase 2 PA roadmap documented.",
        "PA Admin trained on indicator activation and threshold management.",
    ],
    process_decisions=[
        ("Who can modify PA dashboards and indicators post-go-live?",
         "PA Admin role only -- Customer named PA Admin controls all changes.",
         "Open dashboard modification creates widget proliferation and threshold drift. One named PA Admin is the gatekeeper."),
        ("How should new dashboard requests be handled?",
         "New requests go to Customer PA Admin. PA Admin evaluates against OOTB indicator availability. Custom indicators go through Change Management (RFC).",
         "Treating new dashboard requests as mini-change items prevents uncontrolled PA sprawl."),
        ("When should thresholds be revised?",
         "At each monthly scorecard review. Thresholds should be revised quarterly based on trend data, not reactively after a single bad month.",
         "Reactive threshold changes (lowering targets after a bad month) destroy the governance integrity of the scorecard. Quarterly revision with data is the right cadence."),
    ],
    dependencies=[
        ("Named PA Admin with pa_admin role", "Required", "Customer", "Sprint 6 close", "PA governance requires a named admin."),
        ("Dashboard owners trained on PA navigation", "Required", "ECS", "Sprint 6", "Owners must know how to view, export, and interpret their dashboards."),
    ],
    config_sections=[
        ("Governance Model", [
            ("PA Admin role", "Named Customer PA Admin -- controls indicator activation, threshold changes, dashboard sharing", "Customer to name PA Admin before Sprint 6 close", True),
            ("Dashboard modification process", "PA Admin reviews request, evaluates OOTB indicator availability, implements change", "New requests via email to PA Admin; tracked in PA Admin log", False),
            ("Custom indicator RFC requirement", "Any custom indicator (non-OOTB) requires IT Change Request and PA Admin approval", "Prevents uncontrolled custom indicator proliferation", False),
            ("Threshold revision cadence", "Quarterly -- at each quarter-end scorecard review", "Do not revise thresholds reactively after single bad period", False),
        ]),
        ("Review Cadence", [
            ("Weekly (Service Desk Team Lead)", "Review Service Desk Performance dashboard every Monday", "Team Lead owns -- no ECS involvement post-handover", False),
            ("Monthly (IT Manager)", "Review Incident Management dashboard on last Friday of month", "IT Manager owns -- part of regular management cycle", False),
            ("Monthly (IT Director)", "Review ITSM Executive Overview and Scorecard on last Friday of month", "IT Director owns -- ECS PM attends during engagement only", False),
            ("Quarterly threshold review", "IT Director + PA Admin -- review and revise thresholds based on trend data", "Scheduled recurring invite in calendar", False),
        ]),
        ("Phase 2 PA Roadmap", [
            ("Custom indicator library", "Build indicators for request fulfillment SLA, change success, and problem MTTR", "Scope for first post-stabilization sprint", False),
            ("Department-level dashboards", "Individual dashboards per business unit for HR, Finance, etc.", "Requires HR and Finance ITSM usage data to be meaningful", False),
            ("AI-assisted forecasting", "Now Assist integration with PA for predictive capacity forecasting", "Requires 6+ months of PA trend data as input", False),
        ]),
    ],
    raci_rows=[
        ("Name and configure PA Admin", "I", "R/A", "Customer IT Director names; ECS grants role."),
        ("Train PA Admin on indicator and threshold management", "R/A", "Attend", "ECS delivers 1-hour admin training in Sprint 6."),
        ("Train dashboard owners on navigation and export", "R/A", "Attend", "ECS delivers 30-min owner briefing per dashboard."),
        ("Schedule recurring review calendar invites", "R (during engagement)", "A (post-engagement)", "ECS schedules during engagement; Customer PM takes over."),
        ("Phase 2 PA scope documentation", "R/A", "Review", "ECS documents at 90-day review."),
    ],
    consultant_guide_sections=[
        ("PA Admin training scope", "The 1-hour PA Admin training should cover: (1) how to activate a new OOTB indicator, (2) how to set and change thresholds, (3) how to share a dashboard with a new user or role, (4) how to export the scorecard as PDF. These four skills cover 90% of post-go-live PA Admin tasks."),
        ("Governance enforcement", "The most common PA failure mode is uncontrolled dashboard proliferation -- every manager wants their own custom dashboard. Enforce the governance model from day one: new dashboards go through the PA Admin. The OOTB indicator library is large -- most needs can be met without custom indicators."),
        ("Phase 2 sequencing", "Phase 2 PA work should not begin until 6 months of OOTB data has accumulated. The first 90 days produce noise. Months 3-6 produce signal. Custom indicators and department dashboards built on 6 months of data will be far more accurate and useful than ones built on 30 days."),
    ],
    adoption_rows=[
        ("Every manager wants their own dashboard",
         "Named dashboard owners only at go-live; department dashboards in Phase 2.",
         "One dashboard per manager without governance creates 20 dashboards measuring slightly different things with different thresholds -- none of which tell the same story to leadership.",
         "We have three dashboards that cover the three key audiences. Every manager's questions can be answered from these dashboards or from OOTB Reports. If there is a question no existing dashboard answers, the PA Admin evaluates whether a new widget or a new OOTB Report is the right answer. Department dashboards are the Phase 2 roadmap -- grounded in real usage data.",
         "Phase 2 -- department dashboards after 6 months of OOTB baseline."),
    ],
    snmap_sections=[
        ("PA Governance", [
            ("pa_admin role", "Grants full PA admin access -- indicator activation, threshold management, sharing", "sys_user_role"),
            ("pa_viewer role", "Grants read-only access to PA dashboards -- for dashboard owners", "sys_user_role"),
            ("change_request", "RFC process for custom indicator requests -- customer governance", "change_request"),
        ]),
    ],
)

def build_readme():
    meta = DocMeta(
        eyebrow="ACCELERATOR PACK",
        title="Performance Analytics\nAccelerator Pack",
        subtitle="OOTB PA -- Dashboards, Indicators, Scorecard, and Governance for ITSM",
        doc_id="AP-19",
        version="1.0",
        status="Released",
        audience="ECS Consultants (Internal) + Customer IT Director / PA Admin (selected tabs)",
        running_header_label="Performance Analytics Accelerator Pack · ECS Federal",
        confidentiality="Internal Use Only · Confidential",
    )
    doc = EcsDocument(meta=meta)
    doc.add_cover_page()
    doc.h1("Pack Overview")
    doc.para(
        "AP-19 guides the ECS team through activating and configuring OOTB Performance Analytics "
        "during Month 3 (Sprint 6) of the 18-week engagement. The pack covers dashboard inventory "
        "and scope decisions, OOTB indicator library, dashboard layout design, scorecard "
        "configuration, and ongoing governance. All work is OOTB -- no custom indicators, "
        "no scripted data collectors, and no external BI tool integrations in the 18-week scope. "
        "Custom indicators and department dashboards are documented as Phase 2 items."
    )
    doc.h1("Workbook Inventory")
    doc.table(
        headers=["#", "Workbook", "Owner", "Sprint"],
        rows=[
            ("WB1", "PA Scope & Dashboard Inventory", "ECS + Customer IT Director", "Sprint 6"),
            ("WB2", "OOTB Indicator Library", "ECS Consultant", "Sprint 6"),
            ("WB3", "Dashboard Design & Layout", "ECS Consultant", "Sprint 6"),
            ("WB4", "Scorecard Configuration", "ECS + Customer IT Director", "Sprint 6"),
            ("WB5", "PA Governance & Review Cadence", "ECS PM + Customer PM", "Sprint 6"),
        ],
    )
    doc.h1("Key OOTB Decisions")
    doc.para(
        "Dashboards at go-live: ITSM Executive Overview, Incident Management, Service Desk Performance. "
        "Indicators: OOTB only -- no custom indicators in 18-week scope. "
        "Data ramp-up: 2-4 weeks before dashboards show meaningful trends -- communicate to leadership upfront. "
        "Thresholds: SLA-based at go-live; revised quarterly with trend data. "
        "Governance: Named PA Admin controls all changes. Custom indicators require RFC. "
        "Phase 2: Custom indicators, department dashboards, AI-assisted forecasting -- after 6-month baseline."
    )
    out = os.path.join(PACK_DIR, "00_README_Performance_Analytics_Pack.docx")
    doc.save(out)
    print(f"README saved: {out}")

if __name__ == "__main__":
    print("Building Performance Analytics Accelerator Pack...")
    workbooks = [
        ("01_pa_scope_dashboard_inventory.xlsx", wb1),
        ("02_ootb_indicator_library.xlsx", wb2),
        ("03_dashboard_design.xlsx", wb3),
        ("04_scorecard_configuration.xlsx", wb4),
        ("05_pa_governance.xlsx", wb5),
    ]
    for filename, content in workbooks:
        build_workbook(content, os.path.join(PACK_DIR, filename))
        print(f"  check {filename}")
    build_readme()
    print("Performance Analytics Accelerator Pack complete.")
