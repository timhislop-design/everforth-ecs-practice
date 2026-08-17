# -*- coding: utf-8 -*-
"""
Build: Connection — Staged Rollout Release & Execution Runbook (ECS internal)
Same five-drop format as the client rollout, from the ECS side of the table:
for each drop, the EM's release directions (when, how, what to check) and the
delivery team's execution directions (which internal artifacts carry that stage).
Output lands in 06_Client_Upload/Connection_Staged_Rollout/Internal_Release_Kit/.
"""
import sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
OUT = os.path.join(REPO, "06_Client_Upload", "Connection_Staged_Rollout",
                   "Internal_Release_Kit", "Release_and_Execution_Runbook_INTERNAL.docx")

doc = EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL · STAGED ROLLOUT",
    title="Release & Execution\nRunbook",
    subtitle="EM release directions and team execution directions for each staged document drop",
    org="ECS Federal · ServiceNow Practice",
    audience="ECS Engagement Manager, Solution Architect, BPC/BA, Technical Consultants, Practice Lead",
    companion_to="Drop_Email_Templates_INTERNAL · Staged_Rollout_Guide.xlsx · Connection Sprint Operating Kit",
    doc_id="INT-CONN-ROLL-02",
    version="1.0",
    status="Released",
    confidentiality="Internal Use Only · Confidential",
    running_header_label="Internal · Release & Execution Runbook",
), logo_path=LOGO)

doc.add_cover_page()
doc.page_break()

doc.h1("How This Runbook Works", numbered=False)
doc.para(
    "The client sees five document drops, released just-in-time as each phase approaches. This "
    "runbook is the ECS side of that rhythm. For every drop there are two halves: Release — the "
    "EM's steps to get the package out, the review meeting booked, and expectations set; and "
    "Execution — what the delivery team is running with internally while the client digests that "
    "drop. Internal artifact references point into the working framework "
    "(05_Clients/Connection) and the internal sections of the static library."
)
doc.callout(
    "The standing release pattern, every drop: (1) personalize the drop's email template, "
    "(2) send the drop zip or SharePoint link, (3) book the review meeting within one week of the "
    "send, (4) walk the documents on screen together and set expectations, (5) log the release "
    "date and any follow-ups. Workshop decks are the exception to advance release: they live in each "
    "drop's Post_Workshop folder and go out right after their session. Never release silently."
)

# ---------------------------------------------------------------- Drop 1
doc.h1("Drop 1 — Initial Package", numbered=True)
doc.h2("Release (EM)")
doc.bullet("Timing: with or just ahead of the Sprint 0 kickoff — this drop and the kickoff are one motion.")
doc.bullet("Before sending: confirm name placeholders are filled in the Onboarding Guide, Communication Plan, and Kickoff Deck; set the project-plan start date (18-Week Project Plan, tab 1).")
doc.bullet("Send using the Drop 1 email template; attach the drop zip or the SharePoint folder link.")
doc.bullet("Book the 45-minute package review within a week of kickoff. Agenda: walk the Onboarding Guide and Communication Plan, complete the Communication Plan contact roster live, agree the Dependency Tracker rhythm, show the SOW Deliverables Matrix as the standing scoreboard, and use the Document Roadmap to set the just-in-time expectation for everything that follows.")
doc.bullet("Log the release date; carry any unanswered questions into the Weekly Status Report.")
doc.h2("Execution (team)")
doc.bullet("Everyone: read Connection_Team_Onboarding_and_Vision and the Engagement Delivery Guidelines before kickoff — the client hears one consistent story from every seat.")
doc.bullet("EM: stand up the governance rhythm — Customization Council chartered, Governance Triage & RAID log initialized, Weekly Status and Sponsor Sync invites on calendars per the Communication Plan.")
doc.bullet("BPC/BA (Scrum Master): stand up the sprint cadence from the Sprint Operating Kit; import the user-story backlog (Connection_User_Stories_SN_Agile — epics first) and baseline the Sprint Plan & Capacity model.")
doc.bullet("SA: review the Platform Architecture & CSDM Alignment skeleton; confirm instance access and integration prerequisites via the Dependency Tracker.")
doc.bullet("All roles: check your lane in Connection_Role_and_Accountability_QuickRef; the joint Sprint 0 tasks live in the Onboarding Checklist.")

# ---------------------------------------------------------------- Drop 2
doc.h1("Drop 2 — Foundation & Data", numbered=True)
doc.h2("Release (EM)")
doc.bullet("Timing: ~1 week before the first Stage 1 workshop (Weeks 3-6 window).")
doc.bullet("Send using the Drop 2 email template. Highlight the pre-reads and the data packs; name which workshops need which Connection attendees. Hold the Post_Workshop decks — release each one right after its session.")
doc.bullet("Book the 30-minute review. Agenda: workshop schedule + attendees, data-pack walk-through (who fills what, by when), RACI confirmation.")
doc.bullet("After the review: log agreed data-pack due dates in the Dependency Tracker and track them weekly.")
doc.h2("Execution (team)")
doc.bullet("BPC/BA + SA: prep each session from the Workshop Facilitation Guide (five-tier framework, six-beat pattern); scope nuances per module are in Connection_Workshop_Scope_Notes.")
doc.bullet("SA: run the CSDM demo from INT-DS-05 ahead of the CSDM workshop; drive CI-class and service-taxonomy decisions into the CMDB_CSDM pack's consultant tabs.")
doc.bullet("TC: stage Foundation data imports as packs come back — customer data in the system early is the demo engine for everything downstream.")
doc.bullet("EM: first Sponsor Sync with the Executive Health Dashboard this stage; any deviation requests from workshops go straight to the Triage log — never absorbed silently into sprints.")

