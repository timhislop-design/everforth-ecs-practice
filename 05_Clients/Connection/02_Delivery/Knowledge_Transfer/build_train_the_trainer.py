import sys, os
REPO="/sessions/eager-epic-davinci/mnt/everforth-ecs-practice"
sys.path.insert(0, os.path.join(REPO,"03_Shared","00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta
LOGO=os.path.join(REPO,"00_Master_Blueprint","assets","everforth_logo.png")
CONF="ECS Federal - ServiceNow Practice - Confidential"
OUT=os.path.join(REPO,"05_Clients","Connection","02_Delivery","Knowledge_Transfer","Connection_Train_the_Trainer_Toolkit.docx")
d=EcsDocument(meta=DocMeta(eyebrow="CLIENT DELIVERABLE - TRAIN THE TRAINER",
 title="Connection ServiceNow\nTrain-the-Trainer Toolkit",
 subtitle="Enabling Connection's trainers to deliver end-user training - Go-Live KT Package",
 org="ECS Federal - ServiceNow Practice",
 audience="Connection designated trainers & process owners",
 companion_to="SOW v2.0 Sec 11 - Administrator Guide & KT - library demo scripts (INT-DS)",
 doc_id="DEL-CONN-T3-01", version="1.0 (template)", status="Template",
 confidentiality=CONF, running_header_label="Connection - Train-the-Trainer Toolkit", footer_left=CONF), logo_path=LOGO)
d.add_cover_page(); d.page_break()
d.h1("How to Use This Toolkit", numbered=False)
d.para("Per SOW Section 11, ECS delivers two remote Train-the-Trainer sessions per process area to enable Connection's designated trainers; Connection then delivers end-user training and owns ongoing adoption. This toolkit standardizes how ECS runs those sessions and what each trainer leaves with. The live demos draw on the ECS module demo scripts.")
d.h1("The Train-the-Trainer Model", numbered=True)
d.bullet("Two remote sessions per in-scope process area, scheduled near Go-Live.")
d.bullet("Session 1 = ECS demonstrates and explains; Session 2 = trainer teach-back with ECS coaching.")
d.bullet("Trainers leave able to deliver the end-user training and answer common questions.")
d.h1("Session Structure (per area)", numbered=True)
d.table(headers=["Segment","Time","Focus"], rows=[
 ["Overview","10 min","The process, the OOTB happy path, what changed for users"],
 ["Live demo","25 min","Walk the end-user tasks against real Connection data"],
 ["Hands-on","20 min","Trainers practice the tasks in sub-production"],
 ["Teach-back","20 min","Trainer presents a segment; ECS coaches"],
 ["Q&A + materials","15 min","Common questions; hand over the quick-reference outline"],
])
d.h1("Process-Area Coverage", numbered=True)
d.para("Each area gets the two sessions. Use the referenced ECS demo scripts as the demo backbone.")
d.table(headers=["Process area","End-user tasks to cover","Demo script reference"], rows=[
 ["Incident","Raise/triage, work notes, resolve, search KB","INT-DS-01 Incident"],
 ["Request / Catalog","Order an item, track a request, approvals","INT-DS-02 Catalog/Request"],
 ["Knowledge","Find, use, and give feedback on articles","INT-DS-03 Knowledge/VA"],
 ["Employee Center / VA","Self-service portal, Virtual Agent, AI Search","INT-DS-03 Knowledge/VA"],
 ["Change (fulfillers)","Raise standard/normal change, CAB basics","INT-DS-04 Change"],
])
d.h1("Trainer Preparation Checklist", numbered=True)
d.bullet("Confirm access to a sub-production training instance with realistic Connection data.")
d.bullet("Review the relevant demo script and run through the end-user tasks once before the session.")
d.bullet("Prepare 2-3 Connection-specific scenarios per area (real services, real catalog items).")
d.bullet("Confirm the end-user quick-reference outline is ready to hand to trainees.")
d.h1("End-User Quick-Reference Outline", numbered=True)
d.para("Connection builds end-user materials from this outline (ECS provides the structure; Connection owns the content):")
d.bullet("What changed and why (one paragraph, plain language).")
d.bullet("How to do the top 3-5 tasks for the area (step list with screenshots).")
d.bullet("Where to get help (Employee Center, Virtual Agent, service desk).")
d.h1("Delivery Tips", numbered=True)
d.bullet("Use real Connection data, never Lorem ipsum - 'this is OUR data' is when it clicks.")
d.bullet("Teach the OOTB happy path first; note exceptions briefly.")
d.bullet("Keep it task-focused - users care about getting their job done, not the platform.")
d.callout("This toolkit pairs with the Administrator Guide & KT to complete the Knowledge Transfer Package handed over at Go-Live.")
d.save(OUT); print("Saved t3")
