"""
build_exec_brief_b.py — ECS ExecBrief Blueprint B (Table Extends)
Rebuilt with canonical ECS Federal branding via ecs_template.py
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
OUT  = os.path.join(HERE, "ECS_ExecBrief_BlueprintB_TableExtends_INTERNAL.docx")

doc = EcsDocument(
    meta=DocMeta(
        eyebrow="INTERNAL · OVERHEAD INVESTMENT REQUEST",
        title="Executive Investment Briefing\nBlueprint B — Table Extends Approach",
        subtitle="ECS Delivery Intelligence Platform · Overhead Approval Package · May 2026",
        audience="Senior Director, Practice Lead, Director of Technical Services",
        companion_to="Blueprint B Technical Architecture · ECS_ProjectPlan_BlueprintB_TableExtends.xlsx · Arch Rationale",
        doc_id="INT-DA-EXEC-B",
        version="1.0",
        status="For Review & Approval",
        confidentiality="Confidential — Internal Use Only",
        running_header_label="Internal · Blueprint B Executive Briefing",
    ),
    logo_path=LOGO,
)

doc.add_cover_page()
doc.page_break()

# ── STAT BANNER ─────────────────────────────────────────────────────────────
doc.table(
    headers=["10–12 Weeks", "~960 Hours", "5 Roles", "Unlimited"],
    rows=[["Build Duration", "Total Investment", "Team Required", "Engagements Served"]],
    col_widths_in=[2.34, 2.34, 2.34, 2.34],
    alt_shading=False,
)

# ── 1. EXECUTIVE SUMMARY ────────────────────────────────────────────────────
doc.h1("Executive Summary")
doc.para(
    "Everforth is requesting internal overhead investment to build the ECS Delivery Intelligence Platform — "
    "a system that replaces manual spreadsheets and static status documents with a living, record-driven "
    "delivery management experience inside the customer's ServiceNow instance."
)
doc.para(
    "Blueprint B is the table-extends approach. It achieves the same outcome as Blueprint A — role-based "
    "portal, real-time health scoring, Agile and SPM integration, customer transparency — by extending "
    "ServiceNow's existing native tables rather than building a full custom application. It requires fewer "
    "hours, a less specialized developer, and no App Engine SKU on the customer instance."
)
doc.callout(
    "The ask: Approve ~960 hours of internal overhead across 5 roles over 10–12 weeks, starting June 2026. "
    "Blueprint B delivers the same customer-facing platform as Blueprint A, faster and at lower cost, with "
    "the option to rebuild as a full custom app (Blueprint A) once the design is proven in the field."
)

# ── 2. THE OPPORTUNITY ──────────────────────────────────────────────────────
doc.h1("The Opportunity")
doc.para(
    "Our delivery process runs on manually maintained artifacts that are always slightly stale and require "
    "hours of upkeep every week. Blueprint B replaces that entirely — turning every delivery artifact into "
    "a live record derived from real work in the platform."
)
doc.h2("Blueprint B's Core Advantage")
doc.para(
    "Blueprint B reaches the same destination as Blueprint A — live portal, health score, replaced "
    "spreadsheets — but does it 6–8 weeks sooner and with ~440 fewer hours of investment. By working within "
    "ServiceNow's existing native table structure, we avoid the complexity of custom app certification while "
    "still delivering a fully functional platform. The first real engagement can be running on the platform "
    "by mid-August 2026."
)
doc.h2("The Proof-of-Concept Value")
doc.para(
    "Blueprint B serves as the proof-of-concept for the platform design before committing to a larger "
    "Blueprint A investment. If the portal design or health score logic needs significant changes after "
    "real-world use, it is far cheaper to discover that on a table-extends implementation than on a fully "
    "built custom application."
)

# ── 3. INVESTMENT REQUIRED ──────────────────────────────────────────────────
doc.h1("Investment Required — Hours by Role")
doc.para(
    "The following table represents the total internal overhead hours for Blueprint B. Blueprint B requires "
    "a configurator-level developer rather than a full Studio app developer, which may also reduce the "
    "per-hour cost of the primary resource."
)
doc.table(
    headers=["Role", "Ph 0\nPre-Build", "Ph 1\nExtensions & Roles", "Ph 2\nPortal & Health", "Ph 3\nIntegrations & Content", "Ph 4\nHardening & Release", "TOTAL\nHours", "FTE\nWeeks"],
    rows=[
        ["Lead Configurator / Developer", "8", "140", "140", "100", "80", "468", "11.7"],
        ["Delivery Manager", "8", "30", "30", "24", "86", "178", "4.5"],
        ["Content / Methodology Owner", "4", "16", "16", "48", "72", "156", "3.9"],
        ["QA / ATF Engineer", "0", "0", "60", "48", "40", "148", "3.7"],
        ["Practice Leader (reviews only)", "4", "4", "4", "4", "4", "20", "0.5"],
        ["TOTAL — ALL ROLES", "24", "190", "250", "224", "282", "970", "24.3"],
    ],
    col_widths_in=[2.2, 0.75, 1.05, 1.05, 1.35, 1.15, 0.8, 0.71],
)
doc.callout(
    "FTE equivalent: 970 hours ÷ 40 hrs/week = 24.3 FTE weeks total across all roles — 31% fewer than "
    "Blueprint A. The Lead Configurator is the critical path resource at ~12 FTE weeks; a configurator-level "
    "developer (rather than Studio app developer) reduces both cost and scarcity risk."
)
doc.h2("Role Profiles Required")
doc.table(
    headers=["Role", "Profile Needed", "Can Be"],
    rows=[
        ["Lead Configurator / Developer", "ServiceNow table extensions, portal development, business rules, scripted APIs — no Studio required", "Senior SNow developer or configurator; lower scarcity than Blueprint A Studio developer"],
        ["Delivery Manager", "ECS methodology knowledge; portal UX input; content review", "Existing ECS delivery manager with bandwidth"],
        ["Content / Methodology Owner", "Deep knowledge of ECS collateral; tagging and loading existing docs", "Senior consultant or existing DM; can be part-time Phase 1–2"],
        ["QA / ATF Engineer", "ServiceNow ATF framework; test case design", "Senior developer performing peer QA role; does not need to be dedicated"],
        ["Practice Leader", "Milestone review and strategic sign-off", "Senior Director — 4 hours per phase review only"],
    ],
    col_widths_in=[2.2, 3.8, 3.36],
)

# ── 4. TIMELINE SUMMARY ─────────────────────────────────────────────────────
doc.h1("Timeline Summary")
doc.para(
    "Blueprint B runs 10–12 weeks from decision to v1.0 release — 6–8 weeks faster than Blueprint A. "
    "The shorter timeline is driven by removing the custom app scaffolding (Phase 1 Foundation) and replacing "
    "it with direct table extensions that can begin immediately."
)
doc.table(
    headers=["Phase", "Calendar Weeks", "Target Dates", "Key Milestone"],
    rows=[
        ["Phase 0 — Pre-Build", "Weeks −2 to 0", "May – Jun 2026", "Architecture decision; PDI live; field extension design confirmed"],
        ["Phase 1 — Extensions & Roles", "Weeks 1–3", "Jun 2026", "v0.3: all u_ecs_ fields deployed, role groups configured, ACLs live"],
        ["Phase 2 — Portal & Health Engine", "Weeks 4–7", "Jun–Jul 2026", "v0.6: all portal pages, health score live, customer access working"],
        ["Phase 3 — Integrations & Content", "Weeks 8–10", "Jul–Aug 2026", "v0.8: Agile velocity, SPM milestones, KB content tagged and surfaced"],
        ["Phase 4 — Hardening & Release", "Weeks 11–12", "Aug 2026", "v1.0: ATF coverage, hardening, pilot on first engagement"],
    ],
    col_widths_in=[2.5, 1.4, 1.5, 4.0],
)
doc.callout(
    "First engagement target: mid-August 2026. Blueprint B puts a working delivery platform in consultants' "
    "hands 6–8 weeks before Blueprint A. That is one full engagement cycle of real-world validation before "
    "the Blueprint A investment decision needs to be final."
)

# ── 5. RISK PROFILE ─────────────────────────────────────────────────────────
doc.h1("Risk Profile")
doc.table(
    headers=["Risk Level", "Description"],
    rows=[
        ["LOW",  "Resourcing: configurator-level developer is more available than Studio app developer. Less scheduling risk than Blueprint A."],
        ["LOW",  "No App Engine SKU dependency: Blueprint B works on any ServiceNow instance with standard licensing. Eliminates the SKU conversation in customer discovery."],
        ["MED",  "Upgrade risk: extensions to native tables (Task, pm_project, kb_knowledge) carry exposure when ServiceNow releases major platform versions. Mitigate by limiting field naming to u_ecs_ prefix and documenting all extensions in an upgrade guide."],
        ["MED",  "Commercial packaging: table-extend implementations are harder to package as Store apps. Blueprint B is not a viable ServiceNow Store product without migration to Blueprint A. This is acceptable if Blueprint B is treated as a proof-of-concept rather than the final commercial product."],
        ["LOW",  "Content loading: all ECS collateral already exists. Phase 3 content work is tagging and importing existing docs — no new authoring required."],
    ],
    col_widths_in=[1.2, 8.16],
)

# ── 6. RETURN ON INVESTMENT ──────────────────────────────────────────────────
doc.h1("Return on Investment")
doc.h2("Channel 1 — Delivery Efficiency (Immediate)")
doc.para(
    "Same efficiency gain as Blueprint A: 2–4 hours per week per engagement saved. Across 10 active "
    "engagements annually, that is 1,040–2,080 hours per year recovered — exceeding the build investment "
    "in year one. Blueprint B reaches this return 6–8 weeks earlier than Blueprint A."
)
doc.h2("Channel 2 — Sales Differentiation (Engagements 1+)")
doc.para(
    "Customer-facing delivery portal is the same product for the customer regardless of the underlying "
    "architecture. Blueprint B delivers identical sales differentiation for the OOTB proof narrative at "
    "lower internal cost."
)
doc.h2("Channel 3 — Staged Investment Path")
doc.para(
    "Blueprint B's 970-hour investment proves the design on real engagements before committing ~1,400 hours "
    "to Blueprint A. If the portal design holds up across 2–3 engagements, the migration to Blueprint A "
    "(for the Store path) is de-risked. If the design needs significant changes, we discover this before "
    "the larger investment is made."
)

# ── 7. BLUEPRINT A vs B AT A GLANCE ─────────────────────────────────────────
doc.h1("Blueprint A vs. Blueprint B at a Glance")
doc.table(
    headers=["Factor", "Blueprint A (Custom App)", "Blueprint B (This Brief)"],
    rows=[
        ["Build Duration",              "16–18 weeks",            "10–12 weeks"],
        ["Total Investment",            "~1,400 hours",           "~970 hours"],
        ["Hours Saved vs. Blueprint A", "—",                      "~430 hours (31% less)"],
        ["Lead Developer Profile",      "App developer (Studio)", "Configurator"],
        ["App Engine SKU Required",     "Yes",                    "No"],
        ["Commercial / Store Path",     "Clean — Store-ready",    "Messy — harder to package"],
        ["Upgrade Risk",                "Low — scoped, isolated", "Medium — native table exposure"],
        ["First Engagement Deploy",     "~Oct 2026",              "~Aug 2026"],
        ["Right Choice When",           "Store is the strategic goal; dedicated Studio dev available", "Speed to first use; App Engine uncertain; want proof-of-concept first"],
    ],
    col_widths_in=[2.6, 3.38, 3.38],
)

# ── 8. RECOMMENDATION & DECISION REQUIRED ───────────────────────────────────
doc.h1("Recommendation & Decision Required")
doc.callout(
    "Recommendation: Approve Blueprint B as the starting architecture. The 430-hour savings and 6–8 week "
    "earlier first-engagement deployment make it the right first step. Blueprint B is not the final answer — "
    "it is the proof-of-concept that validates the design before committing to Blueprint A. Define a specific "
    "trigger for the Blueprint A migration (e.g., after 3 successful engagements, or when Store path is "
    "formally committed) so Blueprint B does not become permanent by default."
)
doc.para("Decisions required from this briefing:", bold=True)
doc.table(
    headers=["Decision", "Options", "Owner", "Needed By"],
    rows=[
        ["Architecture approach", "Blueprint B (start) with defined A migration trigger, or Blueprint A directly", "Senior Director + Shawn", "End of architecture review"],
        ["Blueprint A migration trigger", "Define: N engagements, Store commitment, or other trigger", "Senior Director + Shawn", "At same time as arch decision"],
        ["Lead developer resource", "Identify configurator-level developer; confirm availability", "Senior Director", "1 week post-approval"],
        ["Phase 0 kickoff date", "Target: week of 01 Jun 2026", "Senior Director", "This week"],
    ],
    col_widths_in=[2.5, 3.0, 2.0, 1.86],
)

doc.save(OUT)
print(f"Saved: {OUT}")
