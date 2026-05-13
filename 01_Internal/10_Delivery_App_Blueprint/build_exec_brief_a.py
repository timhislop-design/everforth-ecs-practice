"""
build_exec_brief_a.py — ECS ExecBrief Blueprint A (Full Custom App)
Rebuilt with canonical ECS Federal branding via ecs_template.py
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
OUT  = os.path.join(HERE, "ECS_ExecBrief_BlueprintA_CustomApp_INTERNAL.docx")

doc = EcsDocument(
    meta=DocMeta(
        eyebrow="INTERNAL · OVERHEAD INVESTMENT REQUEST",
        title="Executive Investment Briefing\nBlueprint A — Full Custom Application",
        subtitle="ECS Delivery Intelligence Platform · Overhead Approval Package · May 2026",
        audience="Senior Director, Practice Lead, Director of Technical Services",
        companion_to="Blueprint A Technical Architecture · ECS_ProjectPlan_BlueprintA_CustomApp.xlsx · Arch Rationale",
        doc_id="INT-DA-EXEC-A",
        version="1.0",
        status="For Review & Approval",
        confidentiality="Confidential — Internal Use Only",
        running_header_label="Internal · Blueprint A Executive Briefing",
    ),
    logo_path=LOGO,
)

doc.add_cover_page()
doc.page_break()

# ── STAT BANNER ─────────────────────────────────────────────────────────────
doc.table(
    headers=["16–18 Weeks", "~1,400 Hours", "5 Roles", "Unlimited"],
    rows=[["Build Duration", "Total Investment", "Team Required", "Engagements Served"]],
    col_widths_in=[2.34, 2.34, 2.34, 2.34],
    alt_shading=False,
)

# ── 1. EXECUTIVE SUMMARY ────────────────────────────────────────────────────
doc.h1("Executive Summary")
doc.para(
    "Everforth is requesting internal overhead investment to build the ECS Delivery Intelligence Platform — "
    "a ServiceNow application that replaces every manual spreadsheet, static status report, and disconnected "
    "document in our delivery process with a living, record-driven system installed directly on the customer's "
    "ServiceNow instance."
)
doc.para(
    "Blueprint A is the full custom application approach. It builds a scoped ServiceNow application with "
    "purpose-designed tables, a role-based portal, native Agile and SPM integrations, and a health scoring "
    "engine that gives customers real-time engagement transparency. It is the architecturally cleanest approach, "
    "the strongest commercial product, and the one best positioned for the ServiceNow Store."
)
doc.callout(
    "The ask: Approve ~1,400 hours of internal overhead across 5 roles over 16–18 weeks, starting June 2026. "
    "In return: a reusable platform asset that differentiates every ECS proposal, reduces delivery overhead on "
    "every engagement, and builds toward a commercially distributable ServiceNow Store product."
)

# ── 2. THE OPPORTUNITY ──────────────────────────────────────────────────────
doc.h1("The Opportunity")
doc.para(
    "Every ECS engagement today runs on a set of manually maintained artifacts: RAG status spreadsheets updated "
    "on Fridays, risk logs in Excel, decision trackers in Word, sprint tracking worksheets that are always one "
    "version behind. These documents require time to maintain, are stale the moment they are saved, and give "
    "customers a fragmented view of what is happening on their engagement."
)
doc.para(
    "The platform eliminates this entirely. It turns every delivery artifact into a live record in the system "
    "the customer already uses. The delivery manager's job gets simpler. The customer's trust goes up. And every "
    "completed engagement leaves an auditable delivery history that we can use for post-engagement analysis, "
    "benchmarking, and continuous improvement."
)
doc.h2("What This Enables for Sales")
doc.bullet("Every proposal can include: 'You will have real-time visibility into your engagement through our delivery portal — from day one.'")
doc.bullet("The app is a live demonstration of our OOTB philosophy applied to our own operations.")
doc.bullet("Long-term: a ServiceNow Store listing creates a recurring revenue stream independent of services engagement volume.")
doc.h2("What This Enables for Delivery")
doc.bullet("Delivery managers spend less time updating status documents and more time managing delivery.")
doc.bullet("New consultants have guided workflow — 'here is what you need to do this sprint' — reducing ramp time.")
doc.bullet("Practice leadership gets a portfolio-level health view across all active engagements for the first time.")

# ── 3. INVESTMENT REQUIRED ──────────────────────────────────────────────────
doc.h1("Investment Required — Hours by Role")
doc.para(
    "The following table represents the total internal overhead hours required to build Blueprint A to "
    "production-ready v1.0, broken down by role and phase. These hours are non-billable internal investment "
    "charged against practice overhead."
)
doc.table(
    headers=["Role", "Ph 0\nPre-Build", "Ph 1\nFoundation", "Ph 2\nPortal & Health", "Ph 3\nIntegrations", "Ph 4\nContent & ATF", "TOTAL\nHours", "FTE\nWeeks"],
    rows=[
        ["Lead Architect / App Developer", "8", "200", "200", "160", "80", "648", "16.2"],
        ["Delivery Manager", "8", "40", "40", "32", "120", "240", "6.0"],
        ["Content / Methodology Owner", "4", "20", "20", "64", "120", "228", "5.7"],
        ["QA / ATF Engineer", "0", "0", "80", "64", "120", "264", "6.6"],
        ["Practice Leader (reviews only)", "4", "4", "4", "4", "4", "20", "0.5"],
        ["TOTAL — ALL ROLES", "24", "264", "344", "324", "444", "1,400", "35.0"],
    ],
    col_widths_in=[2.5, 0.75, 0.75, 1.1, 0.9, 1.0, 0.8, 0.7],
)
doc.callout(
    "FTE equivalent: 1,400 hours ÷ 40 hrs/week = 35 FTE weeks total across all roles. "
    "The Lead Architect / App Developer is the critical path resource at ~16 FTE weeks and should be "
    "dedicated (not shared across engagements) for the duration."
)
doc.h2("Role Profiles Required")
doc.table(
    headers=["Role", "Profile Needed", "Can Be"],
    rows=[
        ["Lead Architect / App Developer", "ServiceNow Studio app development, scoped apps, custom tables, Service Portal, ATF", "Senior SNow architect; may need to backfill delivery on one engagement"],
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
    "Blueprint A runs 16–18 weeks from decision to v1.0 release. The four build phases can run with some "
    "parallelism where resources allow, but the Lead Architect is the critical path throughout."
)
doc.table(
    headers=["Phase", "Calendar Weeks", "Target Dates", "Key Milestone"],
    rows=[
        ["Phase 0 — Pre-Build", "Weeks −2 to 0", "May – Jun 2026", "Architecture decision; PDI live; team assigned"],
        ["Phase 1 — Application Foundation", "Weeks 1–5", "Jun 2026", "v0.5: scoped app, custom tables, roles, portable update set"],
        ["Phase 2 — Portal & Health Engine", "Weeks 6–10", "Jul 2026", "v0.7: all portal pages, health score live, customer access working"],
        ["Phase 3 — Native Integrations", "Weeks 11–14", "Aug 2026", "v0.9: Agile velocity, SPM milestones, PA charts, VA topics"],
        ["Phase 4 — Content & ATF Release", "Weeks 15–18", "Sep–Oct 2026", "v1.0: content loaded, ATF 80%+, Store prep, pilot on first engagement"],
    ],
    col_widths_in=[2.5, 1.4, 1.5, 4.0],
)
doc.callout(
    "Store certification parallel track: ServiceNow ISV partner enrollment should begin in Phase 0 (Week −2) "
    "and run concurrently with development. Certification review takes 4–6 weeks independently of build progress. "
    "Target Store listing: Q1 2027."
)

# ── 5. RISK PROFILE ─────────────────────────────────────────────────────────
doc.h1("Risk Profile")
doc.table(
    headers=["Risk Level", "Description"],
    rows=[
        ["LOW", "Upgrade risk: scoped app is isolated from ServiceNow platform upgrades. Extensions do not conflict with native tables."],
        ["MED", "Resourcing: Lead Architect / App Developer is a dedicated resource. If shared across engagements, calendar duration extends. Mitigate by ring-fencing one senior developer for 16 weeks."],
        ["MED", "App Engine SKU dependency: customer must have App Engine Standard or equivalent. Confirm during Sprint 0 discovery. Design does not assume PA availability — graceful fallback to native reporting."],
        ["LOW", "Commercial packaging: clean scoped app is the ServiceNow Store standard. No structural obstacles to certification beyond time and ISV program enrollment."],
        ["LOW", "Content loading: all ECS collateral already exists. Phase 4 content work is tagging and importing existing docs — no new authoring required."],
    ],
    col_widths_in=[1.2, 8.16],
)

# ── 6. RETURN ON INVESTMENT ──────────────────────────────────────────────────
doc.h1("Return on Investment")
doc.para(
    "The investment pays back through three channels, each compounding over time."
)
doc.h2("Channel 1 — Delivery Efficiency (Immediate)")
doc.para(
    "Eliminating manual status reporting saves an estimated 2–4 hours per week per engagement. Across 10 active "
    "engagements annually, that is 1,040–2,080 hours per year of recovered billable consultant time — exceeding "
    "the build investment in year one alone."
)
doc.h2("Channel 2 — Sales Differentiation (Engagements 1+)")
doc.para(
    "A customer-facing delivery portal is a differentiator in proposals that competitors cannot replicate without "
    "a similar investment. It directly supports the OOTB proof narrative: we deliver the way we say we deliver, "
    "and we can show you in real time."
)
doc.h2("Channel 3 — Commercial Product (Year 2+)")
doc.para(
    "A ServiceNow Store listing creates a product revenue stream. Even at modest adoption (10–20 customers paying "
    "a subscription or per-engagement fee), the asset generates recurring income independent of services revenue. "
    "The Store listing also drives inbound awareness of the ECS practice from customers shopping for delivery "
    "methodology tools."
)

# ── 7. BLUEPRINT A vs B AT A GLANCE ─────────────────────────────────────────
doc.h1("Blueprint A vs. Blueprint B at a Glance")
doc.table(
    headers=["Factor", "Blueprint A (This Brief)", "Blueprint B (Table Extends)"],
    rows=[
        ["Build Duration",           "16–18 weeks",             "10–12 weeks"],
        ["Total Investment",         "~1,400 hours",            "~960 hours"],
        ["Lead Developer Profile",   "App developer (Studio)",  "Configurator"],
        ["App Engine SKU Required",  "Yes",                     "No"],
        ["Commercial / Store Path",  "Clean — Store-ready",     "Messy — harder to package"],
        ["Upgrade Risk",             "Low — scoped, isolated",  "Medium — native table exposure"],
        ["Long-term Product Potential", "High",                 "Lower"],
        ["Right Choice When",        "Strategic product investment; Store is the goal", "Speed to first use; App Engine not available"],
    ],
    col_widths_in=[2.6, 3.38, 3.38],
)

# ── 8. RECOMMENDATION & DECISION REQUIRED ───────────────────────────────────
doc.h1("Recommendation & Decision Required")
doc.callout(
    "Recommendation: Approve Blueprint A as the target architecture. The additional 440 hours over Blueprint B "
    "are justified by the significantly stronger commercial product, lower long-term maintenance overhead, and "
    "clean path to the ServiceNow Store. Begin Phase 0 immediately following this approval — the architecture "
    "decision and PDI provisioning can start within one week."
)
doc.para("Decisions required from this briefing:", bold=True)
doc.table(
    headers=["Decision", "Options", "Owner", "Needed By"],
    rows=[
        ["Architecture approach", "Blueprint A or Blueprint B", "Senior Director + Shawn", "End of architecture review"],
        ["Lead developer resource", "Identify and ring-fence dedicated developer", "Senior Director", "1 week post-approval"],
        ["ISV partner program enrollment", "Begin now or defer to Q4 2026", "Senior Director + Practice Mgr", "2 weeks post-approval"],
        ["Phase 0 kickoff date", "Target: week of 01 Jun 2026", "Senior Director", "This week"],
    ],
    col_widths_in=[2.5, 3.0, 2.0, 1.86],
)

doc.save(OUT)
print(f"Saved: {OUT}")
