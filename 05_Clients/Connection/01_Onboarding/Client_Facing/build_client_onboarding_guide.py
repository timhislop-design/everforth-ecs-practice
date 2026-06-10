# -*- coding: utf-8 -*-
"""
Build: Connection — Client Onboarding Guide (client-facing)
Theme: Modernizing the Core. Audience: Connection stakeholders.
Built via EcsDocument (ecs_template.py). Confidential footer — NOT internal.
"""
import sys, os

REPO = "/sessions/eager-epic-davinci/mnt/everforth-ecs-practice"
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
OUT = os.path.join(REPO, "05_Clients", "Connection", "01_Onboarding", "Client_Facing",
                   "Connection_Client_Onboarding_Guide.docx")

CONF = "ECS Federal · ServiceNow Practice · Confidential"

doc = EcsDocument(meta=DocMeta(
    eyebrow="CLIENT ONBOARDING GUIDE",
    title="Modernizing the Core\nYour Onboarding Guide",
    subtitle="What to expect, who does what, and how we keep the engagement on track — together.",
    org="ECS Federal · ServiceNow Practice",
    audience="Connection — Project Sponsor, Project Manager, Process Owners & Stakeholders",
    companion_to="Connection SOW v2.0 · Governance Charter · 18-Week Project Plan",
    doc_id="CLT-CONN-ONB-01",
    version="1.0",
    status="Draft",
    confidentiality=CONF,
    running_header_label="Connection · Client Onboarding Guide",
    footer_left=CONF,
), logo_path=LOGO)

doc.add_cover_page()
doc.page_break()

# ---- How to use ----
doc.h1("Welcome to the Engagement", numbered=False)
doc.para(
    "Welcome to your ServiceNow reimplementation with ECS Federal. Over the next 18 weeks we will stand up "
    "a clean, modern, AI-ready ServiceNow platform for Connection — built on proven out-of-the-box capability "
    "and a healthy data foundation. This guide is your orientation to the engagement: what we are building, "
    "how the work is sequenced, what your team is responsible for, and the simple checks that keep everyone — "
    "your team and ours — aligned and on track."
)
doc.para(
    "It is intentionally short. It is not the contract (that is the SOW) or the rulebook (that is the Governance "
    "Charter); it is the map. Read it once, keep it handy, and use it to orient anyone joining the effort.",
    italic=True, color=None,
)
doc.callout(
    "The theme of this engagement is “Modernizing the Core.” We are standing up a proven baseline first, "
    "then improving from there. Where the baseline does not fit, the request is captured and managed — never lost."
)

# ---- 1. At a glance ----
doc.h1("The Engagement at a Glance", numbered=True)
doc.para(
    "Connection is moving off a domain-separated shared instance and onto a dedicated, governed platform that is "
    "ready for the AI capabilities you have invested in. Phase 1 is an 18-week effort focused on the core of the "
    "platform: IT Service Management, a healthy CMDB aligned to ServiceNow's Common Service Data Model (CSDM), and "
    "a modern Employee Center."
)
doc.h2("What success looks like")
doc.bullet("A modern, OOTB-aligned platform that is upgrade-friendly and ready for Now Assist, Agentic AI, and Predictive Intelligence.")
doc.bullet("A clean, CSDM-aligned CMDB that supports change risk scoring and trustworthy reporting.")
doc.bullet("A modern Employee Center with Virtual Agent and AI Search that deflects tickets and improves the employee experience.")
doc.bullet("Measurable operational gains tracked from day one: Mean Time to Resolution (MTTR), SLA attainment, and change success rate.")

# ---- 2. OOTB-First, in plain terms ----
doc.h1("The OOTB-First Approach — What It Means for You", numbered=True)
doc.para(
    "Our delivery discipline is “OOTB-First”: we start every build from standard ServiceNow functionality and "
    "demonstrate it before considering any change. This is how we protect your investment, keep the platform "
    "upgradeable, and shorten time-to-value. It is a partnership approach — we will always show you the standard "
    "path first and explain the trade-offs."
)
doc.h2("When something needs to differ from standard")
doc.para(
    "Sometimes a genuine business need cannot be met by configuration alone. When that happens, we do not simply "
    "say no, and we do not quietly build a customization. The request is logged, assessed, and decided transparently "
    "(see “How We Keep on Track” below). Every request is visible to your team — nothing is lost; it is managed."
)
doc.callout(
    "The Rule of Three (plain version): if a need can be met by (1) configuration, (2) a UI policy, or (3) a no-code "
    "flow, we build it. If it cannot, it is treated as a customization and goes through a quick, transparent review "
    "before any work starts."
)

