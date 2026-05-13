# ECS Federal — ServiceNow Practice Brand Standard

> **Single source of truth for the visual identity of every document in the practice library.**
> Canonical reference: `01_Internal/05_Discipline_How-To_Guides/ECS_Internal_Governance_Operating_Guide.docx`
> Implementation: `03_Shared/00_Templates_and_Branding/ecs_template.py` (Python helper) and `00_Master_Blueprint/assets/ECS_Internal_Document_Template.dotx` (native Word template)

---

## 1. The non-negotiable rule

Every Internal artifact in the practice library is built using `ecs_template.py`. Scripts that bypass the module and try to roll their own styling will produce inconsistent docs, and the practice's "all from the same playbook" promise to the team and the customer is broken.

If you need a primitive the module does not yet provide (e.g., a footnote helper, a two-column section, a different callout color), extend the module rather than building locally. Send the addition back for inclusion.

---

## 2. Brand constants

| Token            | Hex       | Where it appears                                                                    |
|------------------|-----------|-------------------------------------------------------------------------------------|
| Navy             | `#0B1F3A` | H1 / H2 text · Table header cell fill · Cover title · Org name on cover             |
| Bright teal      | `#14B8A6` | Cover eyebrow tag · Cover divider line · Page-header bottom border                  |
| Deep teal        | `#0D9488` | Cover subtitle italic                                                               |
| Accent blue      | `#2E74B5` | H3 text · Callout border                                                            |
| Slate            | `#475569` | Header right-side running label · Footer text · Audience / companion meta lines     |
| Body dark        | `#1A1A1A` | Body prose                                                                          |
| Alt row shading  | `#F8FAFC` | Table body alternating rows                                                         |
| Table border     | `#E2E8F0` | All table cell borders                                                              |
| Callout bg       | `#EAF1F8` | Callout box fill                                                                    |
| White            | `#FFFFFF` | Table header text                                                                   |

---

## 3. Typography

| Element       | Font    | Size  | Weight | Color        | Notes                                    |
|---------------|---------|-------|--------|--------------|------------------------------------------|
| Cover eyebrow | Calibri | 9pt   | Bold   | Bright teal  | Uppercase, letter-spaced (w:spacing 60)  |
| Cover title   | Calibri | 28pt  | Bold   | Navy         | Multi-line via `\n` in `meta.title`      |
| Cover subtitle| Calibri | 12pt  | Italic | Deep teal    | One-line tagline                         |
| H1            | Calibri | 16pt  | Bold   | Navy         | Auto-numbered when `numbered=True`       |
| H2            | Calibri | 13pt  | Bold   | Navy         |                                          |
| H3            | Calibri | 11.5pt| Bold   | Accent blue  |                                          |
| Body          | Calibri | 11pt  | Regular| Body dark    | Default `Normal` style                   |
| Bullet        | Calibri | 11pt  | Regular| Body dark    | `List Bullet` style, hanging indent      |
| Footer        | Calibri | 8pt   | Regular| Slate        | Left meta + tab + Page X of Y            |
| Running header| Calibri | 9pt   | Regular| Slate        | Letter-spaced (w:spacing 30)             |
| Table header  | Calibri | 11pt  | Bold   | White on navy| Cell margins T/B 120 L/R 160 dxa         |
| Table body    | Calibri | 10pt  | Regular| Body dark    | Cell margins T/B 100 L/R 160 dxa         |

---

## 4. Page setup

- US Letter: 8.5 in × 11 in
- Margins: 1 in left/right, 0.8 in top/bottom
- Header distance: 0.35 in
- Footer distance: 0.4 in

---

## 5. Page elements

### Running header (every page including cover)

- Left: Everforth ECS Federal logo at 1.05 in width
- Right (tab-aligned to 9360 dxa): `"Internal · {Document Title}"` letter-spaced slate
- Bottom border: Bright teal, single line, sz 8, space 1

### Footer

- Left: `"{Org} · Internal Use Only"` slate 8pt
- Right (tab-aligned to 9360 dxa): `"Page X of Y"` slate 8pt

