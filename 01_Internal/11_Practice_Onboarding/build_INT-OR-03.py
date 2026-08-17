"""
Build INT-OR-03 — Solution Architect Role Narrative (v2.0)
Internal artifact: concise, general-purpose role & responsibilities narrative for a
ServiceNow Solution Architect splitting time 50/50 between delivery and presales
(demos, RFX response technical content). Summary-first, ~3 content pages.
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
OUT = os.path.join(HERE, "INT-OR-03_Solution_Architect_Role_Narrative_INTERNAL.docx")

doc = EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL ROLE DESCRIPTION",
    title="Solution Architect\nRole Narrative",
    subtitle="A hybrid ServiceNow role — half delivery leadership, half presales",
    audience="Practice Lead, Delivery Leadership, Engagement Managers, Solution Architects, Capture & Proposal Leads",
    companion_to="ServiceNow Leadership R&R (V4) · Roles & Expectations (CLT-EO-02)",
    doc_id="INT-OR-03",
    version="2.0",
    status="Draft",
    running_header_label="Internal · Solution Architect Role Narrative",
), logo_path=LOGO)
doc.add_cover_page()
doc.page_break()

# ─────────────────────────────────────────────────
# ROLE SUMMARY AT A GLANCE
# ─────────────────────────────────────────────────
doc.h1("Role Summary at a Glance", numbered=False)
doc.para(
    "The ECS Solution Architect is the practice's senior ServiceNow technical resource, "
    "with time committed evenly between active delivery engagements and presales pursuits. "
    "One person, two halves: the technical authority on the engagements we have won, and "
    "the technical voice on the work we are trying to win."
)
doc.h3("Delivery responsibilities (50%)")
doc.bullet("Own the solution architecture and technical design for assigned engagements.")
doc.bullet("Lead technical design decisions — data model, integrations, security, and platform configuration approach.")
doc.bullet("Provide technical sign-off: review and accept configuration, code, and integration work before it reaches the customer.")
doc.bullet("Serve as the technical voice in design workshops and requirements sessions.")
doc.bullet("Guide the technical consultants; set and enforce development and configuration standards.")
doc.bullet("Own technical risk: identify, escalate, and resolve architecture and platform risks through go-live.")
doc.h3("Presales responsibilities (50%)")
doc.bullet("Lead technical discovery with prospective customers; assess current platforms and requirements.")
doc.bullet("Shape solution concepts: products, phasing, integration approach, and delivery assumptions.")
doc.bullet("Design, build, and deliver product demonstrations tailored to the customer's use cases.")
doc.bullet("Develop the technical content of RFX responses — solution narratives, technical approaches, compliance responses, white papers, and orals support.")
doc.bullet("Provide draft level-of-effort and scoping input to the estimate.")
doc.bullet("Maintain reusable presales assets: demo environments and scenarios, reference architectures, solution briefs.")
doc.bullet("Hand off the technical solution baseline to the delivery team at award.")
doc.h3("Key boundaries")
doc.bullet("Drafts level of effort only — final hours, staffing, pricing, rates, and margin are owned by delivery and practice leadership.")
doc.bullet("Complex, high-risk, or nonstandard pursuit solutions are validated with the Lead Architect before submission.")
doc.bullet("Committed delivery obligations are protected first when delivery and pursuit demands collide.")

# ─────────────────────────────────────────────────
# 1. ROLE PURPOSE
# ─────────────────────────────────────────────────
doc.h1("Role Purpose", numbered=True)
doc.para(
    "The 50/50 split is deliberate. An architect who only sells drifts toward promising "
    "what the platform brochure says; an architect who only delivers loses sight of what "
    "the market is asking for. The hybrid Solution Architect closes that loop: "
    "demonstrations and proposals are grounded in patterns the SA has personally "
    "delivered, and every estimate carries the credibility of someone who will live with "
    "it after award. What we demonstrate is what we deliver — because the same person "
    "owns both."
)

# ─────────────────────────────────────────────────
# 2. DELIVERY HALF
# ─────────────────────────────────────────────────
doc.h1("The Delivery Half", numbered=True)
doc.para(
    "On an active engagement the SA is the technical authority. The SA owns the "
    "end-to-end solution architecture — data model, module configuration approach, "
    "integration design, security model, and environment strategy — and every design "
    "decision traces back to the SA. Where a requirement can be met multiple ways, the "
    "SA weighs configuration against custom development, documents the trade-offs, and "
    "makes the recommendation that best serves the customer's long-term platform health."
)
doc.para(
    "The SA holds technical sign-off: configuration and code review, integration "
    "acceptance, and the technical quality of what the delivery team builds. The SA "
    "mentors the technical consultants, sets development standards, and is the "
    "escalation point for any technical blocker. In workshops and requirements "
    "sessions, the SA is the voice that makes the platform's capabilities concrete."
)
doc.para(
    "The SA's delivery load is front-weighted: heaviest during initiation and design, "
    "steady through build (reviews and sign-off), lighter through testing and go-live. "
    "That shape is what makes the hybrid model workable — presales surges are steered "
    "toward the lighter phases, and design-heavy windows are protected in advance."
)

# ─────────────────────────────────────────────────
# 3. PRESALES HALF
# ─────────────────────────────────────────────────
doc.h1("The Presales Half", numbered=True)
doc.para(
    "The other half of the SA's time belongs to pre-award growth, working with capture "
    "and proposal teams, delivery leadership, and the Practice Lead. For each qualified "
    "pursuit the SA leads technical discovery — the prospect's processes, existing "
    "platform, integrations, data, and constraints — and translates it into a credible "
    "solution concept: which ServiceNow products, what phasing, what is configuration "
    "versus development versus integration, and where the risk lives. The SA adjusts "
    "the technical altitude for the audience without changing the substance."
)
doc.para(
    "Demonstrations are a core craft of the role. The SA designs, prepares, and delivers "
    "demos tied to the customer's actual use cases — not feature tours — and maintains "
    "the practice's demo environments, scenarios, and scripts so each pursuit starts "
    "from a working foundation. Every demonstration must reflect what a real delivery "
    "team can build and support; the SA's own delivery half is the built-in reality check."
)
doc.para(
    "On RFX responses, the SA owns the technical volume: solution narratives, technical "
    "approaches, architecture diagrams, compliance responses, white papers, and orals "
    "support across RFIs, RFQs, RFPs, task orders, and teaming requests — content that "
    "is accurate, persuasive, internally consistent, and traceable to the solicitation's "
    "requirements. The SA also develops the technical scope baseline — assumptions, "
    "dependencies, exclusions, and risks — and provides draft level-of-effort input, "
    "flagging weak requirements and capability gaps before submission. When a pursuit is "
    "won, the SA hands the delivery team the full solution baseline and stays available "
    "for questions of pre-award intent."
)

# ─────────────────────────────────────────────────
# 4. DECISION RIGHTS
# ─────────────────────────────────────────────────
doc.h1("Decision Rights and Boundaries", numbered=True)
doc.table(
    headers=["Decision", "SA's role", "Who decides"],
    rows=[
        ["Engagement architecture and design", "Owns", "SA"],
        ["Technical sign-off on delivered work", "Owns", "SA"],
        ["Pre-award solution baseline (standard)", "Owns", "SA, within delegated thresholds"],
        ["High-risk / nonstandard pursuits", "Develops", "SA + Lead Architect validation"],
        ["Level of effort and staffing", "Drafts input", "Delivery leadership"],
        ["Pricing strategy, rates, and margin", "Informs", "Delivery leadership + Practice Lead"],
        ["Bid / no-bid", "Recommends", "Practice leadership"],
    ],
    col_widths_in=[3.5, 1.9, 3.96],
)
doc.callout(
    "THE LINE THAT MATTERS MOST: The SA never owns price — final hours, staffing, "
    "rates, and margin belong to delivery and practice leadership."
)

# ─────────────────────────────────────────────────
# 5. MANAGING THE SPLIT
# ─────────────────────────────────────────────────
doc.h1("Managing the 50/50 Split", numbered=True)
doc.para(
    "The split is a planning commitment measured over a quarter, not a weekly timesheet "
    "target. Collisions are managed by rule: committed delivery obligations are protected "
    "first, with pursuits drawing on pre-identified backup architecture capacity; presales "
    "surges are planned against the engagement calendar weeks ahead; and sustained drift "
    "past roughly 60/40 is raised to leadership as a capacity signal. When a genuine "
    "conflict remains, delivery leadership and the Practice Lead arbitrate — the SA does "
    "not adjudicate their own split."
)

# ─────────────────────────────────────────────────
# 6. SUCCESS MEASURES
# ─────────────────────────────────────────────────
doc.h1("Success Measures", numbered=True)
doc.bullet("Delivery: engagement technical health, quality of technical sign-off (defect escape rate), and customer confidence in the architecture.")
doc.bullet("Presales: on-time, compliant technical volumes; demos that materially advance (or correctly disqualify) opportunities; currency and reuse of demo and proposal assets; estimate integrity — how rarely pre-award assumptions surface as surprises after award.")
doc.bullet("The loop: alignment between what was proposed and what was delivered on pursuits the SA shaped — the signature metric of the hybrid model.")

doc.save(OUT)
print(f"Saved: {OUT}")