# ---- 3. The journey ----
doc.h1("The 18-Week Journey", numbered=True)
doc.para(
    "The engagement runs as two-week sprints, grouped into four stages. A short Sprint 0 sets the foundation before "
    "the build sprints begin. Go-Live is targeted for Week 16, followed by two weeks of Hypercare support."
)
doc.table(
    headers=["Stage", "Sprints / Weeks", "Focus"],
    rows=[
        ["Stage 1 — Initiate & Plan", "Sprints 0–2 · Wks 1–6", "Governance setup, greenfield platform stand-up, CSDM-aligned data foundation."],
        ["Stage 2 — Execute", "Sprints 3–5 · Wks 7–12", "ITSM Core (Incident/Problem/Change/Request) in Service Operations Workspace; CAB; Employee Center, Virtual Agent & Knowledge."],
        ["Stage 3 — Deliver", "Sprints 6–7 · Wks 13–16", "HAM foundations, analytics, system & user acceptance testing, governed cutover. Go-Live Week 16."],
        ["Stage 4 — Close", "Sprint 8 · Wks 17–18", "Hypercare, stabilization, knowledge transfer, lessons learned, and the 12-month roadmap."],
    ],
    col_widths_in=[2.7, 2.4, 4.26],
)
doc.para(
    "Each sprint ends with a demonstration of working functionality, so you see progress every two weeks rather than "
    "waiting for a big reveal at the end.", italic=True,
)

# ---- 4. Scope ----
doc.h1("What's In Scope for Phase 1", numbered=True)
doc.para("Phase 1 delivers the capabilities below — each chosen because it delivers value now and is a prerequisite for the AI capabilities ahead.")
doc.table(
    headers=["Area", "Phase 1 Scope"],
    rows=[
        ["ITSM Core", "Incident, Request, Knowledge, Problem and Major Incident; Change with CAB Workbench; all in the Service Operations Workspace."],
        ["Service Catalog", "Your 10–15 highest-impact catalog items, plus a small number of generic request items so no team is left without a service path."],
        ["Employee Experience", "Connection-branded Employee Center, Virtual Agent (5 baseline topics), AI Search, and a curated Knowledge Base."],
        ["Platform Baselines", "Subscription Management, Security Center, Predictive Intelligence, and Platform Analytics with benchmarks."],
        ["CMDB & CSDM", "CSDM-aligned CMDB, CI relationship standards, Service Graph Connectors (SCCM, Intune), and Discovery."],
        ["Hardware Asset Mgmt", "Stockrooms and foundational HAM configuration to keep CSDM aligned ahead of Phase 2."],
        ["Integrations", "Active Directory / SSO, SCCM, Intune, and Vonage — leveraging your existing configuration where it is sound."],
    ],
    col_widths_in=[2.5, 6.86],
)
doc.h2("What comes later")
doc.para(
    "Phase 1 deliberately focuses on the core. Later phases build on it: Phase 2 (baseline expansion and enhanced "
    "user experience), Phase 3 (IT Operations Management and intelligence), and Phase 4+ (full AI realization). "
    "Items outside Phase 1 are captured for those phases — not forgotten."
)

# ---- 5. Roles & accountability ----
doc.h1("Who Does What — Roles & Accountability", numbered=True)
doc.para(
    "A clean engagement depends on clear ownership on both sides. The roles below define who does the work and who "
    "owns the decisions. Names are confirmed during Sprint 0 and recorded in your project workspace."
)
doc.h2("Your team (Connection)")
doc.table(
    headers=["Role", "What they own", "Time commitment"],
    rows=[
        ["Project Sponsor  [Name]", "Executive decisions, budget authority, business-need approval (first key), Go-Live authorization.", "4–8 hrs/week"],
        ["Project Manager  [Name]", "Day-to-day coordination, SME scheduling, status to the Sponsor, action tracking.", "50–100%"],
        ["Technical Lead  [Name]", "Environment access, integration credentials, technical approvals.", "25–50%"],
        ["Process SMEs  [Names]", "Process decisions and workshop participation for ITSM, Catalog, Employee Experience, and Asset Management.", "~50% during relevant sprints"],
        ["UAT Testers  [Names]", "Execute acceptance test scenarios and log feedback during testing (Weeks 13–16).", "100% during UAT"],
    ],
    col_widths_in=[2.6, 5.0, 1.76],
)
doc.h2("Our team (ECS)")
doc.table(
    headers=["Role", "What they own"],
    rows=[
        ["Engagement Manager  [Name]", "Overall delivery, governance, schedule, risk, and the Sponsor relationship."],
        ["Solution Architect  [Name]", "Platform architecture, CSDM, technical decisions, and impact assessments."],
        ["Process Consultant  [Name]", "Workshop facilitation, OOTB guidance, training, and UAT support."],
        ["Technical Consultant(s)  [Names]", "Configuration, data loads, and integration builds."],
        ["ECS Practice Lead  [Name]", "Independent quality oversight and the technical-path approval (second key)."],
    ],
    col_widths_in=[2.8, 6.56],
)

