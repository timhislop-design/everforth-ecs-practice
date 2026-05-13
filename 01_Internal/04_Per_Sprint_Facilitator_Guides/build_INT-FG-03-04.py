"""Build INT-FG-03 and INT-FG-04 — Sprint 2 Facilitator Guides"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

# ============================================================
# INT-FG-03 — Sprint 2 Catalog & Request
# ============================================================
OUT03 = os.path.join(HERE, "INT-FG-03_Sprint2_Catalog_Facilitator_Guide_INTERNAL.docx")
doc = EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL · PER-SPRINT FACILITATOR GUIDE",
    title="Sprint 2 — Service Catalog & Request\nFacilitator Guide",
    subtitle="Workshop agenda, decision pre-fills, OOTB defense language, common pitfalls, and retro template for Sprint 2 Service Catalog & Request Management",
    audience="ECS Lead Consultant, Solution Architect, Engagement Manager",
    companion_to="Sprint 2 Catalog Workbook · INT-DS-02 Catalog Demo Script · INT-AR-01 Catalog Rationalization Cheatsheet",
    doc_id="INT-FG-03", version="1.0", status="Released",
    running_header_label="Internal · Sprint 2 Catalog & Request Facilitator Guide",
), logo_path=LOGO)

doc.add_cover_page(); doc.page_break()

doc.h1("How to Use This Guide", numbered=False)
doc.para("This guide is for the ECS consultant facilitating the Sprint 2 Service Catalog & Request Management workshops. Service Catalog is where customer expectations peak — everyone has a list of items they want in the catalog, and the workshop's job is to rationalize that list to a maintainable OOTB baseline before anyone starts building. The worst outcome in Sprint 2 is a catalog that looks complete at demo but becomes a maintenance burden after go-live.")
doc.callout("The governing principle: catalog items that cannot be owned and updated by a named business owner should not exist in production. Ownership is the filter. Complexity is the enemy.")
doc.page_break()

doc.h1("Sprint Overview")
doc.table(headers=["Item","Detail"], rows=[
    ["Sprint number","Sprint 2 of 6 (Month 2, Weeks 5-6), concurrent with Employee Center (INT-FG-04)"],
    ["Duration","2 weeks (workshops Week 5; configuration Weeks 5-6; demo Week 6)"],
    ["Primary discipline","Service Catalog & Request Management — category structure, catalog item rationalization, fulfillment workflows, approval design, and request portal integration"],
    ["Sprint goal","A rationalized service catalog with ≤ 40 published items, each with a named owner, clear fulfillment path, and OOTB approval chain. Zero orphan items and zero items with custom fulfillment workflows at MVP."],
    ["Customer participants required","Catalog Owner (decision authority), Service Desk Manager, 3-4 department heads (HR, IT, Facilities — whoever owns catalog categories), Portal Admin if applicable"],
    ["ECS participants","Lead Consultant (facilitator), Solution Architect (configuration), Engagement Manager (decision log)"],
    ["Key artifacts produced","Catalog item inventory (rationalized), Category hierarchy (finalized), Fulfillment workflow matrix, Approval chain decisions, Service Catalog Accelerator Pack (completed)"],
    ["Sprint dependency","Employee Center configuration (INT-FG-04) depends on catalog being published — catalog must be demo-ready before EC portal goes live"],
], col_widths_in=[2.4,7.0])
doc.page_break()

doc.h1("Workshop Agendas")
doc.h2("Workshop 1 — Catalog Item Inventory and Rationalization (90 min)")
doc.table(headers=["Time","Agenda Item","Facilitation Notes"], rows=[
    ["0:00–0:15","Inventory review — what exists today","Ask the Catalog Owner to share the current catalog item list. Do not react to size. Simply count: how many items? How many have been requested in the last 90 days? Items with zero requests in 90 days are candidates for retirement."],
    ["0:15–0:40","The 40-item MVP filter","Present the ECS recommendation: MVP catalog = the 40 most-requested items, each with a named owner. Work through the inventory applying two filters: (1) Usage — was this requested in the last 90 days? (2) Ownership — can someone name the person who maintains this item? Items that fail both filters are parked, not deleted."],
    ["0:40–1:05","Category structure alignment","Present the ECS recommended category hierarchy (aligned to CSDM service taxonomy). Goal: ≤ 6 top-level categories, ≤ 8 items per category. Common pushback: IT categories are easy but HR and Facilities want their own top-level nodes. Resolution: the category structure is for navigation, not org chart representation — group by employee need, not by department."],
    ["1:05–1:20","Decision record + parking lot","Confirm the 40-item MVP list. Items not making MVP go into the Governed Exceptions log with a Phase 2 target date. Not deleted — deferred."],
    ["1:20–1:30","Next steps","ECS to configure the category structure and create placeholder items. Customer to provide fulfillment workflow details for top 10 items before Workshop 2."],
], col_widths_in=[1.0,2.6,5.8])

doc.h2("Workshop 2 — Fulfillment Workflows and Approval Chains (90 min)")
doc.table(headers=["Time","Agenda Item","Facilitation Notes"], rows=[
    ["0:00–0:10","Review Workshop 1 decisions","Show the dev instance with the category structure and item placeholders. Confirm the MVP list hasn't changed."],
    ["0:10–0:40","Fulfillment workflow design","Walk through each item category's fulfillment pattern. OOTB has three patterns: (1) Auto-fulfillment — system actions only, no human task; (2) Single-group fulfillment — one assignment group receives and fulfills the task; (3) Multi-stage fulfillment — sequential tasks across groups (max 3 stages at MVP). Ask for each item: which pattern applies? Anything requiring custom catalog client scripts or complex variable sets goes to the Customization Council."],
    ["0:40–1:05","Approval design","OOTB supports three approval patterns: (1) None — no approval required; (2) Group manager approval — auto-routes to requester's manager; (3) Named approver — specific user or group. Map each item to one pattern. Common pushback: 'We need multi-level approval for some items.' OOTB supports sequential approval chains — demonstrate this before the customer asks for custom code."],
    ["1:05–1:20","Variable set standards","Review the OOTB variable types. Establish the rule: no more than 8 variables per catalog item at MVP. Variable sets that are reused across items should be common variable sets (OOTB feature). Items with more than 8 variables need rationalization — are all variables truly required for fulfillment?"],
    ["1:20–1:30","Decisions and next steps","Confirm fulfillment and approval decisions. ECS to configure top 10 items fully before the validation session."],
], col_widths_in=[1.0,2.6,5.8])

doc.h2("Workshop 3 — Catalog Validation (60 min)")
doc.table(headers=["Time","Agenda Item","Facilitation Notes"], rows=[
    ["0:00–0:10","Live catalog walkthrough","Open the dev Employee Center portal. Navigate the catalog as a requester. Show the category hierarchy, search, and item display."],
    ["0:10–0:40","Item-by-item validation","Walk through the top 10 items with the Catalog Owner: submit a test request for each, confirm the workflow triggers, approval routes correctly, and the fulfillment task lands in the right group. Capture discrepancies without fixing on the spot."],
    ["0:40–0:55","Notification review","Confirm the request acknowledgment notification (to requester), fulfillment task notification (to fulfillment group), and completion notification (to requester) are all working."],
    ["0:55–1:00","Sprint demo prep","Confirm demo participants, date, and which 5 catalog items to feature in the demo."],
], col_widths_in=[1.0,2.6,5.8])
doc.page_break()

doc.h1("Decision Pre-Fills — ECS Recommendations")
doc.h2("Decision 1 — Catalog Category Structure")
doc.table(headers=["ECS Recommendation","Rationale","Common Pushback","ECS Response"], rows=[
    ["6 top-level categories: IT Services, Software & Access, Hardware, HR Services, Facilities, Employee Onboarding/Offboarding",
     "Reflects the most common employee request patterns across our customer base. Mirrors the CSDM service taxonomy so catalog items map to services without manual cross-referencing.",
     "'HR wants their own section separate from IT.'",
     "'HR Services is already a top-level category. Items under HR Services are owned by HR — the category name is the employee's lens, not the department's. HR items show up under HR Services regardless of who fulfills them.'"],
    ["No more than 40 items at MVP. Publish only items with named owners.",
     "Unmaintained catalog items are the primary source of portal abandonment. Employees stop using the portal when items are outdated, broken, or return no response.",
     "'We have 200 items in our current catalog.'",
     "'Of those 200, how many were requested in the last 90 days? In every catalog rationalization we have done, that number is under 40. The rest exist because no one had the authority to retire them. We are giving you that authority today.'"],
], col_widths_in=[2.2,2.2,2.0,3.0])

doc.h2("Decision 2 — Fulfillment Workflow Pattern")
doc.table(headers=["ECS Recommendation","Rationale","Common Pushback","ECS Response"], rows=[
    ["OOTB Flow Designer workflows only. No Workflow Editor (legacy). No inline catalog client scripts.",
     "Flow Designer workflows are upgrade-safe and visible to non-developers. Workflow Editor and client scripts are the primary source of catalog technical debt in every customer we've inherited.",
     "'Our current catalog uses client scripts extensively.'",
     "'We know — that is why we are rebuilding it. Client scripts that fire on variable changes are fragile, invisible to administrators, and break unpredictably after upgrades. Flow Designer achieves the same outcomes with less code and more visibility. We will migrate the logic, not the scripts.'"],
    ["Maximum 3-stage fulfillment for MVP items. Items requiring more than 3 stages go to Phase 2.",
     "3-stage fulfillment covers 90% of IT and HR catalog scenarios. Beyond 3 stages, the catalog item is usually a process that belongs in a workflow module, not a catalog item.",
     "'Some items need 5 approval steps.'",
     "'5 approval steps for a catalog item is a process design problem, not a system requirement. Walk me through what each step is actually doing — in most cases, 3 of the 5 steps can be handled by the fulfillment group internally without surfacing them as separate ServiceNow approval records.'"],
], col_widths_in=[2.2,2.2,2.0,3.0])
doc.page_break()

doc.h1("Common Pitfalls")
for title, body in [
    ("Pitfall 1 — The Catalog Migration Trap",
     "The customer wants to migrate all 200 existing catalog items 'as-is' before rationalizing. This produces 200 items of variable quality in the new portal on day one and makes rationalization politically impossible afterward.\n\nRedirect: 'Migration and rationalization are the same project. We migrate only what passes the ownership and usage filters. Items that do not pass are retired in the old system, not migrated to the new one. This is the most impactful thing we will do in Sprint 2.'"),
    ("Pitfall 2 — Variable Set Scope Creep",
     "A department submits a catalog item with a 25-variable intake form. Every variable 'is required' according to the department. The fulfillment team needs the data, but requesters abandon the form.\n\nRedirect: 'How many of these 25 variables could be pre-populated from the user's HR record? How many could the fulfillment team look up themselves? In our experience, 25-variable forms can be reduced to 8 by separating requester-facing questions from fulfillment data lookups. Let us do that exercise.'"),
    ("Pitfall 3 — Approval Chain Ownership Gap",
     "The customer approves the approval chain design in the workshop but the named approvers are not set up as users in ServiceNow yet. The demo shows approval routing to a user who doesn't exist.\n\nEarly signal: approval chains that reference specific named individuals (not groups). Redirect: 'Approval routing to named individuals is fragile — what happens when that person is on leave? OOTB group-based approval (routes to the group's manager role) is more resilient. Let us use group-based approval for MVP and add named approver exceptions only where required by policy.'"),
    ("Pitfall 4 — The Portal Branding Blocker",
     "The customer's comms team gets involved and the sprint stalls on portal branding decisions: logo placement, color scheme, department images. These are not Sprint 2 decisions.\n\nRedirect: 'Portal branding is an Employee Center configuration item, not a catalog item. We are configuring the catalog in this sprint. Portal branding is in scope for Sprint 2 Employee Center (INT-FG-04) and the decisions there are: header logo, background color, and department tile images. We will do that in the parallel sprint. Today we are locking catalog item structure.'"),
]; 
    doc.h2(title); doc.para(body)

doc.page_break()
doc.h1("Sprint Demo Discipline")
doc.h2("Pre-Demo Checklist")
doc.table(headers=["#","Check","Owner","Status"], rows=[
    ["1","Top 10 catalog items published with correct category, variables, and fulfillment workflows","ECS SA","☐"],
    ["2","Approval chains tested end-to-end for at least 3 items requiring approval","ECS SA","☐"],
    ["3","Employee Center portal showing catalog with correct category navigation","ECS SA","☐"],
    ["4","Test requests submitted and fulfilled for top 5 items — confirmation emails confirmed working","ECS SA","☐"],
    ["5","Catalog item search returning expected results","ECS Lead","☐"],
    ["6","INT-TBV-06 Sprint Demo Discipline Audit prepared","EM","☐"],
], col_widths_in=[0.4,5.8,1.4,1.0])

doc.h1("Sprint Retro Template")
doc.table(headers=["Category","Question","Capture Here"], rows=[
    ["What worked","Which catalog items were configured cleanest? What made them easy?",""],
    ["What worked","How did the customer respond to the 40-item filter?",""],
    ["What didn't work","Which items required the most back-and-forth? Why?",""],
    ["Governed exceptions","How many items are in the Phase 2 backlog? Who owns the review?",""],
    ["Sprint 3 readiness","Is the customer ready for Sprint 3 (Knowledge + Virtual Agent)?",""],
    ["ECS learning","What would we do differently?",""],
], col_widths_in=[1.6,4.0,3.8])

doc.save(OUT03)
print(f"INT-FG-03 built → {OUT03}")

# ============================================================
# INT-FG-04 — Sprint 2 Employee Center
# ============================================================
OUT04 = os.path.join(HERE, "INT-FG-04_Sprint2_EmployeeCenter_Facilitator_Guide_INTERNAL.docx")
doc2 = EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL · PER-SPRINT FACILITATOR GUIDE",
    title="Sprint 2 — Employee Center\nFacilitator Guide",
    subtitle="Workshop agenda, decision pre-fills, OOTB defense language, and common pitfalls for Sprint 2 Employee Center configuration",
    audience="ECS Lead Consultant, Solution Architect, Engagement Manager",
    companion_to="Sprint 2 EC Workbook · Employee Center Accelerator Pack (AP-15) · INT-FG-03 Catalog Facilitator Guide",
    doc_id="INT-FG-04", version="1.0", status="Released",
    running_header_label="Internal · Sprint 2 Employee Center Facilitator Guide",
), logo_path=LOGO)

doc2.add_cover_page(); doc2.page_break()

doc2.h1("How to Use This Guide", numbered=False)
doc2.para("This guide covers the Sprint 2 Employee Center configuration. Employee Center is the primary employee-facing surface — how it looks and works on day one shapes adoption for the entire engagement. The job in Sprint 2 is to configure a clean, navigable EC portal that showcases the catalog built in INT-FG-03. Keep branding decisions fast and portal structure decisions grounded in OOTB layouts.")
doc2.callout("Employee Center is the engagement's most visible deliverable. Customers judge the entire project by whether the portal looks professional and works on day one. Every hour spent configuring catalog structure pays off here. Every hour spent debating color schemes here is borrowed from configuration.")
doc2.page_break()

doc2.h1("Sprint Overview")
doc2.table(headers=["Item","Detail"], rows=[
    ["Sprint number","Sprint 2 of 6 (Month 2, Weeks 5-6), concurrent with Catalog & Request (INT-FG-03)"],
    ["Duration","2 weeks — EC workshops in Week 5; portal configuration Weeks 5-6; combined Catalog+EC demo in Week 6"],
    ["Primary discipline","Employee Center Pro — homepage layout, department taxonomy, topic taxonomy alignment, search configuration, and portal branding"],
    ["Sprint goal","A published Employee Center portal with the Sprint 2 catalog items visible, search returning accurate results, and portal branding matching the customer's standards"],
    ["Customer participants","Portal Owner, HR representative (for HR topic taxonomy), Comms/Marketing (for branding assets: logo, colors), IT Director (for demo signoff)"],
    ["ECS participants","Lead Consultant (facilitator), Solution Architect (EC configuration), Engagement Manager"],
    ["Key artifacts produced","Published EC portal (dev), Homepage layout decision (locked), Topic taxonomy (finalized), Search configuration (baseline), Branding assets (collected and applied)"],
    ["Critical dependency","Sprint 2 Catalog items must be published before EC portal can be properly validated. INT-FG-03 Workshop 2 decisions must be complete before INT-FG-04 Workshop 2."],
], col_widths_in=[2.4,7.0])
doc2.page_break()

doc2.h1("Workshop Agendas")
doc2.h2("Workshop 1 — Portal Structure and Topic Taxonomy (90 min)")
doc2.table(headers=["Time","Agenda Item","Facilitation Notes"], rows=[
    ["0:00–0:15","Employee Center Pro overview","Show the OOTB EC Pro homepage in the dev instance. Walk through the key components: Hero banner, Topic taxonomy tiles, Featured catalog items, and Search bar. Establish the frame: 'We are configuring a portal, not designing a website. The OOTB layouts are our starting point.'"],
    ["0:15–0:45","Topic taxonomy design","EC Pro organizes content around Topics, not departments. A Topic is an employee need ('I need help with my laptop') not an org unit ('IT Department'). Present the ECS-recommended topic taxonomy aligned to the catalog categories from INT-FG-03. Common pushback: 'We want a tile for each department.' Response: 'Employees don't think in departments — they think in needs. Research shows topic-based navigation reduces time-to-request by 40% compared to department-based navigation.'"],
    ["0:45–1:10","Homepage layout decision","Present the 3 OOTB homepage layout options. Recommendation: Layout B (Hero + 6-tile topic grid + featured items section). Ask for approval. The only branding inputs needed now: hero banner text, logo file, and primary brand color hex code."],
    ["1:10–1:25","Branding asset collection","Document what branding assets are needed and who provides them. Set a deadline: 48 hours before Workshop 2. Missing assets = placeholder branding at the demo. This is a customer deliverable."],
    ["1:25–1:30","Next steps","ECS to configure the homepage layout with placeholders. Customer to deliver branding assets."],
], col_widths_in=[1.0,2.6,5.8])

doc2.h2("Workshop 2 — Search, Featured Items, and Portal Validation (60 min)")
doc2.table(headers=["Time","Agenda Item","Facilitation Notes"], rows=[
    ["0:00–0:10","Branding assets applied","Show the portal with the customer's logo, colors, and hero banner. This is typically the moment customer confidence peaks — keep the momentum."],
    ["0:10–0:25","Search configuration","OOTB EC Pro search is powered by the Now Platform search engine. Configure the search scope: catalog items, knowledge articles (when Knowledge sprint is complete), and service catalog categories. Test 5 search queries the customer's employees would actually use. Adjust the search configuration if obvious terms return no results."],
    ["0:25–0:45","Featured items selection","Select the top 6 catalog items to feature on the homepage. These should be the highest-volume requests from the MVP list. The Portal Owner makes this decision."],
    ["0:45–0:55","End-to-end user journey test","Submit a test request through EC Pro end-to-end: find catalog item via search, submit request, confirm approval notification, confirm fulfillment task created. This is the demo journey."],
    ["0:55–1:00","Combined demo prep","Confirm the Sprint 2 combined demo (Catalog + EC) date and audience."],
], col_widths_in=[1.0,2.6,5.8])
doc2.page_break()

doc2.h1("Decision Pre-Fills — ECS Recommendations")
doc2.h2("Decision 1 — Portal Structure")
doc2.table(headers=["ECS Recommendation","Rationale","Common Pushback","ECS Response"], rows=[
    ["OOTB Employee Center Pro with standard homepage layouts. No custom Angular components or Service Portal widgets.",
     "Custom portal components require front-end developer skills to maintain. Every ServiceNow upgrade risks breaking custom components. OOTB EC Pro receives continuous UX improvements from ServiceNow — custom builds do not.",
     "'We want a custom homepage that matches our intranet design.'",
     "'Employee Center Pro is designed to complement intranets, not replace them. We can match your brand colors, logo, and language within the OOTB layout. A full intranet-match redesign is a Phase 2 project and requires front-end development resources that are outside this engagement scope.'"],
    ["Topic-based navigation aligned to catalog categories. Maximum 8 topic tiles on homepage.",
     "8 tiles is the maximum readable on a standard browser without scrolling. More tiles reduce discoverability of each individual topic.",
     "'We need a tile for every department — that is 15 departments.'",
     "'15 department tiles is a navigation problem for employees — where do I go for something that spans departments? Topic tiles represent employee needs, not reporting lines. Your 15 departments map to 6-8 employee need topics. We can show a department filter once the employee is inside a topic.'"],
], col_widths_in=[2.2,2.2,2.0,3.0])

doc2.page_break()
doc2.h1("Common Pitfalls")
for title, body in [
    ("Pitfall 1 — Branding Asset Delay",
     "The customer's comms team takes more than 48 hours to provide logo and color assets. The demo happens with placeholder branding and executives are unimpressed.\n\nPrevention: at Workshop 1, name a specific person who owns branding asset delivery and get their mobile number. If assets aren't delivered within 48 hours, use the customer's existing website logo (publicly available) as a placeholder and document the substitution."),
    ("Pitfall 2 — 'It Needs to Look Like SharePoint'",
     "The IT Director or CIO sees the portal and says it needs to match the existing intranet (SharePoint, Confluence, etc.) exactly. This is a scope change.\n\nRedirect: 'Matching SharePoint exactly requires custom front-end development outside our engagement scope. What we can match: your logo, your primary brand color, your font family if it's web-safe, and your content structure. The portal will be recognizably yours without being a pixel-perfect SharePoint clone. If an exact match is a requirement, that needs to be scoped as a Phase 2 change request.'"),
    ("Pitfall 3 — Catalog/EC Sync Gap",
     "The EC portal is configured before the catalog items from INT-FG-03 are fully published. The demo shows an empty portal or items with missing descriptions.\n\nPrevention: do not schedule the EC validation workshop until INT-FG-03 Workshop 2 catalog decisions are finalized and at least the top 10 items are configured. Track this dependency explicitly on the sprint plan."),
]; 
    doc2.h2(title); doc2.para(body)

doc2.h1("Sprint Demo Discipline")
doc2.h2("Pre-Demo Checklist")
doc2.table(headers=["#","Check","Owner","Status"], rows=[
    ["1","EC Pro portal published in dev with customer branding applied","ECS SA","☐"],
    ["2","Topic tiles displaying correct catalog items for each topic","ECS SA","☐"],
    ["3","Search returning top 6 expected catalog items for common search terms","ECS SA","☐"],
    ["4","End-to-end request journey tested: EC search → submit → approval → fulfillment","ECS SA","☐"],
    ["5","Mobile view tested (EC Pro is responsive — confirm it works on phone)","ECS Lead","☐"],
], col_widths_in=[0.4,5.8,1.4,1.0])

doc2.h1("Sprint Retro Template")
doc2.table(headers=["Category","Question","Capture Here"], rows=[
    ["What worked","What did the customer respond to most positively in the portal?",""],
    ["What worked","Which branding decisions went smoothly?",""],
    ["What didn't work","What customization requests came up that we had to push to Phase 2?",""],
    ["Sprint 3 readiness","Is Knowledge ready to configure in Sprint 3? Are there existing articles to review?",""],
    ["ECS learning","What would we do differently?",""],
], col_widths_in=[1.6,4.0,3.8])

doc2.save(OUT04)
print(f"INT-FG-04 built → {OUT04}")
