/**
 * Connection - Executive Health Dashboard (one-page, client-safe). v2 - delivery metrics.
 * 6-vector ECS health model + DELIVERY metrics (sprint health, defect rate, story/deliverable completion).
 * Operational KPIs (MTTR/SLA) begin post Go-Live and are intentionally not shown here.
 */
"use strict";
const path = require("path");
const REPO = "/sessions/eager-epic-davinci/mnt/everforth-ecs-practice";
const brand = require(path.join(REPO, "03_Shared/00_Templates_and_Branding/pptx_brand.js"));
const LOGO = path.join(REPO, "00_Master_Blueprint/assets/everforth_logo.png");
const OUT = path.join(REPO, "05_Clients/Connection/02_Delivery/Connection_Executive_Health_Dashboard.pptx");
const { pres, COLORS, addContentSlide } =
  brand.init({ logoPath: LOGO, footerLabel: "CONNECTION   |   EXECUTIVE HEALTH DASHBOARD   |   CONFIDENTIAL" });
const RR = pres.shapes.ROUNDED_RECTANGLE, RECT = pres.shapes.RECTANGLE;
const CA = "Calibri", TR = "Trebuchet MS";
const RAG = { G:{bg:"DCFCE7",bd:"86EFAC",tx:"166534",lbl:"GREEN"}, Y:{bg:"FEF9C3",bd:"FDE68A",tx:"854D0E",lbl:"YELLOW"}, R:{bg:"FEE2E2",bd:"FECACA",tx:"991B1B",lbl:"RED"} };

const s = addContentSlide("EXECUTIVE HEALTH DASHBOARD", "Connection - Engagement Health", null);
s.addText("Reporting period: [Wk NN]   |   Sprint [N] of 8   |   Stage [X]   |   Prepared by [EM]",
  { x: 0.5, y: 1.4, w: 8.8, h: 0.3, fontSize: 11, color: COLORS.MID, fontFace: CA });
const ov = RAG.G;
s.addShape(RR, { x: 9.5, y: 1.32, w: 3.3, h: 0.5, fill:{color:ov.bg}, line:{color:ov.bd}, rectRadius:0.1 });
s.addText([{text:"OVERALL:  ",options:{bold:true,color:COLORS.SLATE}},{text:ov.lbl,options:{bold:true,color:ov.tx}}],
  { x: 9.5, y: 1.32, w: 3.3, h: 0.5, fontSize: 12, align:"center", valign:"middle", fontFace: CA });

// Health vectors
s.addText("ENGAGEMENT HEALTH VECTORS  (per ECS trust-but-verify model)", { x: 0.5, y: 1.95, w: 12.3, h: 0.25, fontSize: 10.5, bold:true, charSpacing:1.5, color: COLORS.TEAL_DK, fontFace: CA });
const vectors = [["Process Adoption","G"],["Config Hygiene","G"],["Customization Variance","G"],["Adoption Readiness","G"],["Sponsor & SME Alignment","G"],["Schedule to Go-Live","G"]];
vectors.forEach((v,i)=>{
  const x = 0.5 + i*2.075; const c = RAG[v[1]];
  s.addShape(RR, { x, y: 2.25, w: 1.95, h: 0.85, fill:{color:c.bg}, line:{color:c.bd}, rectRadius:0.08 });
  s.addText([{text:v[0]+"\n",options:{fontSize:9.5,bold:true,color:COLORS.SLATE}},{text:c.lbl,options:{fontSize:11,bold:true,color:c.tx}}],
    { x: x+0.05, y: 2.3, w: 1.85, h: 0.75, align:"center", valign:"middle", fontFace: CA, lineSpacingMultiple:1.0 });
});

// DELIVERY METRICS (replaces operational KPIs)
s.addText("DELIVERY METRICS  (engagement health - operational KPIs begin post Go-Live)", { x: 0.5, y: 3.3, w: 12.3, h: 0.25, fontSize: 10.5, bold:true, charSpacing:1.5, color: COLORS.TEAL_DK, fontFace: CA });
const dm = [["SPRINT HEALTH","[X / Y pts]","Velocity vs planned (3-sprint avg)"],
            ["DEFECT RATE","[P1/P2 open]","Open UAT defects (P1/P2)"],
            ["STORY COMPLETION","[N%]","Config + delivery stories Done"],
            ["DELIVERABLES","[N / 27]","SOW deliverables complete / on track"]];