# ---- 6. Checks and balances ----
doc.h1("How We Keep on Track — Governance & Checks-and-Balances", numbered=True)
doc.para(
    "Governance on this engagement is deliberately simple and transparent. It exists so decisions are made in the "
    "open, deviations are managed rather than hidden, and leadership on both sides always knows where things stand."
)
doc.h2("The rhythm")
doc.table(
    headers=["Cadence", "What happens", "Who"],
    rows=[
        ["Weekly", "Status report — progress, risks, decisions needed.", "ECS EM → Connection PM"],
        ["Every 2 weeks", "Sprint demo of working functionality + Sponsor sync.", "Both teams"],
        ["As needed (48-hr SLA)", "Customization Council reviews any request to deviate from standard.", "Sponsor + ECS Practice"],
        ["Monthly", "Steering review — outcomes, KPIs, and roadmap.", "Leadership, both sides"],
    ],
    col_widths_in=[2.2, 5.4, 1.76],
)
doc.h2("The Two-Key Decision Model")
doc.para(
    "Any deviation from standard ServiceNow requires two independent approvals: the Connection Sponsor confirms the "
    "business need (first key), and the ECS Practice Lead confirms the technical path (second key). Both keys are "
    "required. This is the single most important protection of your investment — it ensures every customization is "
    "both a real business need and a real technical necessity. In practice a decision takes about 48 hours."
)
doc.h2("The Governance Triage Log")
doc.para(
    "Every deviation request is logged within 24 hours and is visible to your team at any time. The log is the shared, "
    "transparent record of what was requested, what was decided, and why — so nothing is lost and no decision is made "
    "behind closed doors."
)
doc.callout(
    "Your simple check as leadership: each week you should be able to see progress (status report), see it working "
    "(sprint demo), and see every open decision (triage log). If those three are healthy, the engagement is on track."
)

# ---- 7. What we need from you ----
doc.h1("What We Need From You", numbered=True)
doc.para("The engagement moves at the speed of decisions and data. The biggest accelerators are on the Connection side:")
doc.bullet("Empowered process owners who can make decisions in workshops without long approval chains.")
doc.bullet("Timely completion of the Foundation Data Pack (users, locations, groups, assignment rules, SLAs) distributed in Sprint 0.")
doc.bullet("Environment access and integration credentials provided during Sprint 0.")
doc.bullet("SME availability during the sprints relevant to their process area.")
doc.bullet("Prompt feedback during demos and acceptance testing.")

# ---- 8. First two weeks ----
doc.h1("Your First Two Weeks (Sprint 0)", numbered=True)
doc.para("Sprint 0 sets the foundation. Here is what to expect and what we will ask of you:")
doc.table(
    headers=["Activity", "Your part"],
    rows=[
        ["Kickoff meeting", "Sponsor, PM, and key stakeholders attend; we walk the full 18-week journey together."],
        ["Governance setup", "Confirm the Sponsor, sign the Customization Council charter, and agree the meeting rhythm."],
        ["Environment & access", "Technical Lead provisions access and credentials for the dev/test/prod instances."],
        ["Foundation Data Pack", "PM routes the data workbooks to the right owners to begin populating."],
        ["Stakeholder & SME mapping", "Identify process owners and SMEs per area so workshops can be scheduled."],
    ],
    col_widths_in=[2.6, 6.76],
)

# ---- 9. Contacts ----
doc.h1("Key Contacts", numbered=True)
doc.table(
    headers=["Role", "Name", "Contact"],
    rows=[
        ["ECS Engagement Manager", "[Name]", "[email / phone]"],
        ["ECS Solution Architect", "[Name]", "[email]"],
        ["Connection Project Sponsor", "[Name]", "[email]"],
        ["Connection Project Manager", "[Name]", "[email]"],
        ["Escalation path", "[Name]", "[email / phone]"],
    ],
    col_widths_in=[3.0, 3.0, 3.36],
)
doc.callout("Welcome aboard. We are looking forward to modernizing the core with you.")

doc.save(OUT)
print("Saved:", OUT)
