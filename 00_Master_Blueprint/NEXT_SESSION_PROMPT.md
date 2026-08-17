# Next Session — Pickup Prompt

> Paste the prompt block below into a new Cowork session to resume the OOTB collateral build exactly where we left off. Update the "Last completed" line each session and roll the "Next up" pointer down the roadmap.

---

## Status snapshot (last update: 2026-08-07)

**Session addition (2026-08-07):**
- **CLT-S0-06 — Communication Plan (Client-Facing)** → `02_Client/02_Sprint0_Customer_Readiness/CLT-S0-06_Communication_Plan.docx`
  - Client-facing adaptation of INT-S0-07 (internal comms plan). New ID — added to the Sprint 0 Customer Readiness table in `blueprint_catalog.json` as **Built**
  - 5 sections: Purpose · Communication Cadence (full Sprint 0 → Hypercare table, internal template IDs stripped, Governance Triage Log framed as a feature) · Roles & Responsibilities (your team / ECS team) · Escalation Path (3 steps with owners + clocks) · Contact Roster (fill-in at Sprint 0 kickoff)
  - Internal-only Sprint Retro row dropped; client tone per BRAND_STANDARD (partnership-oriented, "Confidential — prepared for the recipient and their organization", client footer)
  - Build script: `build_CLT-S0-06.py` (co-located) — includes a `fix_layout()` helper that pins `w:tblLayout` fixed + explicit `tblGrid` so `col_widths_in` actually render (template default autofit ignores them); reusable for future width-sensitive tables
  - Master Blueprint re-rendered from JSON

**Session addition (2026-08-03):**
- **INT-OR-03 — Solution Architect Role Narrative (v2.0, 50/50 model)** → `01_Internal/11_Practice_Onboarding/INT-OR-03_Solution_Architect_Role_Narrative_INTERNAL.docx`
  - Concise (cover + 3 pages) internal role & responsibilities narrative for the hybrid SA: 50% delivery (architecture, technical sign-off, workshops, standards) / 50% presales (technical discovery, demos, RFX technical volumes, draft LOE)
  - v2.0 per Tim's direction: generic ServiceNow framing (not OOTB-first heavy) with a "Role Summary at a Glance" bullet section up front for easy reuse in 2–3 page docs; v1.0 (longer, OOTB-first/practice-model flavored) is in git history if needed
  - Encodes pricing boundary (SA drafts LOE only; delivery leadership owns hours/staffing; rates & margin with delivery + practice leadership), collision rules for the split, decision-rights table, success measures
  - Build script: `build_INT-OR-03.py` · Status in `blueprint_catalog.json`: **Built** (Practice Onboarding & Adoption table; INT-OR-02 Rollout Staging Plan remains Plan)

**Completed across the build sessions so far:**

1. **INT-TBV-01 — Manager's Trust-But-Verify Playbook** (Internal, 18 pages, .docx) — `01_Internal/09_Trust_but_Verify_Management/`
10. **INT-TBV-02 through INT-TBV-09 — Full Trust-But-Verify Pack** (Internal) — `01_Internal/09_Trust_but_Verify_Management/`
    - INT-TBV-02: Engagement Health Dashboard (6-tab xlsx — Roll-Up, 5 vector tabs with traffic-light scoring + reference tables)
    - INT-TBV-03: Customization Variance Tracker (4-tab xlsx — Instructions, Variance Log, Decision Log, Sprint Capacity Calculator)
    - INT-TBV-04: Bi-Weekly Sponsor Sync Agenda Template (docx — pre-meeting checklist, 5 agenda blocks, action tracker, carry-forward tracker)
    - INT-TBV-05: Customization Council Pre-Read Template (docx — 7 sections: request, OOTB alt analysis, scope/effort, business outcome, contract risk, recommendation, decision record)
    - INT-TBV-06: Sprint Demo Discipline Audit (docx — 6 scored items: C-1/C-2/C-3 configuration + L-1/L-2/L-3 language, coaching trigger table, dashboard update instructions)
    - INT-TBV-07: Practice Management Monthly Review Template (docx — cross-engagement roll-up, 5 pattern-spotting questions, response routing, Practice Health Tile, action tracker)
    - INT-TBV-08: Engagement Course-Correction Playbook (docx — decision tree, 4 class playbooks each with action protocol + communication templates, executive escalation protocol)
    - INT-TBV-09: Consultant Coaching Conversation Templates (docx — 7 patterns A–G with full conversation scripts, coaching log)
    - All 8 artifacts marked **Built** in `blueprint_catalog.json`
