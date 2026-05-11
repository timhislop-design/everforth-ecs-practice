# Next Session — Pickup Prompt

> Paste the prompt block below into a new Cowork session to resume the OOTB collateral build exactly where we left off. Update the "Last completed" line each session and roll the "Next up" pointer down the roadmap.

---

## Status snapshot (last update: 2026-05-11)

**Completed across the build sessions so far:**

1. **INT-TBV-01 — Manager's Trust-But-Verify Playbook** (Internal, 18 pages, .docx) — `01_Internal/09_Trust_but_Verify_Management/`
2. **ECS canonical template + infrastructure** — `ecs_template.py`, `BRAND_STANDARD.md`, `.dotx` template
3. **Master Blueprint re-rendered** from JSON (31 pages) — `00_Master_Blueprint/ECS_OOTB_Collateral_Blueprint.docx`
4. **INT-CH-01 — Consultant Handbook (v1 skeleton)** (Internal, 17 pages, .docx) — `01_Internal/01_Consultant_Handbook/`
5. **AP-06 — SAM Foundations Accelerator Pack** (Shared, 4-page README + 6 xlsx workbooks) — `03_Shared/01_Accelerator_Packs/SAM_Foundations_Accelerator_Pack/`
6. **AP-07 — SAM Realization Accelerator Pack** (Shared, 5-page README + 8 xlsx workbooks) — `03_Shared/01_Accelerator_Packs/SAM_Realization_Accelerator_Pack/`
   - Build script: `build_AP-07.py`
   - 8 workbooks: Entitlement Catalog · Reconciliation Rules · Vendor-Specific Licensing (Big Six: Oracle/MS/IBM/SAP/Adobe/Salesforce) · True-Up Forecast · Audit Defense (playbook-only) · Cloud SaaS Subscription Mgmt · Renewal Workflow · KPIs & Savings Tracking
   - All at AP-06 baseline depth, all 8 canonical tabs per workbook
   - Status in `blueprint_catalog.json`: **Built**

