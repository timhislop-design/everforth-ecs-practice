# Delivery (non-config) stories. add(epic, short, role, want, benefit, ac[], sprint, owner, trace, points, priority, wtype)
EPICS = {  # epic name: abbr
 "PMO & Governance":"GOV","Engagement Setup":"S0","Onboarding & Enablement":"ONB","Workshops":"WS",
 "Documentation":"DOC","Training & Knowledge Transfer":"KT","Testing & Quality":"QA","Go-Live & Cutover":"GL","Hypercare & Closeout":"CO"}
STORIES=[]
def add(epic,short,role,want,benefit,ac,sprint,owner,trace,points=3,priority="3 - Moderate",wtype="Delivery"):
    STORIES.append(dict(epic=epic,short=short,role=role,want=want,benefit=benefit,ac=ac,sprint=sprint,owner=owner,trace=trace,points=points,priority=priority,wtype=wtype))

# ---------------- PMO & Governance ----------------
e="PMO & Governance"
add(e,"Issue the weekly status report","Engagement Manager","a weekly status report issued to the Sponsor and PM","leadership sees progress, risks, and decisions every week",
 ["Given the cadence, When each Friday arrives, Then a status report is issued with RAG by workstream, accomplishments, risks, and decisions needed.","Given a Yellow/Red status, When reported, Then a Monday 1:1 and mitigation are triggered.","Given the report, When produced, Then it uses the approved template and is stored in 02_Delivery."],
 "All sprints","Engagement Manager","Connection_Weekly_Status_Report_TEMPLATE.docx")
add(e,"Maintain the Executive Health Dashboard","Engagement Manager","the one-page exec health dashboard kept current","Sponsor and ECS leadership review health in real time",
 ["Given the review cadence, When a steering/sponsor review occurs, Then the dashboard reflects current RAG, KPIs, and top risks/decisions.","Given the 6 health vectors, When updated, Then each reflects the latest signal.","Given the dashboard, When shared, Then it is client-safe and current."],
 "All sprints","Engagement Manager","Connection_Executive_Health_Dashboard.pptx")
add(e,"Operate the Governance Triage Log / RAID","Engagement Manager","the triage log and RAID kept current","every deviation and risk is transparent to both teams",
 ["Given a deviation request, When raised, Then it is logged within 24 hours with disposition.","Given the customization cap, When approached, Then the count and remaining-before-PCR are visible.","Given RAID items, When reviewed weekly, Then material items surface in the status report."],
 "All sprints","Engagement Manager","Connection_Governance_Triage_and_RAID.xlsx")
add(e,"Run the Customization Council","Engagement Manager","the weekly Customization Council operated","OOTB discipline is enforced and deviations are governed",
 ["Given pending requests, When the weekly slot arrives, Then the Council reviews each with an impact assessment and records the two-key decision.","Given no requests, When the slot arrives, Then the meeting is canceled.","Given a decision, When made, Then it is logged in the Triage Log within 24 hours."],
 "All sprints","Engagement Manager","Engagement Delivery Guidelines")
add(e,"Maintain the Baseline Risk Register","Engagement Manager","a current risk register maintained","risks are visible and actively managed",
 ["Given Sprint 0, When set up, Then the register is initialized with known risks, owners, and mitigations.","Given a new risk, When identified, Then it is added with severity and owner.","Given the register, When reviewed, Then it informs the status report and dashboard."],
 "Sprint 0","Engagement Manager","Connection_Governance_Triage_and_RAID.xlsx (RAID)",2)
add(e,"Run bi-weekly Sponsor syncs","Engagement Manager","bi-weekly Sponsor syncs run with agenda and notes","the Sponsor stays aligned and sentiment is tracked",
 ["Given the cadence, When each sync occurs, Then an agenda is shared and decisions/notes are captured.","Given a concern, When raised, Then it is logged and actioned.","Given sentiment, When assessed, Then it feeds the health dashboard."],
 "All sprints","Engagement Manager","Sponsor Sync (trust-but-verify)",2)
