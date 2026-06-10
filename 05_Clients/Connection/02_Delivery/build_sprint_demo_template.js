/**
 * Connection - Sprint Demo Deck TEMPLATE (client-facing, reusable).
 * Built via pptx_brand.js. Source pure ASCII. Duplicate per sprint; fill [tokens].
 */
"use strict";
const path = require("path");
const REPO = "/sessions/eager-epic-davinci/mnt/everforth-ecs-practice";
const brand = require(path.join(REPO, "03_Shared/00_Templates_and_Branding/pptx_brand.js"));
const LOGO = path.join(REPO, "00_Master_Blueprint/assets/everforth_logo.png");
const OUT = path.join(REPO, "05_Clients/Connection/02_Delivery/Connection_Sprint_Demo_TEMPLATE.pptx");

const { pres, COLORS, addContentSlide, addTitleSlide, addSectionDivider, addCallout } =
  brand.init({ logoPath: LOGO, footerLabel: "CONNECTION   |   SPRINT DEMO   |   CONFIDENTIAL" });
const CA="Calibri";
const bodyBox=(x,y,w,h)=>({x,y,w,h,fontSize:14,color:COLORS.SLATE,fontFace:CA,valign:"top",lineSpacingMultiple:1.1});
const B=(t,opt={})=>({text:t,options:{bullet:{indent:14},paraSpaceAfter:8,...opt}});
let pg=1;

addTitleSlide("Sprint [N] Demo","Connection - [Sprint Theme]",
  "Two-week sprint review - what we built, what's signed off, what's next.",
  "Everforth ECS Federal   |   ServiceNow Practice   |   Confidential", pg++);

let s=addContentSlide("AGENDA","Today's Demo", pg++);
s.addText([B("Sprint goal and scope"),B("What we built (live demo)"),B("Signed-off stories and decisions"),
  B("Deferred items and any deviations"),B("Sprint metrics"),B("Next sprint preview")], bodyBox(0.6,1.6,11.8,5.0));

s=addContentSlide("THIS SPRINT","Sprint Goal & Scope", pg++);
s.addText([B("Goal: [the outcome this sprint set out to deliver]"),
  B("In scope: [stories / capabilities committed]"),
  B("OOTB focus: [the standard ServiceNow capability demonstrated]")], bodyBox(0.6,1.6,11.8,4.4));
addCallout(s,"Reminder:","Every story shown was built OOTB-first and met the Definition of Done before this demo.","tip");

s=addContentSlide("DEMO","What We Built", pg++);
s.addText([B("[Capability 1] - [one-line what it does for Connection]"),
  B("[Capability 2] - [ ]"),B("[Capability 3] - [ ]"),
  B("[Live demo against real Connection data - not Lorem ipsum]", {italic:true})], bodyBox(0.6,1.6,11.8,4.6));

s=addContentSlide("SIGNED OFF","Stories Accepted & Decisions Made", pg++);
s.addText([B("[Story / decision accepted by the Product Owner]"),
  B("[Decision made in-room, with owner]"),B("[ ]")], bodyBox(0.6,1.6,11.8,4.6));

s=addContentSlide("MANAGED","Deferred & Deviations", pg++);
s.addText([B("Deferred to backlog: [item + rationale]"),
  B("Deviation raised: [item -> logged in Governance Triage Log -> Council / two-key]"),
  B("Nothing built outside OOTB without the two-key decision.", {italic:true})], bodyBox(0.6,1.6,11.8,4.6));

s=addContentSlide("METRICS","Sprint Snapshot", pg++);
s.addText([B("Velocity: [points completed vs planned]"),
  B("Definition of Done: [stories meeting all gates]"),
  B("Customizations approved: [N of 5]"),
  B("Open risks / dependencies: [N - see RAID log]")], bodyBox(0.6,1.6,11.8,4.6));

addSectionDivider("Next Sprint", "[Sprint N+1 theme] - [weeks]", "What we'll build, and what we need from you.", pg++);

s=addContentSlide("LOOK AHEAD","Next Sprint Preview", pg++);
s.addText([B("Focus: [next sprint goal]"),
  B("We'll need from Connection: [SME time / decisions / data]"),
  B("Upcoming milestone: [demo date / Go-Live Wk 16]")], bodyBox(0.6,1.6,11.8,4.6));

addSectionDivider("Questions & Discussion", "Thank you.", "Your ECS Engagement Manager is your first point of contact.", pg++);

pres.writeFile({fileName:OUT}).then(()=>console.log("Saved:",OUT));