2. **ECS canonical template + infrastructure** — `ecs_template.py`, `BRAND_STANDARD.md`, `.dotx` template
3. **Master Blueprint re-rendered** from JSON (31 pages) — `00_Master_Blueprint/ECS_OOTB_Collateral_Blueprint.docx`
4. **INT-CH-01 — Consultant Handbook (v1 skeleton)** (Internal, 17 pages, .docx) — `01_Internal/01_Consultant_Handbook/`
5. **AP-06 — SAM Foundations Accelerator Pack** (Shared, 4-page README + 6 xlsx workbooks) — `03_Shared/01_Accelerator_Packs/SAM_Foundations_Accelerator_Pack/`
6. **AP-07 — SAM Realization Accelerator Pack** (Shared, 5-page README + 8 xlsx workbooks) — `03_Shared/01_Accelerator_Packs/SAM_Realization_Accelerator_Pack/`
7. **CLT-DT-01 — Decision Topic Guide: Catalog Item Rationalization** (Client, 14 pages, .docx) — `02_Client/04_Decision_Topic_Guides/`
   - Build script: `build_CLT-DT-01.py`
   - Warmer-partnership tone matching the existing Category Realignment whitepaper exemplar
   - **NEW TEMPLATE FEATURE:** `ecs_template.DocMeta` now accepts a `footer_left` override. Client artifacts pass `footer_left="ECS Federal · ServiceNow Practice  ·  Confidential"` so footers don't leak "Internal Use Only" on customer-facing docs.
   - Status in `blueprint_catalog.json`: **Built**
8. **CLT-WP-01 + CLT-WP-02 — All 16 Workshop Pre-Reads** (Client, ~5 pages each, .docx) — `02_Client/05_Workshop_Pre-Reads/`
   - Single build script: `build_CLT-WP-all.py` — generates all 16 in one run
   - 16 disciplines: Platform Foundation, Incident Mgmt, Major Incident Mgmt, Problem Mgmt, Change Mgmt, Service Catalog & Request, Knowledge Mgmt, Employee Center, Virtual Agent, Predictive Intelligence, Now Assist/GenAI, CSDM, CMDB, Discovery, Service Graph Connectors, HAM
   - Structure per pre-read: How to Use → What Is It → Why It Matters → OOTB Capabilities (table) → Key Workshop Decisions → Things to Think About Before We Meet
   - Validated: client-tone footers ("Confidential", not "Internal Use Only"), correct eyebrow tags, H1 structure
   - Also fixed a pre-existing JSON truncation bug in `blueprint_catalog.json` (was missing closing `}`)
   - Status in `blueprint_catalog.json`: **Built**
9. **CLT-DT-02 through CLT-DT-14 — All 13 remaining Decision Topic Guides** (Client, ~10 pages each, .docx) — `02_Client/04_Decision_Topic_Guides/`
   - Shared renderer: `dtg_builder.py` — `build_dtg(d: dict)` called from 3 batch scripts
   - `build_batch1_DT02-05.py` → CLT-DT-02 (Category Structure), 03 (SLA Discipline), 04 (Assignment Rules), 05 (Approval Discipline)
   - `build_batch2_DT06-09.py` → CLT-DT-06 (State & Lifecycle), 07 (Knowledge Curation), 08 (Virtual Agent Topics), 09 (Predictive Intelligence Readiness)
   - `build_batch3_DT10-14.py` → CLT-DT-10 (CMDB Class Selection), 11 (Discovery Phasing), 12 (Integration Prioritization), 13 (Custom vs. OOTB Framework), 14 (Technical Debt Elimination Roadmap)
   - Validated: all 13 docx files pass client-tone check (Confidential=True, Internal Use Only=False)
   - Status in `blueprint_catalog.json`: **All Built**