add(e,"Run monthly Steering reviews","Engagement Manager","monthly steering reviews run with leadership","leadership reviews outcomes, KPIs, and roadmap",
 ["Given the monthly cadence, When a review occurs, Then outcomes, KPIs, and the roadmap are presented.","Given a decision, When made, Then it is recorded.","Given the review, When complete, Then actions are tracked."],
 "Monthly","Engagement Manager","Executive Health Dashboard",2)
add(e,"Report trust-but-verify health to practice management","Engagement Manager","weekly engagement-health metrics reported to ECS practice management","practice leadership supports early without micromanaging",
 ["Given Friday COB, When metrics are sent, Then velocity, customization count, and dependency slips are reported with RAG.","Given Yellow/Red, When reported, Then a Monday 1:1 plans the response.","Given the report, When produced, Then it uses the trust-but-verify model."],
 "All sprints","Engagement Manager","Engagement Delivery Guidelines",2)

# ---------------- Engagement Setup ----------------
e="Engagement Setup"
add(e,"Run the internal ECS kickoff and assign consultants","Engagement Manager","an internal ECS kickoff held and the team assigned","the delivery team is aligned and ready before customer kickoff",
 ["Given the SOW, When the internal kickoff runs, Then scope is reviewed and roles/decision-rights are confirmed.","Given the team, When assigned, Then each role and reading path is set (per onboarding).","Given tooling, When loaded, Then backlog and templates are ready."],
 "Sprint 0","Engagement Manager","Connection_Team_Onboarding_and_Vision.docx",2)
add(e,"Run the customer kickoff meeting","Engagement Manager","the joint customer kickoff delivered","Connection and ECS start aligned on goals, journey, and roles",
 ["Given the kickoff deck, When delivered, Then the 18-week journey, scope, roles, and governance are walked through.","Given stakeholders, When present, Then questions are addressed and next steps agreed.","Given the meeting, When complete, Then notes and actions are recorded."],
 "Sprint 0","Engagement Manager","Connection_Kickoff_Deck.pptx",2)
add(e,"Run the governance & decision-rights workshop and sign the Council charter","Engagement Manager","the governance workshop run and the Customization Council charter signed","decision rights and the operating model are agreed before build",
 ["Given the workshop, When run, Then decision rights, RACI, and escalation are agreed.","Given the charter, When signed, Then the Council quorum, cadence, and two-key model are in effect.","Given outputs, When recorded, Then they are stored and referenced."],
 "Sprint 0","Engagement Manager","Customer_Governance_Charter.docx",3,"2 - High")
add(e,"Establish the communication plan and cadence","Engagement Manager","the communication plan and meeting cadence established","everyone knows when and how the engagement communicates",
 ["Given Sprint 0, When set, Then weekly status, bi-weekly sponsor sync, and sprint demos are scheduled.","Given the plan, When shared, Then audiences and channels are clear.","Given cadence, When live, Then invites are issued."],
 "Sprint 0","Engagement Manager","Communication plan",1)
add(e,"Distribute the Foundation Data Workbooks","Process Consultant","the accelerator-pack data workbooks distributed to Connection","customer data collection starts early to enable demos",
 ["Given Sprint 0, When distributed, Then the Foundation and in-scope packs are handed to the right owners.","Given the workbooks, When issued, Then due dates and instructions are clear.","Given collection, When underway, Then progress is tracked in the onboarding checklist."],
 "Sprint 0","Process Consultant","02_Delivery/Accelerator_Packs/",2)
add(e,"Confirm environments provisioned and access granted","Solution Architect","sub-prod/prod environments and ECS access confirmed","the team can build from Sprint 1",
 ["Given provisioning, When complete, Then sub-prod and prod exist with ECS admin access.","Given credentials, When set, Then they are vaulted and least-privilege.","Given readiness, When validated, Then it is checked off in the readiness tracker."],
 "Sprint 0","Solution Architect","Onboarding Checklist",2)
add(e,"Complete stakeholder and SME mapping","Engagement Manager","stakeholder and SME mapping completed","the right people are engaged per process area",
 ["Given the org, When mapped, Then SMEs, decision owners, and change champions are named per area.","Given gaps, When found, Then they are escalated to the Sponsor.","Given the map, When complete, Then it informs workshop scheduling."],
 "Sprint 0","Engagement Manager","Stakeholder Mapping",1)
