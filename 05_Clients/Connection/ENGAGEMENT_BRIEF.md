# Engagement Brief — Connection — Delivery Onboarding

> Active execution engagement (`05_Clients/`). This brief is the single source of truth for the Connection engagement and grows as delivery proceeds.

---

## Engagement Identity

| Field | Value |
|---|---|
| Client | Connection |
| Engagement Type | Active delivery (won work) |
| Current Phase | Onboarding |
| Short Title | Delivery Onboarding |
| Start Date | 2026-06-09 |
| Contract / Vehicle | Phase 1 fixed-scope SOW — ROM $350,000 |
| Document | SOW v2.0 (DOC0004841), dated 2026-06-03 |
| Primary Client Contact | Neveena (Connection Project Manager) — primary recipient for all document releases; distributes internally per each drop email's distribution section |
| Internal Lead | Timothy Hislop |
| Delivery Team | TBD |

---

## Scope Summary

Connection (PC Connection) is exiting a domain-separated shared ServiceNow instance and standing up a modern, **AI-ready** platform under an **OOTB-First** delivery discipline. **Phase 1 is an 18-week reimplementation** (16 weeks build + 2 weeks Hypercare; ROM **$350,000**) focused on ITSM Core, a CSDM-aligned CMDB, and a modern Employee Center — establishing the architectural foundation for later AI capabilities (Now Assist, Agentic Agents, Predictive Intelligence, Workflow Data Fabric). Authoritative source: **SOW v2.0 (2026-06-03)** in `00_Source_Inputs/`, which also serves as the Project Charter.

Our **first work product** is the **delivery onboarding package** — making this engagement digestible by role for the ECS team and right-sized for the client, with simple checks-and-balances for leadership.

---

## In-Scope Applications & Modules (per SOW v2)

- **ITSM Core** — Incident, Request, Knowledge, Problem, Major Incident; Change incl. CAB Workbench + [2–3] standard changes; **Service Operations Workspace**.
- **Service Catalog** — top [10–15] highest-impact catalog items; [2–3] generic catch-all request items.
- **Employee Experience** — Employee Center (Connection branding); **Virtual Agent** (5 baseline topics); **AI Search**; **Knowledge Management** (taxonomy, structure, ported articles).
- **Platform Baselines** — Subscription Management; Security Center; **Predictive Intelligence** + Task Intelligence; **Platform Analytics**, Data Visualization, Benchmarks.
- **CMDB & CSDM** — foundational CSDM alignment; CI relationship standards; Service Graph Connectors (SCCM, Intune); Discovery (leverage existing where clean).
- **HAM** — enable Stockrooms + foundational HAM config for CSDM alignment (pre-Phase 2).
- **Integrations** — AD/SSO, MS SCCM, Intune, Vonage (leverage existing where best-practice-aligned).

> **Out of scope / later phases:** Phase 2 (baseline expansion + UX), Phase 3 (ITOM + Intelligence), Phase 4+ (full AI realization). Anything not listed above is out of Phase 1 scope.

---

## Constraints & Guardrails (must live by)

- **OOTB-First** — every build starts from a demo of OOTB functionality; customization is the exception, not the default.
- **Rule of Three** — if a requirement can't be met by (1) Configuration, (2) UI Policy, or (3) Flow Designer, it's a Customization → separate technical review + impact assessment + **Project Sponsor sign-off** before any work.
- **Deviation threshold** — a delta from OOTB is acceptable only when (a) tied to a documented business outcome, (b) not achievable via OOTB configuration, and (c) signed off by the Project Sponsor. ECS presents the OOTB alternative every time first.
- **Definition of Done** — acceptance criteria approved by the Product Owner *before* build; all criteria met + approved at close.
- **MVP mindset** + **Upgradeability Scorecard** + **Low-Code/No-Code governance** applied throughout.
- **PCR process** governs all scope/schedule changes; a Governance Triage Log tracks intake.
- **Agile, 2-week sprints**, workshop-led; customer data in the system early to enable demos.
- Success measured via Platform Analytics: **MTTR, SLA attainment, change success rate**.

