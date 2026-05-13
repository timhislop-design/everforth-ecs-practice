/**
 * build_ecs_presentation_template.js
 * Generates ECS_Presentation_Template.pptx — the blank starter deck.
 *
 * Run from the 03_Shared/00_Templates_and_Branding/ folder:
 *   NODE_PATH=/usr/local/lib/node_modules_global/lib/node_modules node build_ecs_presentation_template.js
 */
"use strict";

// When run from this file's own directory, pptx_brand.js is co-located.
// When called from elsewhere, adjust the require path accordingly.
const LOGO_PATH = "/sessions/jolly-beautiful-rubin/mnt/everforth-ecs-practice/00_Master_Blueprint/assets/everforth_logo.png";
const brand = require("./pptx_brand");
const {
  pres, COLORS,
  addTitleSlide, addSectionDivider, addContentSlide,
  addTwoColSlide, addDecisionSlide, addCallout, addSectionTag, addFooter, addLogo
} = brand.init({ logoPath: LOGO_PATH });

// ---------------------------------------------------------------------------
// SLIDE 1 — COVER (Title slide layout)
// ---------------------------------------------------------------------------
addTitleSlide(
  "Presentation Title\nGoes Here",
  "Subtitle — Workshop / Briefing / Guide",
  "One-line italic descriptor for this presentation",
  "Prepared by Everforth ECS Federal  ·  ServiceNow Practice  ·  Confidential",
  1
);

// ---------------------------------------------------------------------------
// SLIDE 2 — SECTION DIVIDER
// ---------------------------------------------------------------------------
addSectionDivider(
  "Section Title",
  "Supporting statement or transition phrase",
  "Optional italic note — set the expectation for what follows",
  2
);

// ---------------------------------------------------------------------------
// SLIDE 3 — STANDARD CONTENT SLIDE (single column)
// ---------------------------------------------------------------------------
{
  const s = addContentSlide("THE SECTION LABEL", "Slide headline goes here — one bold statement", 3);

  // Example: three-column card grid
  const cols = [
    { title: "Point One", body: "Add supporting detail here. Keep it concise — one or two sentences per card." },
    { title: "Point Two", body: "Add supporting detail here. Keep it concise — one or two sentences per card." },
    { title: "Point Three", body: "Add supporting detail here. Keep it concise — one or two sentences per card." },
  ];
  const cW = 3.9, cGap = 0.27;
  let cx = 0.5;
  for (const col of cols) {
    s.addShape(pres.shapes.RECTANGLE, { x: cx, y: 1.5, w: cW, h: 0.42, fill: { color: COLORS.TEAL_DK }, line: { color: COLORS.TEAL_DK } });
    s.addText(col.title, { x: cx, y: 1.5, w: cW, h: 0.42, fontSize: 12, bold: true, color: COLORS.WHITE, align: "center", valign: "middle", margin: 0 });
    s.addShape(pres.shapes.RECTANGLE, { x: cx, y: 1.92, w: cW, h: 4.9, fill: { color: COLORS.LT_BG }, line: { color: COLORS.LT_GRY } });
    s.addText(col.body, { x: cx + 0.15, y: 2.05, w: cW - 0.28, h: 4.6, fontSize: 13, color: COLORS.SLATE, fontFace: "Calibri", valign: "top" });
    cx += cW + cGap;
  }
}

// ---------------------------------------------------------------------------
// SLIDE 4 — TWO-COLUMN CONTENT SLIDE
// ---------------------------------------------------------------------------
{
  const { slide: s, leftX, rightX, leftW, rightW, contentY } = addTwoColSlide(
    "THE COMPARISON",
    "Slide headline — use for contrasts, before/after, configuration vs. customization",
    "LEFT COLUMN HEADER",
    "RIGHT COLUMN HEADER",
    COLORS.TEAL_DK,
    COLORS.NAVY,
    4
  );

  const leftItems = [
    "Add left-column bullet point one here",
    "Add left-column bullet point two here",
    "Add left-column bullet point three here",
    "Add left-column bullet point four here",
  ];
  const rightItems = [
    "Add right-column bullet point one here",
    "Add right-column bullet point two here",
    "Add right-column bullet point three here",
    "Add right-column bullet point four here",
  ];

  s.addText(leftItems.map((p, i) => ({
    text: p,
    options: { bullet: true, breakLine: i < leftItems.length - 1, fontSize: 13, color: COLORS.SLATE, fontFace: "Calibri", paraSpaceAfter: 8 }
  })), { x: leftX, y: contentY, w: leftW, h: 4.6, valign: "top" });

  s.addText(rightItems.map((p, i) => ({
    text: p,
    options: { bullet: true, breakLine: i < rightItems.length - 1, fontSize: 13, color: COLORS.SLATE, fontFace: "Calibri", paraSpaceAfter: 8 }
  })), { x: rightX, y: contentY, w: rightW, h: 4.6, valign: "top" });

  addCallout(s, "Note:", "Use this bar for a key takeaway, ground rule, or important qualifier.", "info");
}

