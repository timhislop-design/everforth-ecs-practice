# Everforth ECS Federal - ServiceNow Practice

This repository is the working framework for the ECS Federal ServiceNow delivery
practice: an OOTB-first collateral library plus live client engagements.

It is the **ECS team's source-of-truth and audit baseline.** It contains the build
scripts (`.py` / `.js`), data, and source inputs behind every artifact. The
client-facing, code-free copy for SharePoint lives under `06_Client_Upload/`.

---

## Start here

**Running a Connection delivery role?** Open the execution navigator and pick your role:

- `06_Client_Upload/Connection/00_START_HERE/Connection_Execution_Navigator.html`
  - Pick your role (ECS or client) and the current phase; it shows only the
    artifacts that are yours, right now, with click-through links.
- `06_Client_Upload/Connection/00_START_HERE/Connection_Execution_Guide.docx`
  - The same role + phase guidance in document form.
- `06_Client_Upload/Connection/00_START_HERE/Connection_Library_Index.xlsx`
  - The full catalog of every artifact in the static library.

**Want the full engagement context?**

- `05_Clients/Connection/ENGAGEMENT_BRIEF.md` - single source of truth: scope,
  deliverables, status, and session log for the Connection engagement.

---

## Workspace structure

| Folder | What it holds |
|---|---|
| `00_Master_Blueprint/` | OOTB north star - the practice collateral source of truth |
| `01_Internal/` | OOTB consultant-only artifacts |
| `02_Client/` | OOTB client-facing artifacts |
| `03_Shared/` | OOTB shared artifacts + the shared asset hub (branding, templates, past performance, quals) |
| `04_Projects/` | Pursuits - RFX responses, SOWs, PWS, whitepapers, reviews (pre-win) |
| `05_Clients/` | Won engagements under execution (e.g. `Connection/`) - the live working framework |
| `06_Client_Upload/` | Static, code-free copies for SharePoint - artifacts only, regenerated from 05 |

---

## Two audiences, two channels

- **ECS delivery team** lives in this GitHub repo - they get the full framework,
  including the build scripts and audit baseline.
- **Clients and the broader audience** get the static library in `06_Client_Upload/`
  (no `.py`, `.json`, or source inputs), published to SharePoint. The navigator HTML
  is the front door.

The static library is **generated, not hand-maintained.** To refresh it after editing
artifacts in `05_Clients/Connection/`, re-run the export trigger:

```
python 05_Clients/Connection/_tools/export_execution_library.py
```

That mirrors the finalized artifacts into `06_Client_Upload/Connection/`, rebuilds the
library index and the navigator, and re-zips the upload package.

---

## Build rules (non-negotiable)

- Every `.docx` is built via `EcsDocument` (`03_Shared/00_Templates_and_Branding/ecs_template.py`).
- Every `.pptx` is built via `pptx_brand.js` using `brand.init()`.
- Client-facing footer: `ECS Federal - ServiceNow Practice - Confidential`.
- Internal footer: `Internal Use Only`.
- Brand rules live in `03_Shared/00_Templates_and_Branding/BRAND_STANDARD.md` - read before producing any document.