---

## Engagement Deliverables (per SOW cadence)

- **Sprint 0 (Wks 1–2):** kickoff & SOW review, governance setup, accelerator-pack data collection, backlog triage, roles/acceptance criteria.
- **Month 1 (Wks 3–6):** CSDM data model, greenfield basics (SSO/AD/roles/SLAs), Foundation data imports, Discovery + SCCM/Intune Service Graph kickoff.
- **Month 2 (Wks 7–10):** ITSM Core (INC/PRB/CHG/REQ) in SO Workspace, CI-driven change risk scoring, CAB Workbench.
- **Month 3 (Wks 11–14):** Employee Center, Virtual Agent + AI Search, KM, Predictive Intelligence, HAM foundations, Performance Analytics.
- **Go-Live (Wks 15–16):** SIT, UAT cycles, training/KT, governed cutover. Deliverables: UAT/SIT Report, Go-Live Checklist, Cutover Runbook.
- **Hypercare/Close (Wks 17–18):** stabilization, formal closeout, Lessons Learned, KT library/SOPs/Admin 101, 12-month roadmap.

---

## Onboarding Package — Deliverables

| File | Audience | Location | Type | Status | Notes |
|---|---|---|---|---|---|
| `Connection_Client_Onboarding_Guide.docx` | Connection | `01_Onboarding/Client_Facing/` | docx | **Draft v1.0** | Built via EcsDocument. What to expect, 18-wk journey, roles/accountability, governance & checks. Confidential footer. Name placeholders. |
| `Connection_Kickoff_Deck.pptx` | Joint | `01_Onboarding/Client_Facing/` | pptx | **Draft v1.0** | 12 slides via pptx_brand.js. Built from the guide + SOW + sales deck. |
| `Connection_Team_Onboarding_and_Vision.docx` | ECS team | `01_Onboarding/Internal_Team/` | docx | **Draft v1.0** | Vision/why, engagement at a glance, OOTB discipline, curate-don't-copy, role reading paths |
| `Connection_Engagement_Delivery_Guidelines.docx` | ECS team | `01_Onboarding/Internal_Team/` | docx | **Draft v1.0** | Rule of Three, deviation path, Customization Council, DoD, trust-but-verify, client do's & don'ts |
| `Connection_Role_and_Accountability_QuickRef.docx` | ECS team | `01_Onboarding/Internal_Team/` | docx | **Draft v1.0** | Decision-rights table + one section per role (own / read / heaviest sprints) |
| `Connection_Workshop_Facilitation_Guide.docx` | ECS team | `01_Onboarding/Internal_Team/` | docx | **Draft v1.0** | 5-tier framework, six-beat pattern, decision-forcing techniques, scripted rebuttals, sign-off discipline |
| `Connection_Onboarding_Checklist.xlsx` | Both | `01_Onboarding/` | xlsx | **Draft v1.0** | 19 Sprint 0 readiness tasks (ECS/Connection/Joint); status dropdown, conditional formatting, live summary |
| `Connection_Communication_Plan.docx` | Connection | `01_Onboarding/Client_Facing/` | docx | **Draft v1.0** | Built via EcsDocument (CLT-CONN-ONB-02). Full comms cadence (Sprints 0–8 / 4 stages), roles & responsibilities, escalation path, contact roster. Adapted from library CLT-S0-06. Confidential footer. Name placeholders. |
| `Connection_Document_Roadmap.docx` | Connection | `01_Onboarding/Client_Facing/` | docx | **Draft v1.0** | Built via EcsDocument (CLT-CONN-ONB-03). The five-drop JIT rollout at a glance — ships in Drop 1. |

> **Onboarding package complete.** Client-facing: onboarding guide, kickoff deck, governance charter. Internal: vision guide, delivery guidelines, role quick-ref, workshop facilitation guide. Plus the shared onboarding tracker. Remaining: fill name placeholders; set project-plan start date.

---

## Delivery Artifacts (`02_Delivery/`) — generic, reusable

Consolidated from existing 00–03 base components (per-sprint briefs, trust-but-verify dashboard INT-TBV-02/03, demo scripts), made Connection-specific and lean.

