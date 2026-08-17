"""
build_ai_enablement_guidebook.py — ECS-AIE-01
AI Enablement Guidebook & Project Plan (Internal)
Built with EcsDocument from ecs_template.py per practice build rules.
Project: 04_Projects/ECS_WP_AIEnablement_2026
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ecs_template import EcsDocument, DocMeta, Brand

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(HERE, "everforth_logo.png")

doc = EcsDocument(
    meta=DocMeta(
        eyebrow="INTERNAL PRACTICE GUIDEBOOK",
        title="AI Enablement\nGuidebook & Project Plan",
        subtitle="Four engines, one governed foundation, and a phased plan that fits around the day job",
        org="ECS Federal · ServiceNow Practice",
        audience="Practice leadership and the AI capability working group",
        companion_to="OOTB Collateral Blueprint · Trust-But-Verify Playbook · Delivery Intelligence Platform blueprints",
        doc_id="ECS-AIE-01",
        version="1.1",
        status="Draft for working-group review",
        confidentiality="Internal Use Only · Confidential",
        running_header_label="Internal · AI Enablement Guidebook",
    ),
    logo_path=LOGO,
)

doc.add_cover_page()
doc.add_page_break()

# =========================================================================
# HOW TO USE
# =========================================================================
doc.h1("How to Use This Guidebook", numbered=False)
doc.para("This guidebook is the single reference for the practice's AI enablement effort. It does four things: it consolidates the team's capability wish-list into a small number of buildable engines; it inventories the collateral we have already built and defines how each shelf gets reviewed — by role, by lifecycle stage — before we automate on top of it; it names the gaps and foundational decisions the original list did not cover; and it lays out a prioritized, phased project plan that is honest about our constraint: a handful of people, all of whom have day jobs.")
doc.para("Read Sections 1–3 for the strategy. Sections 4–9 define the four engines, the meeting-intelligence evidence stream, and the builder-assistance applications, each with concrete build steps. Section 10 defines the collateral review program. Sections 11–12 cover gaps (including the library gap register) and foundations, including the AI Center of Excellence. Sections 13–16 are the plan itself: phases, ways of working, risks, and the first thirty days.")
doc.callout("The one-sentence version: we are not building twenty-seven tools — we are building four engines on top of a baseline library the team will review and ratify stage by stage, prioritized to fix our biggest gap first: new sales and the sales pipeline.")

# =========================================================================
# 1. WHY
# =========================================================================
doc.h1("Why This Effort, and Why Now")
doc.para("The goal is to use AI to improve how the practice operates across every function — capture, pre-sales, proposals, PMO, delivery, and customer partnership. Specifically, we want scalable capabilities the team can pick up and use when appropriate: to set projects up correctly from the start, to verify work efforts and deliverable status continuously rather than at review time, to surface indicators that guide decision making early, and to strengthen how we partner with customers.")
doc.para("Three realities shape the approach. First, the team's capability asks (twenty-seven items across three contributions, captured in Section 3) are strong but read as twenty-seven separate tools; built that way, each one would be a bespoke effort and most would stall. Second, we are not starting from zero: roughly 170 collateral artifacts have been cataloged and roughly 150 built, spanning capture through closeout. That library is a proposed baseline, not an accepted one — the team has not yet reviewed it, and this plan builds that review in stage by stage (Section 10) rather than assuming acceptance. Reviewed and ratified, it becomes our biggest asset: every AI capability gets seeded from it, and several become dramatically easier because of it. Third, this is a side-of-desk effort. The plan is sized for three to five people contributing four to eight hours a week each, shipping small increments continuously rather than promising big deliveries.")
doc.h2("What success looks like")
doc.bullet("A pipeline that fills itself: opportunities surfaced, qualified, and scored in days, not weeks — because new sales is our biggest gap, this comes first.")
doc.bullet("Proposals that start compliant: shred, compliance matrix, and outline generated within a day of a solicitation dropping.")
doc.bullet("Projects that start right: deliverables register, WBS, and tailored Sprint 0 kit generated from the award documents.")
doc.bullet("Delivery that verifies itself: stories, deliverables, and RIDAC items reconciled against meeting minutes and status data continuously.")
doc.bullet("Decisions guided by indicators: portfolio health, early warnings, and customer-value reporting produced from live data, not hand-built spreadsheets.")

# =========================================================================
# 2. COLLATERAL BASELINE
# =========================================================================
doc.h1("The Proposed Baseline — A Library Built, Not Yet Reviewed")
doc.para("A substantial collateral library has already been built for the practice — but the team has not yet reviewed it, and this guidebook does not assume it will be accepted as-is. Treat it as a proposed baseline: a strong starting position that earns its authority only through the stage-by-stage team review defined in Section 10. It matters for three reasons: once reviewed and ratified, it becomes the governed corpus the AI draws from; its templates and standards become the rulebooks the engines enforce; and its verification collateral — the Trust-But-Verify pack, UAT test packs, baseline story library — already encodes, in human-executed form, the kinds of checks we want to automate. The inventory below is summarized from the blueprint catalog (the source of truth for build status).")
doc.table(
    headers=["Lifecycle stage", "What exists today (built / cataloged)", "Marquee assets"],
    rows=[
        ["Capture & pre-sales", "Sales & Pre-Engagement bundle (7/7)", "Discovery Questionnaire + Interview Guide, ROI Calculator, AI License Realization talking points, Objection Handling Top 20, Pre-Sales Demo Script"],
        ["Proposal & SOW", "Proposal template + shared assets", "OOTB-first SOW/Proposal Template (INT-SP-05), Past Performances, Boilerplate, Company Quals, Why-OOTB whitepaper"],
        ["Award & Sprint 0", "Sprint 0 Setup (8/8), Project Plans (3/5)", "Sprint 0 Facilitator Playbook, 18-Week Master Project Plan, Roles & Expectations, Decision Rights, Onboarding Role-by-Phase Roadmap"],
        ["Delivery (Sprints 1–6)", "How-Tos (20/20), Cheatsheets (16/16), Facilitator Guides (13/15), Accelerator Packs (18/21), Decision Guides (15/15)", "JIT Baseline Story Library — 91 stories across 15 process areas; Adopt-vs-Re-engineer cheatsheets; Demo scripts; Workshop pre-reads"],
        ["Verification & PMO", "Trust-But-Verify pack (9/9), UAT packs (3/3); Steering & Governance 0/5", "TBV Playbook, Engagement Health Dashboard, Variance Tracker, Sprint Demo Audit — GAP: status report, risk/issue tracker, steering deck templates not yet built"],
        ["Closeout & hypercare", "Closeout pack (7/7), Lessons Learned (4/4)", "Go-Live Checklist, Operational Handoff Pack, SOP Library, Lessons-Learned + Customization Pattern Library, Quarterly Retro"],
        ["Practice governance", "Handbook (4/4), Onboarding (1/2)", "Consultant Handbook, Internal Governance Operating Guide, Role model + decision rights"],
    ],
    col_widths_in=[1.1, 2.2, 3.2],
)
doc.h2("What the proposed baseline changes about the AI effort")
doc.bullet("Document generation is nearly free. Every artifact is already script-built from a canonical brand template — the practice literally generates documents from structured inputs today. Engine 1 extends a working system rather than inventing one.")
doc.bullet("Story validation has a candidate baseline. The 91-story JIT library plus the adopt-vs-re-engineer cheatsheets and how-to guides are the raw material for the definition-of-complete library that story validation checks against — once the team has reviewed and shaped them.")
doc.bullet("Trust-But-Verify is a candidate reconciliation spec. The TBV pack defines a set of management checks; if the team confirms those are the right checks, Engine 3 automates them and the pack becomes the requirements document.")
doc.bullet("The collateral gaps are AI dependencies. The unbuilt Steering & Governance templates (weekly status report, risk/issue tracker) are precisely the structured evidence formats Engine 3 needs to reconcile against. Building them is now part of this plan, not a separate effort.")
doc.bullet("Nothing gets automated before it gets reviewed and ratified. A stage's shelf goes through team review — validate, challenge, or replace — immediately before we build capabilities on it. Section 10 defines that program, and review is a genuine decision gate, not a formality.")

# =========================================================================
# 3. CONSOLIDATION
# =========================================================================
doc.h1("The Consolidation — Twenty-Seven Asks, Four Engines")
doc.para("Three team contributions feed this consolidation: the original thirteen-item capability list, the story-validation gap a team member correctly flagged, and a second thirteen-item round covering proposal drafting, estimation, knowledge retrieval, people development, engineering assistance, and AI governance. Together they consolidate into four repeatable engines, one evidence stream, and one standing function. Almost every requested capability is one of these engines pointed at a different stage of the lifecycle — and the second round did something valuable: it named the fourth engine (knowledge retrieval) that the first round's capabilities quietly depended on. This is the central design decision of the whole effort: build the engine once, then configure it per stage, instead of building point tools.")
doc.table(
    headers=["Original ask", "Consolidates into"],
    rows=[
        ["Document Generator", "Engine 1 — Document Services"],
        ["Document QA", "Engine 1 — Document Services"],
        ["Document Anonymizer", "Engine 1 — Document Services"],
        ["Document Governance Alignment", "Engine 1 (QA with the governance corpus as rulebook)"],
        ["Solicitation Analysis / Bid–No-Bid", "Engine 2 — Shredder + scorecard output"],
        ["Proposal Compliance Matrix", "Engine 2 output; updates via Engine 3 reconciliation"],
        ["Proposal Response Generator", "Engine 2 output (outline from the shred)"],
        ["Award Deliverables", "Engine 2 — same shredder pointed at the award"],
        ["Award WBS Generator", "Engine 2 output, anchored to the 18-week master plan"],
        ["Project Deliverables Compliance Matrix", "Engine 3 — baseline vs. status evidence"],
        ["Project RIDAC Analysis", "Engine 3 — RIDAC log vs. project evidence"],
        ["Sprint/Story Planner + performance analysis", "Engine 3, seeded by the JIT story library"],
        ["Story Validation (team-flagged gap)", "Engine 3 + Definition-of-Complete library"],
        ["Meeting Notes / Agendas", "Evidence stream feeding Engine 3 (Section 8)"],
    ],
    col_widths_in=[3.0, 3.5],
)
doc.h2("The second-round asks and where they land")
doc.table(
    headers=["Second-round ask", "Consolidates into"],
    rows=[
        ["Proposal/RFP response drafting assistant", "Engines 1 + 4 — narrative drafts retrieved from past responses and boilerplate; writers edit, not write"],
        ["LOE / estimation copilot", "Engine 2 (structured estimate from the shred) + Engine 3 (delivery actuals feed the model); two-key pricing unchanged"],
        ["Internal knowledge base / RAG over practice artifacts", "Engine 4 — this ask named the fourth engine"],
        ["Best-practice and precedent research assistant", "Engine 4 (internal precedent + external research mode)"],
        ["New-hire / cross-training onboarding accelerator", "Engine 4 application — tutor over the ratified handbook and playbooks"],
        ["Resourcing and staffing-fit assistant", "Engine 4 over a skills/certs/history inventory (new data prerequisite)"],
        ["Client/engagement health signal monitoring", "Engine 3 portfolio configuration — velocity, rework, escalation signals; converges with the Delivery Intelligence Platform"],
        ["AI governance / internal center of excellence", "Standing function — the working group chartered as a lightweight CoE (Sections 12 and 14)"],
        ["AI-assisted code/config generation", "Builder assistance (Section 9), paired with OOTB/standards compliance checking"],
        ["Test case generation from requirements", "Builder assistance — closes the traceability thread from stories to tests"],
        ["Architecture and design review copilot", "Builder assistance — Engine 3 pointed at designs vs. standards and lessons learned"],
        ["Requirements-to-design translation assistant", "Builder assistance — Engines 1 + 4 producing first-pass designs and options analyses"],
        ["Client-facing artifact generation (diagrams, design docs)", "Engine 1 extension — polished visuals and documents from structured design decisions"],
    ],
    col_widths_in=[2.5, 4.0],
)
doc.h2("Operating principles")
doc.bullet("Engines, not point tools. Every new capability request gets mapped to an engine first; if it maps to none, it is a genuinely new engine and gets scrutinized accordingly.")
doc.bullet("The reviewed library is the corpus. AI outputs are seeded from, and checked against, collateral the team has reviewed and ratified — never from a blank page, and never from unreviewed material.")
doc.bullet("Human accountability is designed in. Every capability names who reviews and approves its output. AI drafts; named people decide.")
doc.bullet("Ship on live work. Capabilities are built and proven on a real pursuit or project, never on toy examples.")
doc.bullet("Sales first. Sequencing follows business impact, and our biggest gap is new sales and pipeline.")

# =========================================================================
# 4. ENGINE 1
# =========================================================================
doc.h1("Engine 1 — Document Services Layer")
doc.para("What it is: a horizontal service layer that produces, checks, and sanitizes documents against our own templates and rules. It unlocks four of the original asks — Generator, QA, Anonymizer, and Governance Alignment — as one system with different rulebooks. Every other engine emits its outputs through this layer, which is why it is the platform tier.")
doc.para("What we already have: the canonical brand system (ecs_template.py, pptx_brand.js, accelerator pack builder), roughly 150 script-built artifacts demonstrating the patterns, the brand standard, and the governance operating guide. The missing piece is not tooling — it is machine-readable specifications of what each document type must contain.")
doc.h2("Defined build steps")
doc.table(
    headers=["#", "Step", "Output"],
    rows=[
        ["1", "Inventory document types and pick the two or three highest-value first (proposal volume, SOW, status report)", "Ranked template list"],
        ["2", "Codify each into a template spec: required sections, elements, style rules, audience, footer rules", "Template spec sheets (the QA rubric and the generation instructions are the same artifact)"],
        ["3", "Build the Generator skill: spec + source content in, compliant draft out via the existing build system", "Generator capability + usage guide"],
        ["4", "Build the QA skill: document in, rubric-scored findings report out", "QA capability"],
        ["5", "Add the Anonymizer: PII/CUI pattern rules + mandatory human verification pass before anything leaves the boundary", "Anonymizer capability + release checklist"],
        ["6", "Assemble the governance corpus (org structure, R&R, RACI, vision/pillars, process frameworks) with a defined hierarchy; run alignment as QA with that rulebook", "Governance Alignment capability"],
        ["7", "Pilot each on a live document, measure findings quality and time saved, iterate, then publish with a named owner", "Published team skills"],
    ],
    col_widths_in=[0.35, 3.6, 2.55],
)
doc.callout("Definition of done for this engine: a teammate who did not build it produces a compliant draft and a QA report on a real document without help.")

# =========================================================================
# 5. ENGINE 2
# =========================================================================
doc.h1("Engine 2 — The Shredder (Obligation Extraction)")
doc.para("What it is: one extraction engine that turns a source document — solicitation, RFI, or award — into structured, traceable requirement records. Its outputs are the capabilities the team asked for: solicitation analysis with Bid/No-Bid scoring, the proposal compliance matrix, the response outline, the award deliverables register (explicit and implicit), and the WBS, charter, and comms plan starter set.")
doc.para("What we already have: the pursuit template's working rules already mandate a shred and compliance matrix — today it is manual. The Bid/No-Bid scorecard criteria can be codified from how we make those calls now; the WBS generator anchors to the 18-week master project plan and Sprint 0 playbook instead of inventing structure; the proposal outline anchors to the OOTB-first proposal template and win-theme discipline.")
doc.h2("Defined build steps")
doc.table(
    headers=["#", "Step", "Output"],
    rows=[
        ["1", "Define the standard requirement record: ID, source file, section reference, verbatim text, type (explicit/implicit), owner, response reference, status", "Requirement record schema — shared by every downstream output"],
        ["2", "Build the solicitation shred skill (Sections L/M/C, attachments, amendments) emitting requirement records", "Shredder capability"],
        ["3", "Codify the Bid/No-Bid scorecard with leadership: customer knowledge, incumbency, past-performance fit, capacity, price-to-win posture, teaming; weightings agreed once, applied every time", "Scored Bid/No-Bid brief per solicitation"],
        ["4", "Generate the compliance matrix and response outline from the shred; response updates reconcile via Engine 3", "Compliance matrix + outline capabilities"],
        ["5", "Point the same shredder at award documents to emit the deliverables register — explicit and implicit obligations", "Award deliverables capability"],
        ["6", "Generate WBS, charter, and comms plan drafts anchored to the 18-week master plan and Sprint 0 collateral", "Project setup generator"],
        ["7", "Calibrate: run against two or three past pursuits with known outcomes; compare AI shred to the human shred; tune until the deltas are acceptable", "Calibration report + trust baseline"],
    ],
    col_widths_in=[0.35, 3.6, 2.55],
)
doc.callout("Definition of done for this engine: a live solicitation is shredded, scored, and matrixed within one working day of drop, and the capture lead trusts the output enough to run the bid decision from it.")

# =========================================================================
# 6. ENGINE 3
# =========================================================================
doc.h1("Engine 3 — Reconciliation (Baseline vs. Evidence)")
doc.para("What it is: one engine that holds a structured baseline, ingests an evidence stream, and reports gaps, drift, and risk with citations back to the evidence. Configured per stage, it delivers the deliverables compliance matrix, RIDAC gap analysis, sprint/story performance analysis, the story validation the team flagged, and scope-creep detection. This engine is where 'verify work efforts and deliverable status' and 'indicators that guide decision making' actually live.")
doc.para("What we already have: the Trust-But-Verify pack is the candidate specification for this engine — once the verification-stage review confirms its checks are the right ones, they become the reconciliation rules. The JIT Baseline Story Library (91 stories, 15 process areas), adopt-vs-re-engineer cheatsheets, and how-to guides seed the definition-of-complete library, again subject to their stage review. The UAT packs define acceptance evidence. What is missing are the structured evidence formats — the unbuilt weekly status report and risk/issue tracker templates — which this plan builds as a dependency.")
doc.h2("Defined build steps")
doc.table(
    headers=["#", "Step", "Output"],
    rows=[
        ["1", "Define baseline formats: deliverables register (from Engine 2), story set, RIDAC log — structured enough to reconcile against", "Baseline schemas"],
        ["2", "Standardize evidence formats: build the missing status report and risk/issue tracker templates; define the structured meeting-minutes format (Section 7)", "Evidence templates (closes the SH-SG collateral gap)"],
        ["3", "Build the core reconciliation skill: baseline + evidence in, cited gap/risk report out", "Reconciliation capability"],
        ["4", "First configuration — deliverables compliance: award register vs. status evidence; flags missing, late, and at-risk deliverables", "Deliverables compliance matrix"],
        ["5", "Second configuration — story validation: baseline stories vs. requirement-session minutes, checked against the definition-of-complete library per ServiceNow artifact type (catalog item: variables AND categories, user criteria, descriptions, placement)", "Story validation + DoC library v1"],
        ["6", "Third and fourth configurations — RIDAC gap analysis and scope-creep detection (discussion vs. contracted scope)", "RIDAC + scope watch capabilities"],
        ["7", "Close the loop: every miss found in delivery updates the DoC library and baselines; sprint actuals feed the planner and future estimates", "The flywheel"],
    ],
    col_widths_in=[0.35, 3.6, 2.55],
)
doc.callout("Definition of done for this engine: an engagement manager gets a weekly, evidence-cited exception report — and the Trust-But-Verify audit that took hours takes minutes.")

# =========================================================================
# 7. ENGINE 4 — PRACTICE KNOWLEDGE
# =========================================================================
doc.h1("Engine 4 — Practice Knowledge (Ask the Library)")
doc.para("What it is: a retrieval layer over everything the practice knows — ratified collateral, design patterns, lessons learned, past responses, prior deliverables — so anyone can ask 'have we solved this before?' and get an answer with sources, instead of searching folders or relying on whoever has the longest memory. The first three engines make things; this one makes everything we know findable. It unlocks the knowledge-base ask directly, and it quietly powers several others: proposal narrative drafting retrieves from past responses, precedent research retrieves from lessons learned and patterns, the onboarding tutor retrieves from the handbook and playbooks, and staffing-fit retrieves from a skills inventory.")
doc.para("What we already have: the library itself is the substrate, and the review program is what makes retrieval trustworthy — answers are only as good as the corpus, which is exactly why ratification matters. The lessons-learned pack, customization pattern library, and knowledge repository index are purpose-built for this. What is missing is the retrieval layer itself, and — just as important — the directions: people will not use what they do not know how to ask.")
doc.h2("Defined build steps")
doc.table(
    headers=["#", "Step", "Output"],
    rows=[
        ["1", "Confirm the substrate: the governed corpus from Phase 0, with every indexed item carrying its review verdict; answers always cite source and verdict", "Indexing rules"],
        ["2", "Stand up retrieval in the approved AI environment — the Phase 0 CUI/data-handling rule governs what may be indexed", "Working retrieval layer"],
        ["3", "Version one — Ask the Library: capture and proposal shelves plus lessons learned, launched alongside their stage reviews", "First queryable slice"],
        ["4", "Write the directions: a one-page user guide per audience — what it is good for, what it is not, twenty example questions that work, and how to read a cited answer", "Usage guides + example-question library"],
        ["5", "Add precedent and research mode: internal patterns and lessons first, external best practice second, always labeled which is which", "Research assistant"],
        ["6", "Add the onboarding tutor: a guided persona over the ratified handbook and playbooks — safe to query without live client access; shortens time-to-productive and eases moves between engagements", "Onboarding accelerator"],
        ["7", "Extend the index to a skills, certifications, and project-history inventory (a new data set the practice does not have today) to power staffing-fit suggestions", "Staffing-fit assistant"],
        ["8", "Measure: questions asked, answer usefulness, citation correctness, and reinvention avoided; misses feed the corpus curation list", "Adoption + quality loop"],
    ],
    col_widths_in=[0.35, 3.9, 2.25],
)
doc.callout("Definition of done for this engine: a consultant on their second day, or an architect starting an unfamiliar problem, gets a useful, cited answer in one try — because the directions taught them what to ask.")

# =========================================================================
# 8. MEETING INTELLIGENCE
# =========================================================================
doc.h1("Meeting Intelligence — The Evidence Stream")
doc.para("The original list treats meeting agendas and notes as a convenience feature. They are more than that: meetings are the richest evidence stream Engine 3 has. The story-validation gap proves it — the miss is detected precisely by comparing baseline stories against what was actually discussed in requirements sessions. So this capability is scoped as structured capture, not just note-taking.")
doc.bullet("Agendas generated from the engagement's collateral (facilitator guides, decision topic guides) and the current reconciliation exceptions — the agenda is what needs deciding, not a blank page.")
doc.bullet("Minutes captured in a structured format: decisions, action items, commitments, scope signals, and configuration details tagged so Engine 3 can consume them directly.")
doc.bullet("Follow-ups and actions flow into the RIDAC log automatically, closing the loop between conversation and record.")
doc.para("Build steps are deliberately light: define the structured minutes format alongside the Engine 3 evidence templates, pilot it in one engagement's cadence meetings, then generate agendas from exceptions once reconciliation is live.")

# =========================================================================
# 9. BUILDER ASSISTANCE
# =========================================================================
doc.h1("Builder Assistance — The Engines Applied to Design and Build Work")
doc.para("The second-round list surfaced a family the first round missed: assistance for the people doing technical design and configuration work — solution architects, process consultants, and technical consultants. These are not new engines; they are the same four engines pointed at technical work products instead of documents and deliverables. The guardrails are the same too: every output is a draft, every draft is checked against our standards, and a named human owns what ships.")
doc.table(
    headers=["Capability", "How it works", "Who benefits"],
    rows=[
        ["Requirements-to-design translation", "Engines 1 + 4: raw requirements in, a structured first-pass solution design or options analysis out, following a repeatable design template regardless of which architect is writing", "SAs — compresses the blank-page phase; delivery — consistent design structure"],
        ["Architecture and design review copilot", "Engine 3: proposed design reconciled against internal standards, adopt-vs-re-engineer guidance, and lessons learned; surfaces questions before formal review", "Tech leads — deeper reviews without more of their time; the practice — one shared definition of 'good'"],
        ["Code/config generation and pairing", "Scaffolds configuration, scripts, and integrations from a validated story; paired with the standards-compliance check so generated work is born compliant, not remediated later", "Developers — senior-quality first drafts; the practice — throughput without matching headcount growth"],
        ["Test case generation", "Engine 3 traceability: acceptance criteria and stories in, draft test scenarios out, feeding the existing UAT pack structure", "QA and delivery — coverage consistency; fewer 'we forgot to test that' defects"],
        ["Client-ready diagrams and design docs", "Engine 1 extension: structured design decisions converted to polished, brand-compliant diagrams and documentation", "SAs — design time spent on design, not formatting"],
    ],
    col_widths_in=[1.5, 3.0, 2.0],
)
doc.para("Sequencing note: these land in Phases 3–4, after the shredder and reconciliation cores exist, because each one leans on them — designs trace to shredded requirements, reviews reconcile against ratified standards, and tests trace to validated stories.", italic=True)

# =========================================================================
# 10. COLLATERAL REVIEW PROGRAM
# =========================================================================
doc.h1("Collateral Review — By Role, By Stage")
doc.para("Before any stage's capabilities are built, that stage's shelf goes through team review by the people who own that stage in practice. This is the first time the team formally reviews the library, so the review carries real authority: reviewers are expected to validate what holds up, challenge what does not, and replace what should be different — acceptance is an outcome of the review, not its starting assumption. The review serves three purposes: it turns a one-author library into a team-owned baseline; it keeps that baseline honest (the AI amplifies whatever it is fed — unvetted collateral becomes unvetted automation); and it makes each artifact AI-ready, meaning structured enough for an engine to consume as a template, rulebook, or baseline. Reviews are scheduled just-in-time, in the phase immediately before the stage is automated, so the effort stays small and the review is fresh when it matters.")
doc.h2("The four review questions")
doc.bullet("Right — do we agree this artifact reflects how we should work and what we sell today? If not, what changes?")
doc.bullet("Complete — is anything missing at this stage that the AI capability will need (the steering/governance gap is the model example)?")
doc.bullet("AI-ready — is it structured enough to serve as a template spec, rulebook, or baseline, or does it need conversion?")
doc.bullet("Connected — which engine consumes it, and is that documented in the collateral-to-capability map?")
doc.h2("Review assignments by stage and role")
doc.table(
    headers=["Stage (review timing)", "Shelf under review", "Lead reviewer", "Feeds"],
    rows=[
        ["Capture & pre-sales (Phase 0)", "Discovery questionnaire + interview guide, ROI calculator, talking points, objection handling, demo script", "Sr. Director (capture) + Practice Lead", "Opportunity briefs, Bid/No-Bid context, Engine 2"],
        ["Proposal & SOW (Phase 2 entry)", "Proposal/SOW template, boilerplate, past performances, quals, whitepaper", "Sr. Director + proposal leads", "Engine 1 template specs, Engine 2 outline"],
        ["Award & Sprint 0 (Phase 3 entry)", "Sprint 0 playbook + setup pack, 18-week master plan, roles & expectations, decision rights", "Engagement Manager / Project Lead + Solution Architect", "Engine 2 WBS/charter, project setup kit"],
        ["Delivery Sprints 1–6 (Phase 4 entry)", "JIT story library, how-to guides, adopt-vs-re-engineer cheatsheets, facilitator guides, accelerator packs, decision guides", "Solution Architect + BPC/BA", "Engine 3 story validation, DoC library"],
        ["Verification & PMO (Phase 4 entry)", "Trust-But-Verify pack, UAT packs; build the missing status report + risk/issue tracker", "Engagement Manager + Practice Lead", "Engine 3 reconciliation rules + evidence formats"],
        ["Closeout & hypercare (Phase 5 entry)", "Closeout pack, lessons-learned + customization pattern library, quarterly retro", "Engagement Manager", "Flywheel: lessons to estimates and bid scoring"],
        ["Practice governance (Phase 0, then quarterly)", "Handbook, governance operating guide, R&R/RACI, brand standard", "Practice Lead", "Engine 1 governance alignment corpus"],
    ],
    col_widths_in=[1.35, 2.35, 1.4, 1.4],
)
doc.para("Each review produces three things: a verdict per artifact (ratified / needs update / replace / gap), a short update list executed inside the phase, and an entry in the collateral-to-capability map so the connection between shelf and engine is explicit. Only ratified artifacts enter the governed corpus. The map lives in the project folder and becomes part of the corpus itself.")

# =========================================================================
# 9. GAPS
# =========================================================================
doc.h1("Gaps and Recommendations")
doc.para("The original list starts at 'solicitation in hand' and stops mid-delivery. The gaps cluster in four groups; the first is the priority because it is where our biggest business gap is.")
doc.h2("Front of the lifecycle — new sales and pipeline (priority)")
doc.bullet("Opportunity pipeline monitoring: standing scans of SAM.gov, agency forecasts, and recompete timelines producing a qualification brief per hit — the pipeline should fill before a solicitation ever drops.")
doc.bullet("Capture intelligence: incumbent and competitor context assembled per opportunity, feeding the Bid/No-Bid scorecard rather than living in someone's head.")
doc.bullet("Past-performance matching: given an opportunity, retrieve and tailor the best-fit narratives from the PP library; promote approved narratives back into the shared shelf.")
doc.bullet("Key-personnel and resume tailoring against labor category requirements.")
doc.bullet("Evaluator simulation: score draft responses the way the government scores — against Section M — as a color-review accelerator; the compliance matrix alone only proves Section L.")
doc.bullet("Amendment and Q&A impact analysis: when an amendment drops, identify what changed and what in our response it touches.")
doc.bullet("Basis-of-estimate support fed by delivery actuals — evidence for the humans who own pricing, consistent with the two-key pricing model.")
doc.h2("Back of the lifecycle")
doc.bullet("Status report generation from the same data the compliance matrix consumes — reporting becomes a byproduct, not a chore.")
doc.bullet("Scope-creep detection: meeting evidence reconciled against contracted scope, flagged early, protecting both margin and the relationship.")
doc.bullet("Test and acceptance generation: validated stories feeding the existing UAT pack structure.")
doc.bullet("OOTB configuration compliance: proposed configuration checked against our adopt-vs-re-engineer standards — the most differentiated capability we could build, and entirely on-brand.")
doc.bullet("Closeout automation: tailoring the closeout pack per engagement; harvesting lessons learned into the flywheel; CPARS self-assessment preparation.")
doc.h2("Indicators and customer partnership")
doc.bullet("Portfolio health roll-up with early-warning indicators — converges deliberately with the Delivery Intelligence Platform app initiative rather than duplicating it.")
doc.bullet("Customer-facing value reporting and QBR generation: delivery data turned into the partnership narrative.")
doc.bullet("Relationship signals mined from meeting and communication streams.")
doc.h2("Foundations the list assumed but did not name")
doc.bullet("A governed corpus with a curation owner (Section 12).")
doc.bullet("A CUI and data-handling policy decided before rollout, not after.")
doc.bullet("A human accountability model — an R&R/RACI for AI use itself, now formalized as the lightweight CoE (Section 12).")
doc.bullet("A structured skills, certifications, and project-history inventory — the data behind both staffing-fit and key-personnel/resume tailoring does not exist today except as tribal knowledge.")
doc.bullet("Measurement and feedback loops: win/loss recalibrating the bid scorecard, delivery actuals feeding estimates, validation misses updating the DoC library.")
doc.bullet("Packaging and directions: every capability ships as a documented, self-serve skill with an owner and a one-page user guide — people will not use what they do not know how to ask for. Scalability is a packaging problem as much as a capability problem.")
doc.h2("The library gap register — what the shelf itself is missing")
doc.para("The capability gaps above are about what the AI should do. This register is about the collateral: artifacts the library needs corrected or added, found by comparing the catalog, the actual files on disk, and what the engines and the sales-first plan will require. It pre-seeds the stage reviews — reviewers confirm, amend, or strike these entries rather than starting from a blank page. Items marked with an asterisk are already cataloged as planned-but-unbuilt; the rest are new adds this effort surfaced.")
doc.table(
    headers=["Stage", "Correct or add"],
    rows=[
        ["Capture & pre-sales", "Opportunity qualification brief template; capture plan template; Bid/No-Bid scorecard as a real artifact (criteria + weightings); competitor/incumbent intel one-pager; win/loss debrief template"],
        ["Proposal & SOW", "Proposal volume templates beyond the SOW (technical, management, staffing); compliance matrix template; color-review checklist; win-theme worksheet; key-personnel/resume template; basis-of-estimate model template (feeds the estimation copilot)"],
        ["Award & Sprint 0", "Sprint burndown* and dependency-tracking* templates; the missing Sprint 0 customer-readiness item*; engagement-shape variants or a tailoring guide for the 18-week plan — not every award is the same shape, and the plan baseline must flex to the RFP's objectives"],
        ["Delivery", "Definition-of-complete checklist library per artifact type; solution design document + options analysis templates; design review checklist (feeds the review copilot); generic RIDAC/RAID log template (risk register exists, the full log does not); SIT test template"],
        ["Verification & PMO", "The entire steering & governance set*: steering committee deck, customization council deck, weekly status report, change request template, risk/issue tracker — all five are also Engine 3 evidence-format dependencies"],
        ["Closeout & hypercare", "CPARS self-assessment preparation template; customer QBR / value report template — the partnership narrative artifact the current pack lacks"],
        ["Practice governance", "Practice rollout staging plan*; template spec sheets (Engine 1's rulebooks); governance hierarchy map (which document governs which); structured meeting minutes format; prompt/pattern registry; skills/certs inventory"],
        ["Cross-cutting", "Catalog-to-disk reconciliation: several items the catalog marks as planned already exist on disk (and counts drift the other way too) — a one-time audit in Phase 0 makes the catalog trustworthy again"],
    ],
    col_widths_in=[1.3, 5.2],
)

# =========================================================================
# 10. FOUNDATIONS
# =========================================================================
doc.h1("Foundations First")
doc.h2("The governed corpus")
doc.para("Every engine reads from a curated set of authoritative sources: reviewed collateral, governance documents, template specs, past performances, and baselines. Phase 0 stands up version one from the existing library as a proposed baseline — the work is curation and structure, not creation — but artifacts only become authoritative as their stage review ratifies them. One named owner curates the corpus; the stage reviews in Section 10 are both the ratification gate and the ongoing maintenance mechanism. Anything not ratified into the corpus is not authoritative, and the AI is instructed accordingly.")
doc.h2("CUI and data handling")
doc.para("Solicitations, awards, and project data can carry CUI and sensitive customer information. Before any capability touches live pursuit data, leadership decides which AI environment is approved for which data classes, and writes it as a one-page rule everyone can follow. The anonymizer supports distribution of outputs; the environment decision governs inputs. This is a Phase 0 exit criterion — deliberately boring, deliberately first.")
doc.h2("Human accountability")
doc.para("Every capability names an accountable reviewer role in its capability card: the capture lead owns bid decisions, the proposal manager owns what goes in a response, the engagement manager owns what a customer sees, pricing follows the existing two-key model. AI output is a draft until the named human accepts it. This mirrors the practice's existing decision-rights discipline — the same rulebook the governance-alignment capability enforces.")
doc.h2("The AI Center of Excellence — lightweight, but real")
doc.para("The second-round list asked for it by name, and it is the right call: the working group doubles as a lightweight AI center of excellence. Not a new org — the same few people, wearing one more hat with three duties. Vet: new AI asks come through the CoE and get mapped to an engine (or parked with a reason — the intake rule that keeps the backlog honest). Standardize: prompts, patterns, and capability configurations live in a versioned registry in the repo, not in personal notebooks, so individual experimentation becomes shared capability instead of silos. Share: every capability ships with its one-page user directions and gets a five-minute demo at the build sync — adoption is a CoE duty, not an afterthought. The CoE also owns the compliance edge: it is the standing checkpoint that the CUI rule and the accountable-reviewer model are actually being followed as tools multiply.")
doc.h2("Measurement")
doc.para("Each phase defines its measures up front (they appear in Section 13). Beyond phase measures, three standing indicators tell us whether the effort itself is working: adoption (who used which capability this month), cycle time (shred-to-bid-decision, proposal cycle, project setup time), and trust (how often reviewers accept output with minor edits versus rework). If adoption stalls, we fix the capability or retire it — shelf-ware is the failure mode this plan is designed against.")

# =========================================================================
# 11. PROJECT PLAN
# =========================================================================
doc.h1("The Project Plan")
doc.h2("Capacity and pacing")
doc.para("Planning assumption: three to five people contributing four to eight hours per week each — roughly twenty committed hours a week in aggregate, about the capacity of half a person. Everyone has a day job, and the day job wins in a crunch. The plan absorbs that reality three ways: increments are sized to ship something usable every two to three weeks; every phase has a minimum viable scope that survives a bad month; and dates are expressed in months with explicit pause rules (Section 14) instead of pretending to week-level precision. At this capacity the full arc runs roughly twelve months; that is expected, and the phases are sequenced so value lands from Phase 1 onward, not at the end.")
doc.para("One more honest sentence, added as the capability list grew: more ideas did not create more capacity. The backlog now holds more than the twelve-month arc can carry, and that is fine — the phases hold their minimum viable scope, the CoE intake rule keeps new asks from displacing committed work, and anything beyond the arc waits its turn or waits for the team to grow. A longer backlog is a sign of engagement, not a schedule commitment.")
doc.h2("Why this order")
doc.para("New sales and pipeline is the biggest business gap, so the front of the lifecycle comes first — Phase 1 is entirely capture-side, and Phase 2 accelerates proposals. Project setup and delivery verification follow, because they compound on Engine 2's outputs and because existing human processes (Trust-But-Verify) cover delivery today. Indicators and the flywheel come last not because they matter least but because they consume everything built before them.")

doc.h2("Phase 0 — Foundations (Month 1)")
doc.para("Decisions and scaffolding; deliberately small.", italic=True)
doc.bullet("Name the working group, capability owners, and the weekly one-hour build sync — and charter the group's CoE hat: intake rule, prompt/pattern registry started, adoption duty.")
doc.bullet("Decide the approved AI environment and write the one-page CUI/data-handling rule (leadership sign-off).")
doc.bullet("Stand up corpus v1 from the existing library as the proposed baseline — explicitly pending stage-by-stage ratification; name the curation owner.")
doc.bullet("Run the capture-stage and practice-governance collateral reviews (Section 10) — the shelves Phase 1 builds on.")
doc.bullet("Ratify the capability backlog and Phase 1 scope; pick one live opportunity as the pilot.")
doc.para("Exit criteria: environment decided, data rule signed, corpus v1 standing, capture shelf reviewed, pilot opportunity chosen. Measures: none yet — this phase is judged on its exit criteria alone.")

doc.h2("Phase 1 — Fill the Pipeline (Months 2–4)")
doc.para("Entirely capture-side; the sales gap is the target.", italic=True)
doc.bullet("Opportunity monitor and qualification brief: standing SAM.gov and forecast scans producing a one-page brief per hit, packaged into a weekly pipeline review.")
doc.bullet("Solicitation shredder plus Bid/No-Bid scorecard (Engine 2 steps 1–3), calibrated against two or three past pursuits.")
doc.bullet("Past-performance matcher over the PP library.")
doc.bullet("Execute the capture-shelf update list from the Phase 0 review (ROI calculator and objection-handling content feed the briefs).")
doc.para("Measures: qualified opportunities per month; days from solicitation drop to bid decision; percentage of bid decisions made with the scorecard; pipeline value reviewed weekly.")

doc.h2("Phase 2 — Propose Faster, Win More (Months 4–6)")
doc.para("Proposal-stage shelf review at entry.", italic=True)
doc.bullet("Compliance matrix and response outline generation from the shred (Engine 2 steps 4).")
doc.bullet("Document Generator and QA v1 for proposal volumes (Engine 1 steps 1–4), specs seeded from the proposal template.")
doc.bullet("Proposal narrative drafting assistant: technical narrative sections drafted from the past-response and boilerplate library (Engines 1 + 4) — writers edit instead of starting from scratch, and senior staff spend their hours on differentiation and win strategy.")
doc.bullet("LOE / estimation copilot v1: backlog or requirements in, structured first-draft estimate model out — consistent sizing across engagements, less dependence on any one person's memory of 'how we usually size this.' Two-key pricing decision rights unchanged: the copilot produces evidence, humans own the number.")
doc.bullet("Ask the Library v1 (Engine 4): retrieval over the ratified capture and proposal shelves plus lessons learned — shipped with its user directions and example-question guide.")
doc.bullet("Evaluator simulation against Section M as the color-review accelerator.")
doc.bullet("Anonymizer v1 with the mandatory human verification pass.")
doc.para("Measures: proposal cycle time; compliance findings at color review trending down; past-performance reuse rate; estimate variance across estimators; Ask-the-Library questions per week.")

doc.h2("Phase 3 — Start Projects Right (Months 7–8)")
doc.para("Award and Sprint 0 shelf review at entry.", italic=True)
doc.bullet("Award shredder emitting the explicit-and-implicit deliverables register (Engine 2 step 5).")
doc.bullet("WBS, charter, and comms plan generation anchored to the 18-week master plan (Engine 2 step 6).")
doc.bullet("Project setup kit: existing Sprint 0 collateral auto-tailored to the award — shaped by the RFP's objectives, since not every engagement runs the same delivery model.")
doc.bullet("Requirements-to-design translation assistant: shredded requirements into a first-pass solution design or options analysis on the standard design template (builder assistance, Section 9).")
doc.para("Measures: project setup time from award to kickoff-ready; percentage of deliverables baselined at kickoff; design-draft turnaround time.")

doc.h2("Phase 4 — Deliver and Verify (Months 9–12)")
doc.para("Delivery and verification shelf reviews at entry; the Trust-But-Verify pack becomes the reconciliation spec.", italic=True)
doc.bullet("Build the missing evidence templates — weekly status report and risk/issue tracker — closing the steering-and-governance collateral gap (Engine 3 step 2).")
doc.bullet("Meeting intelligence: structured minutes format piloted in one engagement's cadence.")
doc.bullet("Deliverables compliance reconciliation; then story validation with the definition-of-complete library seeded from the JIT story library and cheatsheets; then RIDAC gap analysis and scope-creep detection.")
doc.bullet("Builder assistance wave (Section 9): test-case generation from validated stories; the design review copilot checking designs against ratified standards and lessons learned; code/config scaffolding paired with the standards-compliance check; client-ready diagram and design-doc generation.")
doc.para("Measures: at-risk deliverables flagged at least two weeks before due; story rework rate; time to complete a Trust-But-Verify audit; test-coverage consistency; design-review findings caught before formal review.")

doc.h2("Phase 5 — Indicators and the Flywheel (Month 12 onward)")
doc.para("Closeout shelf review at entry; converges with the Delivery Intelligence Platform initiative.", italic=True)
doc.bullet("Portfolio health roll-up and early-warning indicators for the monthly practice review — velocity, rework, and escalation signals flagging engagements trending toward risk before the status meeting does.")
doc.bullet("Customer-facing value reporting and QBR generation.")
doc.bullet("People capabilities on Engine 4: the onboarding tutor over the ratified handbook and playbooks (safe to query, no client environment needed), and the staffing-fit assistant once the skills/certs/history inventory exists — faster, more defensible staffing and skill gaps surfaced before they become delivery risk.")
doc.bullet("Feedback loops: win/loss analysis recalibrating the bid scorecard; lessons learned harvested into estimates and the DoC library; closeout pack tailoring; estimation copilot recalibrated from delivery actuals.")
doc.bullet("Governance alignment rolled out across document flows.")
doc.para("Measures: indicators used in the monthly review; lessons-learned items demonstrably feeding bid and estimate decisions; time-to-productive for new or transitioning staff.")

doc.h2("The capability backlog at a glance")
doc.table(
    headers=["Capability", "Engine", "Phase", "Size"],
    rows=[
        ["Opportunity monitor + qualification brief", "2 + corpus", "1", "M"],
        ["Solicitation shredder", "2", "1", "M"],
        ["Bid/No-Bid scorecard", "2", "1", "S"],
        ["Past-performance matcher", "2 + corpus", "1", "S"],
        ["Compliance matrix + response outline", "2", "2", "M"],
        ["Document generator + QA (proposal volumes)", "1", "2", "M"],
        ["Evaluator simulation (Section M)", "2", "2", "S"],
        ["Anonymizer", "1", "2", "S"],
        ["Award deliverables register", "2", "3", "S"],
        ["WBS / charter / comms generator", "2", "3", "M"],
        ["Project setup kit tailoring", "1 + 2", "3", "S"],
        ["Evidence templates (status report, risk tracker)", "3", "4", "S"],
        ["Meeting intelligence (structured capture)", "3", "4", "M"],
        ["Deliverables compliance reconciliation", "3", "4", "M"],
        ["Story validation + DoC library", "3", "4", "L"],
        ["RIDAC gap analysis", "3", "4", "S"],
        ["Scope-creep detection", "3", "4", "S"],
        ["Proposal narrative drafting assistant", "1 + 4", "2", "M"],
        ["LOE / estimation copilot", "2 + 3", "2", "M"],
        ["Ask the Library (practice retrieval) + user directions", "4", "2", "M"],
        ["Requirements-to-design translation assistant", "1 + 4", "3", "M"],
        ["Test-case generation from stories", "3", "4", "S"],
        ["Design review copilot", "3 + 4", "4", "M"],
        ["Code/config scaffolding + standards check", "1 + 3", "4", "M"],
        ["Client-ready diagram / design-doc generation", "1", "4", "S"],
        ["Portfolio health indicators", "3", "5", "M"],
        ["QBR / value reporting", "1 + 3", "5", "M"],
        ["Onboarding tutor", "4", "5", "M"],
        ["Skills inventory + staffing-fit assistant", "4", "5", "M"],
        ["Win/loss + lessons feedback loops", "3", "5", "M"],
        ["Governance alignment rollout", "1", "5", "M"],
    ],
    col_widths_in=[3.3, 1.1, 0.9, 1.2],
)
doc.para("Sizes are working-group effort at our capacity: S is one to two increments (two to four weeks of side-of-desk work), M is three to four, L is five or more and should be split before it is started.", italic=True, size=10)

# =========================================================================
# 12. WAYS OF WORKING
# =========================================================================
doc.h1("Ways of Working")
doc.bullet("Cadence: one 60-minute build sync per week — demo what shipped, unblock what stalled, commit the next increment. If the sync produces no demo three weeks running, the phase scope gets cut, not the quality bar.")
doc.bullet("Ownership: every capability has exactly one owner and one tester; the tester is always someone who did not build it.")
doc.bullet("Increment rule: nothing in flight longer than three weeks. If it will not ship in three weeks, split it.")
doc.bullet("Capability card: each capability gets a one-page card — purpose, engine, inputs, outputs, accountable reviewer role, corpus sources, and its definition of done. The card is the documentation the team self-serves from.")
doc.bullet("User directions ship with the capability: a one-page how-to in plain language — what it's for, what it isn't, example inputs that work, and how to judge the output. The builder's documentation is not the user's directions; both are required.")
doc.bullet("CoE intake: new AI asks route through the working group, get mapped to an engine, and enter the backlog with a phase — or get parked with a written reason. No side-channel builds.")
doc.bullet("Definition of done: documented as a skill, tested on a real artifact by the non-building tester, accountable reviewer named, user directions written, filed in the shared library and prompt/pattern registry, owner assigned. Not before.")
doc.bullet("Live-work rule: every capability is proven on an active pursuit or engagement before it is called done.")
doc.bullet("Pause rule: when day-job load spikes, the working group formally pauses at an increment boundary and records the restart point — a clean pause beats a slow fade, and the plan survives it because value ships at every phase.")

# =========================================================================
# 13. RISKS
# =========================================================================
doc.h1("Risks and Mitigations")
doc.table(
    headers=["Risk", "Mitigation"],
    rows=[
        ["Day-job crunch stalls the effort", "Small increments, minimum viable phase scope, formal pause rule, visible wins from Phase 1 to sustain sponsorship"],
        ["CUI or sensitive data mishandled", "Environment decision and one-page rule before any live data (Phase 0 exit criterion); anonymizer with human verification; approved-environment-only processing"],
        ["AI output trusted too much, or too little", "Calibration runs against known outcomes; named accountable reviewer per capability; trust measured as accept-vs-rework rate"],
        ["Unreviewed or stale corpus amplified at scale", "Only ratified artifacts enter the corpus; named curation owner; just-in-time stage reviews (Section 10); quarterly governance-shelf review"],
        ["Baseline review becomes a rubber stamp — or a rewrite that never ends", "Review verdicts are explicit (ratify / update / replace / gap); updates are timeboxed inside the phase; disagreements escalate to the practice's existing decision-rights model"],
        ["Capabilities become shelf-ware", "Built on live work with the people who will use them; adoption measured monthly; unused capabilities fixed or retired"],
        ["Knowledge concentrated in one builder", "One-owner-one-tester rule; capability cards as documentation; skills published, not scripts on laptops"],
        ["Effort duplicates the Delivery Intelligence Platform app", "Phase 5 explicitly converges with the app initiative; the app is the indicator surface, this effort feeds it"],
        ["Growing backlog displaces committed work", "CoE intake rule: every new ask maps to an engine and takes a place in line; phases keep minimum viable scope; backlog re-prioritized quarterly, not per request"],
        ["Capabilities built but not used because nobody knows how", "User directions are part of definition of done; five-minute demo at the build sync per shipped capability; adoption measured monthly by the CoE"],
    ],
    col_widths_in=[2.5, 4.0],
)

# =========================================================================
# 14. FIRST 30 DAYS
# =========================================================================
doc.h1("The First Thirty Days")
doc.bullet("Week 1 — Name the working group and capability owners; put the weekly build sync on the calendar; confirm the backlog and Phase 1 scope from this guidebook.")
doc.bullet("Week 2 — Decide the approved AI environment; draft and sign the one-page CUI/data-handling rule; name the corpus curation owner.")
doc.bullet("Week 3 — Stand up corpus v1 from the existing library; begin the capture-stage collateral review with the Section 10 questions.")
doc.bullet("Week 4 — Finish the capture review and its update list; pick the live pilot opportunity; commit the first Phase 1 increment (the opportunity qualification brief) at the build sync.")
doc.para("Thirty days from now the effort has an environment, a rule, a corpus, a reviewed capture shelf, and a first increment in flight against a real opportunity. That is the whole point of this plan: small, governed, and already producing.")

out = os.path.join(HERE, "ECS_AI_Enablement_Guidebook_and_Project_Plan_v1.1.docx")
doc.save(out)
print("Saved:", out)
