"""
Build AP-06 — SAM Foundations Accelerator Pack
6 xlsx workbooks + 1 README docx, all branded to the canonical ECS standard.
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
TEMPLATES = os.path.join(REPO, "03_Shared", "00_Templates_and_Branding")
sys.path.insert(0, TEMPLATES)

from accelerator_pack_builder import TabContent, build_workbook
from ecs_template import EcsDocument, DocMeta

PACK_NAME = "SAM Foundations Accelerator Pack"

# =============================================================================
# WORKBOOK 1 — Software Publishers
# =============================================================================
wb1 = TabContent(
    workbook_title="01 — Software Publishers",
    pack_name=PACK_NAME,
    purpose="Defines the software publishers ServiceNow SAM will track at MVP and the contract relationship ECS holds with each. Publishers are the root of the SAM hierarchy — every product, model, and entitlement traces back to one.",
    who_fills="Customer-side: SAM Process Owner working with the Procurement and Vendor Management leads. Publishers without an active commercial relationship can be excluded at MVP.",
    sprint_window="End of Sprint 0, Week 1",
    estimated_effort="2-4 hours for a typical mid-market customer (40-60 publishers)",
    related_workbooks=["02 Software Products", "03 Software Models & Versions", "Foundation Data Pack — Vendors"],
    success_criteria=[
        "Every active commercial software publisher is represented with at least one named relationship owner.",
        "Publisher categorization (Tier 1 strategic / Tier 2 managed / Tier 3 tracked-only) is decided and applied.",
        "The pre-loaded baseline of 40 common publishers has been reviewed; in-scope ones marked, out-of-scope removed.",
        "Procurement contact for the top 10 spend publishers is captured.",
    ],
    process_decisions=[
        ("Publisher coverage at MVP — all commercial relationships or top-spend only?",
         "Top 50 by spend + every publisher with a true-up clause in the next 12 months. Tracking 200+ publishers at MVP creates noise without commensurate value.",
         "SAM Foundations is the credibility-building phase. Customers who try to boil the ocean here typically lose 3-4 weeks before realizing they can't keep the data current."),
        ("Publisher tiering — formal tiers or flat list?",
         "Three tiers: Tier 1 strategic (top 10 by spend or risk), Tier 2 managed (next 30), Tier 3 tracked-only (the rest). Tier drives review cadence and reconciliation frequency.",
         "Tier 1 publishers get quarterly reconciliation; Tier 2 semi-annual; Tier 3 annual. Without tiering, every publisher gets the same effort and the program loses focus."),
        ("Publisher record ownership — IT or Procurement?",
         "Procurement owns the publisher record; IT owns the products and installs. Both are named on the publisher record.",
         "Procurement holds the contract relationship; IT consumes the products. Single-owner models break down at the first true-up."),
        ("Treatment of acquisitions and rebrands (e.g., publishers acquired by another publisher)?",
         "Maintain the historical publisher record; add the acquiring publisher as the new parent in the publisher hierarchy. Do not retire the historical record until all related entitlements roll forward.",
         "Premature retirement loses install history and breaks reconciliation. The publisher table in ServiceNow supports parent_publisher for this exact case."),
        ("Open-source and freeware publishers — track or exclude?",
         "Exclude from MVP. Track only publishers with a contractual relationship that creates compliance risk or commercial reporting obligation.",
         "Open-source has no compliance signal at MVP; including it inflates the publisher count and dilutes focus on the publishers that matter."),
        ("Internal-developed software — separate publisher or under 'In-House'?",
         "Single 'In-House' publisher record; products under it identified with the actual development team.",
         "Avoids creating dozens of fake publishers for internal apps while still capturing the products in the same SAM hierarchy."),
        ("Publisher records source of truth — ServiceNow or external?",
         "ServiceNow becomes source of truth at go-live. Pre-loaded from this workbook + Procurement export. Maintained going forward via Vendor Management workflow.",
         "If the publisher table stays read-only against an external system, the SAM Workspace experience degrades and reconciliation requires constant cross-system reference."),
        ("Vendor Management integration — feed or separate?",
         "ServiceNow Vendor Management module is the integration target. Publishers in SAM reference the Vendor record via vendor_id link.",
         "Decouples the publisher entity (SAM concern) from the vendor entity (Procurement concern). Both can evolve without breaking the other."),
    ],
    dependencies=[
        ("Foundation Data Pack — Vendors imported (publisher records link to vendor records)", "In Progress", "ECS", "End of Sprint 0, Wk 1", ""),
        ("Procurement spend report (last 24 months) provided", "Pending", "Customer", "Sprint 0, Wk 1", "CSV or Excel acceptable; ECS will normalize against the SAM publisher list"),
        ("Top 20 publisher Procurement contacts identified", "Pending", "Customer", "Sprint 0, Wk 1", "Name + email per publisher; needed for true-up and renewal coordination"),
        ("Customer-specific publisher list (acquired, renamed, internal) reviewed", "Pending", "Customer", "Sprint 0, Wk 1", "Use the baseline tab in this workbook as starting point"),
        ("SAMP plugin activated in ServiceNow instance", "Pending", "ECS", "Sprint 0, Wk 1", "Required for cmdb_sam_sw_publisher table; cannot proceed without this"),
    ],
    config_sections=[
        ("Publisher Catalog", [
            ("Total publishers at MVP", "50", "40 baseline pre-loaded + 10 customer-specific. Customer reviews & adjusts.", True),
            ("Naming convention", "Official legal name (per Procurement)", "e.g., 'Microsoft Corporation' not 'MSFT' or 'Microsoft'. Aliases captured in alt_names field.", False),
            ("Publisher table", "cmdb_sam_sw_publisher", "OOTB SAMP table", False),
            ("Active flag default", "Y for all in-scope; N for tracked-only / historical-only", "OOTB", False),
        ]),
        ("Tiering & Ownership", [
            ("Tier 1 strategic — count", "10", "Top 10 by spend OR by compliance risk", True),
            ("Tier 2 managed — count", "30", "Next 30 by spend / contract complexity", True),
            ("Tier 3 tracked-only — count", "10", "Remaining in-scope publishers", True),
            ("Procurement owner — named per publisher", "Customer to populate", "Required for Tier 1 and Tier 2; optional for Tier 3", True),
            ("IT owner — named per publisher", "Customer to populate", "Single named individual; group ownership not permitted at Tier 1", True),
        ]),
        ("Vendor Management Integration", [
            ("Link to Vendor Management", "Yes", "publisher.vendor → vmt_vendor", False),
            ("Vendor record must exist before publisher creation", "Yes (enforced via UI policy)", "Prevents orphan publisher records", False),
            ("Contract record link — required at Tier 1/2", "Yes", "contract_id field on publisher; supports renewal alerts", False),
        ]),
        ("Reconciliation Cadence", [
            ("Tier 1 reconciliation frequency", "Quarterly", "Aligned to fiscal quarters", False),
            ("Tier 2 reconciliation frequency", "Semi-annual", "April and October by default", False),
            ("Tier 3 reconciliation frequency", "Annual", "Per fiscal year close", False),
            ("Reconciliation report owner", "SAM Process Owner", "Receives the auto-generated report; routes to Procurement for action", False),
        ]),
    ],
    raci_rows=[
        ("Publisher baseline review (the 40 pre-loaded)", "C", "R", "ECS provides; Customer marks in/out of scope"),
        ("Procurement spend report extraction", "I", "R", "Customer-only activity; ECS receives result"),
        ("Customer-specific publisher list (acquired, internal)", "C", "R", "Customer authoritative; ECS validates against vendor table"),
        ("Tiering decisions (Tier 1/2/3 classification)", "R", "C", "ECS facilitates the tiering workshop; customer makes the calls"),
        ("Procurement and IT owner assignment per publisher", "I", "R", "Customer-only; ECS provides the role definition"),
        ("Vendor record validation (Vendor Mgmt link)", "R", "C", "ECS owns the integration; customer confirms vendor coverage"),
        ("Publisher table configuration in ServiceNow", "R", "I", "ECS executes; customer informed of imports"),
        ("Reconciliation cadence calendar setup", "R", "C", "ECS configures; customer confirms fiscal alignment"),
    ],
    consultant_guide_sections=[
        ("OOTB Software Publishers Foundations",
         "Use cmdb_sam_sw_publisher OOTB. Do not create a custom publisher table — every customer who has tried inherits months of integration debt when they later adopt SAMP fully. The OOTB table supports parent_publisher (for acquisitions), vendor link (for Procurement integration), and alt_names (for renamed publishers). All three are non-negotiable at MVP."),
        ("Implementation Sequence",
         "Day 1-2: import the 40 baseline publishers from this workbook. Day 3-5: customer review session, mark in/out of scope, add customer-specific publishers. Day 6-8: tiering workshop with Procurement and SAM Process Owner together. Day 9-10: owner assignment, vendor record validation, reconciliation calendar config."),
        ("Common Failure Modes",
         "Three patterns we have seen kill SAM Foundations: (1) trying to track every publisher the customer has ever purchased — leads to a publisher table no one trusts; (2) building a custom publisher hierarchy with five tiers when OOTB has three — never extends to SAMP later; (3) skipping the Vendor Management link because 'we will integrate later' — orphans every publisher record and breaks renewal workflow."),
        ("Field Mapping to SAMP",
         "The SAMP module reads publisher data from cmdb_sam_sw_publisher directly. If the customer is on a SAMP-enabled subscription, this table immediately powers the SAMP Workspace home page and the publisher-level true-up forecast. No custom integration required."),
        ("Sprint 1 Handoff",
         "By the end of Sprint 0, publishers are loaded and tiered. Sprint 1 picks up with Software Products (workbook 02), which references publisher_id. If publishers are not locked by end of Sprint 0, Sprint 1 stalls — flag this in the variance scan if it slips."),
    ],
    adoption_rows=[
        ("'We need a custom field for the publisher's account manager.'",
         "Use the Vendor Management contact_account_manager field (linked via publisher.vendor → vmt_vendor → contacts).",
         "Two custom fields on publisher diverge from SAMP's expectations. Vendor Mgmt is the OOTB home for contacts.",
         "'The account manager belongs to the vendor relationship, not the SAM product hierarchy. Let me show you how Vendor Mgmt holds this — it links straight to the publisher.'",
         "Never. This is a process discipline question, not a system limitation."),
        ("'We track each publisher's renewal date on the publisher record.'",
         "Renewal dates live on the contract record (vmt_contract), linked from publisher via contract_id. One publisher → many contracts → many renewal dates.",
         "Storing a single renewal date on the publisher record is the #1 reason renewal alerts miss. Most publishers have 3-5 active contracts with different renewal windows.",
         "'A renewal date on the publisher record only tells you about one contract. Let me show you the contract-level view — it's where the renewal alerts actually fire.'",
         "Never. Customer process should evolve to the contract-level model."),
        ("'Publisher names should match our PO system exactly, including the abbreviations.'",
         "Use legal name in cmdb_sam_sw_publisher.name; capture PO-system abbreviations in alt_names field. Reconciliation tolerates both.",
         "Different systems will always have different naming conventions. The alt_names field is exactly designed for this case.",
         "'The publisher table needs to match SAMP's expectations to work with Now Assist. Let me show you how alt_names handles your PO abbreviations without breaking the SAMP linkage.'",
         "Never. The alt_names approach is OOTB and Now-Assist-compatible."),
        ("'We need separate publisher records for each subsidiary of a large publisher.'",
         "Use the parent_publisher field for hierarchies. Microsoft Corp can have child publishers if the customer has separate contracts; one publisher record with multiple contracts is the default.",
         "Subsidiary proliferation creates dozens of false publishers. The parent_publisher hierarchy was designed for this exact case.",
         "'Let me show you the publisher hierarchy view — it preserves the subsidiary distinction without creating duplicate records that break reconciliation.'",
         "Yes, when subsidiaries have entirely separate contracts AND separate Procurement relationships. Rare but legitimate."),
        ("'Internal apps should each have their own publisher record.'",
         "Single 'In-House' publisher record; products under it identified with the actual development team via dev_team_owner field.",
         "Creating a publisher record per internal app inflates the publisher count and makes Procurement-driven workflows nonsensical for internal apps.",
         "'In-house apps don't have a commercial publisher relationship. The In-House publisher is a single record; the actual ownership lives at the product level.'",
         "Never."),
        ("'We want to exclude all open-source publishers entirely.'",
         "Open-source IS excluded at MVP. Re-introduce in SAM Realization (AP-07) when compliance-tracked open-source becomes in scope.",
         "Open-source has no commercial signal at Foundations stage; tracking it now is process overhead with no business outcome.",
         "'Agreed — open-source is out of Foundations scope. Realization (AP-07) adds it back with the right compliance metadata.'",
         "Already aligned; no customization needed."),
    ],
    snmap_sections=[
        ("Primary table(s)", [
            ("cmdb_sam_sw_publisher", "SAM software publisher master record", "OOTB SAMP plugin table"),
        ]),
        ("Field mapping (customer data → ServiceNow field)", [
            ("Publisher name", "cmdb_sam_sw_publisher.name", "Legal name per Procurement"),
            ("Aliases / abbreviations", "cmdb_sam_sw_publisher.alt_names", "Comma-separated list"),
            ("Tier", "cmdb_sam_sw_publisher.u_tier", "Choice field (1/2/3) — custom but flat, no schema change"),
            ("Procurement owner", "cmdb_sam_sw_publisher.procurement_owner", "Reference to sys_user"),
            ("IT owner", "cmdb_sam_sw_publisher.it_owner", "Reference to sys_user"),
            ("Vendor link", "cmdb_sam_sw_publisher.vendor", "Reference to vmt_vendor"),
            ("Active", "cmdb_sam_sw_publisher.active", "Boolean; default Y for in-scope publishers"),
        ]),
        ("OOTB features leveraged", [
            ("Publisher hierarchy", "parent_publisher field", "Supports acquisitions, subsidiaries"),
            ("Vendor Management link", "vendor reference", "Integrates with vmt_vendor and contracts"),
            ("SAMP Workspace home", "Reads publisher table directly", "No additional config required"),
            ("Now Assist for SAM", "Publisher-level true-up forecast", "Available on SAMP-enabled subscriptions"),
        ]),
        ("Integrations", [
            ("Procurement spend export", "Manual one-time import + monthly delta", "CSV via Import Set"),
            ("Vendor Management module", "Native ServiceNow integration", "Via vendor reference field"),
            ("Active Directory / SSO", "Owner references", "Foundation Data Pack — Users"),
        ]),
    ],
)

# =============================================================================
# WORKBOOK 2 — Software Products Baseline
# =============================================================================
wb2 = TabContent(
    workbook_title="02 — Software Products Baseline",
    pack_name=PACK_NAME,
    purpose="The MVP product catalog: the specific software products ServiceNow will track at Foundations stage. Products are the child of publisher and the parent of model/version. The MVP catalog covers the products that drive 80% of license spend and compliance risk.",
    who_fills="Customer-side: SAM Process Owner working with IT Service Owners and Application Owners.",
    sprint_window="End of Sprint 0, Week 2",
    estimated_effort="4-8 hours including product owner workshops",
    related_workbooks=["01 Software Publishers", "03 Software Models & Versions", "04 Install & Usage Capture"],
    success_criteria=[
        "MVP product list covers ≥80% of license spend and 100% of compliance-tracked products (audit-sensitive).",
        "Every product has a named Application Owner.",
        "Product family hierarchy is decided (suite vs. individual product treatment).",
        "Products not in MVP scope are explicitly excluded with rationale captured.",
    ],
    process_decisions=[
        ("Product coverage — how many products at MVP?",
         "60-100 products covering 80% of spend + 100% of audit-sensitive (Microsoft, Oracle, IBM, SAP, Adobe enterprise).",
         "More than 100 products at MVP becomes a data-currency problem. The 80/20 cut is the right depth for Foundations."),
        ("Product family treatment — track suite or individual products?",
         "Track the licensable unit. Microsoft 365 = one product (the licensable unit); Office, Teams, SharePoint are not separate products at MVP.",
         "Customers who track Office, Teams, and SharePoint as separate products at MVP end up with three products that share one license — reconciliation goes sideways."),
        ("Discontinued / end-of-life products — include?",
         "Yes, with lifecycle state = End of Life. Required for compliance reporting on legacy installs.",
         "Excluding discontinued products creates blind spots for audits. The lifecycle state machine handles this OOTB."),
        ("Product identification — internal name or publisher SKU?",
         "Publisher's official product name as primary; SKU captured in product.sku field for procurement linkage.",
         "Internal nicknames diverge between teams. Publisher names are the canonical SAMP reference."),
        ("Application Owner — required at MVP?",
         "Yes. Every MVP product has a named Application Owner. No exceptions.",
         "Products without an owner become orphaned at first reconciliation; the owner is who Procurement and IT route to."),
        ("License model attribution — Foundations or Realization?",
         "Capture the license model at Foundations (user-based, device-based, capacity-based, named-user, concurrent) but defer entitlement counting to Realization (AP-07).",
         "License model affects install/usage capture design (workbook 04). Without it, install data has no structure to compare against."),
        ("Cloud SaaS products — include at MVP?",
         "Yes. SaaS is in scope at MVP. SaaS-specific tracking (subscription seats, API call quotas) deferred to Realization.",
         "Cloud SaaS is the fastest-growing license category; excluding at MVP creates a blind spot exactly where compliance pressure is increasing."),
    ],
    dependencies=[
        ("Workbook 01 (Publishers) complete and imported", "Pending", "ECS", "Sprint 0, Wk 1", "Product records require publisher_id reference"),
        ("Application owner list (per product) compiled", "Pending", "Customer", "Sprint 0, Wk 2", "Single named individual per product"),
        ("Procurement product master export", "Pending", "Customer", "Sprint 0, Wk 1", "If available; ECS can work from this workbook alone if not"),
        ("Audit history (last 2 audits) reviewed by ECS", "Pending", "ECS", "Sprint 0, Wk 1", "Customer provides; ECS extracts product-level scope"),
    ],
    config_sections=[
        ("Product Catalog", [
            ("Total products at MVP", "75", "Customer to confirm count after baseline review", True),
            ("Product table", "cmdb_sam_sw_product_definition", "OOTB SAMP table", False),
            ("Naming convention", "Publisher's official product name", "e.g., 'Microsoft 365 E5' not 'M365' or 'Office'", False),
            ("Active flag default", "Y for in-scope, N for tracked-only / EOL", "OOTB", False),
        ]),
        ("License Model Attribution", [
            ("User-based products — count", "30", "User CALs, named-user licenses", True),
            ("Device-based products — count", "15", "Device CALs, per-machine licensing", True),
            ("Capacity-based products — count", "8", "Per-core, per-GB, per-transaction", True),
            ("Concurrent products — count", "5", "Floating-user / concurrent licenses", True),
            ("Subscription / SaaS — count", "17", "Cloud SaaS subscriptions", True),
        ]),
        ("Application Ownership", [
            ("Named Application Owner — required", "Yes (UI policy enforces)", "OOTB", False),
            ("Backup owner — required at Tier 1 publisher products", "Yes", "Custom UI policy; needed for compliance continuity", False),
            ("Owner notification — at renewal -90 days", "Email via OOTB notification rules", "Tier 1 only", False),
        ]),
        ("Product Hierarchy", [
            ("Product family / suite parent — when to use", "Microsoft 365 → child products only if licensed separately", "OOTB SAMP supports product_family hierarchy", False),
            ("Bundle / unbundle handling", "Track at licensable unit; bundles tagged via product.bundle_components", "OOTB", False),
        ]),
    ],
    raci_rows=[
        ("Product baseline review and approval", "C", "R", "ECS provides starting list; Customer approves"),
        ("Application Owner assignment", "I", "R", "Customer-only; ECS validates completeness"),
        ("License model attribution per product", "R", "C", "ECS classifies; Customer confirms"),
        ("Audit-sensitive product flagging", "R", "C", "ECS extracts from audit history; Customer confirms scope"),
        ("Cloud SaaS product inventory", "C", "R", "Customer-driven; ECS provides SaaS-specific guidance"),
        ("Product table configuration in ServiceNow", "R", "I", "ECS executes; Customer informed"),
        ("Product → Publisher linkage validation", "R", "C", "ECS runs validation script; Customer reviews flags"),
        ("Product naming reconciliation (PO ↔ SAMP)", "R", "C", "ECS produces variance report; Customer adjudicates"),
    ],
    consultant_guide_sections=[
        ("OOTB Software Products Foundations",
         "Use cmdb_sam_sw_product_definition OOTB. The MVP catalog targets 60-100 products — anything more becomes a currency problem within 90 days. Every product references a publisher (workbook 01) and has a named Application Owner. License model (user-based, device-based, capacity-based, concurrent, subscription) is captured at MVP; entitlement counts are deferred to Realization."),
        ("Why 80% of spend, not 100% coverage",
         "Customers who try to inventory every product end up with 400+ records, only the top 60-80 of which are actually maintained. The 80/20 cut puts effort where compliance and renewal exposure actually concentrate. Tail products go into Realization or into the next year's expansion."),
        ("License Model Capture",
         "License model is a Foundations decision because it drives the install/usage capture design in workbook 04. Without it, install data has no structure. We do not count entitlements at Foundations — that's Realization (AP-07). We just classify each product into one of the five license models."),
        ("Application Owner Discipline",
         "Application Owner is the single most important field on the product record. No owner = no reconciliation. The owner is the person who answers 'do we still use this?' when the question comes up at true-up. Enforce via UI policy at MVP."),
        ("Sprint 1 Handoff",
         "By the end of Sprint 0 Wk 2, the product catalog is locked. Sprint 1 picks up with install/usage capture (workbook 04). If the product list is not locked, install data will land against unknown products and the reconciliation pipeline breaks immediately."),
    ],
    adoption_rows=[
        ("'We need to track every Microsoft product separately — Word, Excel, PowerPoint, Teams.'",
         "Track at licensable unit. Microsoft 365 E5 is one product; the apps within are not separately licensable.",
         "Splitting into 8 products creates 8 reconciliation problems where there is 1 license. SAMP's licensable-unit model is the OOTB-defensible answer.",
         "'You buy Microsoft 365 as a single subscription — that's the licensable unit. Let me show you how the SAMP workspace surfaces app-level usage under the single product record.'",
         "Never at Foundations. App-level usage rolls up under the licensable unit in Realization."),
        ("'Cloud SaaS shouldn't be in SAM — it's an app management problem.'",
         "Cloud SaaS IS in SAM at Foundations. The license compliance and renewal mechanics are identical to on-premise.",
         "Excluding SaaS from SAM is the most common 2024 SAM mistake. Renewal pressure and compliance audits don't distinguish.",
         "'SaaS is the fastest-growing license category for most enterprises. Excluding it from SAM at Foundations creates a blind spot exactly where pressure is rising.'",
         "Never. SaaS is in scope."),
        ("'Application Owner field is too restrictive — we want it optional.'",
         "Required at MVP. Enforced via UI policy. Backup owner required at Tier 1.",
         "Products without owners become orphaned at first reconciliation; we have seen this exact failure mode at three previous engagements.",
         "'No owner = no reconciliation. Procurement and IT route the renewal conversation to the named owner. Without that name, the conversation has no destination.'",
         "Never."),
        ("'We track 200+ products today — we need to keep all of them in SAM.'",
         "Limit MVP to ~75 products covering 80% of spend + 100% of audit-sensitive. Tail products go into Realization expansion.",
         "Tracking 200+ products at Foundations becomes a data-currency problem within 90 days. The 80/20 cut is what makes Foundations actually deliverable.",
         "'Let me show you the 80/20 view of your spend. The bottom 130 products are 15% of spend; tracking them all at MVP means none of them get maintained.'",
         "Never at Foundations. Tail products expand in Realization."),
        ("'Product names should match our internal naming conventions, not the publisher's.'",
         "Publisher name as primary; internal name captured in product.alias.",
         "Internal names diverge between teams; SAMP and Now Assist need the canonical publisher reference for workspace-level features to work.",
         "'Let me show you how alias preserves your internal naming for searches and reports while keeping the SAMP linkage intact.'",
         "Never. Alias is the OOTB pattern for this case."),
        ("'EOL products shouldn't be tracked — they're going away.'",
         "Track with lifecycle state = End of Life. Required for compliance reporting and to surface legacy installs needing decommissioning.",
         "EOL products often have the highest compliance risk (vendor enforcement increases as customers migrate off). Removing them creates exactly the blind spot vendors exploit.",
         "'End-of-life products are where most audit findings come from — vendors prosecute legacy installs hardest. Let me show you the lifecycle-state-EOL view that keeps them tracked without confusing them with active products.'",
         "Never."),
    ],
    snmap_sections=[
        ("Primary table(s)", [
            ("cmdb_sam_sw_product_definition", "Master product definition record", "OOTB SAMP plugin table"),
            ("cmdb_sam_sw_product_family", "Product family / hierarchy", "OOTB; used for suite parent relationships"),
        ]),
        ("Field mapping", [
            ("Product name", "cmdb_sam_sw_product_definition.name", "Publisher's official product name"),
            ("Publisher", "cmdb_sam_sw_product_definition.publisher", "Reference to cmdb_sam_sw_publisher"),
            ("License model", "cmdb_sam_sw_product_definition.license_model", "Choice: user, device, capacity, concurrent, subscription"),
            ("Application Owner", "cmdb_sam_sw_product_definition.application_owner", "Reference to sys_user"),
            ("Lifecycle state", "cmdb_sam_sw_product_definition.lifecycle_state", "From workbook 05"),
            ("SKU / part number", "cmdb_sam_sw_product_definition.sku", "Procurement linkage"),
            ("Alias / internal name", "cmdb_sam_sw_product_definition.alias", "Customer-specific naming"),
        ]),
        ("OOTB features leveraged", [
            ("Product family hierarchy", "product_family reference", "Suites and bundles"),
            ("License model choice list", "OOTB choice field", "Drives Realization entitlement design"),
            ("SAMP Workspace product page", "Reads product table directly", "Native integration"),
        ]),
        ("Integrations", [
            ("Procurement product master", "Manual import + monthly delta", "CSV via Import Set"),
            ("Application Portfolio Management (if licensed)", "Native ServiceNow integration", "Bidirectional link to cmdb_ci_appl"),
        ]),
    ],
)

# =============================================================================
# WORKBOOK 3 — Software Models & Versions
# =============================================================================
wb3 = TabContent(
    workbook_title="03 — Software Models & Versions",
    pack_name=PACK_NAME,
    purpose="The specific versions of each product the customer has deployed or is licensed for. Models/versions are the child of product and the parent of install/usage. At MVP we capture the licensed-and-deployed versions, not every version that has ever existed.",
    who_fills="Customer-side: IT Operations and Application Owners. Discovery / SCCM / Intune feeds can populate much of this automatically once mapping is established.",
    sprint_window="End of Sprint 0, Week 2 (data prep) → Sprint 1 Week 1 (validation)",
    estimated_effort="6-10 hours including discovery validation",
    related_workbooks=["02 Software Products", "04 Install & Usage Capture", "Foundation Data Pack — Locations"],
    success_criteria=[
        "Every MVP product has at least one version record.",
        "Unauthorized / unlicensed versions are surfaced for action (not silently included).",
        "Version-to-product mapping rules are documented for discovery normalization.",
        "Major version vs. minor/patch tracking depth is decided.",
    ],
    process_decisions=[
        ("Version depth — major-only or major.minor.patch?",
         "Major version at MVP (e.g., 'Windows 11', not 'Windows 11 22H2 19045.2965'). Minor versions tracked only for products with version-specific licensing (Oracle DB, SQL Server).",
         "Tracking every patch version explodes the model table without adding compliance signal for most products. Major version is the licensable granularity."),
        ("Version normalization — strict or fuzzy match?",
         "Strict for top 20 products (Microsoft, Oracle, SAP, IBM); fuzzy match for the rest with quarterly cleanup.",
         "Strict matching catches license violations but rejects valid installs that don't conform. Fuzzy matching trades precision for completeness; right answer depends on product."),
        ("Unauthorized version handling — surface or suppress?",
         "Surface. Unauthorized versions appear in a separate 'Unmapped' bucket; never silently mapped to authorized versions.",
         "Silent mapping hides license violations. The Unmapped bucket forces conscious decisions about each unauthorized install."),
        ("Discovery source priority — SCCM, Intune, or SN Discovery?",
         "SCCM primary for Windows workstations and servers; Intune primary for mobile and Mac; SN Discovery for Linux/Unix. Customer-specific priorities adjusted as needed.",
         "Single-source discovery misses entire device classes. Tiered priority by device type is the OOTB-defensible approach."),
        ("Beta / preview versions — track?",
         "No. Beta/preview installs filtered out at the discovery normalization layer.",
         "Beta installs are not licensable and inflate the model count. Filtering at normalization keeps the model table clean."),
        ("Custom-built versions of commercial products — how?",
         "Tag with model.is_modified = true; keep linked to the upstream product/version.",
         "Most commercial products tolerate light customization without changing the licensing posture. The is_modified flag preserves the linkage while flagging the divergence."),
        ("End-of-support versions — flag for action?",
         "Yes. Versions past vendor support date appear in a quarterly EOS report routed to the Application Owner.",
         "EOS versions are the highest-risk source of audit findings and security exposure. Quarterly EOS reporting is OOTB."),
    ],
    dependencies=[
        ("Workbook 02 (Products) complete and imported", "Pending", "ECS", "Sprint 0, Wk 2", "Model records require product_id reference"),
        ("SCCM / Intune / SN Discovery feeds operational", "In Progress", "ECS", "Sprint 0, Wk 1", "Required for automated version capture"),
        ("Discovery normalization rules drafted", "Pending", "ECS", "Sprint 0, Wk 2", "ECS provides starting rules; customer review"),
        ("Vendor support lifecycle data sourced", "Pending", "ECS", "Sprint 0, Wk 2", "From vendor websites or licensed source like Flexera / Snow"),
    ],
    config_sections=[
        ("Model Catalog", [
            ("Total model records at MVP (est.)", "300", "75 products × ~4 versions each on average", True),
            ("Model table", "cmdb_sam_sw_product_model", "OOTB SAMP table", False),
            ("Version granularity (default)", "Major version only", "OOTB choice; per-product overrides allowed", False),
            ("Active flag default", "Y for currently deployed versions; N for retired/EOS", "OOTB", False),
        ]),
        ("Discovery Source Priority", [
            ("SCCM coverage — workstations", "100% Windows", "Primary", False),
            ("SCCM coverage — Windows servers", "100%", "Primary", False),
            ("Intune coverage — Mac and mobile", "100%", "Primary for these device classes", False),
            ("SN Discovery — Linux/Unix", "TBD by customer environment", "Required for non-Windows server coverage", True),
            ("Manual entry — appliances and embedded", "Annual refresh", "For non-discoverable devices", False),
        ]),
        ("Normalization Rules", [
            ("Strict-match products (no fuzzy)", "Top 20 by audit risk", "Microsoft, Oracle, SAP, IBM, Adobe Enterprise", False),
            ("Fuzzy-match threshold", "85% string similarity + publisher match", "OOTB SAMP setting", False),
            ("Unmapped bucket size budget", "≤5% of total installs", "Above 5% triggers a normalization review", False),
            ("Beta / preview filter", "Active (regex pattern)", "Excludes beta, preview, RC, CTP installs", False),
        ]),
        ("Lifecycle / Support Flags", [
            ("End-of-support reporting cadence", "Quarterly", "Routed to Application Owner", False),
            ("Mainstream support end source", "Vendor data feed (where available)", "Manual for niche products", False),
            ("Action on EOS finding", "Remediation plan due in 30 days", "Tracked in SAM Workspace", False),
        ]),
    ],
    raci_rows=[
        ("Discovery normalization rules", "R", "C", "ECS authors; customer reviews exceptions"),
        ("Top 20 strict-match product list", "R", "C", "ECS proposes; customer confirms"),
        ("SCCM / Intune integration validation", "R", "C", "ECS executes; customer validates coverage"),
        ("Unmapped bucket triage", "R", "C", "ECS produces; customer adjudicates"),
        ("Vendor support lifecycle data sourcing", "R", "I", "ECS sources; customer informed"),
        ("Model record creation in ServiceNow", "R", "I", "ECS automated via discovery; customer informed"),
        ("Quarterly EOS review", "C", "R", "Customer-led after Foundations; ECS supports first cycle"),
        ("Custom-built / modified version tagging", "C", "R", "Customer identifies; ECS configures"),
    ],
    consultant_guide_sections=[
        ("OOTB Software Models Foundations",
         "Use cmdb_sam_sw_product_model OOTB. The model table captures versions of each product. At Foundations we go to major-version granularity for most products and major.minor for products with version-specific licensing (Oracle DB, SQL Server, IBM DB2). Going deeper inflates the table without compliance benefit."),
        ("Discovery is the leverage point",
         "The model table should be 90% populated from discovery automatically. Manual model creation at MVP is a process failure waiting to happen. Spend Sprint 0 Week 1 getting SCCM/Intune/SN Discovery feeds operational; spend Week 2 on the normalization rules. The actual model records appear in the table once the feeds flow."),
        ("The Unmapped Bucket",
         "Discovery will land 5-15% of installs as 'unmapped' at first run. This is normal. The Unmapped Bucket is the queue for normalization tuning. Target ≤5% unmapped within 30 days of go-live. Above 5% indicates a normalization gap that needs cleanup before reconciliation runs."),
        ("EOS Reporting",
         "End-of-Support version reporting is one of the highest-leverage SAM outputs. Quarterly EOS reports surface the products customers should be migrating off; they convert SAM from a compliance burden into a security and modernization driver. Make sure the EOS report is configured before go-live."),
        ("Sprint 1 Handoff",
         "By end of Sprint 0, discovery feeds operational and normalization rules drafted. Sprint 1 picks up with the first full discovery sweep and the unmapped bucket triage. Workbook 04 (Install & Usage Capture) builds on the model table established here."),
    ],
    adoption_rows=[
        ("'We want every patch version tracked, not just major versions.'",
         "Major version at MVP; minor for products with version-specific licensing only.",
         "Patch-level granularity creates a 10× larger model table without compliance signal for most products. Limited value, high maintenance cost.",
         "'Let me show you the version-specific licensing list — these get minor-version tracking. Everything else, the major version is what licensing actually cares about.'",
         "Yes for specific products if Oracle DB / SQL Server / IBM DB2 / similar require minor-level tracking. Configure at the product level, not globally."),
        ("'Unmapped installs should auto-suppress — they clutter the view.'",
         "Surface them in a dedicated bucket. Never silently suppress.",
         "Silent suppression hides license violations and unauthorized installs. The Unmapped bucket is the discipline that prevents that.",
         "'The Unmapped bucket is where audit findings come from. Hiding it isn't reducing risk — it's deferring it to the auditor.'",
         "Never."),
        ("'Beta versions should be tracked too — we have a lot of preview deployments.'",
         "Beta/preview filtered at normalization. Tracked separately if customer truly needs beta visibility.",
         "Beta installs are not licensable and inflate the model count. If beta visibility is genuinely needed, a separate tag handles it without polluting the model table.",
         "'Beta isn't licensable, so it doesn't belong in the SAM model table. If you need beta visibility, let me show you the discovery-tag approach that keeps it separate.'",
         "Yes when customer has a structured beta program with compliance implications; tag in discovery, not in model table."),
        ("'Custom-modified versions should be entirely new model records.'",
         "Tag is_modified = true on the existing model. Keep the upstream linkage.",
         "Detaching from the upstream model breaks vendor support lookups and EOS reporting; the is_modified flag preserves both.",
         "'The is_modified flag preserves your license entitlement linkage to the upstream version. Creating a separate model orphans the modification from the license terms.'",
         "Never at Foundations."),
        ("'SCCM doesn't catch our DevOps tools — we need manual entries for those.'",
         "Add SN Discovery for the Linux/cloud surface where DevOps tools run; manual entries only as last resort.",
         "Manual entries become stale within a quarter. SN Discovery covers the gap SCCM leaves on cloud/Linux.",
         "'Let me show you what SN Discovery picks up on your DevOps surface. Manual entry is the fallback, not the default.'",
         "Yes for genuinely non-discoverable systems (appliances, embedded devices). Manual entries require annual refresh process."),
        ("'EOS reporting is a security team thing — keep it out of SAM.'",
         "EOS reporting lives in SAM. Quarterly route to Application Owner; security team copied.",
         "SAM owns the version inventory; that inventory is exactly where EOS is detected. Splitting the report creates duplicate effort with version mismatches.",
         "'SAM is where the version data lives, so EOS detection has to start here. Security gets the report; they don't need to maintain a parallel inventory.'",
         "Never."),
    ],
    snmap_sections=[
        ("Primary table(s)", [
            ("cmdb_sam_sw_product_model", "Specific version of a product", "OOTB SAMP plugin table"),
            ("cmdb_sam_sw_discovery_map", "Discovery → product/version mapping rules", "OOTB SAMP normalization layer"),
        ]),
        ("Field mapping", [
            ("Version", "cmdb_sam_sw_product_model.version", "Major version string"),
            ("Product reference", "cmdb_sam_sw_product_model.product", "Reference to cmdb_sam_sw_product_definition"),
            ("Edition", "cmdb_sam_sw_product_model.edition", "Standard / Pro / Enterprise / etc."),
            ("Release date", "cmdb_sam_sw_product_model.release_date", "From vendor data"),
            ("EOS date", "cmdb_sam_sw_product_model.end_of_support", "Drives quarterly EOS report"),
            ("Is modified", "cmdb_sam_sw_product_model.is_modified", "Boolean"),
        ]),
        ("OOTB features leveraged", [
            ("Discovery normalization engine", "cmdb_sam_sw_discovery_map", "Rules-based discovery → model"),
            ("EOS reporting", "Scheduled report on end_of_support", "Quarterly OOTB"),
            ("SAMP Workspace version drill-down", "Reads model table", "Native"),
        ]),
        ("Integrations", [
            ("SCCM", "Native ServiceNow integration", "Primary for Windows"),
            ("Microsoft Intune", "Native ServiceNow integration", "Primary for Mac/mobile"),
            ("ServiceNow Discovery", "Native", "Primary for Linux/Unix/cloud"),
            ("Vendor support lifecycle feed (Flexera / Snow / vendor sites)", "Manual + scheduled refresh", "EOS data source"),
        ]),
    ],
)

# =============================================================================
# WORKBOOK 4 — Install & Usage Capture
# =============================================================================
wb4 = TabContent(
    workbook_title="04 — Install & Usage Capture",
    pack_name=PACK_NAME,
    purpose="How ServiceNow captures every software install and (where licensed) usage signal. Install data is the basis for reconciliation against entitlement. Without reliable install capture, SAM is decorative.",
    who_fills="Customer-side: IT Operations, Endpoint Management, and Application Owners. ECS configures the integration plumbing.",
    sprint_window="Sprint 0 Wk 2 (integration setup) → Sprint 1 Wk 1 (first full capture)",
    estimated_effort="8-16 hours including discovery validation and reconciliation testing",
    related_workbooks=["02 Software Products", "03 Software Models & Versions", "Integration Pack — SCCM/Intune"],
    success_criteria=[
        "Discovery sources cover ≥95% of in-scope devices (workstations + servers).",
        "Install records flow to cmdb_sam_sw_install with publisher/product/model resolution.",
        "Usage capture is operational for the top 10 license-constrained products.",
        "First reconciliation run completed with <5% unmapped variance.",
    ],
    process_decisions=[
        ("Install capture sources — which feeds at MVP?",
         "SCCM (Windows), Intune (Mac/mobile), SN Discovery (Linux/Unix). Manual entries only for non-discoverable.",
         "Three-source coverage handles 95%+ of typical enterprise environments. Manual entries become stale fast."),
        ("Usage capture — measured or inferred?",
         "Measured for the top 10 license-constrained products (Microsoft Office launch tracking, Adobe license server, Oracle DB sessions). Inferred (last-login, last-active) for the rest.",
         "Measured usage requires per-product instrumentation; inferred usage is good enough for 80% of license reconciliation purposes."),
        ("Inactive install threshold — what defines unused?",
         "90 days without usage signal = inactive. 180 days = candidate for reclamation.",
         "Industry-standard thresholds. Aggressive (30/90) creates user friction; loose (180/365) leaves licenses on the shelf."),
        ("Reclamation workflow — automated or human-gated?",
         "Human-gated at MVP. Inactive licenses surface in a reclamation queue; the Application Owner approves reclamation.",
         "Automated reclamation at MVP creates user backlash. Human gate at Foundations; selective automation in Realization."),
        ("Server install handling — track entitlements differently?",
         "Server installs capture the host CI; entitlement calculation deferred to Realization (AP-07).",
         "Server licensing (Oracle DB processor-based, SQL Server core-based) is complex enough to warrant its own workbook in Realization."),
        ("VDI / virtual desktop installs — count once or per session?",
         "Count once per persistent VDI image; per-session for non-persistent.",
         "VDI licensing depends on persistence; this is the OOTB-defensible default."),
        ("Cloud SaaS install capture — API or SSO logs?",
         "SSO logs (Okta, Entra) for SaaS coverage at MVP. Vendor API integration deferred to Realization.",
         "SSO logs are universally available; vendor APIs require per-publisher integration work."),
        ("Mobile / BYOD install tracking — in scope?",
         "Yes for managed mobile (via Intune). BYOD out of scope at Foundations — privacy and discovery constraints.",
         "BYOD raises HR/privacy issues that Foundations is not the right stage to resolve."),
    ],
    dependencies=[
        ("SCCM integration operational", "In Progress", "ECS", "Sprint 0, Wk 1", "From Integration Accelerator Pack 03"),
        ("Intune integration operational", "In Progress", "ECS", "Sprint 0, Wk 1", "From Integration Accelerator Pack 04"),
        ("SN Discovery configured for Linux/Unix", "Pending", "ECS", "Sprint 0, Wk 2", "Mid-server, credentials"),
        ("Workbook 03 (Models) discovery normalization rules", "Pending", "ECS", "Sprint 0, Wk 2", "Prerequisite for install resolution"),
        ("SSO logs accessible (for SaaS coverage)", "Pending", "Customer", "Sprint 0, Wk 2", "Read-only access to Okta or Entra audit logs"),
        ("Endpoint count baseline established", "Pending", "Customer", "Sprint 0, Wk 1", "From CMDB or asset inventory; defines 95% coverage target"),
    ],
    config_sections=[
        ("Install Capture Sources", [
            ("SCCM coverage target", "100% Windows workstations + servers", "Primary source", False),
            ("Intune coverage target", "100% Mac + managed mobile", "Primary for these device classes", False),
            ("SN Discovery coverage target", "100% Linux/Unix + cloud workloads", "Required for non-Windows server coverage", False),
            ("Manual entry budget", "≤2% of total installs", "Annual refresh only", True),
            ("Coverage gap threshold (alert if missed)", "5% of in-scope devices", "Triggers integration health alert", False),
        ]),
        ("Usage Capture", [
            ("Measured usage — top 10 products", "Per-product instrumentation", "Microsoft Office telemetry, Adobe license server, Oracle DB sessions, etc.", False),
            ("Inferred usage — last-login / last-active", "All other products", "From OS / SSO / discovery probes", False),
            ("Inactive threshold (warn)", "90 days no usage signal", "OOTB SAMP default", False),
            ("Inactive threshold (reclamation candidate)", "180 days no usage signal", "OOTB SAMP default", False),
            ("Reclamation workflow", "Human-gated via Application Owner", "OOTB SAMP workflow", False),
        ]),
        ("Reconciliation", [
            ("First reconciliation run target date", "Sprint 1, Wk 1", "Required for Sprint 1 demo", False),
            ("Unmapped variance budget (first run)", "≤10%", "Tightens to ≤5% by Sprint 2", False),
            ("Reconciliation cadence post-go-live", "Monthly automated; quarterly review with Procurement", "OOTB scheduled report", False),
        ]),
        ("Cloud SaaS Capture", [
            ("SaaS coverage source at MVP", "SSO logs (Okta or Entra)", "Login frequency = usage signal", False),
            ("API integration for top 5 SaaS products", "Deferred to Realization (AP-07)", "Salesforce, Workday, ServiceNow self, etc.", False),
        ]),
        ("VDI / Virtual", [
            ("Persistent VDI handling", "Count once per image", "Per-image entitlement tracking", False),
            ("Non-persistent VDI handling", "Per-session", "Concurrent licensing model", False),
        ]),
    ],
    raci_rows=[
        ("SCCM / Intune integration setup", "R", "C", "ECS executes; customer provides access"),
        ("SN Discovery configuration for Linux/Unix", "R", "C", "ECS executes; customer provides credentials"),
        ("Discovery normalization rule tuning", "R", "C", "ECS authors; customer reviews exceptions"),
        ("Usage capture instrumentation (top 10)", "R", "C", "ECS configures; customer confirms per-product approach"),
        ("Inactive / reclamation threshold setting", "C", "R", "ECS recommends; customer policy decision"),
        ("First reconciliation run execution", "R", "I", "ECS runs; customer informed of results"),
        ("Unmapped bucket triage", "R", "C", "ECS provides; customer adjudicates"),
        ("Cloud SaaS coverage via SSO logs", "R", "C", "ECS integrates; customer provides log access"),
    ],
    consultant_guide_sections=[
        ("OOTB Install & Usage Foundations",
         "Use cmdb_sam_sw_install OOTB. Install records are populated from SCCM/Intune/SN Discovery via the SAMP normalization layer. The normalization layer maps discovery output to publisher/product/model records (workbooks 01-03). The unmapped bucket captures discovery output that does not normalize cleanly; the goal is ≤5% unmapped by Sprint 2."),
        ("Usage capture — measured vs. inferred",
         "Measured usage requires per-product instrumentation: Microsoft Office telemetry, Adobe license server logs, Oracle DB session counts, etc. We do this for the top 10 license-constrained products at MVP. Inferred usage (last-login from OS/SSO) covers the rest. Most license reconciliation uses cases work fine on inferred usage."),
        ("The Reconciliation Trigger",
         "Reconciliation is the moment SAM proves its value. The first run is the credibility test. Target: first run completes by Sprint 1 Wk 1 with ≤10% variance, dropping to ≤5% by Sprint 2. If variance is wider than 10% at first run, the customer concludes SAM is unreliable and Realization gets hard."),
        ("Reclamation Discipline",
         "Reclamation is human-gated at MVP because automated reclamation creates user backlash. The reclamation queue routes to the Application Owner; the owner approves or defers. Selective automation can come in Realization once trust is established with the user community."),
        ("Sprint 1 Handoff",
         "By end of Sprint 0, integrations are operational and normalization rules drafted. Sprint 1 Wk 1: first full reconciliation. Sprint 1 Wk 2: variance triage and unmapped bucket cleanup. Sprint 2 picks up with Realization-track entitlement setup (AP-07)."),
    ],
    adoption_rows=[
        ("'We want to automate reclamation — pull licenses after 60 days inactive.'",
         "Human-gated reclamation at MVP via Application Owner approval.",
         "Auto-reclamation at MVP creates user backlash strong enough to delegitimize the program. Foundations is when trust is built; aggressive automation comes later.",
         "'Auto-reclamation at MVP is how SAM programs lose their internal champion. Let me show you the human-gated workflow — it's the same reclamation outcome with the trust-building step intact.'",
         "Never at Foundations. Realization (AP-07) can introduce selective auto-reclamation for clearly inactive licenses."),
        ("'Inactive should be 30 days, not 90 — we want aggressive recovery.'",
         "90 days warn / 180 days reclaim at MVP. OOTB SAMP defaults.",
         "30-day thresholds catch users on parental leave, sabbatical, or seasonal cycles. 90/180 is the industry default for a reason.",
         "'Let me show you why the 90/180 thresholds exist. Aggressive thresholds create false positives that consume more Application Owner attention than the licenses recover.'",
         "Specific products can override (rarely). Per-product threshold is OOTB; global aggressive thresholds are not OOTB-defensible."),
        ("'BYOD users need their installs tracked too.'",
         "BYOD out of scope at Foundations. Privacy and discovery constraints.",
         "BYOD raises HR and privacy issues Foundations is not the right stage to resolve. Realization with the right legal review is the path.",
         "'BYOD opens privacy questions that should be answered before we start tracking installs on personal devices. Let me note this for Realization where we can scope it properly.'",
         "Never at Foundations. Realization with explicit HR/legal sign-off."),
        ("'We need per-session usage on every product, not just the top 10.'",
         "Measured per-session for top 10 license-constrained; inferred (last-login) for the rest.",
         "Per-session instrumentation requires per-product integration work. The top 10 captures 80% of the license value; the long tail does fine on inferred usage.",
         "'Per-session for every product is multi-quarter integration work. Inferred usage covers reconciliation needs for the tail. Let me show you the 80/20 cut.'",
         "Yes for additional products where customer has compliance audit pressure — case by case."),
        ("'Cloud SaaS should use vendor APIs, not SSO logs.'",
         "SSO logs at MVP; vendor APIs in Realization.",
         "SSO logs are universally available; vendor APIs require per-publisher integration work. Foundations covers the breadth; Realization adds depth.",
         "'SSO gives us SaaS visibility for all your SaaS providers in one move. Vendor APIs are better data but require per-product engineering work — Realization is the right place for that.'",
         "Never at Foundations."),
        ("'Server installs need full entitlement calculation now.'",
         "Server installs capture host CI at Foundations; entitlement calculation deferred to Realization.",
         "Server licensing (Oracle processor-based, SQL Server core-based, IBM PVU) is complex enough to warrant its own workbook in Realization.",
         "'Server entitlements are a separate engineering effort because the licensing models are so different. Let me note this for Realization where we have the right workbook for it.'",
         "Never at Foundations."),
        ("'We have a homegrown discovery tool — keep using it.'",
         "Phase-out plan. SCCM/Intune/SN Discovery is the OOTB stack; homegrown discovery becomes a maintenance liability.",
         "Custom discovery diverges from the SAMP normalization layer. Maintenance burden grows; SAMP capability gains are forfeited.",
         "'Your homegrown tool can run alongside through Sprint 1 for validation. By Realization, we want to have phased it out — the SAMP integration depends on the OOTB discovery stack.'",
         "Never. Transition plan required."),
    ],
    snmap_sections=[
        ("Primary table(s)", [
            ("cmdb_sam_sw_install", "Software install record", "OOTB SAMP plugin table"),
            ("cmdb_sam_sw_usage", "Usage signal record", "OOTB SAMP usage tracking"),
            ("cmdb_sam_sw_discovery_map", "Discovery normalization rules", "OOTB SAMP"),
        ]),
        ("Field mapping", [
            ("Host CI", "cmdb_sam_sw_install.installed_on", "Reference to cmdb_ci"),
            ("Product / model", "cmdb_sam_sw_install.product_model", "Reference to cmdb_sam_sw_product_model"),
            ("Install date", "cmdb_sam_sw_install.install_date", "From discovery source"),
            ("Last seen", "cmdb_sam_sw_install.last_scanned", "Discovery refresh timestamp"),
            ("Usage status", "cmdb_sam_sw_install.usage_status", "Active / Inactive / Reclamation candidate"),
            ("Discovery source", "cmdb_sam_sw_install.discovery_source", "SCCM / Intune / SN Discovery / Manual"),
        ]),
        ("OOTB features leveraged", [
            ("SAMP normalization engine", "cmdb_sam_sw_discovery_map", "Discovery → install resolution"),
            ("Usage tracking", "cmdb_sam_sw_usage", "Per-install usage signals"),
            ("Reclamation workflow", "OOTB SAMP workflow", "Human-gated approval"),
            ("Reconciliation engine", "OOTB scheduled report", "Install ↔ entitlement match"),
        ]),
        ("Integrations", [
            ("SCCM / MECM", "Native", "Primary Windows"),
            ("Microsoft Intune", "Native", "Primary Mac/mobile"),
            ("ServiceNow Discovery", "Native", "Primary Linux/Unix/cloud"),
            ("Okta / Microsoft Entra (SSO)", "Audit log import", "SaaS coverage"),
            ("Application Portfolio Management", "Native (if licensed)", "Cross-link to cmdb_ci_appl"),
        ]),
    ],
)

# =============================================================================
# WORKBOOK 5 — Lifecycle States Baseline
# =============================================================================
wb5 = TabContent(
    workbook_title="05 — Lifecycle States Baseline",
    pack_name=PACK_NAME,
    purpose="The lifecycle state model for software products and installs. Lifecycle drives reconciliation behavior, EOS reporting, and the in/out-of-scope determination for each product.",
    who_fills="Customer-side: SAM Process Owner with input from Application Owners.",
    sprint_window="End of Sprint 0, Week 2",
    estimated_effort="2-3 hours; mostly decision-making",
    related_workbooks=["02 Software Products", "03 Software Models & Versions", "04 Install & Usage Capture"],
    success_criteria=[
        "Product-level lifecycle states are defined: Approved / In Use / End of Life / Sunset.",
        "Install-level lifecycle states are defined: Active / Inactive / Reclamation Candidate / Retired.",
        "Transitions between states are documented (who triggers, what triggers).",
        "Quarterly EOS review process is established with named owner.",
    ],
    process_decisions=[
        ("Product lifecycle state count — OOTB four or expanded?",
         "OOTB four: Approved, In Use, End of Life, Sunset. No expansion at MVP.",
         "Expanded state machines are common customer requests; they uniformly fail to add reconciliation signal."),
        ("Install lifecycle states — match OOTB?",
         "OOTB four: Active, Inactive, Reclamation Candidate, Retired. No expansion.",
         "Same logic as product — OOTB states map cleanly to reconciliation behavior."),
        ("Approved state — required before deployment?",
         "Yes. Products must be in Approved state before any installs can be reconciled to them.",
         "Approved state enforces the procurement-to-deployment workflow. Skipping it silently approves shadow IT."),
        ("End of Life — what triggers the transition?",
         "Vendor EOS date OR Application Owner declares EOL OR last install retired (whichever first).",
         "Three triggers cover the main paths. EOS date and Application Owner declaration are proactive; last-install-retired is reactive but catches the cases the other two miss."),
        ("Sunset state — how long after EOL?",
         "12 months after EOL with zero active installs.",
         "Sunset hides the record from default views but preserves history for audit. 12 months is the industry default."),
        ("Reclamation Candidate — auto-transition or human-triggered?",
         "Auto-transition at 180 days inactive; human approval before reclamation execution.",
         "Auto-transition surfaces; human approval acts. Best of both."),
        ("Retired install handling — delete or archive?",
         "Archive (lifecycle_state = Retired). Never delete.",
         "License audits look back 7+ years; deleted records break that lookback."),
    ],
    dependencies=[
        ("Workbook 02 (Products) lifecycle field exists", "Pending", "ECS", "Sprint 0, Wk 2", "lifecycle_state field on product table"),
        ("Workbook 04 (Install) lifecycle field exists", "Pending", "ECS", "Sprint 0, Wk 2", "usage_status field on install table"),
        ("EOS data source identified", "Pending", "ECS", "Sprint 0, Wk 2", "From workbook 03 dependency"),
    ],
    config_sections=[
        ("Product Lifecycle States", [
            ("Approved", "Procurement-approved, ready for deployment", "Initial state on creation; required before installs allowed", False),
            ("In Use", "Active installs exist", "Auto-transition on first install", False),
            ("End of Life", "Vendor EOS reached OR App Owner declared", "Triggers quarterly EOS report inclusion", False),
            ("Sunset", "EOL + 12 months with zero installs", "Hidden from default views", False),
        ]),
        ("Install Lifecycle States", [
            ("Active", "Used within last 90 days", "Default state for new installs", False),
            ("Inactive", "No usage for 90-180 days", "Surfaced in quarterly review", False),
            ("Reclamation Candidate", "No usage for 180+ days", "Routes to Application Owner queue", False),
            ("Retired", "Reclaimed or uninstalled", "Archived, never deleted", False),
        ]),
        ("Transition Rules", [
            ("Approved → In Use", "Auto on first reconciled install", "OOTB", False),
            ("In Use → End of Life", "Vendor EOS date OR App Owner trigger", "Quarterly review enforces", False),
            ("End of Life → Sunset", "Auto at EOL + 12mo with zero installs", "OOTB scheduled job", False),
            ("Active → Inactive", "Auto at 90 days no usage", "OOTB", False),
            ("Inactive → Reclamation Candidate", "Auto at 180 days no usage", "OOTB", False),
            ("Reclamation Candidate → Retired", "Human approval via Application Owner", "Human-gated", False),
        ]),
        ("Review Cadence", [
            ("Quarterly EOS review", "First week of each fiscal quarter", "Routed to Application Owners", False),
            ("Annual Sunset review", "Q4 each fiscal year", "Sunset → permanent archive decisions", False),
            ("Reclamation review", "Monthly", "Application Owner queue", False),
        ]),
    ],
    raci_rows=[
        ("Lifecycle state definitions and approval", "R", "A", "ECS proposes; Customer approves the model"),
        ("State transition rule configuration", "R", "I", "ECS configures in ServiceNow"),
        ("EOS data source operationalization", "R", "C", "ECS sets up; Customer validates accuracy"),
        ("Application Owner training on reclamation queue", "R", "C", "ECS trains; Customer attends"),
        ("Quarterly EOS review execution (post-go-live)", "I", "R", "Customer-led; ECS supports first cycle"),
        ("Annual Sunset review", "I", "R", "Customer-only after Foundations"),
    ],
    consultant_guide_sections=[
        ("OOTB Lifecycle Foundations",
         "ServiceNow SAMP ships with a four-state product lifecycle (Approved / In Use / End of Life / Sunset) and a four-state install lifecycle (Active / Inactive / Reclamation Candidate / Retired). Both are sufficient at MVP and at scale. Customers who propose expanded state machines without exception find them fail to add reconciliation signal."),
        ("State Machine Discipline",
         "The state machine is what makes reconciliation deterministic. Every product is in exactly one state at any moment; transitions are triggered by named events with clear ownership. Customers who allow products to skip states or sit in 'between' states create exactly the kind of dirty data that makes reconciliation unreliable."),
        ("Approved State — Why It Matters",
         "The Approved state is the procurement-to-deployment workflow's anchor. A product cannot have installs reconciled against it until it is Approved. This sounds bureaucratic; it is the discipline that catches shadow IT. Without it, shadow IT installs silently aggregate against arbitrary product records."),
        ("Reclamation Flow Through States",
         "The reclamation flow is: Active (using) → Inactive (90-day warning surface) → Reclamation Candidate (180-day route to Application Owner) → Retired (human-approved reclaim). This four-step flow is what differentiates a SAM program that respects users from one that doesn't. Skipping the Inactive warning step is the most common mistake."),
        ("Sprint 1 Handoff",
         "By end of Sprint 0, lifecycle states are configured and transition rules in place. Sprint 1 picks up with the first reconciliation run (workbook 04); the state machine immediately starts driving install records into Active/Inactive based on usage data."),
    ],
    adoption_rows=[
        ("'We need a Pending Approval state before Approved.'",
         "Use the Procurement-to-Approved workflow (separate from SAM lifecycle). Approved is the entry point to SAM.",
         "A Pending state inside SAM mixes Procurement workflow with SAM workflow. Vendor Management module already handles pending-approval procurement.",
         "'Pending approval is a Procurement workflow state, not a SAM state. Vendor Mgmt module handles that, then hands off to SAM at the Approved transition.'",
         "Never at MVP."),
        ("'Inactive should be 30 days, not 90.'",
         "OOTB defaults of 90/180 are the industry standard.",
         "30 days catches false positives (sabbatical, parental leave, seasonal users). 90/180 is the right balance.",
         "'Let me show you the false-positive rate at 30-day thresholds — it overwhelms the Application Owner queue.'",
         "Specific products can override per-product. Global override not OOTB-defensible."),
        ("'We don't want auto-transitions — humans should approve every state change.'",
         "Auto-transition to surface; human approval to act (Reclamation Candidate → Retired).",
         "Auto-transition to surface scales; human approval to act maintains discipline. Pure manual breaks within a quarter.",
         "'Auto-transitions surface what needs attention. Human approval still gates the consequential action (reclamation). It's the same control, just at the right point in the flow.'",
         "Never."),
        ("'We want to delete retired install records to keep the database lean.'",
         "Archive (Retired state), never delete. Required for audit lookback.",
         "License audits look back 7+ years. Deleting retired records breaks the audit and creates compliance risk far larger than the database size.",
         "'Audit lookback is what retired-state preserves. Database size at SAMP scale is not the constraint; audit defense is.'",
         "Never."),
        ("'Sunset hides the record entirely — we want a separate Sunset view, not a hidden state.'",
         "Sunset is hidden from default views; visible in Sunset-specific views and reports.",
         "Default-view hiding is OOTB and reduces noise; explicit Sunset view preserves access for audit and review.",
         "'Sunset is hidden from the day-to-day SAMP workspace but still accessible via the Sunset report. That's the OOTB pattern — hidden by default, available when needed.'",
         "Never."),
        ("'EOL should be triggered by the customer, not by vendor EOS date automatically.'",
         "Three triggers: vendor EOS date, Application Owner declaration, or last-install-retired. All valid.",
         "Single-trigger models miss cases. Three triggers cover proactive and reactive paths.",
         "'Vendor EOS is one trigger; Application Owner declaration is another. Both available. We don't want EOL detection waiting on a single source.'",
         "Never. Multi-trigger is the OOTB-defensible approach."),
    ],
    snmap_sections=[
        ("Primary table(s)", [
            ("cmdb_sam_sw_product_definition", "lifecycle_state field", "Product state machine"),
            ("cmdb_sam_sw_install", "usage_status field", "Install state machine"),
        ]),
        ("Field mapping", [
            ("Product lifecycle state", "cmdb_sam_sw_product_definition.lifecycle_state", "Choice: Approved/In Use/EOL/Sunset"),
            ("Product EOS date", "cmdb_sam_sw_product_definition.end_of_support", "From workbook 03"),
            ("Install usage status", "cmdb_sam_sw_install.usage_status", "Choice: Active/Inactive/Reclamation Candidate/Retired"),
            ("Install last usage", "cmdb_sam_sw_install.last_usage", "Date; drives state transitions"),
        ]),
        ("OOTB features leveraged", [
            ("State machine on cmdb_sam_sw_product_definition", "OOTB", "Product lifecycle"),
            ("State machine on cmdb_sam_sw_install", "OOTB", "Install lifecycle"),
            ("Scheduled job: EOL → Sunset at +12mo", "OOTB", "Automatic"),
            ("Scheduled job: Usage → state transitions", "OOTB", "Daily"),
            ("Application Owner reclamation queue", "OOTB", "Native UI"),
        ]),
        ("Integrations", [
            ("EOS data feed", "Manual + scheduled refresh", "From workbook 03"),
            ("Application Owner email notifications", "OOTB notification rules", "Native"),
        ]),
    ],
)

# =============================================================================
# WORKBOOK 6 — Software Assignment & Owners
# =============================================================================
wb6 = TabContent(
    workbook_title="06 — Software Assignment & Owners",
    pack_name=PACK_NAME,
    purpose="How software entitlements are assigned to users and devices, and who owns each part of the SAM workflow. Assignment is the link between license entitlement (Realization) and install/user (this Pack). Ownership is the human side of the workflow.",
    who_fills="Customer-side: SAM Process Owner, IT Operations, HR (for joiner/leaver flows).",
    sprint_window="End of Sprint 0, Week 2",
    estimated_effort="3-5 hours including joiner/leaver workflow design",
    related_workbooks=["02 Software Products", "04 Install & Usage Capture", "Foundation Data Pack — Users / Groups"],
    success_criteria=[
        "User-based, device-based, and concurrent assignment models defined.",
        "Joiner / mover / leaver workflows are documented for software access.",
        "Application Owner role is defined with named responsibilities.",
        "SAM Process Owner role is defined with named responsibilities.",
    ],
    process_decisions=[
        ("Assignment model — user-based default or device-based default?",
         "Per product. User-based for productivity apps (Office, Slack, Salesforce); device-based for engineering tools tied to a workstation.",
         "Single-model defaults fight the natural licensing model. Per-product is OOTB and follows the publisher's intent."),
        ("Group-based assignment — allow at MVP?",
         "Yes for products with group entitlements (Microsoft 365 via AD group). Group assignment via OOTB SAMP, never custom.",
         "Group-based assignment is OOTB-supported and matches how Procurement actually buys (per-role bundles)."),
        ("Joiner workflow — manual or HR-triggered?",
         "HR-triggered via Onboarding workflow. Default software bundle by role.",
         "Manual joiner workflow is the #1 source of license waste and shadow IT in the first 90 days. HR-triggered is OOTB."),
        ("Mover workflow — role-change retrigger?",
         "Yes. Role change triggers software-assignment review automatically.",
         "Mover handling catches the role-change license drift that mid-career employees accumulate."),
        ("Leaver workflow — license reclamation timing?",
         "Day 1: deactivate access. Day 30: reclaim assigned licenses unless extended (executive offboarding).",
         "Same-day reclamation can break compliance reviews still in flight. 30-day default with executive exception is OOTB."),
        ("Application Owner — IT or business?",
         "Business owner with IT delegate. Business owns the decision; IT owns the configuration.",
         "Pure-IT ownership disconnects from business value; pure-business ownership disconnects from technical execution. Business + IT delegate is the OOTB pattern."),
        ("SAM Process Owner — full-time or shared?",
         "Full-time at the size where Foundations applies (typically 5,000+ endpoints). Below that, a shared SAM/ITAM role.",
         "SAM at 5,000+ endpoints generates more decision flow than a part-time role can sustain."),
    ],
    dependencies=[
        ("Foundation Data Pack — Users imported", "In Progress", "ECS", "Sprint 0, Wk 1", "Required for assignment workflow"),
        ("Foundation Data Pack — Groups imported", "In Progress", "ECS", "Sprint 0, Wk 1", "Required for group-based assignment"),
        ("HR Onboarding integration operational", "Pending", "Customer", "Sprint 0, Wk 2", "Workday / SuccessFactors / similar"),
        ("Default software bundles by role defined", "Pending", "Customer", "Sprint 0, Wk 2", "HR provides role list; Customer SAM Owner provides bundle"),
        ("Application Owner list (per product) confirmed", "Pending", "Customer", "Sprint 0, Wk 2", "From workbook 02"),
    ],
    config_sections=[
        ("Assignment Models", [
            ("User-based assignment products", "30 (from workbook 02)", "Office, Slack, Salesforce, etc.", False),
            ("Device-based assignment products", "15 (from workbook 02)", "Engineering tools tied to workstation", False),
            ("Concurrent assignment products", "5 (from workbook 02)", "Floating license pools", False),
            ("Group-based assignment — enabled", "Yes", "Via OOTB SAMP group assignment", False),
            ("Assignment table", "cmdb_sam_sw_assignment", "OOTB SAMP", False),
        ]),
        ("Joiner / Mover / Leaver", [
            ("Joiner trigger source", "HR system (Workday/SuccessFactors)", "Native integration via Onboarding", True),
            ("Joiner default bundle — by role", "TBD per customer role list", "Customer provides", True),
            ("Mover trigger", "Role change in HR system", "Re-evaluation workflow", False),
            ("Leaver Day 1 action", "Access deactivation", "OOTB", False),
            ("Leaver Day 30 action", "License reclamation", "OOTB; executive exception allowed", False),
            ("Executive offboarding extension", "90 days", "Default; per-org adjustable", True),
        ]),
        ("Ownership Roles", [
            ("Application Owner — count", "75 (one per product)", "From workbook 02", False),
            ("Backup Application Owner — required at Tier 1", "Yes", "From workbook 01", False),
            ("SAM Process Owner — full-time role", "Yes", "5,000+ endpoint threshold", True),
            ("SAM Steering Committee — established", "Yes", "Quarterly", True),
        ]),
        ("Approval Patterns", [
            ("New software request — approval path", "Application Owner → SAM Process Owner → Procurement", "OOTB request workflow", False),
            ("Reclamation approval", "Application Owner only", "Human gate from workbook 04", False),
            ("Bundle exceptions (joiner gets non-default)", "Manager + SAM Process Owner", "OOTB approval workflow", False),
        ]),
    ],
    raci_rows=[
        ("Assignment model per product", "R", "C", "ECS classifies; Customer confirms"),
        ("Joiner default bundles per role", "C", "R", "Customer-only; ECS provides bundle template"),
        ("HR Onboarding integration setup", "R", "C", "ECS configures; Customer provides access"),
        ("Mover workflow design", "R", "C", "ECS designs; Customer reviews"),
        ("Leaver workflow — Day 1 / Day 30 timing", "C", "R", "Customer policy decision; ECS configures"),
        ("Application Owner training", "R", "C", "ECS trains; Customer attends"),
        ("SAM Process Owner role definition", "C", "R", "Customer staffs; ECS provides role definition"),
        ("SAM Steering Committee charter", "C", "R", "Customer convenes; ECS contributes charter template"),
    ],
    consultant_guide_sections=[
        ("OOTB Assignment & Ownership Foundations",
         "Software assignment uses cmdb_sam_sw_assignment OOTB. User-based, device-based, group-based, and concurrent assignment models are all OOTB-supported. Per-product assignment model (workbook 02 license_model field) drives which assignment pattern applies. No customization needed at MVP."),
        ("The Joiner Workflow",
         "The joiner workflow is the single highest-leverage operational improvement SAM Foundations delivers. HR-triggered software provisioning catches the first 90 days where most license waste accumulates. Default bundles by role mean a new hire gets the right software automatically; the SAM Process Owner sees the bundle assignment and tracks it from there."),
        ("Application Owner — Business + IT Delegate",
         "Application Owner is a business role with an IT delegate. Business owner decides 'do we still need this software?' IT delegate configures, troubleshoots, escalates. Pure-IT ownership disconnects SAM from business value; pure-business ownership leaves SAM without execution capacity. The business+IT-delegate model is what works."),
        ("SAM Process Owner — Full-time at Scale",
         "SAM Process Owner is full-time at 5,000+ endpoints. Below that, a shared SAM/ITAM role works. Above 5,000, the decision flow (reclamation approvals, bundle exceptions, true-up coordination, audit response) exceeds part-time capacity. Customers who try to staff SAM as part-time at scale see the program quality degrade within two quarters."),
        ("Sprint 1 Handoff",
         "By end of Sprint 0, assignment models configured, joiner/mover/leaver workflows operational, ownership roles staffed. Sprint 1: first full HR-triggered onboarding cycle (typically 5-20 new hires); validate bundle assignment, reclamation queue routing, mover workflow."),
    ],
    adoption_rows=[
        ("'Joiner provisioning should be manual — we want IT to review every new hire.'",
         "HR-triggered automation with IT review of exceptions only.",
         "Manual joiner review is the #1 source of license waste in the first 90 days. Automation with exception-review is OOTB and scales.",
         "'Manual review for every joiner doesn't scale past about 50 hires/year. Let me show you the HR-triggered automation with exception flagging — it gives you the IT-review capacity where it actually matters.'",
         "Never at scale. Customers under 50 hires/year can stay manual if they prefer."),
        ("'Default software bundles by role limit our flexibility.'",
         "Default bundles for the bulk; exception workflow for special cases.",
         "Without defaults, every new hire is a custom decision. Defaults cover the 80%; exceptions cover the rest.",
         "'Defaults are the baseline, not the ceiling. The exception workflow handles any new hire who needs something special — it's still routed to the right approvers.'",
         "Never. Defaults are required for HR-triggered automation to work."),
        ("'Leaver reclamation should be same-day — every day costs money.'",
         "Day 1 access deactivation; Day 30 license reclamation.",
         "Same-day reclamation can break compliance reviews still in flight (terminated employees' access can be subject to legal hold).",
         "'Day 1 access is gone — that's the security control. Day 30 reclamation gives compliance time to extract whatever needs extracting from the terminated user's access.'",
         "Specific cases (immediate-threat termination) can be same-day with proper governance. Default is 30."),
        ("'Application Owner should be a group, not an individual.'",
         "Single named individual with a named backup at Tier 1.",
         "Group ownership creates the diffusion-of-responsibility pattern. No one renews because everyone assumes someone else will.",
         "'Group ownership is what creates the renewal surprise. Let me show you the individual + backup model — it preserves the redundancy without the diffusion.'",
         "Never."),
        ("'SAM Process Owner can be part-time at 8,000 endpoints — we don't have budget for full-time.'",
         "Full-time at 5,000+. Below 8,000 can be a SAM+ITAM shared role; above that, full-time is necessary.",
         "At 8,000 endpoints, the decision flow (reclamation, bundle exceptions, true-up, audit response) exceeds 20 hours/week. Part-time degrades the program within two quarters.",
         "'8,000 endpoints generates more weekly decision flow than a part-time role can sustain. The shared SAM+ITAM model can work; pure part-time SAM at this scale doesn't.'",
         "Never at 5,000+ endpoints. Shared role with explicit time allocation can work; ambiguous part-time doesn't."),
        ("'We want to assign software via custom AD groups, not OOTB SAMP groups.'",
         "OOTB SAMP group assignment can read AD groups directly. Custom layer not needed.",
         "Adding a custom group layer means maintaining mapping between AD groups and SAMP group records. OOTB integration eliminates that.",
         "'SAMP group assignment reads AD groups natively — your existing AD group structure becomes the SAMP assignment driver with no custom mapping layer.'",
         "Never."),
        ("'Concurrent license assignment is too complex — we want to ignore concurrent products at MVP.'",
         "Concurrent products in scope at MVP if customer has them. Workflow is OOTB.",
         "Concurrent products are often the highest-value licenses (engineering tools). Excluding them at MVP misses the products with the largest reclamation opportunity.",
         "'Concurrent licenses are typically your most expensive per-seat. Including them at MVP is where the largest reclamation savings show up first.'",
         "Never. Concurrent is OOTB."),
    ],
    snmap_sections=[
        ("Primary table(s)", [
            ("cmdb_sam_sw_assignment", "Software assignment record", "OOTB SAMP"),
            ("cmdb_sam_sw_entitlement", "Entitlement record (Realization-track)", "Foundations references; populated in AP-07"),
        ]),
        ("Field mapping", [
            ("Assigned to (user)", "cmdb_sam_sw_assignment.assigned_to_user", "Reference to sys_user"),
            ("Assigned to (device)", "cmdb_sam_sw_assignment.assigned_to_device", "Reference to cmdb_ci"),
            ("Assigned to (group)", "cmdb_sam_sw_assignment.assigned_to_group", "Reference to sys_user_group"),
            ("Product", "cmdb_sam_sw_assignment.product", "Reference to cmdb_sam_sw_product_definition"),
            ("Assignment type", "cmdb_sam_sw_assignment.assignment_type", "Choice: user/device/group/concurrent"),
            ("Source", "cmdb_sam_sw_assignment.source", "Choice: HR onboarding / manual / mover / etc."),
        ]),
        ("OOTB features leveraged", [
            ("HR Service Delivery onboarding workflow", "Native integration", "Joiner trigger"),
            ("Onboarding case → SAM assignment", "OOTB", "Default bundle"),
            ("Mover workflow re-evaluation", "OOTB", "Role change trigger"),
            ("Offboarding case → reclamation queue", "OOTB", "Leaver flow"),
            ("Application Owner approval workflow", "OOTB", "Native UI"),
        ]),
        ("Integrations", [
            ("HR system (Workday / SuccessFactors / etc.)", "Via HR Service Delivery", "Native"),
            ("Active Directory / Entra (groups)", "Via Foundation Data Pack", "Group assignment source"),
            ("Procurement (new software request)", "Via Vendor Mgmt", "Approval workflow"),
        ]),
    ],
)

# =============================================================================
# BUILD ALL WORKBOOKS
# =============================================================================
workbooks = [
    ("01_software_publishers.xlsx",      wb1),
    ("02_software_products_baseline.xlsx", wb2),
    ("03_software_models_and_versions.xlsx", wb3),
    ("04_install_and_usage_capture.xlsx", wb4),
    ("05_lifecycle_states_baseline.xlsx", wb5),
    ("06_software_assignment_and_owners.xlsx", wb6),
]

for fname, content in workbooks:
    out = os.path.join(HERE, fname)
    build_workbook(content, out)
    print(f"  Saved: {fname}")

# =============================================================================
# BUILD THE README DOCX
# =============================================================================
doc = EcsDocument(meta=DocMeta(
    eyebrow="ACCELERATOR PACK · SAM FOUNDATIONS",
    title="SAM Foundations\nAccelerator Pack — README",
    subtitle="Six workbooks. Stand up baseline software publishers, products, models, install/usage, lifecycle, and assignment — fast.",
    audience="Customer Project Sponsor and named Software Asset Management SMEs; ECS Federal SAM consultants",
    companion_to="Foundation Data Pack (AP-01) · ITSM Pack (AP-02) · Integration Pack (AP-03) · ITAM_HAM Packs (AP-04, AP-05)",
    doc_id="AP-06",
    version="1.0",
    status="Released",
    confidentiality="Confidential — for the recipient and their organization",
    running_header_label="SAM Foundations Accelerator Pack · README",
))

doc.add_cover_page()

# Opener
doc.para(
    "This Accelerator Pack contains six workbooks that capture the foundation a ServiceNow Software Asset "
    "Management (SAM) program needs to deliver initial value in the first sprint. The focus is deliberately narrow: "
    "stand up the software publisher relationships, the MVP product catalog, the version/model layer, the install "
    "and usage capture pipeline, the lifecycle state model, and the assignment and ownership workflow."
)
doc.para(
    "This is the foundation-first delivery in our two-prong SAM approach. The companion SAM Realization Accelerator "
    "Pack (AP-07) covers full entitlement counting, reconciliation rules, true-up forecast, audit defense, and "
    "vendor-specific licensing models (Oracle processor-based, SQL Server core-based, IBM PVU, Microsoft Microsoft "
    "365 E5 add-ons, etc.). Customers who go straight to full realization without baseline often spend months "
    "perfecting reconciliation rules nobody trusts. Foundations first lets the business see real installs, in real "
    "products, attributed to real publishers — which earns the credibility full SAM needs."
)
doc.para(
    "Completing this Pack accurately and on time directly determines how much of Sprint 1 we spend gathering data "
    "versus configuring the platform. It is the highest-leverage thing the customer team can do in the first two "
    "weeks of a SAM engagement."
)

doc.h1("The Six Workbooks", numbered=False)
doc.table(
    headers=["#", "Workbook", "What it Captures", "Customer Owner", "Due"],
    rows=[
        ["01", "Software Publishers",      "Publisher catalog, tiering, ownership, Vendor Mgmt linkage",                          "SAM Process Owner",         "End of Sprint 0, Wk 1"],
        ["02", "Software Products",        "MVP product catalog (~75 products covering 80% of spend + audit-sensitive)",          "SAM Process Owner + App Owners", "End of Sprint 0, Wk 2"],
        ["03", "Software Models & Versions", "Versions of each product (major-version granularity for most)",                     "IT Operations + App Owners", "End of Sprint 0, Wk 2"],
        ["04", "Install & Usage Capture",  "Discovery feeds, install records, usage tracking, reconciliation",                    "IT Operations + SAM Process Owner", "Sprint 0 Wk 2 → Sprint 1 Wk 1"],
        ["05", "Lifecycle States Baseline","Product and install lifecycle states + transition rules + EOS reporting",             "SAM Process Owner",         "End of Sprint 0, Wk 2"],
        ["06", "Software Assignment & Owners", "Joiner / mover / leaver flows, App Owner role, SAM Process Owner role",            "SAM Process Owner + IT Ops + HR", "End of Sprint 0, Wk 2"],
    ],
    col_widths_in=[0.4, 1.9, 3.6, 1.8, 1.66],
)

doc.para(
    "Each workbook contains eight tabs that mirror the canonical ECS Accelerator Pack architecture: Instructions "
    "(start here); Process Decisions (workshop questions with ECS OOTB recommendations pre-filled); Dependencies "
    "(other Packs and source data that must be in place); Configuration Data (final OOTB-aligned values used to "
    "configure ServiceNow); R&R (RACI matrix); Consultant Guide (internal ECS reference); Adoption vs Re-engineering "
    "(legacy-pushback scenarios with OOTB defense language); and ServiceNow Mapping (target tables and OOTB features). "
    "Customers focus on Instructions, Process Decisions, and Dependencies; ECS owns Configuration Data, Consultant "
    "Guide, and ServiceNow Mapping; both work the R&R and Adoption tabs together."
)

doc.h1("Roles & Responsibilities", numbered=False)
doc.para(
    "This Pack is delivered as a partnership. ECS provides the structure, the platform expertise, and the configuration. "
    "The customer provides authoritative data, named decision-makers, and the access ECS needs to import. The split "
    "below removes ambiguity about who owns what during Sprint 0 and Sprint 1."
)

doc.h2("ECS Federal Responsibilities")
doc.table(
    headers=["Role", "Owns"],
    rows=[
        ["Solution Architect", "Workbook structure, mapping to ServiceNow OOTB tables (cmdb_sam_sw_publisher, cmdb_sam_sw_product_definition, cmdb_sam_sw_product_model, cmdb_sam_sw_install), normalization rules, validation script, import pipeline, decision facilitation in workshops"],
        ["Process Consultant", "Workshop facilitation, lifecycle state model alignment with SAM best practice, joiner/mover/leaver workflow design, reclamation discipline coaching"],
        ["Engagement Manager", "Schedule, dependencies, escalation when customer inputs slip, sponsor sync, scope discipline (defer Realization concerns to AP-07)"],
        ["Developer",          "Configuration of publisher, product, model tables; discovery normalization rules; assignment workflow integration with HR; SAMP plugin activation"],
    ],
    col_widths_in=[2.0, 7.36],
)

doc.h2("Customer Responsibilities")
doc.table(
    headers=["Role", "Owns"],
    rows=[
        ["SAM Process Owner",       "Full-time at 5,000+ endpoints. Owns the decisions in workbooks 01-06; staffs Application Owner network; convenes SAM Steering Committee"],
        ["Application Owners",      "Named per product. Decides 'do we still need this?' at reclamation review; approves new software requests for their product"],
        ["IT Operations",           "SCCM / Intune / SN Discovery operational data; install validation; mover workflow execution"],
        ["HR (Onboarding)",         "Onboarding/offboarding integration; default software bundle definitions per role"],
        ["Procurement",             "Publisher relationships, contract data, spend export; renewal coordination"],
    ],
    col_widths_in=[2.4, 6.96],
)

doc.h1("Sprint 0 Timing", numbered=False)
doc.para(
    "All six workbooks are due by end of Sprint 0, Week 2. The dependency chain runs: 01 Publishers (Wk 1) → 02 Products "
    "(Wk 2) → 03 Models (Wk 2) and 04 Install/Usage (Wk 2 setup, Sprint 1 Wk 1 first capture) → 05 Lifecycle (Wk 2) → "
    "06 Assignment (Wk 2). Workbooks 02-06 can be worked in parallel once 01 is in place. The Engagement Manager runs "
    "a daily 15-minute SAM standup during these two weeks to surface blockers before they slip."
)

doc.callout(
    "If any workbook misses its Sprint 0 deadline, surface it immediately. The reconciliation pipeline (workbook 04) "
    "depends on all prior workbooks; a single late workbook delays the first reconciliation run that anchors Sprint 1's "
    "credibility demo. Treat Sprint 0 SAM workbooks as Tier 1 dependencies."
)

doc.h1("Cross-References", numbered=False)
doc.bullet("AP-01 Foundation Data Pack — Vendors, Users, Locations, Groups (prerequisites for workbooks 01 and 06)")
doc.bullet("AP-03 Integration Accelerator Pack — Active Directory, SCCM, Intune (prerequisites for workbook 04)")
doc.bullet("AP-04 ITAM HAM Foundations — sister pack on the hardware side; shares the discovery integration with AP-06 workbook 04")
doc.bullet("AP-07 SAM Realization Accelerator Pack (next) — full entitlement counting, reconciliation rules, true-up forecast, vendor-specific licensing models")
doc.bullet("ECS Accelerator Pack Blueprint (03_Shared/01_Accelerator_Packs/) — canonical pack architecture and tab definitions")

doc.save(os.path.join(HERE, "00_README_SAM_Foundations_Pack.docx"))
print("  Saved: 00_README_SAM_Foundations_Pack.docx")
print()
print("AP-06 build complete.")
