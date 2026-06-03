# Everforth ECS — Project Instructions (Cowork)
> This file is the source of truth for the Cowork project instruction text.
> Copy the content between the dashed lines into Cowork > Project Settings > Instructions.

---
COPY FROM HERE
---

## Who You Are Working With

Timothy Hislop — ServiceNow Senior Director of Deliverey Services at Everforth ECS Federal. Tim leads a practice built around an OOTB-first approach to ServiceNow delivery, AI realization, and long-term technical debt elimination. He operates as both a delivery leader and a business developer — building practice collateral, responding to federal opportunities, and managing multiple concurrent workstreams.

---

## Workspace Structure

This workspace (`everforth-ecs-practice`) contains two categories of work. Always identify which mode applies before starting any task.

```
00_Master_Blueprint/          OOTB north star — source of truth for practice collateral
01_Internal/                  OOTB consultant-only artifacts
02_Client/                    OOTB client-facing artifacts
03_Shared/                    OOTB shared artifacts + THE shared asset hub for ALL work
  └── 00_Templates_and_Branding/
        ├── BRAND_STANDARD.md
        ├── ECS_Presentation_Template.pptx
        ├── ecs_template.py / pptx_brand.js
        ├── Past_Performances/     PPQs, CPARS, project summaries
        ├── Boilerplate_Content/   Company overview, bios, differentiators
        └── Company_Quals/         CAGE, UEI, NAICS, certifications
04_Projects/                  All mini-projects (RFX, SOW, PWS, whitepapers, reviews)
  └── _TEMPLATE/              Starter scaffold — copy and rename for each new project
```

---

## Mode 1 — OOTB Practice Library (folders 00–03)

The primary long-running workstream. Produces a complete consultant + client collateral library for the ECS Federal ServiceNow practice across an 18-week delivery framework.

**Session startup for OOTB work — read in this order:**
1. `PROJECT_STATUS.md` — orientation and build status
2. `00_Master_Blueprint/NEXT_SESSION_PROMPT.md` — active artifact and pickup prompt
3. `00_Master_Blueprint/blueprint_catalog.json` — build status source of truth
4. `03_Shared/00_Templates_and_Branding/BRAND_STANDARD.md` — brand rules

Then confirm with Tim what we're building before starting.

**Sprint schedule authority:** The 18-week engagement runs Sprint 0 + Sprints 1–6 + Hypercare, grouped into three monthly phases. All collateral that references sprint cadence must follow the schedule in memory.

**Non-negotiable build rules:**
- Every `.docx` → built via `EcsDocument` from `ecs_template.py` — never roll custom styling
- Every `.pptx` → built via `pptx_brand.js` using `brand.init()` — never inline color constants
- Every accelerator pack workbook → `accelerator_pack_builder.TabContent + build_workbook()`
- Client-facing footer: `"ECS Federal · ServiceNow Practice · Confidential"`
- Internal footer: `"Internal Use Only"` (default — never let this leak on client docs)
- After each artifact: update `blueprint_catalog.json` → re-run `build_master_blueprint.py` → update `PROJECT_STATUS.md` and `NEXT_SESSION_PROMPT.md`

---

## Mode 2 — Mini-Projects (folder 04_Projects/)

Discrete, bounded engagements: RFX responses, SOWs, PWS documents, whitepapers, proposal reviews, and project plans. Each mini-project lives in its own named subfolder. They are self-contained — they never modify OOTB collateral.

**Folder naming convention — client first:**
`[CLIENT]_[TYPE]_[ShortTitle]_[YYYY]`

Types: `RFX` | `SOW` | `PWS` | `WP` (whitepaper) | `REVIEW`

Examples:
- `DHS_RFX_CyberSOC_2026`
- `VA_SOW_ITSMModernization_2026`
- `DOD_PWS_ServiceDeskOps_2026`
- `DISA_REVIEW_IncidentRFP_2026`

**Starting a new mini-project:**
1. Copy `04_Projects/_TEMPLATE/` and rename using the convention above
2. Fill in `PROJECT_BRIEF.md` — client, type, due date, scope, shared assets needed
3. All deliverables stay inside that project's subfolder
4. Never save mini-project output into folders 01, 02, or 03

**Session startup for mini-project work:**
1. Read `04_Projects/[PROJECT_FOLDER]/PROJECT_BRIEF.md`
2. Read any referenced shared assets from `03_Shared/00_Templates_and_Branding/`
3. Confirm scope and deliverables with Tim before building

---

## Shared Assets — Single Source of Truth

`03_Shared/00_Templates_and_Branding/` is the hub for all reusable content across both modes.

| Subfolder | Contents | How to Use |
|---|---|---|
| `Past_Performances/` | PPQs, CPARS, project summaries | Reference by path; adapt for each RFX — never submit raw |
| `Boilerplate_Content/` | Company overview, team bios, differentiators | Pull relevant sections; adapt framing to the opportunity |
| `Company_Quals/` | CAGE, UEI, NAICS, certs, contract vehicles | Reference directly — do not maintain per-project copies |

**Rule:** Reference shared assets by path. Do not copy template files or boilerplate into a project folder. Keep content current in one place.

---

## Content Reuse Between Projects

When a mini-project needs content similar to an existing OOTB artifact (e.g., a SOW that references HAM scope, or an RFX that needs the accelerator pack summary), reference the OOTB document as source material — summarize or adapt, and note the source file in the project's `PROJECT_BRIEF.md`. Do not copy-paste between projects.

When two mini-projects cover similar ground (e.g., two RFX responses for similar scopes), extract the reusable content into `Boilerplate_Content/` rather than duplicating across project folders.

---

## Branding — Non-Negotiable for All Output

Read `03_Shared/00_Templates_and_Branding/BRAND_STANDARD.md` before producing any document in any mode. The brand system applies to all work in this workspace regardless of whether it is OOTB collateral or a mini-project deliverable.

---

## Daily Log — End of Every Session

At the end of every session, generate a log entry in this format:

```
[Date] — Updated: [files changed]
         Added: [new files]
         Pending: [work in progress]
```

If multiple documents were updated, list each separately. Always prompt Tim to copy and save the log before closing the thread.

---
END COPY
---
