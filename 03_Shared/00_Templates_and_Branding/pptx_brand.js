/**
 * pptx_brand.js
 * ECS Federal — ServiceNow Practice
 * Presentation brand module — the PPTX equivalent of ecs_template.py
 *
 * Usage:
 *   const brand = require("./pptx_brand");
 *   const { pres, COLORS, addLogo, addFooter, sectionTag,
 *           addTitleSlide, addSectionDivider, addContentSlide,
 *           addTwoColSlide, addDecisionSlide } = brand.init();
 *
 * NODE_PATH must include pptxgenjs:
 *   NODE_PATH=/usr/local/lib/node_modules_global/lib/node_modules node build_my_deck.js
 */

"use strict";
const pptxgen = require("pptxgenjs");
const fs      = require("fs");
const path    = require("path");

// ---------------------------------------------------------------------------
// Brand constants (keep in sync with BRAND_STANDARD.md)
// ---------------------------------------------------------------------------
const COLORS = {
  NAVY:      "1E3A5F",   // Primary dark — title backgrounds, section dividers
  TEAL:      "14B8A6",   // Bright accent — section tags, accent bars
  TEAL_DK:   "0D9488",   // Deep teal — column headers, OOTB boxes
  TEAL_LT:   "F0FDFA",   // Teal tint — OOTB recommendation backgrounds
  TEAL_BDR:  "CCF0EA",   // Teal border
  WHITE:     "FFFFFF",
  LT_BG:     "F7F9FC",   // Light content background
  SLATE:     "334155",   // Body text dark
  MID:       "64748B",   // Secondary text, captions
  LT_GRY:    "E2E8F0",   // Dividers, borders
  AMBER:     "F59E0B",   // Warning accent
  AMBER_LT:  "FEF3C7",   // Warning background
  AMBER_BDR: "FDE68A",   // Warning border
  RED_DK:    "B91C1C",   // Customization header
  RED_LT:    "FFF1F2",   // Customization background
  RED_BDR:   "FECDD3",   // Customization border
  BLUE_LT:   "EFF6FF",   // Info/callout background
  BLUE_BDR:  "BFDBFE",   // Info/callout border
};

// ---------------------------------------------------------------------------
// Default logo path (override by passing logoPath to init())
// ---------------------------------------------------------------------------
// Default logo path — resolved relative to THIS module's location.
// When pptx_brand.js is deployed to 03_Shared/00_Templates_and_Branding/,
// the logo lives three directories up then into 00_Master_Blueprint/assets/.
// When run from a temporary outputs folder, pass logoPath explicitly to init().
const DEFAULT_LOGO_PATH = path.resolve(
  __dirname,
  "../../../00_Master_Blueprint/assets/everforth_logo.png"
);