add(e,"Pass the Sprint 0 readiness gate","Engagement Manager","the Sprint 0 readiness validation completed","build does not start until dependencies are met",
 ["Given the readiness checklist, When validated, Then env, access, governance, data pack, and risks are confirmed.","Given an unmet item, When found, Then a dependency-slip conversation occurs with the Sponsor.","Given the gate, When passed, Then the Sprint 0 Complete milestone is set."],
 "Sprint 0","Engagement Manager","Connection_Onboarding_Checklist.xlsx",3,"2 - High")

# ---------------- Onboarding & Enablement ----------------
e="Onboarding & Enablement"
add(e,"Deliver the internal team onboarding package","Engagement Manager","the ECS team onboarded via the vision/guidelines/role materials","the team absorbs the approach by role and starts aligned",
 ["Given the onboarding set, When delivered, Then each consultant has read their role path.","Given the vision, When shared, Then the OOTB-first discipline and curate-don't-copy principle are understood.","Given onboarding, When complete, Then the team can execute the delivery guidelines."],
 "Sprint 0","Engagement Manager","01_Onboarding/Internal_Team/",2)
add(e,"Deliver the client onboarding package","Process Consultant","Connection onboarded via the client guide and kickoff","the client knows what to expect and their accountabilities",
 ["Given the client guide + deck, When delivered, Then roles, journey, governance, and checks are clear to Connection.","Given the Sponsor/PM, When onboarded, Then their accountabilities are confirmed.","Given onboarding, When complete, Then the client is ready for Sprint 0."],
 "Sprint 0","Process Consultant","01_Onboarding/Client_Facing/",2)

# ---------------- Workshops ----------------
e="Workshops"
def wstory(area,sprint,mods):
    add(e,f"Facilitate and sign off the {area} workshop(s)","Process Consultant",f"the {area} workshop(s) facilitated to signed-off decisions",f"the {area} configuration stories are unblocked with agreed decisions",
     [f"Given the pre-read and demo, When the {area} workshop runs, Then each in-scope decision is made in the room.",
      "Given a decision, When made, Then it is signed off by the named process owner and captured.",
      "Given a deviation, When raised, Then it is routed to the Triage Log; the workshop ends with signed-off stories (not a 'to think about' list)."],
     sprint,"Process Consultant",f"Connection_{mods}_Workshop.pptx + Scope Notes",2,"2 - High","Workshop")
wstory("Platform Foundation","Sprint 1","Platform_Foundation")
wstory("CSDM","Sprint 1","CSDM")
wstory("CMDB & Discovery","Sprint 2","CMDB")
wstory("Incident, Problem & Major Incident","Sprint 3","Incident")
wstory("Change","Sprint 4","Change")
wstory("Service Catalog","Sprint 4","Service_Catalog")
wstory("Integrations & Service Graph Connectors","Sprint 3","Integrations")
wstory("Vonage CTI & Interactions","Sprint 4","Interactions_Vonage_CTI")
wstory("Knowledge","Sprint 5","Knowledge")
wstory("Employee Center & Virtual Agent","Sprint 5","Employee_Center")
wstory("Predictive Intelligence","Sprint 5","Predictive_Intelligence")
wstory("HAM","Sprint 6","HAM")
wstory("Performance Analytics","Sprint 6","Performance_Analytics")

# ---------------- Documentation ----------------
e="Documentation"
add(e,"Produce the Platform Architecture & CSDM Alignment Document","Solution Architect","the Month 1 architecture & CSDM alignment document produced and signed off","the data foundation is documented and accepted before Month 2 build",
 ["Given the CSDM/CMDB workshop decisions, When drafted, Then the doc covers topology, CSDM alignment, CI classes/relationships, sources, and risk-scoring readiness.","Given the draft, When reviewed, Then the Technical Lead and Sponsor sign off.","Given the doc, When complete, Then it is built from the brand template and stored."],
 "Sprint 2","Solution Architect","Connection_Platform_Architecture_and_CSDM_Alignment.docx",5,"2 - High","Documentation")
