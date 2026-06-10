# -*- coding: utf-8 -*-
"""Build: Connection - Weekly Status Report TEMPLATE (client-facing).
Reusable template via EcsDocument. Confidential footer. Fill [bracketed] fields each period."""
import sys, os
REPO = "/sessions/eager-epic-davinci/mnt/everforth-ecs-practice"
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta
LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
OUT = os.path.join(REPO, "05_Clients", "Connection", "02_Delivery", "Connection_Weekly_Status_Report_TEMPLATE.docx")
CONF = "ECS Federal - ServiceNow Practice - Confidential"

doc = EcsDocument(meta=DocMeta(
    eyebrow="CLIENT STATUS REPORT - TEMPLATE",
    title="Connection Engagement\nWeekly Status Report",
    subtitle="Reporting period: [Wk NN] - Sprint [N] - Overall status: [GREEN / YELLOW / RED]",
    org="ECS Federal - ServiceNow Practice",
    audience="Connection Project Sponsor & PM; ECS Delivery Leadership",
    companion_to="Executive Health Dashboard - Governance Triage Log - 18-Week Project Plan",
    doc_id="DEL-CONN-STATUS-01", version="1.0 (template)", status="Template",
    confidentiality=CONF,
    running_header_label="Connection - Weekly Status Report",
    footer_left=CONF,
), logo_path=LOGO)

doc.add_cover_page()
doc.page_break()

doc.h1("How to Use This Template", numbered=False)
doc.para("Reusable weekly status report for the EM-to-Sponsor cadence. Duplicate it each week, set the period/sprint/overall status on the cover, and replace the [bracketed] placeholders and sample rows. Keep it to one read - it pairs with the Executive Health Dashboard for leadership reviews.")

doc.h1("Report Snapshot", numbered=True)
doc.table(headers=["Field", "Value"], rows=[
    ["Reporting period", "[Week NN - MM/DD to MM/DD]"],
    ["Sprint / Stage", "[Sprint N - Stage X]"],
    ["Overall status", "[GREEN / YELLOW / RED]"],
    ["Prepared by", "[Engagement Manager]"],
    ["Distribution", "Connection Sponsor & PM; ECS Practice Lead"],
])

doc.h1("Executive Summary", numbered=True)
doc.para("[1-2 sentences: where the engagement stands this week, the headline, and any decision or help needed.]")

doc.h1("Status by Workstream", numbered=True)
doc.para("RAG per in-scope workstream. Green = on track; Yellow = watch; Red = needs intervention.")
doc.table(headers=["Workstream", "RAG", "Notes"], rows=[
    ["ITSM Core (INC/REQ/PRB/CHG/CAB)", "[G/Y/R]", "[progress / blockers]"],
    ["Service Catalog", "[G/Y/R]", "[ ]"],
    ["Employee Experience (EC / VA / AI Search / KM)", "[G/Y/R]", "[ ]"],
    ["CMDB & CSDM", "[G/Y/R]", "[ ]"],
    ["HAM Foundations", "[G/Y/R]", "[ ]"],
    ["Integrations (AD/SSO, SCCM, Intune, Vonage)", "[G/Y/R]", "[ ]"],
    ["Governance & Data Readiness", "[G/Y/R]", "[ ]"],
])

doc.h1("Accomplishments This Period", numbered=True)
doc.bullet("[Signed-off story / milestone delivered]")
doc.bullet("[Workshop completed with sign-off]")
doc.bullet("[ ]")

doc.h1("Planned for Next Period", numbered=True)
doc.bullet("[Workshops / builds scheduled]")
doc.bullet("[Demos / sign-offs targeted]")
doc.bullet("[ ]")

doc.h1("Risks & Issues", numbered=True)
doc.table(headers=["Item", "Impact", "Owner", "Mitigation / Action", "Status"], rows=[
    ["[Risk or issue]", "[H/M/L]", "[name]", "[action]", "[Open/Closed]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
])

doc.h1("Decisions Needed", numbered=True)
doc.table(headers=["Decision", "Needed by", "Owner"], rows=[
    ["[Decision required from Sponsor / SME]", "[date]", "[name]"],
    ["[ ]", "[ ]", "[ ]"],
])

doc.h1("Governance & Metrics Snapshot", numbered=True)
doc.para("Transparent snapshot shared with the Sponsor each week.")
doc.table(headers=["Measure", "This Period", "Notes"], rows=[
    ["Sprint velocity (3-sprint avg)", "[pts vs planned]", "[trend]"],
    ["Customizations approved (cap 5)", "[N of 5]", "[#6 triggers a PCR conversation]"],
    ["Open Customization Requests", "[N]", "[in triage / at Council]"],
    ["Dependency slips (open)", "[N]", "[from readiness checklist]"],
    ["KPI snapshot (MTTR / SLA / change success)", "[values]", "[once baselined in Platform Analytics]"],
])

doc.h1("Upcoming Milestones", numbered=True)
doc.bullet("[Next sprint demo - date]")
doc.bullet("[Stage milestone - date]")
doc.bullet("[Go-Live - Week 16]")

doc.callout("Pair this report with the Executive Health Dashboard for Sponsor and leadership reviews. Log every deviation in the Governance Triage Log.")

doc.save(OUT)
print("Saved:", OUT)
