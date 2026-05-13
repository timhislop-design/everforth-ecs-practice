# ECS OOTB Collateral Build — Project Status
> **Foundation document. Read this first in every session.**
> Last updated: 2026-05-12 (Session 4)

---

## What this project is

A complete practice-library build for **Everforth ECS Federal's ServiceNow OOTB delivery practice**. We are systematically producing every artifact in the collateral catalog — internal consultant guides, client-facing decision tools, and shared accelerator packs — all generated from Python build scripts using a canonical brand template.

**Owner:** Timothy Hislop (tim.hislop@gmail.com)
**Repo:** `everforth-ecs-practice` (GitHub, local at `C:\Users\timhi\Documents\GitHub\everforth-ecs-practice`)
**Built with:** Cowork + Python (`python-docx`, `openpyxl`) + brand template system

> ⚠️ **Folder discipline:** This project lives exclusively at `C:\Users\timhi\Documents\GitHub\everforth-ecs-practice`.
> Do NOT use the OneDrive `whollyfare` folder — that is personal business only and unrelated to this project.

---

## Folder structure

```
00_Master_Blueprint/        Master catalog (JSON) + rendered blueprint (.docx)
01_Internal/                Consultant-only artifacts (handbooks, playbooks, how-to guides)
02_Client/                  Customer-facing artifacts (decision guides, pre-reads, closeout)
03_Shared/                  Both audiences (accelerator packs, sprint workbooks, governance)
```

---

## Key files — read these to get fully oriented

| File | Purpose |
|------|---------|
| `PROJECT_STATUS.md` | **This file** — session foundation and orientation |
| `00_Master_Blueprint/NEXT_SESSION_PROMPT.md` | Detailed build instructions, roadmap, and pickup prompt for the active artifact |
| `00_Master_Blueprint/blueprint_catalog.json` | Source of truth for every artifact's build status |
| `03_Shared/00_Templates_and_Branding/BRAND_STANDARD.md` | Non-negotiable brand rules for all docx/xlsx/pptx output |
| `03_Shared/00_Templates_and_Branding/ecs_template.py` | Python module — every docx artifact imports from here |
| `03_Shared/00_Templates_and_Branding/pptx_brand.js` | Node.js module — every pptx artifact imports from here (PPTX equivalent of ecs_template.py) |
| `03_Shared/00_Templates_and_Branding/ECS_Presentation_Template.pptx` | Blank 7-slide starter deck showing all available layouts |

---

## Build status snapshot (last updated: 2026-05-12 Session 4)

**Notable built blocks (not exhaustive — catalog JSON is source of truth):**

| # | Artifact | ID | Status |
|---|----------|----|--------|
| 1 | Manager's Trust-But-Verify Playbook | INT-TBV-01 | ✅ Built |
| 2 | Engagement Health Dashboard | INT-TBV-02 | ✅ Built |
| 3 | Customization Variance Tracker | INT-TBV-03 | ✅ Built |
| 4 | Bi-Weekly Sponsor Sync Agenda Template | INT-TBV-04 | ✅ Built |
| 5 | Customization Council Pre-Read Template | INT-TBV-05 | ✅ Built |
| 6 | Sprint Demo Discipline Audit | INT-TBV-06 | ✅ Built |
| 7 | Practice Management Monthly Review | INT-TBV-07 | ✅ Built |
| 8 | Engagement Course-Correction Playbook | INT-TBV-08 | ✅ Built |
| 9 | Consultant Coaching Conversation Templates | INT-TBV-09 | ✅ Built |
| 10 | Consultant Handbook v1 skeleton | INT-CH-01 | ✅ Built |
| 11 | SAM Foundations Accelerator Pack | AP-06 | ✅ Built |
| 12 | SAM Realization Accelerator Pack | AP-07 | ✅ Built |
| 13 | HAM Foundations Accelerator Pack | AP-04 | ✅ Built |
| 14 | HAM Realization Accelerator Pack | AP-05 | ✅ Built |
| 15 | Decision Topic Guides (CLT-DT-01 through CLT-DT-14) | CLT-DT-01–14 | ✅ Built |
| 16 | Workshop Pre-Reads (16 disciplines) | CLT-WP-01–02 | ✅ Built |
| 17 | Adopt-vs-Re-engineer Cheatsheet — Catalog | INT-AR-01 | ✅ Built |
| 18 | Adopt-vs-Re-engineer Cheatsheet — Category | INT-AR-02 | ✅ Built |
| 19 | Adopt-vs-Re-engineer Cheatsheet — SLA | INT-AR-03 | ✅ Built |
| 20 | HAM How-To Consultant Guide | INT-HT-16 | ✅ Built |
| 21 | Sprint 1 Platform Foundation Facilitator Guide | INT-FG-01 | ✅ Built |
| 22 | Incident Management Demo Script | INT-DS-01 | ✅ Built |
| 23 | Event Management Foundations Accelerator Pack | AP-08 | ✅ Built |
| 24 | Event Management Workshop Pre-Read | CLT-WP-17 | ✅ Built |
| 25 | Event Management Decision Topic Guide | CLT-DT-15 | ✅ Built |
| 26 | JIT Baseline Story Library (91 stories, 15 process areas) | INT-SS-01 | ✅ Built |
| 27 | Event Management Realization Accelerator Pack | AP-09 | ✅ Built |
| 28 | Sprint 1 Incident Management Facilitator Guide | INT-FG-02 | ✅ Built |
| 29 | Incident Management How-To Consultant Guide | INT-HT-02 | ✅ Built |
| 30 | Adopt-vs-Re-engineer Cheatsheet — Event Management | INT-AR-04 | ✅ Built |
| 31 | Adopt-vs-Re-engineer Cheatsheet — AIOps & Advanced Correlation | INT-AR-05 | ✅ Built |

