"""
Build INT-OR-01 — ECS Practice Onboarding Roadmap
Internal artifact: phased role-by-role onboarding guide for the OOTB-first model.
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

OUT = os.path.join(HERE, "INT-OR-01_ECS_Practice_Onboarding_Roadmap_INTERNAL.docx")

doc = EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL PRACTICE GUIDE",
    title="ECS Practice\nOnboarding Roadmap",
    subtitle="Phased role-by-role adoption of the OOTB-first delivery model",
    audience="Practice Lead, Engagement Managers, Solution Architects, Process Consultants, Developers",
    companion_to="Consultant Handbook (INT-CH-01) · Manager's TBV Playbook (INT-TBV-01) · Internal Governance Operating Guide",
    doc_id="INT-OR-01",
    version="1.0",
    status="Released",
    running_header_label="Internal · ECS Practice Onboarding Roadmap",
))
doc.add_cover_page()
doc.page_break()

# ─────────────────────────────────────────────────
# HOW TO USE THIS GUIDE
# ─────────────────────────────────────────────────
doc.h1("How to Use This Guide", numbered=False)
doc.para(
    "This guide is the practice lead's primary tool for onboarding consultants, "
    "engagement managers, and technical staff to the ECS OOTB-first delivery model. "
    "It answers three questions: what does each role need to know, in what order, "
    "and how do we change the default behavior that has accumulated over years of "
    "custom-first delivery?"
)
doc.para(
    "The guide is organized into three phases. Phase 1 is the minimum viable "
    "onboarding — the documents and concepts every person must internalize before "
    "their first engagement sprint. Phase 2 activates the discipline-specific toolkit "
    "during Sprint 0 through the first two sprints. Phase 3 establishes the muscle "
    "memory through manager reinforcement and field repetition. Do not collapse the "
    "phases. The culture change requires staged exposure, not a document dump."
)
doc.callout(
    "HOW TO RUN AN ONBOARDING SESSION: Phase 1 content should be delivered as a "
    "facilitated 90-minute read-through, not sent as attachments. "
    "Consultants need a room to ask 'but what about when...' questions. "
    "That conversation is where the culture shift starts."
)

# ─────────────────────────────────────────────────
# THE OCM CHALLENGE
# ─────────────────────────────────────────────────
doc.h1("The OCM Challenge: Flipping the Default", numbered=True)
doc.para(
    "The ECS team is technically skilled and customer-oriented. That is exactly "
    "the problem. Years of custom-first delivery have trained consultants to hear "
    "a customer requirement and immediately think: how do we build this? The OOTB-first "
    "model requires a different reflex: how does ServiceNow already do this, and "
    "how do we show the customer why that is better?"
)
doc.para(
    "This is not a knowledge gap — it is a habit gap. The library of how-to guides, "
    "cheatsheets, accelerator packs, and demo scripts exists to make the new habit "
    "easier than the old one. But the habit only forms if the material is introduced "
    "in the right sequence and reinforced by management through the Trust-But-Verify "
    "tools. The three-phase model below is designed to create that sequence."
)

doc.h2("The Three Culture-Change Levers")
doc.para(
    "Three things must change in parallel for the model to stick across the team: "
    "vocabulary (everyone uses the same language for OOTB decisions), tools "
    "(everyone reaches for the same cheatsheet or facilitator guide in the moment), "
    "and visibility (management can see when the model is holding and when it is "
    "slipping). The phases below address all three."
)

doc.table(
    headers=["Lever", "What Changes", "Primary Tool"],
    rows=[
        ["Vocabulary", "Consultants use OOTB-first language in workshops; customers hear 'Modernizing the Core' instead of 'we can customize that'", "INT-CH-04 OOTB-First Glossary + INT-CH-03 Decision Rights Reference"],
        ["Tools", "Consultants reach for cheatsheets, facilitator guides, and demo scripts before ad-libbing", "INT-AR-01 to 16 Cheatsheets + INT-FG series Facilitator Guides"],
        ["Visibility", "Practice management tracks OOTB-defense usage and customization variance by sprint", "INT-TBV-02 Engagement Health Dashboard + INT-TBV-03 Customization Variance Tracker"],
    ]
)

# ─────────────────────────────────────────────────
# PHASE OVERVIEW
# ─────────────────────────────────────────────────
doc.h1("Three-Phase Onboarding Overview", numbered=True)
doc.para(
    "Each phase is designed around the natural rhythm of an engagement. "
    "Phase 1 happens before or at the start of Sprint 0. Phase 2 activates "
    "during Sprint 0 and carries through Sprint 2. Phase 3 is field-reinforced "
    "from Sprint 3 onward and continues through every subsequent engagement."
)

doc.table(
    headers=["Phase", "Timing", "Goal", "Delivery Method"],
    rows=[
        ["Phase 1 — The Contract", "Before first engagement / Days 1–5 of onboarding", "Shared vocabulary, clear decision rights, 3–4 anchor documents per role", "Facilitated 90-min group read-through — not email attachments"],
        ["Phase 2 — The Toolkit", "Sprint 0 through Sprint 2 of first engagement", "Role-specific tools active in the field; cheatsheets and facilitator guides used in real workshops", "Context-triggered delivery — 48 hrs before each sprint"],
        ["Phase 3 — The Standard", "Sprint 3 onward + every subsequent engagement", "OOTB-first behavior is ambient; management TBV checks active; lessons feed back", "Manager reinforcement via TBV tools; practice retro loop"],
    ]
)

# ─────────────────────────────────────────────────
# ENGAGEMENT MANAGER
# ─────────────────────────────────────────────────
doc.page_break()
doc.h1("Engagement Manager Onboarding Package", numbered=True)
doc.para(
    "The EM's culture change is the most critical in the practice. EMs are the "
    "single point at which OOTB-first discipline is either enforced or quietly eroded. "
    "An EM who does not have the TBV tools, the decision-rights frame, and the "
    "customization council process internalized will accommodate customer customization "
    "requests not out of bad intent, but because accommodation is the path of least "
    "resistance in the moment. The Phase 1 package for an EM is shorter than other "
    "roles but carries the highest consequences if skipped."
)

doc.h2("Phase 1 — The Contract")
doc.para(
    "Three documents. Read in full before the first engagement kickoff. The EM must "
    "be able to answer: who decides what, what does a customization council request "
    "look like, and what does engagement health drift look like before it becomes a "
    "visible problem."
)
doc.table(
    headers=["Doc ID", "Document", "What the EM Takes From It"],
    rows=[
        ["INT-CH-01", "Consultant Handbook — Decision Rights, Customization Council, and Engagement Spine sections", "The rules of the model: who decides what, how escalations work, what the 18-week cadence commits to"],
        ["INT-TBV-01", "Manager's Trust-But-Verify Playbook", "How to recognize OOTB-first drift, what the weekly health signals are, and how to course-correct before an escalation"],
        ["INT-CH-03", "Engagement Decision Rights Reference", "The one-page quick reference for who can approve what — carried into every sponsor sync"],
    ]
)

doc.h2("Phase 2 — The Toolkit")
doc.para(
    "Six tools that become the EM's operational cadence for the first engagement. "
    "Introduced at Sprint 0 kickoff and used every sprint thereafter."
)
doc.table(
    headers=["Doc ID", "Document", "When to Use It"],
    rows=[
        ["INT-S0-01", "Sprint 0 Facilitator Playbook", "Run Sprint 0 end-to-end using this as the operating guide"],
        ["INT-TBV-02", "Engagement Health Dashboard", "Updated weekly; reviewed at every sponsor sync and in practice management reviews"],
        ["INT-TBV-03", "Customization Variance Tracker", "Updated when any customization is approved; trend line is the primary drift signal"],
        ["INT-TBV-04", "Bi-Weekly Sponsor Sync Agenda Template", "Use verbatim for the first three sponsor syncs; adapt after that"],
        ["INT-S0-06", "Risk Register Template", "Populated at Sprint 0 kickoff; live document through hypercare"],
        ["INT-S0-07", "Communication Plan Template", "Agreed with the customer at Sprint 0; governs all sprint communications"],
    ]
)

doc.h2("Phase 3 — The Standard")
doc.para(
    "From Sprint 3 onward, the EM operates the full TBV suite and begins coaching "
    "their team against the model. The practice monthly review becomes the vehicle "
    "for surfacing lessons back to the practice lead."
)
doc.table(
    headers=["Doc ID", "Document", "How It Is Used at Phase 3"],
    rows=[
        ["INT-TBV-05", "Customization Council Pre-Read Template", "Prepared by the requesting consultant; reviewed and approved or denied in council"],
        ["INT-TBV-06", "Sprint Demo Discipline Audit", "EM completes before each sprint demo to confirm OOTB scope is holding"],
        ["INT-TBV-07", "Practice Management Monthly Review Template", "EM presents engagement health to practice lead monthly"],
        ["INT-TBV-08", "Engagement Course-Correction Playbook", "Pulled when Health Dashboard signals drift; not a corrective action — a prevention tool"],
        ["INT-TBV-09", "Consultant Coaching Conversation Templates", "Used when the EM needs to redirect a consultant who is accommodating outside the model"],
    ]
)

# ─────────────────────────────────────────────────
# SOLUTION ARCHITECT
# ─────────────────────────────────────────────────
doc.page_break()
doc.h1("Solution Architect Onboarding Package", numbered=True)
doc.para(
    "An SA's reflex problem is proposing custom solutions because they can. "
    "The OOTB-first flip is proposing OOTB configurations because they are better "
    "positioned for AI realization — and because the SA can demonstrate that in a "
    "live demo. Phase 1 for an SA reframes the architecture default. The cheatsheet "
    "and the decision framework give the SA a new vocabulary for conversations where "
    "they would previously have said yes to a custom pattern."
)

doc.h2("Phase 1 — The Contract")
doc.table(
    headers=["Doc ID", "Document", "What the SA Takes From It"],
    rows=[
        ["INT-CH-01", "Consultant Handbook — OOTB-First Model and Engagement Spine sections", "The delivery model the SA is architecting within; what OOTB-first means technically"],
        ["INT-CH-04", "OOTB-First Glossary", "The vocabulary to use in workshops when discussing configuration vs. customization"],
        ["INT-AR-14", "Custom-vs-OOTB Decision Framework Cheatsheet", "The decision tree for every architecture question; the SA's primary field reference in Sprints 4–5"],
        ["Platform Foundation How-To", "INT-HT-01 Platform Foundation How-To Consultant Guide", "The technical baseline the SA is responsible for standing up in Sprint 1"],
    ]
)

doc.h2("Phase 2 — The Toolkit")
doc.para(
    "Delivered at Sprint 0 and expanded sprint-by-sprint as technical disciplines "
    "are activated. The SA should receive each how-to guide and its matching "
    "accelerator pack 48 hours before the relevant sprint, not all at once."
)
doc.table(
    headers=["Doc ID", "Document", "Sprint Relevance"],
    rows=[
        ["INT-HT-12 / INT-HT-13", "CSDM How-To + CMDB How-To Consultant Guides", "Sprint 4 — the SA's primary technical ownership sprints"],
        ["INT-HT-14", "Discovery How-To Consultant Guide", "Sprint 4 — pairs with CMDB"],
        ["AP-10/11", "CMDB/CSDM Accelerator Pack", "Sprint 4 — SA walks the customer through these worksheets"],
        ["AP-12", "Discovery Accelerator Pack", "Sprint 4"],
        ["INT-FG-08", "Sprint 4 CSDM Facilitator Guide", "SA uses to prep and run the Sprint 4 CSDM workshop"],
        ["INT-FG-09", "Sprint 4 CMDB Facilitator Guide", "SA uses to prep and run the Sprint 4 CMDB workshop"],
        ["INT-FG-10", "Sprint 4 Discovery Facilitator Guide", "SA uses to prep and run the Sprint 4 Discovery workshop"],
        ["INT-AR-11", "CMDB Class Selection Cheatsheet", "SA's OOTB defense reference for class proliferation requests"],
        ["INT-AR-12", "Discovery Phasing Cheatsheet", "SA's OOTB defense for 'discover everything now' requests"],
    ]
)

doc.h2("Phase 3 — The Standard")
doc.table(
    headers=["Doc ID", "Document", "How It Is Used at Phase 3"],
    rows=[
        ["INT-HT-15", "Service Graph Connectors How-To", "Sprint 5 — SA owns SGC configuration"],
        ["INT-HT-20", "Integrations How-To (AD/Entra, SSO, SCCM, Intune)", "Sprint 5 — SA owns integration architecture"],
        ["INT-DS-05", "CSDM Service Map Demo Script", "SA can deliver an unscripted OOTB demo by Phase 3"],
        ["INT-DS-08", "Now Assist / GenAI Demo Script", "AI realization demo; the SA's closing argument for the OOTB-first model"],
        ["INT-FG-11", "Sprint 5 Service Graph Facilitator Guide", "Full Sprint 5 technical leadership"],
        ["INT-FG-13", "Sprint 5 Integrations Facilitator Guide", "Integration sprint leadership"],
    ]
)

# ─────────────────────────────────────────────────
# PROCESS CONSULTANT
# ─────────────────────────────────────────────────
doc.page_break()
doc.h1("Process Consultant Onboarding Package", numbered=True)
doc.para(
    "Process consultants sit directly across from the customer's SME who says "
    "'but our old system did X.' Their reflex is empathy and accommodation. "
    "The OOTB-first flip is confident defense with pre-built explanations that "
    "do not feel like a lecture. The Adopt-vs-Re-engineer cheatsheets are the "
    "single highest-leverage Phase 1 tool for a process consultant. They should "
    "read the cheatsheets for their assigned disciplines before their first workshop "
    "and carry them into every session."
)
doc.para(
    "Note: assign each process consultant 2–3 discipline areas at onboarding. "
    "Give them the cheatsheets and how-to guides for those areas only at Phase 1 and 2. "
    "Depth before breadth — a consultant who knows Incident and Change cold is "
    "more valuable than one who has skimmed all 20 disciplines."
)

doc.h2("Phase 1 — The Contract")
doc.table(
    headers=["Doc ID", "Document", "What the Process Consultant Takes From It"],
    rows=[
        ["INT-CH-01", "Consultant Handbook — Workshop Facilitation and OOTB Defense sections", "The facilitation model, when to push back on customization, and how the customization council works"],
        ["INT-CH-04", "OOTB-First Glossary", "Vocabulary to use when describing OOTB patterns to customers who are used to legacy language"],
        ["INT-AR-01", "Catalog Item Rationalization Cheatsheet", "Covers the most common workshop friction point; read first regardless of assigned discipline"],
        ["INT-AR-03", "SLA Discipline Cheatsheet", "Second most common friction point; SLA proliferation affects almost every engagement"],
        ["INT-AR-14", "Custom-vs-OOTB Decision Framework Cheatsheet", "The consultant's field guide for any in-workshop customization request"],
    ]
)
doc.callout(
    "PHASE 1 DELIVERY NOTE: Run a 45-minute cheatsheet review session per assigned discipline area. "
    "Have the consultant read the cheatsheet, then role-play a customer pushback scenario. "
    "The role-play is not optional — reading without practice does not build the reflex."
)

doc.h2("Phase 2 — The Toolkit")
doc.para(
    "Delivered 48 hours before each relevant sprint. The process consultant "
    "receives the how-to guide, the matching cheatsheets, the workshop pre-read "
    "(so they know what the customer received), and the facilitator guide for "
    "their assigned sprint discipline."
)
doc.table(
    headers=["Doc ID", "Document", "When to Deliver"],
    rows=[
        ["INT-HT-02", "Incident Management How-To", "48 hrs before Sprint 1 Incident workshops"],
        ["INT-HT-05", "Change Management How-To", "48 hrs before Sprint 4 Change workshop"],
        ["INT-HT-06", "Service Catalog & Request Management How-To", "48 hrs before Sprint 2 Catalog workshop"],
        ["INT-HT-07", "Knowledge Management How-To", "48 hrs before Sprint 3 Knowledge workshop"],
        ["INT-FG-02", "Sprint 1 Incident Management Facilitator Guide", "48 hrs before Sprint 1"],
        ["INT-FG-03", "Sprint 2 Catalog & Request Facilitator Guide", "48 hrs before Sprint 2"],
        ["INT-FG-05", "Sprint 3 Knowledge Facilitator Guide", "48 hrs before Sprint 3"],
        ["INT-FG-07", "Sprint 4 Change Facilitator Guide", "48 hrs before Sprint 4"],
        ["AP-02", "ITSM Accelerator Pack (6 workbooks)", "Sprint 0 — so the consultant understands what the customer is filling in"],
        ["Matching CLT-WP", "Workshop Pre-Read for each sprint discipline", "1 week before each sprint — read what the customer received"],
    ]
)

doc.h2("Phase 3 — The Standard")
doc.table(
    headers=["Doc ID", "Document", "How It Is Used at Phase 3"],
    rows=[
        ["INT-HT-08 / INT-HT-09", "Employee Center + Virtual Agent How-To Guides", "Sprint 3 extensions — EC and VA complement Knowledge"],
        ["INT-DS-02", "Catalog & Request Demo Script", "Process consultant delivers Sprint 2 OOTB demo unscripted"],
        ["INT-DS-03", "Knowledge / Virtual Agent Combined Demo Script", "Sprint 3 demo delivery"],
        ["INT-DS-04", "Change & CAB Workbench Demo Script", "Sprint 4 demo delivery"],
        ["INT-UAT-02", "UAT Execution Playbook", "Process consultant runs UAT facilitation using this guide"],
        ["INT-LL-01", "Lessons Learned — OOTB Defense Patterns", "After first engagement: process consultant contributes lessons"],
    ]
)

# ─────────────────────────────────────────────────
# DEVELOPER
# ─────────────────────────────────────────────────
doc.page_break()
doc.h1("Developer Onboarding Package", numbered=True)
doc.para(
    "A developer's OCM challenge is different from the consulting roles. Developers "
    "are less likely to be in workshops, but they are the ones who build the "
    "customization when a consultant (incorrectly) scopes it. Their Phase 1 is "
    "short and boundary-focused: what requires a customization council decision, "
    "what does OOTB configuration look like technically, and how do they raise a "
    "concern if they are being asked to build something outside the model."
)
doc.para(
    "Keep Phase 1 for developers concise. They do not need workshop facilitation "
    "theory. They need clear rules and a path to escalate when the rules are being "
    "violated. Phase 2 is where depth builds — through the accelerator packs and "
    "sprint workbooks that define what they will actually configure."
)

doc.h2("Phase 1 — The Contract")
doc.table(
    headers=["Doc ID", "Document", "What the Developer Takes From It"],
    rows=[
        ["INT-CH-01", "Consultant Handbook — Customization Council and OOTB Configuration sections only", "The boundary: what can be configured (OOTB), what requires a council decision, who to escalate to"],
        ["INT-CH-04", "OOTB-First Glossary", "Technical vocabulary — the difference between configuration, customization, and extension in ServiceNow terms"],
        ["INT-AR-14", "Custom-vs-OOTB Decision Framework Cheatsheet", "The developer's personal reference when scoping a build request"],
    ]
)

doc.h2("Phase 2 — The Toolkit")
doc.para(
    "Introduced at Sprint 0 and expanded as each sprint activates. "
    "The developer should receive the accelerator pack and sprint workbook "
    "for their assigned disciplines before Sprint 1 begins."
)
doc.table(
    headers=["Doc ID", "Document", "When to Deliver"],
    rows=[
        ["INT-HT-01", "Platform Foundation How-To", "Sprint 0 — the technical baseline the developer is building on"],
        ["AP-01", "Foundation Data Pack (8 workbooks)", "Sprint 0 — the developer configures what the customer fills in"],
        ["AP-02", "ITSM Accelerator Pack (6 workbooks)", "Sprint 1 — developer configures Incident, MIM, Problem, Change, Request, Knowledge"],
        ["AP-03", "Integration Accelerator Pack (4 workbooks)", "Sprint 0/1 — developer owns AD, SSO, SCCM, Intune configuration"],
        ["INT-S0-04", "Decision Rights Setup Template", "Sprint 0 — developer understands what requires configuration vs. build"],
        ["Sprint Workbooks", "03_Shared/04_Sprint_Workbooks — relevant sprint workbooks", "48 hrs before each sprint — developer reads alongside accelerator packs"],
    ]
)

doc.h2("Phase 3 — The Standard")
doc.table(
    headers=["Doc ID", "Document", "How It Is Used at Phase 3"],
    rows=[
        ["INT-UAT-01", "UAT Test Pack — Master Template", "Developer understands what will be tested against their build before they build it"],
        ["INT-HT-14", "Discovery How-To", "Sprint 4 technical depth — developer who owns Discovery configuration"],
        ["INT-HT-20", "Integrations How-To (AD/Entra, SSO, SCCM, Intune)", "Sprint 5 — developer owns integration build-out"],
        ["AP-04 / AP-05", "HAM Foundations + Realization Accelerator Packs", "Sprint 5 — developer who owns HAM configuration"],
        ["INT-LL-03", "Lessons Learned — CMDB Technical Patterns", "After first engagement: developer contributes technical lessons"],
    ]
)

# ─────────────────────────────────────────────────
# DELIVERY MECHANISM GUIDANCE
# ─────────────────────────────────────────────────
doc.page_break()
doc.h1("Delivery Mechanism Guidance", numbered=True)
doc.para(
    "The three-phase content only produces culture change if the delivery mechanism "
    "matches the goal. These are the non-negotiable rules for rolling this out."
)

doc.h2("Rule 1 — Facilitate Phase 1, Do Not Email It")
doc.para(
    "Phase 1 for every role must be a facilitated session — not a SharePoint link "
    "with attachments. The format is: practice lead (or senior EM) runs a 90-minute "
    "read-through of the 3–4 anchor documents. Participants read aloud, stop to "
    "discuss 'but what about when...' questions, and surface the assumptions they "
    "bring from their prior delivery experience. This conversation is where the "
    "culture shift starts. Documents alone do not change defaults — facilitated "
    "discussion of documents does."
)

doc.h2("Rule 2 — Trigger Phase 2 Content Contextually, Not In Advance")
doc.para(
    "The best time to give a process consultant the Incident Management How-To "
    "guide is 48 hours before their first Incident workshop — not during onboarding "
    "six weeks earlier. Context-triggered learning produces retention; pre-loading "
    "produces shelved documents. Use the sprint schedule as the delivery trigger: "
    "48 hours before each sprint, the consultant gets the how-to, the cheatsheets, "
    "and the facilitator guide for that sprint's disciplines."
)

doc.h2("Rule 3 — Make Phase 3 Visible via TBV Tools")
doc.para(
    "Culture does not stick unless management is checking. The Engagement Health "
    "Dashboard (INT-TBV-02) and Customization Variance Tracker (INT-TBV-03) are "
    "what convert Phase 3 from aspiration to standard. Once consultants know their "
    "EM reviews those dashboards weekly, the default behavior changes. The TBV tools "
    "are not auditing tools — they are coaching tools. The EM's job is to see the "
    "drift signal early enough to have a coaching conversation, not a corrective one."
)

doc.h2("Rule 4 — Close the Loop With Lessons Learned")
doc.para(
    "After each engagement's first sprint cycle (typically after Sprint 2), the "
    "practice lead runs a 60-minute lessons-learned session using INT-LL-01 and "
    "INT-LL-02 as the template. The patterns that emerge feed back into the "
    "cheatsheets and how-to guides as living updates. The library is not static — "
    "every engagement makes it better. This loop is what converts the library from "
    "a one-time build into a compounding practice asset."
)

doc.callout(
    "PHASED ROLLOUT FOR EXISTING TEAM: For consultants already mid-engagement, "
    "do not restart at Phase 1. Identify their current sprint and inject the Phase 2 "
    "materials for that sprint (facilitator guide + relevant cheatsheets). "
    "Run Phase 1 as a catch-up session at the next available engagement pause point "
    "(e.g., between Sprint 2 and Sprint 3). Retroactive onboarding is better than "
    "waiting for the next clean start."
)

# ─────────────────────────────────────────────────
# QUICK REFERENCE: PHASE 1 MINIMUMS BY ROLE
# ─────────────────────────────────────────────────
doc.h1("Quick Reference: Phase 1 Minimums by Role", numbered=True)
doc.para(
    "The table below is the single-page cheat sheet for practice leads running "
    "onboarding sessions. Every person in every role reads INT-CH-01 and INT-CH-04 "
    "at Phase 1. The role-specific additions are listed in the third column."
)
doc.table(
    headers=["Role", "Universal Phase 1 Docs", "Role-Specific Phase 1 Additions"],
    rows=[
        ["Engagement Manager",
         "INT-CH-01 (Decision Rights + Engagement Spine sections)\nINT-CH-04 OOTB-First Glossary",
         "INT-TBV-01 Manager's TBV Playbook\nINT-CH-03 Engagement Decision Rights Reference"],
        ["Solution Architect",
         "INT-CH-01 (OOTB-First Model + Engagement Spine sections)\nINT-CH-04 OOTB-First Glossary",
         "INT-AR-14 Custom-vs-OOTB Decision Framework Cheatsheet\nINT-HT-01 Platform Foundation How-To"],
        ["Process Consultant",
         "INT-CH-01 (Workshop Facilitation + OOTB Defense sections)\nINT-CH-04 OOTB-First Glossary",
         "INT-AR-01 Catalog Rationalization Cheatsheet\nINT-AR-03 SLA Discipline Cheatsheet\nINT-AR-14 Custom-vs-OOTB Decision Framework"],
        ["Developer",
         "INT-CH-01 (Customization Council + OOTB Configuration sections)\nINT-CH-04 OOTB-First Glossary",
         "INT-AR-14 Custom-vs-OOTB Decision Framework Cheatsheet"],
    ]
)

doc.para(
    "After Phase 1 is complete for a cohort, update the Consultant Onboarding "
    "Checklist (INT-CH-02) for each individual and file it with the engagement record. "
    "Phase 1 completion is a prerequisite for billing to an engagement in the "
    "OOTB-first model."
)

doc.save(OUT)
print(f"Saved: {OUT}")