# ---------------------------------------------------------------- Drop 3
doc.h1("Drop 3 — ITSM Core", numbered=True)
doc.h2("Release (EM)")
doc.bullet("Timing: ~1 week before the ITSM workshops (Weeks 7-10 window).")
doc.bullet("Send using the Drop 3 email template; stress process-owner attendance — this is the stage where the right people in the room matters most. Post_Workshop decks go out after each session.")
doc.bullet("Book the 30-minute review. Agenda: workshop calendar, process-decision expectations (OOTB baseline first, Rule of Three for exceptions), catalog-item shortlist timing.")
doc.h2("Execution (team)")
doc.bullet("BPC/BA: run Incident, Change, and Catalog demos from INT-DS-01, INT-DS-04, and INT-DS-02; six-beat every workshop; decisions land in the ITSM and Service Catalog pack tabs same-day.")
doc.bullet("SA: hold the line on the Rule of Three — every deviation request gets the OOTB alternative presented first and a Triage log entry; Council reviews on the bi-weekly cadence.")
doc.bullet("TC: build from accepted stories only (Definition of Ready enforced at intake); story completion feeds the Executive Health Dashboard.")
doc.bullet("EM: sprint demos every two weeks from the Sprint Demo template — working software, no slideware.")

# ---------------------------------------------------------------- Drop 4
doc.h1("Drop 4 — Employee Experience & Analytics", numbered=True)
doc.h2("Release (EM)")
doc.bullet("Timing: ~1 week before the experience workshops (Weeks 11-14 window).")
doc.bullet("Send using the Drop 4 email template; encourage a wider audience — internal comms and employee-experience voices in the Employee Center and Virtual Agent sessions. Post_Workshop decks go out after each session.")
doc.bullet("Book the 30-minute review. Agenda: session attendees, what go-live looks like for employees, UAT window preview (testers identified now, not in Week 13).")
doc.h2("Execution (team)")
doc.bullet("BPC/BA: run Knowledge/VA, HAM, and PA demos from INT-DS-03, INT-DS-06, and INT-DS-07; Virtual Agent topics capped at the five baseline topics — expansion goes to the roadmap, not the sprint.")
doc.bullet("SA: Predictive Intelligence readiness depends on data quality — validate against the PI pack before committing scope; HAM stays foundations-only per SOW.")
doc.bullet("EM + BPC/BA: begin UAT logistics — tester roster, UAT window on calendars, defect triage rhythm agreed; SIT planning starts from Connection_SIT_Test_Scripts.")
doc.bullet("EM: watch sprint-capacity pressure this stage (widest module spread); PCR anything that threatens the Go-Live date — scope moves, the date holds.")

# ---------------------------------------------------------------- Drop 5
doc.h1("Drop 5 — Testing, Go-Live & Handoff", numbered=True)
doc.h2("Release (EM)")
doc.bullet("Timing: as UAT scheduling begins (Weeks 13-16 window); KT and handoff pieces can re-release at Hypercare start.")
doc.bullet("Send using the Drop 5 email template; frame UAT findings as the system working, not failing.")
doc.bullet("Book the 45-minute review. Agenda: UAT window and tester onboarding (Guidebook walk-through), go/no-go criteria from the Readiness Checklist, KT schedule for admins and trainers.")
doc.bullet("Go/no-go is a formal joint session against the gated checklist — schedule it in Week 15, not go-live week.")
doc.h2("Execution (team)")
doc.bullet("TC + SA: execute SIT from Connection_SIT_Test_Scripts before UAT opens; test data per the pack's Test Data Plan.")
doc.bullet("BPC/BA: run daily defect triage through the UAT window using the Defect Log in the UAT scripts workbook; story-coverage tab proves nothing falls through.")
doc.bullet("SA: rehearse the Cutover Runbook end-to-end before Week 16 — sequence, validation points, rollback trigger owned and named.")
doc.bullet("EM + PL: Hypercare per the Communication Plan cadence; close with the Operational Handoff Pack, lessons learned, and the 12-month roadmap conversation from Connection_Closeout material.")
doc.bullet("PL: independent trust-but-verify pass before closeout — the engagement ends the way it ran: governed, demonstrated, documented.")

doc.callout(
    "If the client rhythm and the ECS rhythm ever disagree, the Communication Plan wins — it is "
    "the promise we made. Update it deliberately (and re-release it) rather than drifting from it."
)

doc.save(OUT)
print(f"Saved: {OUT}")
