"""
Build INT-HT-16 — HAM How-To Consultant Guide
Hardware Asset Management (Foundations + Realization)

Internal audience — operational, candid, prescriptive.
Pairs with AP-04 (HAM Foundations) and AP-05 (HAM Realization) already in repo.
Covers: discipline overview, OOTB capability set, two-phase delivery approach,
common customer patterns vs OOTB defenses, demo flow, UAT scenarios,
post-go-live ownership, and when to actually customize.
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

OUT = os.path.join(HERE, "HAM_How-To_Consultant_Guide_INTERNAL.docx")

doc = EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL · DISCIPLINE HOW-TO GUIDE",
    title="Hardware Asset Management\nHow-To Guide",
    subtitle="Foundations and Realization — how to configure, defend, demo, and hand off HAM in the 18-week OOTB-first engagement",
    audience="ECS Delivery Consultants, Solution Architects, Engagement Managers",
    companion_to="AP-04 HAM Foundations Accelerator Pack · AP-05 HAM Realization Accelerator Pack · INT-AR series Cheatsheets",
    doc_id="INT-HT-16",
    version="1.0",
    status="Released",
    running_header_label="Internal · HAM How-To Guide",
), logo_path=LOGO)

doc.add_cover_page()
doc.page_break()

# =============================================================================
# How to Use This Guide
# =============================================================================
doc.h1("How to Use This Guide", numbered=False)
doc.para(
    "This guide is your operational reference for delivering Hardware Asset Management in the ECS "
    "OOTB-first engagement. Read it before your first HAM workshop. Keep it open during delivery. "
    "It covers what HAM means in ServiceNow OOTB, how the two-phase delivery approach works, "
    "which customer requests to push back on and why, how to run a clean demo, which UAT scenarios "
    "to use, and what post-go-live ownership should look like."
)
doc.para(
    "This guide does not replace the accelerator packs — AP-04 (HAM Foundations) and AP-05 (HAM "
    "Realization) contain the customer-fillable workbooks and the configuration data your team needs "
    "to build. This guide tells you how to run the discipline, not how to fill the workbooks. Use both."
)
doc.callout(
    "HAM is one of the highest-visibility AI realization disciplines. Clean asset data — accurate "
    "CI records, lifecycle states, assignment chains — is the foundation that makes Now Assist "
    "asset queries, Predictive Intelligence incident routing, and CMDB-backed change advisory work. "
    "Selling HAM discipline is selling AI readiness. Use that framing in every executive conversation."
)
doc.page_break()

# =============================================================================
# 1. What HAM Is in ServiceNow OOTB
# =============================================================================
doc.h1("What Hardware Asset Management Is in ServiceNow OOTB")
doc.para(
    "Hardware Asset Management in ServiceNow is the end-to-end operational model for physical IT "
    "assets — from procurement and receipt through assignment, use, maintenance, and retirement. "
    "OOTB ServiceNow provides a complete HAM capability set without customization. The most "
    "common reason customers think they need customization is that they did not know what OOTB "
    "already does."
)

doc.h2("Core OOTB HAM capabilities")
doc.table(
    headers=["Capability", "What it does OOTB", "Where it lives in ServiceNow"],
    rows=[
        ["Asset Stockrooms", "Tracks physical storage locations for unassigned assets. Multiple stockrooms per site supported.", "Asset > Stockrooms"],
        ["Asset Classes and Models", "Hierarchical classification: Asset Class > Model > individual CI. OOTB classes cover laptops, desktops, mobile, peripherals, networking.", "Asset > Product Models"],
        ["Lifecycle States", "OOTB states: In Stock, In Use, In Maintenance, Retired, Consumed, Stolen/Lost. State transitions drive workflows automatically.", "Asset record > State field"],
        ["IMAC Workflows", "Install, Move, Add, Change workflows for common asset operations. OOTB flow designer templates for each.", "Flow Designer > Asset workflows"],
        ["Procurement and Intake", "Purchase order → receipt → stockroom intake workflow. Integrates with vendor catalog for model matching.", "Procurement > Purchase Orders"],
        ["Disposal and Retirement", "Retirement workflow with data-wipe tracking, disposal vendor assignment, and audit trail.", "Asset > Disposal Orders"],
        ["Discovery Integration", "ServiceNow Discovery (MID Server) auto-populates CI records and links to asset records. No manual CI creation needed for networked devices.", "Discovery > Discovered Items"],
        ["Audit and Reconciliation", "Scheduled asset audits with mobile scan support. Reconciliation between asset records and discovered CIs.", "Asset > Audits"],
        ["Reporting and Dashboards", "OOTB PA indicators: asset by lifecycle state, unallocated assets, assets approaching end-of-life, assignment gaps.", "Performance Analytics > HAM"],
        ["HAM Workspace", "Unified HAM manager workspace for asset operations, alerts, and drill-down — no custom portal needed.", "Asset Management > HAM Workspace"],
    ],
    col_widths_in=[2.0, 3.6, 3.76],
)

doc.h2("What HAM is NOT (scope boundaries)")
doc.para(
    "Be explicit about scope during the workshop to prevent scope creep. HAM in the OOTB-first "
    "engagement covers physical IT hardware. It does not cover:"
)
doc.bullet("Software assets and licenses — that is SAM (covered in AP-06 and AP-07)")
doc.bullet("Facilities assets (furniture, HVAC, building equipment) — out of scope for ServiceNow ITAM")
doc.bullet("Financial asset depreciation and GL posting — ServiceNow has OOTB depreciation schedules but full ERP integration is a separate workstream")
doc.bullet("Vendor contract management — covered by Contract Management module, not HAM")
doc.para(
    "If a customer raises one of these in a HAM workshop, acknowledge it and park it in the "
    "Governance Triage Log. Do not let it expand the HAM workstream."
)
doc.page_break()

# =============================================================================
# 2. The Two-Phase Delivery Approach
# =============================================================================
doc.h1("The Two-Phase Delivery Approach")
doc.para(
    "HAM is delivered in two phases in the ECS engagement model: Foundations in Sprint 5 "
    "(Month 3, first sprint) and Realization in Sprint 6 (Month 3, second sprint). Each phase "
    "has a named accelerator pack. The split is intentional — Foundations establishes the data "
    "and structural baseline; Realization builds the operational workflows on top of it."
)

doc.h2("Phase 1: HAM Foundations (Sprint 5 — AP-04)")
doc.para(
    "The Foundations phase answers: what assets do we have, where are they, and how are they "
    "classified? By the end of Foundations, the customer has:"
)
doc.bullet("Stockrooms defined and mapped to physical locations")
doc.bullet("Asset classes and model catalog populated (hardware categories the organization actually uses)")
doc.bullet("Initial asset inventory loaded or imported (from existing CMDB, spreadsheet, or Discovery)")
doc.bullet("Lifecycle states configured and baseline state assignments applied")
doc.bullet("Assignment and receiving workflows operational")

doc.para(
    "The AP-04 workbook drives the data collection for this phase. The six tabs in AP-04 are the "
    "data inputs for the Sprint 5 configuration build. Your job in the Foundations workshop is to "
    "get the customer to fill those workbooks with real data — not placeholder data. The build "
    "only works if the data is real."
)
doc.callout(
    "Foundations gating rule: do not start Realization until stockrooms, asset classes, and "
    "at least 80% of the asset inventory are in the system. Realization workflows built on "
    "placeholder data will need to be rebuilt. Push back on the timeline before accepting bad data."
)

doc.h2("Phase 2: HAM Realization (Sprint 6 — AP-05)")
doc.para(
    "The Realization phase answers: how do assets move through their lifecycle, and who is "
    "accountable at each stage? By the end of Realization, the customer has:"
)
doc.bullet("IMAC workflows (Install, Move, Add, Change) configured and tested")
doc.bullet("Procurement and intake workflow operational (PO to stockroom receipt)")
doc.bullet("Disposal and retirement workflow with data-wipe and audit trail")
doc.bullet("Reconciliation process between Discovery-discovered CIs and asset records")
doc.bullet("HAM KPIs live in Performance Analytics")
doc.bullet("Named asset manager roles and post-go-live operating model documented")

doc.para(
    "The AP-05 workbook drives the data collection and decision-making for this phase. "
    "Key decisions in Realization: stockroom strategy (centralized vs. distributed), "
    "IMAC workflow triggers (manual request vs. auto-trigger from Discovery), "
    "disposal vendor assignment, and reconciliation schedule."
)
doc.page_break()

# =============================================================================
# 3. OOTB Defense — Common Customer Requests
# =============================================================================
doc.h1("OOTB Defense — Common Customer Requests and How to Handle Them")
doc.para(
    "These are the customization requests that come up in nearly every HAM engagement. The "
    "column on the right tells you what to say and what to do. When in doubt, adopt OOTB and "
    "flag exceptions in INT-TBV-03."
)

doc.table(
    headers=["Customer Request", "OOTB Defense", "When to Actually Customize"],
    rows=[
        [
            "Custom asset fields (department cost code, asset tag format, warranty tracking fields)",
            "ServiceNow OOTB asset record has 40+ fields covering the vast majority of asset attributes. Show the customer the OOTB field list before agreeing to add any custom fields. Dictionary extensions (new fields on existing tables) are low-risk but still count as customization.",
            "A specific field is required for a downstream integration and has no OOTB equivalent. Document the integration requirement and the specific field in INT-TBV-03 before building."
        ],
        [
            "Custom lifecycle states beyond OOTB (e.g., 'Pending Procurement', 'In Repair', 'Awaiting Disposal Approval')",
            "OOTB lifecycle states cover the full standard asset lifecycle. 'In Repair' maps to 'In Maintenance'; 'Pending Procurement' is handled by the PO workflow before asset creation. Show the state transition diagram before adding states.",
            "A state is required for a regulatory audit trail that has no OOTB equivalent and cannot be inferred from workflow history. Rare — get the regulatory requirement in writing."
        ],
        [
            "Custom IMAC workflows with approval gates not in OOTB templates",
            "OOTB IMAC flow designer templates support approval gates natively. Walk the customer through the OOTB template before agreeing to build a custom flow. Most 'custom' requirements fit the template with configuration, not code.",
            "An approval gate requires integration with an external approval system (e.g., HR system approval for asset assignment) that cannot be handled by ServiceNow approval engine. Flag as integration work, not HAM customization."
        ],
        [
            "Separate asset databases or shadow IT tracking outside ServiceNow",
            "The entire point of HAM is consolidating asset records into a single system of record. Parallel databases should be decommissioned, not integrated. Offer to help map the parallel database to ServiceNow fields during the Foundations phase.",
            "Never. A parallel asset database is a data quality problem, not a HAM design feature. Escalate to the Delivery Manager if the customer insists."
        ],
        [
            "Barcode/RFID scanning integration for physical audits",
            "ServiceNow supports mobile barcode scanning for asset audits OOTB via the Now Mobile app. Walk the customer through the native scanning capability before proposing a custom integration.",
            "The customer has an existing RFID infrastructure that cannot be replaced and requires a custom integration. Treat as an Integration Accelerator Pack item, not a HAM customization."
        ],
        [
            "Automated asset assignment based on HR data (new hire, transfer, termination)",
            "ServiceNow OOTB supports HR-triggered workflows via the Employee Lifecycle Operations module. If HR integration is in scope (Active Directory/Workday), asset assignment can be automated within OOTB capabilities.",
            "HR system is not integrated with ServiceNow and the customer does not want to integrate it. Document as a manual process gap and include in the post-go-live operating model."
        ],
    ],
    col_widths_in=[2.4, 3.8, 3.16],
)
doc.page_break()

# =============================================================================
# 4. Demo Flow
# =============================================================================
doc.h1("Demo Flow — HAM Receive-Assign-Return-Retire")
doc.para(
    "The canonical HAM demo shows the full asset lifecycle end-to-end in under 15 minutes. "
    "This is the demo you run in the Sprint 5 kickoff to show the customer what OOTB HAM looks "
    "like before they have filled in their own data. Run it against the HAM demo data set — "
    "not against the customer's production data."
)

doc.h2("Pre-demo setup (do before the meeting starts)")
doc.bullet("Confirm HAM Workspace is active and accessible on the demo instance")
doc.bullet("Pre-load: one demo stockroom (e.g., 'Central IT Stockroom, Building A'), 5-10 demo laptop models, 20 demo asset records in 'In Stock' state")
doc.bullet("Have one demo user account ready for assignment (name: Alex Demo, department: Finance)")
doc.bullet("Open tabs: HAM Workspace, Asset record list, one PO record, one open IMAC request")
doc.bullet("Confirm Discovery is configured and has at least one discovered CI to link")

doc.h2("Demo narrative and click flow")

doc.h3("Act 1 — Receiving a new asset (3 minutes)")
doc.para("Opening line: 'Let me show you how a new laptop goes from a purchase order to a consultant's desk.'")
doc.bullet("Navigate to Procurement > Purchase Orders. Open the demo PO (3 laptops, Lenovo ThinkPad X1).")
doc.bullet("Show PO details: vendor, model, quantity, expected delivery. Point out the OOTB PO-to-receipt workflow.")
doc.bullet("Click 'Receive Order'. Show the receipt form — stockroom auto-populates from PO.")
doc.bullet("Submit receipt. Show the three new asset records created automatically in 'In Stock' state, assigned to the demo stockroom.")
doc.bullet("Talking point: 'No manual data entry. The PO drove the asset record creation.'")

doc.h3("Act 2 — Assigning an asset to a user (3 minutes)")
doc.para("Transition: 'Now Alex in Finance needs a laptop on Day 1. Here is how that works.'")
doc.bullet("Open HAM Workspace. Show the 'Available Assets' tile — the three new laptops appear.")
doc.bullet("Select one. Click 'Assign'. Type 'Alex Demo'. The assignment form auto-fills location from Alex's HR record.")
doc.bullet("Submit. The asset record updates: state changes to 'In Use', assigned-to populates, location populates.")
doc.bullet("Show the Discovery link: the laptop's serial number is already in the CMDB from the last Discovery run — the asset record and CI record are now linked.")
doc.bullet("Talking point: 'One action in ServiceNow and the asset record, the CMDB, and the Discovery record are all aligned.'")

doc.h3("Act 3 — Asset return and stockroom processing (3 minutes)")
doc.para("Transition: 'Six months later, Alex transfers to a different office and returns the laptop.'")
doc.bullet("From the asset record, click 'Return to Stockroom'. Select stockroom. Add a note.")
doc.bullet("State changes to 'In Stock'. The previous assignment is preserved in the audit trail.")
doc.bullet("Show the audit trail tab: full history of who had the asset, when, and what changed.")
doc.bullet("Talking point: 'Every hand the asset passed through is on record. Audit-ready without any manual logging.'")

doc.h3("Act 4 — Retirement and disposal (3 minutes)")
doc.para("Transition: 'This laptop is now 5 years old and past end-of-life. Here is how we retire it.'")
doc.bullet("From HAM Workspace, open the 'Approaching End-of-Life' alert. Three assets flagged.")
doc.bullet("Select one. Click 'Retire'. The OOTB disposal workflow triggers: data-wipe confirmation required, disposal vendor assignment, final audit stamp.")
doc.bullet("Show the disposal order record created automatically.")
doc.bullet("Talking point: 'End-of-life assets do not fall through the cracks. ServiceNow flags them, drives the disposal workflow, and documents the chain of custody.'")

doc.h3("Closing (2 minutes)")
doc.para(
    "Closing line: 'What you just saw — receive, assign, return, retire — is 100% OOTB ServiceNow. "
    "No custom code. The workflow you saw is what we will configure for your asset classes, your "
    "stockrooms, and your naming conventions. The accelerator pack workbooks we will walk through "
    "next are how we collect the specifics to make this yours.'"
)
doc.callout(
    "Demo recovery note: if Discovery is not populated on the demo instance, skip the Discovery "
    "link in Act 2 and say: 'Once Discovery is running and your MID Servers are configured, the "
    "CI linkage happens automatically — we will set that up in Sprint 4.' Do not apologize for "
    "the missing data; redirect to the future state."
)
doc.page_break()

# =============================================================================
# 5. UAT Scenarios
# =============================================================================
doc.h1("UAT Scenarios")
doc.para(
    "These scenarios are the minimum viable HAM UAT set. They test the Foundations and Realization "
    "configuration against real customer data before go-live. Each scenario has a pass/fail criterion. "
    "Do not accept UAT sign-off until all scenarios pass with real data — not demo data."
)

doc.table(
    headers=["Scenario", "Steps", "Pass Criterion"],
    rows=[
        [
            "HAM-UAT-01: New asset procurement and receipt",
            "1. Create a PO for 2 assets of a real model in the customer catalog.\n2. Receive the PO against the primary stockroom.\n3. Confirm asset records created with correct model, state, and stockroom.",
            "Two asset records exist in 'In Stock' state, linked to the correct model, stockroom, and PO record. No manual data entry required beyond the PO."
        ],
        [
            "HAM-UAT-02: Asset assignment to a real user",
            "1. Assign one of the received assets to a named user in Finance.\n2. Confirm state change, location, and assigned-to populate correctly.\n3. Confirm Discovery links the CI to the asset record within 24 hours.",
            "Asset record shows 'In Use', correct user, correct location. CI record in CMDB is linked to the asset record."
        ],
        [
            "HAM-UAT-03: IMAC — Move an asset to a different location",
            "1. Raise an IMAC Move request for the assigned asset.\n2. Approve the request per the customer's approval chain.\n3. Complete the move. Confirm asset record location updates.",
            "IMAC workflow completes with all approval gates satisfied. Asset record shows new location. Audit trail records the move with timestamp and approver."
        ],
        [
            "HAM-UAT-04: Asset return and stockroom processing",
            "1. Return the assigned asset to the stockroom.\n2. Confirm state reverts to 'In Stock'.\n3. Confirm audit trail shows the full assignment history.",
            "State is 'In Stock'. Audit trail is complete. Previous assignment is preserved and queryable in reporting."
        ],
        [
            "HAM-UAT-05: Disposal workflow",
            "1. Flag one asset as 'Retired'.\n2. Complete the disposal workflow: data-wipe confirmation, disposal vendor, final audit stamp.\n3. Confirm disposal order record created.",
            "Disposal order exists and is linked to the asset record. Asset state is 'Retired'. Disposal vendor and wipe confirmation are recorded."
        ],
        [
            "HAM-UAT-06: HAM reporting — lifecycle state report",
            "1. Open the HAM Performance Analytics dashboard.\n2. Confirm the asset-by-lifecycle-state indicator shows current real data.\n3. Confirm the 'unallocated assets' indicator is accurate against actual stockroom contents.",
            "PA dashboard shows accurate data that matches the asset records created in UAT-01 through UAT-05. No data lag exceeding the PA collection schedule."
        ],
    ],
    col_widths_in=[2.2, 3.8, 3.36],
)
doc.page_break()

# =============================================================================
# 6. Post-Go-Live Ownership
# =============================================================================
doc.h1("Post-Go-Live Ownership")
doc.para(
    "HAM only delivers long-term value if someone owns it after ECS leaves. The ownership model "
    "must be documented and agreed before go-live — not assumed. The handoff conversation should "
    "happen in the final week of Sprint 6, not at hypercare end."
)

doc.h2("Named roles the customer must fill")
doc.table(
    headers=["Role", "Responsibilities", "Minimum FTE"],
    rows=[
        [
            "HAM System Owner",
            "Owns HAM configuration in ServiceNow. Approves changes to lifecycle states, IMAC workflows, asset classes. Single point of accountability for HAM data quality.",
            "0.25 FTE (can be shared with broader ITAM/ITSM owner role)"
        ],
        [
            "Stockroom Managers",
            "Physically receive assets, process returns, perform audits. One per physical stockroom location. Use ServiceNow Now Mobile for scan-based auditing.",
            "One named person per stockroom (can be part-time)"
        ],
        [
            "Asset Data Steward",
            "Runs monthly reconciliation between Discovery CIs and asset records. Flags discrepancies. Manages the disposal queue.",
            "0.25 FTE"
        ],
        [
            "Procurement Liaison",
            "Creates and closes purchase orders in ServiceNow. Coordinates with vendors on model catalog updates.",
            "Existing procurement role — add HAM responsibilities to current job"
        ],
    ],
    col_widths_in=[2.0, 5.0, 2.36],
)

doc.h2("Post-go-live operating cadence")
doc.bullet("Weekly: stockroom manager reviews unallocated asset queue and processes any pending returns or assignments")
doc.bullet("Monthly: data steward runs Discovery reconciliation report and resolves discrepancies")
doc.bullet("Quarterly: HAM system owner reviews asset class and model catalog — add new models, retire obsolete ones")
doc.bullet("Annually: full physical audit using Now Mobile scan. Reconcile physical count against ServiceNow records.")

doc.h2("Continuous improvement roadmap (hand to customer at closeout)")
doc.bullet("Phase 2 roadmap item: Software Asset Management integration with HAM (SAM Realization — AP-07)")
doc.bullet("Phase 2 roadmap item: Vendor managed inventory integration for auto-replenishment")
doc.bullet("Phase 2 roadmap item: HAM-driven CMDB health scoring for AI realization metrics")

doc.callout(
    "Ownership handoff is not optional. If you leave an engagement without documented HAM owners "
    "and a signed operating model, the HAM configuration will drift within 90 days. Schedule the "
    "handoff conversation no later than Day 3 of the final sprint. Use the Operational Handoff Pack "
    "(CLT-CO-04) to structure the conversation."
)
doc.page_break()

# =============================================================================
# 7. When to Actually Customize
# =============================================================================
doc.h1("When to Actually Customize")
doc.para(
    "OOTB-first means OOTB by default — not OOTB always. There are legitimate customization cases "
    "in HAM. The discipline is recognizing them and keeping the list short. Every item on the list "
    "below has earned its place through real engagement experience. If a customization request does "
    "not appear on this list, that is a signal to push back harder, not to add it to the list."
)

doc.h2("Legitimate customization cases in HAM")
doc.table(
    headers=["Customization", "Justification", "What to do"],
    rows=[
        [
            "New asset field required by an external system integration",
            "Downstream system (ERP, finance tool) requires a specific field value at asset creation that has no OOTB equivalent.",
            "Dictionary extension (new field on asset table). Low-risk. Document the integration requirement and field mapping in INT-TBV-03. Get DM sign-off."
        ],
        [
            "Custom lifecycle state required for regulatory audit",
            "A regulatory body (FISMA, FedRAMP auditor, contract requirement) requires a specific state name in the audit trail that cannot be mapped to an OOTB state.",
            "Add the state to the lifecycle state choice list. Get the regulatory requirement in writing. Document in INT-TBV-03. Note that this is a configuration extension, not a code change."
        ],
        [
            "IMAC approval gate integration with non-ServiceNow approval system",
            "Customer's policy requires approval from an HR or ERP system that cannot be replicated within ServiceNow's approval engine.",
            "Integration workstream item — not a HAM customization. Route to the Integration Accelerator Pack. Scope the integration separately."
        ],
        [
            "RFID/IoT asset tracking integration",
            "Customer has an existing RFID or IoT asset tracking infrastructure and requires two-way sync with ServiceNow asset records.",
            "Integration workstream item. OOTB ServiceNow does not include RFID/IoT integration natively. Scope as a Phase 2 integration item unless the customer has a compelling business case for Sprint 5/6."
        ],
    ],
    col_widths_in=[2.4, 3.6, 3.36],
)

doc.h2("The customization rule")
doc.para(
    "Every customization approved for HAM goes into INT-TBV-03 (Customization Variance Tracker) "
    "with: the item description, the business justification, the customer who requested it, the "
    "ECS engineer who approved it, and the Delivery Manager who signed off. No exceptions. "
    "Customizations without a Triage Log entry are unauthorized scope — escalate to the DM immediately."
)

doc.save(OUT)
print(f"Saved: {OUT}")