| File | Audience | Type | Status | Notes |
|---|---|---|---|---|
| `Connection_18Week_Project_Plan.xlsx` | Shared | xlsx | Active | Sprints 0–8 / 4 stages; set start date (B3) |
| `Connection_Weekly_Status_Report_TEMPLATE.docx` | Client-facing | docx | Template v1.0 | EM→Sponsor weekly; RAG by workstream, metrics snapshot. Confidential footer |
| `Connection_Executive_Health_Dashboard.pptx` | Client-safe | pptx | Template v1.0 | One-page; 6-vector health model, KPI trend, schedule, risks/decisions |
| `Connection_Governance_Triage_and_RAID.xlsx` | Shared | xlsx | Template v1.0 | Triage Log (customization cap 5 + two-key) + RAID tab; dropdowns + summary |
| `Connection_Sprint_Demo_TEMPLATE.pptx` | Client-facing | pptx | Template v1.0 | 10-slide reusable shell for the bi-weekly sprint demo |

> Generic delivery artifacts complete. Candidates for promotion to `03_Shared/` if reused across engagements.

### Scope-specific: Workshop decks (`02_Delivery/Workshops/`)

15 in-scope **client (Modernizing the Core)** workshop decks copied from the (now-corrected) library and rebranded to Connection, plus `Connection_Workshop_Scope_Notes.docx` (internal — per-module Phase 1 nuances). Light tailoring per Tim; principles already baked in.

**17 decks:** Platform Foundation, CSDM, CMDB, Discovery, Service Graph Connectors, Incident, **Major Incident**, Problem, Change, Service Catalog, Knowledge, Employee Center, Virtual Agent, Performance Analytics, **Predictive Intelligence**, HAM, Integrations. (MIM + PI use the older/narrower template — cosmetic only; content correct.)

### Scope-specific: Accelerator Packs (`02_Delivery/Accelerator_Packs/`)

12 in-scope packs copied as Connection working copies (populate during delivery): Foundation, ITSM, CMDB_CSDM, Discovery, Integration (AD/SSO·SCCM·Intune·**Vonage**), Service_Catalog, Knowledge, Employee_Center, Virtual_Agent, Performance_Analytics, Predictive_Intelligence, ITAM_HAM_Foundations. See `README.md` for sprint mapping.

