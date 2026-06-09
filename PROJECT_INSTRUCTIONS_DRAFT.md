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

This workspace (`everforth-ecs-practice`) contains three categories of work. Always identify which mode applies before starting any task.

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
04_Projects/                  Mode 2 — pursuits (RFX, SOW, PWS, whitepapers, reviews)
  └── _TEMPLATE/              Starter scaffold — copy and rename for each new pursuit
05_Clients/                   Mode 3 — won work we execute (active client engagements)
  └── _TEMPLATE/              Starter scaffold — copy and rename for each new engagement
```

**The three modes, at a glance:**

| Mode | Folders | Nature | Lifespan |
|---|---|---|---|
| 1 — OOTB Practice Library | 00–03 | The reusable collateral we build *from* | Long-running |
| 2 — Pursuits | `04_Projects/` | RFX/SOW/PWS/WP/REVIEW — "we're going after this" | Bounded; closes when submitted/decided |
| 3 — Client Engagements | `05_Clients/` | "we won and have to execute" | Long-running; grows across the engagement |

**Per-folder Working Rules:** every `04_Projects/` and `05_Clients/` subfolder carries its own `PROJECT_BRIEF.md` / `ENGAGEMENT_BRIEF.md` with a **Working Rules** section at the top. That section is the local source of truth for working in that folder — read it first. These instructions hold only the shared rules; the per-folder briefs hold the specifics.

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
2. Drop the originating source doc into `00_Source_Inputs/` — the government Statement of Objectives (SOO), RFP/solicitation, or the client-specific starting doc — and log it in that folder's `MANIFEST.md`
3. Fill in `PROJECT_BRIEF.md` — client, type, due date, scope, shared assets needed
4. All deliverables stay inside that project's subfolder
5. Never save mini-project output into folders 01, 02, or 03

**Session startup for mini-project work:**
1. Read `04_Projects/[PROJECT_FOLDER]/PROJECT_BRIEF.md` — start with its **Working Rules** section
2. Read `00_Source_Inputs/` — the solicitation/SOO and customer source docs that seed the response
3. Read any referenced shared assets from `03_Shared/00_Templates_and_Branding/`
4. Confirm scope and deliverables with Tim before building

> **The originating doc is the seed.** Every pursuit starts from what the customer puts out — a SOO, RFP, or a doc they hand us. That goes in `00_Source_Inputs/`; folders 00–03 are the modeling source we build the response *from*.

---

## Mode 3 — Client Engagements (folder 05_Clients/)

Won work we are now executing — long-running active engagements. The delivery counterpart to Mode 2 pursuits. Each engagement lives in its own subfolder and **grows across the engagement lifecycle**; it does not modify OOTB collateral.

**Folder naming:** client first — `[Client]/` (or `[Client]_[ShortTitle]/` if a client has more than one engagement).

**Engagement folder structure** (from `05_Clients/_TEMPLATE/`):

```
05_Clients/[Client]/
  ENGAGEMENT_BRIEF.md        Single source of truth + Working Rules
  00_Source_Inputs/          Context hub — SOW, sales docs, client docs to build from (see MANIFEST.md)
  01_Onboarding/             The onboarding package + ONBOARDING_MAP.md
    Internal_Team/             Consultant-facing (internal footer)
    Client_Facing/             Client-facing (confidential footer)
  02_Delivery/               Live delivery docs accumulated as the engagement runs
  03_Internal/               Strategy, decisions, notes — never client-facing
```

**Core principle — curate, don't copy.** The OOTB library is comprehensive; an engagement uses a curated subset, distilled by role for the team and right-sized for the client. Never dump the full library on either audience. The per-engagement `ONBOARDING_MAP.md` defines the role-based and client cuts.

**Starting a new engagement:**
1. Copy `05_Clients/_TEMPLATE/` and rename to the client name
2. Drop the originating/awarded docs into `00_Source_Inputs/` — signed SOW, the SOO/RFP, baseline sales docs, and client-provided material — and log them in its `MANIFEST.md`
3. Fill in `ENGAGEMENT_BRIEF.md` — client, scope, in-scope modules, shared assets, team
4. All work stays inside the engagement folder — never save into folders 00–04

**Session startup for engagement work:**
1. Read `05_Clients/[Client]/ENGAGEMENT_BRIEF.md` — start with its **Working Rules** section
2. Read `00_Source_Inputs/` — SOW, sales docs, and client docs that ground the engagement
3. Read `01_Onboarding/ONBOARDING_MAP.md` for the curation/role plan
4. Read referenced shared assets from `03_Shared/00_Templates_and_Branding/`
5. Confirm scope and the next deliverable with Tim before building

**Footers:** default to client-facing (`ECS Federal · ServiceNow Practice · Confidential`); use the internal footer only for `03_Internal/` and `01_Onboarding/Internal_Team/` docs.

**Pursuit → Engagement handoff (when we win):** when a `04_Projects/` pursuit converts to won work, stand up the `05_Clients/[Client]/` engagement and carry its context forward — copy the originating source docs (SOO/RFP + our winning response) and the signed SOW into the engagement's `00_Source_Inputs/`, and note the originating pursuit folder in `ENGAGEMENT_BRIEF.md`. The pursuit folder stays closed in `04_Projects/` as the historical record.

---

## Shared Assets — Single Source of Truth

`03_Shared/00_Templates_and_Branding/` is the hub for all reusable content across all three modes.

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
