"""
build_CLT-DT-15_event_management.py
Generates Event_Management_Decision_Guide_CLIENT.docx

Uses dtg_builder.py (shared renderer) — same pattern as CLT-DT-01 through CLT-DT-14.
Client-facing, partnership tone, Everforth ECS branding.
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from dtg_builder import build_dtg

DATA = {
    "doc_id":     "CLT-DT-15",
    "filename":   "Event_Management_Decision_Guide_CLIENT.docx",
    "short_name": "Event Management",
    "title":      "Event Management\nDecision Topic Guide",
    "subtitle":   "Connecting your monitoring tools to your ITSM workflow",
    "audience":   "IT Operations Lead, Service Desk Manager, Infrastructure & Security Teams",
    "companion_to": (
        "Workshop Pre-Read: Event Management (WP-17)  ·  "
        "AP-08 Event Management Foundations Pack  ·  "
        "Incident Management Decision Guide (CLT-DT-01)"
    ),

    "how_to_use_paras": [
        "This guide prepares you for the Event Management workshop. It frames the four decisions "
        "your team will make, explains the trade-offs at each, and shares what we have observed "
        "across comparable engagements. Read it once before we meet — 20 minutes is enough.",
        "The four decisions in Section 3 are the ones we will spend the most time on. If you have "
        "strong views on any of them before the workshop, write them down. If you have no view yet, "
        "that is equally fine — the workshop is designed to develop them with you.",
    ],

    "why_matters": [
        {
            "h2": "Your monitoring tools already know when something is wrong",
            "body": (
                "Most IT organizations have made significant investments in monitoring. They know "
                "within seconds when a server's CPU spikes, a network device stops responding, or "
                "an application's error rate climbs. The problem is not detection — it is what "
                "happens next. A monitoring alert in a tool that no one is actively watching at "
                "2am on a Sunday is not an operational capability. It is a log entry. Event "
                "Management turns that detection into a response workflow — automatically, "
                "consistently, and at any hour."
            ),
        },
        {
            "h2": "The gap between monitoring and ITSM costs time your SLAs do not have",
            "body": (
                "The time between 'the monitoring tool fires an alert' and 'an incident exists in "
                "ServiceNow with the right team assigned' is where MTTR lives. In a manual world, "
                "that gap is often 15–45 minutes: someone has to see the alert, decide it is real, "
                "figure out who owns it, and create the ticket. In an Event Management world, that "
                "gap is under 60 seconds. The SLA clock starts on the alert, not on the moment "
                "someone noticed it. For P1 incidents with 15-minute response SLAs, that difference "
                "is the difference between compliance and breach."
            ),
        },
        {
            "h2": "Alert fatigue is a design problem, not a volume problem",
            "body": (
                "The most common objection to Event Management is: 'our monitoring generates too "
                "much noise — it will just flood the incident queue.' That concern is legitimate, "
                "but it describes the problem that Event Management is designed to solve. The "
                "noise suppression, deduplication, and correlation capabilities in ServiceNow exist "
                "specifically to ensure that operators see only what requires action — not every "
                "heartbeat from every server. The design work is in defining what is noise and what "
                "is signal. That is exactly what the workshop builds."
            ),
        },
        {
            "h2": "Auto-resolution is where the ROI becomes measurable",
            "body": (
                "When a monitoring tool signals recovery, ServiceNow can resolve the linked incident "
                "automatically — no agent needed. Organizations that implement auto-resolution "
                "typically see 30–50% of Event Management incidents resolved without any human "
                "action. That is a measurable reduction in close-out workload, a measurable "
                "improvement in MTTR, and a metric your leadership will notice. It is also an "
                "OOTB capability that requires configuration, not development."
            ),
        },
    ],

    "signal_subject": "Event Management",
    "signals": [
        {
            "h2": "Your operations team watches multiple monitoring dashboards simultaneously",
            "body": (
                "Each monitoring tool has its own dashboard, its own alert format, and its own "
                "severity vocabulary. Operators flip between them looking for the one that is "
                "firing. The institutional knowledge of 'which tool watches which part of the "
                "environment' lives in people, not in a system. When those people are not available, "
                "coverage gaps appear."
            ),
        },
        {
            "h2": "Incidents are created manually from monitoring alerts",
            "body": (
                "An operator sees an alert, decides it is worth a ticket, looks up the right "
                "assignment group, creates the incident, and adds the monitoring context by hand. "
                "This process works — but it is slow, inconsistent across operators, and entirely "
                "dependent on someone being awake and attentive at the moment the alert fires. "
                "The fastest operators in the world cannot match an automated system for "
                "speed and consistency."
            ),
        },
        {
            "h2": "High-severity incidents are sometimes discovered by users before IT",
            "body": (
                "When a monitoring alert goes unnoticed and a service degrades, users feel it "
                "first. The incident is then created reactively — from a user call or a spike in "
                "portal submissions — rather than proactively from the monitoring signal that fired "
                "minutes or hours earlier. This is the most visible sign that the gap between "
                "monitoring and ITSM is costing SLA compliance."
            ),
        },
        {
            "h2": "Incident resolution requires a human to close the ticket even when the system has already recovered",
            "body": (
                "A network device recovers automatically. The monitoring tool shows green. "
                "The incident sits in 'In Progress' until an agent notices it, confirms the device "
                "is up, and manually resolves the ticket. This close-out work is time-consuming "
                "and low-value. It is also the scenario where auto-resolution delivers its "
                "highest and most immediate return."
            ),
        },
    ],

    "decisions": [
        {
            "label": "Which monitoring tools connect at go-live?",
            "body": (
                "You have more monitoring tools than you need to connect at go-live. The question "
                "is which two or three cover the infrastructure where a failure would breach an "
                "SLA or impact a business service. Those are the right starting tools. Others "
                "can be added in subsequent phases once the foundation is stable and the event "
                "rules are tuned. Connecting too many tools at once extends the go-live timeline "
                "and creates more noise to filter before the system earns operator trust."
            ),
            "questions": [
                "Which monitoring tools generate alerts that your operations team currently acts on? Which ones generate alerts they routinely ignore?",
                "Which monitoring tools cover your most SLA-critical infrastructure — the systems where a failure would breach a commitment to your organization's leadership?",
                "Are any of your current monitoring tools being decommissioned or replaced within the next 12 months? Those should be excluded from go-live scope.",
                "Do any tools require special network access (e.g., isolated segments, air-gapped environments) that would require additional infrastructure (MID Server nodes) to connect?",
            ],
            "landing": (
                "Most organizations start with 2–3 monitoring tools at go-live — typically their "
                "primary infrastructure monitoring tool, their application performance tool, and "
                "one additional source. That scope is manageable, delivers clear value, and "
                "provides the confidence to expand in Phase 2."
            ),
        },
        {
            "label": "What thresholds trigger automatic incident creation?",
            "body": (
                "Automatic incident promotion is the feature that delivers the MTTR improvement. "
                "The threshold design is what prevents it from creating noise. The decision has "
                "three dimensions: severity (which alert severity levels auto-promote), duration "
                "(does a threshold need to be breached for a minimum time before promoting), and "
                "CI tier (do non-production CIs auto-promote, or are they reviewed manually?). "
                "Getting these thresholds right is more important than getting them perfect on "
                "day one — they will be tuned based on 30 days of production data. The workshop "
                "establishes the starting position."
            ),
            "questions": [
                "What is your current definition of a P1 incident — what service state or failure condition triggers your highest-priority response?",
                "Does your team currently treat non-production infrastructure alerts differently from production alerts? Should that distinction be reflected in the promotion rules?",
                "What is the acceptable rate of 'false positive' incidents — tickets created by Event Management that an agent closes without action because the alert was transient?",
                "How long should a threshold breach persist before an incident is created? Immediate promotion for critical alerts is common; 10–15 minute delays for medium-severity alerts give transient issues time to self-resolve.",
            ],
            "landing": (
                "A common starting position: Critical and Major alerts auto-promote immediately; "
                "Medium alerts auto-promote after 15 minutes without acknowledgement; "
                "Informational and low alerts never auto-promote. Non-production CIs route to a "
                "manual triage queue, not to automatic promotion. These thresholds are revisited "
                "at the 30-day mark."
            ),
        },
        {
            "label": "How will events be matched to your CI inventory?",
            "body": (
                "ServiceNow matches each incoming event to a Configuration Item using the "
                "identifier in the event — typically a hostname, IP address, or FQDN. That match "
                "is what enables automatic routing (the incident goes to the team that owns the "
                "CI), service impact analysis (which services are affected by this CI's failure), "
                "and CMDB-linked reporting. The quality of the match depends on the completeness "
                "of your CMDB. Events for CIs that are not in the CMDB are not lost — they are "
                "routed to a manual triage queue — but they do not receive the full benefit of "
                "CI-linked automation. The workshop will assess your CMDB coverage and define "
                "the plan for closing the gaps."
            ),
            "questions": [
                "What percentage of your monitored infrastructure has a CI record in ServiceNow today, with a populated hostname and IP address?",
                "Does your monitoring tool use the same naming convention as your CMDB? Or do monitoring tool hostnames sometimes differ from CMDB CI names?",
                "Do you have cloud or containerized infrastructure that changes frequently? That infrastructure requires an automated CI population mechanism (Discovery or a cloud connector) to stay correlated.",
                "Who owns the CMDB data quality improvement work? Event Management CI correlation is a strong incentive for CMDB investment — the connection is worth making explicitly to your CMDB owner.",
            ],
            "landing": (
                "A target CI correlation rate of 85% or higher at go-live is achievable for most "
                "organizations with a moderately complete CMDB. Events that do not correlate are "
                "routed to an Event Triage group for manual review — that queue also serves as "
                "a real-time CMDB gap report, making it a useful tool for the CMDB improvement "
                "effort that typically runs in parallel."
            ),
        },
        {
            "label": "Who manages the operator workspace, and how does escalation work?",
            "body": (
                "The Event Management Operator Workspace replaces the multi-dashboard monitoring "
                "wall with a single queue of alerts across all connected tools. Someone needs to "
                "own that queue. The workshop will identify the designated operators, define the "
                "shift or on-call rotation, establish the acknowledgement SLA (how quickly a "
                "Critical alert must be acknowledged before an escalation fires), and confirm "
                "the on-call notification mechanism for after-hours events. An unmanned operator "
                "workspace defeats the purpose of automated promotion just as surely as not "
                "configuring the promotion rules at all."
            ),
            "questions": [
                "Who on your operations team would be the primary operator of the Event Management workspace on a day-to-day basis?",
                "Do you have an existing on-call rotation for critical infrastructure incidents? Is it managed in a tool (PagerDuty, OpsGenie) or informally?",
                "What is an acceptable response time for a Critical alert during business hours? Outside business hours?",
                "If a Critical alert is created at 2am and no one acknowledges it within 10 minutes, what should happen — who gets notified, and through what channel?",
            ],
            "landing": (
                "Named operators with a defined acknowledgement SLA and a tested escalation path "
                "are the minimum viable operating model. Organizations with existing on-call tools "
                "integrate them with Event Management so that the on-call rotation handles "
                "after-hours critical alerts through the tool they already use. The workspace "
                "then becomes the day-shift operational view."
            ),
        },
    ],

    "good_rows": [
        ["Monitoring tools connect via certified ServiceNow connectors", "Custom REST parsers built for tools that have certified connectors"],
        ["Promotion thresholds reviewed and tuned at 30 and 60 days post-launch", "Promotion thresholds set once in Sprint 1 and never revisited"],
        ["CI correlation rate ≥ 85% at go-live; tracked monthly thereafter", "CI correlation not measured; unknown percentage of events unmatched"],
        ["Named operators with defined acknowledgement SLAs", "Operator workspace monitored informally — 'whoever is around'"],
        ["Auto-resolution active for P2–P4 incidents; measured monthly", "Auto-resolution disabled because 'we want humans to confirm everything'"],
        ["Event Triage queue actively reviewed as a CMDB gap report", "Uncorrelated events ignored or discarded"],
        ["Noise suppression rules reviewed monthly in first quarter", "Noise suppression rules not configured; all events promoted"],
        ["MID Server sized for peak event volume + 20% headroom", "MID Server sized for average volume; drops events during storms"],
    ],

    "patterns": [
        {
            "label": "The monitoring-wall organization",
            "body": (
                "A mid-size federal IT organization with four monitoring tools — infrastructure, "
                "network, application, and cloud — ran a six-screen monitoring wall staffed by "
                "rotating operators. Incidents were created manually when an operator identified "
                "something worth escalating. Mean time between alert and incident creation was "
                "22 minutes. After Event Management, the four tools connected, promotion rules "
                "set for Critical and Major, and a 15-minute triage window for Medium: mean time "
                "to incident dropped to under 90 seconds. The monitoring wall was repurposed for "
                "long-horizon capacity planning rather than real-time triage."
            ),
        },
        {
            "label": "The noise concern that shaped the design",
            "body": (
                "An organization with a high-volume infrastructure monitoring tool hesitated to "
                "connect Event Management because their tool generated 8,000 events per day. "
                "A full connection at that volume would have flooded the incident queue. The "
                "solution: event rules filtered to promote only events tied to CIs in production "
                "service tiers, with a severity threshold of Major or higher. The effective "
                "volume that reached the incident queue was 12–15 incidents per day — manageable, "
                "high-signal, and trusted by the operations team within two weeks."
            ),
        },
        {
            "label": "The CMDB investment that Event Management unlocked",
            "body": (
                "One organization's Event Management go-live produced a correlation rate of 71% — "
                "below the 85% target. Rather than treating this as a failure, the team used the "
                "Event Triage queue as a real-time CMDB gap report. Over 60 days, the operations "
                "team identified 340 production CIs that existed in monitoring but not in the "
                "CMDB, prioritized the top 200 by alert frequency, and loaded them into the CMDB. "
                "The correlation rate reached 91% without a formal CMDB remediation project — "
                "the incentive of improving auto-assignment was sufficient motivation."
            ),
        },
    ],

    "workshop_para": (
        "The Event Management workshop runs approximately 3 hours and covers the four decisions "
        "above in sequence. We begin with the monitoring tool scope decision — it sets the "
        "boundaries for everything else. We then work through promotion thresholds and CI "
        "correlation strategy together, drawing on the CMDB coverage data your team brings. "
        "We close with the operator model, which is as much an organizational conversation as "
        "a technical one. By the end, we will have a configuration baseline that your ECS team "
        "can begin building immediately in Sprint 0."
    ),

    "need_bullets": [
        "List of active monitoring tools with vendor name and approximate daily alert volume per tool",
        "CMDB coverage estimate: what percentage of your monitored production infrastructure has a CI record in ServiceNow with a hostname or IP address?",
        "Current on-call process: how are after-hours critical incidents currently escalated? (Informal description is fine.)",
        "Network topology overview: can your monitoring tools reach the internet (ServiceNow directly), or are they isolated behind a firewall (requiring a MID Server)?",
        "Contact for your monitoring tool administrators — we will need their involvement during connector configuration",
        "Incident priority matrix from your Incident Management configuration: what priority maps to what SLA target?",
    ],

    "questions": [
        "Which monitoring alert in the past 90 days caused the longest delay between detection and the incident being created? What caused the delay?",
        "Is there a monitoring tool your operations team trusts most — whose alerts they almost always act on? That tool is usually the right first connection.",
        "Are there categories of monitoring alerts your team currently ignores because they are always noise? Understanding those helps us build the suppression rules.",
        "What would a successful Event Management go-live look like to your Service Desk Manager? What would they be able to do or see that they cannot today?",
        "Does your organization have a formal on-call policy, or does on-call work informally? If informal, is the workshop the right moment to formalize it?",
    ],

    "xrefs": [
        ["Workshop Pre-Read: Event Management (WP-17)", "Foundational orientation — read before this guide", "02_Client/05_Workshop_Pre-Reads/"],
        ["Incident Management Decision Guide (CLT-DT-01)", "Incident promotion thresholds connect directly to the Incident priority model", "02_Client/04_Decision_Topic_Guides/"],
        ["AP-08 Event Management Foundations Pack", "Configuration workbooks for event sources, rules, CI correlation, and operator workspace", "03_Shared/01_Accelerator_Packs/Event_Management_Foundations_Accelerator_Pack/"],
        ["CMDB Class Selection Decision Guide (CLT-DT-10)", "CI correlation quality depends on CMDB completeness — review alongside this guide", "02_Client/04_Decision_Topic_Guides/"],
        ["Integration Prioritization Decision Guide (CLT-DT-12)", "MID Server and connector architecture connects to the broader integration strategy", "02_Client/04_Decision_Topic_Guides/"],
    ],
}

if __name__ == "__main__":
    print("Building CLT-DT-15 Event Management Decision Topic Guide ...")
    build_dtg(DATA)
    print("Done.")