add(e,"Produce Sprint 1-2 Design Documentation","Solution Architect","the Sprint 1-2 design documentation produced (workbooks updated with decisions)","Month 1 decisions are captured and traceable",
 ["Given the Stage 1 workshops, When documented, Then the design workbooks reflect the agreed decisions.","Given the docs, When reviewed, Then they are accepted by the Product Owner.","Given the Triage Log, When current, Then deviations are reflected."],
 "Sprint 2","Solution Architect","03_Shared/04_Sprint_Workbooks (Connection copies)",3,"3 - Moderate","Documentation")
add(e,"Produce Sprint 3-4 Design Documentation","Process Consultant","the Sprint 3-4 design documentation produced","Month 2 decisions are captured and traceable",
 ["Given the Stage 2 workshops, When documented, Then the design workbooks reflect the agreed decisions.","Given the docs, When reviewed, Then they are accepted by the Product Owner.","Given the Triage Log, When current, Then deviations are reflected."],
 "Sprint 4","Process Consultant","Sprint Workbooks",3,"3 - Moderate","Documentation")
add(e,"Produce Month 3 Design Documentation","Process Consultant","the Month 3 design documentation produced","late-build decisions (EX, HAM, PA) are captured",
 ["Given the Stage 2-3 workshops, When documented, Then EX/HAM/PA decisions are recorded.","Given the docs, When reviewed, Then they are accepted.","Given the set, When complete, Then it joins the KT Package."],
 "Sprint 6","Process Consultant","Sprint Workbooks",2,"3 - Moderate","Documentation")
add(e,"Produce the Governance Charter Package","Engagement Manager","the governance charter package produced (decision rights, council charter, RACI)","the operating model is documented and agreed",
 ["Given Sprint 0, When produced, Then the charter, decision-rights, and RACI are delivered.","Given the package, When reviewed, Then ECS and the Sponsor agree it.","Given the docs, When complete, Then they are stored and referenced."],
 "Sprint 0","Engagement Manager","Customer_Governance_Charter.docx + Role Quick-Ref",2,"2 - High","Documentation")
add(e,"Maintain the SOW Deliverables Matrix","Engagement Manager","the SOW deliverables matrix kept current","leadership tracks every committed deliverable and its status",
 ["Given the 27 SOW deliverables, When tracked, Then each shows status (Ready/Adapt/Gap/Complete), owner, and sprint.","Given a deliverable completion, When recorded, Then its status updates.","Given the matrix, When reviewed, Then it reconciles to the project plan."],
 "All sprints","Engagement Manager","Connection_SOW_Deliverables_Matrix.xlsx",2,"3 - Moderate","Documentation")
add(e,"Produce and maintain the configuration story backlog","Solution Architect","the configuration user-story backlog maintained in SN Agile","development is tracked story-by-story with traceability",
 ["Given the 141 stories, When imported, Then epics and stories exist in SN Agile with acceptance criteria and DoD.","Given a sprint, When planned, Then stories are estimated and assigned.","Given progress, When tracked, Then the backlog reflects state."],
 "All sprints","Solution Architect","Connection_User_Stories_SN_Agile.xlsx",3,"2 - High","Documentation")

# ---------------- Testing & Quality ----------------
e="Testing & Quality"
add(e,"Produce the UAT end-to-end test scripts","QA / UAT Lead","the end-to-end UAT scripts produced with story traceability","UAT is contained, managed, and tied back to the stories",
 ["Given the stories, When authored, Then scripts are grouped into end-to-end suites with story-ID traceability.","Given coverage, When checked, Then every story is covered E2E or flagged sprint-test-only.","Given the scripts, When complete, Then they are ready for tester assignment."],
 "Sprint 6","QA / UAT Lead","Connection_UAT_End_to_End_Test_Scripts.xlsx",3,"2 - High","Testing")
