# 05_Clients — Active Execution Engagements

This folder holds **won work we are now executing** — one subfolder per client engagement. It is the delivery counterpart to `04_Projects/`.

## How this differs from 04_Projects

| | `04_Projects/` | `05_Clients/` |
|---|---|---|
| Nature | **Pursuits** | **Execution** |
| Examples | RFX responses, whitepapers, SOWs, PWS, proposal reviews | Active engagements where we won and are delivering |
| Lifespan | Bounded — closes when submitted/decided | Long-running — grows across the engagement lifecycle |
| Trigger | "We are going after this" | "We won something and have to execute" |

## Structure of a client engagement folder

```
05_Clients/
  _TEMPLATE/                 Copy + rename to start a new engagement
  [Client]/
    ENGAGEMENT_BRIEF.md        Single source of truth + Working Rules
    00_Source_Inputs/          Context hub — drop the SOW, sales docs, client docs here
    01_Onboarding/             The delivery onboarding package + ONBOARDING_MAP.md
      Internal_Team/             Consultant-facing onboarding
      Client_Facing/             Client-facing onboarding
    02_Delivery/               Live delivery docs accumulated as the engagement runs
    03_Internal/               Strategy, decisions, notes (never client-facing)
```

## Rules

- **Reference shared assets by path** from `03_Shared/00_Templates_and_Branding/` — do not copy boilerplate, past performance, or quals into a client folder.
- **Branding is non-negotiable.** Read `03_Shared/00_Templates_and_Branding/BRAND_STANDARD.md` before producing any document. `.docx` via `EcsDocument`, `.pptx` via `pptx_brand.js`.
- **Footers:** client-facing → `ECS Federal · ServiceNow Practice · Confidential`; internal → `Internal Use Only`.
- Keep all engagement work inside its client subfolder. Do not write into folders 00–04.

## Current engagements

| Client | Status | Started |
|---|---|---|
| Connection | Onboarding | 2026-06-09 |