### Cover page block (above-fold elements, top-to-bottom)

1. Two blank paragraphs of breathing space
2. Eyebrow tag in bright teal — `meta.eyebrow.upper()`
3. Title in navy bold 28pt — split on `\n` for multi-line
4. Subtitle in deep-teal italic 12pt — `meta.subtitle`
5. Bright-teal divider line (paragraph border bottom, sz 12, space 1)
6. Org name in navy bold 11pt — `meta.org`
7. `"Audience: {meta.audience}"` in slate 10pt
8. `"Companion to: {meta.companion_to}"` in slate 10pt
9. `"Document ID: X · Version: Y · Status: Z"` in slate 10pt
10. `meta.confidentiality` in slate italic 10pt

The cover page ends with a `page_break()` and the body content begins.

### Table style

- Header row marked as `tblHeader` so it repeats on page breaks
- Header cells: navy fill, white bold text, light-gray borders
- Body cells: light-gray borders, alternating rows shaded with alt-row fill (`alt_shading=True` by default)
- Cell margins generous enough for two-line wrapping

### Callout style

- Light blue fill (`Callout bg`) with accent-blue border on all four sides
- Navy bold text, 10pt Calibri

---

## 6. Section-numbering convention

`EcsDocument.h1(text, numbered=True)` auto-numbers H1 sections starting at 1. Use `numbered=False` for non-section headings like *How to Use This Guide*, *Companion Artifact Index*, and *Cross-References*. The blueprint document uses natural-language section names without numbering and passes `numbered=False` for every H1.

---

## 7. How to build a new doc

### From a Python script (the practice's default)

```python
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, ".."))  # adjust depth per file location
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

doc = EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL [DOCUMENT TYPE]",
    title="Document Title\nGoes Here",
    subtitle="One-line italic tagline",
    audience="Target audience",
    companion_to="Parent/sibling artifacts",
    doc_id="INT-XX-NN",
    version="1.0",
    status="Draft",
    running_header_label="Internal · Document Title",
))
doc.add_cover_page()
doc.page_break()
doc.h1("First Section", numbered=True)   # → "1.  First Section"
doc.h2("Sub-section")
doc.para("Body prose.")
doc.bullet("Bullet item")
doc.h3("Sub-sub heading")
doc.table(headers=["A","B"], rows=[["1","2"],["3","4"]])
doc.callout("Key principle to highlight.")
doc.save("/full/path/output.docx")
```

### From Word (for human authors)

1. Open `00_Master_Blueprint/assets/ECS_Internal_Document_Template.dotx`
2. *File* → *New from Template*
3. Replace the placeholder cover meta, then replace example sections with content
4. Save As `.docx` to the appropriate folder under `01_Internal/`, `02_Client/`, or `03_Shared/`

---

## 8. Audience tagging

Every artifact carries an audience tag in two places:
- The eyebrow tag on the cover (`INTERNAL …`, `CLIENT …`, `SHARED …`)
- The `audience:` line below the divider, naming the specific roles

Tone follows audience:
- **Internal** — operationally candid, blunt about customer pushback patterns, never circulated externally
- **Client** — partnership-oriented, never preachy, avoids framing prior choices as wrong
- **Shared** — neutral; tabs/sections within carry per-audience tone

---

## 9. Where things live

| Item                                                | Path                                                                            |
|-----------------------------------------------------|---------------------------------------------------------------------------------|
| Logo (PNG, 220×41)                                  | `00_Master_Blueprint/assets/everforth_logo.png`                                  |
| Native Word template (.dotx)                        | `00_Master_Blueprint/assets/ECS_Internal_Document_Template.dotx`                 |
| Python helper module                                | `03_Shared/00_Templates_and_Branding/ecs_template.py`                            |
| Brand standard (this doc)                           | `03_Shared/00_Templates_and_Branding/BRAND_STANDARD.md`                          |
| Master Blueprint catalog (source of truth, JSON)    | `00_Master_Blueprint/blueprint_catalog.json`                                    |
| Master Blueprint rendered view                      | `00_Master_Blueprint/ECS_OOTB_Collateral_Blueprint.docx`                        |
| Canonical reference doc (the brand exemplar)        | `01_Internal/05_Discipline_How-To_Guides/ECS_Internal_Governance_Operating_Guide.docx` |

