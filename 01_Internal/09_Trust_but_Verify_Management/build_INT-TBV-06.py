"""
Build INT-TBV-06 — Sprint Demo Discipline Audit
Post-demo scorecard completed by the Solution Architect within 24 hours of every sprint demo.
Scores 3 configuration items + 3 language/discipline items. Feeds the health dashboard.
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

OUT = os.path.join(HERE, "INT-TBV-06_Sprint_Demo_Discipline_Audit.docx")

d = EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL AUDIT TEMPLATE · TRUST-BUT-VERIFY DISCIPLINE",
    title="Sprint Demo\nDiscipline Audit",
    subtitle="Completed by Solution Architect within 24 hours of every sprint demo — findings feed INT-TBV-02",
    audience="Solution Architect (completes) · Engagement Manager (reviews within 48 hrs) · Practice Lead (monthly roll-up)",
    companion_to="INT-TBV-01 (Manager Playbook) · INT-TBV-02 (Health Dashboard) · INT-TBV-09 (Coaching Templates)",
    doc_id="INT-TBV-06",
    version="1.0",
    status="Released",
    running_header_label="Internal · Sprint Demo Discipline Audit",
))

d.add_cover_page()

d.para(
    "The sprint demo is where stated discipline meets actual configuration. A team that has been silently "
    "drifting cannot hide it during the demo — the configured artifacts speak for themselves. This audit "
    "converts what the demo revealed into management action within 24 hours."
)

d.h1("How to Use This Audit", numbered=False)
d.para(
    "Complete one audit per sprint demo. The Solution Architect scores all six items within 24 hours of the demo. "
    "The Engagement Manager reviews the completed audit and initiates coaching conversations (INT-TBV-09) "
    "for any item scored below Green within 48 hours. Audit findings that are not coaching opportunities "
    "are wasted findings. Store the completed audit in the engagement's SharePoint folder alongside the "
    "sprint demo recording or slide deck."
)
d.callout(
    "Audit findings are operational, not punitive. Drift is a discipline gap, not a performance failure. "
    "The language used in coaching debrief matters: 'Here is what we observed and here is what we will do "
    "differently next sprint' — not 'here is what you did wrong.'"
)

d.page_break()

d.h1("Audit Header", numbered=False)
d.table(
    headers=["Field", "Value"],
    rows=[
        ["Engagement Name",              "[Enter engagement name]"],
        ["Sprint",                       "[e.g., Sprint 3]"],
        ["Demo Date",                    "[Date]"],
        ["Audit Completed By",          "[Solution Architect name]"],
        ["Audit Date",                  "[Date — must be within 24 hrs of demo]"],
        ["EM Review Date",              "[Date — must be within 48 hrs of audit completion]"],
        ["Modules Demonstrated",        "[List all ServiceNow modules shown in the demo]"],
        ["Customer Attendees",          "[Roles attending — Sponsor, SMEs, etc.]"],
    ],
    col_widths_in=[2.4, 6.0],
)

d.page_break()

# ── CONFIGURATION ITEMS ───────────────────────────────────────────────────────
d.h1("Part A — Configuration Audit Items (3 items)")
d.para(
    "Score each item based on what was demonstrated. Evidence is required for any Yellow or Red score. "
    "'Evidence' means a specific configuration object, screenshot reference, or demo timestamp — not a general impression."
)

d.h2("C-1: Process routing — OOTB tables and states")
d.para(
    "Were the demonstrated processes (Incident, Change, Request, etc.) routing through OOTB tables "
    "(incident, change_request, sc_req_item, etc.) and OOTB states without custom routing logic?"
)
d.table(
    headers=["Score", "Criteria"],
    rows=[
        ["Green ✓",  "All demonstrated processes use OOTB tables and states. No custom routing observed."],
        ["Yellow ⚠", "At least one custom UI policy or client script observed in the demonstrated flow."],
        ["Red ✗",    "Custom table, custom workflow, or custom routing engine observed."],
    ],
    col_widths_in=[1.0, 7.4],
)
d.para("Score: [Green / Yellow / Red]", bold=True, space_after=2)
d.para("Evidence (required if Yellow or Red): [Describe specifically what was observed]")
d.para("Management action required: [None / Coaching debrief / Variance Tracker update / Course-correction]")

d.h2("C-2: Configuration hygiene — catalog, categories, rules, SLAs")
d.para(
    "Were the demonstrated catalog items, category structures, assignment rules, and SLA configurations "
    "within OOTB-defensible counts and patterns per the Config Hygiene tab of INT-TBV-02?"
)
d.table(
    headers=["Score", "Criteria"],
    rows=[
        ["Green ✓",  "All demonstrated configuration objects are within reference counts and patterns."],
        ["Yellow ⚠", "One or more object classes are at the Yellow threshold for this sprint stage."],
        ["Red ✗",    "One or more object classes are at the Red threshold or no rationalization plan exists."],
    ],
    col_widths_in=[1.0, 7.4],
)
d.para("Score: [Green / Yellow / Red]", bold=True, space_after=2)
d.para("Evidence (required if Yellow or Red): [Name the specific metric and the count observed vs. threshold]")
d.para("Management action required: [None / Coaching debrief / Variance Tracker update / Course-correction]")

d.h2("C-3: Customization compliance — approved vs. unannounced builds")
d.para(
    "Did everything demonstrated either (a) represent OOTB configuration, or "
    "(b) represent a Council-approved customization that is logged in INT-TBV-03? "
    "Were there any artifacts demonstrated that appear to be customizations but are not in the Variance Tracker?"
)
d.table(
    headers=["Score", "Criteria"],
    rows=[
        ["Green ✓",  "All demonstrated artifacts are either OOTB or Council-approved and logged."],
        ["Yellow ⚠", "One artifact appears to be a customization not yet in the deviation lifecycle (may be an oversight — verify)."],
        ["Red ✗",    "One or more customizations were demonstrated that are not in INT-TBV-03 and were not surfaced to the EM."],
    ],
    col_widths_in=[1.0, 7.4],
)
d.para("Score: [Green / Yellow / Red]", bold=True, space_after=2)
d.para("Evidence (required if Yellow or Red): [Name the artifact and the gap]")
d.para("Management action required: [None / Log in INT-TBV-03 immediately / Red band trigger — invoke INT-TBV-08]")

d.page_break()

# ── LANGUAGE / DISCIPLINE ITEMS ───────────────────────────────────────────────
d.h1("Part B — Language and Discipline Audit Items (3 items)")
d.para(
    "Score each item based on what was said during the demo, not what was built. Language is a leading indicator "
    "of discipline posture. The 'we just' minimization pattern and the 'absorb the ask' pattern are often "
    "observable in demo language before they show up in the configuration."
)

d.h2("L-1: OOTB defense when challenged")
d.para(
    "When a customer asked a question or raised a concern about an OOTB configuration ("
    "'Why can't we have a custom field here?' 'Our old system had this differently'), "
    "did the consultant deploy the OOTB defense — named the business outcome, described the OOTB path, "
    "and routed any deviation request through the Council lifecycle?"
)
d.table(
    headers=["Score", "Criteria"],
    rows=[
        ["Green ✓",  "Consultant named the business outcome and described the OOTB path when challenged. Any customization request was immediately routed ('Let me get that into the Council process')."],
        ["Yellow ⚠", "Consultant acknowledged the concern but did not fully deploy the OOTB defense. No explicit routing to the Council."],
        ["Red ✗",    "Consultant verbally agreed to a customization in the demo without routing to the Council. Or consultant said 'we can probably do that' without the two-key framework."],
    ],
    col_widths_in=[1.0, 7.4],
)
d.para("Score: [Green / Yellow / Red]", bold=True, space_after=2)
d.para("Specific exchange observed (quote or paraphrase): [Enter here]")
d.para("Management action required: [None / Coaching debrief (INT-TBV-09 Pattern A or B) / Variance Tracker update]")

d.h2("L-2: Deviation lifecycle framing")
d.para(
    "When a customization request or deviation was raised (by the customer or by the consultant), "
    "was it explicitly framed through the deviation lifecycle — raised, analyzed, Council-staged — "
    "rather than handled ad hoc in the meeting?"
)
d.table(
    headers=["Score", "Criteria"],
    rows=[
        ["Green ✓",  "All deviations raised in the demo were immediately framed as Council items with a named next step."],
        ["Yellow ⚠", "Deviation raised but routing was vague ('we'll look at that') without naming the Council process."],
        ["Red ✗",    "Deviation absorbed verbally or ignored — not routed to the Council lifecycle."],
    ],
    col_widths_in=[1.0, 7.4],
)
d.para("Score: [Green / Yellow / Red]", bold=True, space_after=2)
d.para("Specific exchange observed (quote or paraphrase): [Enter here]")
d.para("Management action required: [None / Coaching debrief (INT-TBV-09 Pattern B) / Log deviation in INT-TBV-03]")

d.h2("L-3: 'We just' minimization language")
d.para(
    "Did the consultant use 'we just' minimization language to describe a customization? "
    "Examples: 'We just added a small client script,' 'We just tweaked the workflow,' "
    "'We just made a minor change to the form.' This language normalizes customization and "
    "signals that the discipline posture is eroding."
)
d.table(
    headers=["Score", "Criteria"],
    rows=[
        ["Green ✓",  "No 'we just' minimization language observed. Customizations were described accurately if they were discussed."],
        ["Yellow ⚠", "One or two minimization phrases observed but the substance of the customization was not hidden."],
        ["Red ✗",    "Minimization language used to obscure the nature or extent of a customization from the customer or EM."],
    ],
    col_widths_in=[1.0, 7.4],
)
d.para("Score: [Green / Yellow / Red]", bold=True, space_after=2)
d.para("Specific phrase observed: [Quote exactly if possible]")
d.para("Management action required: [None / Coaching debrief (INT-TBV-09 Pattern A) / Escalate to EM]")

d.page_break()

# ── SUMMARY AND ACTIONS ───────────────────────────────────────────────────────
d.h1("Audit Summary and Management Actions")

d.h2("Score summary")
d.table(
    headers=["Audit Item", "Score", "Management Action Required"],
    rows=[
        ["C-1: Process routing",              "[Green/Yellow/Red]", ""],
        ["C-2: Configuration hygiene",        "[Green/Yellow/Red]", ""],
        ["C-3: Customization compliance",     "[Green/Yellow/Red]", ""],
        ["L-1: OOTB defense when challenged", "[Green/Yellow/Red]", ""],
        ["L-2: Deviation lifecycle framing",  "[Green/Yellow/Red]", ""],
        ["L-3: 'We just' minimization",       "[Green/Yellow/Red]", ""],
        ["Overall audit result",              "[Green/Yellow/Red]", ""],
    ],
    col_widths_in=[2.8, 1.4, 4.2],
)

d.h2("Overall audit interpretation")
d.table(
    headers=["Result", "Criteria", "What the EM Does"],
    rows=[
        ["Green",  "All 6 items Green",             "No action required. File audit. Note in weekly variance scan."],
        ["Yellow", "1–2 items Yellow, none Red",    "Coaching debrief within 48 hrs. Note in weekly scan. Update health dashboard."],
        ["Red",    "Any item Red OR 3+ items Yellow","Coaching debrief within 24 hrs. Update health dashboard vector. Assess for band change. Escalate to Practice Lead if C-3 is Red."],
    ],
    col_widths_in=[1.0, 2.8, 4.6],
)

d.h2("Coaching debriefs required")
d.para("List the coaching conversations this audit triggers. Reference INT-TBV-09 for templates.")
d.table(
    headers=["Consultant", "Pattern (from INT-TBV-09)", "EM Target Date", "Completed?"],
    rows=[
        ["", "", "", "☐"],
        ["", "", "", "☐"],
        ["", "", "", "☐"],
    ],
    col_widths_in=[2.0, 3.0, 2.0, 1.4],
)

d.h2("Dashboard update")
d.para("Update the following tabs in INT-TBV-02 based on this audit's findings:")
d.bullet("Process Adoption tab — update vector score for this sprint week if C-1 scored Yellow or Red.")
d.bullet("Config Hygiene tab — update vector score if C-2 scored Yellow or Red.")
d.bullet("Custom Variance tab — update if C-3 revealed an unlogged customization (log in INT-TBV-03 first).")
d.para("Dashboard updated by: [SA or EM name]    Date: [Date]")

d.callout(
    "If C-3 scored Red (unannounced customization discovered), the EM must invoke the Course-Correction Playbook "
    "(INT-TBV-08) same-day. An unannounced customization automatically triggers the Red variance band — "
    "this is not optional and is not a coaching conversation, it is a course-correction event."
)

d.save(OUT)
print(f"Saved: {OUT}")
