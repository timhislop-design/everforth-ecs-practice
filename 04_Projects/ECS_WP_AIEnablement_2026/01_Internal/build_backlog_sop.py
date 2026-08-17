"""
build_backlog_sop.py — ECS-AIE-04
Backlog & Enhancement Management SOP (Internal)
Project: 04_Projects/ECS_WP_AIEnablement_2026
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ecs_template import EcsDocument, DocMeta, Brand

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(HERE, "everforth_logo.png")

doc = EcsDocument(
    meta=DocMeta(
        eyebrow="INTERNAL STANDARD OPERATING PROCEDURE",
        title="Backlog & Enhancement\nManagement SOP",
        subtitle="One intake, three backlogs, clear decision rights — how ideas become committed work without displacing it",
        org="ECS Federal · ServiceNow Practice",
        audience="Practice team, AI working group / CoE",
        companion_to="AI Enablement Guidebook (ECS-AIE-01 v1.1) · Collateral Blueprint Catalog · Library Navigator",
        doc_id="ECS-AIE-04",
        version="1.0",
        status="Draft for working-group review",
        confidentiality="Internal Use Only · Confidential",
        running_header_label="Internal · Backlog & Enhancement SOP",
    ),
    logo_path=LOGO,
)

doc.add_cover_page()
doc.add_page_break()

doc.h1("Purpose", numbered=False)
doc.para("This SOP is the single home for how the practice manages backlogs and enhancement requests. The process previously lived in pieces across the AI Enablement Guidebook, the blueprint catalog, and working-session notes; this document consolidates it. When this SOP and another document disagree on process, this SOP wins; when it disagrees on strategy, the guidebook wins.")
doc.callout("The one-rule version: every idea enters through one intake, lands on exactly one of three backlogs, and gets prioritized on a cadence — never in the moment, and never by displacing committed work.")

doc.h1("The Three Backlogs")
doc.para("Different kinds of work live on different backlogs with different sources of truth. The first routing decision for any request is simply: which backlog does this belong to?")
doc.table(
    headers=["Backlog", "What's on it", "Source of truth", "Prioritized by"],
    rows=[
        ["A — AI Capability Backlog", "AI engines, capabilities, and enhancements to them (the guidebook §13 table)", "AI Enablement Guidebook §13; working copy maintained by the CoE", "Working group / CoE, quarterly; sales-first ordering per the guidebook"],
        ["B — Library Collateral Backlog", "Practice collateral to build, correct, or add — including the §11 gap register and everything stage reviews surface", "blueprint_catalog.json (+ PROJECT_STATUS.md snapshot); review verdicts in library_review_status.json", "Practice Lead + Sr. Director; gap-register items ride their stage's review phase"],
        ["C — Engagement Delivery Backlogs", "Stories, changes, and enhancements inside a client engagement — one backlog per engagement, owned there", "The engagement's story/backlog tracker (JIT Baseline Stories as the seed); change requests via the CR process", "Engagement's own cadence (EM/PL + client product owner); this SOP sets the pattern, not the priorities"],
    ],
    col_widths_in=[1.5, 2.2, 1.7, 1.6],
)
doc.para("Boundary rule: engagement-specific work never lands on backlogs A or B. If an engagement surfaces something reusable — a pattern, a template fix, a capability idea — the reusable kernel is extracted and submitted to A or B through intake; the engagement-specific work stays in that engagement.", italic=True)

doc.h1("Intake — How Anything Gets In")
doc.para("One intake path, run by the working group wearing its CoE hat. No side-channel builds: work that skipped intake does not get adopted, supported, or added to the registry.")
doc.table(
    headers=["Step", "What happens", "Who"],
    rows=[
        ["1. Submit", "Requester brings the ask to the weekly build sync or drops it in the intake list with two sentences: what it does, who benefits", "Anyone"],
        ["2. Route", "Which backlog — A, B, or C? Engagement-specific work goes back to its engagement (with the reusable kernel extracted if there is one)", "CoE at the build sync"],
        ["3. Map", "Backlog A items map to an engine (1–4). Maps to none? It is either a genuinely new engine — rare, and scrutinized accordingly — or it gets parked. Backlog B items map to a lifecycle stage and shelf", "CoE"],
        ["4. Size & place", "S / M / L sizing (guidebook §13 scale); assigned a phase or the unscheduled pool. L items are split before they start", "CoE"],
        ["5. Decide", "Accepted onto the backlog, parked with a one-line written reason, or declined. Parked is a real answer — it means 'not ahead of committed work,' not 'never'", "Decision owner (see below)"],
    ],
    col_widths_in=[1.1, 4.0, 1.4],
)
doc.h2("Enhancements to existing capabilities and collateral")
doc.para("An enhancement request follows the same path with one addition: the owner of the existing capability or artifact gets first say on whether it is an enhancement (same thing, better) or a new item (different thing) — because enhancements inherit the original's priority and owner, while new items compete for a backlog slot like everything else. Bug-class fixes to something already shipped skip the queue: the owner fixes or schedules them within one increment, because broken-and-adopted outranks new-and-shiny.")

doc.h1("Decision Rights")
doc.table(
    headers=["Decision", "Owner"],
    rows=[
        ["Routing, engine mapping, sizing", "CoE (working group) at the build sync"],
        ["Backlog A acceptance and phase placement", "Working group consensus; Sr. Director breaks ties"],
        ["Backlog B acceptance and build order", "Practice Lead + Sr. Director; stage reviewers feed it via verdicts and the gap register"],
        ["Backlog C (engagement)", "That engagement's EM/PL with the client product owner — per the engagement's own governance"],
        ["Parking or declining any item", "Same owner as acceptance; always with a written one-liner"],
        ["Emergency insertion mid-phase", "Sr. Director only — and it displaces something visibly, by name, at the same size"],
    ],
    col_widths_in=[2.9, 3.6],
)

doc.h1("Cadence")
doc.bullet("Weekly (build sync, 60 min): intake triage for new asks; demo what shipped; commit the next increment. Intake triage is timeboxed to ten minutes — depth belongs in the quarterly review.")
doc.bullet("Per phase entry: the stage's collateral review runs (guidebook §10), and its verdicts and gap items land on Backlog B for that phase's scope.")
doc.bullet("Quarterly: full re-prioritization of Backlogs A and B — the only time standing priorities move. Adoption data decides too: shipped capabilities nobody uses get fixed or retired before anything new starts.")
doc.bullet("Never: re-prioritization in the moment because something new feels urgent. Urgency claims route to the emergency-insertion rule and its named owner.")

doc.h1("Statuses and the Paper Trail")
doc.para("Every item on Backlogs A and B carries exactly one status: Proposed (through intake, not yet decided), Accepted (on the backlog with a phase or pool), In Progress (owned, inside an increment), Shipped (definition of done met — including user directions), Parked (with its one-line reason), or Declined. The working copies live in the project folder and the catalog; status changes happen at the build sync, not in private. The prompt/pattern registry records what shipped; the navigator and review-status file record what the library holds and what the reviews decided.")

doc.h1("What Good Looks Like")
doc.bullet("A teammate with an idea knows exactly where to take it, and gets an answer — including 'parked, because' — within a week.")
doc.bullet("Committed work is never silently displaced; when priorities change, something is visibly traded, by name.")
doc.bullet("The backlogs are honest: everything on them is really coming; everything parked says why; nothing lives in someone's head.")
doc.bullet("Enhancements strengthen what exists before the practice builds what doesn't.")

out = os.path.join(HERE, "ECS_Backlog_and_Enhancement_SOP_v1.0.docx")
doc.save(out)
print("Saved:", out)