---

## 10. Changing the brand

Brand evolution is allowed but must be intentional. To change a brand constant:
1. Update the relevant `Brand.*_HEX` value in `ecs_template.py`
2. Re-run every build script in the library (each artifact's `build_*.py`) to regenerate the .docx outputs
3. Regenerate the `.dotx` template via `python3 ecs_template.py` then patching content types (see `00_Master_Blueprint/assets/` build instructions)
4. Update this doc with the new value and the rationale

Do **not** hand-edit colors or fonts inside generated .docx files. Those edits are lost the next time the build script runs.

---

## 11. Messaging conventions

### The theme is bigger than "OOTB"

"OOTB-First" is the right discipline language for **internal** artifacts — consultant playbooks, how-to guides, trust-but-verify materials. It is blunt, intentional, and should stay that way inside the team.

For **customer-facing** artifacts — presentations, decision guides, workshop pre-reads, facilitator decks — the governing theme is **"Modernizing the Core."** The message is:

> *We are standing up a proven, AI-ready baseline implementation of ServiceNow. Any deviations from that baseline are captured in a governance triage log — they are not lost, they are managed — and addressed iteratively through a follow-on engagement once the core is stable and delivering value.*

This framing does four things at once: it scopes the current engagement cleanly, it positions deviations as governed decisions rather than gaps or failures, it sets up the follow-on contract naturally, and it connects every decision back to AI realization as the long-term goal.

### Language rules by audience

| Context | Use | Avoid |
|---------|-----|-------|
| Internal docs (playbooks, how-to guides, cheatsheets) | "OOTB-First", "OOTB approach", "customization vs. configuration" | No restriction |
| Client presentations and decks | "Modernizing the Core", "baseline implementation", "governed deviation", "triage log", "AI realization", "sustainable value" | "OOTB-First" as a headline or theme — use it in body text only when explaining the methodology |
| Workshop slide titles | "Modernizing the Core — [process area]" | "OOTB-First [process area] Workshop" |
| Decision guide titles | Keep current naming ("Decision Topic Guide: …") — the topic names are process-area specific | — |

### Canonical deck title pattern

```
Title:    Modernizing the Core
Subtitle: [Process Area] — Ensuring AI Realization and Optimizing Long-Term Value
```

Examples:
- *Modernizing the Core — Incident Management: Ensuring AI Realization and Optimizing Long-Term Value*
- *Modernizing the Core — Service Catalog: Ensuring AI Realization and Optimizing Long-Term Value*
- *Modernizing the Core — Employee Experience: Ensuring AI Realization and Optimizing Long-Term Value*

The subtitle pattern is a template, not a lock. Adjust the second clause when the specific process area warrants it (e.g., for HAM: "Establishing the Asset Foundation for AI-Driven Lifecycle Management").

### The governance triage log

Any time a customer decision deviates from the baseline, that deviation goes in the **Governance Triage Log** — a living artifact tracking the deviation, its rationale, its scope impact, and its disposition (deferred to follow-on / accepted as configuration / escalated). Client-facing materials should reference this log by name and frame it as a feature, not a safety net: it is how the engagement protects both the baseline and the customer's legitimate requirements simultaneously.

---

## 12. Presentations (.pptx)

### Overview

Every practice .pptx is built from `pptx_brand.js` — the PowerPoint equivalent of `ecs_template.py`. It provides the same brand constants, consistent slide layouts, and a factory function that returns pre-wired helpers. Scripts should never roll their own pptxgenjs calls; add to the module instead.

### Where things live

| Item | Path |
|------|------|
| Brand module | `03_Shared/00_Templates_and_Branding/pptx_brand.js` |
| Template build script | `03_Shared/00_Templates_and_Branding/build_ecs_presentation_template.js` |
| Blank starter deck (7 slides) | `03_Shared/00_Templates_and_Branding/ECS_Presentation_Template.pptx` |
| Workshop decks | `03_Shared/05_Workshop_Presentations/` |

### Brand constants (PPTX)

| Token | Hex | Where it appears |
|-------|-----|------------------|
| `NAVY` | `1E3A5F` | Cover/divider slide bg · col headers · H2 text |
| `TEAL` | `14B8A6` | Cover accent bar · closing slide CTA text |
| `TEAL_DK` | `0D9488` | Section tags · card header fills · left col header |
| `TEAL_LT` | `F0FDFA` | Info callout background |
| `WHITE` | `FFFFFF` | Header text on dark fills |
| `LT_BG` | `F7F9FC` | Card body fill |
| `SLATE` | `334155` | Body prose |
| `MID` | `64748B` | Agenda descriptors · secondary text |
| `LT_GRY` | `E2E8F0` | Dividers · card borders |

Typography: **Trebuchet MS** for all headings and display text; **Calibri** for all body, bullet, and caption text.

### How to build a new deck

```js
"use strict";
const path = require("path");
const LOGO_PATH = path.resolve(__dirname,
  "../../../00_Master_Blueprint/assets/everforth_logo.png");
const brand = require(path.resolve(__dirname, "pptx_brand"));
const {
  pres, COLORS,
  addTitleSlide, addSectionDivider, addContentSlide,
  addTwoColSlide, addDecisionSlide, addCallout, addSectionTag, addFooter, addLogo
} = brand.init({ logoPath: LOGO_PATH });

// Add slides ...
addTitleSlide("Deck Title", "Subtitle", "Italic descriptor", "Prepared by ECS Federal", 1);

// Write output
const outPath = "/absolute/path/to/output.pptx";
pres.writeFile({ fileName: outPath })
  .then(() => console.log("Written:", outPath))
  .catch(e => console.error("Error:", e));
```

Run with:
```
NODE_PATH=/usr/local/lib/node_modules_global/lib/node_modules node build_your_deck.js
```

### Available slide layouts

| Helper | Purpose |
|--------|---------|
| `addTitleSlide(title, subtitle, italicNote, footerLeft, slideNum)` | Navy cover — use as slide 1 |
| `addSectionDivider(title, subtitle, italicNote, slideNum)` | Navy full-bleed section break |
| `addContentSlide(sectionTag, headline, slideNum)` | White content slide — returns slide object for custom shapes |
| `addTwoColSlide(sectionTag, headline, leftHdr, rightHdr, leftColor, rightColor, slideNum)` | Two-column layout — returns `{ slide, leftX, rightX, leftW, rightW, contentY }` |
| `addDecisionSlide(decisionNum, question, leftContent, rightContent, defenseText, slideNum)` | OOTB-first decision frame — left = recommendation, right = customer questions |
| `addCallout(slide, boldLabel, body, style, x, y, w, h)` | Inline callout bar — style: `"info"` / `"warning"` / `"tip"` |
| `addLogo(slide)` | Places Everforth logo top-right — called automatically by all layout helpers |
| `addFooter(slide, slideNum, darkBg)` | Footer rule + text — called automatically by all layout helpers |
| `addSectionTag(slide, label)` | Small teal eyebrow tag — called automatically by layout helpers |

### Non-negotiable rules

1. All presentation build scripts import `pptx_brand.js` — never inline color constants or shape helpers.
2. The logo path must resolve at build time; pass `logoPath` explicitly if the script is not co-located with the module.
3. Slide dimensions are always LAYOUT_WIDE: **13.33 in × 7.5 in**. Do not change layout.
4. Client-facing decks: ensure the footer left label reads `"ECS Federal · ServiceNow Practice · Confidential"` (pass as `footerLabel` to `init()`).
5. After building a new deck, QA with LibreOffice: `python3 scripts/office/soffice.py <file.pptx>` then inspect pages with pdftoppm.