---

## Active artifact — Next session candidates

**Highest priority (completes the internal bundle for Incident/Change/Problem):**
- INT-FG-03 Sprint 2 Catalog & Request Facilitator Guide
- INT-FG-04 Sprint 2 Employee Center Facilitator Guide
- INT-HT-03 Major Incident Management How-To
- INT-HT-04 Problem Management How-To

**Also high value:**
- INT-AR-06 State/Lifecycle Discipline Cheatsheet
- INT-AR-07 Knowledge Article Curation Cheatsheet
- AP-10 CSDM Accelerator Pack
- AP-11 CMDB Accelerator Pack

---

## The non-negotiable rules

1. **Every Internal/Client .docx** is built using `EcsDocument` from `ecs_template.py` — never roll custom styling
2. **Every Accelerator Pack workbook** uses `accelerator_pack_builder.TabContent + build_workbook()`
3. **Every .pptx deck** is built using `pptx_brand.js` via `brand.init()` — never inline color constants or shape helpers
4. **Client artifacts** must pass `footer_left="ECS Federal · ServiceNow Practice  ·  Confidential"` in `DocMeta` (docx) or `footerLabel` to `init()` (pptx) — the default footer says "Internal Use Only" which leaks on customer docs
5. **After each artifact:** update `blueprint_catalog.json` → re-run `build_master_blueprint.py` → update this file and `NEXT_SESSION_PROMPT.md`

---

## Session startup checklist

At the start of any new session, read in this order:
1. This file (`PROJECT_STATUS.md`) — orientation
2. `00_Master_Blueprint/NEXT_SESSION_PROMPT.md` — active artifact details and pickup prompt
3. `00_Master_Blueprint/blueprint_catalog.json` — build status source of truth
4. `03_Shared/00_Templates_and_Branding/BRAND_STANDARD.md` — brand rules

Then confirm with the user what we're working on before building anything.

---

## Working patterns and decisions

- **Build scripts are co-located with artifacts** — each artifact's `build_*.py` (docx) or `build_*.js` (pptx) lives in the same folder as the output file
- **Closest model for Client decision guides:** `02_Client/04_Decision_Topic_Guides/build_CLT-DT-01.py`
- **Closest model for workshop decks:** `03_Shared/05_Workshop_Presentations/build_IM_Workshop.js` (or reference `build_ecs_presentation_template.js`)
- **Validate after every build:** `docx/scripts/office/validate.py` + spot-check PDF via `soffice` (works for both .docx and .pptx)
- **PPTX run command:** `NODE_PATH=/usr/local/lib/node_modules_global/lib/node_modules node build_your_deck.js`
- **Session limit strategy:** finish the artifact in flight, update this file and `NEXT_SESSION_PROMPT.md`, then stop cleanly
- **Context discipline:** save early to files — don't let large drafts live in chat

---

## How to update this file

After each session, update:
- The **Build status snapshot** table (flip status to ✅ Built)
- The **Active artifact** section (roll to the next item)
- The **Last updated** date at the top

Keep it short. The detail lives in `NEXT_SESSION_PROMPT.md`.