**Session 4 additions (2026-05-12):**
- **AP-09 — Event Management Realization Accelerator Pack** → `03_Shared/01_Accelerator_Packs/Event_Management_Realization_Accelerator_Pack/`
  - 8 xlsx workbooks: 01_service_health_maps, 02_storm_management, 03_aiops_integration, 04_alert_intelligence, 05_remediation_workflows, 06_advanced_correlation, 07_analytics_and_kpis, 08_hypercare_and_maturity
  - README docx: 00_README_Event_Management_Realization_Pack.docx
  - Build script: build_AP-09.py
- **INT-FG-02 — Sprint 1 Incident Management Facilitator Guide** → `01_Internal/04_Per_Sprint_Facilitator_Guides/INT-FG-02_Sprint1_Incident_Facilitator_Guide_INTERNAL.docx`
  - 6 sections: How to Use, Sprint Overview, 3 Workshop Agendas (Category/State, Priority/Assignment/SLA, Validation), Decision Pre-Fills (5 decisions with ECS pre-fills + pushback language), Common Pitfalls (5 pitfalls), Sprint Demo Discipline, Sprint Retro Template
  - Build script: build_INT-FG-02.py
- **INT-HT-02 — Incident Management How-To Consultant Guide** → `01_Internal/05_Discipline_How-To_Guides/Incident_Management_How-To_Consultant_Guide_INTERNAL.docx`
  - 6 sections: OOTB Capabilities (Core Workflow + Major Incident + Reporting), Two-Phase Approach, OOTB Defense Language (5 patterns), Demo Flow (4 Acts), UAT Scenarios (5 scenarios), Post-Go-Live Ownership
  - Build script: build_INT-HT-02.py
- **INT-AR-04 — Event Management Adopt-vs-Re-engineer Cheatsheet** → `01_Internal/06_Adopt_vs_Reengineer_Cheatsheets/INT-AR-04_Event_Management_Cheatsheet_INTERNAL.docx`
  - 10 patterns: event sources, MID Server, event rules, CI correlation, alert promotion
  - Build script: build_INT-AR-04-05.py (shared script with INT-AR-05)
- **INT-AR-05 — AIOps and Advanced Correlation Cheatsheet** → `01_Internal/06_Adopt_vs_Reengineer_Cheatsheets/INT-AR-05_AIOps_Advanced_Correlation_Cheatsheet_INTERNAL.docx`
  - 10 patterns: AIOps/ML, storm management, advanced correlation, runbook automation

**NOTE ON INT-AR NUMBERING:** The blueprint_catalog.json had INT-AR-04/05 originally planned as "Assignment Rules" and "Approval Discipline." We built Event Management/AIOps instead as higher priority. In the next session, remap the catalog: add INT-AR-06 = Assignment Rules, INT-AR-07 = Approval Discipline, and treat INT-AR-04/05 as the Event Management bundle we built.

**Session 3 additions (2026-05-12):**
- **AP-08 — Event Management Foundations Accelerator Pack** → `03_Shared/01_Accelerator_Packs/Event_Management_Foundations_Accelerator_Pack/`
  - 6 xlsx workbooks: 01_event_sources, 02_event_rules_baseline, 03_alert_promotion_rules, 04_ci_correlation_mapping, 05_mid_server_configuration, 06_operator_workspace_setup
  - README docx: 00_README_Event_Management_Foundations_Pack.docx
  - Build script: build_AP-08.py
- **CLT-WP-17 — Event Management Workshop Pre-Read** → `02_Client/05_Workshop_Pre-Reads/WP_17_Event_Management_CLIENT.docx`
  - Build script: build_CLT-WP-17_event_management.py; now 17 workshop pre-reads total
- **CLT-DT-15 — Event Management Decision Topic Guide** → `02_Client/04_Decision_Topic_Guides/Event_Management_Decision_Guide_CLIENT.docx`
  - Build script: build_CLT-DT-15_event_management.py; now 15 Decision Topic Guides total
