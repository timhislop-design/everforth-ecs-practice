"""
build_CLT-WP-all.py — Generates all 16 Workshop Pre-Read documents (CLT-WP-02)
Client-facing. Partnership tone. Everforth ECS branding.

Produces one .docx per discipline in the same folder as this script:
    02_Client/05_Workshop_Pre-Reads/

Each pre-read: ~4-6 pages
Structure (per document):
    Cover
    Section 0 — How to Use This Document (unnumbered)
    Section 1 — What Is [Discipline]?
    Section 2 — Why It Matters in Your ServiceNow Journey
    Section 3 — What ServiceNow Delivers Out of the Box
    Section 4 — The Key Decisions You Will Make in Our Workshop
    Section 5 — Things to Think About Before We Meet

Artifact IDs: CLT-WP-02a through CLT-WP-02p (one per discipline)
"""

import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

FOOTER = "ECS Federal · ServiceNow Practice  ·  Confidential"
CONFIDENTIALITY = "Confidential — prepared for the recipient and their organization"
ORG = "ECS Federal · ServiceNow Practice"


def build_pre_read(discipline):
    """Build a single workshop pre-read document from discipline dict."""
    d = discipline
    filename = os.path.join(HERE, d["filename"])

    doc = EcsDocument(meta=DocMeta(
        eyebrow=f"WORKSHOP PRE-READ  ·  {d['short_name'].upper()}",
        title=d["title"],
        subtitle=d["subtitle"],
        audience=d["audience"],
        companion_to=d["companion_to"],
        doc_id=d["doc_id"],
        version="1.0",
        status="Released",
        confidentiality=CONFIDENTIALITY,
        running_header_label=f"Workshop Pre-Read  ·  {d['short_name']}",
        footer_left=FOOTER,
    ))

    doc.add_cover_page()
    doc.add_page_break()

    # -------------------------------------------------------------------------
    # Section 0 — How to Use This Document
    # -------------------------------------------------------------------------
    doc.h1("How to Use This Document", numbered=False)
    doc.para(
        f"This document is your preparation guide for the {d['short_name']} workshop. "
        "It is designed to be read in 15–20 minutes before we meet, so that our time together "
        "is spent on your specifics rather than foundational concepts."
    )
    doc.para(d["how_to_use"])
    doc.callout(
        "You are the decision-maker. Our role is to frame the choices, share what we have seen "
        "in comparable engagements, and partner with you to implement the approach that fits your "
        "organization. Every section below is written with that dynamic in mind."
    )

    # -------------------------------------------------------------------------
    # Section 1 — What Is [Discipline]?
    # -------------------------------------------------------------------------
    doc.h1(f"What Is {d['short_name']}?")
    doc.para(d["what_is"])
    for point in d.get("what_is_bullets", []):
        doc.bullet(point)
    if d.get("what_is_closing"):
        doc.para(d["what_is_closing"])

    # -------------------------------------------------------------------------
    # Section 2 — Why It Matters in Your ServiceNow Journey
    # -------------------------------------------------------------------------
    doc.h1("Why It Matters in Your ServiceNow Journey")
    doc.para(d["why_matters"])
    if d.get("why_matters_bullets"):
        for point in d["why_matters_bullets"]:
            doc.bullet(point)
    if d.get("why_matters_closing"):
        doc.para(d["why_matters_closing"])

    # -------------------------------------------------------------------------
    # Section 3 — What ServiceNow Delivers Out of the Box
    # -------------------------------------------------------------------------
    doc.h1("What ServiceNow Delivers Out of the Box")
    doc.para(d["ootb_intro"])
    doc.table(
        headers=["Capability", "What It Does for Your Team"],
        rows=d["ootb_capabilities"],
        col_widths_in=[2.8, 5.76],
    )
    if d.get("ootb_closing"):
        doc.para(d["ootb_closing"])

    doc.add_page_break()

    # -------------------------------------------------------------------------
    # Section 4 — The Key Decisions You Will Make in Our Workshop
    # -------------------------------------------------------------------------
    doc.h1("The Key Decisions You Will Make in Our Workshop")
    doc.para(d["decisions_intro"])
    for i, decision in enumerate(d["decisions"], 1):
        doc.h2(f"Decision {i}: {decision['label']}")
        doc.para(decision["body"])
        if decision.get("tradeoff"):
            doc.para(f"Trade-off to consider: {decision['tradeoff']}", italic=True)

    # -------------------------------------------------------------------------
    # Section 5 — Things to Think About Before We Meet
    # -------------------------------------------------------------------------
    doc.h1("Things to Think About Before We Meet")
    doc.para(d["reflection_intro"])
    for q in d["reflection_questions"]:
        doc.bullet(q)
    doc.para(
        "You do not need answers to all of these before the workshop. They are prompts for "
        "reflection, not prerequisites. Bring what you have. The workshop is where we work "
        "through the rest together."
    )

    if d.get("what_to_bring"):
        doc.h2("What to Bring to the Workshop")
        for item in d["what_to_bring"]:
            doc.bullet(item)

    doc.callout(
        f"Your ECS team will follow up with a short agenda before the {d['short_name']} workshop. "
        "If you have questions after reading this document, reach out to your ECS engagement manager — "
        "we are happy to walk through any section in advance."
    )

    doc.save(filename)
    print(f"  ✓  {d['doc_id']}  →  {os.path.basename(filename)}")
    return filename


# =============================================================================
# DISCIPLINE DEFINITIONS — All 16 Workshop Pre-Reads
# =============================================================================

