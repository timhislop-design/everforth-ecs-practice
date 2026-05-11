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
7. **CLT-DT-01 — Decision Topic Guide: Catalog Item Rationalization** (Client, 14 pages, .docx) — `02_Client/04_Decision_Topic_Guides/`
   - Build script: `build_CLT-DT-01.py`
   - Warmer-partnership tone matching the existing Category Realignment whitepaper exemplar
   - Includes 2-3 de-identified examples (Pattern A healthcare merger, Pattern B federal AI readiness, Pattern C higher-ed governance)
   - 10 sections: How to use → Why now → Signals → Four Decisions → What good looks like → Common patterns → Workshop preview → What we'll need → Questions to consider → Cross-references
   - **NEW TEMPLATE FEATURE:** `ecs_template.DocMeta` now accepts a `footer_left` override. Client artifacts pass `footer_left="ECS Federal · ServiceNow Practice  ·  Confidential"` so footers don't leak "Internal Use Only" on customer-facing docs. Default behavior unchanged for Internal artifacts.
   - Status in `blueprint_catalog.json`: **Built**

**Next up (Roadmap item #6):**

- **CLT-DT-02 — Decision Topic Guide: Category Structure Simplification** → save to `02_Client/04_Decision_Topic_Guides/`
- Same audience and tone as CLT-DT-01. The natural follow-on (catalog rationalization simplifies the items; categorization simplifies the navigation/taxonomy that sits beside it).

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

WORKED EXAMPLES BY ARTIFACT TYPE
- Internal full docx:        01_Internal/09_Trust_but_Verify_Management/build_INT-TBV-01.py
- Internal skeleton docx:    01_Internal/01_Consultant_Handbook/build_INT-CH-01.py
- JSON-driven docx:          00_Master_Blueprint/build_master_blueprint.py
- Shared Accelerator Pack:   03_Shared/01_Accelerator_Packs/SAM_Foundations_Accelerator_Pack/build_AP-06.py
- Client decision guide:     02_Client/04_Decision_Topic_Guides/build_CLT-DT-01.py  ← closest model for CLT-DT-02

NEXT ARTIFACT — CLT-DT-02 Decision Topic Guide: Category Structure Simplification
- Folder: 02_Client/04_Decision_Topic_Guides/  (co-locate with CLT-DT-01)
- Build script: build_CLT-DT-02.py
- Format: ~12-15 pages, docx, Client audience
- The natural companion to CLT-DT-01. Catalog rationalization simplifies the requestable items;
  category structure simplification rationalizes the categorization/routing taxonomy that sits beside it.
- Reference for both tone AND content depth: 02_Client/05_Workshop_Pre-Reads/Category_Realignment_Customer_WhitePaper.docx
  (NOTE: the whitepaper covers similar ground; the Decision Topic Guide should be ACTION-oriented decisions
  rather than the whitepaper's exposition. Cross-reference the whitepaper rather than duplicate it.)

SUGGESTED H1 SPINE for CLT-DT-02 (mirrors CLT-DT-01 structure):
0. How to use this guide (unnumbered)
1. Why category structure simplification matters now
2. The signals that the categorization needs work
3. The four decisions:
   - Decision 1: What is the right shape — single-level taxonomy, two-level, or N-level?
   - Decision 2: What does each level mean — categorization, identification, or routing?
   - Decision 3: How do CSDM / CMDB / Service Graph absorb what the dropdown used to carry?
   - Decision 4: How do we sustain the simplification over time?
4. What good looks like
5. Common patterns we have seen (2-3 de-identified examples)
6. How we'll workshop this together
7. What we'll need from your team
8. Questions to consider before our session
9. Cross-references and next steps (cross-link CLT-DT-01)

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
| 6 | Decision Topic Guide — Category Structure Simplification | CLT-DT-02 | `02_Client/04_Decision_Topic_Guides/` | **Next** |
| 7 | Decision Topic Guide — SLA Discipline | CLT-DT-03 | `02_Client/04_Decision_Topic_Guides/` | Pending |
| 8 | Adopt-vs-Re-engineer Cheatsheet — Catalog Item Rationalization | INT-AR-01 | `01_Internal/06_Adopt_vs_Reengineer_Cheatsheets/` | Pending |
| 9 | Event Management Foundations Accelerator Pack | AP-08 | `03_Shared/01_Accelerator_Packs/` | Pending |
| 10 | Event Management Realization Accelerator Pack | AP-09 | `03_Shared/01_Accelerator_Packs/` | Pending |
| 11 | HAM How-To Consultant Guide | INT-HT-16 | `01_Internal/05_Discipline_How-To_Guides/` | Pending |
| 12 | Sprint 1 Platform Foundation — Facilitator Guide | INT-FG-01 | `01_Internal/04_Per_Sprint_Facilitator_Guides/` | Pending |

**Roadmap progress: 5 of 12 built.**

---

## Notes for CLT-DT-02 (next session) — Decision Topic Guide: Category Structure Simplification

**Audience:** Same as CLT-DT-01: Service Owners, Catalog Owners, Process Managers, Service Desk Leadership.

**Companion to:** CLT-DT-01 (Catalog Item Rationalization) and the existing Category_Realignment_Customer_WhitePaper.docx in 02_Client/05_Workshop_Pre-Reads/.

**Key positioning:** The whitepaper explains *why* the legacy category structure got large. The Decision Topic Guide gives the customer *the four decisions to make* in the upcoming workshop. The two artifacts serve different parts of the same workflow — pair them in the workshop pre-read pack.

**Cross-link discipline:** Reference the whitepaper for background; do not duplicate its exposition. The Decision Topic Guide is action-oriented.

**Open questions to surface in AskUserQuestion before building:**

1. Length — match CLT-DT-01 at ~12-15 pages, or shorter (since whitepaper covers the why)?
2. Tone — match CLT-DT-01 warmer partnership exactly, or shift slightly more diagnostic since we have the whitepaper companion?
3. Worked examples — share the same de-identified customers from CLT-DT-01 (Pattern A healthcare, Pattern B federal, Pattern C higher-ed) for narrative continuity, or different customers for breadth?

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
