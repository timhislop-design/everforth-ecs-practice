"""
Build INT-TBV-05 — Customization Council Pre-Read Template
48-hour-advance document for every Customization Council meeting.
Contains: Request summary, OOTB Alternative Analysis, Business Outcome Alignment,
          Contract Risk, SA Recommendation, and Council Decision block.
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

OUT = os.path.join(HERE, "INT-TBV-05_Council_Pre-Read_Template.docx")

d = EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL TEMPLATE · CUSTOMIZATION COUNCIL",
    title="Customization Council\nPre-Read Template",
    subtitle="Circulate 48 hours before every Council meeting — no pre-read, no Council",
    audience="Practice Lead · Engagement Manager · Solution Architect · Customer Sponsor (receives redacted version)",
    companion_to="INT-TBV-01 (Manager Playbook) · INT-TBV-03 (Variance Tracker) · ECS Internal Governance Operating Guide",
    doc_id="INT-TBV-05",
    version="1.0",
    status="Released",
    running_header_label="Internal · Customization Council Pre-Read Template",
))

d.add_cover_page()

d.para(
    "The Customization Council Pre-Read is the mechanism that separates a disciplined customization decision "
    "from a verbal commitment made under sponsor pressure. Every Council meeting requires this document, circulated "
    "48 hours in advance. Sponsors who arrive without reading the pre-read are rescheduled. The Council is not "
    "the reading session."
)

d.h1("How to Use This Template", numbered=False)
d.para(
    "The Solution Architect completes Sections 1 through 4. The Engagement Manager completes Section 5 "
    "(Contract Risk). The SA and EM jointly draft the Recommendation in Section 6. The Practice Lead reviews "
    "the complete pre-read before circulation. Section 7 (Council Decision) is completed during the meeting. "
    "A copy of the completed pre-read — including the decision — is filed in the engagement's SharePoint folder "
    "and the decision is recorded in INT-TBV-03 (Variance Tracker)."
)
d.callout(
    "This template covers one customization request per document. If multiple requests are being decided "
    "in the same Council session, create one pre-read per request and bundle them with a cover page listing all items."
)

d.page_break()

# ── SECTION 1: REQUEST SUMMARY ────────────────────────────────────────────────
d.h1("Section 1 — Customization Request Summary")
d.para("Complete this section before the OOTB Alternative Analysis. It frames what is being decided.")
d.table(
    headers=["Field", "Value"],
    rows=[
        ["Request ID (from INT-TBV-03)",       "[CVT-###]"],
        ["Engagement Name",                     "[Enter engagement name]"],
        ["Sprint Raised",                       "[e.g., Sprint 2]"],
        ["Requestor",                           "[Customer SME name and role]"],
        ["Request Date",                        "[Date raised]"],
        ["Council Date (proposed)",             "[Date — 48+ hrs after this pre-read circulation]"],
        ["Classification",                      "[Customization | PCR]"],
        ["Request Description (one paragraph)", "[Describe the customer's stated need in their language — not ECS language]"],
        ["Business Justification (as stated by customer)", "[Verbatim or close paraphrase of what the customer said — resist translating yet]"],
        ["ServiceNow Module / Area Affected",   "[e.g., Incident Management, Service Catalog, CMDB]"],
        ["Scope Estimate (hours)",              "[SA initial estimate — will be refined in Section 3]"],
    ],
    col_widths_in=[2.6, 5.8],
)

d.page_break()

# ── SECTION 2: OOTB ALTERNATIVE ANALYSIS ─────────────────────────────────────
d.h1("Section 2 — OOTB Alternative Analysis")
d.para("Completed by the Solution Architect. This is the core discipline document. Be specific — 'the OOTB way works' is not an analysis.")

d.h2("2.1 What the customer is trying to accomplish")
d.para(
    "Translate the customer's stated request into the underlying business outcome they are trying to achieve. "
    "Often the request and the outcome are different. Example: 'We want a custom approval flow' → "
    "Outcome: 'We want to ensure that hardware requests over $5,000 are approved by a VP before fulfillment.'"
)
d.para("[Enter the underlying business outcome here — one or two sentences]")

d.h2("2.2 The OOTB path to that outcome")
d.para("Describe specifically how ServiceNow OOTB handles the underlying business outcome. Include table names, module names, and configuration options.")
d.para("[Enter the OOTB approach here — be specific enough that a consultant could implement it from this description]")

d.h2("2.3 Gap analysis — what OOTB does not cover")
d.para(
    "Identify the specific gap between what OOTB provides and what the customer needs. "
    "Be precise — 'OOTB doesn't support that' is not a gap analysis. "
    "A gap analysis names the specific field, workflow step, or behavior that cannot be configured without code."
)
d.para("[Enter the specific gaps here. If there are no real gaps — if OOTB fully covers the need — state that and recommend rejection.]")

d.h2("2.4 Effort to close the gap via OOTB configuration")
d.para("If the gap can be closed with OOTB configuration (not customization), estimate the effort and describe the configuration approach.")
d.para("[Enter OOTB configuration effort estimate and approach, or 'Not applicable — gap requires code change']")

d.h2("2.5 OOTB Alternative Recommendation")
d.table(
    headers=["SA Assessment", "Detail"],
    rows=[
        ["OOTB fully covers the need",           "[Yes / No]"],
        ["OOTB with configuration covers the need","[Yes / No — if yes, describe the configuration]"],
        ["Genuine gap requiring code change",    "[Yes / No — if yes, estimated scope: ___ hours]"],
        ["SA recommends",                        "[Approve / Reject / Redesign with customer / PCR]"],
    ],
    col_widths_in=[3.0, 5.4],
)

d.page_break()

# ── SECTION 3: SCOPE AND EFFORT ───────────────────────────────────────────────
d.h1("Section 3 — Scope and Effort Estimate")
d.para("Completed by the Solution Architect. Required whether the recommendation is Approve or Reject.")

d.table(
    headers=["Estimate Component", "Hours", "Notes"],
    rows=[
        ["Build (code / configuration)",  "", ""],
        ["Test (unit + integration)",     "", ""],
        ["Customer validation / UAT support", "", ""],
        ["Documentation",                 "", ""],
        ["Post-go-live support / maintenance (annual estimate)", "", "Customer-owned after handoff"],
        ["TOTAL",                         "=SUM above", ""],
    ],
    col_widths_in=[3.0, 1.2, 4.2],
)

d.h2("Sprint capacity impact")
d.para("Express the total effort as a percentage of the sprint capacity in which it would be built.")
d.table(
    headers=["Metric", "Value"],
    rows=[
        ["Sprint target for this build",        "[Sprint X]"],
        ["Sprint capacity (hrs)",               "[From INT-TBV-03 Capacity Reference tab]"],
        ["This request's effort (hrs)",         "[From table above]"],
        ["Capacity consumed by this request",   "[Effort / Capacity × 100%]"],
        ["Cumulative variance if approved",     "[From INT-TBV-02 — current variance + this request]"],
        ["Projected band after approval",       "[Green / Yellow / Orange / Red]"],
    ],
    col_widths_in=[3.0, 5.4],
)

d.page_break()

# ── SECTION 4: BUSINESS OUTCOME ALIGNMENT ────────────────────────────────────
d.h1("Section 4 — Business Outcome and AI Realization Alignment")
d.para(
    "Completed by the Solution Architect with input from the Process Consultant. "
    "The Council's two-key decision model requires both a business-need key (customer) and a technical-path key (ECS). "
    "This section supplies the analysis that allows the customer to sign the business-need key in an informed way."
)

d.h2("4.1 AI realization impact")
d.para(
    "ServiceNow's AI features (Now Assist, Predictive Intelligence, Virtual Agent resolution, etc.) depend on "
    "clean, OOTB-aligned data in standard tables. Customizations that write to custom tables or bypass OOTB "
    "workflows can block AI adoption. Assess this request's impact."
)
d.table(
    headers=["AI Impact Factor", "Assessment", "Detail"],
    rows=[
        ["Now Assist compatibility",         "[Not impacted / Reduced / Blocked]", ""],
        ["Predictive Intelligence data quality","[Not impacted / Reduced / Blocked]", ""],
        ["Virtual Agent resolution scope",   "[Not impacted / Reduced / Blocked]", ""],
        ["Future OOTB upgrade compatibility","[Not impacted / Reduced / Blocked]", ""],
    ],
    col_widths_in=[2.4, 1.8, 4.2],
)

d.h2("4.2 Technical debt created")
d.para("Describe the technical debt this customization introduces if approved. Be specific — 'it adds debt' is not an assessment.")
d.para("[Enter specific technical debt created: upgrade risk, maintenance burden, future rework estimate]")

d.h2("4.3 Alternative ways to meet the business need")
d.para(
    "If the OOTB alternative does not fully close the gap, describe alternative business process approaches "
    "that could meet the outcome without customization. Example: a process change that eliminates the need "
    "for the custom approval flow, or a phased approach that defers the requirement to a follow-on engagement."
)
d.para("[Enter alternatives — or 'No viable process alternative identified']")

d.page_break()

# ── SECTION 5: CONTRACT RISK ──────────────────────────────────────────────────
d.h1("Section 5 — Contract Risk Assessment")
d.para("Completed by the Engagement Manager.")

d.table(
    headers=["Contract Risk Factor", "Assessment", "Notes"],
    rows=[
        ["Is this within the current SOW scope?",  "[Yes / No / Borderline]", ""],
        ["Does approving this require a PCR?",     "[Yes / No — if borderline, explain]", ""],
        ["Does approving this set a precedent that opens the door to similar requests?",
         "[Yes / No — if yes, name the follow-on risk]", ""],
        ["Is the SOW language ambiguous in a way the customer may use to argue entitlement?",
         "[Yes / No — if yes, cite the clause]", ""],
        ["Recommended commercial action",          "[No action / Monitor / PCR / Escalate]", ""],
    ],
    col_widths_in=[3.2, 1.8, 3.4],
)

d.page_break()

# ── SECTION 6: RECOMMENDATION ─────────────────────────────────────────────────
d.h1("Section 6 — ECS Recommendation")
d.para("Drafted jointly by the Solution Architect and Engagement Manager. The Practice Lead reviews before circulation.")

d.h2("6.1 Recommended Council decision")
d.table(
    headers=["Option", "Selected?", "Rationale"],
    rows=[
        ["Approve — build in Sprint [X]",    "[Yes / No]", ""],
        ["Approve — defer to product backlog","[Yes / No]", ""],
        ["Reject — OOTB alternative sufficient","[Yes / No]", ""],
        ["PCR — scope exceeds SOW",           "[Yes / No]", ""],
    ],
    col_widths_in=[2.4, 1.0, 5.0],
)

d.h2("6.2 Recommendation rationale")
d.para("[Enter a concise paragraph summarizing why ECS is making this recommendation. This is what the sponsor reads most carefully.]")

d.h2("6.3 Conditions of approval (if recommending Approve)")
d.para("If recommending approval, state the conditions — what the customer must confirm and what ECS must deliver.")
d.para("[Enter conditions, or 'Not applicable — rejection or PCR recommended']")

d.h2("6.4 What happens if the Council rejects this recommendation")
d.para(
    "Describe the path forward if the Council makes a different decision than recommended. "
    "This ensures the Council understands consequences and is not deciding blind."
)
d.para("[Enter the alternative path — e.g., 'If the Council approves contrary to SA recommendation, ECS will build under protest and document the AI realization risk in the engagement record.']")

d.page_break()

# ── SECTION 7: COUNCIL DECISION ───────────────────────────────────────────────
d.h1("Section 7 — Council Decision Record")
d.para("Completed during the Council meeting by the Engagement Manager. This is the official record.")

d.table(
    headers=["Field", "Value"],
    rows=[
        ["Council Date",                    ""],
        ["Attendees (name and role)",        ""],
        ["Decision",                        "[Approve-Sprint / Approve-Backlog / Reject / PCR]"],
        ["Sprint approved for (if applicable)", ""],
        ["Conditions of approval",          ""],
        ["Customer sponsor sign-off",       "[Sponsor name + verbal confirmation noted]"],
        ["Practice Lead sign-off",          "[Practice Lead name + signature or initials]"],
        ["Date entered in INT-TBV-03",      ""],
        ["Date filed in engagement SharePoint", ""],
    ],
    col_widths_in=[2.8, 5.6],
)

d.callout(
    "A Council decision is not final until both keys are signed: the customer sponsor signs the business-need key "
    "and the ECS Practice Lead signs the technical-path key. Verbal agreement in the meeting is not sufficient. "
    "The EM records both sign-offs in this table before any build commitment is made."
)

d.h1("Quick Reference — Completing This Template")
d.table(
    headers=["Section", "Who Completes", "When"],
    rows=[
        ["1 – Request Summary",               "Engagement Manager",      "Immediately when request is raised"],
        ["2 – OOTB Alternative Analysis",     "Solution Architect",      "Within 48 hrs of request"],
        ["3 – Scope and Effort",              "Solution Architect",      "With Section 2"],
        ["4 – Business Outcome Alignment",    "SA + Process Consultant", "Before scheduling Council"],
        ["5 – Contract Risk",                 "Engagement Manager",      "Before scheduling Council"],
        ["6 – Recommendation",               "SA + EM, reviewed by PL", "48 hrs before Council — then circulate"],
        ["7 – Council Decision",             "EM (during meeting)",     "During Council — filed within 24 hrs"],
    ],
    col_widths_in=[2.6, 2.2, 3.6],
)

d.save(OUT)
print(f"Saved: {OUT}")