DISCIPLINES = [

    # =========================================================================
    # 1. Platform Foundation
    # =========================================================================
    {
        "doc_id": "CLT-WP-02a",
        "short_name": "Platform Foundation",
        "filename": "WP_01_Platform_Foundation_CLIENT.docx",
        "title": "Platform Foundation\nWorkshop Pre-Read",
        "subtitle": "Understanding the baseline that makes everything else possible",
        "audience": "IT Leadership, Platform Owners, Security & Compliance Teams, Project Sponsors",
        "companion_to": "Sprint 0 Customer Readiness Checklist · 18-Week Engagement Overview",
        "how_to_use": (
            "The Platform Foundation workshop is one of the first sessions in your engagement. "
            "The decisions made here — about instance strategy, user provisioning, access controls, "
            "and integration foundations — shape everything that comes after. Reading this gives you "
            "the context to participate fully and make those early decisions with confidence."
        ),
        "what_is": (
            "Platform Foundation refers to the core configuration layer of your ServiceNow instance: "
            "the instance strategy, data architecture, identity and access management, integration "
            "framework, and the baseline platform health that every downstream process area depends on. "
            "It is the invisible scaffolding that determines whether your ServiceNow investment compounds "
            "or fragments over time."
        ),
        "what_is_bullets": [
            "Instance strategy — single instance vs. multi-instance, domain separation decisions",
            "User provisioning — how users are created, managed, and deactivated (typically Active Directory or Entra ID)",
            "Role and access management — who can see and do what in the platform",
            "Integration framework — how ServiceNow connects to your other enterprise systems",
            "Platform health baseline — performance, update schedule, and upgrade readiness",
        ],
        "what_is_closing": (
            "Getting foundation decisions right at the start is significantly less costly than revisiting "
            "them mid-engagement. This workshop exists precisely to surface those decisions early."
        ),
        "why_matters": (
            "Every process area in your implementation — Incident, Change, Catalog, CMDB, Virtual Agent, "
            "AI — sits on top of the platform foundation. A well-structured foundation means cleaner "
            "data, faster onboarding of new capabilities, and a direct path to AI realization. "
            "A fragmented foundation means rework that compounds with every capability you add."
        ),
        "why_matters_bullets": [
            "Identity integration (AD/Entra) done correctly means no manual user management throughout the engagement",
            "Role design done once, correctly, prevents access-control debt that typically surfaces during UAT",
            "Integration framework decisions determine whether your 16-week build is additive or constantly interrupted by connectivity issues",
        ],
        "ootb_intro": (
            "ServiceNow's out-of-the-box platform capabilities are more comprehensive than most teams "
            "realize before their first implementation. Below are the key capabilities your team will "
            "work with during the Foundation workshop."
        ),
        "ootb_capabilities": [
            ["Identity Provider Integration (AD/Entra/SAML)", "Automated user provisioning, group sync, and single sign-on — eliminates manual user management"],
            ["Role-Based Access Control (RBAC)", "Granular, auditable access by role, group, and condition — OOTB roles cover most operational needs"],
            ["Import Sets & Transform Maps", "Structured data ingestion from external systems with field mapping, transformation, and error handling"],
            ["REST/SOAP Integration Framework", "Bi-directional API connectivity with external systems, with built-in retry, logging, and error management"],
            ["Update Sets & Source Control", "Configuration packaging for promotion across dev/test/prod instances"],
            ["Scheduled Jobs & System Properties", "Platform-level automation for maintenance, cleanup, and operational hygiene"],
            ["Instance Upgrade Management", "Structured approach to staying current with ServiceNow releases"],
        ],
        "ootb_closing": (
            "The workshop will walk through which of these capabilities apply to your environment "
            "and what inputs are needed from your team to configure them correctly from the start."
        ),
        "decisions_intro": (
            "These are the decisions that will shape your platform foundation. We will work through "
            "each one in the workshop. Knowing they are coming lets you bring the right stakeholders "
            "and information."
        ),
        "decisions": [
            {
                "label": "Instance Strategy",
                "body": "Will you use a single ServiceNow instance for all business units, or a multi-instance model? For most mid-to-large federal organizations, a single instance with domain awareness is the right answer — but the tradeoffs deserve a deliberate conversation.",
                "tradeoff": "Single instance simplifies governance and reduces cost; multi-instance provides stronger isolation but multiplies administrative overhead.",
            },
            {
                "label": "Identity Integration Approach",
                "body": "How will users be provisioned — via Active Directory sync, Entra ID (Azure AD), SAML federation, or a combination? The answer determines your user data quality from day one. We will review your current directory structure and recommend an integration pattern.",
                "tradeoff": "Directory sync is the most automated and accurate; manual provisioning is fastest to stand up but creates ongoing maintenance debt.",
            },
            {
                "label": "Role Design Scope",
                "body": "Will you use ServiceNow's baseline OOTB role set, supplement with custom roles for specific business units, or build a fully custom role hierarchy? OOTB roles cover the overwhelming majority of operational needs and are maintained through upgrades.",
                "tradeoff": "Custom roles offer precise fit but require maintenance with every upgrade; OOTB roles are upgrade-safe and sufficient for most requirements.",
            },
            {
                "label": "Environment Promotion Strategy",
                "body": "How many instances will you use (dev/test/prod), and what is the process for promoting changes between them? We will recommend a promotion workflow that keeps environments synchronized without slowing delivery.",
                "tradeoff": "More environments provide more testing gates but increase management overhead; fewer environments move faster but carry higher production risk.",
            },
        ],
        "reflection_intro": (
            "These questions will help you come to the workshop prepared. Share them with the colleagues "
            "who own these areas — you may not have all the answers yourself, and that is expected."
        ),
        "reflection_questions": [
            "Who owns your Active Directory or Entra ID environment, and are they available to engage during the foundation sprint?",
            "Do you currently have a dev/test/prod instance structure, or are you starting fresh?",
            "Are there business units or organizational boundaries that need to be preserved in the platform (e.g., separate data visibility for different departments)?",
            "What enterprise systems will ServiceNow need to connect to in the first phase of implementation?",
            "Who has authority to approve changes to your identity provider configuration?",
        ],
        "what_to_bring": [
            "Current Active Directory / Entra ID structure (org chart or group listing)",
            "List of enterprise systems that should connect to ServiceNow (with technical contacts)",
            "Existing instance details if you have a current ServiceNow environment",
            "IT security policies related to SSO, MFA, and API access",
        ],
    },

    # =========================================================================
    # 2. Incident Management
    # =========================================================================
    {
        "doc_id": "CLT-WP-02b",
        "short_name": "Incident Management",
        "filename": "WP_02_Incident_Management_CLIENT.docx",
        "title": "Incident Management\nWorkshop Pre-Read",
        "subtitle": "Restoring service faster with a clean, AI-ready incident process",
        "audience": "Service Desk Leadership, Incident Managers, IT Operations, Process Owners",
        "companion_to": "Incident Management Accelerator Pack · Category Structure Simplification Decision Guide",
        "how_to_use": (
            "Incident Management is typically one of the first process areas configured in your "
            "engagement. The decisions made here set the baseline for service restoration speed, "
            "SLA performance, and the data quality that AI capabilities like Predictive Intelligence "
            "and Now Assist require. This document gives you the context to make those decisions "
            "deliberately."
        ),
        "what_is": (
            "Incident Management is the process of restoring normal service operation as quickly "
            "as possible after an unplanned disruption, while minimizing the adverse impact on business "
            "operations. In ServiceNow, it is the process most users interact with daily — whether "
            "they are submitting a ticket, resolving one, or reporting on the ones in between."
        ),
        "what_is_bullets": [
            "Incident logging — how disruptions are captured (portal, email, phone, Virtual Agent)",
            "Categorization and routing — getting the right ticket to the right team, automatically",
            "Priority and SLA — ensuring the right sense of urgency for the right impact",
            "Resolution and closure — closing tickets correctly so data is accurate and reusable",
            "Major Incident subprocess — escalation path when a single incident affects multiple users or critical services",
        ],
        "why_matters": (
            "Incident Management is the highest-volume process in most IT organizations. It is also "
            "the process most sensitive to data quality — every field that gets filled in inconsistently "
            "represents a data gap that AI-powered capabilities like Predictive Intelligence cannot "
            "close. Getting Incident Management right is the foundational investment in your AI roadmap."
        ),
        "why_matters_bullets": [
            "Categorization discipline directly determines the quality of Predictive Intelligence routing — garbage in, garbage out",
            "SLA configuration determines whether your team's performance is measured accurately or obscured by inherited technical debt",
            "A simplified, OOTB-aligned incident form dramatically reduces the training burden for new agents",
        ],
        "ootb_intro": (
            "ServiceNow's OOTB Incident Management is mature and comprehensive. The following "
            "capabilities are available from day one — no customization required."
        ),
        "ootb_capabilities": [
            ["Multi-channel intake", "Email, portal (Employee Center), phone, Virtual Agent — all route to the same incident queue with consistent data capture"],
            ["Automated categorization routing", "Assignment rules route incidents to the right group based on category, CI, location, and other criteria"],
            ["SLA Engine", "Configurable SLA definitions with breach warnings, escalation, and reporting built in"],
            ["Major Incident Management", "Dedicated workflow for Sev-1/P1 situations: war-room bridge, stakeholder notification, and timeline tracking"],
            ["Predictive Intelligence (ready-state)", "ML-based category and assignment group prediction — activates once sufficient clean ticket data exists"],
            ["Now Assist for Incident", "AI-generated incident summaries and resolution notes — reduces handle time significantly"],
            ["Performance Analytics dashboards", "OOTB incident metrics: MTTR, volume by category, SLA compliance, reopen rate"],
        ],
        "decisions_intro": (
            "These decisions will be worked through in the Incident Management workshop. Some of them "
            "require input from people outside the room — knowing in advance gives you time to gather "
            "that input."
        ),
        "decisions": [
            {
                "label": "Categorization Structure",
                "body": "How will you organize your incident categories, subcategories, and service classifications? A clean, two-level taxonomy (Category → Subcategory) that maps to your actual service delivery teams is the OOTB-aligned baseline. Many organizations arrive with 5-10 levels inherited from previous tools.",
                "tradeoff": "Simplified taxonomy reduces routing errors and enables AI; complex taxonomy preserves historical granularity but creates maintenance burden and degrades ML performance.",
            },
            {
                "label": "Priority and Urgency Matrix",
                "body": "ServiceNow uses a standard Impact × Urgency = Priority matrix. The question is whether you will adopt the OOTB 3×3 matrix, adjust thresholds to match your SLA commitments, or map in a custom priority scheme from your existing process documentation.",
                "tradeoff": "OOTB matrix is upgrade-safe and immediately available; custom schemes require ongoing maintenance and often replicate legacy complexity.",
            },
            {
                "label": "SLA Definition Set",
                "body": "Which SLA targets will you formalize in ServiceNow? We recommend starting with the SLAs your team is already measured against, and configuring them exactly — no extras, no aspirational additions. This is the single most common source of SLA report credibility issues.",
                "tradeoff": "Fewer, accurate SLAs produce trustworthy metrics; too many SLAs dilute accountability and make reporting difficult to interpret.",
            },
            {
                "label": "Closure Criteria",
                "body": "What defines a closed incident? The OOTB approach uses a Resolution Code + Resolution Notes combination to ensure closure data is complete. The workshop will align on the minimum required fields for meaningful data.",
                "tradeoff": "Requiring resolution notes improves data quality for AI and reporting; removing the requirement speeds closure but degrades downstream knowledge and analytics.",
            },
        ],
        "reflection_intro": (
            "These are the questions worth thinking about — and discussing with your team — before "
            "the Incident Management workshop."
        ),
        "reflection_questions": [
            "How many active incident categories do you currently have in your existing tool? (A count or export is helpful.)",
            "What are your current SLA targets — by priority level — and where are they documented?",
            "Which teams handle incidents today, and are those teams' structures reflected in ServiceNow assignment groups?",
            "Where do your users currently submit incidents — email, phone, a portal, all of the above?",
            "What percentage of incidents are resolved by the service desk vs. escalated to Tier 2/3?",
        ],
        "what_to_bring": [
            "Current incident category/subcategory list (export from existing tool if possible)",
            "SLA targets by priority (documented or from existing tool configuration)",
            "Assignment group list with owning team leads",
            "Approximate monthly incident volume by team or category",
        ],
    },

    # =========================================================================
    # 3. Major Incident Management
    # =========================================================================
    {
        "doc_id": "CLT-WP-02c",
        "short_name": "Major Incident Management",
        "filename": "WP_03_Major_Incident_Management_CLIENT.docx",
        "title": "Major Incident Management\nWorkshop Pre-Read",
        "subtitle": "Coordinating your response when incidents affect multiple users or critical services",
        "audience": "Incident Managers, IT Leadership, Service Desk Leadership, Business Continuity Teams",
        "companion_to": "Incident Management Pre-Read · SLA Discipline Decision Guide",
        "how_to_use": (
            "Major Incident Management is the escalation layer that activates when a single incident "
            "or outage affects enough users or critical systems to require coordinated response beyond "
            "the standard queue. This pre-read prepares you to define what 'major' means for your "
            "organization and how you want ServiceNow to support — and accelerate — your response."
        ),
        "what_is": (
            "Major Incident Management (MIM) is a structured subprocess within Incident Management "
            "that activates when an incident meets defined severity criteria: typically high impact on "
            "critical systems, multiple users affected, or executive-level visibility required. "
            "The goal is coordinated, time-boxed restoration with clear accountability."
        ),
        "what_is_bullets": [
            "Major Incident declaration — who can declare, what triggers it, what changes operationally",
            "War room and bridge management — coordinating multiple resolver teams in real time",
            "Stakeholder communications — automated updates to executives, users, and impacted parties",
            "Timeline and action tracking — capturing what happened, when, and who did what",
            "Post-Major Incident Review — connecting MIM records to the Problem Management process",
        ],
        "why_matters": (
            "Major Incidents are the highest-visibility events your IT organization manages. "
            "The way you handle them — how quickly you communicate, how clearly you coordinate, "
            "how completely you document — directly shapes executive and user confidence in IT. "
            "A well-configured MIM process in ServiceNow removes the chaos from the response "
            "and creates the audit trail that post-incident reviews depend on."
        ),
        "why_matters_bullets": [
            "Automated stakeholder notifications mean one less thing to manage during a crisis",
            "Timeline tracking in ServiceNow creates an accurate record without relying on memory after the fact",
            "Direct linkage to Problem Management ensures major incidents produce prevention, not just restoration",
        ],
        "ootb_intro": (
            "ServiceNow's OOTB Major Incident Management capabilities are purpose-built for high-pressure "
            "situations. The following capabilities activate when a Major Incident is declared."
        ),
        "ootb_capabilities": [
            ["Major Incident declaration workflow", "Single-click promotion from Incident to Major Incident, with automatic field population and notification triggers"],
            ["Candidate identification (alert-based)", "Automated flagging of potential Major Incidents based on volume, CI impact, or external alert sources"],
            ["Stakeholder notification engine", "Configurable notification templates for executives, resolver teams, and affected users — by severity and phase"],
            ["War room (Conference Bridge) integration", "Built-in bridge tracking with attendee log, action items, and resolution timeline"],
            ["Timeline widget", "Real-time visual timeline of all MIM activities, accessible to all stakeholders"],
            ["Post-Major Incident Review (PMIR)", "Structured review workflow that auto-links to Problem Management for root cause analysis"],
            ["MIM dashboard and reporting", "OOTB metrics: declaration-to-restoration time, frequency by service, SLA performance under MIM"],
        ],
        "decisions_intro": (
            "These are the decisions we will work through in the Major Incident Management workshop. "
            "Some of them require cross-team alignment — particularly the declaration criteria and "
            "stakeholder communication lists."
        ),
        "decisions": [
            {
                "label": "Major Incident Declaration Criteria",
                "body": "What defines a Major Incident in your organization? The OOTB framework provides a configurable criteria set: combinations of impact level, affected CI criticality, user population affected, and/or manual declaration by an authorized role. The workshop will align on your specific thresholds.",
                "tradeoff": "Tight criteria prevent false declarations that desensitize the organization; loose criteria ensure nothing falls through the cracks. Most organizations calibrate after their first real MIM cycle.",
            },
            {
                "label": "Communication Cadence and Templates",
                "body": "How frequently will you send stakeholder updates during an active Major Incident — every 30 minutes, every hour, at phase transitions? ServiceNow can automate these based on your preference. The workshop will build your initial template set.",
                "tradeoff": "More frequent updates maintain confidence but require template quality; less frequent updates reduce noise but create information gaps that executives fill with speculation.",
            },
            {
                "label": "Post-Incident Review Process",
                "body": "Every Major Incident should produce a Problem record for root cause investigation. We will configure the automatic linkage between MIM closure and Problem creation, and define what constitutes a complete PMIR.",
                "tradeoff": "Automatic linkage ensures nothing is missed; manual linkage allows judgment calls but introduces the risk of 'closed without review' outcomes.",
            },
        ],
        "reflection_intro": (
            "Bringing answers to these questions — even partial ones — will help us move faster in the workshop."
        ),
        "reflection_questions": [
            "How does your organization currently define a Major Incident? Is there a written policy or SLA document?",
            "Who needs to be notified when a Major Incident is declared — and at what level of detail?",
            "Do you have a current on-call or incident command structure for major events?",
            "How are Major Incidents currently tracked and reported to leadership?",
            "What is the current average time from declaration to resolution for your most significant incidents?",
        ],
        "what_to_bring": [
            "Current Major Incident policy or criteria (if documented)",
            "Stakeholder notification distribution list (who gets alerted, at what severity)",
            "Example of a recent Major Incident report or post-mortem",
            "On-call escalation matrix or incident command structure",
        ],
    },

    # =========================================================================
    # 4. Problem Management
    # =========================================================================
    {
        "doc_id": "CLT-WP-02d",
        "short_name": "Problem Management",
        "filename": "WP_04_Problem_Management_CLIENT.docx",
        "title": "Problem Management\nWorkshop Pre-Read",
        "subtitle": "Eliminating recurring incidents by addressing root causes systematically",
        "audience": "Problem Managers, IT Operations Leadership, Incident Managers, Change Managers",
        "companion_to": "Incident Management Pre-Read · Change Management Pre-Read",
        "how_to_use": (
            "Problem Management sits between Incident and Change: it takes the patterns that Incident "
            "Management surfaces and turns them into structured root cause investigations that ultimately "
            "drive Changes to prevent recurrence. This pre-read prepares you to define how that flow "
            "works in your ServiceNow implementation."
        ),
        "what_is": (
            "Problem Management is the process of identifying and eliminating the root causes of recurring "
            "incidents. Where Incident Management focuses on restoring service quickly, Problem Management "
            "focuses on preventing the same disruptions from happening again. The two processes are deeply "
            "linked — and a ServiceNow implementation that connects them cleanly compounds value over time."
        ),
        "what_is_bullets": [
            "Problem identification — how incidents graduate to Problems (volume-based, post-MIM, or manual)",
            "Root cause analysis — structured investigation workflow with assignment, timeline, and workaround management",
            "Known Error Database (KEDB) — documented workarounds and interim solutions for recurring issues",
            "Problem resolution — the Change or fix that eliminates the root cause",
            "Problem review and closure — confirming that the fix held and the pattern is gone",
        ],
        "why_matters": (
            "Organizations that skip Problem Management tend to run Incident Management on a treadmill — "
            "resolving the same issues repeatedly without building institutional knowledge about why they "
            "keep occurring. ServiceNow's connected architecture means that Problems, Incidents, and Changes "
            "share data — so fixing one root cause updates the incident record, the KEDB, and the Change "
            "automatically. That connection is what makes the model compound."
        ),
        "ootb_intro": (
            "ServiceNow's OOTB Problem Management includes everything needed for a disciplined, connected "
            "root cause practice."
        ),
        "ootb_capabilities": [
            ["Problem identification from Incidents", "One-click promotion from Incident to Problem, with related incident linkage and automatic problem record population"],
            ["Root Cause Analysis workspace", "Structured investigation workspace with timeline, notes, related records, and workaround management"],
            ["Known Error Database (KEDB)", "Searchable repository of known errors with documented workarounds — visible to agents and, optionally, end users"],
            ["Problem task management", "Sub-tasks for investigation activities with assignment, due dates, and progress tracking"],
            ["Change linkage", "Automatic association between Problem resolution and the Change record that implements the fix"],
            ["Recurrence detection", "Automatic flagging when an incident pattern matches an open Problem record — prevents duplicate investigation"],
            ["Problem analytics", "OOTB metrics: open problems by age, by service, by priority; time-to-resolution; recurrence rate post-closure"],
        ],
        "decisions_intro": (
            "These are the decisions that will define your Problem Management process in ServiceNow. "
            "They are worth thinking through before the workshop — particularly the criteria for what "
            "constitutes a Problem."
        ),
        "decisions": [
            {
                "label": "Problem Identification Criteria",
                "body": "What triggers a Problem record? Options include: manual creation by an analyst, automatic creation when an incident volume threshold is crossed (e.g., 3+ incidents with the same cause in 30 days), or mandatory creation after every Major Incident closure. We will configure the triggers that match your operational model.",
                "tradeoff": "Automatic thresholds ensure nothing is missed but can generate too many problems; manual creation gives analysts judgment but risks under-identification of recurring patterns.",
            },
            {
                "label": "KEDB Visibility",
                "body": "Should Known Errors and their workarounds be visible only to IT agents, or also to end users through the Employee Center? The OOTB framework supports both. Broader visibility reduces repetitive contact volume; narrower visibility prevents users from self-applying complex workarounds incorrectly.",
                "tradeoff": "User-facing KEDB reduces repeat contacts; agent-only KEDB keeps sensitive system details internal.",
            },
            {
                "label": "Problem-to-Change Linkage",
                "body": "Will every Problem resolution require a Change record before closure, or will some problems be resolved through direct fixes (e.g., restoring a configuration)? The workshop will define which categories of resolution require formal Change and which can be closed with direct action.",
            },
        ],
        "reflection_intro": (
            "These questions will help you come to the workshop with a clear picture of your current state."
        ),
        "reflection_questions": [
            "Does your team currently use a formal Problem Management process, or is root cause investigation informal?",
            "Are there recurring incidents that your team is already aware of but has not formally documented as known errors?",
            "Who owns Problem Management — is there a dedicated Problem Manager, or is this responsibility shared across Incident teams?",
            "What is your current process for communicating workarounds to the service desk?",
            "Are there categories of recurring incidents that you would want to prioritize for Problem review first?",
        ],
        "what_to_bring": [
            "List of known recurring incidents or 'repeat offenders' from your current tool",
            "Current root cause analysis documentation format (if one exists)",
            "Existing Known Error or workaround documentation, however informal",
        ],
    },

    # =========================================================================
    # 5. Change Management
    # =========================================================================
    {
        "doc_id": "CLT-WP-02e",
        "short_name": "Change Management",
        "filename": "WP_05_Change_Management_CLIENT.docx",
        "title": "Change Management\nWorkshop Pre-Read",
        "subtitle": "Controlling risk while enabling the pace your business needs",
        "audience": "Change Managers, CAB Members, IT Leadership, Release Teams, Service Owners",
        "companion_to": "Problem Management Pre-Read · CMDB Pre-Read",
        "how_to_use": (
            "Change Management is one of the most opinion-intensive process areas in any ITSM "
            "implementation. Every organization has a view on what a Change is, who approves it, "
            "and how fast it should move. This pre-read helps you understand what ServiceNow "
            "delivers natively and what decisions you will need to make — so the workshop is "
            "spent on your specifics, not on foundational concepts."
        ),
        "what_is": (
            "Change Management is the process of controlling modifications to IT infrastructure, "
            "applications, and services — ensuring that changes are assessed, authorized, and "
            "implemented in a way that minimizes disruption to service quality. In ServiceNow, "
            "it includes the full lifecycle from request through approval, scheduling, implementation, "
            "and post-implementation review."
        ),
        "what_is_bullets": [
            "Change types — Normal, Standard, Emergency: each with its own workflow and approval path",
            "Risk and impact assessment — automated scoring and manual override for high-complexity changes",
            "CAB (Change Advisory Board) workbench — structured review and approval for Normal changes",
            "Change scheduling — calendar view, conflict detection, and blackout window management",
            "Change closure and PIR — post-implementation review confirming the change achieved its goal",
        ],
        "why_matters": (
            "Change Management is the gatekeeper between intent and production. An under-defined Change "
            "process creates the conditions for incidents — unauthorized changes, untested configurations, "
            "and production surprises. An over-defined process creates a different problem: so much friction "
            "that teams route around it, eliminating the visibility the process was designed to provide. "
            "The OOTB ServiceNow model is calibrated for the middle — enough control to protect stability, "
            "enough flexibility to enable pace."
        ),
        "why_matters_bullets": [
            "CMDB-linked Change records give you visibility into which CI is being changed — essential for risk assessment",
            "Standard Change pre-approval accelerates routine changes without bypassing governance",
            "Emergency Change workflow provides a documented fast path that preserves auditability",
        ],
        "ootb_intro": (
            "ServiceNow's OOTB Change Management is designed for organizations that need control without "
            "bureaucracy. These capabilities are available from day one."
        ),
        "ootb_capabilities": [
            ["Three-type change model (Normal/Standard/Emergency)", "Pre-built workflows for each change type with configurable approval gates and SLA targets"],
            ["Risk Assessment engine", "Automated risk score based on CI criticality, change type, and historical change success — reduces subjective CAB debate"],
            ["CAB Workbench", "Digital CAB meeting management: agenda, voting, decision recording — replaces email chains and spreadsheets"],
            ["Change Calendar & conflict detection", "Visual schedule with freeze-window enforcement and automated conflict flagging"],
            ["Standard Change Catalog", "Pre-approved change templates for routine activities — reduces CAB volume for low-risk changes"],
            ["Now Assist for Change", "AI-generated risk assessment and implementation plan suggestions based on historical change data"],
            ["Change analytics", "OOTB dashboards: change success rate, unauthorized change rate, CAB velocity, emergency change frequency"],
        ],
        "decisions_intro": (
            "These are the Change Management decisions that will be worked through in the workshop. "
            "They have implications for your CAB process, your approval hierarchy, and your "
            "relationship with downstream teams."
        ),
        "decisions": [
            {
                "label": "Change Type Definitions",
                "body": "How will you define Normal, Standard, and Emergency changes for your organization? ServiceNow's OOTB definitions are a strong starting point. The workshop will map your existing change categories to this three-type model — a necessary step before configuring approval workflows.",
                "tradeoff": "Aligning to OOTB definitions simplifies workflow and enables AI; custom definitions require ongoing maintenance and may fragment reporting.",
            },
            {
                "label": "Approval Hierarchy",
                "body": "Who approves changes, at what level, and under what conditions? The workshop will design your approval matrix: which roles approve Normal changes, which require CAB, which can be auto-approved as Standard. Keeping the approval chain as simple as possible is the most common area where organizations over-engineer and then route around the process.",
                "tradeoff": "Simple, layered approval is faster and actually followed; complex multi-level approval creates bottlenecks and encourages workarounds.",
            },
            {
                "label": "Standard Change Library Scope",
                "body": "Which changes are routine enough to pre-approve as Standard Changes? Building a Standard Change library is one of the highest-leverage early investments — it reduces CAB volume and accelerates routine work without reducing governance. The workshop will identify your first 10–20 candidates.",
            },
            {
                "label": "CAB Meeting Cadence",
                "body": "How frequently will your CAB meet, and for how long? The OOTB CAB Workbench supports synchronous and asynchronous review. Many organizations move to asynchronous CAB (vote via the platform, no meeting required) for routine Normal Changes, reserving live CAB for high-risk or complex items.",
            },
        ],
        "reflection_intro": (
            "These questions will help your team come to the workshop with a shared starting point."
        ),
        "reflection_questions": [
            "How many changes does your IT organization process per month, and what percentage are routine vs. high-risk?",
            "What is your current CAB structure — who attends, how often do you meet, how are decisions made?",
            "Do you currently have a Standard Change or pre-approved change process, even informally?",
            "What are your most common change failure or rollback scenarios?",
            "Are there blackout windows (freezes) that need to be encoded in the ServiceNow calendar?",
        ],
        "what_to_bring": [
            "Current change type definitions or change policy documentation",
            "CAB membership list and meeting cadence",
            "Existing Standard Change or pre-approved change list (however informal)",
            "Change calendar with existing blackout windows",
        ],
    },

    # =========================================================================
    # 6. Service Catalog & Request Management
    # =========================================================================
    {
        "doc_id": "CLT-WP-02f",
        "short_name": "Service Catalog & Request Management",
        "filename": "WP_06_Service_Catalog_Request_CLIENT.docx",
        "title": "Service Catalog & Request\nManagement Workshop Pre-Read",
        "subtitle": "Simplifying how your users request services and how your teams fulfill them",
        "audience": "Catalog Owners, Service Owners, Service Desk Leadership, Process Managers",
        "companion_to": "Catalog Item Rationalization Decision Guide · Category Structure Simplification Decision Guide",
        "how_to_use": (
            "The Service Catalog and Request Management workshop addresses both what users can request "
            "and how those requests flow to fulfillment. If you have read the Catalog Item Rationalization "
            "and Category Structure Simplification Decision Guides, this pre-read builds on that "
            "foundation — moving from 'what belongs in the catalog' to 'how requests move through the "
            "system once submitted.'"
        ),
        "what_is": (
            "The Service Catalog is the user-facing menu of services and products that IT (and optionally "
            "other business units) makes available for request. Request Management is the fulfillment "
            "process behind it: the workflows, approvals, tasks, and SLAs that turn a submitted request "
            "into a delivered outcome. In ServiceNow, the two are tightly integrated — the catalog item "
            "defines the request, and the workflow behind it defines the fulfillment."
        ),
        "what_is_bullets": [
            "Catalog items — the requestable products and services (software access, hardware, onboarding packages, etc.)",
            "Categories and subcategories — the taxonomy that organizes items for users navigating the catalog",
            "Record Producers — catalog items that create other record types (incidents, change requests, etc.)",
            "Workflows / Flow Designer — the automated fulfillment process behind each request",
            "Approvals — configurable approval gates within the fulfillment workflow",
            "Request SLAs — time targets for fulfillment, by item or item type",
        ],
        "why_matters": (
            "The Service Catalog is typically the most visible IT touchpoint for end users. A well-designed "
            "catalog reduces the support burden on the service desk (users find what they need and submit "
            "complete requests), improves fulfillment speed (workflows route requests automatically), "
            "and produces the clean request data that Virtual Agent and Predictive Intelligence need to "
            "function well."
        ),
        "why_matters_bullets": [
            "Catalog item variable quality directly determines how complete and accurate incoming request data is",
            "Approval logic embedded in workflows eliminates email-chain approvals and their associated audit gaps",
            "Request data feeds Virtual Agent topic coverage and Predictive Intelligence routing — making catalog quality an AI prerequisite",
        ],
        "ootb_intro": (
            "ServiceNow's OOTB Service Catalog and Request Management are fully featured from day one. "
            "These capabilities form the foundation your workshop will configure."
        ),
        "ootb_capabilities": [
            ["Catalog Item Builder (no-code)", "Drag-and-drop catalog item creation with configurable variable sets, conditional logic, and fulfillment workflow attachment"],
            ["Flow Designer", "Visual, no-code workflow builder for fulfillment automation — approvals, tasks, notifications, and integrations"],
            ["Category and subcategory taxonomy", "Hierarchical organization of catalog items with icons, descriptions, and access controls"],
            ["Request Portal (Employee Center)", "OOTB self-service portal with search, category browse, order status tracking, and guided request flows"],
            ["Approval engine", "Configurable approval chains — sequential, parallel, group-based — embedded in fulfillment workflows"],
            ["Request SLA engine", "Time-based SLA definitions per catalog item with breach warnings and reporting"],
            ["Now Assist for Catalog", "AI-assisted variable population and request routing based on user context and historical patterns"],
        ],
        "decisions_intro": (
            "These are the decisions that will be worked through in the Catalog and Request Management "
            "workshop. They build directly on the catalog rationalization and category structure "
            "discussions."
        ),
        "decisions": [
            {
                "label": "Catalog Item Scope for Initial Go-Live",
                "body": "Which catalog items will be in scope for Sprint 2? This is distinct from the rationalization question (which items should exist) — this is the sequencing question (which will be configured in this sprint vs. a later phase). We will recommend a prioritization approach based on request volume and fulfillment complexity.",
                "tradeoff": "Fewer items in sprint one means higher quality and faster delivery; more items extend the sprint but provide a broader user surface at go-live.",
            },
            {
                "label": "Approval Design",
                "body": "How complex should your approval chains be? The OOTB recommendation is: start with the minimum approval required for compliance and progressively add only when a clear business requirement exists. Over-approval is the most common catalog design failure pattern.",
                "tradeoff": "Leaner approval chains mean faster fulfillment and less abandonment; complex chains provide more control but slow every request and increase workaround behavior.",
            },
            {
                "label": "Variable Set Standardization",
                "body": "Will you build reusable variable sets for common data collection (user data, manager, cost center, etc.), or configure each catalog item independently? Standardized variable sets are the OOTB-aligned approach — they reduce configuration time for new items and ensure consistent data capture.",
            },
            {
                "label": "Fulfillment Workflow Ownership",
                "body": "Who owns the fulfillment workflows behind each catalog item — the Catalog team, the fulfillment teams, or a shared admin? Clarifying ownership now prevents the common pattern where workflows are abandoned or misconfigured because no one feels accountable for them.",
            },
        ],
        "reflection_intro": (
            "These questions will prepare your team — particularly Catalog Owners and Service Owners — "
            "for the workshop conversation."
        ),
        "reflection_questions": [
            "How many catalog items does your current system have, and how many are actively used?",
            "What are the top 10–20 most frequently requested services from your users?",
            "Who currently maintains your catalog items — is there a dedicated catalog administrator?",
            "What approval patterns do you have today, and which are required by policy vs. by habit?",
            "Are there fulfillment tasks that should be automated but are currently manual?",
        ],
        "what_to_bring": [
            "Current catalog item list (export or screenshot from existing tool)",
            "Top 20 request types by volume (from ticket data if available)",
            "Approval matrix — who approves what, under what conditions",
            "Fulfillment team contacts for each major service area",
        ],
    },

    # =========================================================================
    # 7. Knowledge Management
    # =========================================================================
    {
        "doc_id": "CLT-WP-02g",
        "short_name": "Knowledge Management",
        "filename": "WP_07_Knowledge_Management_CLIENT.docx",
        "title": "Knowledge Management\nWorkshop Pre-Read",
        "subtitle": "Turning your team's expertise into a searchable, AI-ready knowledge base",
        "audience": "Knowledge Managers, Service Desk Leadership, Process Owners, Content Owners",
        "companion_to": "Virtual Agent Pre-Read · Now Assist/GenAI Pre-Read",
        "how_to_use": (
            "Knowledge Management is the foundation for your AI strategy on ServiceNow. "
            "Virtual Agent uses knowledge articles to answer user questions. Now Assist uses "
            "knowledge articles to generate suggested resolutions. The quality and structure of "
            "your knowledge base directly determines the quality of your AI outputs. "
            "This pre-read prepares you to make the decisions that set that foundation well."
        ),
        "what_is": (
            "Knowledge Management in ServiceNow is the process of capturing, structuring, maintaining, "
            "and distributing institutional knowledge — primarily as knowledge articles that can be "
            "accessed by agents, end users, and AI capabilities. It includes the knowledge base "
            "structure, the article authoring and review workflow, the lifecycle management process, "
            "and the integration with ServiceNow's search and AI layers."
        ),
        "what_is_bullets": [
            "Knowledge bases — top-level containers (e.g., IT Knowledge Base, HR Knowledge Base)",
            "Knowledge categories — the taxonomy that organizes articles within a knowledge base",
            "Article types — How-To, FAQ, Reference — each with its own template and use pattern",
            "Article lifecycle — Draft → Review → Published → Retired, with configurable review ownership",
            "Search and findability — full-text search, AI-enhanced search, and Virtual Agent integration",
        ],
        "why_matters": (
            "Most organizations have institutional knowledge distributed across email threads, "
            "SharePoint pages, shared drives, and individual experts' heads. ServiceNow Knowledge "
            "Management does not eliminate that — it gives you a structured home for the knowledge "
            "that matters for service delivery, and connects it directly to the AI capabilities "
            "that amplify its value. An article published in ServiceNow is automatically available "
            "to Virtual Agent topics, Now Assist suggestions, and agent search — without additional configuration."
        ),
        "why_matters_bullets": [
            "Each knowledge article is an AI training asset — the more quality articles, the better Virtual Agent and Now Assist perform",
            "Agents with searchable knowledge resolve incidents faster and with higher first-contact resolution rates",
            "End users with self-service knowledge reduce contact volume — the clearest path to deflection metrics",
        ],
        "ootb_intro": (
            "ServiceNow's OOTB Knowledge Management is ready to use immediately. The following "
            "capabilities form the foundation your workshop will configure."
        ),
        "ootb_capabilities": [
            ["Multi-knowledge-base support", "Separate knowledge bases for different audiences (IT, HR, Facilities) with independent access controls and ownership"],
            ["Article templates by type", "OOTB templates for How-To, FAQ, Known Error, and Reference articles — enforces structure and quality"],
            ["Lifecycle workflow (Draft → Review → Published)", "Configurable review and approval workflow for article publishing — prevents low-quality content from reaching users"],
            ["Full-text search with AI ranking", "Keyword and semantic search with ML-based relevance ranking — improves article findability without tagging effort"],
            ["Virtual Agent integration", "Knowledge articles are automatically searched by Virtual Agent topics — no separate integration required"],
            ["Now Assist for Knowledge", "AI-generated article drafts from incident resolution notes — accelerates article creation for high-volume issues"],
            ["Article feedback and effectiveness metrics", "User ratings, view counts, and search-to-click metrics to identify articles needing improvement"],
        ],
        "decisions_intro": (
            "These are the decisions that will define your Knowledge Management process. "
            "They have implications for your content team, your Virtual Agent design, and "
            "your AI roadmap."
        ),
        "decisions": [
            {
                "label": "Knowledge Base Structure",
                "body": "How many knowledge bases will you start with, and who owns each one? The OOTB recommendation is to start with one primary IT knowledge base and expand only when you have clear audience separation needs (e.g., a separate HR knowledge base with different access controls).",
                "tradeoff": "Fewer knowledge bases are simpler to maintain and search across; more knowledge bases allow finer audience control but increase content fragmentation.",
            },
            {
                "label": "Article Quality Standards",
                "body": "What are the minimum requirements for a publishable article — template compliance, review sign-off, minimum word count? Establishing standards before go-live prevents the common pattern where a knowledge base grows large but low-quality, becoming a search problem rather than a search solution.",
            },
            {
                "label": "Retirement and Review Schedule",
                "body": "How often will articles be reviewed for accuracy, and what triggers automatic retirement? ServiceNow supports scheduled review reminders and automatic expiration. Without this, knowledge bases accumulate stale content that degrades search quality and user trust.",
                "tradeoff": "Scheduled review cycles maintain quality but require content owner commitment; no review schedule means faster growth but gradual degradation.",
            },
            {
                "label": "Initial Article Migration",
                "body": "Will you migrate existing knowledge content from your current tools, start fresh, or do a selective import of only high-quality content? The recommendation is selective migration — bring only articles that are current, accurate, and structured — rather than bulk import that transfers existing quality problems.",
            },
        ],
        "reflection_intro": (
            "These questions will help you come prepared to make knowledge structure decisions in the workshop."
        ),
        "reflection_questions": [
            "Where does your team's institutional knowledge currently live — SharePoint, a wiki, email, individual experts?",
            "Do you have existing knowledge articles in your current ITSM tool? Are they current and accurate?",
            "Who would own the knowledge authoring and review process? Do they have capacity for this role?",
            "What are the top 10 questions your service desk answers repeatedly?",
            "Are there topics you would want Virtual Agent to handle that would require knowledge articles to support them?",
        ],
        "what_to_bring": [
            "Export or list of existing knowledge articles (with last-updated dates if available)",
            "Top 10–20 'frequently asked questions' from your service desk",
            "Current knowledge ownership structure (who writes, who approves)",
            "Links to any existing SharePoint, wiki, or FAQ pages you consider high-quality",
        ],
    },

    # =========================================================================
    # 8. Employee Center
    # =========================================================================
    {
        "doc_id": "CLT-WP-02h",
        "short_name": "Employee Center",
        "filename": "WP_08_Employee_Center_CLIENT.docx",
        "title": "Employee Center\nWorkshop Pre-Read",
        "subtitle": "Designing the self-service experience your employees will actually use",
        "audience": "IT Leadership, HR Leaders, Communications Teams, Service Desk Leadership, UX Stakeholders",
        "companion_to": "Service Catalog Pre-Read · Knowledge Management Pre-Read · Virtual Agent Pre-Read",
        "how_to_use": (
            "Employee Center is the front door to every ServiceNow capability your employees will "
            "interact with — catalog requests, knowledge articles, incident submission, HR services, "
            "and Virtual Agent. The decisions made in this workshop determine what employees see, "
            "how they find what they need, and whether they adopt self-service or call the desk. "
            "This pre-read helps you approach those decisions with a clear picture of what is possible."
        ),
        "what_is": (
            "Employee Center (EC) is ServiceNow's unified self-service portal — the single, branded "
            "experience that surfaces IT services, HR services, knowledge, announcements, and Virtual "
            "Agent from a single interface. It replaces legacy portals (Service Portal, legacy HR portal) "
            "with a modern, searchable, role-aware experience that can be configured without code."
        ),
        "what_is_bullets": [
            "Unified service catalog — IT, HR, Facilities, and other departments in one portal",
            "Knowledge search — searchable access to knowledge bases across departments",
            "Announcements and news — configurable content for IT updates, policy changes, HR announcements",
            "Virtual Agent entry point — conversational interface embedded directly in the portal",
            "Order status tracking — users can track their own requests without contacting the desk",
            "Role-aware personalization — different content and catalog items for different user populations",
        ],
        "why_matters": (
            "Self-service adoption is the clearest indicator of whether your ServiceNow investment is "
            "reaching employees or staying within IT. Employee Center is the vehicle for that adoption. "
            "A well-designed EC means employees submit requests through the portal, find knowledge "
            "articles before calling, and use Virtual Agent for routine questions. Each of those "
            "behaviors reduces service desk contact volume and improves the data quality that your "
            "AI capabilities depend on."
        ),
        "why_matters_bullets": [
            "Portal submission produces structured data; phone submission produces unstructured data — portal adoption is an AI readiness investment",
            "Announcement and news capability replaces email blasts that get lost — increasing IT visibility with employees",
            "Mobile-ready OOTB design means employees access services from anywhere without additional development",
        ],
        "ootb_capabilities": [
            ["No-code page builder", "Drag-and-drop page and topic page configuration — no developer required for most customizations"],
            ["Unified search", "Single search across catalog items, knowledge articles, and announcements — with AI-enhanced ranking"],
            ["Department-specific pages (Topic Pages)", "Dedicated page for IT, HR, Facilities — configurable content, catalog sections, and branding per department"],
            ["Virtual Agent widget", "Embedded conversational interface — employees can start a request or find an answer without leaving the portal"],
            ["My Requests tracking", "Real-time status view of submitted requests and open incidents — reduces 'where is my ticket?' contacts"],
            ["Announcements and targeted content", "Role-aware news and announcement publishing — employees see what is relevant to them"],
            ["Mobile-optimized experience", "OOTB responsive design for phone and tablet — no separate mobile app required"],
        ],
        "ootb_intro": (
            "Employee Center's OOTB capabilities are production-ready from day one. The workshop "
            "will configure the structure, content, and branding for your organization."
        ),
        "decisions_intro": (
            "These are the key Employee Center decisions. The most important one — what the portal "
            "is called — seems trivial but shapes adoption. Start there."
        ),
        "decisions": [
            {
                "label": "Portal Scope: IT-Only or Multi-Department",
                "body": "Will Employee Center launch as an IT self-service portal only, or will it include HR, Facilities, or other departments at go-live? Starting with IT only is faster; a multi-department launch provides more value but requires coordination across business owners.",
                "tradeoff": "IT-only launch is faster and fully within your control; multi-department launch provides more value but requires cross-organizational coordination.",
            },
            {
                "label": "Branding and Naming",
                "body": "What will employees call the portal? Organizations that name it something other than 'ServiceNow' or 'IT Portal' — something that reflects their brand or their service culture — see higher adoption. The OOTB branding tools allow full logo, color, and naming customization without development.",
            },
            {
                "label": "Navigation Structure",
                "body": "How will the portal be organized — by department, by service type, or by employee journey (e.g., New Hire, IT Issue, I Need Software)? Journey-based organization consistently outperforms department-based organization for employee usability, but requires cross-department coordination.",
                "tradeoff": "Journey-based navigation is more intuitive for employees; department-based navigation is easier to maintain and govern.",
            },
            {
                "label": "Featured Content at Launch",
                "body": "What will the homepage feature — your most popular catalog items, key announcements, or a guided new-hire experience? The initial homepage content determines first-impression adoption. We will prioritize based on your top request types and user population.",
            },
        ],
        "reflection_intro": (
            "These questions will help your communications and IT teams prepare for the Employee Center workshop."
        ),
        "reflection_questions": [
            "Do employees currently have a self-service portal? If so, what is the adoption rate?",
            "What are the top reasons employees contact the service desk instead of self-serving?",
            "Are there other departments (HR, Facilities) who would want to participate in an Employee Center launch?",
            "What branding or naming constraints exist (must align with internal brand guidelines, intranet naming, etc.)?",
            "Is there a communications plan or champion program for driving portal adoption?",
        ],
        "what_to_bring": [
            "Current self-service portal URL or screenshot (if one exists)",
            "Organization branding guidelines (logo, primary colors)",
            "Top 10–15 service requests by volume — these become featured catalog items",
            "HR or Facilities contact if multi-department scope is under consideration",
        ],
    },

    # =========================================================================
    # 9. Virtual Agent
    # =========================================================================
    {
        "doc_id": "CLT-WP-02i",
        "short_name": "Virtual Agent",
        "filename": "WP_09_Virtual_Agent_CLIENT.docx",
        "title": "Virtual Agent\nWorkshop Pre-Read",
        "subtitle": "Deploying conversational AI that deflects contacts and delivers outcomes — not just answers",
        "audience": "IT Leadership, Service Desk Leadership, Knowledge Managers, Process Owners",
        "companion_to": "Knowledge Management Pre-Read · Employee Center Pre-Read · Now Assist Pre-Read",
        "how_to_use": (
            "Virtual Agent is the conversational AI layer that sits inside Employee Center and Microsoft "
            "Teams, letting employees ask questions and complete requests through natural language. "
            "Its effectiveness depends directly on the quality of your knowledge base and the design "
            "of the topics behind it. This pre-read helps you understand what makes Virtual Agent "
            "succeed — and what commonly causes it to underperform."
        ),
        "what_is": (
            "Virtual Agent (VA) is ServiceNow's built-in conversational AI — a chatbot embedded in the "
            "Employee Center portal and optionally in Microsoft Teams. It handles user questions "
            "by searching knowledge articles, executing pre-built conversation flows (topics), "
            "and, where appropriate, routing to a live agent. Unlike external chatbot products, "
            "VA is native to ServiceNow — it can look up ticket status, submit catalog items, "
            "reset passwords, and create incidents without leaving the conversation."
        ),
        "what_is_bullets": [
            "Topics — the conversation flows that handle specific user intents (e.g., 'I need a password reset', 'What is the status of my request?')",
            "Natural Language Understanding (NLU) — the ML model that maps what a user types to the right topic",
            "Knowledge Search integration — automatic article search when no topic matches the user's question",
            "Live Agent handoff — escalation to a human agent when the bot cannot resolve",
            "Teams / Slack integration — VA can operate inside Microsoft Teams or Slack without the portal",
        ],
        "why_matters": (
            "Contact deflection is the most measurable ROI from Virtual Agent — every question answered "
            "by VA without a live agent contact represents cost savings and faster resolution for the user. "
            "But deflection only works if VA actually resolves the question, not just redirects it. "
            "A VA that consistently says 'I didn't understand that — let me connect you to an agent' "
            "generates frustration, not value. The difference between a high-performing VA and a "
            "frustrating one is topic coverage, knowledge quality, and outcome design."
        ),
        "why_matters_bullets": [
            "Password reset via VA is the single highest-ROI starting topic — high volume, fully automatable, zero agent value in the resolution",
            "Ticket status inquiry via VA eliminates 'where is my ticket?' contacts entirely — immediate value from day one",
            "Knowledge article search integration means VA improves automatically as your knowledge base grows",
        ],
        "ootb_intro": (
            "ServiceNow's OOTB Virtual Agent comes with pre-built topics that cover the most common "
            "service desk scenarios. The following capabilities are available from day one."
        ),
        "ootb_capabilities": [
            ["OOTB topic library (50+ topics)", "Pre-built conversation flows for IT topics: password reset, ticket status, software request, access request, and more"],
            ["NLU model training", "OOTB NLU model for IT language — improves with usage and can be trained on your organization's specific terminology"],
            ["Knowledge article search", "Automatic knowledge base search when user question doesn't match a configured topic"],
            ["Live Agent handoff", "Configurable escalation to ServiceNow Agent Workspace for live agent conversations"],
            ["Microsoft Teams integration", "VA operates natively inside Teams — employees ask questions without leaving their collaboration tool"],
            ["Now Assist in VA", "Generative AI enhancement — VA can generate contextual answers from knowledge articles, not just return links"],
            ["VA analytics", "Topic performance dashboard: containment rate, deflection rate, escalation rate, user satisfaction by topic"],
        ],
        "decisions_intro": (
            "These decisions will shape your Virtual Agent deployment. The most important one "
            "is which topics to launch with — quality of a small set outperforms quantity of a large set."
        ),
        "decisions": [
            {
                "label": "Launch Topic Set",
                "body": "Which VA topics will be active at go-live? The recommendation is to start with 5–8 high-volume, fully automatable topics and expand based on usage data. Common starting set: password reset, ticket status, software request, access request, Wi-Fi/VPN help, and onboarding questions.",
                "tradeoff": "Fewer topics with full resolution capability outperforms many topics with partial resolution — quality drives adoption, quantity alone does not.",
            },
            {
                "label": "Integration Scope (Portal vs. Teams)",
                "body": "Will VA launch in Employee Center only, or also in Microsoft Teams at go-live? Teams integration dramatically increases adoption because employees access VA in the tool they already live in — but it requires additional configuration and an approved Teams app.",
            },
            {
                "label": "Live Agent Handoff Design",
                "body": "When VA cannot resolve a question, what happens? Options include: route to email (incident creation), route to live chat (if you have Agent Chat configured), or provide knowledge articles and invite the user to call. The workshop will design the handoff flow that matches your service model.",
            },
            {
                "label": "NLU Training Approach",
                "body": "Will you use the OOTB NLU model as-is, or supplement with organization-specific training phrases? Adding training phrases for your internal terminology (system names, acronyms, department-specific language) measurably improves VA accuracy.",
            },
        ],
        "reflection_intro": (
            "These questions will help shape your launch topic prioritization."
        ),
        "reflection_questions": [
            "What are the top 10 reasons users contact your service desk today?",
            "Which of those contacts are fully resolvable without a human — i.e., the answer or action is always the same?",
            "Do you have an existing chatbot or VA tool? If so, what topics does it handle, and what is its containment rate?",
            "Are your employees primarily working from a browser portal, or from Microsoft Teams?",
            "Who would own VA topic configuration and maintenance post-go-live?",
        ],
        "what_to_bring": [
            "Service desk contact reason categories and volume (top 10–20 by frequency)",
            "Any existing chatbot or VA configuration documentation",
            "Microsoft Teams environment details (tenant, admin contacts) if Teams integration is in scope",
            "Knowledge base readiness assessment (articles available for VA to search)",
        ],
    },

    # =========================================================================
    # 10. Predictive Intelligence
    # =========================================================================
    {
        "doc_id": "CLT-WP-02j",
        "short_name": "Predictive Intelligence",
        "filename": "WP_10_Predictive_Intelligence_CLIENT.docx",
        "title": "Predictive Intelligence\nWorkshop Pre-Read",
        "subtitle": "Using machine learning to route, categorize, and prioritize without manual effort",
        "audience": "IT Leadership, Incident Managers, Service Desk Leadership, Data and Analytics Owners",
        "companion_to": "Incident Management Pre-Read · Now Assist/GenAI Pre-Read",
        "how_to_use": (
            "Predictive Intelligence (PI) is the ML layer that learns from your historical ServiceNow "
            "data and applies that learning to incoming records — suggesting categories, assignment groups, "
            "and priorities automatically. Its effectiveness depends almost entirely on the quality "
            "and consistency of the data it is trained on. This pre-read helps you understand what "
            "PI requires and what decisions you will make in the workshop."
        ),
        "what_is": (
            "Predictive Intelligence is ServiceNow's built-in machine learning capability. It analyzes "
            "patterns in your historical incident, request, and change records and uses those patterns "
            "to make predictions on new records — before a human has to touch them. The most common use "
            "cases are category prediction and assignment group prediction for incoming incidents."
        ),
        "what_is_bullets": [
            "Category prediction — PI suggests the category and subcategory for a new incident based on the description",
            "Assignment group prediction — PI suggests the correct resolver group based on category, CI, and description",
            "Priority prediction — PI suggests urgency/impact based on the requester, CI, and historical patterns",
            "Similarity detection — PI identifies incidents similar to open ones, enabling clustering and deduplication",
            "Continuous learning — PI models improve as more data is generated and corrected by agents",
        ],
        "why_matters": (
            "Every minute a ticket spends with the wrong category or in the wrong queue is latency in "
            "your service delivery. PI eliminates that latency — not by being perfect, but by being "
            "right often enough to accelerate the queue. More importantly, PI requires clean, consistent "
            "historical data to train on. That means Incident Management data quality is not just an "
            "operational concern — it is an AI prerequisite."
        ),
        "why_matters_bullets": [
            "Miscategorized tickets that would previously sit in a queue for hours are rerouted in seconds by PI",
            "Assignment accuracy improvements reduce inter-team handoffs — a major source of MTTR latency",
            "PI trains on your data — improving categorization discipline now compounds into better predictions later",
        ],
        "ootb_intro": (
            "ServiceNow's OOTB Predictive Intelligence framework provides ML infrastructure, training pipelines, "
            "and prediction application — without requiring a data science team."
        ),
        "ootb_capabilities": [
            ["Clustering solutions", "Groups similar incidents together — identifies patterns and candidates for Problem Management or Known Errors"],
            ["Classification solutions", "Predicts field values (category, subcategory, assignment group, priority) for incoming records"],
            ["Training pipeline", "Automated model training against historical data — configurable training schedule and data window"],
            ["Prediction confidence threshold", "Configurable confidence level — predictions below threshold are not applied, reducing false positives"],
            ["Agent feedback loop", "Agents confirm or correct PI predictions — corrections improve the model over time"],
            ["PI analytics", "Model performance dashboard: prediction accuracy by field, confidence distribution, agent correction rate"],
        ],
        "decisions_intro": (
            "These decisions shape how Predictive Intelligence is deployed and governed in your environment."
        ),
        "decisions": [
            {
                "label": "Initial PI Use Cases",
                "body": "Which fields will PI predict at go-live? The recommendation is to start with category and assignment group for Incident — the highest-volume, highest-impact use case. Expand to Request and Change after the Incident model is validated.",
            },
            {
                "label": "Training Data Quality Assessment",
                "body": "Is your historical incident data clean enough to train a PI model? The workshop will assess your data quality — specifically: categorization consistency, assignment group accuracy, and volume (minimum 1,000–2,000 records per category for meaningful training). We will identify gaps and a remediation approach if needed.",
                "tradeoff": "Starting with clean data produces accurate models; starting with inconsistent data produces unreliable predictions that agents learn to ignore.",
            },
            {
                "label": "Confidence Threshold and Override Design",
                "body": "What confidence level is required before PI applies a prediction automatically vs. suggests it for agent review? Higher thresholds mean fewer auto-applications but higher accuracy. The workshop will calibrate based on your volume and tolerance for prediction errors.",
            },
        ],
        "reflection_intro": (
            "These questions will help your team assess PI readiness before the workshop."
        ),
        "reflection_questions": [
            "How consistent is your current incident categorization? Do agents categorize tickets differently for the same type of issue?",
            "How many incidents does your environment process per month? Per year?",
            "What percentage of incidents are miscategorized or reassigned after initial assignment?",
            "Do you have at least 12 months of historical incident data in your current tool?",
            "Who would own the Predictive Intelligence model governance — monitoring performance and triggering retraining?",
        ],
        "what_to_bring": [
            "Incident volume by month (last 12–24 months)",
            "Category and assignment group distribution from current tool",
            "Reassignment rate data if available",
            "Data export or sample from current tool for quality assessment",
        ],
    },

    # =========================================================================
    # 11. Now Assist / GenAI
    # =========================================================================
    {
        "doc_id": "CLT-WP-02k",
        "short_name": "Now Assist / GenAI",
        "filename": "WP_11_Now_Assist_GenAI_CLIENT.docx",
        "title": "Now Assist & Generative AI\nWorkshop Pre-Read",
        "subtitle": "Activating the AI capabilities that make your ServiceNow investment realize its full value",
        "audience": "IT Leadership, Service Desk Leadership, Process Owners, Security & Compliance Teams",
        "companion_to": "Predictive Intelligence Pre-Read · Virtual Agent Pre-Read · Knowledge Management Pre-Read",
        "how_to_use": (
            "Now Assist is ServiceNow's generative AI layer — the suite of AI capabilities powered by "
            "large language models that augment agent productivity, accelerate resolution, and elevate "
            "the self-service experience. This pre-read explains what Now Assist does, what it requires "
            "to work well, and the decisions your organization will make about its deployment."
        ),
        "what_is": (
            "Now Assist is ServiceNow's brand name for its generative AI product suite — built on "
            "large language model (LLM) technology integrated natively into the ServiceNow platform. "
            "Unlike Predictive Intelligence (which predicts field values from patterns in your data), "
            "Now Assist generates natural language outputs — summaries, suggested resolutions, "
            "knowledge article drafts, and conversational responses — based on your ticket data, "
            "knowledge articles, and platform context."
        ),
        "what_is_bullets": [
            "Now Assist for Incident — generates incident summaries, suggested resolutions, and resolution note drafts",
            "Now Assist for Change — generates risk assessments and implementation plan suggestions",
            "Now Assist for Virtual Agent — powers generative answers in VA conversations, reducing reliance on exact article matches",
            "Now Assist for Knowledge — generates article drafts from resolution notes",
            "Now Assist for Case Management — case summaries and suggested next actions for HR and Customer Service",
        ],
        "why_matters": (
            "Your organization made a significant investment in ServiceNow AI licensing. Now Assist "
            "is where that investment becomes visible — in agent time saved, in faster resolution, "
            "in self-service interactions that feel like conversations rather than search. But Now Assist "
            "performs in proportion to the quality of the data and knowledge it has access to. "
            "This is why the OOTB-first approach matters: clean process data, a structured knowledge base, "
            "and well-configured workflows are the prerequisites that Now Assist requires to deliver value."
        ),
        "why_matters_bullets": [
            "Incident Summary generation reduces the time agents spend reading context before acting — immediate productivity gain",
            "Resolution note generation improves knowledge base quality automatically — resolved tickets become knowledge assets",
            "Now Assist in VA means the chatbot can answer questions it was never explicitly programmed for — if the knowledge exists",
        ],
        "ootb_intro": (
            "Now Assist capabilities are included in your ServiceNow AI licensing. The following "
            "are available for activation — each with its own configuration and prerequisite checklist."
        ),
        "ootb_capabilities": [
            ["Now Assist for Incident (Summary + Resolution Suggestion)", "AI-generated incident summary for agents; suggested resolution steps based on similar closed tickets and knowledge"],
            ["Now Assist for Change (Risk Assessment)", "AI-generated risk assessment narrative based on the CI being changed, historical change data, and impacted services"],
            ["Now Assist for Virtual Agent (Generative Answers)", "LLM-powered conversational answers grounded in your knowledge articles — improves VA containment without additional topic configuration"],
            ["Now Assist for Knowledge (Article Generation)", "Converts incident resolution notes to knowledge article drafts — accelerates knowledge base growth"],
            ["Responsible AI controls (Data residency, PII filtering)", "OOTB controls for AI output governance — configurable content filters and data handling policies"],
            ["Now Assist analytics", "Usage dashboard: interactions by capability, agent acceptance rate, time saved estimates"],
        ],
        "decisions_intro": (
            "These are the decisions your team will make about Now Assist deployment scope and governance."
        ),
        "decisions": [
            {
                "label": "Now Assist Activation Scope",
                "body": "Which Now Assist capabilities will be activated at go-live, and which will be deferred to a later phase? The recommendation is to activate Incident Summary and Resolution Suggestion first — immediate, measurable agent productivity gain with low data prerequisite.",
            },
            {
                "label": "Data Governance and Privacy",
                "body": "What data will Now Assist have access to — all incident data, or a filtered subset that excludes sensitive records? Your security and compliance team will need to review the Now Assist data flow documentation and sign off on the scope of data used for AI generation.",
                "tradeoff": "Broader data access produces better AI outputs; narrower data scope provides stronger privacy controls but limits AI quality for edge cases.",
            },
            {
                "label": "Agent Acceptance Workflow",
                "body": "When Now Assist suggests a resolution, is it applied automatically or does the agent review and accept it? The OOTB model is agent-in-the-loop — suggestions are presented, not applied. The workshop will confirm this design and configure the UX accordingly.",
            },
        ],
        "reflection_intro": (
            "These questions help scope the Now Assist conversation for your organization."
        ),
        "reflection_questions": [
            "What AI capabilities are included in your current ServiceNow license tier?",
            "Are there data classification or handling requirements that would restrict what data Now Assist can access?",
            "What is your security team's review process for new AI capability deployment?",
            "How mature is your knowledge base? Now Assist for VA improves dramatically with well-structured knowledge articles.",
            "What productivity metrics does your service desk currently track? These will be the baseline for measuring Now Assist impact.",
        ],
        "what_to_bring": [
            "ServiceNow license tier documentation (confirms which Now Assist capabilities are included)",
            "Data classification policy — particularly around ticket content and PII",
            "Security review contacts for AI capability deployment",
            "Current service desk productivity metrics (handle time, first-contact resolution rate)",
        ],
    },

    # =========================================================================
    # 12. CSDM
    # =========================================================================
    {
        "doc_id": "CLT-WP-02l",
        "short_name": "CSDM",
        "filename": "WP_12_CSDM_CLIENT.docx",
        "title": "Common Service Data Model\n(CSDM) Workshop Pre-Read",
        "subtitle": "Building the service taxonomy that connects your IT capabilities to business outcomes",
        "audience": "IT Leadership, Service Architects, CMDB Owners, Process Owners, Business Relationship Managers",
        "companion_to": "CMDB Pre-Read · Discovery Pre-Read · Change Management Pre-Read",
        "how_to_use": (
            "CSDM is one of the more conceptual workshops in the engagement — it is about defining "
            "the language and structure that connects IT assets (servers, applications, devices) to "
            "the business services they support. Getting this structure right unlocks value across "
            "Incident, Change, CMDB, Service Graph, and AI capabilities. This pre-read gives you "
            "the conceptual foundation before the workshop."
        ),
        "what_is": (
            "The Common Service Data Model (CSDM) is ServiceNow's framework for structuring how "
            "IT services, applications, and technical components relate to each other and to the "
            "business outcomes they support. It defines a set of standard tables, relationships, "
            "and classification levels — from raw infrastructure (servers, databases) up through "
            "technical services, business applications, and business services."
        ),
        "what_is_bullets": [
            "Business Services — the IT-delivered capabilities that the business cares about (e.g., 'Payroll Processing', 'Email')",
            "Business Applications — the software applications that deliver business services",
            "Technical Services — the technical building blocks that support applications",
            "CIs (Configuration Items) — the individual infrastructure components (servers, databases, network devices)",
            "Service relationships — the parent-child hierarchy that connects CIs to services to business outcomes",
        ],
        "why_matters": (
            "Without CSDM, your ServiceNow data is a collection of disconnected records — incidents "
            "that reference systems by name, changes that don't know which business service they affect, "
            "a CMDB full of CIs with no context for why they matter. CSDM provides the connective tissue. "
            "With it, an incident automatically shows which business service is affected, a Change's risk "
            "score reflects the criticality of the service it touches, and AI capabilities understand "
            "the business context of a technical event."
        ),
        "why_matters_bullets": [
            "Business service mapping enables automated impact assessment for incidents and changes",
            "Service hierarchy data is the prerequisite for Service Graph Connectors to produce useful maps",
            "CSDM provides the business context that makes AI recommendations meaningful, not just technically accurate",
        ],
        "ootb_intro": (
            "ServiceNow's OOTB CSDM framework provides a ready-to-use data model, guided setup tools, "
            "and a maturity assessment to help you adopt the model at the right pace."
        ),
        "ootb_capabilities": [
            ["CSDM framework tables (OOTB)", "Pre-built tables for Business Service, Business Application, Technical Service, and all relationship layers"],
            ["CSDM maturity assessment", "Guided assessment tool that identifies where your current data sits on the CSDM maturity curve"],
            ["Service Mapping (guided)", "Assisted process for mapping technical CIs to business services — with pattern-based auto-discovery options"],
            ["Application Portfolio Management (APM)", "OOTB application registry and lifecycle tracking built on CSDM tables"],
            ["Impact mapping", "Automatic incident impact calculation based on CSDM service hierarchy — surfaces business exposure from technical events"],
            ["CSDM health dashboard", "Data quality metrics for CSDM completeness — identifies gaps in service mapping"],
        ],
        "decisions_intro": (
            "These are the CSDM decisions for the workshop. The most important is scope — "
            "how much of the CSDM hierarchy to build at implementation vs. grow over time."
        ),
        "decisions": [
            {
                "label": "CSDM Adoption Scope for Phase One",
                "body": "How much of the CSDM hierarchy will you build in Sprint 4? The recommendation is to start with Business Services and their direct application relationships — this produces immediate value for Incident impact mapping and Change risk scoring. Full CSDM maturity is a program, not a sprint.",
                "tradeoff": "Starting narrow produces faster value; attempting full CSDM maturity in one sprint typically produces incomplete, low-quality data.",
            },
            {
                "label": "Business Service Definition",
                "body": "What are your organization's Business Services — the IT-delivered capabilities that the business cares about? This is a business-IT alignment conversation. The workshop will facilitate the initial list, but it requires input from business relationship managers or process owners, not just IT.",
            },
            {
                "label": "Data Ownership",
                "body": "Who owns CSDM data ongoing — who populates it, who validates it, and who keeps it current as the environment changes? Without clear ownership, CSDM data decays quickly after go-live. We will define data ownership roles in the workshop.",
            },
        ],
        "reflection_intro": (
            "These questions will help your team prepare for the CSDM discussion."
        ),
        "reflection_questions": [
            "Can you name the 10–15 most critical business capabilities that IT supports? (These become your starting Business Services.)",
            "Do you have an existing application inventory or CMDB? How current and complete is it?",
            "Who in your organization owns the relationship between IT systems and business processes — IT, Enterprise Architecture, or Business Relationship Management?",
            "Are there specific Incident or Change use cases where understanding business service impact is most critical?",
        ],
        "what_to_bring": [
            "Application inventory or existing CMDB export (however rough)",
            "List of 10–15 critical business services or capabilities",
            "Enterprise architecture or service portfolio documentation if available",
            "Business relationship manager contacts",
        ],
    },

    # =========================================================================
    # 13. CMDB
    # =========================================================================
    {
        "doc_id": "CLT-WP-02m",
        "short_name": "CMDB",
        "filename": "WP_13_CMDB_CLIENT.docx",
        "title": "CMDB Workshop Pre-Read",
        "subtitle": "Building the configuration foundation that powers accurate operations and AI insights",
        "audience": "CMDB Owners, IT Operations, Infrastructure Teams, Security Teams, Asset Management",
        "companion_to": "CSDM Pre-Read · Discovery Pre-Read · HAM Pre-Read",
        "how_to_use": (
            "The CMDB (Configuration Management Database) workshop defines which infrastructure "
            "components your ServiceNow instance will track, how they will be discovered or "
            "populated, and how they will be kept current. This pre-read helps you understand "
            "the scope of the CMDB conversation and the decisions that will define its architecture."
        ),
        "what_is": (
            "The CMDB is ServiceNow's database of Configuration Items (CIs) — the infrastructure "
            "components (servers, applications, databases, network devices, endpoints) that your "
            "IT environment depends on. It is the source of truth for what exists in your environment "
            "and what connects to what. The CMDB powers Incident impact assessment, Change risk scoring, "
            "Discovery, Service Graph, HAM, and AI capabilities across the platform."
        ),
        "what_is_bullets": [
            "Configuration Items (CIs) — individual tracked components (servers, applications, switches, endpoints)",
            "CI classes — the taxonomy that defines what types of CIs exist and what attributes each type has",
            "Relationships — the connections between CIs (runs on, hosted by, depends on, connects to)",
            "CMDB Health — data quality metrics that measure completeness, accuracy, and freshness",
            "Discovery integration — automated CI population from network scans and agent-based discovery",
        ],
        "why_matters": (
            "The CMDB is the nervous system of your ServiceNow platform. Incidents reference CIs to "
            "show what is affected. Changes reference CIs to calculate risk. HAM tracks assets as CIs. "
            "Discovery populates CIs automatically. AI capabilities use CI context to make smarter "
            "recommendations. A well-maintained CMDB is the single most cross-cutting data quality "
            "investment in a ServiceNow implementation."
        ),
        "why_matters_bullets": [
            "CI-linked incidents automatically surface impacted services and related records — reducing investigation time",
            "Change risk scoring requires accurate CI data — particularly CI classification and relationship data",
            "Discovery without a defined CMDB scope produces CI sprawl — tracking everything means making sense of nothing",
        ],
        "ootb_intro": (
            "ServiceNow's OOTB CMDB provides a mature data model, health scoring, and integration "
            "with Discovery and Service Graph out of the box."
        ),
        "ootb_capabilities": [
            ["CI class hierarchy", "OOTB CI taxonomy covering servers, applications, databases, network, endpoints, cloud, and more — extensible without schema changes"],
            ["CMDB Health dashboard", "Data quality scoring across completeness, staleness, duplicates, and orphaned records — identifies where CMDB investment is most needed"],
            ["Identification and Reconciliation Engine (IRE)", "Automated CI deduplication and reconciliation engine — prevents the 'CI sprawl' problem when multiple sources populate the CMDB"],
            ["Relationship mapping", "OOTB relationship types and visual dependency map for CI-to-CI and CI-to-service relationships"],
            ["CMDB Query Builder", "Visual query tool for creating impact assessments and CI reports without database skills"],
            ["Discovery integration", "OOTB Discovery populates and updates CMDB CIs automatically from network and cloud scans"],
            ["Service Graph Connector integration", "Pre-built connectors for AWS, Azure, VMware, and others populate cloud CIs automatically"],
        ],
        "decisions_intro": (
            "These CMDB decisions will define the scope and governance of your configuration data."
        ),
        "decisions": [
            {
                "label": "CI Class Scope",
                "body": "Which CI classes will you populate in Phase 1? The recommendation is to start with the classes that are directly relevant to your in-scope process areas: server and application CIs for Incident and Change, endpoint CIs for HAM. Expand scope in later phases as Discovery coverage grows.",
                "tradeoff": "Narrow scope produces higher quality data for the CIs that matter most; broad scope attempts to capture everything but typically results in low data quality across all classes.",
            },
            {
                "label": "CMDB Population Method",
                "body": "How will CIs be populated — automated Discovery, Service Graph Connectors, manual import, or a combination? The workshop will define a population strategy that matches your environment: on-premises vs. cloud-heavy vs. hybrid.",
            },
            {
                "label": "CMDB Governance and Ownership",
                "body": "Who owns CMDB data quality? Who reviews CMDB Health scores, investigates staleness, and approves new CI classes? Without clear governance, CMDB quality degrades within months of go-live. The workshop will define ownership roles and review cadence.",
            },
        ],
        "reflection_intro": (
            "These questions will help your infrastructure and operations teams prepare."
        ),
        "reflection_questions": [
            "Do you have an existing CMDB? If so, how current and accurate is the data?",
            "How is your infrastructure organized — primarily on-premises, cloud, or hybrid?",
            "Are there specific CI types (servers, applications, endpoints) that are most important for your initial Incident and Change use cases?",
            "Who currently maintains infrastructure inventory in your organization?",
            "What cloud environments (AWS, Azure, GCP) are in scope for Discovery or Service Graph integration?",
        ],
        "what_to_bring": [
            "Existing CMDB export or infrastructure inventory (however informal)",
            "Network and infrastructure architecture diagram",
            "Cloud account inventory (AWS accounts, Azure subscriptions, etc.)",
            "Current data center and server inventory list",
        ],
    },

    # =========================================================================
    # 14. Discovery
    # =========================================================================
    {
        "doc_id": "CLT-WP-02n",
        "short_name": "Discovery",
        "filename": "WP_14_Discovery_CLIENT.docx",
        "title": "Discovery Workshop Pre-Read",
        "subtitle": "Automating the population and maintenance of your CMDB through network-based scanning",
        "audience": "CMDB Owners, Infrastructure Teams, Network Teams, Security Teams",
        "companion_to": "CMDB Pre-Read · Service Graph Pre-Read · HAM Pre-Read",
        "how_to_use": (
            "Discovery is the ServiceNow capability that scans your network infrastructure, "
            "identifies devices and applications, and populates your CMDB automatically. "
            "The Discovery workshop defines the scope, credentials, and schedule for that "
            "scanning process. This pre-read helps you prepare for the technical and scope "
            "decisions the workshop will cover."
        ),
        "what_is": (
            "Discovery is ServiceNow's network-based scanning capability. It uses MID Servers "
            "(Management, Instrumentation, and Discovery servers installed in your network) "
            "to scan IP ranges, authenticate against discovered devices, and extract infrastructure "
            "details — OS, installed software, network interfaces, running processes, and relationships. "
            "That data is used to populate and update CMDB CIs automatically."
        ),
        "what_is_bullets": [
            "MID Server — an agent installed in your network environment that executes Discovery scans",
            "Discovery schedules — configured scan timing and IP range scope",
            "Credentials — authentication details for discovered devices (SSH, WMI, SNMP, etc.)",
            "CI population — Discovery creates and updates CMDB records for discovered components",
            "Horizontal Discovery vs. Service Mapping — Discovery finds what exists; Service Mapping finds how components connect to services",
        ],
        "why_matters": (
            "Manual CMDB population is a project, not a process. It produces a snapshot of your "
            "environment that is accurate at the moment of entry and increasingly inaccurate thereafter. "
            "Discovery turns CMDB maintenance into an ongoing, automated process — CIs are created "
            "when new infrastructure is added and updated when configurations change, without manual effort."
        ),
        "why_matters_bullets": [
            "Automated CI updates mean your CMDB reflects actual infrastructure, not what someone last recorded",
            "Discovery-populated CIs are trusted by Incident, Change, and HAM processes — increasing process accuracy",
            "Discovery scope decisions directly determine CMDB completeness — getting the scope right at the start prevents rework",
        ],
        "ootb_intro": (
            "ServiceNow Discovery is a mature, multi-protocol scanning platform. The following "
            "OOTB capabilities define what Discovery can do without custom development."
        ),
        "ootb_capabilities": [
            ["MID Server (multi-platform)", "Installs on Windows or Linux, deployed in your network segments — one MID Server per network zone or cloud environment"],
            ["Multi-protocol scanning", "Supports SSH (Linux/Unix), WMI (Windows), SNMP (network devices), JDBC (databases), and REST (cloud APIs)"],
            ["Pattern-based discovery", "Pre-built discovery patterns for common infrastructure components: Windows Server, Linux, Cisco, VMware, AWS, Azure, Oracle, SQL Server"],
            ["Cloud Discovery (native)", "Native integration with AWS, Azure, GCP, and other cloud providers — discovers cloud resources without network scanning"],
            ["Discovery schedule management", "Configurable scan schedules by IP range, frequency, and MID Server — supports incremental and full scans"],
            ["CMDB reconciliation", "Automatic CI deduplication and update using ServiceNow's IRE — prevents duplicate CIs from repeat scans"],
            ["Discovery log and audit", "Detailed scan logs for troubleshooting and compliance — shows what was found, what was created, and what failed"],
        ],
        "decisions_intro": (
            "These Discovery decisions will be worked through in the workshop. They require "
            "coordination with your network and security teams."
        ),
        "decisions": [
            {
                "label": "Discovery Scope (Phase 1)",
                "body": "Which IP ranges and network segments will be in scope for Discovery in Phase 1? The recommendation is to start with the segments hosting your most critical services and expand based on CMDB coverage metrics. Attempting to discover the entire network in Phase 1 typically produces CI sprawl.",
                "tradeoff": "Narrow scope produces high-quality, high-trust CMDB data for critical infrastructure; broad scope attempts to capture everything but creates noise that reduces trust in the data.",
            },
            {
                "label": "MID Server Placement",
                "body": "How many MID Servers will be deployed, and where? The workshop will review your network architecture and recommend a MID Server placement that provides scanning coverage without creating security boundary issues.",
            },
            {
                "label": "Credential Management",
                "body": "How will Discovery credentials be provided and managed? ServiceNow Credential Store can hold service account credentials securely. The workshop will define the credential scope and identify which teams need to provide authentication for their environments.",
            },
        ],
        "reflection_intro": (
            "These questions will help your network and security teams prepare for the Discovery workshop."
        ),
        "reflection_questions": [
            "Do you have existing network documentation — IP ranges, VLANs, subnets?",
            "What infrastructure environments are in scope — on-premises data centers, cloud environments, or both?",
            "Are there network security controls (firewalls, segmentation) that would restrict scanning traffic?",
            "What service accounts can be created for Discovery — and who approves service account creation?",
            "Are there environments that should be excluded from Discovery for security or compliance reasons?",
        ],
        "what_to_bring": [
            "Network topology diagram and IP range documentation",
            "List of critical server and infrastructure segments to prioritize",
            "Firewall policy or ACL documentation for Discovery traffic planning",
            "Service account provisioning process and contacts",
            "Cloud environment inventory (AWS accounts, Azure subscriptions, VPC/VNet details)",
        ],
    },

    # =========================================================================
    # 15. Service Graph Connectors
    # =========================================================================
    {
        "doc_id": "CLT-WP-02o",
        "short_name": "Service Graph Connectors",
        "filename": "WP_15_Service_Graph_Connectors_CLIENT.docx",
        "title": "Service Graph Connectors\nWorkshop Pre-Read",
        "subtitle": "Extending CMDB coverage to cloud and third-party tools through purpose-built integrations",
        "audience": "CMDB Owners, Cloud Infrastructure Teams, IT Operations, Enterprise Architecture",
        "companion_to": "CMDB Pre-Read · Discovery Pre-Read · Integrations Pre-Read",
        "how_to_use": (
            "Service Graph Connectors (SGCs) are the bridge between your external infrastructure "
            "tools — AWS, Azure, VMware, Intune, Qualys, and others — and your ServiceNow CMDB. "
            "Where Discovery scans network-accessible devices, SGCs pull structured data directly "
            "from the APIs of third-party platforms. This pre-read helps you understand which "
            "connectors apply to your environment and what decisions they require."
        ),
        "what_is": (
            "Service Graph Connectors are certified, pre-built integrations from ServiceNow that "
            "pull CI data from third-party infrastructure platforms and populate the CMDB. They use "
            "the Service Graph — a real-time, relationship-aware data layer — to ensure that imported "
            "CIs are correctly classified, de-duplicated, and related to each other. They are the "
            "fastest path to CMDB completeness for cloud and managed environments."
        ),
        "what_is_bullets": [
            "Pre-built connectors — certified integrations for 70+ third-party tools (AWS, Azure, VMware, Intune, Okta, Qualys, and more)",
            "Service Graph layer — ensures imported CIs are correctly reconciled against existing CMDB data",
            "Relationship mapping — connectors import not just CIs but the relationships between them",
            "Scheduled synchronization — configurable refresh intervals to keep CMDB data current with source systems",
            "Publisher certification — connectors are certified by ServiceNow and updated with platform releases",
        ],
        "why_matters": (
            "Modern IT environments span multiple cloud providers, managed services, and security tools. "
            "Discovery covers network-accessible infrastructure well, but cloud resources, SaaS applications, "
            "and security scan results require API-based ingestion that Discovery alone does not provide. "
            "Service Graph Connectors fill that gap — extending CMDB coverage to the full breadth of your "
            "environment without custom integration development."
        ),
        "why_matters_bullets": [
            "AWS and Azure SGCs populate cloud resource CIs in near-real-time — eliminating manual cloud inventory tracking",
            "Intune SGC populates endpoint CIs with software inventory — providing the asset data HAM workflows depend on",
            "Qualys or Tenable SGCs enrich CIs with vulnerability data — connecting security findings to the infrastructure they affect",
        ],
        "ootb_intro": (
            "ServiceNow's OOTB Service Graph Connector catalog covers the most common enterprise infrastructure platforms. "
            "The following represent the connectors most relevant to typical ECS Federal engagements."
        ),
        "ootb_capabilities": [
            ["AWS Service Graph Connector", "Populates EC2, S3, RDS, Lambda, VPC, and other AWS resources as CMDB CIs with relationship mapping"],
            ["Azure Service Graph Connector", "Populates Azure VMs, App Services, SQL Databases, Virtual Networks, and Entra ID objects"],
            ["VMware vCenter Connector", "Populates VMs, hosts, clusters, and datastore CIs from on-premises VMware environments"],
            ["Microsoft Intune Connector", "Populates endpoint CIs with hardware, OS, and software inventory — feeds HAM and endpoint management"],
            ["Qualys / Tenable Connectors", "Enriches CI records with vulnerability scan findings and risk scores"],
            ["Okta Connector", "Populates application and user relationship data from identity management"],
            ["ServiceNow Discovery (complementary)", "Connectors and Discovery work together — each covers what the other cannot"],
        ],
        "decisions_intro": (
            "These are the Service Graph Connector decisions for the workshop."
        ),
        "decisions": [
            {
                "label": "Connector Prioritization",
                "body": "Which Service Graph Connectors are in scope for Phase 1? The workshop will map your infrastructure environment to the available connector catalog and prioritize based on CMDB coverage impact. Connectors for cloud environments (AWS, Azure) and endpoint management (Intune) are typically the highest-value starting points.",
            },
            {
                "label": "API Access and Credential Scope",
                "body": "Each connector requires API access to the source system. The workshop will define the permission scope for each connector's service account — read-only API access is sufficient for CI population and avoids write-back risks.",
            },
            {
                "label": "Synchronization Frequency",
                "body": "How frequently should each connector synchronize with its source system? Cloud environments change frequently and benefit from hourly or daily sync; on-premises environments with slower change rates may synchronize weekly without losing meaningful accuracy.",
            },
        ],
        "reflection_intro": (
            "These questions will help map your environment to available connectors."
        ),
        "reflection_questions": [
            "What cloud platforms do you use — AWS, Azure, GCP, a combination?",
            "Is your endpoint estate managed through Microsoft Intune, SCCM, or another MDM platform?",
            "Do you use a vulnerability scanning tool (Qualys, Tenable, Rapid7)? Is there a desire to surface findings in ServiceNow?",
            "What on-premises virtualization platforms are in use (VMware, Hyper-V)?",
            "Who manages API access for your cloud platforms — cloud infrastructure team or a central platform team?",
        ],
        "what_to_bring": [
            "Cloud platform account inventory (AWS accounts, Azure subscriptions)",
            "MDM/endpoint management tool details (Intune tenant, SCCM hierarchy)",
            "Vulnerability scanner deployment details if applicable",
            "API access approval process contacts for cloud platforms",
        ],
    },

    # =========================================================================
    # 16. Hardware Asset Management (HAM)
    # =========================================================================
    {
        "doc_id": "CLT-WP-02p",
        "short_name": "Hardware Asset Management",
        "filename": "WP_16_Hardware_Asset_Management_CLIENT.docx",
        "title": "Hardware Asset Management\nWorkshop Pre-Read",
        "subtitle": "Managing hardware assets from procurement through retirement with full lifecycle visibility",
        "audience": "Asset Managers, IT Procurement, Finance, IT Operations, End User Computing Teams",
        "companion_to": "CMDB Pre-Read · Discovery Pre-Read · Integrations Pre-Read",
        "how_to_use": (
            "Hardware Asset Management (HAM) in ServiceNow tracks the full lifecycle of your physical "
            "and virtual IT assets — from purchase order through assignment, refresh, and retirement. "
            "This pre-read helps you understand the HAM lifecycle model, what ServiceNow delivers "
            "out of the box, and the decisions you will make in the HAM workshop to configure it "
            "for your organization."
        ),
        "what_is": (
            "Hardware Asset Management (HAM) is the discipline of tracking IT hardware assets "
            "through their complete lifecycle — acquisition, receiving, stock management, deployment, "
            "maintenance, refresh, and retirement/disposal. In ServiceNow, HAM is built on the CMDB "
            "(hardware assets are CIs) and adds procurement, inventory, contract, and lifecycle "
            "management on top of that foundation."
        ),
        "what_is_bullets": [
            "Asset lifecycle — the progression of an asset from Ordered → Received → In Stock → Deployed → In Maintenance → Retired",
            "Asset repository — the central catalog of every tracked hardware asset with full attribute history",
            "Procurement and purchase orders — integration between asset requests and purchasing processes",
            "Stock rooms — physical and virtual storage locations for assets not yet deployed",
            "Disposal and retirement — documented end-of-life process with financial reconciliation",
        ],
        "why_matters": (
            "Most organizations have hardware assets distributed across spreadsheets, procurement systems, "
            "and individual team records. The cost of that fragmentation is real: assets that cannot be "
            "found, maintenance contracts paid on retired equipment, refresh cycles missed because the "
            "inventory is inaccurate, and audit responses assembled from incomplete data. "
            "ServiceNow HAM consolidates that into a single, AI-ready asset lifecycle record that "
            "connects procurement, IT operations, finance, and end users."
        ),
        "why_matters_bullets": [
            "Accurate asset inventory eliminates the cost of paying maintenance on retired equipment — a frequent audit finding",
            "Lifecycle tracking with auto-generated refresh reminders means hardware refresh cycles are planned, not emergency decisions",
            "Integration with Discovery and Intune means asset records stay current automatically, not through manual survey",
        ],
        "ootb_intro": (
            "ServiceNow's OOTB Hardware Asset Management is a complete lifecycle platform. "
            "The following capabilities are available from day one in the HAM Foundation and "
            "Realization accelerator packs."
        ),
        "ootb_capabilities": [
            ["Asset lifecycle management", "Full lifecycle state machine from Order through Retirement — with state-specific workflows and notifications"],
            ["Hardware Asset Workspace", "Unified workspace for asset managers: inventory views, lifecycle dashboards, pending actions, and stock management"],
            ["Procurement integration (PO management)", "Purchase order creation, PO-to-asset linkage, and receiving workflow — assets enter the system at receipt"],
            ["Stock room management", "Virtual stock room tracking with check-in/check-out, transfer, and reorder level management"],
            ["Discovery and Intune integration", "Auto-population and update of hardware CIs from network scans and MDM data"],
            ["Maintenance contract linkage", "Asset-to-contract relationships with expiration alerts and renewal workflows"],
            ["Disposal workflow (with ITAD integration)", "Retirement and disposal documentation with audit trail — supports ITAD vendor integration and data sanitization tracking"],
            ["HAM analytics", "OOTB dashboards: asset age distribution, refresh readiness, stock levels, disposal pipeline, cost by category"],
        ],
        "decisions_intro": (
            "These are the HAM decisions that will be worked through in your workshop. "
            "They require input from IT Operations, Finance, and Procurement."
        ),
        "decisions": [
            {
                "label": "Asset Scope for Phase 1",
                "body": "Which hardware asset categories will HAM track at go-live — laptops and desktops only, or also servers, network equipment, mobile devices, and peripherals? The recommendation is to start with end-user computing (laptops, desktops) and expand to data center and network assets in a subsequent phase.",
                "tradeoff": "End-user computing scope is highest-volume and most visible to finance and HR; data center scope is more complex but higher-value for infrastructure management.",
            },
            {
                "label": "Procurement Integration",
                "body": "Will HAM connect to your existing procurement system (Ariba, Oracle, a shared spreadsheet process) to receive purchase order data? Procurement integration is the entry point for assets — without it, assets must be manually received into the system.",
            },
            {
                "label": "Discovery / Intune Linkage",
                "body": "How will HAM CIs be kept current — through ServiceNow Discovery, Intune Service Graph Connector, manual updates, or a combination? Automated population is strongly recommended for end-user computing. The workshop will define the linkage strategy.",
            },
            {
                "label": "Disposal and Retirement Process",
                "body": "What is your current hardware retirement and disposal process, and which steps need to be documented in ServiceNow for audit purposes? Many organizations have data sanitization, ITAD vendor, and financial write-off steps that need to be encoded in the retirement workflow.",
            },
        ],
        "reflection_intro": (
            "These questions will help your asset management, procurement, and finance teams "
            "prepare for the HAM workshop."
        ),
        "reflection_questions": [
            "Where is your current hardware asset inventory maintained — spreadsheets, a dedicated tool, your existing ITSM system?",
            "How many hardware assets does your organization have in active use? Approximate numbers by category (laptops, servers, etc.) are helpful.",
            "What procurement system do you use, and does it generate purchase order data that could be fed to ServiceNow?",
            "Is your endpoint estate managed through Microsoft Intune, SCCM, or another MDM tool?",
            "What is your current hardware refresh cycle — how do you decide when a device is due for replacement?",
        ],
        "what_to_bring": [
            "Current hardware asset inventory export (spreadsheet, CMDB, or existing tool)",
            "Procurement system details and POC for integration planning",
            "MDM tool details (Intune tenant, SCCM hierarchy) if applicable",
            "Current asset categories and approximate counts by category",
            "Hardware refresh policy or lifecycle standards documentation",
        ],
    },
]


# =============================================================================
# BUILD ALL
# =============================================================================
if __name__ == "__main__":
    print(f"\nBuilding {len(DISCIPLINES)} Workshop Pre-Reads → 02_Client/05_Workshop_Pre-Reads/\n")
    built = []
    for d in DISCIPLINES:
        try:
            f = build_pre_read(d)
            built.append(f)
        except Exception as e:
            print(f"  ✗  {d['doc_id']}  ERROR: {e}")
            raise
    print(f"\n✅  All {len(built)} pre-reads built successfully.\n")