dm.forEach((k,i)=>{
  const x = 0.5 + i*3.1;
  s.addShape(RR, { x, y: 3.6, w: 2.88, h: 1.0, fill:{color:COLORS.LT_BG}, line:{color:COLORS.LT_GRY}, rectRadius:0.06 });
  s.addShape(RECT, { x, y: 3.6, w: 0.1, h: 1.0, fill:{color:COLORS.TEAL}, line:{color:COLORS.TEAL} });
  s.addText([{text:k[0]+"\n",options:{fontSize:11.5,bold:true,color:COLORS.NAVY}},{text:k[1]+"\n",options:{fontSize:15,bold:true,color:COLORS.TEAL_DK}},{text:k[2],options:{fontSize:9,color:COLORS.MID}}],
    { x: x+0.2, y: 3.64, w: 2.6, h: 0.92, align:"left", valign:"middle", fontFace: CA, lineSpacingMultiple:1.0 });
});

// Schedule bar
s.addText("SCHEDULE", { x: 0.5, y: 4.75, w: 6, h: 0.25, fontSize: 10.5, bold:true, charSpacing:1.5, color: COLORS.TEAL_DK, fontFace: CA });
s.addShape(RECT, { x: 0.5, y: 5.05, w: 12.3, h: 0.32, fill:{color:COLORS.LT_GRY}, line:{color:COLORS.LT_GRY} });
s.addShape(RECT, { x: 0.5, y: 5.05, w: 4.0, h: 0.32, fill:{color:COLORS.TEAL_DK}, line:{color:COLORS.TEAL_DK} });
s.addText("Sprint [N] of 8  -  Go-Live Week 16  -  Hypercare Wks 17-18   (resize the teal bar to % complete)",
  { x: 0.6, y: 5.05, w: 12.1, h: 0.32, fontSize: 9.5, italic:true, color: "FFFFFF", valign:"middle", fontFace: CA });

// Risks + Decisions
s.addText("TOP RISKS", { x: 0.5, y: 5.55, w: 6, h: 0.25, fontSize: 10.5, bold:true, charSpacing:1.5, color: COLORS.TEAL_DK, fontFace: CA });
s.addShape(RR, { x: 0.5, y: 5.82, w: 6.0, h: 1.2, fill:{color:COLORS.LT_BG}, line:{color:COLORS.LT_GRY}, rectRadius:0.06 });
s.addText([{text:"1.  [Top risk + owner + mitigation]\n",options:{}},{text:"2.  [Risk]\n",options:{}},{text:"3.  [Risk]",options:{}}],
  { x: 0.7, y: 5.88, w: 5.7, h: 1.08, fontSize: 11, color: COLORS.SLATE, valign:"top", fontFace: CA, lineSpacingMultiple:1.12 });
s.addText("DECISIONS NEEDED", { x: 6.8, y: 5.55, w: 6, h: 0.25, fontSize: 10.5, bold:true, charSpacing:1.5, color: COLORS.TEAL_DK, fontFace: CA });
s.addShape(RR, { x: 6.8, y: 5.82, w: 6.0, h: 1.2, fill:{color:COLORS.BLUE_LT}, line:{color:COLORS.BLUE_BDR}, rectRadius:0.06 });
s.addText([{text:"1.  [Decision needed - from whom - by when]\n",options:{}},{text:"2.  [Decision]\n",options:{}},{text:"3.  [Decision]",options:{}}],
  { x: 7.0, y: 5.88, w: 5.7, h: 1.08, fontSize: 11, color: COLORS.SLATE, valign:"top", fontFace: CA, lineSpacingMultiple:1.12 });

pres.writeFile({ fileName: OUT }).then(()=>console.log("Saved:", OUT));