- **INT-SS-01 — JIT Baseline Story Library** → `03_Shared/04_Sprint_Workbooks/ECS_JIT_Baseline_Stories.xlsx`
  - Single xlsx, 15 tabs (one per process area), 91 decision-point-driven stories across all 18-week sprints
  - Build script: build_JIT_baseline_stories.py

**Session 2 additions (2026-05-11):**
- **INT-AR-01/02/03 — Adopt-vs-Re-engineer Cheatsheets (batch)** → `01_Internal/06_Adopt_vs_Reengineer_Cheatsheets/`
  - INT-AR-01: Catalog Item Rationalization | INT-AR-02: Category Structure Simplification | INT-AR-03: SLA Discipline
  - Single batch build script: `build_INT-AR-batch.py`; all 3 docx files confirmed built
- **INT-HT-16 — HAM How-To Consultant Guide** → `01_Internal/05_Discipline_How-To_Guides/`
  - 7 sections: OOTB Capabilities, Two-Phase Approach, OOTB Defense, Demo Flow (4 Acts), UAT Scenarios, Post-Go-Live Ownership
- **INT-FG-01 — Sprint 1 Platform Foundation Facilitator Guide** → `01_Internal/04_Per_Sprint_Facilitator_Guides/`
  - 6 sections: Sprint Overview, 3 Workshop Agendas, Decision Pre-Fills (5 decisions + ECS recs + pushback), Common Pitfalls, Retro Template
- **INT-DS-01 — Incident Management Demo Script** → `01_Internal/07_Demo_Scripts/`
  - 4 sections: Pre-Demo Setup, Demo Narrative (5 Acts, click-by-click), Common Q&A (7 questions), Recovery Notes (6 scenarios)

**NOTE: THE FULL TRUST-BUT-VERIFY PACK (INT-TBV-01 through INT-TBV-09) IS NOW COMPLETE.**
All 9 TBV artifacts are Built in `blueprint_catalog.json`. The folder `01_Internal/09_Trust_but_Verify_Management/` is fully populated.

---

## Pickup Prompt — paste this into the next session

