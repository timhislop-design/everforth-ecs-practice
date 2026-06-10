/**
 * Connection - Project Kickoff Deck (client-facing). Theme: Modernizing the Core.
 * Built via pptx_brand.js brand.init(). Visual pass: timeline, KPI tiles, scope cards, diagrams.
 * Source is pure ASCII.
 */
"use strict";
const path = require("path");
const REPO = "/sessions/eager-epic-davinci/mnt/everforth-ecs-practice";
const brand = require(path.join(REPO, "03_Shared/00_Templates_and_Branding/pptx_brand.js"));
const LOGO = path.join(REPO, "00_Master_Blueprint/assets/everforth_logo.png");
const OUT = path.join(REPO, "05_Clients/Connection/01_Onboarding/Client_Facing/Connection_Kickoff_Deck.pptx");

const { pres, COLORS, addContentSlide, addSectionDivider, addTitleSlide, addTwoColSlide, addCallout } =
  brand.init({ logoPath: LOGO, footerLabel: "MODERNIZING THE CORE   |   CONNECTION   |   CONFIDENTIAL" });

const RR = pres.shapes.ROUNDED_RECTANGLE, RECT = pres.shapes.RECTANGLE,
      ARR = pres.shapes.RIGHT_ARROW, DIA = pres.shapes.DIAMOND, LINE = pres.shapes.LINE;
const TR = "Trebuchet MS", CA = "Calibri";
const bodyBox = (x, y, w, h) => ({ x, y, w, h, fontSize: 14, color: COLORS.SLATE, fontFace: CA, valign: "top", lineSpacingMultiple: 1.06 });
const B = (t, opt = {}) => ({ text: t, options: { bullet: { indent: 14 }, paraSpaceAfter: 8, ...opt } });
let pg = 1;

addTitleSlide("Modernizing the Core", "Connection + ECS  -  Project Kickoff",
  "An 18-week, OOTB-first ServiceNow reimplementation - a clean, AI-ready platform, delivered together.",
  "Prepared by Everforth ECS Federal   |   ServiceNow Practice   |   Confidential", pg++);

let s = addContentSlide("TODAY", "Kickoff Agenda", pg++);
s.addText([
  B("Why we're here - the goal and the outcomes"),
  B("What Phase 1 delivers"),
  B("The 18-week journey"),
  B("How we work: the OOTB-First approach"),
  B("Who does what - roles and accountability"),
  B("How we keep on track - governance and checks"),
  B("What we need from you, and your first two weeks"),
], bodyBox(0.6, 1.6, 11.8, 5.2));

s = addContentSlide("THE GOAL", "Why We're Here", pg++);
s.addText([
  B("Exit the domain-separated shared instance - move to a modern, governed, dedicated platform."),
  B("Stand up a proven, OOTB-aligned baseline that is upgrade-friendly and ready for AI."),
  B("Establish a healthy, CSDM-aligned CMDB - the foundation for change risk scoring and clean data."),
  B("Deliver a modern Employee Center that deflects tickets and helps employees self-serve."),
  B("Track real operational gains from day one."),
], bodyBox(0.6, 1.6, 11.8, 4.3));
addCallout(s, "The theme:", "We modernize the core first, then improve from there. Deviations are managed - never lost.", "tip");

s = addContentSlide("OUTCOMES", "What Success Looks Like", pg++);
const tiles = [["MTTR","Faster mean time to resolution"],["SLA","Higher SLA attainment"],["CHANGE","Higher change success rate"],["DEFLECTION","More tickets self-served"]];
tiles.forEach((t, i) => {
  const x = 0.5 + i * 3.1;
  s.addShape(RR, { x, y: 1.7, w: 2.88, h: 1.95, fill: { color: COLORS.LT_BG }, line: { color: COLORS.LT_GRY }, rectRadius: 0.08 });
  s.addShape(RECT, { x, y: 1.7, w: 2.88, h: 0.12, fill: { color: COLORS.TEAL }, line: { color: COLORS.TEAL } });
  s.addText(t[0], { x, y: 2.05, w: 2.88, h: 0.7, fontSize: 28, bold: true, color: COLORS.TEAL_DK, align: "center", fontFace: TR });
  s.addText(t[1], { x: x + 0.15, y: 2.85, w: 2.58, h: 0.7, fontSize: 11.5, color: COLORS.SLATE, align: "center", fontFace: CA, valign: "top" });
});
s.addText("Tracked transparently in Platform Analytics from day one.", { x: 0.5, y: 3.78, w: 12.3, h: 0.3, fontSize: 11, italic: true, color: COLORS.MID, align: "center", fontFace: CA });
const chips = ["Exit domain separation","AI-ready foundation","Clean CSDM CMDB","Modern Employee Center"];
chips.forEach((c, i) => {
  const x = 0.5 + i * 3.1;
  s.addShape(RR, { x, y: 4.25, w: 2.88, h: 0.62, fill: { color: COLORS.TEAL_LT }, line: { color: COLORS.TEAL_BDR }, rectRadius: 0.1 });
  s.addText(c, { x, y: 4.25, w: 2.88, h: 0.62, fontSize: 11.5, bold: true, color: COLORS.TEAL_DK, align: "center", valign: "middle", fontFace: CA });
});

