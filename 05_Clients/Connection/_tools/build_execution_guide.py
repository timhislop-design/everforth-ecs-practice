import sys, os
REPO="/sessions/eager-epic-davinci/mnt/everforth-ecs-practice"
sys.path.insert(0, os.path.join(REPO,"03_Shared","00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta
LOGO=os.path.join(REPO,"00_Master_Blueprint","assets","everforth_logo.png")
LIB=os.path.join(REPO,"06_Client_Upload","Connection","00_START_HERE")
os.makedirs(LIB, exist_ok=True)
OUT=os.path.join(LIB,"Connection_Execution_Guide.docx")
d=EcsDocument(meta=DocMeta(eyebrow="CONNECTION EXECUTION LIBRARY - START HERE",
 title="Connection Engagement\nExecution Guide (Start Here)",
 subtitle="What to use, by role and by phase - the navigator for this library",
 org="ECS Federal - ServiceNow Practice",
 audience="ECS delivery team and Connection - all roles",
 companion_to="Library Index - every artifact in this package",
 doc_id="LIB-CONN-GUIDE-01", version="1.0", status="Released",
 confidentiality="ECS Federal - ServiceNow Practice - Confidential",
 running_header_label="Connection - Execution Guide",
 footer_left="ECS Federal - ServiceNow Practice - Confidential"), logo_path=LOGO)
d.add_cover_page(); d.page_break()
d.h1("How to Use This Library", numbered=False)
d.para("This is the static, execution-ready library for the Connection engagement. It contains the finished deliverables only - no build files. Find your role or your phase below and it points you to exactly what to use. The full catalog is in the Library Index. Folders: 01_Onboarding, 02_Delivery (with Workshops, Accelerator_Packs, Knowledge_Transfer).")
d.callout("Don't read the whole library. Read your row. Each role and each phase below lists only what you need.")

d.h1("By Role", numbered=True)
d.h2("ECS team")
d.table(headers=["Role","Start with","Use throughout"], rows=[
 ["Engagement Manager","Team Onboarding & Vision; Engagement Delivery Guidelines; Project Plan","Status Report; Exec Dashboard; Dependency Tracker; RAID; Deliverables Matrix; Project Controls; Sprint Operating Kit; RACI"],
 ["Solution Architect","Delivery Guidelines; Architecture & CSDM Alignment; Accelerator Packs","Config User Stories; Workshop decks; SIT Scripts; Cutover Runbook"],
 ["Process Consultant / BA (Scrum Master)","Workshop Facilitation Guide; Workshop decks + Pre-Reads; Demo Scripts; Sprint Operating Kit","Config User Stories; Sprint Demo template; Scope Notes; UAT scripts; runs ceremonies + owns velocity/burndown (SM hat)"],
 ["Technical Consultant","Accelerator Packs; Integration & Vonage packs","Config User Stories; SIT Scripts; Demo Scripts"],
 ["Practice Lead","Engagement Delivery Guidelines (trust-but-verify); RACI","Exec Dashboard; Delivery Readiness Audit; Project Controls"],
])
d.h2("Connection (client)")
d.table(headers=["Role","Start with","Use throughout"], rows=[
 ["Executive Sponsor","Client Onboarding Guide; Kickoff Deck; Governance Charter","Exec Dashboard; Dependency Tracker; Go-Live Readiness; sign-offs"],
 ["Product Owner","Client Onboarding Guide; Governance Charter","Workshop Pre-Reads; Acceptance & Sign-off Log; UAT results"],
 ["Project Manager","Client Onboarding Guide; Dependency Tracker","Status Report; Onboarding Checklist; Workshop schedule"],
 ["Technical Lead","Architecture & CSDM Alignment; Integration packs","Dependency Tracker (env/access/MID/Vonage); Cutover Runbook"],
 ["SMEs / Process Owners","Workshop Pre-Reads for their area; Accelerator Packs","Workshop decks; UAT scripts"],
 ["UAT Testers","UAT Guidebook for End Users","UAT End-to-End Test Scripts"],
 ["Platform Admins","Administrator Guide & KT","Operational Handoff Pack"],
])

d.h1("By Phase", numbered=True)
d.table(headers=["Phase (Sprint / Weeks)","What's in play","Key artifacts"], rows=[
 ["Sprint 0 - Setup (Wks 1-2)","Onboard, govern, set dependencies, collect data","Onboarding (client + internal); Governance Charter; Project Plan; Onboarding Checklist; Dependency Tracker; Accelerator Packs (distribute); RACI"],
 ["Stage 1 Build (Sprints 1-2)","Foundation, CSDM, CMDB, Discovery","Workshop decks + Pre-Reads (PF/CSDM/CMDB/Discovery/SGC); Architecture & CSDM Alignment; Config User Stories; Sprint Operating Kit; Demo Scripts"],
 ["Stage 2 Build (Sprints 3-5)","ITSM Core, Change/CAB, Catalog, EX, Integrations","Workshop decks + Pre-Reads; Config User Stories; Accelerator Packs; Vonage CTI pack + workshop; Sprint Demo template"],
 ["Stage 3 Deliver (Sprints 6-7)","HAM, analytics, SIT, UAT, cutover prep","SIT Scripts + Test Data Plan; UAT Test Scripts; UAT Guidebook; Go-Live Readiness Checklist; Cutover Runbook"],
 ["Go-Live (Wk 16)","Governed cutover to production","Cutover Runbook; Go-Live Readiness Checklist; sign-offs"],
 ["Stage 4 Close (Sprints 8)","Hypercare, KT, handover, close","Admin Guide & KT; Train-the-Trainer; Operational Handoff Pack; Lessons Learned (produced at close)"],
 ["Ongoing / Governance","Run the engagement transparently","Status Report; Exec Dashboard; RAID; Project Controls (PCR/acceptance/decisions/assumptions); Deliverables Matrix; Delivery Readiness Audit"],
])

d.h1("The Backlog (everything is a story)", numbered=True)
d.para("Two workbooks form the complete project backlog - import both to ServiceNow Agile:")
d.bullet("Configuration User Stories (141) - the buildable decisions, with Given/When/Then acceptance criteria.")
d.bullet("Project Delivery Stories (55) - documentation, training, governance, testing, go-live, hypercare - so the whole project is visible, not just the build.")
d.callout("This library is a snapshot. The live, reproducible baseline lives in the ECS working framework; updates are made there and re-exported - do not edit these files directly.")
d.save(OUT); print("Saved execution guide ->", OUT)
