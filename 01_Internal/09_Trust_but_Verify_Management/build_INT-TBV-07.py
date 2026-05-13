"""
Build INT-TBV-07 — Practice Management Monthly Review Template
The Practice Lead's monthly cross-engagement roll-up.
One document per monthly review cycle. Produces the Practice Health Tile and routes escalations.
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

OUT = os.path.join(HERE, "INT-TBV-07_Practice_Management_Monthly_Review.docx")

d = EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL TEMPLATE · PRACTICE MANAGEMENT",
    title="Practice Management\nMonthly Review Template",
    subtitle="Cross-engagement health roll-up for the Practice Lead — 90 minutes once per month",
    audience="Practice Lead (completes and presents) · ECS Leadership (receives Practice Health Tile)",
    companion_to="INT-TBV-01 (Manager Playbook) · INT-TBV-02 (Health Dashboard) · INT-TBV-08 (Course-Correction Playbook)",
    doc_id="INT-TBV-07",
    version="1.0",
    status="Released",
    running_header_label="Internal · Practice Management Monthly Review Template",
))

d.add_cover_page()

d.para(
    "The Practice Management Monthly Review is where the single-engagement view becomes a practice-wide view. "
    "The Practice Lead reviews rolled-up dashboards across all active engagements and produces the Practice "
    "Health Tile — a one-page artifact for ECS leadership. This is where pattern-spotting happens: the same "
    "drift in three engagements at sprint 3 is not three problems, it is one collateral gap."
)

d.h1("How to Use This Template", numbered=False)
d.para(
    "The Practice Lead completes one copy of this template per monthly review cycle (target: first Monday of each month). "
    "Sections 1 through 4 are completed during the 90-minute review session using the rolled-up dashboards from "
    "all active engagements. Section 5 (Practice Health Tile) is extracted and shared with ECS leadership as a "
    "standalone page. Section 6 routes escalations and follow-up actions. "
    "Store the completed review in the practice SharePoint under Practice Management > Monthly Reviews."
)
d.callout(
    "The review exists to answer one question: where is the practice as a whole, not where is any one engagement. "
    "A Practice Lead who reviews only individual engagement status has missed the purpose of this review entirely."
)

d.page_break()

# ── REVIEW HEADER ─────────────────────────────────────────────────────────────
d.h1("Review Header", numbered=False)
d.table(
    headers=["Field", "Value"],
    rows=[
        ["Review Month",                    "[Month Year — e.g., May 2026]"],
        ["Review Date",                     "[Date]"],
        ["Practice Lead",                   "[Name]"],
        ["Active Engagements Reviewed",     "[Number]"],
        ["Engagement Names",                "[List all engagements included in this review]"],
        ["Engagements in Hypercare",        "[List — these are included in roll-up but scored differently]"],
        ["Engagements starting this month", "[List — Sprint 0 or Sprint 1]"],
    ],
    col_widths_in=[2.8, 5.6],
)

d.page_break()

# ── SECTION 1: CROSS-ENGAGEMENT HEALTH ROLL-UP ───────────────────────────────
d.h1("Section 1 — Cross-Engagement Health Roll-Up")
d.para(
    "Transfer the Overall Band from each engagement's INT-TBV-02 Roll-Up tab into the table below. "
    "The Practice Lead reviews each entry and notes any band changes since the prior month."
)
d.table(
    headers=["Engagement", "Sprint", "Process\nAdoption", "Config\nHygiene", "Custom\nVariance", "Adoption\nReadiness", "Sentiment\n& Trust", "Overall\nBand", "Change vs\nPrior Month"],
    rows=[
        ["[Engagement 1]", "", "", "", "", "", "", "", ""],
        ["[Engagement 2]", "", "", "", "", "", "", "", ""],
        ["[Engagement 3]", "", "", "", "", "", "", "", ""],
        ["[Engagement 4]", "", "", "", "", "", "", "", ""],
        ["[Engagement 5]", "", "", "", "", "", "", "", ""],
        ["[Add rows as needed]", "", "", "", "", "", "", "", ""],
    ],
    col_widths_in=[2.0, 0.7, 0.9, 0.9, 0.9, 0.9, 0.9, 0.8, 0.9],
)

d.h2("Band count summary")
d.table(
    headers=["Band", "Count This Month", "Count Last Month", "Change"],
    rows=[
        ["Green",  "", "", ""],
        ["Yellow", "", "", ""],
        ["Orange", "", "", ""],
        ["Red",    "", "", ""],
        ["Total Active Engagements", "", "", ""],
    ],
    col_widths_in=[2.0, 2.0, 2.0, 2.4],
)

d.page_break()

# ── SECTION 2: PATTERN-SPOTTING ───────────────────────────────────────────────
d.h1("Section 2 — Pattern-Spotting Analysis")
d.para(
    "The Practice Lead asks the same five questions every month. A pattern appearing in two or more engagements "
    "at the same sprint stage is not a coincidence — it is a signal that routes to one of four responses: "
    "coaching, collateral build, sales positioning update, or product-feedback escalation."
)

d.h2("Question 1 — Vector patterns: same vector yellow across multiple engagements?")
d.para("Which health vectors are yellow or red in two or more engagements? At what sprint stage does this typically appear?")
d.para("[Enter analysis — or 'No cross-engagement vector pattern identified this month']")
d.table(
    headers=["Vector", "Engagements Affected", "Sprint Stage", "Pattern or Coincidence?", "Response Route"],
    rows=[
        ["Process Adoption",      "", "", "", ""],
        ["Config Hygiene",        "", "", "", ""],
        ["Custom Variance",       "", "", "", ""],
        ["Adoption Readiness",    "", "", "", ""],
        ["Sentiment & Trust",     "", "", "", ""],
    ],
    col_widths_in=[1.8, 1.8, 1.0, 1.8, 2.0],
)

d.h2("Question 2 — Customization patterns: same type of request appearing across engagements?")
d.para(
    "Are certain types of customization requests appearing repeatedly? Same module, same customer archetype, "
    "same OOTB gap? A pattern here signals either a collateral gap (the Adopt-vs-Re-engineer cheatsheet "
    "for that area is missing or insufficient) or a sales positioning gap (the SOW scope is being "
    "interpreted too loosely in presales)."
)
d.para("[Enter analysis]")

d.h2("Question 3 — Sprint timing: drift appearing at the same sprint for multiple engagements?")
d.para(
    "Are engagements drifting at predictable sprint points? Sprints 2 and 4 are historically high-pressure "
    "for customization requests (Catalog at Sprint 2, CMDB at Sprint 4). If multiple engagements are "
    "showing Yellow at the same sprint, the practice may need a Sprint 2 or Sprint 4 specific guide."
)
d.para("[Enter analysis]")

d.h2("Question 4 — Language signals: same customer pushback language appearing across engagements?")
d.para(
    "Are Engagement Managers reporting the same customer language across engagements? "
    "('But our old system did X' for the same X, or 'We have a unique approval requirement' in the same module.) "
    "Repeated language signals either a gap in the pre-workshop pre-reads or a sales expectation mismatch."
)
d.para("[Enter analysis]")

d.h2("Question 5 — Collateral gaps: what would have prevented the drift we observed?")
d.para(
    "For each engagement that moved bands this month, ask: what collateral would have prevented or accelerated "
    "recovery from the drift? A missing Adopt-vs-Re-engineer cheatsheet, a missing discipline how-to guide, "
    "a missing workshop pre-read? These observations drive the quarterly collateral refresh."
)
d.para("[Enter observations]")

d.page_break()

# ── SECTION 3: PATTERN RESPONSE ROUTING ──────────────────────────────────────
d.h1("Section 3 — Pattern Response Routing")
d.para(
    "For each pattern identified in Section 2, the Practice Lead selects one of four response routes. "
    "Multiple routes can be selected for a single pattern. Owners and target dates are assigned."
)
d.table(
    headers=["Pattern", "Response Route", "Owner", "Target Date", "Notes"],
    rows=[
        ["[Pattern from Section 2]", "[Coaching / Collateral / Sales positioning / Product feedback]", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
    ],
    col_widths_in=[2.4, 2.2, 1.2, 1.2, 1.4],
)

d.h2("Response route definitions")
d.table(
    headers=["Route", "Meaning", "Typical Output"],
    rows=[
        ["Coaching",           "A discipline gap in the consultant team — addressed through INT-TBV-09 coaching conversations or a team-wide practice session", "Coaching conversation or team session within 30 days"],
        ["Collateral build",   "A missing or insufficient artifact in the practice library — route to the Master Blueprint catalog as a new build priority", "New artifact added to blueprint roadmap"],
        ["Sales positioning",  "A mismatch between what was sold and what OOTB delivers — route to the sales objection handling pack for update", "Updated INT-SP-06 or presales talking points"],
        ["Product feedback",   "A genuine OOTB gap in ServiceNow that the product team should address — documented and submitted through the ServiceNow partnership channel", "Formal product feedback filed"],
    ],
    col_widths_in=[1.6, 3.4, 3.4],
)

d.page_break()

# ── SECTION 4: ESCALATION DECISIONS ─────────────────────────────────────────
d.h1("Section 4 — Escalation Decisions")
d.para(
    "Three classes of finding escalate from the monthly review to ECS leadership. "
    "Escalation is not an alarm — it is an early-warning so leadership can support, deploy a senior consultant, "
    "or open a sponsor-to-sponsor conversation."
)
d.table(
    headers=["Escalation Class", "Engagement(s)", "Description", "Recommended Leadership Action", "Practice Lead's Ask"],
    rows=[
        ["Red band engagement",          "", "", "", ""],
        ["Pattern in 3+ engagements",    "", "", "", ""],
        ["Renewal / expansion at risk",  "", "", "", ""],
    ],
    col_widths_in=[1.6, 1.4, 2.0, 2.0, 1.4],
)
d.para("Escalation items to be presented to ECS leadership: [Yes / No — if No, state why not applicable this month]")

d.page_break()

# ── SECTION 5: PRACTICE HEALTH TILE ──────────────────────────────────────────
d.h1("Section 5 — Practice Health Tile (Standalone / Leadership Artifact)")
d.para(
    "This section is the artifact the Practice Lead extracts and shares with ECS leadership. "
    "It is designed to be read in under two minutes. Copy the content from Sections 1 through 4 "
    "into this summary format. Do not include raw dashboard data in the tile."
)
d.callout(
    "The Practice Health Tile is for ECS leadership only. It does not go to customers or partners. "
    "It should be formatted to stand alone — do not reference section numbers from this template."
)

d.h2("Practice snapshot — [Month Year]")
d.table(
    headers=["Metric", "Value"],
    rows=[
        ["Active engagements", ""],
        ["Engagements in Green band", ""],
        ["Engagements in Yellow band", ""],
        ["Engagements in Orange band", ""],
        ["Engagements in Red band (named)", ""],
        ["Band movements since last month", ""],
    ],
    col_widths_in=[3.0, 5.4],
)

d.h2("Top 3 findings this month")
d.para("[Finding 1 — one sentence describing the most significant pattern or risk observed this month]")
d.para("[Finding 2 — one sentence]")
d.para("[Finding 3 — one sentence]")

d.h2("Actions the Practice Lead is taking")
d.para("[Action 1 — brief description, owner, target date]")
d.para("[Action 2 — brief description, owner, target date]")
d.para("[Action 3 — brief description, owner, target date]")

d.h2("What Practice Lead needs from ECS leadership")
d.para("[Leadership ask 1 — be specific: a resource, a sponsor-to-sponsor call, a PCR approval, etc. — or 'No leadership action required this month']")

d.page_break()

# ── SECTION 6: ACTION TRACKER ─────────────────────────────────────────────────
d.h1("Section 6 — Monthly Action Tracker")
d.para("All actions identified in this review. The Practice Lead owns tracking through the next monthly review.")
d.table(
    headers=["#", "Action", "Category", "Owner", "Due Date", "Status"],
    rows=[
        ["1", "", "[Coaching/Collateral/Sales/Product]", "", "", "Open"],
        ["2", "", "", "", "", "Open"],
        ["3", "", "", "", "", "Open"],
        ["4", "", "", "", "", "Open"],
        ["5", "", "", "", "", "Open"],
        ["6", "", "", "", "", "Open"],
    ],
    col_widths_in=[0.4, 3.4, 1.8, 1.2, 1.0, 0.8],
)

d.h2("Carry-forward from prior month")
d.para("List any actions from last month's review that are not yet complete.")
d.table(
    headers=["Month Opened", "Action", "Owner", "Status", "Escalate?"],
    rows=[
        ["", "", "", "Open", "No"],
        ["", "", "", "Open", "No"],
        ["", "", "", "Closed", "N/A"],
    ],
    col_widths_in=[1.2, 4.4, 1.2, 1.0, 0.8],
)

d.save(OUT)
print(f"Saved: {OUT}")