addSectionDivider("The 18-Week Journey", "Two-week sprints  |  four stages  |  Go-Live at Week 16", "", pg++);

s = addContentSlide("THE PLAN", "Four Stages, Eight Sprints", pg++);
const stages = [
  { x: 0.5,  w: 4.1,  c: COLORS.TEAL_DK, n: "STAGE 1", t: "Initiate & Plan", sp: "Sprints 0-2", wk: "Weeks 1-6",   f: "Governance, greenfield stand-up, CSDM data foundation" },
  { x: 4.65, w: 4.1,  c: COLORS.TEAL,    n: "STAGE 2", t: "Execute",         sp: "Sprints 3-5", wk: "Weeks 7-12",  f: "ITSM Core & Change/CAB; Employee Center, VA & Knowledge" },
  { x: 8.8,  w: 2.55, c: COLORS.NAVY,    n: "STAGE 3", t: "Deliver",         sp: "Sprints 6-7", wk: "Weeks 13-16", f: "HAM, analytics, SIT/UAT, governed cutover" },
  { x: 11.5, w: 1.3,  c: COLORS.SLATE,   n: "STAGE 4", t: "Close",           sp: "Sprint 8",    wk: "Weeks 17-18", f: "Hypercare, KT, roadmap" },
];
const bandY = 2.6, bandH = 1.7;
stages.forEach(st => {
  s.addShape(RR, { x: st.x, y: bandY, w: st.w, h: bandH, fill: { color: st.c }, line: { color: st.c }, rectRadius: 0.06 });
  s.addText([
    { text: st.n + "\n", options: { fontSize: 10, bold: true, color: "BFE6E0", charSpacing: 2 } },
    { text: st.t + "\n", options: { fontSize: 14, bold: true, color: COLORS.WHITE } },
    { text: st.sp + "\n", options: { fontSize: 10.5, color: COLORS.WHITE } },
    { text: st.wk, options: { fontSize: 10.5, color: "D6E4F0" } },
  ], { x: st.x + 0.1, y: bandY + 0.12, w: st.w - 0.2, h: bandH - 0.2, align: "center", valign: "middle", fontFace: CA, lineSpacingMultiple: 1.05 });
  s.addText(st.f, { x: st.x, y: bandY + bandH + 0.08, w: st.w, h: 0.95, fontSize: 9.5, color: COLORS.MID, align: "center", valign: "top", fontFace: CA });
});
const glx = stages[3].x;
s.addShape(LINE, { x: glx, y: bandY - 0.5, w: 0, h: bandH + 0.5, line: { color: COLORS.AMBER, width: 1.5, dashType: "dash" } });
s.addShape(DIA, { x: glx - 0.22, y: bandY - 0.78, w: 0.44, h: 0.44, fill: { color: COLORS.AMBER }, line: { color: COLORS.AMBER } });
s.addText("GO-LIVE  |  Wk 16", { x: glx - 2.0, y: bandY - 0.78, w: 1.7, h: 0.44, fontSize: 10, bold: true, color: "B45309", align: "right", valign: "middle", fontFace: CA });

s = addContentSlide("SCOPE", "What Phase 1 Delivers", pg++);
const cards = [
  ["ITSM Core", "Incident, Request, Knowledge, Problem & Change/CAB in Service Operations Workspace", COLORS.NAVY],
  ["Service Catalog", "Your 10-15 highest-impact items + generic catch-all requests", COLORS.NAVY],
  ["Employee Experience", "Employee Center, Virtual Agent, AI Search & Knowledge Management", COLORS.NAVY],
  ["Platform Baselines", "Subscription Mgmt, Security Center, Predictive Intelligence, Platform Analytics", COLORS.NAVY],
  ["CMDB & CSDM", "CSDM alignment, Service Graph Connectors (SCCM, Intune), Discovery", COLORS.NAVY],
  ["Hardware Asset Mgmt", "Stockrooms + foundational HAM to keep CSDM aligned for Phase 2", COLORS.NAVY],
  ["Integrations", "AD / SSO, SCCM, Intune & Vonage - leveraging your existing setup", COLORS.NAVY],
  ["Later Phases", "P2 - UX expansion  |  P3 - ITOM & intelligence  |  P4+ - full AI", COLORS.MID],
];
cards.forEach((c, i) => {
  const col = i % 4, row = Math.floor(i / 4);
  const x = 0.5 + col * 3.1, y = 1.55 + row * 2.45;
  s.addShape(RR, { x, y, w: 2.88, h: 2.25, fill: { color: COLORS.LT_BG }, line: { color: COLORS.LT_GRY }, rectRadius: 0.06 });
  s.addShape(RECT, { x, y, w: 2.88, h: 0.5, fill: { color: c[2] }, line: { color: c[2] } });
  s.addText(c[0], { x: x + 0.1, y, w: 2.68, h: 0.5, fontSize: 11.5, bold: true, color: COLORS.WHITE, align: "center", valign: "middle", fontFace: CA });
  s.addText(c[1], { x: x + 0.15, y: y + 0.6, w: 2.58, h: 1.55, fontSize: 10, color: COLORS.SLATE, align: "left", valign: "top", fontFace: CA, lineSpacingMultiple: 1.05 });
});

