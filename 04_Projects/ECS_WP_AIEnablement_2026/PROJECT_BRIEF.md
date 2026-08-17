# Project Brief — ECS WP AIEnablement

> Folder: `04_Projects/ECS_WP_AIEnablement_2026`
> Type: WP (internal whitepaper/guidebook) — internal practice initiative, not a client pursuit.

---

## Working Rules — How to Work in This Folder

- **This is an internal initiative project** — the deliverable set defines and governs the practice's AI enablement effort. It is not a client pursuit; no client-facing footers.
- **The guidebook is the source of truth** for the AI effort's strategy, engine definitions, collateral review program, and phased plan. Update it (bump version) when the working group changes direction — don't fork the strategy into side documents.
- **Self-contained:** all deliverables stay in this folder. Never modify OOTB collateral (00–03) from here; collateral updates identified by stage reviews are executed in the library under its own rules.
- **Branding:** `.docx` via `EcsDocument` (`ecs_template.py`). Build script co-located in `01_Internal/`.

**Session startup for this project:**
1. Read this brief, then `01_Internal/STRATEGY_NOTES.md`.
2. Read the current guidebook in `02_Deliverables/` (or its build script for fast orientation).
3. Confirm with Tim which phase/capability is active before building.

---

## Project Identity

| Field | Value |
|---|---|
| Client / Agency | ECS (internal) |
| Project Type | WP |
| Short Title | AIEnablement |
| Due Date | Rolling — phased plan (12+ months) |
| Submission Method | Internal — working group review |
| Opportunity Number | N/A |
| Primary Contact | Timothy Hislop |
| Internal Lead | Timothy Hislop |

---

## Scope Summary

Define and run the practice's AI enablement effort: consolidate the team's 13-item capability list (plus the story-validation gap) into three engines (Document Services, Shredder/obligation extraction, Reconciliation) plus a meeting-intelligence evidence stream; run just-in-time collateral reviews by role by lifecycle stage before automating each stage; and execute a phased, part-time-capacity project plan prioritized for the biggest business gap — new sales and sales pipeline.

## Key Requirements

- Consolidate team capability list → engines, not point tools (source: team list captured 2026-07-30, in `00_Source_Inputs/MANIFEST.md`)
- Leverage existing collateral library (~170 cataloged / ~150 built per `blueprint_catalog.json`) as the governed corpus seed
- Collateral review program: by role, by stage, capture → closeout, just-in-time before each phase
- Prioritize new sales / pipeline (Phase 1 entirely capture-side)
- Plan sized for 3–5 people at 4–8 hrs/week each; pause rules; 2–3 week shippable increments
- Phase 0 exit criteria include AI environment decision + one-page CUI/data-handling rule

## Deliverables

| File | Type | Status | Notes |
|---|---|---|---|
| 02_Deliverables/ECS_AI_Enablement_Guidebook_and_Project_Plan_v1.1.docx | docx | Draft | ECS-AIE-01 v1.1 — current; v1.0 superseded |
| 01_Internal/build_ai_enablement_guidebook.py | py | Current | Build script (imports 03_Shared ecs_template.py) |
| 02_Deliverables/ECS_SharePoint_Migration_Guide_v1.0.docx | docx | Draft | ECS-AIE-02 — site structure, metadata, permissions, wave plan |
| 01_Internal/build_sharepoint_migration_guide.py | py | Current | Build script for ECS-AIE-02 |
| (repo root) index.html | html | Current | Library Navigator — generated, do not hand-edit |
| 01_Internal/build_library_navigator.py | py | Current | Navigator generator — scans 00–03; `--sharepoint <base-url>` emits SharePoint-link variant after migration |
| 01_Internal/library_review_status.json | json | Current | Review scoreboard: stage status + per-artifact verdicts; edit + re-run generator |
| 02_Deliverables/ECS_Backlog_and_Enhancement_SOP_v1.0.docx | docx | Draft | ECS-AIE-04 — one intake, three backlogs, decision rights, cadence |
| 01_Internal/build_backlog_sop.py | py | Current | Build script for ECS-AIE-04 |

## Internal Notes

- Guidebook doc ID: ECS-AIE-01. Version bumps via build script edits + rebuild.
- Phase 5 deliberately converges with the Delivery Intelligence Platform app initiative (indicators surface there).
- Collateral gaps that are AI dependencies: SH-SG-03 status report, SH-SG-05 risk/issue tracker (built in Phase 4).

## Session Log

| Date | Work Done |
|---|---|
| 2026-07-30 | Project created. Capability list consolidated; collateral baseline inventoried from blueprint_catalog.json; guidebook v1.0 built with engines, review-by-role-by-stage program, gaps, and phased plan. Reframed per Tim: library = proposed baseline pending team ratification. |
| 2026-07-30 | SharePoint migration guide (ECS-AIE-02) built. Library Navigator (index.html, 236 artifacts by role/stage with review verdicts) generated at repo root; generator + review-status JSON in 01_Internal. Local links now; regenerate with --sharepoint after migration. Methodology-neutral framing: kits assembled per RFP objectives. |
| 2026-07-30 | Guidebook → v1.1: third team contribution (13 asks) incorporated — Engine 4 Practice Knowledge (§7), Builder Assistance (§9), AI CoE (§12), library gap register (§11), plan/backlog updates (Ph2: narrative drafting, LOE copilot, Ask the Library; Ph3: reqs-to-design; Ph4: builder wave; Ph5: onboarding tutor, staffing-fit). Sections renumbered; navigator + agenda refs updated. User directions now part of definition of done. |
