"""
Build AP — Service Catalog Accelerator Pack
6 xlsx workbooks + 1 README docx, branded to the canonical ECS standard.

Scope: Category structure rationalization (3-level max), catalog item inventory
and triage, item template and variable standards, fulfillment workflow decisions,
approval policy matrix, and config-ready catalog item data.

Sprint alignment: Month 2 — Sprint 4 (first high-priority catalog items configured),
with final items in Sprint 6.
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
TEMPLATES = os.path.join(REPO, "03_Shared", "00_Templates_and_Branding")
sys.path.insert(0, TEMPLATES)

from accelerator_pack_builder import TabContent, build_workbook
from ecs_template import EcsDocument, DocMeta

PACK_NAME = "Service Catalog Accelerator Pack"

# =============================================================================
# WORKBOOK 1 — Category Rationalization
# =============================================================================
wb1 = TabContent(
    workbook_title="01 — Category Rationalization",
    pack_name=PACK_NAME,
    purpose="Defines the simplified category and subcategory structure for the ServiceNow Service Catalog, applying the OOTB 3-level maximum (Catalog > Category > Subcategory). This workbook replaces the legacy 'everything has its own category' pattern with a user-centric structure that is browsable, maintainable, and compatible with Employee Center search and Virtual Agent intent matching.",
    who_fills="Customer-side: ITSM Process Owner and a representative end user (ideally someone from HR or a business unit that uses IT services heavily). ECS SA facilitates the rationalization workshop. Customer approves the final category structure before Workbook 02 begins.",
    sprint_window="Sprint 3 Week 2 — Sprint 4 Week 1",
    estimated_effort="3–4 hours (one rationalization workshop + customer review)",
    related_workbooks=["02 Catalog Item Inventory", "03 Item Template Standards", "Foundation Data Pack — Departments"],
    success_criteria=[
        "Legacy category list is audited and the proposed new structure is documented.",
        "The new structure has no more than 3 levels (Catalog > Category > Subcategory).",
        "Every category has a named owner (the group responsible for items in that category).",
        "The structure is approved by the ITSM Process Owner before item triage begins.",
        "The total number of top-level categories is 6 or fewer for the IT catalog.",
    ],
    process_decisions=[
        ("How many top-level categories should the IT Service Catalog have?",
         "6 or fewer. Recommended structure: IT Equipment, Software & Licensing, Access & Security, Infrastructure Services, HR & Onboarding, and General Requests. Each category should be meaningful to an end user, not to an IT team.",
         "Catalogs with 20+ top-level categories force users to browse extensively and reduce self-service adoption. OOTB Employee Center search is the primary discovery mechanism — category structure is for browsing, not for taxonomy. Fewer, clearer categories drive higher adoption."),
        ("Should categories reflect IT team structure or user needs?",
         "User needs. Categories should reflect what a user is trying to accomplish, not which IT team handles it. 'Access & Security' is a user need; 'Active Directory Team Requests' is an IT team structure.",
         "User-centric categories drive self-service adoption. Team-centric categories require the user to know which team handles their request before they can find the right item — defeating the purpose of a self-service catalog."),
        ("Should we have separate catalogs for IT and HR?",
         "Yes if HR services are in scope. Use the OOTB multi-catalog feature: one catalog for IT Services, one for HR Services. This is the Employee Center design pattern and requires no customisation.",
         "Mixing IT and HR items in a single catalog creates confusion about ownership and fulfillment. The OOTB multi-catalog model is the right architecture for Employee Center."),
        ("How do we handle categories from the legacy system that don't map neatly?",
         "Map every legacy category to the new structure. Legacy categories that cannot map to any new category are candidates for the 'General Requests' catch-all. Flag these for Workbook 02 triage — some may be retired.",
         "A legacy category that has no equivalent in the new structure usually contains items that are either duplicates, rarely used, or should be handled by a different process (e.g., a category full of items that should be Incident subtypes, not catalog requests)."),
        ("Should subcategories be mandatory or optional?",
         "Optional. Use subcategories only where a category contains more than 8–10 items AND the items naturally cluster into sub-groups. Do not create subcategories for the sake of structure.",
         "Subcategories add a navigation step. If a category has 5 items, a subcategory forces the user to click twice to find them. The OOTB search reduces the value of deep navigation hierarchies."),
        ("How do we handle seasonal or project-specific catalog items (e.g., new hire equipment bundles)?",
         "Keep these as regular catalog items within the appropriate category. Use the 'Available for' field to limit visibility to appropriate user populations. Do not create project-specific categories.",
         "Project-specific categories become orphaned after the project ends. Use item-level visibility controls (Available for, Available to) rather than category proliferation."),
    ],
    dependencies=[
        ("Existing catalog item list (from legacy system or current ServiceNow instance)", "Required", "Customer ITSM Owner", "Sprint 3 Wk 2", "Cannot rationalize categories without knowing what items will live in them."),
        ("Foundation Data Pack — Departments loaded", "Required", "ECS SA", "Sprint 0", "Category ownership maps to departments/groups. Groups must exist."),
        ("CSDM Business Service list (Workbook 03 from CMDB-CSDM pack) confirmed", "Recommended", "ECS SA + Customer EA", "Sprint 2", "Category structure should complement the Business Service taxonomy, not contradict it."),
        ("Employee Center design decisions (Employee Center pack, if in scope)", "Recommended", "ECS SA", "Sprint 3", "Employee Center homepage layout affects how categories are displayed. Align before finalising category names."),
    ],
    config_sections=[
        ("Proposed Category Structure — IT Service Catalog", [
            ("Catalog Name", "IT Services", "OOTB: one catalog per domain (IT, HR). Do not merge.", False),
            ("Category 1", "IT Equipment", "Laptops, monitors, peripherals, mobile devices.", True),
            ("Category 2", "Software & Licensing", "Software requests, licence requests, application access.", True),
            ("Category 3", "Access & Security", "New accounts, access requests, password resets, MFA.", True),
            ("Category 4", "Infrastructure Services", "VPN, storage, network drives, server requests.", True),
            ("Category 5", "HR & Onboarding", "New hire setup, offboarding, transfer requests.", True),
            ("Category 6", "General Requests", "Catch-all for items not fitting the above. Review quarterly.", True),
        ]),
        ("Category Ownership", [
            ("Category owner assignment", "Each category must have a named fulfillment group as owner", "Used for routing and accountability. Must be an existing assignment group.", True),
            ("IT Equipment — owner group", "[Customer to complete]", "Typically End User Computing or IT Operations.", True),
            ("Software & Licensing — owner group", "[Customer to complete]", "Typically Software Asset Management or IT Operations.", True),
            ("Access & Security — owner group", "[Customer to complete]", "Typically Identity & Access Management or IT Security.", True),
            ("Infrastructure Services — owner group", "[Customer to complete]", "Typically Infrastructure/Server team.", True),
            ("HR & Onboarding — owner group", "[Customer to complete]", "Joint: HR and IT Operations.", True),
        ]),
        ("Legacy Category Mapping", [
            ("Legacy category mapping approach", "Document legacy category → new category mapping before Workbook 02", "Every legacy category must be accounted for. Unmapped categories = items to triage.", False),
            ("Legacy categories with no new equivalent", "[Customer to complete — list here]", "These items will be triaged in Workbook 02 as Retire or consolidate.", True),
        ]),
    ],
    raci_rows=[
        ("Facilitate category rationalization workshop", "R/A", "C", "ECS SA runs the workshop using the legacy category list as input."),
        ("Provide legacy category/item list", "I", "R/A", "Customer ITSM Owner provides the existing catalog structure."),
        ("Draft new category structure", "R/A", "C", "ECS SA drafts; customer reviews for user-centricity."),
        ("Map legacy categories to new structure", "R", "C", "ECS SA leads mapping; customer confirms each mapping decision."),
        ("Assign category owner groups", "I", "R/A", "Customer ITSM Owner assigns; must be existing assignment groups."),
        ("Obtain ITSM Process Owner approval", "I", "R/A", "Customer governance step. Required before Workbook 02 begins."),
        ("Configure category structure in ServiceNow", "R/A", "I", "ECS SA configures after customer approval."),
    ],
    consultant_guide_sections=[
        ("The rationalization workshop", "Start the workshop by projecting the current category list (however messy) and asking: 'If you were a new employee trying to request a laptop, which of these categories would you click first?' This exercise immediately highlights whether the current structure is user-centric. Then group items by user intent rather than IT team. The 6-category structure in this workbook is a starting point — adjust it based on the customer's actual item mix, but hold the line on the 3-level maximum."),
        ("The 6-category ceiling", "Customers often want 12–15 categories because they think more categories = more findable items. The opposite is true. Employee Center search is the primary discovery mechanism for most users. Categories are for browsing users who don't know what to search for — typically 20-30% of catalog users. For those users, 6 clear categories are more navigable than 15 specific ones. Use OOTB search analytics (available post-go-live) to validate this with data."),
        ("The General Requests catch-all", "Always include a General Requests category. Without it, items that don't fit neatly into the agreed structure become blockers to the Sprint 4 build. Items in General Requests should be reviewed quarterly by the ITSM Process Owner — if a category consistently has more than 8 items, it has earned its own category. If it stays below 5 items after 6 months, those items are candidates for retirement or consolidation."),
        ("Multi-catalog vs. single catalog", "The decision to create separate IT and HR catalogs should be made in Sprint 3 alongside Employee Center scoping. If Employee Center is in scope (Sprint 5), a multi-catalog approach with a unified Employee Center homepage is the OOTB best practice. If Employee Center is not in scope, a single catalog with IT and HR sections may be simpler to manage. Confirm with the ECS SA responsible for Employee Center before finalising this workbook."),
    ],
    adoption_rows=[
        ("We need to keep our 40 legacy categories for backward compatibility",
         "Implement the new 6-category structure. Map legacy categories to the new structure and retire the legacy ones after go-live.",
         "40 categories is a proven barrier to self-service adoption. Legacy category names are not user-facing after the new catalog goes live — they exist only in reporting history, which can be preserved through incident/request metadata.",
         "'Your users don't know what category a request belongs to — they know what they need. A user who needs a laptop doesn't look for an IT Hardware Provisioning category. They look for IT Equipment. We're not losing your legacy categories; we're translating them into language your users actually use.'",
         "Never preserve 40 legacy categories in the live catalog. Historical reporting references to legacy categories can be handled with a mapping field or report filter."),
        ("We want categories organized by IT team (Helpdesk, Server Team, Network Team)",
         "Organise categories by user need. IT team routing belongs in the fulfillment workflow (Workbook 04), not the category structure.",
         "Team-based categories require users to know which team handles their request before they can submit it. This defeats the purpose of self-service and increases misdirected requests.",
         "'We can absolutely route requests to the right team in the background — that's what the fulfillment workflow is for. The catalog category is what the user sees; the routing is invisible to them. Let's make the front end user-friendly and the back end team-friendly.'",
         "Only if the customer explicitly operates a tiered-portal model where different user populations submit to different team portals. Rare and requires Employee Center configuration."),
        ("Every project needs its own category",
         "Use the 'Available for' field and item tags to scope project-specific items. Do not create project-specific categories.",
         "Project categories become orphaned after the project ends and accumulate in the catalog as dead weight. Item-level visibility controls handle scoping without creating structural debt.",
         "'A project category becomes a zombie after the project ends — it sits in the catalog forever with no owner. If we tag project items and set an expiry or review date, they're automatically tidied up without any structural change to the catalog. The catalog stays clean; the project team still gets their dedicated items.'",
         "Never. There is no valid exception for project-specific categories in a governed catalog."),
    ],
    snmap_sections=[
        ("Catalog Structure Tables", [
            ("Service Catalog", "sc_catalog", "One record per catalog (IT, HR). Configure in Service Catalog > Catalogs."),
            ("Catalog Category", "sc_category", "One record per category within each catalog. Parent/child for subcategories."),
            ("Catalog Item", "sc_cat_item", "Individual request items. Assigned to a category."),
        ]),
        ("Key Category Fields", [
            ("title", "Category display name", "What the user sees on the catalog homepage."),
            ("parent", "Parent category (for subcategories)", "Leave null for top-level categories."),
            ("manager", "Category manager (sys_user)", "Named individual responsible for category items."),
            ("sc_catalog", "Reference to parent catalog", "Links the category to the IT or HR catalog."),
            ("active", "true/false", "Inactive categories are hidden from users but preserved in history."),
        ]),
        ("Employee Center Integration", [
            ("EC Portal", "Employee Center > Topics", "Categories surface as Topics in Employee Center. Align category names with EC topic names.", ),
            ("Search index", "Service Portal > Search Sources", "OOTB Employee Center indexes sc_cat_item.short_description and description for search.", ),
        ]),
    ],
)

# =============================================================================
# WORKBOOK 2 — Catalog Item Inventory & Triage
# =============================================================================
wb2 = TabContent(
    workbook_title="02 — Catalog Item Inventory & Triage",
    pack_name=PACK_NAME,
    purpose="Creates a complete inventory of all catalog items from the legacy system or current state, and applies a Keep / Simplify / Retire triage decision to each. The triage output defines the Sprint 4 build scope and prevents the catalog from launching with legacy clutter that reduces self-service adoption.",
    who_fills="Customer-side: ITSM Process Owner leads the triage, with input from fulfillment team leads for each category. ECS SA facilitates and applies the OOTB-first lens. Target: complete the triage in one 2-hour workshop plus customer review time.",
    sprint_window="Sprint 3 Week 2 — Sprint 4 Week 1",
    estimated_effort="2–4 hours workshop + 1–2 hours customer review. Scale with item count.",
    related_workbooks=["01 Category Rationalization", "03 Item Template Standards", "04 Fulfillment Workflow Decisions"],
    success_criteria=[
        "Every legacy catalog item has a Keep / Simplify / Retire decision.",
        "Items marked 'Keep' or 'Simplify' are mapped to the new category structure from Workbook 01.",
        "The Sprint 4 build list (Keep + Simplify items) contains no more than 15 items.",
        "Items marked 'Retire' have a recorded rationale for the project record.",
        "Every item in the build list has an identified fulfillment owner group.",
    ],
    process_decisions=[
        ("How many catalog items should we launch with at go-live?",
         "10–15 items for the Sprint 4 MVP. Target the highest-volume requests (top 10 by incident/request volume in the last 12 months) plus any items with regulatory or compliance significance.",
         "Customers who try to launch 50+ catalog items in a single sprint typically deliver half of them with poor variable design and broken fulfillment workflows. 10–15 well-built items drive more self-service adoption than 50 partially-built items."),
        ("What is the triage criterion for 'Retire'?",
         "Retire an item if: (a) it has had fewer than 5 requests in the last 12 months, (b) it duplicates another item, (c) it represents a process that should be an incident rather than a request, or (d) the fulfillment process no longer exists.",
         "Legacy catalogs typically contain 20–30% items that have never been used or are duplicates. Retiring them reduces maintenance overhead and makes the catalog more browsable."),
        ("What does 'Simplify' mean in the triage context?",
         "Simplify means: rebuild the item using the OOTB item template (Workbook 03) with a reduced variable set (5 variables or fewer at MVP), standardised fulfillment workflow, and OOTB approval logic. Do not carry over legacy custom variables or complex logic.",
         "Legacy catalog items often have 15–20 variables that were added ad-hoc over years. Most are never read by the fulfillment team. Simplify forces the question: which variables actually change what we do?"),
        ("How should we handle items that require integrations to third-party systems (e.g., AD, SCCM)?",
         "Flag these as 'Sprint 6 items' in the triage. Build the basic catalog item structure in Sprint 4; add the integration trigger in Sprint 6 after the Integration Accelerator Pack is complete.",
         "Building integration-dependent catalog items before integrations are validated creates rework. The catalog item structure is independent of the integration — build the form first, add the automation later."),
        ("What do we do with catalog items that are really just incident types?",
         "Retire the catalog item. Create an Incident category/subcategory for the equivalent Incident type. Catalog requests are for predictable, fulfillable requests with defined completion criteria. Incident types are for unknown or urgent issues.",
         "Confusion between incidents and requests is the most common catalog design anti-pattern. A 'report a broken printer' catalog item is an incident, not a request. The catalog should contain requests — things a user predictably needs IT to provide."),
    ],
    dependencies=[
        ("Category Rationalization (Workbook 01) approved", "Required", "Customer ITSM Owner", "Sprint 3 Wk 2", "Items cannot be triaged to new categories until the category structure is confirmed."),
        ("Legacy catalog item list (with request volume data if available)", "Required", "Customer ITSM Owner", "Sprint 3 Wk 2", "Volume data is the primary triage criterion for Keep vs Retire decisions."),
        ("Fulfillment team leads available for triage workshop", "Required", "Customer IT Ops", "Sprint 3 Wk 2", "Fulfillment owners know which items are actually used and which are obsolete."),
        ("Request volume report (last 12 months) from legacy system", "Recommended", "Customer ITSM Owner", "Sprint 3 Wk 2", "Objective usage data prevents subjective 'we might need it' arguments for keeping low-value items."),
    ],
    config_sections=[
        ("Triage Decision Fields (one row per legacy catalog item)", [
            ("Legacy Item Name", "[Customer to complete]", "Name as it appears in the current system.", True),
            ("Legacy Category", "[Customer to complete]", "Category in the current system.", True),
            ("Request Volume (last 12 months)", "[Customer to complete]", "Number of requests submitted. Use 0 if unknown.", True),
            ("Triage Decision", "[Keep / Simplify / Retire]", "Keep = build as-is with OOTB template. Simplify = rebuild with reduced variables. Retire = decommission.", True),
            ("New Category (from Workbook 01)", "[Customer to complete if Keep/Simplify]", "Map to the new category structure.", True),
            ("Fulfillment Group", "[Customer to complete if Keep/Simplify]", "The group that fulfills this item.", True),
            ("Retire Rationale (if Retire)", "[Customer to complete]", "Record why this item is being retired for the project record.", True),
            ("Sprint Target", "[Sprint 4 / Sprint 6 / Phase 2]", "Sprint 4 = MVP build. Sprint 6 = integration-dependent items. Phase 2 = deferred.", True),
            ("Notes / Special Requirements", "[Customer to complete]", "Flag items with integration dependencies, approvals, or regulatory requirements.", True),
        ]),
    ],
    raci_rows=[
        ("Provide legacy catalog item list with volume data", "I", "R/A", "Customer ITSM Owner prepares the source list."),
        ("Facilitate triage workshop", "R/A", "C", "ECS SA facilitates; customer makes the Keep/Simplify/Retire decisions."),
        ("Apply OOTB-first lens to Simplify decisions", "R/A", "C", "ECS SA advises on what simplification means for each item; customer approves."),
        ("Confirm fulfillment group for each Keep/Simplify item", "I", "R/A", "Customer fulfillment team leads confirm ownership."),
        ("Document Retire rationale", "R/A", "C", "ECS SA records rationale; customer confirms."),
        ("Approve final Sprint 4 build list", "I", "R/A", "Customer ITSM Process Owner approves before Sprint 4 configuration begins."),
    ],
    consultant_guide_sections=[
        ("Triage workshop facilitation", "The triage workshop works best as a fast-paced decision session. Project the legacy item list, go row by row, and ask three questions for each: (1) How many times was this requested in the last year? (2) If we didn't have this item, what would the user do instead? (3) Who fulfills it and do they still exist? These three questions resolve 80% of triage decisions in under 2 minutes per item. Reserve the full discussion time for borderline items."),
        ("The 15-item MVP discipline", "The hardest conversation is holding the Sprint 4 scope to 15 items when the customer has 80 legacy items. The framing: 'We're not retiring these items permanently — we're deferring them to Sprint 6 or Phase 2. The 15 highest-value items go live in Sprint 4 with clean design and working fulfillment. The next 15 go live in Sprint 6, better because we learned from the first build. Items 30+ go into Phase 2 with full design time.' This makes the 15-item limit feel like a quality decision, not a cut."),
        ("Incidents masquerading as catalog items", "Every legacy catalog typically contains 10–20% items that are really incident types: 'My email isn't working', 'I can't access a shared drive', 'My computer is slow'. These should be retired as catalog items and replaced with Incident categories. The test: if the fulfillment team's job is to investigate what's wrong rather than provide a known deliverable, it's an Incident, not a Request."),
    ],
    adoption_rows=[
        ("We need to launch all 80 legacy catalog items on day one",
         "Launch 10–15 MVP items in Sprint 4. Deliver the next set in Sprint 6. Phase 2 covers the remainder.",
         "80 catalog items built in one sprint produces 80 items with inconsistent variable design, untested fulfillment workflows, and no adoption measurement. 15 well-built items produce measurable self-service adoption that justifies the Phase 2 build.",
         "'We're not cutting items — we're sequencing them. The 15 items we build in Sprint 4 will be built correctly, with tested fulfillment and clean forms. Then we measure adoption and use that data to prioritise the next 15. You'll end up with a better catalog faster than if we try to do everything at once.'",
         "Never launch all legacy items without triage. If the customer has a hard business requirement (e.g., regulatory) for specific items, those move to the Sprint 4 list regardless of volume."),
    ],
    snmap_sections=[
        ("Catalog Item Tables", [
            ("sc_cat_item", "Catalog Item", "Main catalog item table. One record per item."),
            ("item_option_new", "Catalog Item Variable", "Variables (form fields) on a catalog item."),
            ("sc_request", "Service Request", "Parent record created when a user submits a catalog request."),
            ("sc_req_item", "Requested Item (RITM)", "One RITM per catalog item in a request. Fulfillment tracks at RITM level."),
        ]),
        ("Key Item Fields", [
            ("name", "Display name — what the user sees", ""),
            ("category", "Reference to sc_category", "Set from the new category structure (Workbook 01)."),
            ("fulfillment_group", "Default assignment group for fulfillment", ""),
            ("delivery_time", "Expected fulfillment duration (days)", "Used in SLA calculation if SLA is applied to RITM."),
            ("active", "true = visible to users", "Set false for items in triage/review."),
        ]),
    ],
)

# =============================================================================
# WORKBOOK 3 — Item Template Standards
# =============================================================================
wb3 = TabContent(
    workbook_title="03 — Item Template Standards",
    pack_name=PACK_NAME,
    purpose="Defines the OOTB-aligned standards that every catalog item must meet: variable set design, item description format, delivery time field, ordering restrictions, and the 5-variable rule. Every item built in Sprint 4 and Sprint 6 is validated against these standards before it goes live.",
    who_fills="ECS SA owns this workbook — it is the build standard, not a customer data collection tool. The customer ITSM Process Owner should review and sign off the standards before Sprint 4 build begins.",
    sprint_window="Sprint 3 Week 2 — Sprint 4 Week 1 (standards agreed before build begins)",
    estimated_effort="2 hours (ECS SA draft + customer review session)",
    related_workbooks=["02 Catalog Item Inventory", "04 Fulfillment Workflow Decisions", "05 Approval Matrix"],
    success_criteria=[
        "OOTB item template fields are documented and agreed for all Sprint 4 items.",
        "The 5-variable rule is adopted (maximum 5 variables at MVP; exceptions require ITSM Process Owner approval).",
        "Variable naming conventions are agreed.",
        "A quality checklist is in place that ECS SA uses before any item goes live.",
        "Customer ITSM Process Owner has signed off the standards.",
    ],
    process_decisions=[
        ("Should all catalog items use a single shared variable set or item-specific variables?",
         "Use a combination: one OOTB shared variable set for common fields (Requested For, Business Justification, Urgency) applied across all items, plus item-specific variables for unique inputs. Do not duplicate common fields on every item.",
         "Shared variable sets reduce maintenance overhead and ensure consistent data collection across all items. Duplicating the same fields on every item means changing a common field requires editing every item individually."),
        ("What is the maximum number of variables per catalog item at MVP?",
         "5 item-specific variables maximum. The shared variable set covers common fields. If a requested item genuinely requires more than 5 item-specific variables, it is a complex request that may need a workflow redesign or a Record Producer rather than a catalog item.",
         "Every additional variable reduces self-service completion rates. Users abandon forms that feel like filling out a tax return. The OOTB benchmark for high-adoption catalog items is 3–5 total fields visible to the user."),
        ("What variable types should be used by default?",
         "Use OOTB variable types: Single Line Text, Multi-Line Text, Reference (for lookups), Choice (for fixed options), Date, and Yes/No. Avoid custom UI pages or client scripts unless a specific business rule requires them.",
         "OOTB variable types are upgrade-safe and work natively in Employee Center, Mobile, and Virtual Agent. Custom UI pages and complex client scripts break on portal upgrades and block Virtual Agent from reading the variables."),
        ("Should catalog items have mandatory fields?",
         "Yes, but be selective. Only make a field mandatory if an empty response genuinely blocks fulfillment. 'Business Justification' for a password reset is not mandatory — it adds friction without value.",
         "Over-use of mandatory fields is the second most common reason users abandon catalog requests. Before marking a field mandatory, ask: 'If the user leaves this blank, can we still fulfill the request?' If yes, it should not be mandatory."),
        ("What should the catalog item description contain?",
         "Three elements: (1) What the user receives — one sentence, plain language. (2) Who can request it — any restrictions. (3) How long it takes — expected delivery time. No IT jargon, no team names, no process codes.",
         "Item descriptions are the only information a user has to decide if this is the right item. Technical descriptions written for IT teams ('Submits a ticket to the AD team to provision an O365 account') drive misdirected requests and abandonment."),
    ],
    dependencies=[
        ("Category Rationalization (Workbook 01) approved", "Required", "Customer ITSM Owner", "Sprint 3 Wk 2", "Item template standards reference category structure."),
        ("Catalog Item Triage (Workbook 02) complete", "Required", "Customer ITSM Owner", "Sprint 4 Wk 1", "Standards are validated against the agreed Sprint 4 item list."),
        ("Employee Center configuration decisions", "Recommended", "ECS SA", "Sprint 3", "EC portal affects which variable types display correctly on mobile and EC."),
    ],
    config_sections=[
        ("Shared Variable Set — Applied to All Catalog Items", [
            ("Variable: Requested For", "Reference — sys_user", "Who is this request for? Defaults to current user. Delegates allowed.", False),
            ("Variable: Business Justification", "Multi-line text — Optional", "Why is this needed? Not mandatory unless item type requires it.", False),
            ("Variable: Urgency", "Choice: High / Medium / Low — default Medium", "Used to set RITM priority. Map to SLA if SLA is applied.", False),
            ("Shared variable set name", "ECS_Catalog_Common", "Apply this set to every catalog item before adding item-specific variables.", False),
        ]),
        ("Item-Specific Variable Standards", [
            ("Maximum item-specific variables at MVP", "5", "Exceptions require ITSM Process Owner approval and documentation.", False),
            ("Allowed variable types (OOTB only)", "Single Line Text, Multi-Line Text, Reference, Choice, Date, Yes/No, Attachment", "No custom UI pages. No complex client scripts at MVP.", False),
            ("Mandatory field policy", "Mandatory only if empty value prevents fulfillment", "Review each mandatory field: if fulfilment can proceed without it, make it optional.", False),
            ("Variable naming convention", "snake_case, no spaces, prefixed by item code — e.g., eq_serial_number", "Consistent naming enables bulk reporting across catalog items.", False),
        ]),
        ("Catalog Item Description Template", [
            ("Line 1 — What you receive", "[Plain language — what IT delivers]", "Example: 'A laptop pre-configured with your standard software image, delivered to your desk within 5 business days.'", False),
            ("Line 2 — Who can request", "[Eligibility statement or 'All employees']", "Example: 'Available to all permanent employees. Contractors must obtain manager approval first.'", False),
            ("Line 3 — Delivery time", "[Expected fulfillment duration]", "Example: 'Expected delivery: 5 business days for standard models; 10 business days for configure-to-order.'", False),
        ]),
        ("Item Quality Checklist (ECS SA pre-launch validation)", [
            ("Description follows 3-element template", "Yes / No", "Reject if description uses IT jargon or team names.", False),
            ("Variable count ≤ 5 item-specific", "Yes / No", "Reject if >5 item-specific variables without ITSM PO approval.", False),
            ("All variables use OOTB types", "Yes / No", "Reject if custom UI pages or complex client scripts are used.", False),
            ("Shared variable set applied", "Yes / No", "ECS_Catalog_Common must be applied before item-specific set.", False),
            ("Delivery time field populated", "Yes / No", "Reject if delivery_time is blank.", False),
            ("Fulfillment group assigned", "Yes / No", "Reject if fulfillment_group is blank.", False),
            ("Category matches Workbook 01 structure", "Yes / No", "Reject if category is not in the approved structure.", False),
            ("Item tested in non-prod with a test RITM", "Yes / No", "Reject if not tested before promoting to production.", False),
        ]),
    ],
    raci_rows=[
        ("Draft item template standards", "R/A", "I", "ECS SA owns this workbook entirely."),
        ("Review and approve template standards", "I", "R/A", "Customer ITSM Process Owner approves before Sprint 4 build begins."),
        ("Build shared variable set (ECS_Catalog_Common)", "R/A", "I", "ECS SA configures the shared variable set in ServiceNow."),
        ("Apply quality checklist to each item before go-live", "R/A", "I", "ECS SA runs the checklist; no item goes live without passing."),
        ("Approve exceptions to the 5-variable rule", "I", "R/A", "Customer ITSM Process Owner approves exceptions."),
        ("Document variable design decisions for each Sprint 4 item", "R/A", "I", "ECS SA documents in the item build notes."),
    ],
    consultant_guide_sections=[
        ("The 5-variable rule conversation", "Customers frequently push back on the 5-variable rule because their legacy items had 15+ variables. The response: 'Look at the last 50 requests submitted for this item. Which of those 15 fields were actually filled in? Which fields, if left blank, would have changed what the fulfillment team did?' In most cases, only 3–4 variables actually influence fulfillment. The rest are data-collection aspirations that the fulfillment team never reads. Start with 5; add variables in Phase 2 if the data shows they're needed."),
        ("Shared variable set setup", "Configure the ECS_Catalog_Common shared variable set in Sprint 3 before any item build begins. The three common fields (Requested For, Business Justification, Urgency) should be on every catalog item regardless of type. This ensures consistent data for reporting and SLA calculation. The shared variable set also simplifies Employee Center variable display — OOTB EC renders shared variable sets cleanly without additional configuration."),
        ("Record Producers vs. Catalog Items", "If a customer has a catalog item that genuinely requires more than 10 variables to capture useful data (e.g., a complex project intake form), suggest a Record Producer instead of a catalog item. Record Producers create records in any ServiceNow table (not just RITM) and support complex form layouts. They are still catalog-accessible but are designed for complex data capture, not simple request fulfillment. Use sparingly — most catalog requests don't need this."),
    ],
    adoption_rows=[
        ("Our legacy items have 15+ variables and users are used to them",
         "Rebuild items with 5 or fewer item-specific variables plus the shared common set. Move remaining variables to fulfillment notes or a post-submission form if absolutely necessary.",
         "More variables = lower self-service completion rate. Legacy variable sets were designed when IT needed to capture everything upfront because there was no way to contact the requester. ServiceNow RITM conversations allow the fulfillment team to ask follow-up questions — this replaces the need for exhaustive upfront capture.",
         "'Your users have 15 fields to fill in before they can submit. Our data shows that completion rates drop 15-20% for every field added beyond 5. Let's identify the 5 fields that actually change what the fulfillment team does, and let the team ask for the rest if they need it. Users who can submit in 2 minutes are more likely to use the catalog than users who have to fill in a form.'",
         "If a regulatory or audit requirement mandates specific data fields at submission time, they may be added as mandatory variables. Document the regulatory basis. Still aim to keep total variables below 10."),
        ("We want to use custom scripts and UI policies for complex validation",
         "Use OOTB variable conditions and mandatory/optional settings for validation. Reserve custom scripts for genuinely unique business logic that has no OOTB equivalent.",
         "Custom client scripts and UI policies break on ServiceNow upgrades and prevent Virtual Agent from reading variable values for AI-assisted request fulfillment.",
         "'OOTB variable conditions cover 90% of the validation logic I've seen in legacy catalogs. Let me show you what we can do without scripting — you'll be surprised how far OOTB gets us. If there's something genuinely unique after that, we'll scope it specifically rather than using scripting as the default.'",
         "Complex calculation logic (e.g., cost estimation based on variable inputs) may require a client script. Scope explicitly, document, and plan for upgrade testing."),
    ],
    snmap_sections=[
        ("Variable Tables", [
            ("item_option_new", "Catalog Item Variable", "Stores individual variables. References sc_cat_item."),
            ("io_set_item", "Variable Set Item", "Associates a variable set with a catalog item."),
            ("sc_variable_set", "Variable Set", "The shared variable set definition."),
        ]),
        ("Key Variable Fields", [
            ("question_text", "Field label shown to user", "Follow the plain-language naming standard."),
            ("type", "Variable type (1=Single Line, 2=Multi-Line, 3=Choice, etc.)", "Use OOTB types only."),
            ("mandatory", "true/false", "Only true if empty value prevents fulfillment."),
            ("reference_table", "Table for Reference type variables", "e.g., sys_user for Requested For."),
        ]),
        ("Employee Center Variable Display", [
            ("EC variable rendering", "Employee Center renders shared variable sets cleanly by default", "No additional portal widget configuration needed for shared variable sets."),
            ("Mobile variable support", "OOTB variable types render on ServiceNow Mobile without scripting", "Custom UI pages do not render on Mobile. Additional reason to avoid them."),
        ]),
    ],
)

# =============================================================================
# WORKBOOK 4 — Fulfillment Workflow Decisions
# =============================================================================
wb4 = TabContent(
    workbook_title="04 — Fulfillment Workflow Decisions",
    pack_name=PACK_NAME,
    purpose="Defines the fulfillment workflow pattern for each catalog item in the Sprint 4 build list: who fulfills it, how it is routed, what the completion criteria are, and which OOTB workflow model applies. The goal is to use OOTB flow designer catalog workflows without custom logic, routing all items to the correct group through standard assignment rules.",
    who_fills="ECS SA completes the OOTB workflow recommendation; customer fulfillment team leads confirm routing and completion criteria. Complete this workbook for each Sprint 4 item before the item is built in ServiceNow.",
    sprint_window="Sprint 4 Weeks 1–2",
    estimated_effort="1–2 hours (one per-item workflow review session with fulfillment team leads)",
    related_workbooks=["02 Catalog Item Inventory", "03 Item Template Standards", "05 Approval Matrix"],
    success_criteria=[
        "Every Sprint 4 item has a documented fulfillment workflow model (Simple, Approval-then-Fulfill, Multi-stage).",
        "Fulfillment group is confirmed for every item.",
        "Completion criteria are defined for every item (what does 'done' look like?).",
        "Delivery time is confirmed and set on the catalog item.",
        "No item requires a custom Flow Designer subflow for MVP fulfillment.",
    ],
    process_decisions=[
        ("Which OOTB fulfillment workflow model applies to most catalog items?",
         "Simple fulfillment: RITM assigned to fulfillment group, group works the RITM, resolves when complete. Use this for 80%+ of catalog items. Add approval only when a business rule or policy genuinely requires it (see Workbook 05).",
         "Adding approvals to every item adds 1–2 days of fulfillment time and reduces catalog adoption. The OOTB simple fulfillment model is purpose-built for the 80% of requests that don't need an approval step."),
        ("Should we use OOTB Flow Designer catalog workflows or custom Workflow Editor flows?",
         "Use OOTB Flow Designer catalog spokes and actions. Do not use the legacy Workflow Editor for new catalog items.",
         "Flow Designer is the ServiceNow platform direction. Workflow Editor flows are not forward-compatible with Now Assist GenAI features and require additional upgrade maintenance. Any new catalog flow built in the legacy Workflow Editor is technical debt from day one."),
        ("How should we handle multi-team fulfillment (e.g., an item that requires both the server team and the network team)?",
         "Use OOTB catalog task chaining: create sequential or parallel catalog tasks within the RITM, each assigned to a different group. The OOTB Catalog Task (sc_task) table handles multi-team fulfillment without custom flows.",
         "Multi-team fulfillment is a common pattern. OOTB catalog tasks handle this natively. Custom flows that split RITMs into child tickets create reporting complexity and break standard RITM dashboards."),
        ("What are the completion criteria for a catalog item?",
         "Define a specific, observable outcome for each item. 'Laptop delivered and user can log in' is a completion criterion. 'Fulfillment complete' is not. Completion criteria drive RITM closure quality and SLA accuracy.",
         "Vague completion criteria mean RITMs are closed prematurely or left open indefinitely. Clear criteria enable the fulfillment team to close RITMs confidently and enable audit of fulfillment quality."),
        ("How should catalog items with integration dependencies be handled at MVP?",
         "Build the catalog item with a manual fulfillment workflow at MVP. Add the integration trigger (e.g., AD account creation, SCCM software push) as a Flow Designer spoke action in Sprint 6 after the integration is validated.",
         "Building integration-dependent automation before the integration is stable creates brittle workflows. The manual fulfillment MVP approach gets the item live and in use while the integration is being validated in parallel."),
    ],
    dependencies=[
        ("Catalog Item Triage (Workbook 02) — Sprint 4 item list confirmed", "Required", "Customer ITSM Owner", "Sprint 4 Wk 1", "Cannot design fulfillment workflows without the confirmed item list."),
        ("Approval Matrix (Workbook 05) agreed", "Required", "Customer ITSM Owner", "Sprint 4 Wk 1", "Workflow model (simple vs. approval-then-fulfill) depends on approval decisions."),
        ("Fulfillment team leads available for per-item review", "Required", "Customer IT Ops", "Sprint 4 Wk 1", "Fulfillment leads confirm routing and completion criteria."),
        ("Integration Accelerator Pack status (if items have integration dependencies)", "Recommended", "ECS Architect", "Sprint 4 Wk 1", "Integration readiness determines whether automation can be added in Sprint 4 or must be deferred to Sprint 6."),
    ],
    config_sections=[
        ("Fulfillment Workflow Template (one section per Sprint 4 item)", [
            ("Catalog Item Name", "[From Workbook 02 triage list]", "", True),
            ("Fulfillment Model", "[Simple / Approval-then-Fulfill / Multi-stage]", "Simple = RITM → fulfill → close. Approval = approval step before RITM is assigned. Multi-stage = catalog tasks.", True),
            ("Primary Fulfillment Group", "[Customer to complete]", "Must be an existing assignment group.", True),
            ("Secondary Fulfillment Group (if multi-stage)", "[Customer to complete or N/A]", "Required only for multi-stage items with catalog task chaining.", True),
            ("Completion Criteria", "[Customer to complete — specific observable outcome]", "Example: 'Account created and user can authenticate. Confirmed by fulfillment team.'", True),
            ("Delivery Time (business days)", "[Customer to complete]", "Used to set the delivery_time field and SLA calculation.", True),
            ("Integration Dependency?", "[Yes / No]", "If Yes, automation deferred to Sprint 6. Manual fulfillment at MVP.", True),
            ("Flow Designer Spoke / Action (if integration)", "[Sprint 6 scope — placeholder]", "Document the intended integration action for Sprint 6 planning.", True),
        ]),
        ("OOTB Fulfillment Workflow Models", [
            ("Simple Fulfillment", "RITM created → assigned to fulfillment group → worked → closed", "Use for 80%+ of catalog items. No approval, no catalog tasks.", False),
            ("Approval-then-Fulfill", "RITM created → approval step → if approved, assigned to fulfillment group → worked → closed", "Use only when policy or business rule mandates approval.", False),
            ("Multi-stage (Catalog Tasks)", "RITM created → sequential or parallel sc_tasks created → each task assigned to group → all tasks complete → RITM closed", "Use for items requiring multiple teams. OOTB catalog task chaining.", False),
        ]),
    ],
    raci_rows=[
        ("Recommend OOTB fulfillment workflow model per item", "R/A", "C", "ECS SA recommends; customer fulfillment leads confirm."),
        ("Confirm fulfillment group for each item", "I", "R/A", "Customer fulfillment team leads confirm group assignment."),
        ("Define completion criteria for each item", "C", "R/A", "Customer fulfillment teams define what 'done' looks like; ECS SA records."),
        ("Configure Flow Designer workflow per item", "R/A", "I", "ECS SA configures in ServiceNow."),
        ("Test fulfillment workflow with test RITM in non-prod", "R/A", "C", "ECS SA tests; customer fulfillment lead validates the test RITM."),
        ("Document integration deferred items for Sprint 6 planning", "R/A", "I", "ECS SA documents the integration scope for Sprint 6."),
    ],
    consultant_guide_sections=[
        ("The 80/20 workflow principle", "Eighty percent of catalog items should use simple fulfillment. The remaining 20% may have an approval step. The very small minority (complex, multi-team items) use catalog task chaining. If you find yourself designing a complex custom Flow Designer flow for a standard request, stop and ask: 'Is this a catalog item or a process that should be managed as a project?' Complex custom flows are a signal that the request scope is too broad for the catalog."),
        ("Flow Designer vs. Workflow Editor", "Never build new catalog workflows in the Workflow Editor. If the customer insists on migrating their legacy Workflow Editor flows, have the conversation about Now Assist: GenAI features (Now Assist for ITSM) read Flow Designer actions but cannot process legacy WE flows. A catalog built on Workflow Editor flows cannot leverage GenAI fulfillment assistance. This is the most compelling argument for rebuilding in Flow Designer."),
        ("Catalog task chaining for multi-team items", "For items that require sequential steps from multiple teams (e.g., 'New Employee Setup' that requires IT account creation AND workstation provisioning AND badge access), use catalog task chaining rather than custom flows. Configure: one parent RITM, two or three sequential sc_tasks, each assigned to the relevant group. The RITM closes automatically when all tasks are complete. This is OOTB functionality that requires no scripting."),
    ],
    adoption_rows=[
        ("We want to automate everything from day one — manual fulfillment is not acceptable",
         "Build manual fulfillment for Sprint 4 items. Add automation via Flow Designer spokes in Sprint 6 after integrations are validated.",
         "Automation built before integrations are stable creates brittle workflows that fail silently. A manual fulfillment workflow that works reliably is better than an automated workflow that fails 20% of the time.",
         "'Manual fulfillment is the safety net that lets us go live fast and prove the catalog works. We add automation in Sprint 6 — the form is already built, the routing is proven, and we're adding one step to a working process rather than building everything at once. This sequence reduces risk significantly.'",
         "If a specific item has a simple, reliable API integration ready and tested, automation can be added in Sprint 4. Validate integration readiness with the ECS Architect before committing."),
        ("We need to keep our legacy workflow email triggers",
         "Replace email triggers with OOTB Flow Designer actions and ServiceNow notifications. Do not replicate email-driven workflows.",
         "Email-driven workflow triggers are not auditable, not scalable, and are not compatible with Virtual Agent and Now Assist. Flow Designer provides the same trigger mechanism with full auditability and AI compatibility.",
         "'Email triggers work until someone's inbox gets full, someone sets up an out-of-office, or the email server has a hiccup. Flow Designer triggers are instant, auditable, and don't have an inbox. Let me show you how the OOTB notification action in Flow Designer replicates exactly what your email trigger does — reliably.'",
         "Never. Email triggers are not an acceptable fulfillment mechanism for a modern ServiceNow catalog."),
    ],
    snmap_sections=[
        ("Fulfillment Tables", [
            ("sc_req_item (RITM)", "Requested Item", "Primary fulfillment record. One per catalog item in a request."),
            ("sc_task", "Catalog Task", "Child tasks for multi-stage fulfillment. Parent = sc_req_item."),
            ("sysapproval_approver", "Approval Record", "Created by approval flow when approval step is required."),
        ]),
        ("Flow Designer", [
            ("Catalog Trigger", "Flow Designer > Catalog > Service Catalog Item Requested", "OOTB trigger for catalog item submission. Do not use Workflow Editor."),
            ("Catalog Task Action", "Flow Designer > ServiceNow Core > Create Catalog Task", "Creates sc_task records for multi-stage fulfillment."),
            ("Approval Action", "Flow Designer > ServiceNow Core > Request Approval", "OOTB approval step. Use instead of legacy approval engine configuration."),
        ]),
    ],
)

# =============================================================================
# WORKBOOK 5 — Approval Matrix
# =============================================================================
wb5 = TabContent(
    workbook_title="05 — Approval Matrix",
    pack_name=PACK_NAME,
    purpose="Defines which catalog items require approval, who approves them, and what the OOTB approval policy configuration looks like. The default position is no approval — approvals are added only where a specific business policy, cost threshold, or compliance requirement mandates them. This workbook prevents the common pattern of approvals being added to every item 'just in case'.",
    who_fills="Customer-side: ITSM Process Owner and Finance/Compliance lead (if cost threshold approvals are required). ECS SA recommends the OOTB approval policy configuration. Agreed before Workbook 04 workflow design begins.",
    sprint_window="Sprint 4 Week 1 (agreed before workflow build)",
    estimated_effort="1–2 hours (one approval policy workshop)",
    related_workbooks=["02 Catalog Item Inventory", "04 Fulfillment Workflow Decisions", "Foundation Data Pack — Groups"],
    success_criteria=[
        "Every Sprint 4 catalog item has an explicit approval decision: required or not required.",
        "Where approval is required, the approver role (manager, department head, etc.) is defined.",
        "OOTB approval policy is used — no custom approval scripts.",
        "Approval SLA (how long an approver has before escalation) is defined.",
        "The no-approval default is documented and agreed by the ITSM Process Owner.",
    ],
    process_decisions=[
        ("What is the default approval policy for catalog items?",
         "No approval required by default. Approval is added only where a specific business rule or compliance requirement mandates it. Most IT service requests do not require approval — adding approvals universally adds 1–2 days to every fulfillment cycle without commensurate governance value.",
         "Universal approval policies are the most common cause of catalog abandonment. Users who submit a request and wait 3 days for manager approval (who approves 99% of requests) quickly learn to call the helpdesk instead. Targeted approvals on high-cost or compliance-sensitive items provide governance value without penalising routine requests."),
        ("What triggers an approval requirement?",
         "Three triggers: (1) Cost threshold — items above a defined cost threshold require manager approval. (2) Compliance/regulatory — items involving privileged access or sensitive data require security team approval. (3) Policy — items where HR or Finance policy mandates sign-off (e.g., new hire equipment for contractors).",
         "Any trigger beyond these three is likely a process smell: either the item is not well-suited for the catalog, or the approval reflects a trust deficit in the fulfillment team. Address the root cause rather than adding approval overhead."),
        ("Who should be the approver for a standard cost-threshold approval?",
         "Requestor's direct manager (OOTB manager approval field on the user record). Do not build custom approver lookup logic unless the manager field is unreliable.",
         "The OOTB manager approval field is populated from the user record and requires no custom lookup. Custom approver logic (e.g., 'find the department head from a cost centre table') requires maintenance and breaks when org structures change."),
        ("What should the approval SLA be?",
         "24 business hours for standard approvals. After 24 hours, escalate to the approver's manager. After 48 hours, return the request to the requester with a note to resubmit. Do not let requests sit in approval indefinitely.",
         "Unresolved approvals are a leading cause of RITM backlog. An OOTB approval SLA with escalation ensures approvers are reminded and requests don't expire silently."),
        ("Should we use group approval or individual approval?",
         "Individual approval (direct manager) for cost-threshold items. Group approval (security team) for privileged access items. Never use ad-hoc 'any member of the group can approve' for compliance-sensitive items — use designated approvers with individual accountability.",
         "Group approval is appropriate for operational approvals where any authorised team member can review. Compliance-sensitive approvals require individual accountability — you need to know who approved what."),
    ],
    dependencies=[
        ("Catalog Item Triage (Workbook 02) — Sprint 4 item list confirmed", "Required", "Customer ITSM Owner", "Sprint 4 Wk 1", "Approval matrix is built against the confirmed item list."),
        ("Cost threshold policy confirmed by Finance or IT Director", "Required", "Customer Finance / IT Director", "Sprint 4 Wk 1", "Cost thresholds are a business policy decision, not an IT configuration decision."),
        ("Foundation Data Pack — Users (manager field populated)", "Required", "ECS SA", "Sprint 0", "OOTB manager approval requires the manager field to be populated on user records."),
        ("Compliance/regulatory requirements review", "Recommended", "Customer Compliance Lead", "Sprint 4 Wk 1", "Identify items with external compliance requirements (SOX, HIPAA, etc.) that mandate approval."),
    ],
    config_sections=[
        ("Approval Policy Matrix (one row per Sprint 4 item)", [
            ("Catalog Item Name", "[From Workbook 02]", "", True),
            ("Approval Required?", "[Yes / No]", "Default: No. Yes only with documented business rule.", True),
            ("Approval Trigger", "[Cost threshold / Compliance / Policy / N/A]", "Document the specific rule that requires approval.", True),
            ("Approver Role", "[Manager / Security Team / IT Director / N/A]", "Who approves? Use OOTB manager field where possible.", True),
            ("Approval SLA", "[24 hrs / 48 hrs / N/A]", "Time before escalation. Default: 24 business hours.", True),
            ("Escalation Path", "[Approver's manager / ITSM PO / N/A]", "Who is notified if approval SLA breaches?", True),
            ("OOTB Approval Policy Name", "[ECS SA to complete]", "The approval policy record in ServiceNow. ECS SA configures.", False),
        ]),
        ("OOTB Approval Policy Configuration Standards", [
            ("Approval policy type", "Catalog Item Approval Policy (OOTB)", "Configure in Service Catalog > Approval Policies. Do not use custom tables.", False),
            ("Approver source — manager", "OOTB: requested_for.manager", "Reads from the user record. Requires manager field populated.", False),
            ("Approver source — security team", "OOTB: Approval Group = [Security Team assignment group]", "Any member of the group can approve for operational approvals.", False),
            ("Approval SLA configuration", "OOTB: SLA on sysapproval_approver table", "Configure in SLA > Definitions. Apply to approval records, not RITM.", False),
            ("Auto-approval for low-value items", "Not recommended at MVP", "Auto-approval can be configured in Phase 2 based on usage data.", False),
        ]),
    ],
    raci_rows=[
        ("Define approval trigger policy (cost thresholds, compliance items)", "I", "R/A", "Customer Finance / IT Director defines the policy; ECS SA records."),
        ("Recommend OOTB approval configuration for each policy type", "R/A", "C", "ECS SA recommends; customer approves the technical approach."),
        ("Complete approval matrix (one row per Sprint 4 item)", "C", "R/A", "Customer ITSM PO completes with input from Finance and Compliance leads."),
        ("Configure OOTB approval policies in ServiceNow", "R/A", "I", "ECS SA configures after matrix is approved."),
        ("Configure approval SLA and escalation", "R/A", "I", "ECS SA configures OOTB SLA on approval records."),
        ("Test approval workflow for each approval-required item", "R/A", "C", "ECS SA tests; customer approver validates the approval notification."),
    ],
    consultant_guide_sections=[
        ("The no-approval default conversation", "The hardest part of the approval matrix workshop is getting the customer to accept that most items should not require approval. The framing: 'Every approval adds 24-48 hours to the request. If your manager approves 99% of requests without reading them, that 48 hours is pure delay with no governance value. Let's save approvals for the 10% of items where the manager actually needs to make a decision.' Then walk through each item and ask: 'What would happen if we fulfilled this without approval?' Usually, the answer is 'nothing bad' for 80% of items."),
        ("Privilege access approval is non-negotiable", "Do not let the customer skip approvals for privileged access requests (admin account creation, elevated permissions, VPN access for external parties). These are compliance requirements in almost every security framework (SOX, ISO 27001, SOC 2). If the customer pushes back, document the risk and have the IT Director sign off. This is not an ECS preference — it is an audit requirement."),
        ("Manager field dependency", "The OOTB manager approval model only works if the manager field is populated on user records. Before Sprint 4 starts, validate that the Foundation Data Pack loaded manager relationships correctly. Run a query: SELECT COUNT(*) FROM sys_user WHERE manager IS NULL AND active = true. If more than 10% of active users have no manager, this must be resolved before approval-required items are configured."),
    ],
    adoption_rows=[
        ("We want every request to require manager approval",
         "Apply the no-approval default. Add approval only where a specific policy requires it.",
         "Universal approval degrades the value of the catalog. If every request requires approval, users call the helpdesk instead of submitting a request — defeating the purpose of a self-service catalog.",
         "'If a manager approves 95% of requests without question, the approval is friction, not governance. Governance value comes from selective approvals where the manager actually makes a decision. Let's target the 10% of requests where approval changes the outcome — those are the ones that deserve the governance step.'",
         "Never universal approval. If a specific compliance requirement mandates approval on every item in a category, document the requirement and apply it to that category only — not the entire catalog."),
        ("We want custom approval routing based on cost center or department hierarchy",
         "Use OOTB manager approval (reads from user record) for cost-threshold items. Custom routing logic requires maintenance when org structures change.",
         "Custom approval routing breaks every time the org structure changes. The OOTB manager field is maintained by HR systems and stays current. Custom cost centre routing requires a separate maintenance process.",
         "'Custom routing sounds precise until your org restructures and the routing table is three months out of date. The OOTB manager field is maintained by your HR system — it's always current. If a specific item genuinely needs a non-manager approver, we can add that as a named approver on the catalog item without building a complex routing engine.'",
         "If the customer has a complex cost centre approval hierarchy that is formally maintained by Finance, a simple lookup table (not a custom rule engine) is acceptable. Design with Practice Lead."),
    ],
    snmap_sections=[
        ("Approval Tables", [
            ("sysapproval_approver", "Approval Record", "One record per approver per RITM. Created by Flow Designer approval action."),
            ("sc_cat_item_approval_policy", "Catalog Item Approval Policy", "Links an approval policy to a catalog item."),
        ]),
        ("Approval Configuration", [
            ("Approval Policy", "Service Catalog > Approval Policies", "Define OOTB approval policies here. One policy per approval pattern."),
            ("Manager field", "sys_user.manager", "OOTB field. Populate from Foundation Data Pack or HR integration."),
            ("Approval SLA", "SLA > Definitions > apply to sysapproval_approver", "Set to 24 business hours. Configure escalation to approver's manager."),
        ]),
    ],
)

# =============================================================================
# WORKBOOK 6 — Catalog Item Configuration Data
# =============================================================================
wb6 = TabContent(
    workbook_title="06 — Catalog Item Configuration Data",
    pack_name=PACK_NAME,
    purpose="The configuration-ready data sheet for every catalog item in the Sprint 4 build list. This workbook is the single source of truth that ECS SA uses to build each item in ServiceNow — containing all agreed fields, variables, fulfillment routing, and approval settings in one place. Customer fills the data; ECS SA loads it.",
    who_fills="Customer-side: ITSM Process Owner completes the per-item data fields, drawing from decisions made in Workbooks 01-05. ECS SA reviews for completeness before building each item. One section per catalog item.",
    sprint_window="Sprint 4 Weeks 1–2",
    estimated_effort="30-60 minutes per catalog item for the customer to complete",
    related_workbooks=["01 Category Rationalization", "02 Catalog Item Inventory", "03 Item Template Standards", "04 Fulfillment Workflow Decisions", "05 Approval Matrix"],
    success_criteria=[
        "Every Sprint 4 catalog item has a complete configuration data section in this workbook.",
        "All fields are customer-completed and ECS SA-reviewed before the item is built.",
        "Item descriptions follow the 3-element template from Workbook 03.",
        "Variable sets are documented with type, label, mandatory status, and OOTB choices (for Choice variables).",
        "No item is built in ServiceNow until its configuration data section is complete and approved.",
    ],
    process_decisions=[
        ("Who is accountable for completing the configuration data for each item?",
         "The item owner (the fulfillment group lead or process owner for that item) completes the configuration data. ECS SA provides the template and reviews for compliance with the item template standards (Workbook 03).",
         "Configuration data that is written by ECS SA without customer input frequently contains inaccurate descriptions, wrong delivery times, and missing variables. The item owner is the only person who knows what the item actually delivers and what data is needed to fulfill it."),
        ("What happens if a customer submits configuration data that doesn't meet the template standards?",
         "ECS SA returns the section to the item owner with specific feedback. The item is not built until the configuration data meets the standards. This is the quality gate.",
         "Building items from non-compliant configuration data creates rework — the item must be rebuilt after go-live when issues surface. The quality gate at configuration data review is cheaper than fixing items in production."),
        ("Should all Sprint 4 items be built simultaneously or sequentially?",
         "Build sequentially — one or two items at a time. Build, test, and validate each item before starting the next. This surfaces variable design issues and workflow problems early, allowing course correction before the pattern is replicated across all items.",
         "Building all items simultaneously and testing at the end means a design flaw discovered in item 10 has already been replicated in items 1–9. Sequential build and test is slower per item but faster overall."),
    ],
    dependencies=[
        ("Workbooks 01–05 complete and approved", "Required", "Customer ITSM Owner + ECS SA", "Sprint 4 Wk 1", "Configuration data must reference approved decisions from all prior workbooks."),
        ("ServiceNow non-production environment available for build and test", "Required", "ECS Architect", "Sprint 4 Wk 1", "Items are built and tested in non-prod before promotion to production."),
        ("Fulfillment group assignment groups configured in ServiceNow", "Required", "ECS SA", "Sprint 0", "Assignment groups must exist before catalog items can reference them."),
    ],
    config_sections=[
        ("Catalog Item Configuration Template (repeat per item)", [
            ("Item Name (display name)", "[Customer to complete]", "What the user sees on the catalog. Plain language.", True),
            ("Short Description (search index)", "[Customer to complete — 1 sentence]", "Used by Employee Center search. Include keywords users would search.", True),
            ("Full Description (3-element template)", "[Customer to complete — what / who / how long]", "Follow the 3-element template from Workbook 03.", True),
            ("Category (from Workbook 01)", "[Customer to complete]", "Must be from the approved category structure.", True),
            ("Fulfillment Group", "[Customer to complete]", "Must be an existing assignment group.", True),
            ("Delivery Time (business days)", "[Customer to complete]", "Realistic estimate. This appears on the item and drives SLA.", True),
            ("Approval Required? (from Workbook 05)", "[Yes / No]", "", True),
            ("Approver Role (if Yes)", "[Manager / Security Team / Other — specify]", "", True),
            ("Available To", "[All employees / Named group / Department]", "Use 'All employees' by default. Restrict only with documented policy.", True),
        ]),
        ("Item Variables (complete per item — up to 5 item-specific)", [
            ("Variable 1 — Label", "[Customer to complete]", "Plain language field label.", True),
            ("Variable 1 — Type", "[Single Line / Multi-Line / Reference / Choice / Date / Yes/No]", "OOTB types only.", True),
            ("Variable 1 — Mandatory?", "[Yes / No]", "Mandatory only if empty prevents fulfillment.", True),
            ("Variable 1 — Choices (if Choice type)", "[List the choices, comma-separated]", "Keep choices to 5 or fewer options.", True),
            ("Variable 2 — Label", "[Customer to complete or N/A]", "", True),
            ("Variable 2 — Type", "[Type or N/A]", "", True),
            ("Variable 2 — Mandatory?", "[Yes / No / N/A]", "", True),
            ("Variable 2 — Choices (if applicable)", "[Choices or N/A]", "", True),
            ("Variable 3 — Label", "[Customer to complete or N/A]", "", True),
            ("Variable 3 — Type", "[Type or N/A]", "", True),
            ("Variable 3 — Mandatory?", "[Yes / No / N/A]", "", True),
            ("Variable 3 — Choices (if applicable)", "[Choices or N/A]", "", True),
            ("Additional variables 4–5", "[Repeat pattern above or mark N/A]", "", True),
        ]),
        ("Fulfillment Workflow (from Workbook 04)", [
            ("Workflow Model", "[Simple / Approval-then-Fulfill / Multi-stage]", "From Workbook 04 decisions.", True),
            ("Catalog Task 1 — Group (if Multi-stage)", "[Group or N/A]", "", True),
            ("Catalog Task 1 — Description", "[What does this team do? or N/A]", "", True),
            ("Catalog Task 2 — Group (if Multi-stage)", "[Group or N/A]", "", True),
            ("Catalog Task 2 — Description", "[What does this team do? or N/A]", "", True),
            ("Completion Criteria", "[Customer to complete — specific observable outcome]", "What does 'done' look like for this item?", True),
        ]),
        ("ECS SA Build Quality Gate", [
            ("Description follows 3-element template", "[ECS to validate — Yes / No / Returned for revision]", "", False),
            ("Variable count ≤ 5 item-specific", "[ECS to validate]", "", False),
            ("All variables use OOTB types", "[ECS to validate]", "", False),
            ("Shared variable set applied", "[ECS to validate]", "", False),
            ("Built and tested in non-prod", "[ECS to validate]", "", False),
            ("Promoted to production and validated", "[ECS to validate]", "", False),
            ("Build sign-off (ECS SA)", "[ECS SA name and date]", "", False),
            ("Customer acceptance", "[Customer ITSM PO name and date]", "", True),
        ]),
    ],
    raci_rows=[
        ("Complete configuration data for each Sprint 4 item", "I", "R/A", "Customer item owners complete; ECS SA reviews."),
        ("Review configuration data against template standards", "R/A", "C", "ECS SA quality gate. Returns non-compliant sections for revision."),
        ("Build each catalog item in non-production ServiceNow", "R/A", "I", "ECS SA builds; sequential order."),
        ("Test each item with a test submission in non-prod", "R/A", "C", "ECS SA tests; customer fulfillment lead validates the test RITM."),
        ("Promote tested items to production", "R/A", "C", "ECS SA promotes; customer ITSM PO approves promotion."),
        ("Customer acceptance sign-off per item", "I", "R/A", "Customer ITSM PO signs off each item before go-live."),
        ("Communicate catalog launch to users", "I", "R/A", "Customer Communications team handles user communication."),
    ],
    consultant_guide_sections=[
        ("Sequential build discipline", "Build one item, test it, get customer sign-off, then build the next. The temptation to build all 15 items simultaneously and test at the end is strong — resist it. A design flaw in item 1 (e.g., wrong variable type, incorrect fulfillment group) caught after all 15 are built means fixing it 15 times. Caught after item 1, you fix it once and the remaining 14 items are built correctly."),
        ("Description quality review", "The most common quality issue is item descriptions written by IT staff that use IT jargon. Review every description as if you are a business user who has never talked to IT. Common red flags: team names ('AD team', 'ServiceNow admin'), process codes, acronyms without definitions, and passive voice. A good description test: read it to someone outside IT and ask 'do you know what you'd receive if you submitted this request?' If they hesitate, rewrite."),
        ("Non-prod to production promotion checklist", "Before promoting any item to production: (1) test RITM submitted and fulfilled in non-prod, (2) approval flow tested if approval is required, (3) fulfillment group assignment validated, (4) delivery time set, (5) description reviewed and approved, (6) customer ITSM PO sign-off on the item record. Do not batch-promote. Promote one item at a time so any production issue can be traced to a specific item."),
        ("Setting launch expectations", "Catalog adoption does not happen automatically at go-live. Coach the customer to: (1) communicate the new catalog to all employees via email or intranet, (2) brief the helpdesk to direct callers to the catalog, (3) add the Employee Center link to the intranet homepage. The first 30 days of adoption data (search terms, most-submitted items, abandoned submissions) is the best input for the Sprint 6 catalog build prioritisation."),
    ],
    adoption_rows=[
        ("We want to go live with all items at once rather than sequentially",
         "Build and test sequentially. All items go live at the same time, but they are built and validated one by one before the simultaneous launch.",
         "Sequential build does not prevent a simultaneous launch date. It prevents rework by catching design issues early. The launch date can be fixed; the build approach must be sequential.",
         "'We can absolutely launch all 15 items on the same day — that's the plan. What we're controlling is the build sequence: build one, test it, fix any issues, then build the next. By the time we reach item 15, we've validated the approach 14 times. All 15 go live together, all tested.'",
         "No exception. Build sequentially; launch simultaneously."),
    ],
    snmap_sections=[
        ("Build Sequence", [
            ("1. Create catalog item record", "sc_cat_item", "Set name, category, fulfillment group, delivery time, active=false."),
            ("2. Apply shared variable set", "io_set_item", "Link ECS_Catalog_Common to the item."),
            ("3. Add item-specific variables", "item_option_new", "Add in order: first visible to user, last internal."),
            ("4. Configure Flow Designer trigger", "Flow Designer > Catalog Trigger", "Set up fulfillment workflow (simple, approval, or task chain)."),
            ("5. Set approval policy (if required)", "sc_cat_item_approval_policy", "Link to the appropriate approval policy from Workbook 05."),
            ("6. Test in non-prod", "Submit test request", "Validate RITM creation, routing, approval (if applicable), and closure."),
            ("7. Set active=true", "sc_cat_item.active", "Activate only after passing quality checklist."),
            ("8. Promote to production", "Update set or ATF", "Promote using standard change management process."),
        ]),
    ],
)


# =============================================================================
# README — 00_README_Service_Catalog_Pack.docx
# =============================================================================
def build_readme(out_path):
    doc = EcsDocument(
        meta=DocMeta(
            eyebrow="ACCELERATOR PACK",
            title="Service Catalog\nAccelerator Pack",
            subtitle="Category rationalization, item normalization, and fulfillment workflow design for the OOTB-first ServiceNow catalog",
            org="ECS Federal · ServiceNow Practice",
            audience="Customer Project Sponsor, ITSM Process Owner, Fulfillment Team Leads, and the ECS SA responsible for the Sprint 4 catalog build",
            companion_to="ITSM Accelerator Pack · CMDB-CSDM Accelerator Pack · Integration Accelerator Pack",
            doc_id="AP-CAT",
            version="1.0",
            status="Released",
            confidentiality="Shared — for the recipient and their organisation",
            running_header_label="Service Catalog Accelerator Pack · ECS Federal",
        )
    )
    doc.add_cover_page()
    doc.add_page_break()

    doc.h1("What This Pack Is", numbered=False)
    doc.para(
        "This Accelerator Pack contains six workbooks that take the Service Catalog from a "
        "legacy list of items to a user-centric, maintainable catalog built on OOTB ServiceNow "
        "patterns. The scope is deliberately bounded: rationalize the category structure, triage "
        "the item list to a manageable MVP set, standardize how items are built, and establish "
        "clean fulfillment and approval patterns that can be extended without rework."
    )
    doc.para(
        "The OOTB-first principle applies to the Service Catalog with particular force. Legacy "
        "catalogs are frequently the most customised part of a ServiceNow instance — and the "
        "most expensive to maintain. Custom variables, scripted approval logic, bespoke workflow "
        "engines, and team-centric category structures accumulate over years and block every "
        "platform upgrade and AI feature that depends on structured catalog data. This pack "
        "eliminates that debt at the point of the rebuild, not retroactively."
    )
    doc.para(
        "The six workbooks follow a deliberate sequence: agree the structure (Workbook 01), "
        "scope the items (Workbook 02), set the build standards (Workbook 03), design the "
        "fulfillment and approval patterns (Workbooks 04 and 05), then build from a complete "
        "configuration data sheet (Workbook 06). Do not skip or reorder workbooks — each one "
        "is a prerequisite for the next."
    )

    doc.h1("The Six Workbooks", numbered=False)
    doc.table(
        headers=["#", "Workbook", "What It Captures", "Customer Owner", "Sprint Window"],
        rows=[
            ["01", "Category Rationalization", "Simplified 3-level category structure (6 categories max); legacy category mapping; category ownership", "ITSM Process Owner", "Sprint 3 Wk 2 – Sprint 4 Wk 1"],
            ["02", "Catalog Item Inventory & Triage", "Legacy item inventory; Keep/Simplify/Retire decisions; Sprint 4 build list (max 15 items)", "ITSM Process Owner + Fulfillment Leads", "Sprint 3 Wk 2 – Sprint 4 Wk 1"],
            ["03", "Item Template Standards", "5-variable rule; shared variable set; OOTB variable types; item description template; quality checklist", "ECS SA (approved by ITSM PO)", "Sprint 3 Wk 2 – Sprint 4 Wk 1"],
            ["04", "Fulfillment Workflow Decisions", "Workflow model per item (Simple/Approval/Multi-stage); fulfillment routing; completion criteria; integration deferral", "ECS SA + Fulfillment Leads", "Sprint 4 Wks 1–2"],
            ["05", "Approval Matrix", "Approval policy per item; approval triggers (cost/compliance/policy); OOTB approval configuration; approval SLA", "ITSM PO + Finance/Compliance", "Sprint 4 Wk 1"],
            ["06", "Catalog Item Configuration Data", "Complete build data for each Sprint 4 item: description, variables, workflow, approval, quality gate", "Customer Item Owners", "Sprint 4 Wks 1–2"],
        ]
    )
    doc.para(
        "Each workbook contains eight tabs following the ECS standard Accelerator Pack structure: "
        "Instructions (start here); Process Decisions (workshop questions with ECS OOTB "
        "recommendations pre-filled); Dependencies; Configuration Data; R&R (RACI); Consultant "
        "Guide (internal ECS reference); Adoption vs Re-engineering (OOTB defence language); "
        "and ServiceNow Mapping. Customers focus on Instructions, Process Decisions, and "
        "Configuration Data."
    )

    doc.h1("Sprint Alignment", numbered=False)
    doc.para(
        "This pack primarily covers Month 2 of the 18-week engagement. The category and item "
        "triage workbooks (01 and 02) begin in Sprint 3 Week 2, alongside the ITSM core "
        "configuration. The catalog build workbooks (03–06) drive the Sprint 4 catalog "
        "configuration, delivering the first 10–15 high-priority catalog items by the end of "
        "Sprint 4. Remaining items from the triage list and any integration-dependent items "
        "are completed in Sprint 6."
    )
    doc.para(
        "Prerequisites from earlier sprints: the Foundation Data Pack (users, groups, locations) "
        "must be complete before fulfillment groups and approvers can be assigned. The CMDB-CSDM "
        "pack (Business Service taxonomy) should be referenced when naming catalog categories to "
        "ensure the two structures are complementary. The Integration Accelerator Pack status "
        "determines which catalog items can have automated fulfillment in Sprint 4 versus Sprint 6."
    )

    doc.h1("OOTB-First Catalog Principles", numbered=False)
    doc.para(
        "Three rules govern every decision in this pack:"
    )
    doc.para(
        "First, 6 categories and 15 items at MVP. The category ceiling and item count are not "
        "arbitrary constraints — they are the boundary between a catalog that gets adopted and "
        "one that gets abandoned. Every item added to the Sprint 4 build without a triage "
        "decision is an item that may be poorly built, poorly tested, or never used."
    )
    doc.para(
        "Second, 5 variables per item. Variables are where customization debt accumulates fastest. "
        "Every variable beyond 5 that cannot be tied directly to a fulfillment decision is a "
        "field that reduces completion rates without adding value. The shared variable set covers "
        "the common fields. Item-specific variables cover only what genuinely changes what the "
        "fulfillment team does."
    )
    doc.para(
        "Third, no-approval default. Approvals are added only where a specific business policy, "
        "cost threshold, or compliance requirement mandates them. Universal approval policies are "
        "the single most common cause of catalog abandonment in the mid-market segment."
    )

    doc.h1("Completing This Pack Accurately and On Time", numbered=False)
    doc.para(
        "The category structure and item triage decisions (Workbooks 01 and 02) must be approved "
        "by the ITSM Process Owner before Sprint 4 begins. Configuration data (Workbook 06) must "
        "be complete for each item before that item is built. The quality gate in Workbook 06 — "
        "where ECS SA validates each item against the template standards before it goes live — is "
        "non-negotiable. Items that fail the quality gate are returned for revision, not built with "
        "the intention of fixing them after go-live."
    )
    doc.para(
        "Catalog adoption is measured from day one. Self-service submission rate, search abandon "
        "rate, and RITM resolution time are the three KPIs that tell you whether the catalog is "
        "working. Build them into the Sprint 4 go-live plan so the data is available for the "
        "Sprint 6 catalog build prioritisation."
    )

    doc.save(out_path)
    print(f"README saved: {out_path}")


# =============================================================================
# Build all files
# =============================================================================
if __name__ == "__main__":
    OUT = HERE

    print("Building Service Catalog Accelerator Pack...")

    workbooks = [
        (wb1, "01_category_rationalization.xlsx"),
        (wb2, "02_catalog_item_inventory.xlsx"),
        (wb3, "03_item_template_standards.xlsx"),
        (wb4, "04_fulfillment_workflow_decisions.xlsx"),
        (wb5, "05_approval_matrix.xlsx"),
        (wb6, "06_catalog_item_config_data.xlsx"),
    ]

    for content, fname in workbooks:
        path = os.path.join(OUT, fname)
        build_workbook(content, path)
        print(f"  ✓ {fname}")

    build_readme(os.path.join(OUT, "00_README_Service_Catalog_Pack.docx"))

    print("\nService Catalog Accelerator Pack complete.")
    print(f"Output: {OUT}")
