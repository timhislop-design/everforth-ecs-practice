# Project Brief — Unisys / Electric Boat — RUNBOOK — System Administration Checklist

> RUNBOOK is a new operational-deliverable type (outside the standard RFX/SOW/PWS/WP/REVIEW pursuit types) for recurring ops artifacts. Confirmed with Tim 2026-07-01.

| Field | Value |
|---|---|
| Client / Agency | Electric Boat (General Dynamics subsidiary) |
| Prime Contractor | Unisys |
| ECS Role | Subcontractor / ServiceNow Architecture & Operations |
| Project Type | RUNBOOK — recurring operational checklist |
| Short Title | System Administration Checklist |
| Due Date | TBD |
| Opportunity Number | N/A (delivery/ops artifact) |
| Internal Lead | Timothy Hislop |
| Status | In Progress — 2026-07-01 |

---

## Scope Summary

A proactive ServiceNow system administration checklist for the ECS admin team supporting the Electric Boat / Unisys ServiceNow platform. Structured as **daily** and **weekly** routine tasks sized to justify roughly 1–2 hours of admin work per day. For each check the workbook states what to verify, how to tell if it's healthy, and — if an issue is found — the next steps to investigate/remediate (e.g., replication down → how to restart it). Grounded in the ServiceNow Yokohama Platform Administration documentation.

---

## Key Requirements

- Daily + weekly cadence; keep it lean — target ~1–2 hrs/day of effort, not exhaustive.
- Cover, at minimum: **replication / MID Server / integrations health** (verify running, restart steps if down), **system logs** (errors, warnings, node health), **instance performance** (response time, slow transactions, semaphore/DB pool), scheduled jobs, and storage/table growth.
- Each row: check → what "healthy" looks like → next steps if a problem is found.
- Client-facing artifact — footer: `ECS Federal · ServiceNow Practice · Confidential`.
- Source authority: `00_Source_Inputs/servicenow-yokohama-platform-administration-enus.pdf`.

---

## Shared Assets to Pull

- [ ] Company Overview — federal version (only if a cover/context tab is wanted)
- [x] Core Differentiators: OOTB-First Methodology, ServiceNow Expertise Depth (frame the proactive-maintenance discipline)
- [ ] Past Performance / Quals — N/A for an internal-facing ops runbook

---

## Deliverables

| File | Type | Status | Notes |
|---|---|---|---|
| Unisys_ElectricBoat_SysAdmin_Checklist_2026.xlsx | xlsx | ✅ Built 2026-07-01 | 3 tabs (How to Use, Daily=8 checks, Weekly=10 checks). Columns: Done (☐/✓/Issue/N/A dropdown) · Area · Check · Where to Look · Healthy Looks Like · Next Steps · Est. Time · Notes. ECS brand colors; Confidential footer. Grounded in Yokohama Platform Admin (Maintaining & Monitoring section). |

---

## Internal Notes

- **Format confirmed (2026-07-01):** Excel workbook (.xlsx) — checkable spreadsheet, daily/weekly tabs with checkbox + task + verify + escalation/next-steps columns.
- **Audience confirmed (2026-07-01):** Client-facing / shared with Unisys + Electric Boat → Confidential footer.
- Electric Boat = GD submarine/defense shipbuilding subsidiary; federal defense context. Unisys is prime, ECS subcontractor.
- **Build blocked:** Cowork Linux sandbox down (HCS 0x80070005). xlsx build + moving the source PDF into this folder are pending the env fix — see repo `COWORK_ENV_TROUBLESHOOTING.md`.
- Related EB project: `04_Projects/Unisys_ElectricBoat_SOW_SNArchitecture_2026`.

---

## Session Log

| Date | Work Done |
|---|---|
| 2026-07-01 | Project scaffolded; format (xlsx) + audience (client-facing) confirmed; source PDF present in _TEMPLATE/00_Source_Inputs (to be moved here). xlsx build deferred pending Cowork env fix. |
| 2026-07-01 | Cowork env restored. Built `Unisys_ElectricBoat_SysAdmin_Checklist_2026.xlsx` — Daily (8) + Weekly (10) checks with How-to-Use tab, grounded in Yokohama Platform Admin. Verified render via LibreOffice. Source PDF still in _TEMPLATE/00_Source_Inputs (move still pending). |