s = addContentSlide("HOW WE WORK", "The OOTB-First Approach", pg++);
s.addText("Every build starts from standard ServiceNow, demonstrated first. We meet the need the standard way before considering any change - protecting your investment and keeping the platform upgradeable.",
  { x: 0.5, y: 1.55, w: 12.3, h: 0.7, fontSize: 13, color: COLORS.SLATE, fontFace: CA, valign: "top" });
s.addText("THE RULE OF THREE", { x: 0.5, y: 2.45, w: 12.3, h: 0.3, fontSize: 11, bold: true, charSpacing: 2, color: COLORS.TEAL_DK, fontFace: CA });
const steps = [["1", "Configuration"], ["2", "UI Policy"], ["3", "No-code Flow Designer"]];
steps.forEach((st, i) => {
  const x = 0.6 + i * 3.05;
  s.addShape(RR, { x, y: 2.85, w: 2.6, h: 1.3, fill: { color: COLORS.TEAL_LT }, line: { color: COLORS.TEAL_BDR }, rectRadius: 0.08 });
  s.addText([
    { text: st[0] + "\n", options: { fontSize: 22, bold: true, color: COLORS.TEAL_DK } },
    { text: st[1], options: { fontSize: 12.5, color: COLORS.SLATE } },
  ], { x: x + 0.1, y: 2.95, w: 2.4, h: 1.1, align: "center", valign: "middle", fontFace: CA, lineSpacingMultiple: 1.0 });
  if (i < 2) s.addShape(ARR, { x: x + 2.62, y: 3.35, w: 0.4, h: 0.3, fill: { color: COLORS.TEAL }, line: { color: COLORS.TEAL } });
});
s.addShape(ARR, { x: 9.7, y: 3.35, w: 0.45, h: 0.3, fill: { color: COLORS.AMBER }, line: { color: COLORS.AMBER } });
s.addShape(RR, { x: 10.2, y: 2.85, w: 2.6, h: 1.3, fill: { color: COLORS.AMBER_LT }, line: { color: COLORS.AMBER_BDR }, rectRadius: 0.08 });
s.addText([
  { text: "Customization\n", options: { fontSize: 13, bold: true, color: "B45309" } },
  { text: "Transparent review + Two-Key sign-off before any work", options: { fontSize: 10.5, color: "78350F" } },
], { x: 10.3, y: 2.95, w: 2.4, h: 1.1, align: "center", valign: "middle", fontFace: CA, lineSpacingMultiple: 1.02 });
addCallout(s, "Nothing is lost:", "Every deviation request is logged, assessed, and decided in the open via the Governance Triage Log.", "tip");

addSectionDivider("Working Together", "Clear roles, simple checks, transparent decisions", "", pg++);

const cols = addTwoColSlide("ROLES & ACCOUNTABILITY", "Who Does What", "CONNECTION", "ECS FEDERAL", COLORS.TEAL_DK, COLORS.NAVY, pg++);
cols.slide.addText([
  B("Project Sponsor - decisions, budget, business-need approval, Go-Live"),
  B("Project Manager - coordination, SME scheduling, status"),
  B("Technical Lead - access, credentials, technical approvals"),
  B("Process SMEs - process decisions & workshops"),
  B("UAT Testers - acceptance testing (Wks 13-16)"),
], { x: cols.leftX, y: cols.contentY, w: cols.leftW, h: 4.7, fontSize: 12.5, color: COLORS.SLATE, fontFace: CA, valign: "top" });
cols.slide.addText([
  B("Engagement Manager - delivery, governance, schedule, risk"),
  B("Solution Architect - architecture, CSDM, impact assessments"),
  B("Process Consultant - workshops, OOTB guidance, training"),
  B("Technical Consultant(s) - configuration, data, integrations"),
  B("Practice Lead - quality oversight, technical-path approval"),
], { x: cols.rightX, y: cols.contentY, w: cols.rightW, h: 4.7, fontSize: 12.5, color: COLORS.SLATE, fontFace: CA, valign: "top" });