// ---------------------------------------------------------------------------
// init() — returns a configured pptxgen instance + all helper functions
// ---------------------------------------------------------------------------
function init({ logoPath = DEFAULT_LOGO_PATH, footerLabel = "SERVICENOW PRACTICE  ·  OOTB-FIRST APPROACH" } = {}) {

  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE"; // 13.3" x 7.5"

  // Load logo
  let logo64 = null;
  try {
    logo64 = "image/png;base64," + fs.readFileSync(logoPath).toString("base64");
  } catch (e) {
    console.warn("Brand: logo not found at", logoPath);
  }

  // ── Helpers ───────────────────────────────────────────────────────────────

  /** Add Everforth ECS logo to top-right corner */
  function addLogo(slide) {
    if (logo64) {
      slide.addImage({ data: logo64, x: 11.4, y: 0.15, w: 1.7, h: 0.58 });
    }
  }

  /**
   * Add standard footer rule + text
   * @param {object} slide
   * @param {number|null} pageNum   - slide number shown on right; pass null to omit
   * @param {boolean}     dark      - true for dark (navy) slides
   * @param {string}      label     - override centre footer text
   */
  function addFooter(slide, pageNum = null, dark = false, label = footerLabel) {
    const lc = dark ? "2A4A70" : "CBD5E1";
    const tc = dark ? "5A7A9F" : "94A3B8";
    slide.addShape(pres.shapes.LINE, { x: 0.4, y: 7.17, w: 12.5, h: 0, line: { color: lc, width: 0.5 } });
    slide.addText("Everforth ECS Federal", { x: 0.4, y: 7.22, w: 3.5, h: 0.2, fontSize: 8, color: tc });
    slide.addText(label, { x: 3.9, y: 7.22, w: 7.0, h: 0.2, fontSize: 8, color: tc, align: "center" });
    if (pageNum !== null) {
      slide.addText(String(pageNum), { x: 12.5, y: 7.22, w: 0.5, h: 0.2, fontSize: 8, color: tc, align: "right" });
    }
  }

  /** Small teal section tag (top-left eyebrow) */
  function addSectionTag(slide, label) {
    slide.addText(label, { x: 0.5, y: 0.28, w: 8, h: 0.22, fontSize: 8, bold: true, charSpacing: 3, color: COLORS.TEAL });
  }

  // ── Slide builders ────────────────────────────────────────────────────────

  /**
   * Title / cover slide (dark navy)
   * @param {string} title       - Primary title (large, white)
   * @param {string} subtitle    - Subtitle line (teal)
   * @param {string} [tagline]   - Italic descriptor line (muted blue)
   * @param {string} [preparedBy]- Bottom-left credit line
   * @param {number} [pageNum]
   */
  function addTitleSlide(title, subtitle, tagline = "", preparedBy = "Prepared by Everforth ECS Federal  ·  ServiceNow Practice  ·  Confidential", pageNum = 1) {
    const s = pres.addSlide();
    s.background = { color: COLORS.NAVY };
    addLogo(s);

    // Vertical accent bar
    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.7, w: 0.07, h: 2.4, fill: { color: COLORS.TEAL }, line: { color: COLORS.TEAL } });

    s.addText(title, { x: 0.75, y: 1.55, w: 10.5, h: 1.5, fontSize: 46, bold: true, color: COLORS.WHITE, fontFace: "Trebuchet MS" });
    s.addText(subtitle, { x: 0.75, y: 3.15, w: 10.5, h: 0.7, fontSize: 30, bold: false, color: COLORS.TEAL, fontFace: "Trebuchet MS" });

    if (tagline) {
      s.addText(tagline, { x: 0.75, y: 3.95, w: 10.5, h: 0.45, fontSize: 15, color: "9CB8D8", fontFace: "Calibri", italic: true });
    }
    s.addText(preparedBy, { x: 0.5, y: 6.85, w: 10, h: 0.28, fontSize: 9, color: "3A5A7F" });
    addFooter(s, pageNum, true);
    return s;
  }

  /**
   * Section divider slide (dark navy — used between major sections)
   * @param {string} heading    - Large white heading
   * @param {string} [sub]      - Teal supporting line
   * @param {string} [note]     - Muted italic note
   * @param {number} [pageNum]
   */
  function addSectionDivider(heading, sub = "", note = "", pageNum = null) {
    const s = pres.addSlide();
    s.background = { color: COLORS.NAVY };
    addLogo(s);

    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 2.2, w: 0.07, h: 1.8, fill: { color: COLORS.TEAL }, line: { color: COLORS.TEAL } });
    s.addText(heading, { x: 0.75, y: 2.1, w: 11, h: 1.0, fontSize: 46, bold: true, color: COLORS.WHITE, fontFace: "Trebuchet MS" });

    if (sub) {
      s.addText(sub, { x: 0.75, y: 3.15, w: 11, h: 0.7, fontSize: 22, color: COLORS.TEAL, fontFace: "Calibri" });
    }
    if (note) {
      s.addText(note, { x: 0.75, y: 3.95, w: 11, h: 0.45, fontSize: 14, color: "9CB8D8", fontFace: "Calibri", italic: true });
    }
    addFooter(s, pageNum, true);
    return s;
  }

  /**
   * Standard content slide (white background, section tag + headline)
   * Returns the slide so caller can add content below y=1.4
   * @param {string} tag       - Section eyebrow label (e.g. "THE APPROACH")
   * @param {string} headline  - Bold slide headline
   * @param {number} [pageNum]
   */
  function addContentSlide(tag, headline, pageNum = null) {
    const s = pres.addSlide();
    s.background = { color: COLORS.WHITE };
    addLogo(s);
    addSectionTag(s, tag);
    addFooter(s, pageNum, false);

    s.addText(headline, {
      x: 0.5, y: 0.55, w: 10.6, h: 0.75,
      fontSize: 26, bold: true, color: COLORS.NAVY, fontFace: "Trebuchet MS"
    });
    s.addShape(pres.shapes.LINE, { x: 0.5, y: 1.35, w: 12.3, h: 0, line: { color: COLORS.LT_GRY, width: 0.5 } });
    return s;
  }

  /**
   * Two-column content slide.
   * Returns { slide, leftY, rightY } — caller adds content starting at those y values.
   * @param {string}  tag           - Section eyebrow
   * @param {string}  headline      - Slide headline
   * @param {string}  leftHeader    - Left column header label
   * @param {string}  rightHeader   - Right column header label
   * @param {string}  leftHColor    - Left header fill (hex, no #)
   * @param {string}  rightHColor   - Right header fill (hex, no #)
   * @param {number}  [pageNum]
   */
  function addTwoColSlide(tag, headline, leftHeader, rightHeader,
    leftHColor = COLORS.TEAL_DK, rightHColor = COLORS.NAVY, pageNum = null) {

    const s = pres.addSlide();
    s.background = { color: COLORS.WHITE };
    addLogo(s);
    addSectionTag(s, tag);
    addFooter(s, pageNum, false);

    s.addText(headline, {
      x: 0.5, y: 0.55, w: 10.6, h: 0.75,
      fontSize: 24, bold: true, color: COLORS.NAVY, fontFace: "Trebuchet MS"
    });
    s.addShape(pres.shapes.LINE, { x: 0.5, y: 1.35, w: 12.3, h: 0, line: { color: COLORS.LT_GRY, width: 0.5 } });

    // Left column header
    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.45, w: 5.9, h: 0.42, fill: { color: leftHColor }, line: { color: leftHColor } });
    s.addText(leftHeader, { x: 0.5, y: 1.45, w: 5.9, h: 0.42, fontSize: 10, bold: true, color: COLORS.WHITE, align: "center", valign: "middle", margin: 0 });
    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.87, w: 5.9, h: 4.95, fill: { color: COLORS.TEAL_LT }, line: { color: COLORS.TEAL_BDR } });

    // Right column header
    s.addShape(pres.shapes.RECTANGLE, { x: 6.8, y: 1.45, w: 6.05, h: 0.42, fill: { color: rightHColor }, line: { color: rightHColor } });
    s.addText(rightHeader, { x: 6.8, y: 1.45, w: 6.05, h: 0.42, fontSize: 10, bold: true, color: COLORS.WHITE, align: "center", valign: "middle", margin: 0 });
    s.addShape(pres.shapes.RECTANGLE, { x: 6.8, y: 1.87, w: 6.05, h: 4.95, fill: { color: COLORS.LT_BG }, line: { color: COLORS.LT_GRY } });

    return { slide: s, leftX: 0.65, rightX: 6.95, leftW: 5.6, rightW: 5.75, contentY: 2.0 };
  }

  /**
   * Key Decision slide (OOTB Recommendation | Decide In The Room + amber risk bar)
   * @param {number}          num          - Decision number
   * @param {string}          question     - Bold headline question (keep under ~80 chars for single line)
   * @param {Array|string}    ootbContent  - pptxgenjs text array or plain string for left column
   * @param {Array|string}    decideContent - pptxgenjs text array or plain string for right column
   * @param {string|null}     riskNote     - Amber OOTB Defense bar text (null to omit)
   * @param {number}          pageNum
   */
  function addDecisionSlide(num, question, ootbContent, decideContent, riskNote, pageNum) {
    const s = pres.addSlide();
    s.background = { color: COLORS.WHITE };
    addLogo(s);
    addSectionTag(s, `KEY DECISION  #${num}`);
    addFooter(s, pageNum, false);

    s.addText(question, {
      x: 0.5, y: 0.55, w: 10.6, h: 0.82,
      fontSize: 21, bold: true, color: COLORS.NAVY, fontFace: "Trebuchet MS"
    });
    s.addShape(pres.shapes.LINE, { x: 0.5, y: 1.42, w: 12.3, h: 0, line: { color: COLORS.LT_GRY, width: 0.5 } });

    // OOTB column
    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.52, w: 5.9, h: 0.42, fill: { color: COLORS.TEAL_DK }, line: { color: COLORS.TEAL_DK } });
    s.addText("OOTB RECOMMENDATION", { x: 0.5, y: 1.52, w: 5.9, h: 0.42, fontSize: 10, bold: true, color: COLORS.WHITE, align: "center", valign: "middle", margin: 0 });
    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.94, w: 5.9, h: 4.0, fill: { color: COLORS.TEAL_LT }, line: { color: COLORS.TEAL_BDR } });
    s.addText(ootbContent, { x: 0.65, y: 2.04, w: 5.6, h: 3.8, fontSize: 12, color: COLORS.SLATE, fontFace: "Calibri", valign: "top" });

    // Decide column
    s.addShape(pres.shapes.RECTANGLE, { x: 6.8, y: 1.52, w: 6.05, h: 0.42, fill: { color: COLORS.NAVY }, line: { color: COLORS.NAVY } });
    s.addText("DECIDE IN THE ROOM", { x: 6.8, y: 1.52, w: 6.05, h: 0.42, fontSize: 10, bold: true, color: COLORS.WHITE, align: "center", valign: "middle", margin: 0 });
    s.addShape(pres.shapes.RECTANGLE, { x: 6.8, y: 1.94, w: 6.05, h: 4.0, fill: { color: COLORS.LT_BG }, line: { color: COLORS.LT_GRY } });
    s.addText(decideContent, { x: 6.95, y: 2.04, w: 5.75, h: 3.8, fontSize: 12, color: COLORS.SLATE, fontFace: "Calibri", valign: "top" });

    // Risk bar
    if (riskNote) {
      s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 6.08, w: 12.3, h: 0.72, fill: { color: COLORS.AMBER_LT }, line: { color: COLORS.AMBER_BDR } });
      s.addText([
        { text: "⚠  OOTB Defense:  ", options: { bold: true, color: "B45309" } },
        { text: riskNote, options: { color: "78350F" } }
      ], { x: 0.65, y: 6.13, w: 12.0, h: 0.62, fontSize: 11, fontFace: "Calibri", valign: "middle" });
    }
    return s;
  }

  /**
   * Callout / info box helper — add to any slide after creation
   * @param {object}  slide
   * @param {string}  boldLabel   - Bold prefix (e.g. "Note:")
   * @param {string}  body        - Body text
   * @param {string}  [style]     - "info" (blue), "warning" (amber), "tip" (teal)
   * @param {number}  x, y, w, h
   */
  function addCallout(slide, boldLabel, body, style = "info", x = 0.5, y = 6.0, w = 12.3, h = 0.72) {
    const styles = {
      info:    { bg: COLORS.BLUE_LT,  bdr: COLORS.BLUE_BDR,  lblColor: "1E3A8A", bodyColor: COLORS.SLATE },
      warning: { bg: COLORS.AMBER_LT, bdr: COLORS.AMBER_BDR, lblColor: "B45309", bodyColor: "78350F" },
      tip:     { bg: COLORS.TEAL_LT,  bdr: COLORS.TEAL_BDR,  lblColor: COLORS.TEAL_DK, bodyColor: COLORS.SLATE },
    };
    const st = styles[style] || styles.info;
    slide.addShape(pres.shapes.RECTANGLE, { x, y, w, h, fill: { color: st.bg }, line: { color: st.bdr } });
    slide.addText([
      { text: boldLabel + "  ", options: { bold: true, color: st.lblColor } },
      { text: body, options: { color: st.bodyColor } }
    ], { x: x + 0.15, y: y + 0.05, w: w - 0.3, h: h - 0.1, fontSize: 11, fontFace: "Calibri", valign: "middle" });
  }

  return {
    pres,
    COLORS,
    addLogo,
    addFooter,
    addSectionTag,
    addTitleSlide,
    addSectionDivider,
    addContentSlide,
    addTwoColSlide,
    addDecisionSlide,
    addCallout,
  };
}

module.exports = { init, COLORS };
