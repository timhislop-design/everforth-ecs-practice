# HOWTO — Operating the Workspace

Quick reference for (A) keeping the project instructions in sync and (B) starting new work on the right footing. Keep this at the repo root.

---

## A. Sync the Project Instructions (do this whenever the structure changes)

`PROJECT_INSTRUCTIONS_DRAFT.md` is the **source file**, but Cowork does **not** auto-load it. The live instructions are whatever is pasted into Project Settings. After any structural change, re-sync:

1. Open `PROJECT_INSTRUCTIONS_DRAFT.md` (repo root).
2. Select everything **between** the `--- COPY FROM HERE ---` and `--- END COPY ---` markers (do **not** include the marker lines themselves).
3. Copy it.
4. In the Cowork desktop app: open this project → its **settings / "Edit project"** → the **Instructions** field. (Exact label may vary by version — it's the project-level instructions box, not a chat message.)
5. **Select all** in that field, delete, and paste the new text. Save.
6. Start a **fresh session** — instruction changes apply to new sessions, not the one already open.

> Rule of thumb: if we add a folder, mode, template, or naming rule, re-sync before the next working session.

---

## B. Kickoff Prompts — paste one of these to start new work

Paste the matching prompt as your **first message** in a new session, fill in the brackets, and attach/drop the source doc. It puts the session in the right mode and template from the first move.

### B1 — New Pursuit (RFX / SOO / WP / SOW / Review) → `04_Projects/`

```
New pursuit. This is Mode 2 (a bounded pursuit in 04_Projects/), NOT a client engagement.

Client/Agency: [CLIENT]
Type: [RFX | SOW | PWS | WP | REVIEW]
Short title: [SHORT TITLE]
Due date: [DATE]
The originating doc (SOO / RFP / client ask) is: [attached | at <path>]

Do this:
1. Copy 04_Projects/_TEMPLATE/ and rename it [CLIENT]_[TYPE]_[ShortTitle]_[YYYY].
2. Put the originating doc in that folder's 00_Source_Inputs/ and log it in its MANIFEST.md.
3. Read the new PROJECT_BRIEF.md Working Rules, then 00_Source_Inputs/, then BRAND_STANDARD.md.
4. Build a compliance/shred matrix from the source doc.
5. Use folders 00–03 as the modeling source — reference shared assets by path, never copy them in.
6. Confirm scope, win themes, and deliverables with me BEFORE building anything.
```

### B2 — New Client Engagement (post-win) → `05_Clients/`

```
New client engagement — we won the work. This is Mode 3 (active execution in 05_Clients/), NOT a pursuit.

Client: [CLIENT]
Short title / scope: [SHORT TITLE]
In-scope ServiceNow modules: [MODULES]
Originating/awarded docs (signed SOW, SOO/RFP, baseline sales docs) are: [attached | at <path>]
Originating pursuit folder (if any): [04_Projects/...]

Do this:
1. Copy 05_Clients/_TEMPLATE/ and rename it to the client name.
2. Put the SOW + originating docs in that folder's 00_Source_Inputs/ and log them in its MANIFEST.md.
3. Read the new ENGAGEMENT_BRIEF.md Working Rules, then 00_Source_Inputs/, then ONBOARDING_MAP.md, then BRAND_STANDARD.md.
4. Use folders 00–03 as the modeling source — curate, don't copy. Distill by role for the team, right-size for the client.
5. Default to the client-facing footer; internal footer only for 03_Internal/ and 01_Onboarding/Internal_Team/.
6. Confirm scope, team roles, and the first deliverable with me BEFORE building anything.
```

### B3 — Convert a won Pursuit into an Engagement (handoff)

```
We won [04_Projects/<pursuit folder>]. Stand up the client engagement and carry the context forward.

Do this:
1. Create 05_Clients/[Client]/ from 05_Clients/_TEMPLATE/.
2. Copy the originating source docs + our winning response + signed SOW from the pursuit's
   00_Source_Inputs/ and deliverables into the engagement's 00_Source_Inputs/; log them in MANIFEST.md.
3. Note the originating pursuit folder in ENGAGEMENT_BRIEF.md.
4. Leave the pursuit folder closed in 04_Projects/ as the historical record.
5. Then confirm scope and the first engagement deliverable with me before building.
```

---

## C. End-of-Session Habit

Ask for the daily log (Updated / Added / Pending), save it, and — after structural changes — re-run Section A.