**Next up (Roadmap item #5):**

- **CLT-DT-01 — Decision Topic Guide: Catalog Item Rationalization** → save to `02_Client/04_Decision_Topic_Guides/`
- **NEW AUDIENCE — Client-facing.** Tone shifts from Internal (operational, candid) to Client (partnership-oriented, never preachy, avoids framing customer's prior choices as wrong). See "Notes for CLT-DT-01" below.

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

CLIENT AUDIENCE TONE SHIFT
CLT-DT-01 is the FIRST Client-facing artifact in the roadmap. Tone discipline matters:
- Partnership-oriented, never preachy
- Never frames customer's prior choices as wrong
- Eyebrow tag uses "CLIENT" or "DECISION GUIDE" (not "INTERNAL ...")
- "Audience:" line names customer roles (Service Owner, Catalog Owner, etc.) not ECS roles
- "Confidentiality" → "Prepared for [Customer] · Confidential" (not "Internal Use Only")
- Avoid operational candor about Customer's old system; speak to "the next chapter" rather than "fixing the mess"

WORKED EXAMPLES
- Internal full docx:        01_Internal/09_Trust_but_Verify_Management/build_INT-TBV-01.py
- Internal skeleton docx:    01_Internal/01_Consultant_Handbook/build_INT-CH-01.py
- JSON-driven docx:          00_Master_Blueprint/build_master_blueprint.py
- Shared Accelerator Pack:   03_Shared/01_Accelerator_Packs/SAM_Foundations_Accelerator_Pack/build_AP-06.py
- Existing Client docx (reference for tone): 02_Client/05_Workshop_Pre-Reads/Category_Realignment_Customer_WhitePaper.docx

NEXT ARTIFACT — CLT-DT-01 Decision Topic Guide: Catalog Item Rationalization
- Folder: 02_Client/04_Decision_Topic_Guides/
- Build script: build_CLT-DT-01.py (co-located)
- Format: ~10-15 pages, docx, Client audience
- Cross-references INT-AR-01 (the Internal companion cheatsheet — pending in roadmap item #8)
- Decision Topic Guides are framed as "how to think about" — they educate the customer
  decision-maker without lecturing. The customer is the decider; ECS is the framer.

STANDARD WORKFLOW
1. Use AskUserQuestion to confirm scope/depth/tone before building
2. Use TaskCreate to track progress
3. Co-locate the build script with the artifact
4. Import EcsDocument from ecs_template
5. doc.save() patches the OOXML zoom attribute automatically
6. Validate: docx via /sessions/.../skills/docx/scripts/office/validate.py
7. Render to PDF via soffice and spot-check via Read tool — verify Client tone, not Internal
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
| 5 | Decision Topic Guide — Catalog Item Rationalization | CLT-DT-01 | `02_Client/04_Decision_Topic_Guides/` | **Next** |
| 6 | Decision Topic Guide — Category Structure Simplification | CLT-DT-02 | `02_Client/04_Decision_Topic_Guides/` | Pending |
| 7 | Decision Topic Guide — SLA Discipline | CLT-DT-03 | `02_Client/04_Decision_Topic_Guides/` | Pending |
| 8 | Adopt-vs-Re-engineer Cheatsheet — Catalog Item Rationalization | INT-AR-01 | `01_Internal/06_Adopt_vs_Reengineer_Cheatsheets/` | Pending |
| 9 | Event Management Foundations Accelerator Pack | AP-08 | `03_Shared/01_Accelerator_Packs/` | Pending |
| 10 | Event Management Realization Accelerator Pack | AP-09 | `03_Shared/01_Accelerator_Packs/` | Pending |
| 11 | HAM How-To Consultant Guide | INT-HT-16 | `01_Internal/05_Discipline_How-To_Guides/` | Pending |
| 12 | Sprint 1 Platform Foundation — Facilitator Guide | INT-FG-01 | `01_Internal/04_Per_Sprint_Facilitator_Guides/` | Pending |

**Roadmap progress: 4 of 12 built.**

---

## Notes for CLT-DT-01 (next session) — Decision Topic Guide: Catalog Item Rationalization

**Audience:** Customer Service Owner, Catalog Owner, Process Manager. Customer-facing.

**Purpose:** Educate the customer decision-maker on how to think about catalog rationalization — without prescribing the answer. The customer is the decider; ECS is the framer.

**Tone discipline:**
- Partnership-oriented. "We've found that…" not "you should…"
- Never frames customer's prior catalog choices as wrong. "Catalogs grow organically" not "your catalog is bloated"
- Speaks to "the next chapter" — the future-state catalog. Past-state language is descriptive, never judgmental.
- Decision questions are open, not leading. "Which of these options fits your service model?" not "you'll want option B"

**Suggested H1 spine** (10 sections, mostly unnumbered for the conversational feel):

0. *How to use this guide* (unnumbered)
1. *Why catalog rationalization matters now* — the case for the conversation
2. *The signal that the catalog needs work* — symptoms the customer recognizes
3. *The four decisions* — the framing structure
   - Decision 1: What is the in-scope service population? (which services merit a catalog item)
   - Decision 2: What does "one catalog item" mean? (granularity)
   - Decision 3: What does the customer see vs. what does fulfillment process? (front-of-house vs. back-of-house)
   - Decision 4: How does the catalog evolve over time? (lifecycle and retirement)
4. *What good looks like* — the future-state characteristics
5. *Common patterns we've seen* — not horror stories; tactful examples
6. *How we'll workshop this together* — the upcoming session structure
7. *What we'll need from your team* — preparation
8. *Questions to think about before our session* — primer questions
9. *Cross-references and next steps*

**Reference for tone:**
- `02_Client/05_Workshop_Pre-Reads/Category_Realignment_Customer_WhitePaper.docx` — existing Client-tone exemplar already in the library

**Open questions to surface in AskUserQuestion before building:**

1. Length — short (8-10 pages, executive summary depth) or medium (12-15 pages, working-session prep depth)?
2. Tone calibration — formal-partnership ("we recommend you consider") or warmer-partnership ("here's how we've seen this play out")?
3. Should the guide include 2-3 worked examples (de-identified) or stay entirely abstract?

---

## Branding decisions baked into the templates

Refer to `03_Shared/00_Templates_and_Branding/BRAND_STANDARD.md` for the full standard. Short version:

- US Letter docx, 1 in left/right, 0.8 in top/bottom margins
- Calibri throughout (docx); Arial throughout (xlsx workbooks)
- H1 16pt navy bold (auto-numbered when `numbered=True`); H2 13pt navy bold; H3 11.5pt accent-blue bold
- Cover: bright-teal eyebrow + 28pt navy title + deep-teal italic subtitle + teal divider line + audience/companion/doc-ID meta block
- Page header: logo + letter-spaced slate running label + teal underline
- Footer: slate org line + tab + "Page X of Y"
- docx tables: navy header (`#0B1F3A`) with white bold text, alternating row shading (`#F8FAFC`), light-gray borders (`#E2E8F0`)
- xlsx workbook banners: navy fill (`#0B1F3A`) with white bold text; cyan section headers (`#ECFEFF`); amber customer-fill cells (`#FEF3C7` bg, `#92400E` text); light-gray alt-row shading (`#F1F5F9`)
- docx callout: light-blue fill, accent-blue border, navy bold text

**Client artifacts use the same template structure** — the brand is consistent across audiences. The difference is tone (the prose) and metadata (eyebrow, audience line, confidentiality marking).

---

The blueprint catalog status field is the last column of each table row. Updates go in the JSON; the rendered Blueprint is regenerated via `build_master_blueprint.py`.