**Vonage CTI & Interactions (built — Phase 1 inbound voice):** `Integration_Accelerator_Pack/05_vonage_cti_interactions.xlsx` (8 tabs incl. **Developer Notes** + **Port from Legacy** — use Connection's existing setup as the spec, rebuild OOTB on OpenFrame + the Vonage connector) and `Workshops/Connection_Interactions_Vonage_CTI_Workshop.pptx`. Chat/email via Interactions deferred to a later phase.

> Workshop set now **18 decks**. Scope-specific build complete for Phase 1.

### EM Day-1: SOW Deliverables Matrix (`02_Delivery/Connection_SOW_Deliverables_Matrix.xlsx`)

Maps all **27** SOW v2.0 committed deliverables (Sec 5, 10–11) to a supporting baseline + status: **18 Ready**, **9 Adapt-from-library** (pull/tailor when the sprint arrives), **0 GAP**. Status dropdown + conditional formatting + summary.

**Gap templates built (closed the 3 gaps):**
1. `Connection_Platform_Architecture_and_CSDM_Alignment.docx` (`02_Delivery/`) — Month 1; SA completes from CSDM/CMDB workshops.
2. `Knowledge_Transfer/Connection_Administrator_Guide_and_KT.docx` — Go-Live KT; 4-session Admin KT plan + admin reference.
3. `Knowledge_Transfer/Connection_Train_the_Trainer_Toolkit.docx` — Go-Live KT; 2 sessions/area, references library demo scripts.

> Turnover set is **clean and ready to execute** — every SOW deliverable maps to a built Connection artifact or a library template to adapt. Nothing missing.

### Team enablement: Default User Story backlog (`02_Delivery/Connection_User_Stories_SN_Agile.xlsx`)

**141 default user stories** seeded from the contract-configurable decisions (the workshop KEY DECISIONS / SOW) — not exhaustive per process, but one story per configurable decision. SN Agile (`rm_story`) import-ready: README/import guide, **Epics** tab (18, import first → `rm_epic`), **Application** (119) + **Integration** (22) story tabs, and a shared **Definition of Done** tab. Each story has an As-a/I-want/So-that description, Given/When/Then acceptance criteria, story points, priority, target sprint, role, and state. Build scripts + data: `build_user_stories.py` + `userstories_data.py`.

### Team enablement: UAT (end-to-end) — distinct from sprint story-testing

- `Connection_UAT_End_to_End_Test_Scripts.xlsx` — **18 end-to-end scripts across 10 functional suites**, each with steps/expected results and **direct story-ID correlation** (Stories Validated column). A **Story Coverage** tab inverts it: every story shows the UAT script(s) that exercise it — **90 covered end-to-end, 51 sprint-story-test-only** (nothing falls through). Result-code dropdowns + a Defect Log tab.
- `Connection_UAT_Guidebook_for_End_Users.docx` — built to genuinely guide first-time testers: what UAT is/isn't, roles, how to run a script step-by-step, how to log a *good* defect (with good/bad examples), do's & don'ts, the 10 suites, go/no-go, and a tester FAQ. Confidential footer.

> Distinction held: **story testing** = team validates acceptance criteria during the sprint; **UAT** = end users validate end-to-end journeys near Go-Live (Sprint 6-7).

### Team enablement: Project Delivery Stories — *everything is a story*

`Connection_Project_Delivery_Stories.xlsx` — **55 stories across 9 work-streams** (PMO & Governance, Engagement Setup, Onboarding, Workshops, Documentation, Training & KT, Testing & Quality, Go-Live, Hypercare/Closeout). Same rigor as config stories: As-a/I-want/So-that, Given/When/Then acceptance criteria, a delivery-specific Definition of Done, traceability to the SOW deliverable/artifact, and a live Work-stream Summary. **Pairs with the 141 config stories → the complete project backlog** so leadership sees the *whole* project (dev + docs + training + PMO) in real time. This is the layer most projects miss.

**Executive Health Dashboard refit (v2):** operational KPIs (MTTR/SLA) removed — they begin post-Go-Live. Now leads with **delivery metrics**: Sprint Health, Defect Rate, Story Completion (config + delivery), Deliverables on-track. 6 health vectors + schedule + risks/decisions retained.

### Delivery Readiness Audit (`02_Delivery/Connection_Delivery_Readiness_Audit.xlsx`)

Start-to-finish audit vs SOW v2.0, both lenses (ECS + customer): **31 items — 10 Have, 10 Partial, 11 Gap (3 P1, 10 P2)**.

**P1 gaps — CLOSED:**
1. ✅ **Customer Responsibilities & Dependency Tracker** — `Connection_Customer_Dependency_Tracker.xlsx` (17 SOW Sec 6 dependencies; owner, timing rule, sprint, status, impact-if-late; RAG + summary).
2. ✅ **Cutover Runbook** — `Connection_Cutover_Runbook.docx` (pre-cutover checklist, sequence with owners/validation, rollback plan, comms, go/no-go, Hypercare handoff).
3. ✅ **Go-Live Readiness Checklist** — `Connection_Go_Live_Readiness_Checklist.xlsx` (19 gated go/no-go criteria across config/data/integrations/testing/training/cutover/support/governance/sign-offs).

**Key P2 gaps:** workshop pre-reads (cold-workshop risk), sprint capacity model (~196 stories vs velocity), SIT scripts + test-data plan, Operational Handoff Pack, PCR template + acceptance/sign-off log, RACI cut.

**Gaps closed (solidify pass):** audit now **26 Have / 5 Partial / 0 Gap**. Added: Sprint Plan & Capacity Model, RACI Matrix, Project Controls (PCR log + form, Acceptance & Sign-off Log, Decision Register, Assumptions/Out-of-Scope), SIT Test Scripts + Test Data Plan, Operational Handoff Pack, Sprint Operating Kit (DoR + planning + retro + cadence); copied 15 client workshop pre-reads + 7 internal demo scripts into Connection. Remaining 5 Partials are timing-based (lessons learned, hypercare exit report, per-sprint design docs, closeout/roadmap, variance tracking) — produced at their phase.

### Two-framework model: working baseline + static upload library

- **Working framework** = `05_Clients/Connection/` — the reproducible audit baseline (build scripts, data, brief). Stays as-is.
- **Static library** = `06_Client_Upload/Connection/` — finalized **artifacts only** (155 files: docx/pptx/xlsx; no .py/.js/.json/.md, no source inputs), mirroring the structure, for SharePoint. Front door is `00_START_HERE/Connection_Execution_Guide.docx` (the **role-based + phase-based navigator**) + `Connection_Library_Index.xlsx`. Zipped as `06_Client_Upload/Connection_Execution_Library.zip`.
- **Trigger** = `05_Clients/Connection/_tools/export_execution_library.py` — re-run to regenerate the static library from the working framework whenever finalized.
- **Convention:** new top-level **`06_Client_Upload/`** = static, upload-ready packages, one subfolder per client (the upload counterpart to `05_Clients/`).

---

## Shared Assets to Pull

From `03_Shared/00_Templates_and_Branding/`:

- [ ] Company Overview — _which version (federal / commercial)?_
- [ ] Team Bios — _which delivery team members?_
- [ ] Core Differentiators — OOTB-First Methodology, ServiceNow Expertise Depth
- [ ] Past Performance — _identify relevant references_
- [ ] Quals / Certs — _which apply_

> Reference by path. Do not copy into this folder.

---

## Sprint / Delivery Cadence

18-week Phase 1, 2-week sprints, organized in the SOW deck as **4 stages**: Stage 1 Initiate & Plan (Sprints 0–2, Wks 1–6), Stage 2 Execute (Sprints 3–5, Wks 7–12), Stage 3 Deliver (Sprints 6–7, Wks 13–16), Stage 4 Close (Sprint 8, Wks 17–18). **Go-Live targeted for Week 16; Hypercare Wks 17–18.**

> Note: this is slightly tailored from the generic ECS baseline (Sprint 0 + Sprints 1–6 + Hypercare). Use the Connection cadence above for all Connection collateral; confirm the exact sprint↔week mapping against the project plan in `02_Delivery/`.

---

## Key Open Questions

- Who are the client-side and ECS-side points of contact, the Project Sponsor / Product Owner, and the ECS delivery team?
- Confirm the team roles for the onboarding map (proposed: EM/Delivery Lead, Solution Architect, Developer, BA/Process Consultant, QA/UAT Lead).
- Which of the four onboarding deliverables are in scope, in what order, and what is the kickoff date?

---

## Source Artifacts & Delivery Docs

Connection-specific docs built while Connection was the OOTB working model now live in `00_Source_Inputs/` (see its `MANIFEST.md`). The curation approach for turning the library into a right-sized, role-based onboarding package is in `01_Onboarding/ONBOARDING_MAP.md`.

**Default project plan:** `02_Delivery/Connection_18Week_Project_Plan.xlsx` — the 18-week baseline plus a resource build-up tab added for Connection. The generic baseline (`03_Shared/02_Project_Plans/ECS_18Week_Baseline_Project_Plan.xlsx`) stays in the library; fold the resource-build-up tab back into it later if it should become standard.

---

## Session Log

| Date | Work Done |
|---|---|
| 2026-06-09 | Created `05_Clients/` category + README; scaffolded Connection workspace + this brief. Moved 6 Connection-specific docs into `00_Source_Inputs/` (+ MANIFEST). Drafted `ONBOARDING_MAP.md` — role-based internal tracks + staged client cut. |
| 2026-06-09 | Added SOW v2.0 + sales deck to `00_Source_Inputs/`; captured full scope, constraints, and deliverables into this brief. Adjusted project plan (retitled for Connection, relabeled to Sprints 0–8 / 4 stages; 670 formulas verified). Built **Client Onboarding Guide** (docx) + **Kickoff Deck** (pptx) — both Draft v1.0, verified. Paused before internal templates. |
| 2026-06-09 | Relocated `Customer_Governance_Charter.docx` → `01_Onboarding/Client_Facing/` (it's a client deliverable, not raw input). Synced Tim's "Technical Consultant(s)" edit into both build scripts. **Revised Kickoff Deck → Draft v1.1, 13 slides** with visual upgrades: roadmap timeline + Go-Live milestone, KPI tiles, scope card grid, Rule-of-Three + Two-Key diagrams. Verified by render. |
| 2026-06-09 | Built **internal baseline (3 docs)** in `01_Onboarding/Internal_Team/`, all Internal Use Only: Team Onboarding & Vision Guide, Engagement Delivery Guidelines, Role & Accountability Quick-Reference. Grounded in the OOTB Delivery Playbook + Internal Governance Operating Guide. Verified footers + render. |
| 2026-06-09 | Built **Workshop Facilitation Guide** (docx, internal) — 5-tier framework, six-beat pattern, decision-forcing techniques, scripted rebuttals — and **Onboarding Checklist/Tracker** (xlsx) — 19 Sprint 0 tasks, status dropdown + conditional formatting + live summary (zero formula errors). Onboarding package complete. |
| 2026-06-09 | Built **generic delivery artifacts** in `02_Delivery/`, consolidated from 00–03 base components: Weekly Status Report (docx, client-facing), Executive Health Dashboard (1-page pptx, 6-vector model), Governance Triage & RAID (xlsx), Sprint Demo template (pptx). Footers verified; xlsx zero formula errors. Paused before scope-specific deliverables. |
| 2026-06-09 | **Library fix (00–03):** audited all 31 workshop decks' "THE LINE" (config-vs-customization) slide. Found 2 defects: (A) garbled char-per-bullet in 9 OOTB-First decks, (B) generic placeholder in 9 Modernizing decks. Fixed all 18 at source — de-garbled losslessly (A) and ported module-specific content (B), RS authored. Verified by render. Now safe to copy/tailor for Connection. |
| 2026-06-09 | **Scope-specific (workshops):** copied 15 in-scope client (Modernizing) workshop decks into `02_Delivery/Workshops/`, rebranded footers to Connection; built `Connection_Workshop_Scope_Notes.docx` (per-module Phase 1 nuances). Flagged MIM + PI client-deck gaps. Accelerator packs next. |
| 2026-06-09 | Added **MIM + PI** client workshop decks (verified content client-appropriate; older template). Copied **12 in-scope accelerator packs** into `02_Delivery/Accelerator_Packs/` (+ index README). Scope notes → v1.1. **Paused on Vonage/Interactions** pending approach discussion. Workshop set now 17 decks. |
| 2026-06-09 | **Vonage CTI & Interactions (Phase 1 inbound voice):** built the accelerator pack `05_vonage_cti_interactions.xlsx` (8 tabs incl. Developer Notes + Port from Legacy, via accelerator_pack_builder styling; zero errors) and the `Connection_Interactions_Vonage_CTI_Workshop.pptx` (10 slides, process flow + 3 key decisions). Updated scope notes → v1.2 and pack README. Workshop set now 18 decks. Scope-specific Phase 1 build complete. |
| 2026-06-09 | **SOW deliverables review:** extracted all 27 committed deliverables from SOW v2.0; mapped each to a supporting baseline. Built `Connection_SOW_Deliverables_Matrix.xlsx` (EM day-1). Result: 15 Ready, 9 Adapt-from-library, 3 GAP. |
| 2026-06-09 | **Closed the 3 gaps:** built Architecture & CSDM Alignment doc (`02_Delivery/`), Administrator Guide & KT + Train-the-Trainer Toolkit (`02_Delivery/Knowledge_Transfer/`) — all docx via EcsDocument, Confidential footer. Updated matrix → **18 Ready / 9 Adapt / 0 GAP**. Turnover set complete. |
| 2026-06-09 | **Default user story backlog:** mined the workshop KEY DECISIONS across 18 modules; built `Connection_User_Stories_SN_Agile.xlsx` — **141 stories** (119 application + 22 integration), 18 epics, SN Agile/`rm_story` import-ready with Given/When/Then acceptance criteria + shared Definition of Done. Team enablement: a ready-to-import Phase 1 configuration backlog. |
| 2026-06-09 | **UAT (end-to-end):** built `Connection_UAT_End_to_End_Test_Scripts.xlsx` — 18 scripts / 10 suites with direct story-ID traceability + Story Coverage matrix (90 E2E, 51 sprint-only) + Defect Log — and `Connection_UAT_Guidebook_for_End_Users.docx` (genuinely guides first-time testers). Kept the story-testing vs UAT distinction explicit. |
| 2026-06-09 | **Everything-is-a-story layer:** built `Connection_Project_Delivery_Stories.xlsx` — 55 delivery stories / 9 work-streams (docs, training, governance, testing, go-live, hypercare) with AC + DoD + traceability + live work-stream summary. Pairs with the 141 config stories = complete project backlog. **Refit the Exec Health Dashboard (v2)** to delivery metrics (sprint health, defect rate, story/deliverable completion); dropped SLAs (post-Go-Live). |
| 2026-06-09 | **Delivery Readiness Audit:** audited all artifacts vs SOW v2.0 lifecycle, both lenses. `Connection_Delivery_Readiness_Audit.xlsx` — 31 items (10 Have / 10 Partial / 11 Gap; 3 P1, 10 P2). P1: Customer Dependency Tracker, Cutover Runbook, Go-Live Readiness Checklist. Identifies the path to close gaps before each phase. |
| 2026-06-09 | **Closed the 3 P1 gaps:** built Customer Dependency Tracker (xlsx, 17 SOW Sec 6 deps), Go-Live Readiness Checklist (xlsx, 19 gated criteria), Cutover Runbook (docx, sequence + rollback). Audit → 13 Have / 8 Gap / 0 P1 (refresh pending — file was open). |
| 2026-06-09 | **Solidify pass + two-framework model:** closed remaining gaps (Capacity Model, RACI, Project Controls [PCR/acceptance/decisions/assumptions], SIT scripts+test data, Operational Handoff, Sprint Operating Kit; copied 15 pre-reads + 7 demo scripts). Fixed delivery-story points bug. Audit → 26 Have / 5 Partial / 0 Gap. Built **`06_Client_Upload/Connection/`** static library (155 artifacts, role+phase Execution Guide + Index, zipped) via re-runnable export trigger. |
| 2026-08-07 | Built **Connection Communication Plan** (docx, client-facing, `01_Onboarding/Client_Facing/`) — Connection-specific adaptation of new library artifact CLT-S0-06: Connection cadence (Sprints 0–8 / 4 stages, Go-Live Wk 16), pod role model incl. BPC/BA Scrum Master hat, cadence rows tied to Connection artifacts (Weekly Status Report, Exec Health Dashboard, Triage & RAID, Dependency Tracker, Go-Live Checklist). Added to navigator; re-ran export trigger → 06 library + zip refreshed. |
| 2026-08-07 | **Staged JIT document rollout:** built `06_Client_Upload/Connection_Staged_Rollout/` — `Client_Drops/` (5 populated drops + ready-to-send zips; Drop 1 = initial package incl. new `Connection_Document_Roadmap.docx` CLT-CONN-ONB-03 + SOW Deliverables Matrix; workshop decks staged in `Post_Workshop/` subfolders, released after each session) and `Internal_Release_Kit/` (`Staged_Rollout_Guide.xlsx` with release log, `Drop_Email_Templates_INTERNAL.docx` INT-CONN-ROLL-01, `Release_and_Execution_Runbook_INTERNAL.docx` INT-CONN-ROLL-02). Regenerable: `_tools/build_staged_rollout.py` + email/runbook builders, run after the library export. Roadmap added to navigator; library re-exported (159) and re-zipped. |
