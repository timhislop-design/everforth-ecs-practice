"""
Build INT-AR-01, INT-AR-02, INT-AR-03 — Adopt-vs-Re-engineer Cheatsheets
Batch build: Catalog Item Rationalization, Category Structure Simplification, SLA Discipline.

Internal audience — direct, prescriptive, zero customer-softening language.
Designed to be printed and kept in the consultant's workshop kit.
Each cheatsheet: customer pattern → OOTB adopt path → re-engineer trigger → decision rule
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta


def build_cheatsheet(meta_kwargs, intro, table_rows, objections, footer_note, out_path):
    doc = EcsDocument(meta=DocMeta(**meta_kwargs), logo_path=LOGO)
    doc.add_cover_page()
    doc.page_break()

    doc.h1("How to Use This Cheatsheet", numbered=False)
    doc.para(intro)

    doc.callout(
        "Governance rule: Any item pattern flagged for Re-engineer goes into the Engagement "
        "Governance Triage Log before any scope commitment. No custom build without Delivery "
        "Manager review and customer sign-off."
    )

    doc.page_break()

    doc.h1("Pattern Decision Table")
    doc.para(
        "For each item pattern encountered during discovery, call Adopt or flag for Re-engineer "
        "using the decision rule in the rightmost column. The Adopt path is the default; Re-engineer "
        "is the exception. Shift the burden of proof to the exception."
    )

    doc.table(
        headers=["Customer Pattern", "OOTB Adopt Path", "Re-engineer Trigger", "Decision Rule"],
        rows=table_rows,
        col_widths_in=[2.0, 2.2, 2.2, 2.96],
    )

    doc.page_break()

    doc.h1("Common Objections — Consulting Response")
    doc.para(
        "These objections surface in nearly every engagement. Use the responses below verbatim or "
        "adapt to the customer's specific language. The responses are designed to acknowledge the "
        "customer's concern before redirecting to the OOTB capability."
    )

    doc.table(
        headers=["Objection", "Consulting Response"],
        rows=objections,
        col_widths_in=[4.0, 5.36],
    )

    doc.para(footer_note, italic=True, size=9)

    doc.save(out_path)
    print(f"Saved: {out_path}")


# =============================================================================
# INT-AR-01 — Catalog Item Rationalization
# =============================================================================
build_cheatsheet(
    meta_kwargs=dict(
        eyebrow="INTERNAL · ADOPT-VS-RE-ENGINEER CHEATSHEET",
        title="Catalog Item\nRationalization",
        subtitle="When to adopt the OOTB catalog model, when to flag an exception, and how to handle the objections",
        audience="ECS Delivery Consultants, Engagement Managers, Solution Architects",
        companion_to="CLT-DT-01 Catalog Item Rationalization Decision Guide · INT-TBV-03 Customization Variance Tracker",
        doc_id="INT-AR-01",
        version="1.0",
        status="Released",
        running_header_label="Internal · Adopt-vs-Re-engineer · Catalog Item Rationalization",
    ),
    intro=(
        "Use this cheatsheet during discovery conversations and workshops when a customer raises "
        "a catalog pattern that may trigger a customization request. The table below gives you the "
        "decision rule for each common pattern before the customer asks. Your job is to call Adopt "
        "proactively — not to wait for the customer to propose a custom build and then respond. "
        "Every flagged Re-engineer item goes into the Engagement Governance Triage Log (INT-TBV-03). "
        "No item gets a custom-build commitment without Delivery Manager review."
    ),
    table_rows=[
        [
            "Near-duplicate items (same service, different names or populations)",
            "Consolidate into one item with OOTB variables/options. Use user criteria for audience targeting.",
            "Distinct regulatory requirement that mandates separate record trails for each variant.",
            "Adopt by default. The burden of proof is on the regulatory requirement — get it in writing before splitting."
        ],
        [
            "Items with 20+ custom fields, many unused by fulfillers",
            "Audit fields with fulfillment team. Remove non-load-bearing fields. Use OOTB variables for the survivors.",
            "Integration requirement that demands specific field payloads at submission time.",
            "Adopt: prune form to load-bearing fields only. Flag integration requirement for integration-layer handling, not catalog-layer."
        ],
        [
            "Approval chains with non-standard sequencing (skip-level, parallel, conditional)",
            "OOTB Approval Engine handles sequential, parallel, and group approvals without customization.",
            "Documented regulatory or contractual requirement for approval sequence not achievable in OOTB engine.",
            "Adopt the OOTB engine first. Model the customer's chain in a whiteboard session — 90% of chains fit without customization."
        ],
        [
            "Items tightly coupled to legacy integrations (ITSM, ERP, HR system)",
            "Decouple at catalog layer. Item captures the request; integration logic lives in the fulfillment workflow.",
            "Integration must receive catalog-item data at the moment of submission (sync, not async).",
            "Adopt catalog item as-is. Flag integration pattern for the Integration Accelerator Pack — not a catalog problem."
        ],
        [
            "Retired items still in catalog (no submissions in 12+ months)",
            "Archive: remove from active catalog, map historical requests to surviving items.",
            "None. Retire. Full stop.",
            "Always retire. Do not preserve for historical browsing — ServiceNow reporting runs against closed records, not catalog items."
        ],
        [
            "Items built from scratch that duplicate OOTB catalog items (software request, hardware request, access request)",
            "Replace with OOTB item. Map differences as options or variables within the OOTB item.",
            "Legal or compliance requirement documented in writing that cannot be met by the OOTB item.",
            "Adopt the OOTB item. Most from-scratch items were built because OOTB wasn't understood, not because OOTB was insufficient."
        ],
        [
            "Items with complex visibility rules (department-gated, role-filtered, org-unit restricted)",
            "OOTB user criteria on catalog items + topic/category access controls in Employee Center.",
            "Visibility must evaluate real-time data from an external system not available in ServiceNow.",
            "Adopt OOTB user criteria. If external data is needed, explore ServiceNow integration before flagging as Re-engineer."
        ],
    ],
    objections=[
        [
            '"Our approvers need to see specific fields in the approval notification."',
            "OOTB approval notifications are fully configurable — field selection, layout, and wording can all be adjusted without custom development. Confirm which fields the approver actually needs before concluding that customization is required."
        ],
        [
            '"We have always had separate items for VIP vs. standard users."',
            "OOTB user criteria + SLA definitions handle tiered service without separate items. Consolidate the items; differentiate via SLA priority and assignment group. The user experience is identical — the back-of-house structure is cleaner."
        ],
        [
            '"Some items have 50+ fields. We cannot lose that data."',
            "50-field forms suppress submission rates, break AI classification, and are maintained by no one. Identify the fields fulfillers actually look at — in practice, almost always fewer than 12. Move non-load-bearing fields to the notes field or a post-submission task."
        ],
        [
            '"Our fulfillment team needs to see each variant as a separate queue entry."',
            "Assignment rules and list views handle queue differentiation without catalog-level separation. Design the fulfillment view alongside the catalog item count — agree queue design first, then see if separate items are still needed."
        ],
        [
            '"We built these items over 10 years — changing them will break everything."',
            "Rationalization does not break in-flight requests. Retired items are archived, not deleted — closed records are preserved. The migration mapping table documents the consolidation path for each item. The change is invisible to users after go-live."
        ],
    ],
    footer_note=(
        "INT-AR-01 v1.0 · Internal Use Only · Confidential. Items flagged for Re-engineer are logged in "
        "INT-TBV-03 Customization Variance Tracker. No scope commitment without Delivery Manager review. "
        "Customer-facing companion: CLT-DT-01 Catalog Item Rationalization Decision Guide."
    ),
    out_path=os.path.join(HERE, "INT-AR-01_Catalog_Rationalization_Cheatsheet_INTERNAL.docx"),
)


# =============================================================================
# INT-AR-02 — Category Structure Simplification
# =============================================================================
build_cheatsheet(
    meta_kwargs=dict(
        eyebrow="INTERNAL · ADOPT-VS-RE-ENGINEER CHEATSHEET",
        title="Category Structure\nSimplification",
        subtitle="When to adopt the OOTB Employee Center taxonomy, when to flag an exception, and how to handle the objections",
        audience="ECS Delivery Consultants, Engagement Managers, Solution Architects",
        companion_to="CLT-DT-02 Category Structure Simplification Decision Guide · INT-TBV-03 Customization Variance Tracker",
        doc_id="INT-AR-02",
        version="1.0",
        status="Released",
        running_header_label="Internal · Adopt-vs-Re-engineer · Category Structure Simplification",
    ),
    intro=(
        "Use this cheatsheet when a customer's existing category structure is being reviewed for the new "
        "Employee Center portal. The most common failure mode is carrying the old taxonomy forward unchanged — "
        "a taxonomy built for a five-level menu will not perform in Employee Center's search-and-browse model. "
        "Your job is to drive toward a simplified taxonomy proactively. Call out category bloat before the "
        "customer defends each node. Every Re-engineer flag goes into the Engagement Governance Triage Log."
    ),
    table_rows=[
        [
            "Category hierarchy deeper than 3 levels",
            "OOTB Employee Center supports 3 levels natively. Flatten to: Domain > Category > Subcategory.",
            "Regulatory requirement to restrict category visibility by org unit that cannot be met with 3-level structure.",
            "Adopt 3-level max. Use OOTB user criteria and topic access controls for audience targeting — depth is not the answer."
        ],
        [
            "Top-level category count > 20",
            "Employee Center performs best with 12-18 top-level categories. Consolidate by service domain.",
            "None. No regulatory or contractual driver justifies category count > 20.",
            "Adopt: target 12-18 top-level categories. Use search and topic taxonomy to compensate for any perceived loss of granularity."
        ],
        [
            "Duplicate categories across service areas (e.g., 'IT Requests' and 'IT Support' and 'IT Help')",
            "One canonical category per service domain. Merge duplicates; redirect to the canonical.",
            "None. Duplicates are always consolidatable.",
            "Adopt: consolidate without exception. Duplicate categories are a usability failure, not a design feature."
        ],
        [
            "Category names reflect IT org structure rather than user language (e.g., 'Infrastructure Services', 'Enterprise Applications')",
            "Rename to match user mental model: 'Computers & Devices', 'Software & Apps'. OOTB taxonomy is fully configurable.",
            "None.",
            "Adopt: user language always wins. Conduct a 5-minute card sort in the workshop if the team disagrees."
        ],
        [
            "Categories with fewer than 5 items",
            "Consolidate into parent or adjacent category. Items too few to warrant a category belong in a broader bucket.",
            "None. Category count is never a compliance requirement.",
            "Adopt: collapse categories with < 5 items. The exception would be a category expected to grow — document the growth plan."
        ],
        [
            "Department-specific sub-portals demanded by each business unit",
            "OOTB Employee Center supports audience-targeted landing pages within a single portal. No separate instances needed.",
            "Regulatory separation requiring distinct portal instances (rare; typically only in defense/classified contexts).",
            "Adopt single portal with audience targeting. Separate portals multiply maintenance burden and fragment the user experience."
        ],
    ],
    objections=[
        [
            '"Each team needs their own category."',
            "Teams get assignment rules and groups, not categories. Categories are for users — they describe what you can request, not which team handles it. Reassign the team model to the fulfillment layer where it belongs."
        ],
        [
            '"We cannot combine IT and HR items in the same navigation."',
            "OOTB topic taxonomy separates content by department at the topic level without requiring separate top-level categories. Employee Center's audience targeting delivers the right content to the right user — the structure doesn't have to mirror the org chart."
        ],
        [
            '"Our current taxonomy has 6 levels. Users know how to navigate it."',
            "Some users may know the current taxonomy because they learned it over years. New users don't. Employee Center users search first; they browse only if search fails. A 6-level taxonomy that requires prior knowledge will underperform in a search-first model."
        ],
        [
            '"If we collapse categories, users will not find things."',
            "The opposite is the finding from nearly every engagement. Fewer, clearer categories with strong naming improve findability because search doesn't have to compete with a confusing hierarchy. The data will show this — pull pre/post search success rates from your most recent go-live."
        ],
    ],
    footer_note=(
        "INT-AR-02 v1.0 · Internal Use Only · Confidential. Items flagged for Re-engineer are logged in "
        "INT-TBV-03 Customization Variance Tracker. No scope commitment without Delivery Manager review. "
        "Customer-facing companion: CLT-DT-02 Category Structure Simplification Decision Guide."
    ),
    out_path=os.path.join(HERE, "INT-AR-02_Category_Simplification_Cheatsheet_INTERNAL.docx"),
)


# =============================================================================
# INT-AR-03 — SLA Discipline
# =============================================================================
build_cheatsheet(
    meta_kwargs=dict(
        eyebrow="INTERNAL · ADOPT-VS-RE-ENGINEER CHEATSHEET",
        title="SLA Discipline",
        subtitle="When to adopt OOTB SLA definitions, when to flag an exception, and how to handle the objections",
        audience="ECS Delivery Consultants, Engagement Managers, Solution Architects",
        companion_to="CLT-DT-03 SLA Discipline Decision Guide · INT-TBV-03 Customization Variance Tracker",
        doc_id="INT-AR-03",
        version="1.0",
        status="Released",
        running_header_label="Internal · Adopt-vs-Re-engineer · SLA Discipline",
    ),
    intro=(
        "SLA configurations are one of the most common sources of unnecessary complexity in ServiceNow "
        "implementations. Customers arrive with 80-200 SLA definitions accumulated over years; OOTB best "
        "practice is 8-15. Your job is to drive toward simplification before the workshop. Every SLA "
        "definition a customer carries forward is a maintenance obligation they will own forever. Use this "
        "cheatsheet to call the adopt path before the customer proposes a custom SLA definition. Every "
        "Re-engineer flag goes into the Engagement Governance Triage Log."
    ),
    table_rows=[
        [
            "SLA count > 30 definitions across incident, request, and change",
            "Consolidate to a priority-based matrix: P1/P2/P3/P4 x business-hours/24-7. OOTB SLA engine supports this natively.",
            "Contractual SLAs tied to specific service areas that are documented in a customer agreement and cannot be subsumed into priority tiers.",
            "Adopt: start with 8-12 definitions. Add service-specific SLAs only where a signed contract requires it — and get the contract clause."
        ],
        [
            "SLA targets tighter than the team can realistically meet (e.g., 30-min response for P3)",
            "OOTB SLA reporting will surface compliance rates immediately. Reset targets to what the team can meet, then improve.",
            "Contractual obligation with financial penalty for breach — already signed.",
            "Adopt realistic targets first. Pull 90-day historical data from the current system. SLAs the team never meets are not SLAs — they are failure documentation."
        ],
        [
            "Business-hours SLAs mixed with 24/7 SLAs without calendar control",
            "OOTB SLA schedules with business-hours calendars handle the mix natively. Define business hours calendar in Sprint 0.",
            "None. OOTB schedule handles all standard business hours patterns.",
            "Adopt: define business hours calendar early. This is a Sprint 0 data item, not a customization."
        ],
        [
            "SLAs that reset the clock on reassignment",
            "OOTB SLA pause/resume handles reassignment scenarios. Pause on reassignment, resume when new group accepts.",
            "Contractual requirement that the SLA clock runs continuously through reassignment (documented in a signed agreement).",
            "Adopt pause/resume. This is the correct operational model in nearly all cases — it incentivizes clean routing."
        ],
        [
            "SLA definitions without escalation paths",
            "Every OOTB SLA definition should have an escalation notification at 50% and 75% of target. OOTB notification engine handles this.",
            "None. Escalation is always appropriate.",
            "Adopt: no SLA definition ships without escalation. An SLA without an escalation is a breach waiting to happen with no warning."
        ],
        [
            "SLAs applied to change records without regard to change type (Normal, Standard, Emergency)",
            "OOTB change management distinguishes change types; SLA application should follow type. Emergency change gets a different SLA than Normal change.",
            "None. OOTB change type SLA mapping is the correct model.",
            "Adopt: define SLAs by change type, not by a single change SLA. The distinction already exists in OOTB change management."
        ],
        [
            "SLAs with complex conditions (VIP caller, specific department, asset class)",
            "OOTB SLA conditions support attribute-based triggering. VIP caller, department, and CI class are native conditions.",
            "Condition requires real-time data from an external system not available in ServiceNow at the time of record creation.",
            "Adopt: model conditions in the SLA definition using OOTB fields. External data dependency goes in the Integration Accelerator Pack."
        ],
    ],
    objections=[
        [
            '"Our SLAs are unique to each service — we cannot standardize."',
            "The claim that every service needs a unique SLA is almost always based on historical practice, not current requirement. Priority tiers handle 80-90% of SLA variation. Ask the customer: what is the consequence of a P2 breach for Service A vs. Service B? If the answer is the same, they don't need different SLAs."
        ],
        [
            '"The business expects 2-hour response for all P2 items."',
            "Pull the last 90 days of P2 SLA compliance from their current system. In most environments, 2-hour P2 response is below 60% compliance. Setting a target you cannot meet is not a service commitment — it is a documented failure. Reset the target to what the team can actually deliver, then build toward the aspirational target."
        ],
        [
            '"We cannot change SLAs without executive approval."',
            "Agreed — and the SLA workshop agenda includes executive sign-off. Frame the conversation as a compliance discussion, not a target reduction. 'We are recommending targets your team can actually meet and report green on, with a roadmap to tighten them as operations mature.' Executives respond to that framing."
        ],
        [
            '"We need SLAs on everything — catalog items, changes, incidents, problems, even tasks."',
            "SLAs on every record type is a sign that the monitoring instinct is sound but the tooling decision is wrong. For tasks and sub-records, use SLA on the parent record and time-tracking on the task. Multiplying SLA definitions multiplies false breaches, alert fatigue, and reporting noise."
        ],
    ],
    footer_note=(
        "INT-AR-03 v1.0 · Internal Use Only · Confidential. Items flagged for Re-engineer are logged in "
        "INT-TBV-03 Customization Variance Tracker. No scope commitment without Delivery Manager review. "
        "Customer-facing companion: CLT-DT-03 SLA Discipline Decision Guide."
    ),
    out_path=os.path.join(HERE, "INT-AR-03_SLA_Discipline_Cheatsheet_INTERNAL.docx"),
)

print("All three cheatsheets built successfully.")