add(e,"Produce the UAT Guidebook for end users","Process Consultant","the UAT guidebook produced for first-time testers","end users know how to test, log defects, and what good looks like",
 ["Given the suites, When documented, Then the guidebook explains UAT, roles, how to run a script, and how to log a defect.","Given a tester, When prepared, Then they can execute without prior experience.","Given the guidebook, When delivered, Then it accompanies tester onboarding."],
 "Sprint 6","Process Consultant","Connection_UAT_Guidebook_for_End_Users.docx",2,"3 - Moderate","Testing")
add(e,"Coordinate UAT execution","QA / UAT Lead","UAT execution coordinated across testers and suites","UAT completes with results recorded and defects logged",
 ["Given assigned scripts, When UAT runs, Then testers record PASS/FAIL/BLOCKED/SKIP per script.","Given a daily standup, When held, Then progress and blockers are tracked.","Given completion, When reached, Then results roll up for go/no-go."],
 "Sprint 7","QA / UAT Lead","UAT Test Scripts",3,"2 - High","Testing")
add(e,"Triage and resolve UAT defects","Solution Architect","UAT defects triaged and resolved","P1/P2 defects are cleared (or planned) before go-live",
 ["Given a logged defect, When triaged, Then severity and owner are set.","Given a fix, When deployed, Then the tester re-tests and confirms.","Given go-live, When approaching, Then no open P1/P2 defects remain without a plan."],
 "Sprint 7","Solution Architect","Connection_UAT_End_to_End_Test_Scripts.xlsx (Defect Log)",3,"2 - High","Testing")
add(e,"Execute System Integration Testing (SIT)","Technical Consultant","SIT executed across integrations end-to-end","integration touchpoints work before UAT/go-live",
 ["Given the integrations, When SIT runs, Then AD/SSO, SCCM, Intune, email, and CTI are validated in sub-prod.","Given a failure, When found, Then it is logged and fixed.","Given SIT, When complete, Then results inform UAT readiness."],
 "Sprint 6","Technical Consultant","Integration packs",3,"2 - High","Testing")

# ---------------- Training & Knowledge Transfer ----------------
e="Training & Knowledge Transfer"
add(e,"Deliver Admin Knowledge Transfer (4 sessions)","Solution Architect","the 4 admin KT sessions delivered","Connection's platform team can administer OOTB and stay upgrade-safe",
 ["Given the KT plan, When delivered, Then 4 sessions cover admin, update sets, and OOTB governance.","Given attendees, When trained, Then they can perform core admin tasks.","Given the sessions, When complete, Then the Admin Guide is handed over."],
 "Sprint 7","Solution Architect","Connection_Administrator_Guide_and_KT.docx",3,"2 - High","Training")
add(e,"Deliver Train-the-Trainer (2 per process area)","Process Consultant","two train-the-trainer sessions per in-scope process area delivered","Connection trainers can deliver end-user training",
 ["Given the toolkit, When delivered, Then each area gets 2 sessions (demo + teach-back).","Given trainers, When enabled, Then they can run end-user training.","Given the sessions, When complete, Then the quick-reference outline is handed over."],
 "Sprint 7","Process Consultant","Connection_Train_the_Trainer_Toolkit.docx",3,"2 - High","Training")
add(e,"Assemble the Knowledge Transfer Package","Solution Architect","the KT Package assembled for handover","Connection receives a complete administration/enablement set at go-live",
 ["Given the components, When assembled, Then the Admin Guide, train-the-trainer materials, and sprint workbook set are bundled.","Given the package, When reviewed, Then it is complete per the SOW.","Given handover, When done, Then KT Certification is issued."],
 "Sprint 7","Solution Architect","KT Package (SOW Sec 11)",2,"2 - High","Training")

# ---------------- Go-Live & Cutover ----------------
e="Go-Live & Cutover"
add(e,"Produce the Go-Live Checklist","Engagement Manager","the Connection go-live checklist produced","go-live readiness is verifiable and signed off",
 ["Given the library checklist, When tailored, Then it reflects Connection's cutover scope.","Given readiness, When assessed, Then each item is confirmed.","Given the checklist, When complete, Then it supports the go/no-go."],
 "Sprint 7","Engagement Manager","lib CLT-CO-02_Go_Live_Checklist.docx",2,"2 - High","Go-Live")
