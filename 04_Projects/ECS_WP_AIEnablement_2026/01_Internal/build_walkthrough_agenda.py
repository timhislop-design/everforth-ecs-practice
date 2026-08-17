"""
build_walkthrough_agenda.py — ECS-AIE-03
AI Enablement Team Walkthrough — Session Agenda (Internal)
Project: 04_Projects/ECS_WP_AIEnablement_2026
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ecs_template import EcsDocument, DocMeta, Brand

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(HERE, "everforth_logo.png")

doc = EcsDocument(
    meta=DocMeta(
        eyebrow="INTERNAL SESSION AGENDA",
        title="AI Enablement\nTeam Walkthrough",
        subtitle="45 minutes · what we're building, how the review works, and what each of us owns",
        org="ECS Federal · ServiceNow Practice",
        audience="Practice team working session",
        companion_to="AI Enablement Guidebook (ECS-AIE-01) · Library Navigator · SharePoint Migration Guide (ECS-AIE-02)",
        doc_id="ECS-AIE-03",
        version="1.0",
        status="Session aid",
        confidentiality="Internal Use Only · Confidential",
        running_header_label="Internal · AI Enablement Walkthrough",
    ),
    logo_path=LOGO,
)

doc.add_cover_page()
doc.add_page_break()

doc.h1("Session Goal", numbered=False)
doc.para("Leave this session with three things: a shared understanding of what's been built and why, agreement on how the library review will work, and names next to the first pieces of ownership. Not a goal today: making detailed decisions — the big ones are parked on purpose and scheduled separately.")
doc.callout("Screen setup: guidebook open, navigator open with the repo pulled so links work live.")

doc.h1("Agenda")
doc.table(
    headers=["#", "Segment", "Time", "Reference"],
    rows=[
        ["1", "Why this, why now", "5 min", "Guidebook §1"],
        ["2", "From the team's lists to four engines", "10 min", "Guidebook §3–9"],
        ["3", "The library and the review", "10 min", "Guidebook §2 + §10, navigator demo"],
        ["4", "Where it will live", "3 min", "SharePoint guide, headline only"],
        ["5", "The plan", "7 min", "Guidebook §13"],
        ["6", "Discussion and asks", "10 min", "—"],
        ["", "Close and next steps", "1 min", "—"],
    ],
    col_widths_in=[0.35, 2.9, 0.8, 2.45],
)

doc.h1("Segment Notes")
doc.h2("1 · Why this, why now (5 min)")
doc.para("The frame: we're using AI to improve how we operate everywhere — capture, proposals, PMO, delivery — and our biggest gap is new sales and pipeline, so that's where the effort points first. Say the honest part up front: this is side-of-desk work for all of us, and the plan is built around that reality instead of pretending otherwise.")

doc.h2("2 · From the team's lists to four engines (10 min)")
doc.para("Credit the contributions — Brian's original list, Kasim's story-validation catch, and the second-round list that added knowledge retrieval, estimation, people development, and builder assistance. Then show the consolidation tables: we're not building twenty-seven tools, we're building four engines pointed at different stages of the lifecycle.")
doc.bullet("Engine 1 in plain words: writes and checks documents against our own templates and rules.")
doc.bullet("Engine 2: reads a solicitation or award and pulls out every requirement — which gives us bid scoring, compliance matrices, response outlines, and deliverables lists automatically.")
doc.bullet("Engine 3: compares what we planned against what's actually happening and flags the gaps.")
doc.bullet("Engine 4: makes everything we know searchable — 'have we solved this before?' with a cited answer. It also powers proposal narrative drafting, precedent research, the onboarding tutor, and eventually staffing-fit. Every capability ships with plain directions on how to use it.")
doc.para("Then Kasim's story-validation catch as the proof case for Engine 3 — the catalog item example lands because everyone has lived it: we talk through variables and miss categories, user criteria, descriptions. His catch became a full capability plus a checklist library: for each thing we configure, a 'here's everything that has to be accounted for' list.")
doc.callout("Check question: does anything from the original list feel lost in this consolidation?")

doc.h2("3 · The library and the review (10 min)")
doc.para("Say the framing plainly: 'I've built about 150 documents. None of you have reviewed them. They're a draft until you do.' Then demo the navigator live — pick someone's role, filter to a stage, show the Proposed badges and the stage-review chips. Walk the review model: each person reviews the shelves for the stages they own, with four real verdicts — keep it, fix it, replace it, or flag what's missing. Only what the team ratifies becomes our working baseline. Show the assignments table in guidebook §10, and mention the library gap register in §11 — the reviews start from a pre-seeded list of known gaps, not a blank page.")
doc.callout("Check question: do the role assignments look right? Speak up if you're mapped to a shelf that isn't really yours.")

doc.h2("4 · Where it will live (3 min)")
doc.para("Headline only: GitHub is where we build; the ECS SharePoint site is where the team — and selectively, clients — consume. Internal and client-facing content live in separate libraries so footers can never leak, and nothing reaches the client-ready side until it's ratified. Engagements pull what fits their RFP — this is not one-size-fits-all delivery. Go deeper only if asked.")

doc.h2("5 · The plan (7 min)")
doc.para("Phases at headline level: foundations first, then pipeline (the sales gap), then proposals, project startup, delivery verification, and finally indicators. Point at the rules that protect a part-time team: nothing in flight longer than three weeks, one owner and one independent tester per capability, and a formal pause rule for delivery crunches.")
doc.callout("Check question: does the sequencing match where you actually feel the pain?")

doc.h2("6 · Discussion and asks (10 min)")
doc.para("Open floor first. Then land the specific asks and capture names in the table on the next page:")
doc.bullet("Who's in the working group, and roughly what hours per week are real?")
doc.bullet("Confirm or correct the stage-review assignments from guidebook §10.")
doc.bullet("Volunteer owners for the first capabilities: opportunity qualification briefs, the solicitation shredder, the past-performance matcher.")
doc.bullet("Which live opportunity becomes the pilot?")
doc.para("Parked on purpose — say so, so nothing looks forgotten: the approved AI environment and data-handling rule, and the Bid/No-Bid scorecard criteria and weightings. Both get a dedicated leadership session.", italic=True)

doc.h2("Close (1 min)")
doc.para("Next steps: notes go out with the captured names, the first weekly build sync goes on the calendar, and the capture-shelf review starts with its owner. First build target: the opportunity qualification brief.")

doc.add_page_break()
doc.h1("Capture Sheet", numbered=False)
doc.para("Fill in during segment 6.", italic=True)
doc.table(
    headers=["Item", "Name(s) / decision", "Notes"],
    rows=[
        ["Working group members + real hrs/wk", "", ""],
        ["Capture & pre-sales shelf reviewer", "", ""],
        ["Proposal & SOW shelf reviewer", "", ""],
        ["Award & Sprint 0 shelf reviewer", "", ""],
        ["Delivery shelf reviewer", "", ""],
        ["Verification & PMO shelf reviewer", "", ""],
        ["Closeout shelf reviewer", "", ""],
        ["Owner: opportunity qualification brief", "", ""],
        ["Owner: solicitation shredder + scorecard", "", ""],
        ["Owner: past-performance matcher", "", ""],
        ["Pilot opportunity", "", ""],
        ["Corpus curation owner", "", ""],
        ["First build sync day/time", "", ""],
    ],
    col_widths_in=[2.6, 2.2, 1.7],
)

out = os.path.join(HERE, "ECS_AI_Enablement_Walkthrough_Agenda.docx")
doc.save(out)
print("Saved:", out)
