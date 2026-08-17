# Project Brief — NIEH PP USPS Past Performance

> Folder: `NIEH_PP_USPSPastPerf_2026` · Type `PP` (Past Performance write-up) — new type code introduced 2026-07-23.

---

## Working Rules — How to Work in This Folder

> Read this first. These are the **local** rules for a bounded pursuit (Mode 2). Global rules (branding, build tooling) live in the project instructions — do not duplicate them here.

- **This is a pursuit** — a bounded response that closes when submitted/decided. Won execution work lives in `05_Clients/`.
- **This pursuit is a past performance write-up** — the deliverable is a polished USPS MTSC/PeMARS past performance narrative for use in the NIEH opportunity. No compliance matrix unless a solicitation lands in `00_Source_Inputs/`.
- **Source authority:** the client-provided instruction document in `00_Source_Inputs/` defines what content must be incorporated. Every capability listed there must appear in the final narrative.
- **Tone:** federal evaluator audience. Persuasive but factual — no claims beyond what the source text states.
- **Reference shared assets by path** from `03_Shared/00_Templates_and_Branding/` — never submit raw.
- **Self-contained:** all deliverables stay in this folder. Never modify OOTB collateral (00–03) or another project's folder.
- **Branding:** `.docx` via `EcsDocument` (`ecs_template.py`) with client-facing footer `ECS Federal · ServiceNow Practice · Confidential`.
- **Promotion path:** once Tim approves the final narrative, copy it to `03_Shared/00_Templates_and_Branding/Past_Performances/` as a reusable qual (approved by Tim 2026-07-23).

**Session startup for this pursuit:**
1. Read this `PROJECT_BRIEF.md` (esp. these Working Rules), then `01_Internal/STRATEGY_NOTES.md`.
2. Read `00_Source_Inputs/` (see `MANIFEST.md`) — the instruction doc is the authority for required content.
3. Read `03_Shared/00_Templates_and_Branding/BRAND_STANDARD.md`.
4. Confirm scope and deliverables with Tim before building.

---

## Project Identity

| Field | Value |
|---|---|
| Client / Agency | NIEH |
| Project Type | PP (Past Performance) |
| Short Title | USPS MTSC / PeMARS Past Performance |
| Due Date | TBD |
| Submission Method | TBD |
| Opportunity Number | TBD |
| Primary Contact | TBD |
| Internal Lead | Timothy Hislop |

---

## Scope Summary

Produce a polished past performance narrative describing ECS's USPS MTSC / PeMARS work (ServiceNow CMMS) for use in an NIEH opportunity. The client-provided source document contains two original paragraphs plus two lists of additional capabilities; the task is to weave the additional capabilities into the two paragraphs so the narrative reads well and shows the comprehensive solution.

---

## Key Requirements

- Incorporate all capabilities from the two supplemental lists into the first two paragraphs (source: `00_Source_Inputs/NIEH_PastPerf_Instructions.docx`)
- Preserve the factual program metrics (19 Product Lines, 23K users, 300 major sites, 33K sub-sites, 105K pieces of equipment)
- Result must read as a cohesive, comprehensive solution narrative — not a bolted-on list
- ECS-branded deliverable via `EcsDocument`, client-facing footer

---

## Shared Assets to Pull

- [x] Brand system: `ecs_template.py`, `BRAND_STANDARD.md`, `everforth_logo.png`
- [ ] Past Performance: n/a (this project *creates* one)
- [ ] Company Overview / Bios / Quals: not required for this deliverable

---

## Deliverables

| File | Type | Status | Notes |
|---|---|---|---|
| `02_Deliverables/USPS_PeMARS_Past_Performance.docx` | docx | Draft | ECS-branded narrative |
| `02_Deliverables/USPS_PeMARS_Past_Performance.md` | md | Draft | Plain-text narrative for copy/paste into proposal volumes |

---

## Internal Notes

- Type code `PP` introduced with this project for past performance write-ups.
- On approval, promote the narrative to `03_Shared/00_Templates_and_Branding/Past_Performances/`.

---

## Session Log

| Date | Work Done |
|---|---|
| 2026-07-23 | Project created; narrative drafted incorporating supplemental capabilities; branded docx built |
