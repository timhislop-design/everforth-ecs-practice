/** Connection - Interactions & Vonage CTI Workshop (client). Phase 1: inbound voice. Pure ASCII. */
"use strict";
const path=require("path");
const REPO="/sessions/eager-epic-davinci/mnt/everforth-ecs-practice";
const brand=require(path.join(REPO,"03_Shared/00_Templates_and_Branding/pptx_brand.js"));
const LOGO=path.join(REPO,"00_Master_Blueprint/assets/everforth_logo.png");
const OUT=path.join(REPO,"05_Clients/Connection/02_Delivery/Workshops/Connection_Interactions_Vonage_CTI_Workshop.pptx");
const {pres,COLORS,addContentSlide,addSectionDivider,addTitleSlide,addTwoColSlide,addCallout,addDecisionSlide}=
  brand.init({logoPath:LOGO,footerLabel:"CONNECTION   |   MODERNIZING THE CORE   |   INTERACTIONS & VONAGE CTI"});
const RR=pres.shapes.ROUNDED_RECTANGLE,ARR=pres.shapes.RIGHT_ARROW;const CA="Calibri",TR="Trebuchet MS";
const body=(x,y,w,h)=>({x,y,w,h,fontSize:14,color:COLORS.SLATE,fontFace:CA,valign:"top",lineSpacingMultiple:1.1});
const B=(t,o={})=>({text:t,options:{bullet:{indent:14},paraSpaceAfter:8,...o}});
let pg=1;

addTitleSlide("Interactions & Vonage CTI","Connection - Modernizing the Core",
 "Phase 1: the inbound voice channel - calls land as Interactions, then become Incidents or Requests.",
 "Prepared by Everforth ECS Federal   |   ServiceNow Practice   |   Confidential",pg++);

let s=addContentSlide("AGENDA","Today's Workshop",pg++);
s.addText([B("Why Interactions - the OOTB entry point for the phone channel"),B("The approach: OOTB CTI, not custom telephony"),
 B("The line: what we configure vs. what's a customization"),B("The process: call to Interaction to Incident/Request"),
 B("Key decisions to make in the room"),B("Next steps and what we need from you")],body(0.6,1.6,11.8,5.0));

s=addContentSlide("THE APPROACH","OOTB CTI Through Interactions",pg++);
s.addText([B("Vonage is the telephony; ServiceNow Interactions is the OOTB record that captures the call."),
 B("Agents work an embedded OpenFrame softphone inside the Agent / Service Operations Workspace - no separate app."),
 B("An inbound call opens an Interaction with caller context (screen-pop); the agent creates or links an Incident or Request from it."),
 B("Phase 1 is the voice channel only. Chat, email, and SMS through Interactions come in a later phase.")],body(0.6,1.6,11.8,4.2));
addCallout(s,"Why it matters:","Interactions is the connective tissue between the phone and the ITSM record - the OOTB foundation for omnichannel, starting with voice.","tip");

// THE LINE (two-column)
const c=addTwoColSlide("THE LINE","What We Configure - and What's a Customization","CONFIGURATION  -  Always available","CUSTOMIZATION  -  Requires Approval + Business Case",COLORS.TEAL_DK,COLORS.NAVY,pg++);
c.slide.addText([B("OpenFrame softphone configuration in the workspace"),B("Vonage CTI adapter install (Store / Vonage-provided)"),
 B("Agent-to-extension mapping; availability states"),B("Vonage queue/skill to assignment group mapping"),
 B("Inbound screen-pop + caller match (phone to user)"),B("Interaction to Incident/Request via OOTB actions"),
 B("Business hours and routing context")],
 {x:c.leftX,y:c.contentY,w:c.leftW,h:4.6,fontSize:12,color:COLORS.SLATE,fontFace:CA,valign:"top"});
c.slide.addText([B("Custom softphone or telephony middleware"),B("Scripted screen-pop beyond OOTB CTI capability"),
 B("Storing call-recording media inside ServiceNow"),B("Bespoke click-to-dial logic outside the connector"),
 B("Custom interaction tables outside the OOTB model")],
 {x:c.rightX,y:c.contentY,w:c.rightW,h:4.6,fontSize:12,color:COLORS.SLATE,fontFace:CA,valign:"top"});