```
Continuing the ECS OOTB collateral build. Before doing anything else, read these three files:
  1. 00_Master_Blueprint/NEXT_SESSION_PROMPT.md   (this file — current status + roadmap)
  2. 00_Master_Blueprint/blueprint_catalog.json   (source of truth for build status)
  3. 03_Shared/00_Templates_and_Branding/BRAND_STANDARD.md  (non-negotiable brand rules for docx artifacts)

THE NON-NEGOTIABLE RULE
Every Internal/Client docx artifact is built using ecs_template.EcsDocument.
Every Accelerator Pack workbook is built using accelerator_pack_builder.TabContent + build_workbook().
Do NOT roll your own docx or xlsx styling. Import from 03_Shared/00_Templates_and_Branding/.

CLIENT AUDIENCE TONE DISCIPLINE (carries over from CLT-DT-01)
- Partnership-oriented, never preachy
- Never frames customer's prior choices as wrong — "didn't grow that way by accident"
- Eyebrow tag uses "DECISION TOPIC GUIDE · ..." (not "INTERNAL ...")
- Audience names customer roles (Service Owners, Catalog Owners, etc.)
- Confidentiality = "Confidential — prepared for the recipient and their organization"
- ALWAYS pass footer_left="ECS Federal · ServiceNow Practice  ·  Confidential" on Client artifacts
  (DocMeta supports this; default footer says "Internal Use Only" which leaks on customer docs)
- Speak to "the next chapter" — the future state — not "fixing the mess"

MESSAGING CONVENTIONS — READ BEFORE WRITING ANY CLIENT-FACING ARTIFACT
The governing theme for ALL customer-facing output is "Modernizing the Core."
"OOTB-First" is internal discipline language — use it freely in internal docs, sparingly in client body text, never as a headline or customer-facing theme.

The customer message is:
  We are standing up a proven, AI-ready baseline. Any deviations are captured in the
  Governance Triage Log — not lost, not ignored — and addressed iteratively in a
  follow-on engagement once the core is stable and delivering value.

- Presentation title pattern: "Modernizing the Core"
- Subtitle pattern:          "[Process Area] — Ensuring AI Realization and Optimizing Long-Term Value"
- Deviations = "governed deviations" captured in the Governance Triage Log (frame as a feature)
- The triage log protects both the baseline AND the customer's legitimate requirements
- "Customization vs. configuration" language is fine in body text / decision guides; never lead with it
- Full rules: 03_Shared/00_Templates_and_Branding/BRAND_STANDARD.md — Section 11 (Messaging Conventions)

WORKED EXAMPLES BY ARTIFACT TYPE
- Internal full docx:        01_Internal/09_Trust_but_Verify_Management/build_INT-TBV-01.py
- Internal skeleton docx:    01_Internal/01_Consultant_Handbook/build_INT-CH-01.py
- JSON-driven docx:          00_Master_Blueprint/build_master_blueprint.py
- Shared Accelerator Pack:   03_Shared/01_Accelerator_Packs/SAM_Foundations_Accelerator_Pack/build_AP-06.py
- Client decision guide:     02_Client/04_Decision_Topic_Guides/build_CLT-DT-01.py
- Shared DTG renderer:       02_Client/04_Decision_Topic_Guides/dtg_builder.py  ← use for any new DTGs

NOTE: ALL 14 DECISION TOPIC GUIDES (CLT-DT-01 through CLT-DT-14) ARE NOW BUILT.
ALL 16 WORKSHOP PRE-READS (CLT-WP-01/02) ARE NOW BUILT.

NEXT ARTIFACT OPTIONS — Choose one (or both) for the next session:

OPTION A — AP-08 + AP-09: Event Management Accelerator Packs (highest field-value gap)
- Folder: 03_Shared/01_Accelerator_Packs/Event_Management_Foundations_Accelerator_Pack/ + Realization/
- Build scripts: build_AP-08_event_foundations.py + build_AP-09_event_realization.py
- Format: xlsx, Shared audience, multi-tab workbook
- Mirror HAM pack structure: Instructions, Process Decisions, Configuration Data, R&R, Consultant Guide, Adoption-vs-Reengineering, ServiceNow Mapping
- Foundations tabs: Alert Rule Design, Event Classification, CI Binding, Correlation Rules, Operational Dashboard setup
- Realization tabs: Alert Intelligence (ML), Remediation Workflows, AIOps Integration, Metrics and Reporting
- Closest model: 03_Shared/01_Accelerator_Packs/SAM_Foundations_Accelerator_Pack/build_AP-06.py
- Use accelerator_pack_builder.TabContent + build_workbook()

OPTION B — INT-FG-02: Sprint 1 Incident Management Facilitator Guide (completes Sprint 1 pair)
- Folder: 01_Internal/04_Per_Sprint_Facilitator_Guides/
- Build script: build_INT-FG-02.py
- Format: ~18 pages, docx, Internal audience
- Mirror INT-FG-01 pattern: Sprint Overview, 3 Workshop Agendas, Decision Pre-Fills, Common Pitfalls, Retro Template
- Companion to: INT-DS-01 (Incident Demo Script just built) + Sprint 1 Incident Workbook in 03_Shared/04_Sprint_Workbooks/
- Closest model: 01_Internal/04_Per_Sprint_Facilitator_Guides/build_INT-FG-01.py

STANDARD WORKFLOW
1. Use AskUserQuestion to confirm scope/depth/examples-vs-abstract before building
2. Use TaskCreate to track progress
3. Co-locate the build script with the artifact
4. Import EcsDocument from ecs_template; pass footer_left for Client tone
5. doc.save() patches the OOXML zoom attribute automatically
6. Validate: docx via /sessions/.../skills/docx/scripts/office/validate.py
7. Render to PDF via soffice and spot-check via Read tool — verify cover eyebrow, audience, footer all show Client-tone
8. Update the artifact's row in blueprint_catalog.json to Built
9. Re-run 00_Master_Blueprint/build_master_blueprint.py to keep the rendered Blueprint in sync
10. Update this NEXT_SESSION_PROMPT.md with the new status snapshot

If approaching session limit, finish the artifact in flight, update this file, and STOP.
```

---

## Build Roadmap — Status Tracker

