"""
Build INT-CH-01 — Consultant Handbook (v1 skeleton)

The master playbook every ECS consultant on the practice reads in full before their
first engagement. v1 is a SKELETON: every section has its H1/H2 scaffolding plus a
focused opening paragraph stating what the section will cover. Content gets filled in
over subsequent sessions as the practice converges on language.

Companions to build immediately after this one (tightly coupled):
  - INT-CH-02 — Consultant Onboarding Checklist
  - INT-CH-03 — Engagement Decision Rights Reference
  - INT-CH-04 — OOTB-First Glossary
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

OUT = os.path.join(HERE, "Consultant_Handbook_INTERNAL.docx")

# =============================================================================
# Cover meta
# =============================================================================
doc = EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL CONSULTANT HANDBOOK · MASTER PLAYBOOK",
    title="ECS Consultant\nHandbook",
    subtitle="The master playbook every ECS consultant reads before their first engagement on the OOTB-first ServiceNow practice",
    audience="All ECS Federal ServiceNow Practice roles — Engagement Managers, Solution Architects, Process Consultants, Developers, Practice Lead",
    companion_to="ECS Internal Governance Operating Guide · Manager's Trust-But-Verify Playbook (INT-TBV-01) · OOTB Delivery Playbook · Accelerator Pack Blueprint",
    doc_id="INT-CH-01",
    version="1.0 (skeleton)",
    status="Skeleton — Released for fill-in",
    running_header_label="Internal · ECS Consultant Handbook",
))

doc.add_cover_page()

# Cover-page opener
doc.para(
    "This Handbook is the operational backbone of the ECS Federal ServiceNow practice. It captures how the "
    "practice delivers the 18-week OOTB-first engagement: the model we sell, the disciplines that make it work, "
    "the decision rights we operate against, the workshops we run, and the way we hand off at go-live. Every "
    "consultant on the practice reads this in full before their first engagement, and returns to it whenever "
    "the work pulls them toward a customization, a custom workflow, or a scope expansion."
)
doc.para(
    "Version 1.0 is a skeleton. Each section is anchored by a focused opening paragraph that states what the "
    "section will cover. Subsequent versions fill in the substance as the practice converges on field-tested "
    "language. The Practice Lead is the document owner; field experience and lessons-learned route through the "
    "quarterly retro into Handbook updates."
)

# =============================================================================
# Section 0 — How to Use This Handbook (unnumbered)
# =============================================================================
doc.h1("How to Use This Handbook", numbered=False)
doc.para(
    "This section orients new readers to the Handbook's structure, the read order by role, and the relationship "
    "between this document and the rest of the practice library. Read this section first; the rest of the Handbook "
    "is structured to be read in order, but experienced consultants can jump to the discipline section relevant to "
    "their current engagement phase."
)
doc.para("Read order by role:", bold=True, space_after=2)
doc.bullet("Engagement Manager — read in full. Pay closest attention to Sections 2 (engagement spine), 3 (decision rights), 5 (Trust-But-Verify cross-ref), and 9 (escalation).")
doc.bullet("Solution Architect — read in full. Sections 4 (OOTB-Defense), 6 (Accelerator Packs), and 7 (Workshop/Demo) are where you operate most directly.")
doc.bullet("Process Consultant — read in full. Section 4 (OOTB-Defense) is the section you live in; Section 7 (Workshop/Demo) is your facilitation reference.")
doc.bullet("Developer — read Sections 1, 3, 4, and 6 before your first engagement. Sections 2, 7, 8, and 9 the first week on the project.")
doc.bullet("Practice Lead — you own this document. Read everything; update against quarterly retro findings.")

doc.callout(
    "This Handbook does not replace the Internal Governance Operating Guide, the Trust-But-Verify Playbook, or the "
    "Accelerator Pack Blueprint. It points to them. The Handbook is the single onboarding artifact every consultant "
    "reads; the others are the operational references they keep open while delivering."
)

doc.page_break()

# =============================================================================
# Section 1 — The OOTB-First Model
# =============================================================================
doc.h1("The OOTB-First Model")
doc.para(
    "This section explains what the OOTB-first model is, why ECS sells it, and what makes it survive across "
    "engagements. The model is not a configuration philosophy — it is a commercial commitment. ECS promises customers "
    "two specific outcomes that only OOTB-aligned delivery can produce, and the practice's economics depend on us "
    "keeping that promise consistently."
)

doc.h2("Why OOTB-first")
doc.para(
    "OOTB-first means we lead every design conversation with the platform's out-of-the-box capability and only deviate "
    "when a business outcome genuinely requires it. This subsection explains the principle, the historical pattern that "
    "made the principle necessary, and the cost of the alternative (custom-first delivery)."
)

doc.h2("The two value propositions")
doc.para(
    "Every OOTB-first SOW is anchored in two outcomes: (1) accelerated AI realization, because Now Assist, Virtual "
    "Agent, and Predictive Intelligence all depend on clean OOTB data and process foundations, and (2) systematic "
    "elimination of technical debt, because OOTB-aligned configuration is what allows the customer to absorb future "
    "platform upgrades without rework. This subsection details both, with talking points for sponsor conversations."
)

doc.h2("What makes the model survive")
doc.para(
    "Two disciplines keep the model intact across engagements: the OOTB-Defense Discipline (Section 4) and the "
    "Trust-But-Verify Discipline (Section 5). Neither is optional. This subsection summarizes why both must be active "
    "and what happens when either erodes."
)

doc.page_break()

# =============================================================================
# Section 2 — The 18-Week Engagement Spine
# =============================================================================
doc.h1("The 18-Week Engagement Spine")
doc.para(
    "This section is the engagement-shape reference. It describes Sprint 0 setup, the six build sprints, and the "
    "hypercare and handoff phase. Every sprint has named workshops, named deliverables, and named decision rights. "
    "The spine is the same across customers; what varies is the configuration data and the customer's adoption "
    "readiness, not the workshop sequence or the sprint cadence."
)

doc.h2("Sprint 0 — Setup")
doc.para(
    "Sprint 0 establishes governance, mobilizes the team, validates customer readiness, and aligns on the engagement "
    "decision rights. The team produces the customization council charter, the risk register, the communication plan, "
    "and the kickoff materials. This subsection details Sprint 0's named workshops and deliverables."
)

doc.h2("Sprints 1–6 — Build")
doc.para(
    "Each build sprint has a named focus: Sprint 1 platform + incident, Sprint 2 catalog + employee center, Sprint 3 "
    "knowledge + virtual agent, Sprint 4 change + CSDM + CMDB + discovery, Sprint 5 service graph + HAM + integrations, "
    "Sprint 6 performance analytics + reporting and stabilization. The summary table below maps each sprint to its "
    "primary disciplines."
)
doc.table(
    headers=["Sprint", "Focus disciplines", "Primary deliverable"],
    rows=[
        ["Sprint 1", "Platform Foundation, Incident Management",          "Platform configured to OOTB baseline; Incident live to a pilot group"],
        ["Sprint 2", "Catalog & Request, Employee Center",                "Rationalized catalog (≤80 items), Employee Center experience"],
        ["Sprint 3", "Knowledge, Virtual Agent",                          "Curated knowledge base, VA topics for top 5 deflection paths"],
        ["Sprint 4", "Change, CSDM, CMDB, Discovery",                     "Change management live; CSDM-aligned CMDB with Discovery phase 1"],
        ["Sprint 5", "Service Graph, HAM, Integrations",                  "HAM Foundations + Realization live; AD/SSO/SCCM/Intune integrated"],
        ["Sprint 6", "Performance Analytics, Reporting & Stabilization",  "PA dashboards live; full-environment reporting; readiness for hypercare"],
    ],
    col_widths_in=[1.0, 4.0, 4.36],
)

doc.h2("Hypercare and handoff")
doc.para(
    "The two weeks immediately after go-live are hypercare; the practice transitions operational responsibility to "
    "the customer over that window. This subsection details the hypercare expectations document, the operational "
    "handoff pack, and the post-go-live ownership matrix."
)

doc.page_break()

# =============================================================================
# Section 3 — Decision Rights & The Customization Council
# =============================================================================
doc.h1("Decision Rights & The Customization Council")
doc.para(
    "This section is the consultant's reference for who decides what on an OOTB-first engagement. The two-key "
    "decision model and the Customization Council are the mechanisms that keep customization from creeping in "
    "informally. The full operational detail lives in the Internal Governance Operating Guide; this section gives "
    "the consultant the working summary."
)

doc.h2("The two-key principle")
doc.para(
    "Every customization commitment requires two keys: the customer sponsor (business need) and the ECS Practice Lead "
    "(technical path). Either key alone is insufficient. This subsection explains why the model is two-key rather than "
    "single-approver and how to use the principle in workshop conversations."
)

doc.h2("Council composition and authority")
doc.para(
    "The Council convenes for any deviation from OOTB that has completed the deviation lifecycle through Stage 4 "
    "(Recommend). Composition: customer sponsor, ECS Practice Lead, Engagement Manager (facilitates), Solution Architect "
    "(presents OOTB Alternative Analysis), Process Consultant (presents Adoption Impact). This subsection details how "
    "the Council operates and the consultant's role in it."
)

doc.h2("Cross-reference to the Governance Operating Guide")
doc.para(
    "The deviation lifecycle, two-key SLAs, Council pre-read templates, contract risk model, and escalation triggers "
    "live in the ECS Internal Governance Operating Guide (01_Internal/05_Discipline_How-To_Guides/). This subsection "
    "summarizes the cross-references and indicates which Governance Guide sections each consultant role should read in full."
)

doc.page_break()

# =============================================================================
# Section 4 — The OOTB-Defense Discipline
# =============================================================================
doc.h1("The OOTB-Defense Discipline")
doc.para(
    "This section is the heart of the Handbook for Solution Architects and Process Consultants. OOTB-Defense is what "
    "the consultant does in the workshop when the customer says 'but our old system did X' or the SME asks for 'just "
    "a small client script.' The discipline is rehearsable; this section captures the patterns the practice has "
    "validated."
)

doc.h2("What OOTB defense looks like in a workshop")
doc.para(
    "Defense is not refusal — it is a structured re-frame. The consultant acknowledges the request, opens the OOTB "
    "alternative, walks the customer through it, and only routes to the Council if the OOTB path genuinely cannot meet "
    "the business outcome. This subsection details the four-step pattern and the language that works."
)

doc.h2("The Adopt-vs-Re-engineer mindset")
doc.para(
    "Every customer process is either adopted as-is (the OOTB pattern fits, or fits with light configuration), or "
    "re-engineered to fit OOTB (the customer's prior process was idiosyncratic and needs to evolve), or — rarely — "
    "extended with a Council-approved customization. This subsection explains how to classify a process in real time."
)

doc.h2("Adopt-vs-Re-engineer Cheatsheets")
doc.para(
    "Sixteen discipline-specific cheatsheets (INT-AR-01 through INT-AR-16) operationalize this section for catalog "
    "rationalization, category structure, SLAs, assignment rules, approvals, state lifecycle, knowledge curation, VA "
    "topics, PI readiness, CMDB classes, discovery phasing, integration prioritization, custom-vs-OOTB framework, "
    "form customization, notifications, and reporting & dashboards. The consultant uses the cheatsheet for the "
    "discipline being workshopped. Status of each cheatsheet is in the Master Blueprint."
)

doc.page_break()

# =============================================================================
# Section 5 — The Trust-But-Verify Discipline
# =============================================================================
doc.h1("The Trust-But-Verify Discipline")
doc.para(
    "This section is the consultant's view of the management-side discipline. Where OOTB-Defense (Section 4) is what "
    "the consultant does, Trust-But-Verify is what the Engagement Manager and Practice Lead do to catch drift before "
    "it accumulates. The full playbook is INT-TBV-01; this section gives consultants the cross-reference and explains "
    "their role in feeding the discipline."
)

doc.h2("The management-side complement to OOTB-Defense")
doc.para(
    "OOTB-Defense catches drift in the moment; Trust-But-Verify catches drift across moments. The two disciplines are "
    "interlocking: when OOTB-Defense holds, Trust-But-Verify confirms green vectors; when OOTB-Defense erodes, "
    "Trust-But-Verify is what surfaces it for management to intervene."
)

doc.h2("What consultants surface upward")
doc.para(
    "Three things consultants must surface to their EM weekly: customization requests raised in the past week (even "
    "if not yet Council-routed), configuration objects approaching the hygiene thresholds, and any sponsor or SME "
    "signal that suggests drift in the relationship. This subsection lists each with the surfacing template and the "
    "expected EM response."
)

doc.h2("Cross-reference to INT-TBV-01")
doc.para(
    "The Manager's Trust-But-Verify Playbook (01_Internal/09_Trust_but_Verify_Management/) is the operating manual for "
    "the management side. Consultants read Sections 1, 3, and 5 of INT-TBV-01 to understand the signals their work "
    "feeds, and Section 10 to understand the coaching patterns they may be on the receiving end of."
)

doc.page_break()

# =============================================================================
# Section 6 — Working with Accelerator Packs
# =============================================================================
doc.h1("Working with Accelerator Packs")
doc.para(
    "This section is the consultant's reference for the Accelerator Pack library. Packs are the practice's "
    "highest-leverage asset: they compress weeks of customer-side configuration prep into a fillable workbook the SME "
    "can complete between workshops. Using a pack well separates a senior consultant from a smart one."
)

doc.h2("Pack architecture")
doc.para(
    "Every pack follows the same architecture: a customer-fillable section (Instructions, Process Decisions, "
    "Configuration Data, Roles & Responsibilities) and an ECS-internal section (Consultant Guide, Adopt-vs-Re-engineer, "
    "ServiceNow Mapping). This subsection explains the architecture and points to the Accelerator Pack Blueprint "
    "(03_Shared/01_Accelerator_Packs/) for the canonical definition."
)

doc.h2("How to use a pack in a workshop")
doc.para(
    "Packs are not pre-reads — they are workshop instruments. The consultant walks the customer through the relevant "
    "tabs in the workshop, captures decisions in real time, and routes the customer's homework explicitly. This "
    "subsection details the four-phase usage pattern (preview, fill, validate, lock)."
)

doc.h2("When (and when not) to extend a pack")
doc.para(
    "Extending a pack is a Council-level decision when the extension is customer-specific (because it forks the pack "
    "from the library); a Practice Lead decision when the extension is candidate practice-wide content. This "
    "subsection details the decision rules and the propose-to-library workflow."
)

doc.page_break()

# =============================================================================
# Section 7 — Workshop & Demo Discipline
# =============================================================================
doc.h1("Workshop & Demo Discipline")
doc.para(
    "This section is the facilitation reference. Workshops and sprint demos are where the OOTB-first model lives or "
    "dies in front of the customer. The same workshop can lock in OOTB alignment or unlock the customization wishlist, "
    "depending entirely on how the consultant runs it."
)

doc.h2("Facilitation patterns that work")
doc.para(
    "Six patterns the practice has validated: open with the OOTB demo, not the question; capture decisions in writing "
    "before the meeting ends; route every SME wishlist item through the Council frame; defer architectural debates to "
    "the next session; use the cheatsheet on screen; close on the decision, not the conversation."
)

doc.h2("Language anti-patterns to avoid")
doc.para(
    "Four phrases that erode discipline: 'we can just,' 'that's easy to customize,' 'we'll handle that post-go-live,' "
    "and 'let me get back to you on whether that's OOTB.' Each is a discipline gap with a paired correction; this "
    "subsection details all four and the replacement language."
)

doc.h2("The sprint demo")
doc.para(
    "The sprint demo is where the engagement's discipline is visible to the customer and to ECS management. This "
    "subsection details the demo run-of-show, what to demo (always OOTB in primary; customizations marked), and how "
    "to handle the inevitable mid-demo customization request without losing the room."
)

doc.page_break()

# =============================================================================
# Section 8 — UAT, Closeout & Hypercare Handoff
# =============================================================================
doc.h1("UAT, Closeout & Hypercare Handoff")
doc.para(
    "This section is the end-of-engagement reference. UAT is when stated discipline meets customer reality; closeout "
    "is when knowledge transfers from the consultant to the customer admin team; hypercare is when the practice "
    "stays close enough to catch any go-live surprises without becoming a permanent presence."
)

doc.h2("UAT discipline")
doc.para(
    "UAT scenarios are written from the OOTB-aligned process documentation, not the customer's prior process flows. "
    "Defect triage classifies findings into OOTB-misconfiguration, customer-process-mismatch, or genuine bugs. This "
    "subsection details the UAT execution playbook (INT-UAT-02), the defect triage guide (INT-UAT-03), and the "
    "customer-side playbook (CLT-UAT-01)."
)

doc.h2("Closeout and knowledge transfer")
doc.para(
    "Closeout produces the knowledge transfer library index (CLT-CO-02), the customer SOP library (CLT-CO-06), and "
    "the operational handoff pack (CLT-CO-04). This subsection details what good knowledge transfer looks like and "
    "the common closeout failure modes."
)

doc.h2("Hypercare expectations")
doc.para(
    "Hypercare is 14 days of close support, not 14 days of additional build. This subsection details the hypercare "
    "expectations document (CLT-CO-03), the post-go-live ownership matrix (CLT-CO-05), and the continuous improvement "
    "roadmap the practice hands the customer for post-hypercare evolution."
)

doc.page_break()

# =============================================================================
# Section 9 — Escalation Paths & Course-Correction
# =============================================================================
doc.h1("Escalation Paths & Course-Correction")
doc.para(
    "This section is the consultant's reference for when, how, and to whom to escalate. Escalation is not failure — "
    "it is the practice's drift-detection mechanism working as designed. This section also points to the "
    "Course-Correction Playbook the EM and Practice Lead invoke when an engagement crosses an intervention threshold."
)

doc.h2("When to escalate")
doc.para(
    "Five escalation triggers: any customization request the consultant cannot frame through the OOTB alternative; "
    "any configuration object approaching a hygiene red threshold; any SME or sponsor signal of relationship drift; "
    "any sprint that misses its primary deliverable; any signal that the engagement is at risk of failing to deliver "
    "the AI realization outcomes that anchor the SOW. This subsection details each trigger."
)

doc.h2("How to escalate")
doc.para(
    "Escalation routes through the EM first; the EM routes to the Practice Lead if the issue requires Council "
    "involvement or sponsor-to-sponsor conversation. This subsection details the escalation message format (situation, "
    "impact, action, ask), the SLA expectations, and the documentation requirement."
)

doc.h2("The Course-Correction Playbook")
doc.para(
    "The four classes of course-correction — Discipline Reset, Council Realignment, Scope Reset (PCR), Sponsor "
    "Realignment — are detailed in INT-TBV-08. This subsection summarizes the four classes and indicates the "
    "consultant's role in each (typically: contribute evidence, do not run the course-correction)."
)

doc.page_break()

# =============================================================================
# Section 10 — The Library Index
# =============================================================================
doc.h1("The Library Index")
doc.para(
    "This section is a roadmap to the rest of the practice library. The authoritative live catalog is "
    "ECS_OOTB_Collateral_Blueprint.docx, regenerated from blueprint_catalog.json. This section gives the consultant "
    "the high-level structure and points them to the right shelf."
)

doc.h2("Library structure at a glance")
doc.para(
    "Every artifact in the library is tagged Internal, Client, or Shared. Internal artifacts are operational and "
    "never circulated externally. Client artifacts are partnership-toned and ready for customer eyes. Shared "
    "artifacts (accelerator packs, project plans, governance materials) serve both audiences with per-section "
    "audience tagging."
)
doc.table(
    headers=["Catalog", "What's in it", "Folder root", "Authoritative view"],
    rows=[
        ["Internal", "Consultant Handbook · Sales & pre-engagement · Sprint 0 setup · Per-sprint facilitator guides · Discipline how-to guides · Adopt-vs-Re-engineer cheatsheets · Demo scripts · UAT test pack templates · Trust-But-Verify management pack · Lessons learned", "01_Internal/", "Master Blueprint (Internal Collateral Catalog)"],
        ["Client",   "Engagement overview · Sprint 0 customer readiness · Per-sprint customer briefs · Decision topic guides · Workshop pre-reads · UAT execution · Closeout & hypercare", "02_Client/",   "Master Blueprint (Client Collateral Catalog)"],
        ["Shared",   "Accelerator packs · Project plans · Steering & governance · Sprint workbooks",  "03_Shared/",   "Master Blueprint (Shared Collateral Catalog)"],
    ],
    col_widths_in=[1.0, 5.5, 1.3, 1.56],
)
doc.h2("Where to start by engagement phase")
doc.para(
    "During pre-sales: review the AI License Realization Whitepaper and the AI Sales Deck. Sprint 0: the customer "
    "readiness checklist and the engagement kickoff facilitation guide. Build sprints: the relevant per-sprint "
    "facilitator guide and the discipline how-to guide for the active workshop. UAT and closeout: the UAT execution "
    "playbook and the hypercare expectations document."
)

doc.h2("Keeping the library current")
doc.para(
    "Updates to artifact status (Plan → Next → Built) happen in blueprint_catalog.json. Re-running "
    "00_Master_Blueprint/build_master_blueprint.py regenerates the rendered Blueprint document. The handoff prompt "
    "(00_Master_Blueprint/NEXT_SESSION_PROMPT.md) tracks the active build roadmap."
)

doc.page_break()

# =============================================================================
# Section 11 — Onboarding Checklist
# =============================================================================
doc.h1("Onboarding Checklist")
doc.para(
    "This section is the new-consultant onboarding spine. It captures what each consultant must read, do, and "
    "demonstrate before being put in front of a customer. The full checklist with task-level detail is INT-CH-02 "
    "(Consultant Onboarding Checklist); this section gives the consultant the high-level shape."
)

doc.h2("Pre-engagement reading")
doc.para(
    "Before the first engagement: this Handbook in full; the Internal Governance Operating Guide; the "
    "Manager's Trust-But-Verify Playbook (sections 1, 3, 5, 10); the Accelerator Pack Blueprint; and the discipline "
    "how-to guides relevant to the consultant's specialty."
)

doc.h2("First-engagement activities")
doc.para(
    "Within the first two weeks: shadow a sprint demo led by a senior consultant; co-facilitate one workshop using "
    "the relevant Accelerator Pack; submit one OOTB Alternative Analysis through the Council process; debrief with "
    "the EM using the coaching conversation templates (INT-TBV-09)."
)

doc.h2("Cross-reference to INT-CH-02")
doc.para(
    "The full onboarding checklist with task-level detail, owners, and completion criteria lives in INT-CH-02 "
    "(01_Internal/01_Consultant_Handbook/). The Practice Lead validates each new consultant against the checklist "
    "before independent customer engagement."
)

doc.page_break()

# =============================================================================
# Section 12 — Glossary
# =============================================================================
doc.h1("Glossary")
doc.para(
    "This section seeds the practice glossary with the terms most often misused or unclear in early conversations. "
    "The full glossary (INT-CH-04) is the canonical reference; this section captures the foundational terms every "
    "consultant should be fluent with by week one."
)

doc.h2("Foundational terms")
doc.table(
    headers=["Term", "Definition"],
    rows=[
        ["OOTB-first",               "ECS's delivery model: lead with the platform's out-of-the-box capability; deviate only when business outcomes require it and the deviation is Council-approved."],
        ["Two-key decision",         "Any customization requires two approvals: customer sponsor (business need) and ECS Practice Lead (technical path). Neither key is sufficient alone."],
        ["Customization Council",    "The formal decision body that approves or rejects deviations from OOTB. Convenes when a request has completed the deviation lifecycle through Stage 4."],
        ["Deviation lifecycle",      "Six-stage process for any deviation from OOTB: Surface → Triage → Document → Recommend → Decide → Route. Detailed in the Governance Operating Guide."],
        ["OOTB-Defense",             "The consultant-side discipline of holding the OOTB line in workshops. Detailed in Section 4 of this Handbook."],
        ["Trust-But-Verify",         "The management-side discipline of catching drift across cadence events. Detailed in INT-TBV-01."],
        ["Adopt-vs-Re-engineer",     "The decision framework for whether a customer process is adopted as-is, re-engineered to fit OOTB, or — rarely — extended with a Council-approved customization."],
        ["Customization Variance",   "Cumulative count and effort of customizations committed relative to the SOW baseline. The master signal in the Trust-But-Verify dashboard."],
        ["Accelerator Pack",         "A customer-fillable workbook plus ECS-internal consultant guide that compresses configuration prep for a discipline area. See Section 6."],
        ["PCR",                      "Project Change Request — the contract mechanism for scope expansion. PCR is the safety valve when course-correction Class C (Scope Reset) is invoked."],
    ],
    col_widths_in=[2.0, 7.36],
)

doc.h2("Cross-reference to INT-CH-04")
doc.para(
    "The full glossary — including process-specific terms (categories, catalog items, SLAs, assignment rules, "
    "approvals, lifecycle states, etc.), platform-specific terms (CSDM, CMDB, Service Graph, Now Assist, Virtual "
    "Agent, Predictive Intelligence), and engagement-specific terms (sprint cadence, demo discipline, two-key "
    "mechanics, etc.) — lives in INT-CH-04 (OOTB-First Glossary)."
)

# Closing callout
doc.callout(
    "This Handbook is the master onboarding artifact for the practice. Field experience and lessons-learned route "
    "through the quarterly retro into Handbook updates. Send corrections, additions, and field examples to the "
    "Practice Lead. The Handbook only gets sharper if the practice keeps writing it down."
)

doc.save(OUT)
print(f"Saved: {OUT}")
