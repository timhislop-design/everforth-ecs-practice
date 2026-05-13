"""
build_CLT-WP-17_event_management.py
Generates WP_17_Event_Management_CLIENT.docx

Follows the exact same structure as build_CLT-WP-all.py.
Client-facing, partnership tone, Everforth ECS branding.
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

FOOTER = "ECS Federal · ServiceNow Practice  ·  Confidential"
CONFIDENTIALITY = "Confidential — prepared for the recipient and their organization"


def build_pre_read(discipline):
    d = discipline
    filename = os.path.join(HERE, d["filename"])

    doc = EcsDocument(meta=DocMeta(
        eyebrow=f"WORKSHOP PRE-READ  ·  {d['short_name'].upper()}",
        title=d["title"],
        subtitle=d["subtitle"],
        audience=d["audience"],
        companion_to=d["companion_to"],
        doc_id=d["doc_id"],
        version="1.0",
        status="Released",
        confidentiality=CONFIDENTIALITY,
        running_header_label=f"Workshop Pre-Read  ·  {d['short_name']}",
        footer_left=FOOTER,
    ))

    doc.add_cover_page()
    doc.add_page_break()

    doc.h1("How to Use This Document", numbered=False)
    doc.para(
        f"This document is your preparation guide for the {d['short_name']} workshop. "
        "It is designed to be read in 15–20 minutes before we meet, so that our time together "
        "is spent on your specifics rather than foundational concepts."
    )
    doc.para(d["how_to_use"])
    doc.callout(
        "You are the decision-maker. Our role is to frame the choices, share what we have seen "
        "in comparable engagements, and partner with you to implement the approach that fits your "
        "organization. Every section below is written with that dynamic in mind."
    )

    doc.h1(f"What Is {d['short_name']}?")
    doc.para(d["what_is"])
    for point in d.get("what_is_bullets", []):
        doc.bullet(point)
    if d.get("what_is_closing"):
        doc.para(d["what_is_closing"])

    doc.h1("Why It Matters in Your ServiceNow Journey")
    doc.para(d["why_matters"])
    if d.get("why_matters_bullets"):
        for point in d["why_matters_bullets"]:
            doc.bullet(point)
    if d.get("why_matters_closing"):
        doc.para(d["why_matters_closing"])

    doc.h1("What ServiceNow Delivers Out of the Box")
    doc.para(d["ootb_intro"])
    doc.table(
        headers=["Capability", "What It Does for Your Team"],
        rows=d["ootb_capabilities"],
        col_widths_in=[2.8, 5.76],
    )
    if d.get("ootb_closing"):
        doc.para(d["ootb_closing"])

    doc.add_page_break()

    doc.h1("The Key Decisions You Will Make in Our Workshop")
    doc.para(d["decisions_intro"])
    for i, decision in enumerate(d["decisions"], 1):
        doc.h2(f"Decision {i}: {decision['label']}")
        doc.para(decision["body"])
        if decision.get("tradeoff"):
            doc.para(f"Trade-off to consider: {decision['tradeoff']}", italic=True)

    doc.h1("Things to Think About Before We Meet")
    doc.para(d["reflection_intro"])
    for q in d["reflection_questions"]:
        doc.bullet(q)
    doc.para(
        "You do not need answers to all of these before the workshop. They are prompts for "
        "reflection, not prerequisites. Bring what you have. The workshop is where we work "
        "through the rest together."
    )

    if d.get("what_to_bring"):
        doc.h2("What to Bring to the Workshop")
        for item in d["what_to_bring"]:
            doc.bullet(item)

    doc.callout(
        f"Your ECS team will follow up with a short agenda before the {d['short_name']} workshop. "
        "If you have questions after reading this document, reach out to your ECS engagement manager — "
        "we are happy to walk through any section in advance."
    )

    doc.save(filename)
    return filename


# =============================================================================
# Event Management discipline data
# =============================================================================
DISCIPLINE = {
    "doc_id": "CLT-WP-17",
    "filename": "WP_17_Event_Management_CLIENT.docx",
    "short_name": "Event Management",
    "title": "Event Management\nWorkshop Pre-Read",
    "subtitle": "Turning monitoring noise into actionable operations",
    "audience": "IT Operations Lead, Service Desk Manager, Infrastructure Team",
    "companion_to": "AP-08 Event Management Foundations Pack · AP-09 Event Management Realization Pack",

    "how_to_use": (
        "Section 2 explains what Event Management is in plain language. Section 3 shows what "
        "ServiceNow delivers without any customization. Section 4 describes the decisions you will "
        "make in the workshop — read these carefully, as they are where we will spend most of our "
        "time together. Section 5 has reflection questions to help your infrastructure and operations "
        "teams prepare."
    ),

    "what_is": (
        "Event Management is the ServiceNow capability that connects your monitoring tools — the "
        "systems that watch your servers, networks, applications, and cloud infrastructure — to your "
        "ITSM processes. It sits between the monitoring world and the incident management world, "
        "translating raw monitoring signals into actionable alerts and, where appropriate, "
        "automatically creating and resolving incidents on your team's behalf."
    ),
    "what_is_bullets": [
        "Your monitoring tools generate thousands of events every day — heartbeats, threshold breaches, connectivity checks, performance warnings.",
        "Without Event Management, those signals live only in the monitoring tool. Your operations team watches multiple dashboards and manually creates incidents when something looks wrong.",
        "With Event Management, those signals flow into ServiceNow, are correlated against your configuration item (CI) inventory, filtered for what is genuinely actionable, and surfaced in a single operator workspace.",
        "When a threshold breach is serious enough to warrant a ticket, ServiceNow creates the incident automatically — routed to the right team, linked to the right CI, with the SLA clock already running.",
    ],
    "what_is_closing": (
        "Think of Event Management as the layer that transforms monitoring from a passive observation "
        "activity into an active operations workflow. Your team stops watching dashboards and starts "
        "managing a queue of things that actually need attention."
    ),

    "why_matters": (
        "Most IT organizations have invested heavily in monitoring tools. They know when something "
        "is wrong before users call. The gap is not detection — it is response. Event Management "
        "closes that gap by connecting the detection layer to the response layer without requiring "
        "a developer to build the bridge."
    ),
    "why_matters_bullets": [
        "Reduce mean time to respond: automated incident creation means the ticket exists before the first user calls the help desk.",
        "Reduce manual triage: alerts are pre-correlated to CIs and pre-routed to assignment groups — operators manage exceptions, not every event.",
        "Reduce alert fatigue: noise suppression and deduplication mean your operators see only what needs attention, not every heartbeat and threshold warning from every tool.",
        "Close the loop automatically: when a monitoring tool signals recovery, ServiceNow can resolve the incident without agent intervention — reducing MTTR and freeing the team for higher-value work.",
        "Single pane of glass: one operator workspace across all monitoring tools, replacing the multi-dashboard monitoring wall.",
    ],
    "why_matters_closing": (
        "The organizations that get the most from Event Management are those that treat it as an "
        "operations model change, not just a technology integration. The workshop is where we design "
        "that model together."
    ),

    "ootb_intro": (
        "ServiceNow Event Management includes a comprehensive set of capabilities that are available "
        "without any custom development. The following table summarizes what your team gains "
        "out of the box."
    ),
    "ootb_capabilities": [
        ["Multi-tool event ingestion", "Certified connectors for Dynatrace, SolarWinds, Nagios, Prometheus, Splunk, and others feed events into a single pipeline without custom code."],
        ["Event deduplication", "Duplicate events from the same source about the same issue are collapsed into one alert — your operators see the situation once, not hundreds of times."],
        ["CI correlation", "Events are automatically linked to the Configuration Items in your CMDB — server names, IP addresses, application records — so context travels with every alert."],
        ["Alert promotion to incident", "When an alert meets your defined thresholds (severity, duration, CI tier), ServiceNow creates the incident automatically, routes it to the right team, and starts the SLA clock."],
        ["Auto-resolution", "When the monitoring tool signals recovery, ServiceNow closes the alert and resolves the linked incident — no agent action required."],
        ["Operator Workspace", "A purpose-built view that shows all alerts across all tools in one place, with CI context, severity grouping, and one-click incident promotion."],
        ["Noise suppression rules", "Configurable rules filter out heartbeats, scheduled maintenance events, and below-threshold signals — so the operator queue contains only what is genuinely actionable."],
        ["Service impact analysis", "When a CI alert arrives, ServiceNow can show which business services are affected based on the service model — giving operators immediate business context."],
        ["Alert storm detection", "When a mass outage triggers hundreds of alerts in minutes, Event Management groups them into a single parent alert and incident rather than flooding the queue."],
        ["MID Server connectivity", "On-premises monitoring tools that cannot reach ServiceNow directly connect via a MID Server — a lightweight bridge component that ECS installs and configures in your environment."],
    ],
    "ootb_closing": (
        "All of the capabilities above are available through configuration. None require custom "
        "code to activate. The workshop is where we determine which capabilities are right for "
        "your environment at go-live and which are best introduced in a later phase."
    ),

    "decisions_intro": (
        "These are the decisions that will shape your Event Management implementation. They "
        "require input from your infrastructure, operations, and security teams. None of them "
        "have a universal right answer — the right answer is the one that fits your environment, "
        "your team's maturity, and your operational model."
    ),
    "decisions": [
        {
            "label": "Which monitoring tools will feed ServiceNow at go-live?",
            "body": (
                "You likely have multiple monitoring tools — infrastructure monitoring, application "
                "performance monitoring, network monitoring, cloud-native alerts, and possibly a SIEM. "
                "Not all of them need to connect at go-live. The workshop will help you identify the "
                "two or three tools that generate the most actionable signals and start there. "
                "Additional tools are connected in subsequent phases once the foundation is stable."
            ),
            "tradeoff": "Connecting more tools at go-live gives broader coverage but increases the complexity of event rules, MID Server sizing, and operator training. Starting with 2–3 core tools produces a faster, more reliable go-live.",
        },
        {
            "label": "How should events be correlated to your CI inventory?",
            "body": (
                "ServiceNow matches each incoming event to a Configuration Item in your CMDB using "
                "the host name, IP address, or fully qualified domain name included in the event. "
                "This matching is what enables automatic incident routing, service impact analysis, "
                "and CMDB-linked reporting. The quality of this matching depends directly on the "
                "completeness of your CMDB. The workshop will assess your current CMDB coverage and "
                "define the strategy for handling events from CIs that are not yet in the CMDB."
            ),
            "tradeoff": "A more complete CMDB at go-live means higher correlation rates and more accurate automatic routing. Lower CMDB completeness means more events land in a manual triage queue — which is a workable interim position, but not the end state.",
        },
        {
            "label": "Which alerts should automatically create incidents — and at what threshold?",
            "body": (
                "Not every alert warrants an incident. Promoting too aggressively fills the incident "
                "queue with noise; promoting too conservatively means real issues go untracked. "
                "The workshop will define your promotion thresholds: which severity levels trigger "
                "automatic incident creation, whether non-production CIs are included, and what "
                "duration a threshold must be breached before promotion occurs. Your Service Desk "
                "Manager and IT Operations lead both need to be part of this decision."
            ),
            "tradeoff": "Broader promotion rules reduce the risk of a missed incident but increase noise. Narrower rules keep the incident queue clean but require operators to manually promote medium-severity alerts.",
        },
        {
            "label": "Will you use auto-resolution — and for which incident types?",
            "body": (
                "When a monitoring tool sends a recovery signal, ServiceNow can automatically "
                "resolve the linked incident without agent intervention. This is one of the highest-ROI "
                "features in Event Management — it reduces MTTR, frees agents from close-out work, "
                "and provides a measurable deflection metric. Some organizations exclude high-priority "
                "incidents from auto-resolution because they want a human to confirm resolution for "
                "critical services. The workshop will define your auto-resolution policy."
            ),
            "tradeoff": "Full auto-resolution maximizes efficiency but may feel uncomfortable for Priority 1 incidents. A hybrid approach (auto-resolve P2–P4; require agent confirmation for P1) is a common middle ground.",
        },
        {
            "label": "Who are the designated Event Management operators, and what is their escalation path?",
            "body": (
                "The Event Management Operator Workspace is the daily tool for whoever watches "
                "the alert queue. That person — or rotation of people — needs to be named before "
                "go-live. The workshop will define the operator role, the shift coverage model, "
                "the acknowledgement SLA (how quickly a critical alert must be acknowledged), "
                "and the escalation path when an alert is not acknowledged in time. An unnamed "
                "operator is the same as no operator."
            ),
            "tradeoff": "A formal on-call rotation with named operators maximizes coverage but requires organizational commitment. A best-effort model (whoever is monitoring the tool that day) is lower-overhead but creates gaps during incidents.",
        },
        {
            "label": "How will on-call notifications reach your team outside business hours?",
            "body": (
                "A Critical severity alert at 2am needs to reach someone. ServiceNow Event Management "
                "can send email and SMS notifications for high-severity alerts. For organizations with "
                "an existing on-call tool (PagerDuty, OpsGenie, or ServiceNow On-Call), Event Management "
                "can integrate with it directly. The workshop will confirm your on-call tooling and "
                "define the notification path for after-hours critical alerts."
            ),
            "tradeoff": "Integrating with an existing on-call tool (PagerDuty, OpsGenie) reuses your team's established escalation paths. Email-only notifications are simpler to configure but less reliable for waking someone at 2am.",
        },
    ],

    "reflection_intro": (
        "These questions will help your infrastructure, operations, and security teams prepare "
        "for the Event Management workshop. Share them with the people who will need to be in "
        "the room."
    ),
    "reflection_questions": [
        "Which monitoring tools are currently in use in your environment? Which ones generate the most alerts that your operations team acts on?",
        "How does your team currently create incidents from monitoring alerts — manually, via email, or through an existing automation? What are the pain points with that process?",
        "How complete is your current CMDB for the infrastructure that your monitoring tools cover? Are server names and IP addresses in ServiceNow today?",
        "Do you have an existing on-call tool (PagerDuty, OpsGenie, or similar)? Who manages the on-call roster?",
        "What does your operations team currently use as their primary monitoring dashboard — the monitoring tool itself, a third-party dashboard, or nothing centralized?",
        "Are there any monitoring tools that are being decommissioned or replaced within the next 12 months? Those should likely be excluded from the go-live scope.",
        "What is your approximate peak event volume — how many monitoring alerts does your environment generate on a busy day?",
    ],
    "what_to_bring": [
        "List of active monitoring tools with the vendor name and approximate event volume per tool",
        "Current on-call process documentation (even informal — a spreadsheet or Slack channel is fine)",
        "CMDB completeness estimate: what percentage of your monitored infrastructure has a CI record in ServiceNow today?",
        "Network topology overview showing whether monitoring tools can reach ServiceNow directly or require an on-premises bridge (MID Server)",
        "Contact for your monitoring tool administrators — we will need their involvement to configure the connectors",
    ],
}


# =============================================================================
# BUILD
# =============================================================================
if __name__ == "__main__":
    print("Building WP_17_Event_Management_CLIENT.docx ...")
    f = build_pre_read(DISCIPLINE)
    print(f"  ✓  {os.path.basename(f)}")
    print("Done.")