add(e,"Produce the Cutover Runbook","Solution Architect","the cutover runbook produced","the production cutover is sequenced and low-risk",
 ["Given the cutover plan, When documented, Then steps, owners, timings, and rollback are defined.","Given the runbook, When reviewed, Then it is accepted by the Technical Lead.","Given cutover, When executed, Then the runbook is followed."],
 "Sprint 7","Solution Architect","Cutover Runbook (new)",3,"2 - High","Go-Live")
add(e,"Obtain Go-Live Readiness Sign-Off","Engagement Manager","go-live readiness signed off by Sponsor and Product Owner","go-live proceeds only with explicit authorization",
 ["Given UAT results and open defects, When reviewed, Then a go/no-go recommendation is made.","Given the review, When held, Then the Sponsor and Product Owner sign off.","Given sign-off, When obtained, Then it is recorded."],
 "Sprint 7","Engagement Manager","Go-Live Readiness Sign-Off",2,"1 - Critical","Go-Live")
add(e,"Execute the governed production cutover","Solution Architect","the governed cutover to production executed","Connection goes live on the new instance (Week 16)",
 ["Given the runbook, When executed, Then in-scope capabilities are live and verified in production.","Given verification, When complete, Then a clean exit from the legacy environment is confirmed.","Given go-live, When done, Then Hypercare begins."],
 "Sprint 7","Solution Architect","Project Plan (Stage 3)",5,"1 - Critical","Go-Live")

# ---------------- Hypercare & Closeout ----------------
e="Hypercare & Closeout"
add(e,"Provide 2-week Hypercare support","Engagement Manager","2 weeks of post-go-live Hypercare provided","production stabilizes with ECS L2+ escalation support",
 ["Given go-live, When Hypercare runs, Then daily standups (Week 1) step down to twice-weekly (Week 2).","Given a P1/P2 production issue, When raised, Then ECS provides L2+ support in business hours.","Given Hypercare, When closing, Then an exit-criteria review is held."],
 "Sprint 8","Engagement Manager","lib CLT-CO-03 Hypercare Support Model",3,"2 - High","Hypercare")
add(e,"Produce the Hypercare Exit Report","Engagement Manager","the Hypercare exit report produced","handover to steady-state operations is formal and clean",
 ["Given the Hypercare window, When closing, Then the exit report summarizes incidents, fixes, and stability.","Given exit criteria, When met, Then handover to operations is approved.","Given the report, When complete, Then it is delivered to Connection."],
 "Sprint 8","Engagement Manager","lib CLT-CO-06 Hypercare Exit Report",2,"3 - Moderate","Hypercare")
add(e,"Produce the Operational Handoff Pack","Engagement Manager","the operational handoff pack produced","Connection owns ongoing operations with a clear support model",
 ["Given the operating model, When documented, Then the ownership matrix, support model, and escalation contacts are defined.","Given the pack, When reviewed, Then Connection's team accepts ownership.","Given handover, When done, Then the pack is delivered."],
 "Sprint 8","Engagement Manager","Operational Handoff Pack",2,"2 - High","Closeout")
add(e,"Produce Lessons Learned & Project Closeout","Engagement Manager","the lessons learned and closeout report produced","the engagement closes with documented outcomes and learning",
 ["Given the engagement, When closing, Then final KPIs, OOTB wins, and lessons learned are captured.","Given the report, When reviewed, Then it is accepted by the Sponsor.","Given closeout, When done, Then artifacts are archived."],
 "Sprint 8","Engagement Manager","lib CLT-CO-01 Closeout Summary + Lessons Learned",2,"3 - Moderate","Closeout")
add(e,"Produce the 12-month strategic roadmap","Solution Architect","a 12-month roadmap produced beyond Phase 1","Connection has a clear path to Phases 2-4 (UX, ITOM, AI)",
 ["Given Phase 1 outcomes, When planned, Then the roadmap outlines Phase 2-4 priorities.","Given the roadmap, When reviewed, Then leadership aligns on the vision.","Given closeout, When done, Then the roadmap is delivered."],
 "Sprint 8","Solution Architect","12-month roadmap",2,"3 - Moderate","Closeout")
