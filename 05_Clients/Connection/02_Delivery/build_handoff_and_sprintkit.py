import sys, os
REPO="/sessions/eager-epic-davinci/mnt/everforth-ecs-practice"
sys.path.insert(0, os.path.join(REPO,"03_Shared","00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta
LOGO=os.path.join(REPO,"00_Master_Blueprint","assets","everforth_logo.png")
CONF="ECS Federal - ServiceNow Practice - Confidential"

# ---- Operational Handoff Pack (client-facing) ----
OUT=os.path.join(REPO,"05_Clients","Connection","02_Delivery","Connection_Operational_Handoff_Pack.docx")
d=EcsDocument(meta=DocMeta(eyebrow="CLIENT DELIVERABLE - OPERATIONAL HANDOFF",
 title="Connection ServiceNow\nOperational Handoff Pack",
 subtitle="Who owns what, the support model, and escalation - for steady-state operations",
 org="ECS Federal - ServiceNow Practice",
 audience="Connection platform team, Service Desk & IT leadership; ECS",
 companion_to="Administrator Guide & KT - Hypercare - Cutover Runbook",
 doc_id="DEL-CONN-HND-01", version="1.0 (template)", status="Template",
 confidentiality=CONF, running_header_label="Connection - Operational Handoff", footer_left=CONF), logo_path=LOGO)
d.add_cover_page(); d.page_break()
d.h1("How to Use This Pack", numbered=False)
d.para("This pack transfers operational ownership of the Connection platform from ECS to Connection at the end of Hypercare. It records who owns each area, the support model, and escalation paths. Confirm names in the [brackets] during Hypercare and sign off at exit.")
d.h1("Ownership Matrix", numbered=True)
d.para("Each platform area has a named Connection owner for steady-state operations:")
d.table(headers=["Area","Connection Owner","What they own"], rows=[
 ["Platform administration","[Platform Admin]","Users, groups, roles, update sets, properties"],
 ["CMDB / CSDM","[CMDB Owner]","CI data quality, health, reconciliation, Discovery"],
 ["ITSM processes","[Process Owner(s)]","Incident, Problem, Change, Request configuration & governance"],
 ["Service Catalog","[Catalog Owner]","Items, approvals, fulfillment, retirement"],
 ["Knowledge","[KM Owner]","KB content, workflow, governance"],
 ["Employee Center / VA","[EX Owner]","Portal, topics, Virtual Agent"],
 ["Integrations / CTI","[Integration Owner]","SGC, AD/SSO, email, Vonage CTI"],
 ["Analytics","[Analytics Owner]","PA indicators, dashboards"],
 ["Governance","[Platform Lead]","Customization Council, Triage Log, upgrade governance"],
])
d.h1("Support Model", numbered=True)
d.para("Tiered support after go-live (per SOW Section 11):")
d.table(headers=["Level","Provider","Function"], rows=[
 ["Level 0","Connection","Self-help, knowledge, Virtual Agent"],
 ["Level 1","Connection","Service Desk intake and first-line resolution"],
 ["Level 2","Connection (then ECS during Hypercare)","In-depth technical support; ECS provides L2+ during the Hypercare window"],
 ["Level 3","ServiceNow","Product/platform vendor support"],
])
d.callout("During Hypercare (2 weeks), ECS provides L2+ escalation for P1/P2 ServiceNow issues in business hours. After Hypercare exit, Connection owns L0-L2; ECS engagement support ends.")
d.h1("Escalation Path & Contacts", numbered=True)
d.table(headers=["Trigger","Escalate to","Contact"], rows=[
 ["P1 production issue (Hypercare)","ECS L2+ / EM","[ECS contact]"],
 ["P1 production issue (post-Hypercare)","Connection platform lead -> ServiceNow","[Connection / SN]"],
 ["Platform/upgrade question","Connection platform lead","[name]"],
 ["Future enhancement / new scope","Connection platform lead -> ECS (new SOW)","[name]"],
])
d.h1("Run & Maintain Responsibilities", numbered=True)
d.bullet("Monitor CMDB Health, scheduled jobs/imports, and integration health.")
d.bullet("Manage update sets and promotions; never develop in production.")
d.bullet("Operate the Customization Council and Triage Log to stay OOTB-aligned.")
d.bullet("Apply ServiceNow releases - test in sub-prod first; review skipped records.")
d.bullet("Maintain knowledge content and catalog items per their governance models.")
d.h1("Transition / Exit Criteria", numbered=True)
d.bullet("Hypercare exit criteria met (stability; no open P1/P2 attributable to ECS config).")
d.bullet("KT Package delivered and acknowledged; admin team confident.")
d.bullet("Ownership matrix names confirmed; escalation contacts live.")
d.bullet("Operational Handoff signed off by Connection platform lead and Sponsor.")
d.callout("Sign-off here marks the formal transition to Connection-owned steady-state operations.")
d.save(OUT); print("Saved handoff")

# ---- Sprint Operating Kit (internal) ----
OUT2=os.path.join(REPO,"05_Clients","Connection","01_Onboarding","Internal_Team","Connection_Sprint_Operating_Kit.docx")
d=EcsDocument(meta=DocMeta(eyebrow="INTERNAL - SPRINT OPERATING KIT",
 title="Connection Engagement\nSprint Operating Kit",
 subtitle="Definition of Ready, ceremonies, and cadence - how we run each sprint",
 org="ECS Federal - ServiceNow Practice",
 audience="ECS delivery team - EM, SA, PC, TC",
 companion_to="Engagement Delivery Guidelines - Sprint Demo template - User Story backlog",
 doc_id="INT-CONN-SOK-01", version="1.0", status="Draft",
 running_header_label="Internal - Connection Sprint Operating Kit"), logo_path=LOGO)
d.add_cover_page(); d.page_break()
d.h1("How to Use This Kit", numbered=False)
d.para("This kit standardizes how we run each two-week sprint on Connection: when a story is Ready, how we plan, demo, and retro, and the weekly cadence. It complements the Definition of Done in the Delivery Guidelines.")
d.h1("Who Runs the Sprint - the Scrum Master Hat", numbered=True)
d.para("On a pod this size we do not staff a dedicated Scrum Master. The Business Process Consultant / Business Analyst (BPC/BA) wears the Scrum Master hat in addition to facilitating workshops and writing stories. As Scrum Master the BPC/BA:")
d.bullet("Runs the ceremonies - planning, daily standup, demo/review, and retro - and owns the two-week cadence.")
d.bullet("Enforces the Definition of Ready at intake and the Definition of Done at close.")
d.bullet("Owns velocity, burndown, and sprint-health signals, and feeds them to the Executive Health Dashboard.")
d.bullet("Removes impediments; escalates the ones the team cannot clear to the Engagement Manager.")
d.bullet("Protects the sprint commitment - shields the pod from mid-sprint scope injection and routes new asks to the backlog or the Customization Council.")
d.bullet("Coaches both the ECS pod and the Connection team on the agile operating rhythm.")
d.callout("Neutrality check: the BPC/BA both writes stories and serves as Scrum Master. Where the two pull against each other - e.g., scope pressure on the sprint - the EM and Practice Lead are the check that keeps the servant-leader role honest. No extra seat required.")
d.h1("Definition of Ready (DoR)", numbered=True)
d.para("A story may enter a sprint only when:")
d.bullet("It traces to a workshop decision (or a clear configuration need) and an epic.")
d.bullet("Acceptance criteria are written (Given/When/Then) and reviewed with the Product Owner.")
d.bullet("Dependencies (data, access, prior stories) are identified and met or scheduled.")
d.bullet("It is estimated (story points) and small enough to finish in the sprint.")
d.bullet("It is OOTB-first; any likely deviation is flagged for the Council before build.")
d.h1("Sprint Planning Agenda (90 min)", numbered=True)
d.bullet("Review sprint goal and capacity (see Sprint Plan & Capacity Model).")
d.bullet("Walk the candidate stories; confirm each meets the DoR.")
d.bullet("Identify dependencies and customer inputs needed this sprint (update the Dependency Tracker).")
d.bullet("Commit the sprint backlog; record in SN Agile.")
d.h1("Sprint Demo / Review", numbered=True)
d.para("Use the Sprint Demo template. Demo working stories against real Connection data; secure Product Owner acceptance (3-business-day window) and record it in the Acceptance & Sign-off Log.")
d.h1("Sprint Retrospective (45 min)", numbered=True)
d.bullet("What went well; what to keep.")
d.bullet("What slowed us; root cause (esp. dependency slips or OOTB-defense churn).")
d.bullet("Actions with owners and due dates; carry into the next sprint.")
d.bullet("Feed material risks/decisions into the RAID and Decision Register.")
d.h1("Weekly Cadence", numbered=True)
d.table(headers=["When","Ceremony / Touchpoint","Owner"], rows=[
 ["Daily","Standup (15 min)","BPC/BA (Scrum Master)"],
 ["Weekly","Status report to Sponsor/PM; health report to practice mgmt (Fri COB)","EM"],
 ["Bi-weekly","Sprint demo + Sponsor sync; planning + retro at sprint boundary","BPC/BA (SM) + EM"],
 ["As needed","Customization Council (48-hr SLA)","EM"],
 ["Monthly","Steering review","EM"],
])
d.callout("The cadence exists to surface issues early. A dependency slip named at standup is cheap; one discovered at the demo is not.")
d.save(OUT2); print("Saved sprint kit")
