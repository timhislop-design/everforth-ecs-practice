"""
build_collateral_index.py — ECS Collateral Index & Team Review Guide
Rebuilt with canonical ECS Federal branding via ecs_template.py
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
OUT  = os.path.join(HERE, "ECS_CollateralIndex_TeamReviewGuide_INTERNAL.docx")

doc = EcsDocument(
    meta=DocMeta(
        eyebrow="INTERNAL · SENIOR DIRECTOR REFERENCE",
        title="Collateral Index &\nTeam Review Guide",
        subtitle="ECS Delivery Intelligence Platform — All documents, what they are, who they are for, and how to use them together",
        audience="Senior Director, Practice Lead, Director of Technical Services",
        companion_to="Blueprint A · Blueprint B · Arch Rationale · Executive Briefings · Project Plans",
        doc_id="INT-DA-INDEX",
        version="1.0",
        status="For Review",
        confidentiality="Internal Use Only · Confidential",
        running_header_label="Internal · Collateral Index & Team Review Guide",
    ),
    logo_path=LOGO,
)

doc.add_cover_page()
doc.page_break()

# ── 1. WHAT THIS PACKAGE IS ─────────────────────────────────────────────────
doc.h1("What This Package Is")
doc.para(
    "We designed a complete architectural and investment package for the ECS Delivery Intelligence Platform — "
    "a ServiceNow application that replaces manual delivery spreadsheets with a living, role-based platform "
    "tied directly to Agile, SPM, and the Knowledge Base."
)
doc.para(
    "Two architectural approaches were fully designed (Blueprint A: full custom app; Blueprint B: table extends), "
    "each with a detailed technical blueprint, a project plan importable to MS Project or ServiceNow PPM, and an "
    "executive briefing for overhead approval. A rationale document was built for the Director of Technical "
    "Services review. This document is the master index that ties everything together."
)
doc.callout(
    "The pending decision: All collateral is complete for a review session with Shawn (Director of Technical "
    "Services). The one outstanding decision is Blueprint A vs. Blueprint B — everything else can proceed once "
    "that is resolved."
)

# ── 2. WHERE EVERYTHING LIVES ────────────────────────────────────────────────
doc.h1("Where Everything Lives")
doc.para(
    "All delivery app documents are in one folder: 01_Internal / 10_Delivery_App_Blueprint /. This folder is "
    "under 01_Internal because all documents in this package are internal to Everforth. Nothing in this folder "
    "should be shared directly with customers — the executive briefings and blueprints are overhead approval and "
    "architectural review documents, not customer deliverables. Customer-facing materials will be a separate "
    "workstream once the architecture is confirmed."
)

# ── 3. COMPLETE DOCUMENT INDEX ───────────────────────────────────────────────
doc.h1("Complete Document Index")

doc.h2("3.1  Technical Architecture Blueprints")
doc.table(
    headers=["Filename", "What It Is", "When to Use It", "Who Reads It"],
    rows=[
        [
            "ECS_DeliveryApp_Blueprint_A_CustomApp_INTERNAL.docx",
            "Full 13-section technical blueprint for the custom scoped app approach. Data model, role framework, portal design, health score, native module integrations, Store path, implementation sequence, trade-offs.",
            "Architecture review with Shawn. Starting point for developer scoping. Reference during Phase 1–4 build.",
            "Shawn, Senior Director, Lead Developer"
        ],
        [
            "ECS_DeliveryApp_Blueprint_B_TableExtends_INTERNAL.docx",
            "Full technical blueprint for the table-extends approach. Same sections as A: which native tables to extend, u_ecs_ field strategy, ACL approach, upgrade risk management.",
            "Architecture review with Shawn (side by side with Blueprint A). Reference if Blueprint B is selected.",
            "Shawn, Senior Director, Lead Developer"
        ],
    ],
    col_widths_in=[2.6, 2.8, 2.0, 2.0],
)

doc.h2("3.2  Project Plans (MS Project / ServiceNow PPM Importable)")
doc.table(
    headers=["Filename", "What It Is", "Tabs Inside"],
    rows=[
        [
            "ECS_ProjectPlan_BlueprintA_CustomApp.xlsx",
            "Detailed 94-task WBS for Blueprint A. Start/end dates from Jun 1 2026, predecessors, resource assignments, planned hours per task. Ready to import.",
            "Project Plan (94 tasks) | Resource Summary (hours by role by phase) | Import Instructions (MS Project + SNow PPM steps)"
        ],
        [
            "ECS_ProjectPlan_BlueprintB_TableExtends.xlsx",
            "Detailed 94-task WBS for Blueprint B. Same structure. Resource Summary tab includes a live Blueprint A vs B comparison with hours saved calculated.",
            "Project Plan (94 tasks) | Resource Summary (with A vs B comparison) | Import Instructions"
        ],
    ],
    col_widths_in=[2.8, 3.8, 2.76],
)

doc.h2("3.3  Executive Briefings (Overhead Approval)")
doc.table(
    headers=["Filename", "What It Is", "Use This When"],
    rows=[
        [
            "ECS_ExecBrief_BlueprintA_CustomApp_INTERNAL.docx",
            "Executive investment brief for Blueprint A. Business case, investment table (hours by role by phase), timeline, RAG risk profile, ROI rationale, A vs B comparison, decisions required.",
            "Presenting the Blueprint A investment case to practice leadership for overhead budget approval."
        ],
        [
            "ECS_ExecBrief_BlueprintB_TableExtends_INTERNAL.docx",
            "Executive investment brief for Blueprint B. Same structure. Emphasises 31% fewer hours, 40% faster deployment, staged investment rationale.",
            "Presenting the Blueprint B investment case, or presenting both side by side to let leadership choose."
        ],
    ],
    col_widths_in=[2.8, 3.8, 2.76],
)

doc.h2("3.4  Supporting Documents")
doc.table(
    headers=["Filename", "What It Is", "Use This When"],
    rows=[
        [
            "ECS_ArchRationale_ForShawnReview_INTERNAL.docx",
            "Detailed reasoning trace of every architectural decision: why an app vs. standalone, why customer instance, why these tables, why this health formula. 10 challenge questions with teal boxes for Shawn to push back on.",
            "Pre-read for the Shawn architecture review session. Shawn marks this up; decisions are recorded as the outcome."
        ],
        [
            "ECS_CollateralIndex_TeamReviewGuide_INTERNAL.docx",
            "This document. Master index of all collateral, what it is, how to use it, review session guide, and decision tracker.",
            "Onboarding team members to the initiative. Structuring review sessions. Tracking the open decisions."
        ],
    ],
    col_widths_in=[2.8, 3.8, 2.76],
)

# ── 4. HOW TO USE THIS PACKAGE ───────────────────────────────────────────────
doc.h1("How to Use This Package — Suggested Review Sequence")
doc.para(
    "There are two distinct review sessions this package is designed to support. Run them in order — the Shawn "
    "architecture review should happen before the overhead approval request, because Shawn's input may change "
    "the recommendation."
)
doc.h2("Session 1 — Architecture Review with Shawn (60–90 minutes)")
doc.para("Goal: Confirm Blueprint A or B. Resolve the 10 open questions in the rationale doc.")
doc.table(
    headers=["Step", "Action", "Document"],
    rows=[
        ["Pre-read (Shawn)", "Shawn reads ECS_ArchRationale_ForShawnReview_INTERNAL.docx before the session and marks up the challenge boxes with his responses", "Arch Rationale doc"],
        ["Review (both)", "Walk through each challenge question. Record Shawn's answers on the rationale doc directly.", "Arch Rationale doc"],
        ["Compare (both)", "If needed: open both blueprint docs side by side on the A vs B trade-off table in each", "Blueprint A + Blueprint B"],
        ["Decide (both)", "Record the architecture decision and any other resolutions from the open questions table in Section 10 of the rationale", "Arch Rationale doc"],
        ["Action (SD)", "Update this index document (Section 6: Decision Log) with the outcomes", "This document"],
    ],
    col_widths_in=[1.6, 5.0, 2.76],
)

doc.h2("Session 2 — Overhead Approval with Practice Leadership (30–45 minutes)")
doc.para("Goal: Get internal budget/overhead approval to begin the build. Confirm resourcing.")
doc.table(
    headers=["Step", "Action", "Document"],
    rows=[
        ["Present", "Present the Executive Briefing for the selected blueprint (A or B) — or both side by side if leadership wants to make the choice", "Selected ExecBrief"],
        ["Resource", "Confirm the specific developer being ring-fenced. Name matters more than title.", "ExecBrief + Project Plan"],
        ["Timeline", "Walk through the 4-phase timeline. Get agreement on Phase 0 kickoff date.", "Project Plan xlsx"],
        ["Approve", "Record formal overhead approval (or conditions for approval). Update Section 6 of this document.", "This document"],
    ],
    col_widths_in=[1.6, 5.0, 2.76],
)

# ── 5. THE NUMBERS AT A GLANCE ───────────────────────────────────────────────
doc.h1("The Numbers at a Glance")
doc.table(
    headers=["", "Blueprint A — Custom App", "Blueprint B — Table Extends"],
    rows=[
        ["Duration",                "16–18 weeks",      "10–12 weeks"],
        ["Total Hours",             "~1,400",            "~970"],
        ["Lead Developer",          "Studio app dev",    "Configurator"],
        ["Lead Developer Hours",    "648",               "468"],
        ["Delivery Manager Hours",  "240",               "178"],
        ["Content Owner Hours",     "228",               "156"],
        ["QA Hours",                "264",               "148"],
        ["Practice Leader Hours",   "20",                "20"],
        ["App Engine SKU Required", "Yes",               "No"],
        ["Store Path",              "Clean",             "Difficult"],
        ["First Engagement Deploy", "~Oct 2026",         "~Sep 2026"],
        ["Upgrade Risk",            "Low",               "Medium"],
        ["Commercial Scalability",  "High",              "Medium"],
    ],
    col_widths_in=[2.8, 3.28, 3.28],
)

# ── 6. DECISION LOG ──────────────────────────────────────────────────────────
doc.h1("Decision Log")
doc.para(
    "Use this table to record decisions as they are made. Update this document after each review session so "
    "it becomes the authoritative record of what was decided and why."
)
doc.table(
    headers=["Decision", "Options", "Decision Made", "Date", "Owner", "Notes"],
    rows=[
        ["Architecture: A or B", "Blueprint A / Blueprint B", "", "", "SD + Shawn", ""],
        ["Lead developer confirmed", "Name resource", "", "", "SD", ""],
        ["ISV program: start or defer", "Start now / defer", "", "", "SD", ""],
        ["Phase 0 kickoff date", "Target: 01 Jun 2026", "", "", "SD", ""],
        ["App Engine SKU on customers", "Confirm % of portfolio with App Engine", "", "", "Shawn", ""],
        ["Health score validation approach", "Backtest on historical data / go with estimate", "", "", "Shawn", ""],
        ["Content table: own or extend KB", "Custom table (A) / KB extension (B or hybrid)", "", "", "Shawn", ""],
        ["Store vs update set", "Store / Update set / Both", "", "", "SD + Shawn", ""],
        ["Blueprint B exit trigger", "Define N engagements or Store commit", "", "", "SD + Shawn", ""],
        ["Overhead approval granted", "Yes / Yes with conditions / No", "", "", "Practice Mgmt", ""],
    ],
    col_widths_in=[2.2, 2.0, 1.4, 0.8, 1.3, 1.66],
)

doc.save(OUT)
print(f"Saved: {OUT}")