s = addContentSlide("STAYING ON TRACK", "How We Keep on Track", pg++);
s.addText("THE TWO-KEY DECISION MODEL", { x: 0.5, y: 1.5, w: 12.3, h: 0.3, fontSize: 11, bold: true, charSpacing: 2, color: COLORS.TEAL_DK, fontFace: CA });
s.addShape(RR, { x: 0.6, y: 1.9, w: 4.7, h: 1.0, fill: { color: COLORS.TEAL_DK }, line: { color: COLORS.TEAL_DK }, rectRadius: 0.06 });
s.addText([{ text: "FIRST KEY\n", options: { fontSize: 10, bold: true, color: "BFE6E0", charSpacing: 1 } }, { text: "Connection Sponsor - business need", options: { fontSize: 12.5, bold: true, color: COLORS.WHITE } }], { x: 0.7, y: 1.9, w: 4.5, h: 1.0, align: "center", valign: "middle", fontFace: CA });
s.addShape(RR, { x: 0.6, y: 3.05, w: 4.7, h: 1.0, fill: { color: COLORS.NAVY }, line: { color: COLORS.NAVY }, rectRadius: 0.06 });
s.addText([{ text: "SECOND KEY\n", options: { fontSize: 10, bold: true, color: "9CB8D8", charSpacing: 1 } }, { text: "ECS Practice - technical path", options: { fontSize: 12.5, bold: true, color: COLORS.WHITE } }], { x: 0.7, y: 3.05, w: 4.5, h: 1.0, align: "center", valign: "middle", fontFace: CA });
s.addShape(ARR, { x: 5.45, y: 2.25, w: 1.1, h: 0.35, fill: { color: COLORS.TEAL }, line: { color: COLORS.TEAL }, rotate: 18 });
s.addShape(ARR, { x: 5.45, y: 3.35, w: 1.1, h: 0.35, fill: { color: COLORS.NAVY }, line: { color: COLORS.NAVY }, rotate: -18 });
s.addShape(RR, { x: 6.9, y: 2.25, w: 5.9, h: 1.45, fill: { color: COLORS.BLUE_LT }, line: { color: COLORS.BLUE_BDR }, rectRadius: 0.06 });
s.addText([
  { text: "Both keys required, decision in ~48 hours\n", options: { fontSize: 13, bold: true, color: COLORS.NAVY } },
  { text: "Logged in the Governance Triage Log within 24 hrs, visible to both teams - nothing is built that isn't both a real business need and a real technical necessity.", options: { fontSize: 11, color: COLORS.SLATE } },
], { x: 7.1, y: 2.35, w: 5.5, h: 1.25, align: "left", valign: "middle", fontFace: CA, lineSpacingMultiple: 1.04 });
s.addText("THE RHYTHM", { x: 0.5, y: 4.35, w: 12.3, h: 0.3, fontSize: 11, bold: true, charSpacing: 2, color: COLORS.TEAL_DK, fontFace: CA });
const cad = ["Weekly - status report", "Every 2 weeks - sprint demo + Sponsor sync", "As needed (48h) - Customization Council", "Monthly - steering & KPIs"];
cad.forEach((c, i) => {
  const x = 0.5 + i * 3.1;
  s.addShape(RR, { x, y: 4.7, w: 2.88, h: 0.75, fill: { color: COLORS.LT_BG }, line: { color: COLORS.LT_GRY }, rectRadius: 0.08 });
  s.addText(c, { x: x + 0.1, y: 4.7, w: 2.68, h: 0.75, fontSize: 10.5, bold: true, color: COLORS.SLATE, align: "center", valign: "middle", fontFace: CA });
});
addCallout(s, "Your weekly check:", "See progress (status), see it working (demo), see every open decision (triage log).", "tip");

s = addContentSlide("GETTING STARTED", "What We Need From You - Sprint 0", pg++);
s.addText([
  B("Empowered process owners who can decide in workshops"),
  B("The Foundation Data Pack completed (users, locations, groups, assignment rules, SLAs)"),
  B("Environment access and integration credentials"),
  B("SME availability during their process-area sprints"),
  B("Prompt feedback during demos and acceptance testing"),
], bodyBox(0.6, 1.6, 11.8, 4.3));
addCallout(s, "First two weeks:", "Kickoff, confirm Sponsor & sign the Council charter, provision access, distribute the data pack, map SMEs.", "info");

addSectionDivider("Let's Modernize the Core", "Next step: confirm names, schedule Sprint 0 workshops, and begin.", "Questions? Your ECS Engagement Manager is your first point of contact.", pg++);

pres.writeFile({ fileName: OUT }).then(() => console.log("Saved:", OUT));