// ---------------------------------------------------------------------------
// SLIDE 5 — KEY DECISION SLIDE
// ---------------------------------------------------------------------------
addDecisionSlide(
  1,
  "The decision question goes here — keep it under ~80 characters for a single line",
  [
    { text: "OOTB Recommendation header\n", options: { bold: true, color: COLORS.TEAL_DK, breakLine: true } },
    { text: "Describe the OOTB approach. Lead with what ServiceNow does out of the box. Be specific — name the field, feature, or behavior.\n\n", options: { breakLine: true } },
    { text: "Why it works:\n", options: { bold: true, color: COLORS.TEAL_DK, breakLine: true } },
    { text: "Explain the business logic behind the OOTB approach. Reference AI, upgrade continuity, or reporting impact where relevant.", options: {} },
  ],
  [
    { text: "Questions to answer:\n\n", options: { bold: true, color: COLORS.NAVY, breakLine: true } },
    { text: "1.  First question the customer must answer — make it concrete.\n\n", options: { breakLine: true } },
    { text: "2.  Second question — tie back to the OOTB recommendation.\n\n", options: { breakLine: true } },
    { text: "3.  Third question — scope, ownership, or timing.\n\n", options: { breakLine: true } },
    { text: "4.  Optional fourth question for complex decisions.", options: {} },
  ],
  "OOTB Defense text goes here — one crisp sentence explaining why the OOTB approach wins and what the cost of customizing is.",
  5
);

// ---------------------------------------------------------------------------
// SLIDE 6 — AGENDA / INDEX SLIDE
// ---------------------------------------------------------------------------
{
  const s = pres.addSlide();
  s.background = { color: COLORS.WHITE };
  addLogo(s);
  addSectionTag(s, "AGENDA");
  addFooter(s, 6, false);

  s.addText("What We'll Cover", {
    x: 0.5, y: 0.55, w: 12.3, h: 0.65, fontSize: 30, bold: true, color: COLORS.NAVY, fontFace: "Trebuchet MS"
  });
  s.addShape(pres.shapes.LINE, { x: 0.5, y: 1.25, w: 12.3, h: 0, line: { color: COLORS.LT_GRY, width: 0.5 } });

  const items = [
    ["01", "Agenda Item One", "Short descriptor — one sentence"],
    ["02", "Agenda Item Two", "Short descriptor — one sentence"],
    ["03", "Agenda Item Three", "Short descriptor — one sentence"],
    ["04", "Agenda Item Four", "Short descriptor — one sentence"],
    ["05", "Agenda Item Five", "Short descriptor — one sentence"],
    ["06", "Agenda Item Six", "Short descriptor — one sentence"],
  ];

  const leftItems  = items.slice(0, 3);
  const rightItems = items.slice(3);

  function agendaItem(slide, num, title, desc, x, y) {
    slide.addShape(pres.shapes.RECTANGLE, { x, y, w: 0.58, h: 0.58, fill: { color: COLORS.NAVY }, line: { color: COLORS.NAVY } });
    slide.addText(num, { x, y, w: 0.58, h: 0.58, fontSize: 15, bold: true, color: COLORS.WHITE, align: "center", valign: "middle", margin: 0 });
    slide.addText(title, { x: x + 0.7, y: y + 0.03, w: 5.3, h: 0.28, fontSize: 14, bold: true, color: COLORS.NAVY, fontFace: "Trebuchet MS" });
    slide.addText(desc,  { x: x + 0.7, y: y + 0.31, w: 5.3, h: 0.26, fontSize: 11, color: COLORS.MID,  fontFace: "Calibri" });
  }

  let yL = 1.42, yR = 1.42;
  for (const it of leftItems)  { agendaItem(s, it[0], it[1], it[2], 0.5, yL); yL += 1.0; }
  for (const it of rightItems) { agendaItem(s, it[0], it[1], it[2], 6.9, yR); yR += 1.0; }

  addCallout(s, "Ground rule:", "Replace placeholder items above. Keep descriptors to one sentence — the slide sets expectations, not detail.", "tip", 0.5, 6.45, 12.3, 0.55);
}

// ---------------------------------------------------------------------------
// SLIDE 7 — CLOSING SLIDE
// ---------------------------------------------------------------------------
{
  const s = pres.addSlide();
  s.background = { color: COLORS.NAVY };
  addLogo(s);

  s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 2.1, w: 0.07, h: 2.3, fill: { color: COLORS.TEAL }, line: { color: COLORS.TEAL } });
  s.addText("Questions?", { x: 0.75, y: 2.0, w: 11, h: 0.9, fontSize: 50, bold: true, color: COLORS.WHITE, fontFace: "Trebuchet MS" });
  s.addText("Next steps or call to action.", { x: 0.75, y: 2.95, w: 11, h: 0.65, fontSize: 28, color: COLORS.TEAL, fontFace: "Trebuchet MS" });

  s.addText([
    { text: "Contact your ECS Account Executive  ·  ", options: { color: "5A7A9F" } },
    { text: "servicenow@ecstech.com", options: { color: COLORS.TEAL } },
  ], { x: 0.5, y: 6.82, w: 12, h: 0.28, fontSize: 10, fontFace: "Calibri" });

  addFooter(s, 7, true);
}

// ---------------------------------------------------------------------------
// Write output
// ---------------------------------------------------------------------------
const outPath = "/sessions/jolly-beautiful-rubin/mnt/outputs/ECS_Presentation_Template.pptx";
pres.writeFile({ fileName: outPath })
  .then(() => console.log("Written:", outPath))
  .catch(e => console.error("Error:", e));
