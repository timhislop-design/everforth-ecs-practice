import sys, os
REPO="/sessions/eager-epic-davinci/mnt/everforth-ecs-practice"
sys.path.insert(0, os.path.join(REPO,"03_Shared","00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta
LOGO=os.path.join(REPO,"00_Master_Blueprint","assets","everforth_logo.png")
CONF="ECS Federal - ServiceNow Practice - Confidential"
OUT=os.path.join(REPO,"05_Clients","Connection","02_Delivery","Connection_Cutover_Runbook.docx")
d=EcsDocument(meta=DocMeta(eyebrow="CLIENT DELIVERABLE - CUTOVER RUNBOOK",
 title="Connection ServiceNow\nGo-Live Cutover Runbook",
 subtitle="The sequenced, owned, reversible plan to move Connection to production - Week 16",
 org="ECS Federal - ServiceNow Practice",
 audience="Connection Technical Lead & Platform Team; ECS Delivery",
 companion_to="Go-Live Readiness Checklist - Customer Dependency Tracker - Operational Handoff Pack",
 doc_id="DEL-CONN-CUT-01", version="1.0 (template)", status="Template",
 confidentiality=CONF, running_header_label="Connection - Cutover Runbook", footer_left=CONF), logo_path=LOGO)
d.add_cover_page(); d.page_break()

d.h1("How to Use This Runbook", numbered=False)
d.para("This runbook governs the production cutover at Go-Live (Week 16). It is sequenced, every step has an owner and a time, and it includes a rollback plan. Fill the [bracketed] specifics during cutover planning (Sprint 7). Do not start cutover until the Go-Live Readiness Checklist clears its blocking gates and the Sponsor authorizes.")
d.callout("Golden rule: no step proceeds without its predecessor validated. If validation fails and cannot be resolved in the window, invoke the Rollback Plan (Section 6).")

d.h1("Cutover Overview", numbered=True)
d.table(headers=["Item","Detail"], rows=[
 ["Cutover window","[Date / time], [duration] - low-traffic window agreed with Connection"],
 ["Change freeze","Configuration freeze from [T-2 days]; only cutover changes permitted"],
 ["Go/No-Go gate","Readiness Checklist blocking gates Met + Sponsor authorization"],
 ["Cutover lead","ECS Solution Architect; Connection Technical Lead co-lead"],
 ["Rollback decision","ECS EM + Connection Sponsor (see Section 6)"],
 ["Comms owner","ECS Engagement Manager + Connection PM"],
])

d.h1("Pre-Cutover Checklist (T-minus)", numbered=True)
d.table(headers=["When","Activity","Owner","Done"], rows=[
 ["T-5 days","Go-Live Readiness Checklist blocking gates confirmed Met","EM","[ ]"],
 ["T-2 days","Configuration freeze in effect; final update sets identified and ordered","SA","[ ]"],
 ["T-2 days","Production clone/backup taken (rollback point)","Tech Lead","[ ]"],
 ["T-1 day","Cutover comms sent to stakeholders and end users","EM + PM","[ ]"],
 ["T-1 day","Cutover team confirmed and on standby with the schedule","SA","[ ]"],
 ["T-0","Final go/no-go held; Sponsor authorizes","EM + Sponsor","[ ]"],
])

d.h1("Cutover Sequence", numbered=True)
d.para("Execute in order. Each step records start/end time and a pass/fail validation before proceeding.")
d.table(headers=["#","Step","Owner","Validation"], rows=[
 ["1","Final data sync/load (delta from sub-prod); confirm Foundation + CMDB data current","Tech Consultant","Record counts match; no load errors"],
 ["2","Promote final update sets in order (dev -> test -> prod); resolve any preview conflicts","Solution Architect","All sets committed; no skipped records unresolved"],
 ["3","Re-point integrations to production: AD/SSO, SCCM, Intune, email","Integration Engineer","Each integration test passes against prod"],
 ["4","Cut over Vonage CTI: re-point OpenFrame/connector to the production Vonage tenant","CTI Engineer","Test inbound call -> Interaction -> Incident in prod"],
 ["5","Run scheduled jobs / first Discovery + connector imports; verify CMDB populates","Tech Consultant","Sample CIs present; CMDB Health at baseline"],
 ["6","Enable user access (SSO, roles via AD groups); confirm agent and EC access","Solution Architect","Sample users in each role can log in and work"],
 ["7","Publish Employee Center; enable Virtual Agent and Knowledge","Process Consultant","EC live; VA responds; KB searchable"],
 ["8","Final smoke tests (Section 5)","UAT Lead","All smoke tests pass"],
])

d.h1("Validation & Smoke Tests", numbered=True)
d.para("Run a fast subset of the UAT end-to-end suites against production to confirm the platform works before declaring go-live:")
d.bullet("Incident: create via Employee Center and via phone (Vonage) - both reach an agent and resolve.")
d.bullet("Request: order a catalog item, approve, and confirm fulfillment routing.")
d.bullet("Change: raise a change tied to a CI; confirm risk scoring and CAB routing.")
d.bullet("Self-service: Employee Center search, Virtual Agent, and knowledge return results.")
d.bullet("Identity: SSO login and role-based access for a sample of each role.")
d.bullet("Integrations: confirm AD/SSO, SCCM/Intune CI data, email, and CTI in production.")
d.callout("If any smoke test fails and cannot be resolved within the window, escalate to the rollback decision (Section 6).")

d.h1("Rollback Plan", numbered=True)
d.para("Rollback returns Connection to the prior state if cutover cannot complete successfully within the window.")
d.h2("Rollback triggers")
d.bullet("A blocking step fails validation and cannot be resolved within the cutover window.")
d.bullet("A critical integration (SSO, CTI, or CMDB data) cannot be made functional in production.")
d.bullet("A P1 issue with no workaround is found during smoke testing.")
d.h2("Rollback decision and steps")
d.bullet("Decision authority: ECS Engagement Manager + Connection Executive Sponsor.")
d.bullet("1. Halt the cutover sequence; freeze further changes.")
d.bullet("2. Restore from the production clone/backup taken at T-2 days (or revert promoted update sets).")
d.bullet("3. Re-point integrations to their prior endpoints.")
d.bullet("4. Confirm the prior state is functional; notify stakeholders of the rollback and the revised plan.")
d.bullet("5. Hold a rapid retro; agree corrective actions and a new cutover date.")

d.h1("Communications Plan", numbered=True)
d.table(headers=["Timing","Message","Audience","Owner"], rows=[
 ["T-1 day","Cutover window, expected impact, where to get help","All users + stakeholders","EM + PM"],
 ["Cutover start","Cutover has begun; system unavailable [if applicable]","Stakeholders","PM"],
 ["Go-live confirmed","Platform is live; how to access; support channels","All users","EM + PM"],
 ["If rollback","Rollback invoked; prior system remains; revised date","Stakeholders","EM + Sponsor"],
])

d.h1("Go / No-Go Decision", numbered=True)
d.para("The final go/no-go is held at T-0. GO requires: all Go-Live Readiness Checklist blocking gates Met, the pre-cutover checklist complete, and explicit authorization from the Connection Executive Sponsor and Product Owner. Any unmet blocking gate is a NO-GO unless the Sponsor accepts a documented risk with a mitigation.")

d.h1("Post-Cutover & Hypercare Handoff", numbered=True)
d.bullet("Confirm go-live in the status report and Executive Health Dashboard.")
d.bullet("Open the Hypercare window: daily standups (Week 1), ECS L2+ escalation support.")
d.bullet("Monitor platform health, scheduled jobs, and early-life incidents against the baseline.")
d.bullet("Hand over per the Operational Handoff Pack at Hypercare exit.")
d.callout("Cutover is not 'done' at go-live - it is done when Hypercare exit criteria are met and steady-state ownership is accepted.")

d.save(OUT); print("Saved cutover")