| # | Artifact | ID | Folder | Status |
|---|---|---|---|---|
| 1 | Manager's Trust-But-Verify Playbook | INT-TBV-01 | `01_Internal/09_Trust_but_Verify_Management/` | **Built** ✅ |
| 2 | Consultant Handbook v1 skeleton | INT-CH-01 | `01_Internal/01_Consultant_Handbook/` | **Built** ✅ |
| 3 | SAM Foundations Accelerator Pack | AP-06 | `03_Shared/01_Accelerator_Packs/SAM_Foundations_Accelerator_Pack/` | **Built** ✅ |
| 4 | SAM Realization Accelerator Pack | AP-07 | `03_Shared/01_Accelerator_Packs/SAM_Realization_Accelerator_Pack/` | **Built** ✅ |
| 5 | Decision Topic Guide — Catalog Item Rationalization | CLT-DT-01 | `02_Client/04_Decision_Topic_Guides/` | **Built** ✅ |
| 5b | All 16 Workshop Pre-Reads | CLT-WP-01/02 | `02_Client/05_Workshop_Pre-Reads/` | **Built** ✅ |
| 6 | Decision Topic Guide — Category Structure Simplification | CLT-DT-02 | `02_Client/04_Decision_Topic_Guides/` | **Built** ✅ |
| 6b | Decision Topic Guides — SLA, Assignment, Approval | CLT-DT-03/04/05 | `02_Client/04_Decision_Topic_Guides/` | **Built** ✅ |
| 6c | Decision Topic Guides — State/Lifecycle, Knowledge, Virtual Agent, PI | CLT-DT-06/07/08/09 | `02_Client/04_Decision_Topic_Guides/` | **Built** ✅ |
| 6d | Decision Topic Guides — CMDB, Discovery, Integration, Custom-vs-OOTB, Tech Debt | CLT-DT-10/11/12/13/14 | `02_Client/04_Decision_Topic_Guides/` | **Built** ✅ |
| 7 | Adopt-vs-Re-engineer Cheatsheet — Catalog (01), Category (02), SLA (03) | INT-AR-01/02/03 | `01_Internal/06_Adopt_vs_Reengineer_Cheatsheets/` | **Built** ✅ |
| 8 | Event Management Foundations Accelerator Pack | AP-08 | `03_Shared/01_Accelerator_Packs/` | **Built** ✅ |
| 9 | Event Management Realization Accelerator Pack | AP-09 | `03_Shared/01_Accelerator_Packs/` | **Built** ✅ |
| 10 | HAM How-To Consultant Guide | INT-HT-16 | `01_Internal/05_Discipline_How-To_Guides/` | **Built** ✅ |
| 11 | Sprint 1 Platform Foundation — Facilitator Guide | INT-FG-01 | `01_Internal/04_Per_Sprint_Facilitator_Guides/` | **Built** ✅ |
| 12 | Incident Management Demo Script | INT-DS-01 | `01_Internal/07_Demo_Scripts/` | **Built** ✅ |
| 13 | Sprint 1 Incident Facilitator Guide | INT-FG-02 | `01_Internal/04_Per_Sprint_Facilitator_Guides/` | **Built** ✅ |
| 14 | Incident Management How-To | INT-HT-02 | `01_Internal/05_Discipline_How-To_Guides/` | **Built** ✅ |
| 15 | Event Management AR Cheatsheet | INT-AR-04 | `01_Internal/06_Adopt_vs_Reengineer_Cheatsheets/` | **Built** ✅ |
| 16 | AIOps & Advanced Correlation AR Cheatsheet | INT-AR-05 | `01_Internal/06_Adopt_vs_Reengineer_Cheatsheets/` | **Built** ✅ |
| 17 | Sprint 2 Catalog & Request Facilitator Guide | INT-FG-03 | `01_Internal/04_Per_Sprint_Facilitator_Guides/` | **Next** ⬅️ |
| 18 | Sprint 2 Employee Center Facilitator Guide | INT-FG-04 | `01_Internal/04_Per_Sprint_Facilitator_Guides/` | Pending |
| 19 | Major Incident Management How-To | INT-HT-03 | `01_Internal/05_Discipline_How-To_Guides/` | Pending |
| 20 | Problem Management How-To | INT-HT-04 | `01_Internal/05_Discipline_How-To_Guides/` | Pending |
| 21 | CSDM Accelerator Pack | AP-10 | `03_Shared/01_Accelerator_Packs/` | Pending |
| 22 | CMDB Accelerator Pack | AP-11 | `03_Shared/01_Accelerator_Packs/` | Pending |

