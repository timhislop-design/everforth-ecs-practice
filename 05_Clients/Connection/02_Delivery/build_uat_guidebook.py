import sys, os
REPO="/sessions/eager-epic-davinci/mnt/everforth-ecs-practice"
sys.path.insert(0, os.path.join(REPO,"03_Shared","00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta
LOGO=os.path.join(REPO,"00_Master_Blueprint","assets","everforth_logo.png")
CONF="ECS Federal - ServiceNow Practice - Confidential"
OUT=os.path.join(REPO,"05_Clients","Connection","02_Delivery","Connection_UAT_Guidebook_for_End_Users.docx")
d=EcsDocument(meta=DocMeta(eyebrow="CLIENT DELIVERABLE - UAT GUIDEBOOK",
 title="Connection ServiceNow\nUAT Guidebook for End Users",
 subtitle="Everything you need to test the new platform with confidence - no prior experience required",
 org="ECS Federal - ServiceNow Practice",
 audience="Connection business testers, UAT Lead & Project Sponsor",
 companion_to="UAT End-to-End Test Scripts - Defect Log - User Story backlog",
 doc_id="DEL-CONN-UATG-01", version="1.0", status="Draft",
 confidentiality=CONF, running_header_label="Connection - UAT Guidebook", footer_left=CONF), logo_path=LOGO)
d.add_cover_page(); d.page_break()

d.h1("Welcome - Start Here", numbered=False)
d.para("You have been asked to help test Connection's new ServiceNow platform before it goes live. You do not need to be technical, and you do not need prior testing experience. This guidebook walks you through exactly what to do. Read it once, keep it open while you test, and ask your UAT Lead whenever you are unsure.")
d.callout("Your job in one sentence: follow each test script as written, and tell us whether the system did what the script says it should. That is it.")

d.h1("What UAT Is - and Is Not", numbered=True)
d.para("User Acceptance Testing (UAT) is your chance to confirm the platform works the way your team needs it to, before go-live. It is business validation, not technical testing - ECS already tested the technology. You are answering one question: does ServiceNow do my job the way we agreed in the workshops?")
d.table(headers=["UAT IS", "UAT IS NOT"], rows=[
 ["Validating that business processes work end-to-end", "Hunting for software bugs in ServiceNow (ECS handles that)"],
 ["Confirming the workshop decisions are reflected in the system", "Requesting new features that were not agreed in workshops"],
 ["Finding genuine gaps between what was agreed and what was built", "Comparing the new system to the old one feature-by-feature"],
 ["Giving sign-off that the platform is ready for production", "An open period to keep changing the configuration"],
])
d.callout("If something was never in scope, it is not a failure. Note it and move on - do not mark the script FAIL.")

d.h1("Who Does What", numbered=True)
d.table(headers=["Role", "What you do", "Time"], rows=[
 ["Business Tester (you)", "Run your assigned test scripts; record PASS/FAIL/BLOCKED/SKIP; log defects; re-test fixes.", "~4-6 hrs per UAT sprint"],
 ["UAT Lead", "Assigns scripts, runs daily standups, escalates to ECS, gives the go/no-go recommendation.", "~50% during UAT"],
 ["ECS Engagement Manager / team", "Triages and fixes defects, supports testers, redeploys fixes.", "On-call during UAT"],
 ["Project Sponsor", "Attends the go/no-go review and authorizes go-live.", "~1 hr"],
])

d.h1("How UAT Works on Connection", numbered=True)
d.para("UAT runs in Stage 3 (Sprints 6-7, Weeks 13-16), just before Go-Live in Week 16. Testing is organized into end-to-end suites - complete business journeys - so you test the way work actually flows, not disconnected clicks.")
d.bullet("You will be assigned scripts from one or more suites that match your area.")
d.bullet("Each day starts with a short standup: what you will test, and any blockers.")
d.bullet("You record results in the UAT End-to-End Test Scripts workbook as you go.")
d.bullet("Anything that fails goes in the Defect Log; ECS fixes it and you re-test.")

d.h1("How to Run a Test Script", numbered=True)
d.para("Every script in the workbook is a short journey with numbered steps and an expected result. Run it like this:")
d.bullet("1. Read the whole script first - the Pre-Conditions, the steps, and the Expected End Result.")
d.bullet("2. Make sure the Pre-Conditions are met (you are logged in, test data exists). If not, ask the UAT Lead.")
d.bullet("3. Do each step exactly as written, in order. Do not skip ahead.")
d.bullet("4. After the last step, compare what happened to the Expected End Result.")
d.bullet("5. Record the Result: PASS, FAIL, BLOCKED, or SKIP (see below).")
d.bullet("6. If it FAILED, log a defect (next section) and put the Defect ID on the script row.")
d.table(headers=["Result", "Use it when..."], rows=[
 ["PASS", "The system did what the Expected End Result describes."],
 ["FAIL", "The system did NOT do what was expected (and it was in scope). Log a defect."],
 ["BLOCKED", "You could not run the script - missing access, data, or a dependency. Tell the UAT Lead."],
 ["SKIP", "The script does not apply to your area or was agreed out of scope."],
])

d.h1("How to Log a Good Defect", numbered=True)
d.para("A good defect is one ECS can reproduce and fix quickly. Capture these in the Defect Log: the script ID, the story ID, what you expected, what actually happened, and the exact steps to reproduce it.")
d.h2("Example - a good defect")
d.para("\"Script UAT-REQ-01, step 3: I approved the request from the email link, but the request stayed in 'Pending Approval' instead of moving to fulfillment. Expected: it should move to In Fulfillment. Steps: ordered item X, approved via email at 10:15. Severity P2.\"", italic=True)
d.h2("Example - not a useful defect")
d.para("\"The catalog is confusing.\" - This cannot be reproduced or fixed. Instead, name the script, the step, what you expected, and what happened.", italic=True)
d.callout("Severity guide: P1 = blocks a critical process, no workaround. P2 = major issue, workaround exists. P3 = minor. P4 = cosmetic.")

d.h1("Do's and Don'ts", numbered=True)
d.h2("Do")
d.bullet("Do follow the script exactly and record results honestly.")
d.bullet("Do test against real Connection scenarios and data.")
d.bullet("Do log defects with steps to reproduce - it is the fastest path to a fix.")
d.bullet("Do raise blockers early at standup.")
d.h2("Don't")
d.bullet("Don't fail a script because the new system differs from the old one - different is expected.")
d.bullet("Don't request new features here - capture them as future ideas for a later phase.")
d.bullet("Don't fix or configure anything yourself - just report what you see.")
d.bullet("Don't skip steps or assume - if unsure, ask.")

d.h1("The Test Suites at a Glance", numbered=True)
d.table(headers=["Suite", "What it validates end-to-end"], rows=[
 ["1. Service Desk - Incident Lifecycle", "Report an issue (portal or phone), route, work, resolve, survey; major incidents."],
 ["2. Request & Catalog Fulfillment", "Order an item, approve, fulfill, deliver, close."],
 ["3. Change & Release", "Raise a change, assess CI impact and risk, CAB approval, implement."],
 ["4. Problem to Permanent Fix", "Recurring incidents become a problem with a workaround and a fix via change."],
 ["5. Employee Self-Service & Deflection", "Search, knowledge, and Virtual Agent self-service."],
 ["6. Identity & Access", "SSO login and role-based access from your directory groups."],
 ["7. CMDB / CSDM & Change Impact", "CI data flows in and drives change impact and risk."],
 ["8. Asset Lifecycle (HAM)", "An asset from intake to assignment to retirement."],
 ["9. Knowledge Management", "Author, review, publish, and consume an article."],
 ["10. Reporting & Dashboards", "Your activity shows up correctly in dashboards."],
])

d.h1("Go / No-Go", numbered=True)
d.para("At the end of UAT, the UAT Lead summarizes results (pass rate, open defects by severity) and gives a go/no-go recommendation. The Project Sponsor makes the final go-live decision. P1 and P2 defects are resolved or have an agreed plan before go-live.")

d.h1("Quick FAQ", numbered=True)
d.bullet("\"I don't know if this is a bug or just new.\" - Compare to the Expected End Result in the script. If it matches, PASS, even if it looks different from the old system.")
d.bullet("\"The screen looks different than the workshop.\" - Minor look-and-feel differences are normal; only FAIL if the outcome is wrong.")
d.bullet("\"I broke something / made a mistake.\" - No problem. Note it, tell the UAT Lead, and re-run the script.")
d.bullet("\"I think I found a great new feature idea.\" - Capture it; it goes on the future-phase list, not the defect log.")
d.callout("When in doubt, ask your UAT Lead. There are no silly questions during UAT - guessing causes more rework than asking.")

d.save(OUT); print("Saved UAT guidebook")