// THE PROCESS (visual flow)
s=addContentSlide("THE PROCESS","Call to Interaction to Resolution",pg++);
const steps=[["1","Inbound Vonage call","Routed by queue/skill"],["2","OpenFrame rings","In the agent workspace"],
 ["3","Interaction opens","Screen-pop; caller matched"],["4","Create / link record","Incident or Request (OOTB)"],
 ["5","Work + recording link","Resolve; link recording in Vonage"]];
const bw=2.3,gap=0.18,y0=2.7;let x0=0.5;
steps.forEach((st,i)=>{
 s.addShape(RR,{x:x0,y:y0,w:bw,h:1.7,fill:{color:i<3?COLORS.TEAL_LT:COLORS.LT_BG},line:{color:i<3?COLORS.TEAL_BDR:COLORS.LT_GRY},rectRadius:0.08});
 s.addText([{text:st[0]+"\n",options:{fontSize:18,bold:true,color:COLORS.TEAL_DK}},{text:st[1]+"\n",options:{fontSize:12.5,bold:true,color:COLORS.NAVY}},{text:st[2],options:{fontSize:10,color:COLORS.MID}}],
  {x:x0+0.08,y:y0+0.12,w:bw-0.16,h:1.5,align:"center",valign:"middle",fontFace:CA,lineSpacingMultiple:1.02});
 if(i<steps.length-1) s.addShape(ARR,{x:x0+bw+0.01,y:y0+0.72,w:gap+0.12,h:0.26,fill:{color:COLORS.TEAL},line:{color:COLORS.TEAL}});
 x0+=bw+gap;
});
addCallout(s,"OOTB throughout:","Every step uses OpenFrame, the Vonage connector, and the OOTB Interaction record - zero custom telephony code.","tip");

// KEY DECISIONS
addDecisionSlide(1,"Inbound only, or include click-to-dial (outbound) in Phase 1?",
 "OOTB inbound voice + screen-pop is the Phase 1 baseline. Click-to-dial is OOTB-available via the connector but adds scope and testing.",
 "Decide: Is outbound click-to-dial in Phase 1, or deferred? Which agent groups need it first?",
 "Adding outbound now expands UAT and agent training. If it is not a Go-Live blocker, defer to keep the core clean.",pg++);
addDecisionSlide(2,"How do we identify callers - and handle unknown numbers?",
 "OOTB matches the caller's number to sys_user phone / mobile_phone and screen-pops the match. No match opens a guest Interaction.",
 "Decide: Match fields and priority order? Guest-caller handling? Any IVR-collected ID we should pass to the match?",
 "Over-engineering caller match (fuzzy logic, external lookups) is a customization. Start with the OOTB phone-field match.",pg++);
addDecisionSlide(3,"Queue mapping and call recording - what's in scope?",
 "OOTB maps Vonage queues/skills to assignment groups for routing context. Recordings stay in Vonage with a link on the Interaction.",
 "Decide: Queue -> assignment group mapping. Is recording in scope for Phase 1? Storage, retention, and consent rules?",
 "Storing call media in ServiceNow is a customization and a compliance risk - keep media in Vonage, link from the Interaction.",pg++);

addSectionDivider("Next Steps","Port the existing Vonage setup; build on OOTB OpenFrame.","We use your current integration as the spec - rebuilt the OOTB way.",pg++);
s=addContentSlide("NEXT STEPS","After This Workshop",pg++);
s.addText([B("Complete the Vonage CTI accelerator pack (Requirements + Configuration Data tabs)."),
 B("Inventory the legacy Vonage integration for porting (see the pack's Port from Legacy tab)."),
 B("Confirm OpenFrame + Interaction prerequisites and Vonage API credentials."),
 B("Provision a test number + test agent for sub-prod validation."),
 B("Target: CTI configured and validated alongside Incident/Request in Stage 2.")],body(0.6,1.6,11.8,4.6));

pres.writeFile({fileName:OUT}).then(()=>console.log("Saved:",OUT));