**Roadmap progress: 16 of 22+ line items built. The full Event Management bundle (Foundations + Realization + AR Cheatsheets + Workshop Pre-Read + Decision Guide + JIT Stories) is complete. Sprint 2 facilitator guides and remaining How-To guides are the highest-priority next items.**

---

## Notes for AP-08 (next session) — Event Management Foundations Accelerator Pack

**Audience:** Shared (customer fills Process Decisions + Configuration Data tabs; ECS works Consultant Guide + Adoption-vs-Reengineering + ServiceNow Mapping tabs).

**Purpose:** Structured workbook to drive Event Management configuration decisions in Sprint 5 (Service Graph + HAM + Integrations). Companion to INT-HT-18 (Event Management How-To, not yet built).

**Mirror the HAM Foundations pack structure (AP-04):**
- Tab 1: Instructions (how to use the pack, tab guide, who fills what)
- Tab 2: Process Decisions (customer fills: alert sources, classification taxonomy, severity mapping, assignment targets, escalation paths)
- Tab 3: Configuration Data (customer fills: connector names, alert rules, CI binding rules, correlation rules, dashboard layout preferences)
- Tab 4: Roles & Responsibilities (RACI for Event Management)
- Tab 5: Consultant Guide (internal — ECS configuration mapping, common pitfalls, ECS recommendations per decision)
- Tab 6: Adoption vs. Re-engineering (internal — OOTB alert processing vs. custom correlation logic decision table)
- Tab 7: ServiceNow Mapping (internal — field mapping from alert sources to Event record fields, integration connector matrix)

**Key Event Management decisions to drive:**
1. Alert sources (monitoring tools: SolarWinds, Dynatrace, Splunk, Datadog, etc.)
2. Event classification taxonomy (how alerts map to categories and sub-categories)
3. CI binding rules (how alerts link to CMDB CIs)
4. Alert-to-incident promotion thresholds (when an alert auto-creates an incident)
5. Correlation rules (grouping related alerts into a single event)
6. Operational dashboard design (who sees what, at what refresh rate)

**Closest model:** `03_Shared/01_Accelerator_Packs/SAM_Foundations_Accelerator_Pack/build_AP-06.py`
**Builder:** `03_Shared/00_Templates_and_Branding/accelerator_pack_builder.py` — use `TabContent + build_workbook()`

---

## Branding decisions baked into the templates

Refer to `03_Shared/00_Templates_and_Branding/BRAND_STANDARD.md` for the full standard. Short version:

- US Letter docx, 1 in left/right, 0.8 in top/bottom margins
- Calibri throughout (docx); Arial throughout (xlsx workbooks)
- H1 16pt navy bold (auto-numbered when `numbered=True`); H2 13pt navy bold; H3 11.5pt accent-blue bold
- Cover: bright-teal eyebrow + 28pt navy title + deep-teal italic subtitle + teal divider line + audience/companion/doc-ID meta block
- Page header: logo + letter-spaced slate running label + teal underline
- Footer: slate org line + tab + "Page X of Y"
  - **Internal artifacts**: footer left = "ECS Federal · ServiceNow Practice · Internal Use Only" (default)
  - **Client artifacts**: pass `footer_left="ECS Federal · ServiceNow Practice  ·  Confidential"` in DocMeta
- docx tables: navy header (`#0B1F3A`) with white bold text, alternating row shading (`#F8FAFC`), light-gray borders (`#E2E8F0`)
- xlsx workbook banners: navy fill with white bold text; cyan section headers; amber customer-fill cells
- docx callout: light-blue fill, accent-blue border, navy bold text

---

The blueprint catalog status field is the last column of each table row. Updates go in the JSON; the rendered Blueprint is regenerated via `build_master_blueprint.py`.
