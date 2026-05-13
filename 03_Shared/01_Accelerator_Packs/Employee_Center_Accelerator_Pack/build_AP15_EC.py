"""Build AP-15 — Employee Center Accelerator Pack. Sprint 5."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from accelerator_pack_builder import TabContent, build_workbook
from ecs_template import EcsDocument, DocMeta

PACK_NAME = "Employee Center Accelerator Pack"

wb1 = TabContent(
    workbook_title="01 — EC Portal Design Decisions",
    pack_name=PACK_NAME,
    purpose="Defines the foundational Employee Center portal design decisions: single vs. multi-catalog, branding approach, navigation structure, and homepage layout. These decisions cascade into every subsequent EC configuration workbook and must be agreed before any portal build begins.",
    who_fills="ECS SA facilitates; Customer IT Director and HR representative approve the portal design. Communications or Marketing team provides branding inputs.",
    sprint_window="Sprint 5 Week 1",
    estimated_effort="2–3 hours (one design workshop)",
    related_workbooks=["02 Topic Taxonomy", "03 Homepage Layout", "Service Catalog Pack", "Knowledge Pack"],
    success_criteria=[
        "Multi-catalog vs. single-catalog decision made and documented.",
        "Portal branding (logo, primary color, font) confirmed by Communications/Marketing.",
        "Navigation structure agreed (top nav items and their order).",
        "Homepage sections and their content sources defined.",
        "Mobile optimization requirement confirmed (Employee Center is mobile-native).",
    ],
    process_decisions=[
        ("Should Employee Center use a single catalog or separate IT and HR catalogs?",
         "Separate catalogs if HR is in scope. OOTB Employee Center natively supports multi-catalog with a unified search experience. IT Catalog and HR Catalog display as separate topic groups on the homepage.",
         "Mixing IT and HR items in one catalog creates fulfillment routing complexity and confuses employees who expect different experiences for IT requests vs. HR transactions. Multi-catalog is the OOTB design pattern for Employee Center."),
        ("Should we use OOTB Employee Center branding or customise to match the corporate brand?",
         "Apply corporate primary color and logo using OOTB branding settings. Do not customise EC CSS or page layouts. OOTB themes are upgrade-safe; custom CSS breaks on every EC upgrade.",
         "Employee Center has an OOTB theming engine that handles color, logo, and font without touching CSS. Custom CSS applied outside the theme engine is overwritten by ServiceNow upgrades and requires remediation every release cycle."),
        ("What should appear in the top navigation of Employee Center?",
         "OOTB top nav items: Home, Catalog (or IT Services / HR Services if multi-catalog), Knowledge, My Requests, Approvals. Do not add custom nav items for MVP — the OOTB nav covers every user need.",
         "Custom top nav items require portal widget customisation. The OOTB nav is well-understood by employees from other ServiceNow deployments and requires no training. Additions should be driven by post-launch analytics, not assumptions."),
        ("Should Employee Center be the single entry point or coexist with a legacy portal?",
         "Employee Center as the single entry point. Redirect legacy portal URLs to EC on go-live. Dual-portal operation creates user confusion and doubles the maintenance burden.",
         "Customers who run EC alongside a legacy portal for a 'transition period' typically end up with both portals active indefinitely as the cutover deadline slips. Set a hard cutover date on go-live day."),
    ],
    dependencies=[
        ("Service Catalog category structure (Catalog Pack Workbook 01)", "Required", "ECS SA", "Sprint 4", "EC homepage topic groups mirror catalog categories."),
        ("Knowledge Base structure (Knowledge Pack Workbook 01)", "Required", "ECS SA", "Sprint 5 Wk 1", "EC homepage surfaces KB articles."),
        ("Corporate brand guidelines (logo, primary colour, font)", "Required", "Customer Communications", "Sprint 5 Wk 1", ""),
        ("HR catalog scope decision", "Required", "Customer HR Director", "Sprint 5 Wk 1", "Determines single vs. multi-catalog architecture."),
    ],
    config_sections=[
        ("Portal Architecture", [
            ("Catalog architecture", "[Single catalog / Multi-catalog (IT + HR)]", "Multi-catalog recommended if HR is in scope.", True),
            ("Legacy portal cutover date", "[Go-live date — redirect legacy portal on this date]", "Hard cutover, no dual-portal period.", True),
            ("Mobile optimization", "Yes — OOTB (Employee Center is mobile-native)", "No additional configuration required.", False),
        ]),
        ("Branding Configuration", [
            ("Portal name", "[Customer to complete — e.g., 'IT Support Center']", "", True),
            ("Primary color (hex)", "[Customer: corporate primary color]", "Applied to header, buttons, and nav highlights.", True),
            ("Logo file", "[Customer: PNG, 200x60px recommended]", "Upload in EC Branding settings.", True),
            ("Font", "[Customer: corporate font or 'default OOTB']", "OOTB font is clean and accessible. Custom fonts require font file upload.", True),
        ]),
        ("Top Navigation", [
            ("Nav item 1", "Home", "OOTB — do not rename.", False),
            ("Nav item 2", "IT Services (or Catalog if single)", "Rename to match catalog name.", True),
            ("Nav item 3 (if multi-catalog)", "HR Services", "Only if HR catalog is in scope.", True),
            ("Nav item 4", "Knowledge", "OOTB — links to Employee Self-Service KB.", False),
            ("Nav item 5", "My Requests", "OOTB — shows user's open requests and approvals.", False),
        ]),
    ],
    raci_rows=[
        ("Facilitate EC design workshop", "R/A", "C", "ECS SA."),
        ("Provide corporate branding assets", "I", "R/A", "Customer Communications/Marketing."),
        ("Approve portal architecture and navigation", "I", "R/A", "Customer IT Director + HR Director."),
        ("Configure EC branding in ServiceNow", "R/A", "I", "ECS SA."),
        ("Configure navigation structure", "R/A", "I", "ECS SA."),
        ("Set redirect from legacy portal to EC", "R/A", "C", "ECS SA configures; customer web team assists if URL is external."),
    ],
    consultant_guide_sections=[
        ("The dual-portal trap", "The most common EC deployment failure is running Employee Center alongside a legacy Service Portal indefinitely. Customers promise a 'parallel run for 4 weeks' that stretches to 12 months. Set a hard cutover date: Employee Center launches on Day X, the legacy portal redirects to EC on Day X. There is no parallel run. Communicate this to the customer in Sprint 5 Week 1 so they can plan their user communications."),
        ("Branding scope management", "Customers frequently want to match Employee Center exactly to their corporate intranet — custom fonts, custom page layouts, custom widgets. Set the boundary early: OOTB theming handles color, logo, and font. Everything beyond that is a customisation that requires upgrade maintenance. A simple question to ask: 'Is the portal for IT self-service or a brand showcase?' The answer is always self-service."),
    ],
    adoption_rows=[
        ("We want to heavily customise the EC portal layout and widgets",
         "Apply OOTB branding (color, logo, font). Use OOTB homepage sections and widgets.",
         "Custom EC widgets and layouts are overwritten by every ServiceNow upgrade. The OOTB EC layout is the result of extensive UX research — it performs well without customisation.",
         "'Every custom widget you add is a widget we need to re-test after every ServiceNow upgrade — typically 3 times a year. The OOTB EC layout performs well out of the box. Let us launch with OOTB and use actual analytics from your users to justify any specific customisations. That way the customisation budget goes where it actually matters.'",
         "Custom widgets are acceptable for genuinely unique content types (e.g., an IT health status dashboard embedded on the EC homepage). Scope explicitly and plan for upgrade maintenance."),
    ],
    snmap_sections=[
        ("Employee Center Configuration", [
            ("EC Portal", "sn_hr_sp_portal", "Employee Center portal record."),
            ("EC Branding", "Employee Center > Administration > Branding", "Configure color, logo, and font here."),
            ("EC Navigation", "Employee Center > Administration > Navigation", "Configure top nav items and order."),
            ("Multi-catalog", "Service Catalog > Catalogs", "One record per catalog. EC surfaces all active catalogs."),
        ]),
    ],
)

wb2 = TabContent(
    workbook_title="02 — Topic Taxonomy",
    pack_name=PACK_NAME,
    purpose="Defines the Employee Center Topic structure — the browsable topic groups on the EC homepage and topic pages. Topics in EC are the user-facing equivalent of Service Catalog categories, but they also surface Knowledge articles and Virtual Agent topics. Aligning the EC topic taxonomy with the Catalog and KB category structures is the key configuration decision for Employee Center.",
    who_fills="ECS SA designs the topic taxonomy based on Catalog and KB categories; customer ITSM Process Owner approves.",
    sprint_window="Sprint 5 Week 1",
    estimated_effort="1–2 hours",
    related_workbooks=["01 EC Design Decisions", "Service Catalog Pack — Category Rationalization", "Knowledge Pack — KB Structure"],
    success_criteria=[
        "EC Topic taxonomy mirrors the Service Catalog category structure.",
        "Each Topic has a named icon and short description.",
        "Topic pages show the correct catalog items and KB articles.",
        "No more than 6 top-level topics for the IT catalog.",
    ],
    process_decisions=[
        ("Should EC Topics exactly mirror Catalog categories or have a different structure?",
         "EC Topics should mirror the Catalog category names exactly. Deviating creates a disconnect: a user who browses the Catalog sees 'IT Equipment'; the same user on the EC homepage sees 'Hardware' and doesn't recognise the connection.",
         "Consistent taxonomy across EC, Catalog, and Knowledge is the OOTB Employee Center design intent. Virtual Agent also uses topic names for intent matching — inconsistency creates intent recognition failures."),
        ("What content appears on each EC Topic page?",
         "OOTB Topic page shows: popular catalog items in that topic, featured knowledge articles in that topic's KB category, and a search bar scoped to that topic. Configure using OOTB EC Topic page settings — no custom widgets required.",
         "The OOTB Topic page content is driven by catalog item popularity (view count) and knowledge article featured flag. Both are configurable without customisation."),
    ],
    dependencies=[
        ("Catalog category structure approved (Sprint 4)", "Required", "ECS SA", "Sprint 4", "Topics must match categories."),
        ("KB categories configured (Knowledge Pack)", "Required", "ECS SA", "Sprint 5 Wk 1", ""),
    ],
    config_sections=[
        ("EC Topic Definitions", [
            ("Topic 1 — Name", "IT Equipment", "Matches Catalog category name exactly.", False),
            ("Topic 1 — Icon", "[Customer: select from OOTB icon library]", "", True),
            ("Topic 1 — Short description", "[Customer: 1 sentence describing what users find here]", "", True),
            ("Topic 2 — Name", "Software & Licensing", "", False),
            ("Topic 2 — Icon", "[Customer: select from OOTB icon library]", "", True),
            ("Topic 3 — Name", "Access & Security", "", False),
            ("Topic 3 — Icon", "[Customer: select from OOTB icon library]", "", True),
            ("Topic 4 — Name", "Infrastructure Services", "", False),
            ("Topic 4 — Icon", "[Customer: select from OOTB icon library]", "", True),
            ("Topic 5 — Name", "HR & Onboarding", "", False),
            ("Topic 5 — Icon", "[Customer: select from OOTB icon library]", "", True),
            ("Topic 6 — Name", "General Requests", "", False),
            ("Topic 6 — Icon", "[Customer: select from OOTB icon library]", "", True),
        ]),
        ("Topic Page Content", [
            ("Popular items source", "OOTB: most-viewed catalog items in that category (auto)", "No configuration required.", False),
            ("Featured articles", "Flag articles as 'Featured' in each KB category", "Featured flag on kb_knowledge record.", False),
            ("Topic search scope", "OOTB: scoped to topic's catalog category + KB category", "No configuration required.", False),
        ]),
    ],
    raci_rows=[
        ("Design EC topic taxonomy", "R/A", "C", "ECS SA; customer approves."),
        ("Select icons and write topic descriptions", "C", "R/A", "Customer ITSM PO selects icons; ECS SA configures."),
        ("Configure EC topics in ServiceNow", "R/A", "I", "ECS SA."),
        ("Flag featured KB articles per topic", "C", "R/A", "Customer KMs flag articles; ECS SA validates display."),
    ],
    consultant_guide_sections=[("Topic icon selection", "OOTB EC has a large icon library. Let the customer choose icons — it takes 20 minutes and gives them ownership of the portal. More importantly, icons chosen by the customer tend to make more intuitive sense to their employees than icons chosen by the consultant. Schedule this as a 20-minute screen-share session in Sprint 5 Week 1.")],
    adoption_rows=[("We want different topic names than our catalog categories", "Use identical names. Taxonomy consistency across EC, Catalog, and Knowledge is non-negotiable for search and VA.", "Inconsistent names fragment user mental models and break Virtual Agent intent matching.", "'If your catalog says IT Equipment and your EC homepage says Hardware, users who navigate from EC to the catalog are in unfamiliar territory. Consistency is the single biggest usability win in portal design — it costs nothing and improves every user interaction.'", "Never. If the customer wants different names, change both catalog and EC simultaneously.")],
    snmap_sections=[("EC Topic Tables", [("EC Topic", "sn_hr_sp_topic", "Employee Center topic record."), ("Topic Category Link", "sn_hr_sp_topic_category", "Links EC topic to catalog category and KB category."), ("Featured Article", "kb_knowledge.featured", "Flag to surface articles on EC topic page.")])],
)

wb3 = TabContent(
    workbook_title="03 — Homepage Layout & Content Blocks",
    pack_name=PACK_NAME,
    purpose="Defines the Employee Center homepage layout: which OOTB content blocks appear, in what order, and what content they surface. The homepage is the first thing every employee sees when they visit the portal — it must communicate value immediately and route users to the right place in two clicks.",
    who_fills="ECS SA designs the layout; Customer IT Director approves. Communications team provides any featured announcement content.",
    sprint_window="Sprint 5 Week 1–2",
    estimated_effort="2 hours (layout design + content block configuration)",
    related_workbooks=["01 EC Design Decisions", "02 Topic Taxonomy"],
    success_criteria=[
        "Homepage uses only OOTB content blocks (no custom widgets).",
        "Homepage loads in under 3 seconds (validate in non-prod).",
        "Hero section has a clear CTA (search bar is always prominent).",
        "Announcements block is configured and the first announcement is drafted.",
        "Popular items block surfaces the top 5 catalog items by volume.",
    ],
    process_decisions=[
        ("What OOTB homepage blocks should be included at MVP?",
         "Recommended OOTB homepage blocks in order: (1) Hero with search bar, (2) Topic tiles (6 topics), (3) Popular catalog items, (4) Announcements/Featured news, (5) Recent items (user's recent requests). Do not add more blocks at MVP.",
         "Five blocks is the OOTB maximum for a homepage that loads quickly and does not overwhelm users. Analytics from the first 60 days post-launch should drive any additions — not assumptions."),
        ("Should we show personalized content on the homepage?",
         "Yes — use OOTB personalisation: 'Recent Items' shows the user's recent requests and approvals. 'Recommended Items' shows catalog items popular with similar users. Both are OOTB and require no configuration.",
         "OOTB personalisation drives repeat usage. Users who see their recent requests on the homepage return to check status more often than users who have to navigate to My Requests. This reduces 'where is my request?' helpdesk calls."),
        ("Who manages homepage announcements?",
         "Assign a named announcement manager (ITSM Process Owner or Communications representative). Use the OOTB Announcement record with start/end dates — announcements automatically appear and disappear without manual intervention.",
         "Announcements without end dates accumulate on the homepage and eventually become noise that users ignore. OOTB start/end dates are the self-cleaning mechanism for announcements."),
    ],
    dependencies=[("EC branding configured (Workbook 01)", "Required", "ECS SA", "Sprint 5 Wk 1", ""), ("EC topics configured (Workbook 02)", "Required", "ECS SA", "Sprint 5 Wk 1", "")],
    config_sections=[
        ("Homepage Block Configuration", [
            ("Block 1 — Hero with search", "OOTB Hero block — search bar centered, tagline text", "Configure tagline text to match portal name.", True),
            ("Block 1 — Tagline text", "[Customer to complete — e.g., 'How can we help you today?']", "", True),
            ("Block 2 — Topic tiles", "OOTB Topic Tiles block — shows 6 EC topics", "Topics from Workbook 02.", False),
            ("Block 3 — Popular items", "OOTB Popular Items block — top 5 by view count", "Auto-populated from catalog usage data.", False),
            ("Block 4 — Announcements", "OOTB Announcement block — active announcements with dates", "", False),
            ("Block 5 — Recent items", "OOTB Recent Items — user's last 5 requests/approvals", "Personalised. No configuration needed.", False),
        ]),
        ("Announcement Configuration", [
            ("Announcement manager", "[Customer to complete]", "Named individual responsible for announcements.", True),
            ("First announcement (for go-live)", "[Customer to draft — EC launch announcement]", "Announce the new portal to employees. Include link to KB article explaining how to use it.", True),
            ("Default announcement duration", "30 days maximum", "All announcements must have an end date.", False),
            ("Announcement approval", "Announcement manager approves before publish", "No workflow needed — KM/AM publishes directly.", False),
        ]),
    ],
    raci_rows=[
        ("Design homepage block layout", "R/A", "C", "ECS SA designs; customer IT Director approves."),
        ("Write homepage tagline text", "C", "R/A", "Customer Communications."),
        ("Configure OOTB homepage blocks", "R/A", "I", "ECS SA."),
        ("Draft go-live announcement", "C", "R/A", "Customer ITSM PO or Communications."),
        ("Validate homepage load time in non-prod", "R/A", "I", "ECS SA."),
        ("Assign announcement manager", "I", "R/A", "Customer IT Director."),
    ],
    consultant_guide_sections=[
        ("Homepage performance", "Validate homepage load time in non-prod before go-live. A homepage that takes more than 4 seconds to load will see immediate user abandonment. The OOTB 5-block homepage is designed for performance. If load time is slow, check: (1) are there large image files in the hero block? (2) are there custom widgets from a previous developer? Remove them. OOTB blocks are optimized; custom widgets often are not."),
        ("The go-live announcement", "Draft the go-live announcement for the customer — they rarely have time to do it themselves. A good go-live announcement covers: 'Starting [date], you can submit all IT requests at [EC URL]. You can also find answers in our new Knowledge Base. Your previous requests are visible under My Requests.' That is all it needs. Send it from the IT Director's email and pin it for 30 days."),
    ],
    adoption_rows=[
        ("We want a custom branded hero banner with animated graphics",
         "Use OOTB Hero block with corporate color and logo. No custom animations.",
         "Custom animations require CSS/JavaScript widgets that break on upgrade and slow page load. The OOTB hero block with the corporate color and logo provides clear branding without the maintenance cost.",
         "'A clean, fast portal with the right color and logo makes a better first impression than a slow, animated one. Your employees will visit this portal multiple times a day — they care about finding things quickly, not the animation. Let us launch clean and fast; if the analytics show users spending time on the homepage rather than clicking through, we can revisit the design then.'",
         "Never animated hero widgets. Static custom hero images (replacing the OOTB background color) are acceptable if provided by Communications in the correct format."),
    ],
    snmap_sections=[
        ("Homepage Configuration", [("EC Homepage", "Employee Center > Administration > Homepage", "Configure blocks and their order here."), ("Announcement", "sn_hr_sp_announcement", "OOTB announcement record. Include start_date and end_date."), ("EC Theme", "Employee Center > Administration > Branding", "Hero color and text configured here.")])
    ],
)

wb4 = TabContent(
    workbook_title="04 — Search Configuration",
    pack_name=PACK_NAME,
    purpose="Defines the Employee Center unified search configuration: which content types are indexed, search result ranking, and the 'No results' experience. EC search is the primary way most employees find what they need — it must search across catalog items, KB articles, and EC topics simultaneously.",
    who_fills="ECS SA configures; customer ITSM PO validates search results for the top 10 expected queries.",
    sprint_window="Sprint 5 Week 2",
    estimated_effort="2 hours",
    related_workbooks=["02 Topic Taxonomy", "Knowledge Pack — Search Optimization"],
    success_criteria=[
        "EC search indexes: catalog items, KB articles, EC topics.",
        "Top 10 expected search queries return relevant results.",
        "No results experience includes a 'Submit a request' fallback.",
        "Search analytics reporting is configured.",
    ],
    process_decisions=[
        ("What content types should EC search return?", "OOTB EC search returns: catalog items (sc_cat_item), knowledge articles (kb_knowledge), and EC topics (sn_hr_sp_topic). All three are indexed by default. Do not restrict search to a single content type.", "Restricting EC search to catalog items only means users who search for a knowledge article get no results and call the helpdesk. The three-content-type search is the OOTB design and handles the full user journey."),
        ("What should the 'No results found' experience show?", "OOTB: 'No results found' page includes a prominent 'Submit a request' button that opens the General Requests catalog item. Configure this before go-live — it converts search failures into catalog submissions rather than helpdesk calls.", "Every search that returns no results is a user who is about to call the helpdesk. The OOTB no-results fallback to 'Submit a request' captures that intent in the catalog instead."),
    ],
    dependencies=[("EC topics configured (Workbook 02)", "Required", "ECS SA", "Sprint 5 Wk 1", ""), ("KB articles published (Knowledge Pack)", "Required", "Customer KMs", "Sprint 5 Wk 2", "Search returns no KB results until articles are published.")],
    config_sections=[
        ("Search Source Configuration", [
            ("Catalog items indexed", "Yes — OOTB sc_cat_item search source", "", False),
            ("Knowledge articles indexed", "Yes — OOTB kb_knowledge search source", "", False),
            ("EC topics indexed", "Yes — OOTB sn_hr_sp_topic search source", "", False),
            ("Search result ranking", "OOTB: catalog items rank above KB for transactional queries; KB ranks above catalog for informational queries", "No configuration needed — OOTB ranking algorithm.", False),
            ("No-results fallback", "OOTB 'No results' page with Submit a Request CTA", "Configure CTA to open General Requests catalog item.", True),
        ]),
        ("Search Validation Queries (top 10)", [
            ("Query 1", "[Customer: most common helpdesk request type]", "Expected result: catalog item", True),
            ("Query 2", "[Customer: second most common request]", "", True),
            ("Query 3", "[Customer: common password/access issue]", "Expected result: KB article or catalog item", True),
            ("Queries 4–10", "[Customer ITSM PO to provide remaining 7 queries]", "Validate all 10 before go-live.", True),
        ]),
    ],
    raci_rows=[
        ("Configure EC search sources", "R/A", "I", "ECS SA."),
        ("Configure no-results fallback", "R/A", "I", "ECS SA."),
        ("Provide top 10 test search queries", "I", "R/A", "Customer ITSM PO."),
        ("Validate search results for all 10 queries", "R/A", "C", "ECS SA tests; customer confirms results are correct."),
        ("Configure search analytics reporting", "R/A", "I", "ECS SA."),
    ],
    consultant_guide_sections=[("Post-launch search analytics", "Configure OOTB EC search analytics before go-live. The first 30 days of search analytics are the most valuable dataset in the engagement: what users search for, what results they click, and where they give up. This data drives: (1) synonym additions to the KB search, (2) new catalog item prioritisation, and (3) VA topic additions. Review search analytics at the Sprint 6 planning session.")],
    adoption_rows=[("We want to exclude KB articles from EC search so users only see catalog items", "Keep all three content types in EC search.", "Excluding KB from EC search forces users who could self-serve with a knowledge article to submit a catalog request instead — increasing fulfillment workload for no benefit.", "'If a user searches for how to reset their password and we only show catalog items, they submit a request. If we also show the KB article, they self-serve in 2 minutes and the helpdesk doesn't get the ticket. Every KB article that surfaces in search is a potential deflection.'", "Never restrict EC search to a single content type.")],
    snmap_sections=[("Search Configuration", [("EC Search Source", "sp_search_source", "Configured per content type in Service Portal > Search Sources."), ("Search Analytics", "Employee Center > Administration > Search Analytics", "OOTB analytics for EC searches — what users searched, what they clicked.")])],
)

wb5 = TabContent(
    workbook_title="05 — Adoption Measurement & Go-Live Plan",
    pack_name=PACK_NAME,
    purpose="Defines the go-live communications plan for Employee Center and the KPIs that will be used to measure adoption in the first 90 days. Employee Center adoption is not automatic — it requires deliberate communication, user training, and helpdesk direction. This workbook ensures those activities happen.",
    who_fills="ECS SA provides the framework; Customer ITSM Process Owner and Communications team execute the communications plan.",
    sprint_window="Sprint 5 Week 2",
    estimated_effort="2 hours",
    related_workbooks=["01 EC Design Decisions", "Knowledge Pack — Knowledge KPIs"],
    success_criteria=[
        "Go-live announcement is drafted and approved.",
        "Helpdesk team has been briefed to direct callers to Employee Center.",
        "A KB article explaining 'How to use Employee Center' is published.",
        "90-day adoption KPI targets are agreed with IT Director.",
        "Monthly adoption review is scheduled.",
    ],
    process_decisions=[
        ("What are the primary adoption KPIs for Employee Center?", "Three KPIs: (1) Self-service submission rate — % of requests submitted via EC vs. phone/email/walk-up. (2) Search-to-submission rate — % of searches that result in a submission without helpdesk contact. (3) Return visit rate — % of users who use EC more than once in 30 days.", "These three KPIs measure different aspects of adoption: that users know EC exists (self-service rate), that search is working (search-to-submission), and that users found value and returned (return visit). Together they provide a complete adoption picture."),
        ("What is a realistic 90-day self-service submission rate target?", "20–30% of total request volume submitted via EC within 90 days of go-live. This is achievable without mandatory enforcement. Targets above 50% in the first 90 days require either mandatory enforcement or an exceptionally well-adopted portal.", "20–30% in 90 days is a realistic OOTB target based on mid-market deployments. It assumes: all IT staff directing users to EC, EC link on the intranet homepage, and go-live announcement to all employees."),
    ],
    dependencies=[("EC portal fully configured and tested", "Required", "ECS SA", "Sprint 5 Wk 2", "Cannot go live without a complete portal."), ("KB article: 'How to use Employee Center' published", "Required", "Customer KM", "Sprint 5 Wk 2", "Users need a self-service guide for the self-service portal.")],
    config_sections=[
        ("Go-Live Communications Plan", [
            ("Announcement medium", "[Customer: email / intranet / Teams / all-hands]", "", True),
            ("Announcement author", "[Customer: IT Director or CIO — send from leadership]", "Leadership-sent announcements have higher open rates.", True),
            ("Announcement send date", "[Go-live date]", "", True),
            ("EC URL to communicate", "[Customer: ServiceNow instance URL / custom vanity URL]", "If vanity URL, confirm DNS before go-live.", True),
            ("Helpdesk briefing date", "[Before go-live — brief IT staff to direct callers to EC]", "", True),
            ("Intranet homepage link", "[Customer: add EC URL to intranet homepage before go-live]", "Single highest-impact adoption action.", True),
        ]),
        ("Adoption KPI Targets", [
            ("Self-service submission rate (90 days)", "[Customer: target % — recommended 20-30%]", "", True),
            ("Search-to-submission rate (90 days)", "[Customer: target % — recommended >40%]", "", True),
            ("Return visit rate (30 days)", "[Customer: target % — recommended >60%]", "", True),
            ("Monthly adoption review owner", "[Customer: ITSM Process Owner]", "", True),
            ("KPI reporting source", "Employee Center > Analytics dashboard (OOTB)", "", False),
        ]),
    ],
    raci_rows=[
        ("Draft go-live announcement", "C", "R/A", "Customer Communications/ITSM PO drafts; ECS SA reviews for accuracy."),
        ("Brief helpdesk team on EC and URL", "I", "R/A", "Customer IT Ops Lead briefs helpdesk team."),
        ("Add EC link to intranet homepage", "I", "R/A", "Customer intranet/web team."),
        ("Publish 'How to use Employee Center' KB article", "C", "R/A", "Customer KM authors; ECS SA reviews template compliance."),
        ("Configure OOTB EC analytics dashboard", "R/A", "I", "ECS SA."),
        ("Run first 30-day adoption review", "C", "R/A", "Customer ITSM PO runs; ECS SA advises on findings."),
    ],
    consultant_guide_sections=[
        ("The intranet homepage link", "The single highest-ROI adoption action is adding the Employee Center URL to the corporate intranet homepage. It costs nothing, takes 5 minutes of the web team's time, and surfaces the portal to every employee who opens their browser to the intranet. Confirm this is in the customer's go-live plan — not as an aspiration but as a committed action with an owner and a date."),
        ("Helpdesk as EC ambassadors", "Brief the helpdesk team before go-live with one simple instruction: when a user calls for anything submittable in the catalog, say 'Let me show you how to submit that in Employee Center — it is faster and you can track the status.' One successful EC submission converts a user. The helpdesk team creates more EC adoptions per day than any marketing campaign."),
    ],
    adoption_rows=[
        ("We will train employees to use EC before go-live",
         "Do not invest in training — invest in communications and helpdesk direction. Employee Center requires no training.",
         "Training sessions for a self-service portal are a sign that the portal is not intuitive enough. An OOTB EC portal with good search should require no training — users find it and use it within 2 minutes. If users need training to use the portal, the portal needs redesign, not training.",
         "'Employee Center is designed to be used without training — like Google or Amazon. If your employees can buy something on Amazon, they can submit an IT request on Employee Center. What they need is to know it exists (go-live announcement) and where to find it (intranet link). Training is for complex tools; EC is designed to be intuitive.'",
         "One-page 'how to use EC' guide (or KB article) is appropriate for the first announcement. No classroom or video training."),
    ],
    snmap_sections=[
        ("EC Analytics", [("EC Usage Analytics", "Employee Center > Administration > Analytics", "Submission rates, search analytics, popular items — all OOTB."), ("Deflection Metric", "incident.knowledge_accessed", "Tracks KB article views before incident submission — measure of EC-driven deflection.")])
    ],
)

def build_readme(out_path):
    doc = EcsDocument(meta=DocMeta(
        eyebrow="ACCELERATOR PACK", title="Employee Center\nAccelerator Pack",
        subtitle="Portal design, topic taxonomy, homepage layout, search, and adoption measurement for the OOTB-first Employee Center deployment",
        org="ECS Federal · ServiceNow Practice",
        audience="Customer IT Director, ITSM Process Owner, HR Director (if HR in scope), and Communications team",
        companion_to="Service Catalog Pack · Knowledge Pack · Virtual Agent Pack",
        doc_id="AP-15", version="1.0", status="Released",
        confidentiality="Shared — for the recipient and their organisation",
        running_header_label="Employee Center Accelerator Pack · ECS Federal",
    ))
    doc.add_cover_page(); doc.add_page_break()
    doc.h1("What This Pack Is", numbered=False)
    doc.para("This Accelerator Pack covers the complete Employee Center configuration for Sprint 5. Employee Center is the unified self-service portal that surfaces the Service Catalog, Knowledge Base, and Virtual Agent in a single, mobile-native experience. It is the user-facing payoff of the Sprint 4 catalog and Sprint 5 knowledge investments.")
    doc.para("The five workbooks address the full EC implementation sequence: foundational design decisions (Workbook 01), topic taxonomy aligned to the catalog and KB (Workbook 02), homepage layout and content blocks (Workbook 03), unified search configuration (Workbook 04), and go-live communications and adoption measurement (Workbook 05).")
    doc.h1("The Five Workbooks", numbered=False)
    doc.table(headers=["#", "Workbook", "What It Covers", "Owner", "Sprint"],
        rows=[
            ["01","EC Portal Design Decisions","Multi-catalog vs single, branding, navigation structure, legacy portal cutover","ECS SA + Customer IT Director","Sprint 5 Wk 1"],
            ["02","Topic Taxonomy","EC topic structure aligned to catalog categories and KB categories; topic icons and descriptions","ECS SA + Customer ITSM PO","Sprint 5 Wk 1"],
            ["03","Homepage Layout & Content Blocks","OOTB homepage blocks, order, tagline, announcements, go-live announcement draft","ECS SA + Customer Communications","Sprint 5 Wks 1–2"],
            ["04","Search Configuration","Search sources, result ranking, no-results fallback, search validation","ECS SA","Sprint 5 Wk 2"],
            ["05","Adoption Measurement & Go-Live Plan","Go-live communications, helpdesk briefing, intranet link, 90-day KPI targets","ECS SA + Customer ITSM PO + Communications","Sprint 5 Wk 2"],
        ])
    doc.h1("Sprint Alignment", numbered=False)
    doc.para("Employee Center is configured in Sprint 5 alongside Knowledge Management and Virtual Agent. The three are interdependent: EC surfaces the Knowledge Base articles configured in the Knowledge Pack, and Virtual Agent (when in scope) launches from the EC portal. All three must be configured and tested together before Sprint 5 go-live.")
    doc.save(out_path); print(f"README saved: {out_path}")

if __name__ == "__main__":
    OUT = HERE
    print("Building Employee Center Accelerator Pack...")
    for content, fname in [(wb1,"01_ec_portal_design.xlsx"),(wb2,"02_topic_taxonomy.xlsx"),(wb3,"03_homepage_layout.xlsx"),(wb4,"04_search_configuration.xlsx"),(wb5,"05_adoption_measurement.xlsx")]:
        build_workbook(content, os.path.join(OUT, fname)); print(f"  ✓ {fname}")
    build_readme(os.path.join(OUT, "00_README_Employee_Center_Pack.docx"))
    print("\nEmployee Center Accelerator Pack complete.")
