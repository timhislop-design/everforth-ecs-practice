"""Build AP-13 — Knowledge Accelerator Pack. Sprint 5."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from accelerator_pack_builder import TabContent, build_workbook
from ecs_template import EcsDocument, DocMeta

PACK_NAME = "Knowledge Accelerator Pack"

wb1 = TabContent(
    workbook_title="01 — Knowledge Base Structure",
    pack_name=PACK_NAME,
    purpose="Defines the Knowledge Base hierarchy: which KBs to create, their categories, audience, and ownership. OOTB ServiceNow supports multiple Knowledge Bases — the recommended pattern is one KB per distinct audience (IT Staff, All Employees, HR). This workbook sets the structure before any articles are authored.",
    who_fills="Customer ITSM Process Owner and Knowledge Manager. ECS SA facilitates.",
    sprint_window="Sprint 5 Week 1",
    estimated_effort="2–3 hours",
    related_workbooks=["02 Article Template Standards", "03 Access Controls", "Service Catalog Pack — Category Rationalization"],
    success_criteria=[
        "Knowledge Bases defined with owner, audience, and category structure.",
        "Maximum 3 Knowledge Bases at MVP (IT Staff, All Employees, optional HR).",
        "Each KB has a named Knowledge Manager.",
        "Category structure aligns with Service Catalog categories where applicable.",
    ],
    process_decisions=[
        ("How many Knowledge Bases should we create at MVP?", "Three maximum: IT Staff KB (internal procedures, runbooks), Employee Self-Service KB (how-to articles for end users), and optionally an HR KB if HR is in scope.", "More than three KBs at MVP creates content silos and complicates search. The OOTB KB search searches all KBs the user has access to — separation is by audience, not by topic."),
        ("Should Knowledge Base categories mirror Service Catalog categories?", "Yes where the KB is user-facing. Employee Self-Service KB categories should mirror the Service Catalog category structure so users experience consistent navigation between catalog and knowledge.", "Consistent taxonomy between catalog and knowledge reduces cognitive load and improves Virtual Agent intent matching, which uses both catalog and knowledge data."),
        ("Who is the Knowledge Manager for each KB?", "Assign a named individual — not a group — as Knowledge Manager per KB. The KM is accountable for article quality, review cycles, and retirement of stale articles.", "Group ownership of a KB means no single person responds when articles become stale. The KM role is 2–3 hours per month for a well-maintained KB."),
    ],
    dependencies=[
        ("Service Catalog category structure (Catalog Pack Workbook 01)", "Recommended", "ECS SA", "Sprint 4", "Align KB categories with Catalog categories for consistent user navigation."),
        ("Virtual Agent topic list (VA Pack, if VA is in scope)", "Recommended", "ECS SA", "Sprint 5", "VA topics link to KB articles — category alignment simplifies VA configuration."),
        ("Foundation Data Pack — Users (for KB Managers)", "Required", "ECS SA", "Sprint 0", "KB Managers must be active user records."),
    ],
    config_sections=[
        ("Knowledge Base Definitions", [
            ("KB 1 — Name", "IT Staff Knowledge Base", "", False),
            ("KB 1 — Audience", "IT Staff only (user criteria restriction)", "", False),
            ("KB 1 — Knowledge Manager", "[Customer to complete]", "", True),
            ("KB 1 — Categories (MVP)", "Incident Procedures; Change Management; Platform Administration; Asset Management", "", True),
            ("KB 2 — Name", "Employee Self-Service", "", False),
            ("KB 2 — Audience", "All employees", "", False),
            ("KB 2 — Knowledge Manager", "[Customer to complete]", "", True),
            ("KB 2 — Categories (MVP)", "IT Equipment; Software & Access; Troubleshooting; Onboarding", "", True),
            ("KB 3 — Name", "HR Knowledge Base (if HR in scope)", "", False),
            ("KB 3 — Audience", "All employees / HR staff only", "Restrict sensitive policy content to HR staff using article-level user criteria.", True),
            ("KB 3 — Knowledge Manager", "[Customer to complete]", "", True),
        ]),
    ],
    raci_rows=[
        ("Define KB structure and categories", "R/A", "C", "ECS SA designs; customer confirms audience and naming."),
        ("Assign Knowledge Managers", "I", "R/A", "Customer ITSM Process Owner assigns."),
        ("Configure KBs in ServiceNow", "R/A", "I", "ECS SA configures."),
        ("Populate initial article set (MVP — 10 articles per KB)", "C", "R/A", "Customer Knowledge Managers author; ECS SA reviews for template compliance."),
    ],
    consultant_guide_sections=[
        ("MVP article count", "Set a realistic MVP article target: 10 articles per KB. Articles that are half-written are worse than no articles — they undermine trust in the KB. Better to launch with 10 excellent articles per KB than 50 draft-quality ones."),
        ("Aligning KB and catalog taxonomy", "During the Sprint 5 KB setup, revisit the Service Catalog category structure from Sprint 4. If categories were adjusted during catalog build, the KB category structure must be updated to match. Misalignment between catalog and knowledge categories confuses users and breaks Virtual Agent's intent-to-knowledge linking."),
    ],
    adoption_rows=[
        ("We want one giant KB for everything", "Create separate KBs by audience. IT Staff should not see draft runbooks when searching as an end user.", "Mixing IT internal content with employee self-service content creates search noise and confidentiality risks. OOTB user criteria on KBs handle this cleanly.", "'One KB sounds simpler, but your IT staff will search and get employee how-to articles mixed with their runbooks. And employees will occasionally find IT procedures that don't make sense to them. Two KBs with the right access controls gives everyone a clean search experience.'", "Only for very small IT teams (<5) with no internal procedures that should be restricted from employees."),
    ],
    snmap_sections=[
        ("Knowledge Tables", [("Knowledge Base", "kb_knowledge_base", "One record per KB."), ("KB Category", "kb_category", "Categories within each KB."), ("Knowledge Article", "kb_knowledge", "Individual articles. References kb_knowledge_base.")]),
    ],
)

wb2 = TabContent(
    workbook_title="02 — Article Template Standards",
    pack_name=PACK_NAME,
    purpose="Defines the OOTB article templates — the structured format every KB article must follow. Consistent templates make articles searchable, Virtual Agent-readable, and maintainable. Unstructured articles written in freeform prose are the primary cause of poor KB search results.",
    who_fills="ECS SA owns this workbook. Customer Knowledge Managers review and approve before article authoring begins.",
    sprint_window="Sprint 5 Week 1",
    estimated_effort="1–2 hours",
    related_workbooks=["01 KB Structure", "04 Article Workflow"],
    success_criteria=[
        "OOTB article templates defined for at least two article types (How-To, Known Error/Workaround).",
        "Template fields are documented and agreed.",
        "Every MVP article uses the appropriate template.",
        "Template compliance is part of the Knowledge Manager review checklist.",
    ],
    process_decisions=[
        ("Which article types should have templates at MVP?", "Two OOTB templates: How-To (step-by-step instructions for end users) and Known Error/Workaround (IT Staff KB — issue description, impact, workaround, fix ETA).", "Two templates cover 90% of knowledge content. Templates ensure Virtual Agent can parse article structure for automated answers."),
        ("Should articles use the OOTB Knowledge Article workflow or a custom approval process?", "OOTB workflow: Draft → Review → Published → Retired. No custom approval steps. Knowledge Manager is the reviewer and publisher.", "Custom approval workflows add days to article publication and are rarely enforced consistently. The OOTB review-and-publish pattern with a named KM is faster and equally rigorous."),
        ("What is the mandatory field set for every article?", "Mandatory: Short Description (used as article title in search), Knowledge Base, Category, Valid to (review date — maximum 12 months from publish). Optional but strongly recommended: Flagged for review date, Related catalog items.", "The Valid to date is the most important field for KB health. Without it, articles stay published indefinitely and become stale."),
    ],
    dependencies=[("KB Structure (Workbook 01) confirmed", "Required", "Customer", "Sprint 5 Wk 1", ""),],
    config_sections=[
        ("How-To Article Template Fields", [
            ("Short Description", "Action verb + object e.g., 'Request a new laptop' or 'Reset your password'", "Used as article title in search. No jargon.", False),
            ("Article body — Section 1: Overview", "One paragraph: what this article helps you do.", "", False),
            ("Article body — Section 2: Before you start", "Prerequisites (accounts, access, information needed).", "", False),
            ("Article body — Section 3: Steps", "Numbered steps. Maximum 10. Each step = one action.", "", False),
            ("Article body — Section 4: Need more help?", "Link to catalog item or contact information.", "", False),
            ("Valid to (review date)", "12 months from publish date", "KM reviews and extends or retires.", False),
            ("Related catalog items", "Link to the catalog item this article supports (if applicable)", "", False),
        ]),
        ("Known Error / Workaround Template Fields", [
            ("Short Description", "Issue description in user language e.g., 'VPN disconnects after 30 minutes'", "", False),
            ("Issue description", "What happens; who is affected; when it started.", "", False),
            ("Workaround", "Step-by-step workaround. Must be immediately actionable.", "", False),
            ("Fix ETA", "Estimated resolution date or 'Under investigation'", "", False),
            ("Severity", "Major / Minor", "", False),
            ("Valid to", "90 days (Known Errors resolve faster than How-Tos)", "", False),
        ]),
    ],
    raci_rows=[
        ("Design and document article templates", "R/A", "I", "ECS SA."),
        ("Review and approve templates", "I", "R/A", "Customer Knowledge Managers."),
        ("Configure OOTB templates in ServiceNow", "R/A", "I", "ECS SA."),
        ("Validate first 5 articles against template standards", "R/A", "C", "ECS reviews; KM confirms quality."),
    ],
    consultant_guide_sections=[("Template enforcement", "Templates are only effective if the Knowledge Manager enforces them during article review. Build the template compliance check into the KM review checklist (Workbook 04): does the article use the correct template? Is the Valid to date set? Is the short description search-friendly? These three checks take 2 minutes per article and prevent the KB from degrading into freeform prose over time.")],
    adoption_rows=[("We want authors to write articles in their own format", "Enforce OOTB templates for all MVP articles.", "Freeform articles produce poor search results and cannot be parsed by Virtual Agent for automated answers. Template structure is the minimum for a machine-readable KB.", "'Authors can absolutely write in their own voice and style — the template just provides the structure. Think of it as a form: the author fills in the steps, the overview, and the valid-to date. The structure is invisible to the reader but critical for search and Virtual Agent.'", "Only for long-form reference content (policy documents, architecture guides) where template structure would be forced. Still require Short Description and Valid to fields.")],
    snmap_sections=[("Article Configuration", [("Knowledge Article", "kb_knowledge", "Main article table."), ("Article Template", "kb_template", "OOTB article templates — configure here."), ("Valid to field", "kb_knowledge.valid_to", "Review date. OOTB KB health flags expired articles.")])],
)

wb3 = TabContent(
    workbook_title="03 — Access Controls & User Criteria",
    pack_name=PACK_NAME,
    purpose="Defines which users can read, author, and manage each Knowledge Base, using OOTB User Criteria. Correct access control is essential for the IT Staff KB (internal content must not be visible to end users) and for any HR KB containing sensitive policy content.",
    who_fills="ECS SA configures user criteria; customer HR/IT Ops confirms audience definitions.",
    sprint_window="Sprint 5 Week 1",
    estimated_effort="1–2 hours",
    related_workbooks=["01 KB Structure"],
    success_criteria=[
        "User criteria are configured for each KB limiting read access to the correct audience.",
        "IT Staff KB is not visible to end users in Employee Center or Service Portal.",
        "Knowledge Managers can publish articles without admin access.",
        "Authors can submit articles for review without publish permission.",
    ],
    process_decisions=[
        ("How should IT Staff KB access be restricted?", "OOTB User Criteria: restrict to 'itil' role (IT service desk and above). All employees with the itil role have IT Staff KB access; other users do not see it in search or browsing.", "The itil role is the OOTB role for IT service management staff. Using it as the access criterion means the KB access automatically follows ServiceNow role assignments — no separate maintenance."),
        ("Should Knowledge Base authorship require a special role?", "Use OOTB Knowledge roles: knowledge_admin (KM — can publish and retire), knowledge (author — can draft and submit for review). Assign via group membership, not individual assignment.", "Group-based role assignment means when a team member joins or leaves, KB authorship access changes with their group membership — no individual user maintenance."),
        ("How should Employee Self-Service KB articles be restricted for regional content?", "Use User Criteria conditions on individual articles (not the KB) to restrict regional content. Article-level criteria do not restrict the KB from search but hide specific articles from users outside the criteria.", "Article-level restrictions are more surgical than KB-level restrictions. A user who searches the Self-Service KB should see global content and their region-specific content — not be blocked from the entire KB because some articles are regional."),
    ],
    dependencies=[("Foundation Data Pack — Groups", "Required", "ECS SA", "Sprint 0", "KB role assignment groups must exist.")],
    config_sections=[
        ("User Criteria Definitions", [
            ("IT Staff KB — Can Read", "User has role: itil", "OOTB itil role.", False),
            ("IT Staff KB — Can Contribute", "User has role: knowledge", "knowledge role for authors.", False),
            ("IT Staff KB — Can Manage", "User has role: knowledge_admin", "knowledge_admin for KM.", False),
            ("Employee Self-Service KB — Can Read", "All active employees (no restriction)", "Default — no user criteria needed for all-employee access.", False),
            ("Employee Self-Service KB — Can Contribute", "User has role: knowledge", "Same authorship role as IT Staff KB.", False),
            ("HR KB — Can Read", "User has role: hr_basic OR sn_hr_core.basic", "HR OOTB role.", True),
        ]),
    ],
    raci_rows=[
        ("Define user criteria per KB", "R/A", "C", "ECS SA defines; customer confirms audience."),
        ("Configure user criteria in ServiceNow", "R/A", "I", "ECS SA."),
        ("Assign knowledge and knowledge_admin roles to appropriate groups", "C", "R/A", "Customer IT Ops/HR assigns roles."),
        ("Test access as an IT Staff user and a non-IT user", "R/A", "C", "ECS tests; customer validates results."),
    ],
    consultant_guide_sections=[("Testing access controls", "Always test knowledge access from three perspectives: (1) a user with the itil role — should see IT Staff KB, (2) a user with no IT roles — should NOT see IT Staff KB, (3) a user with knowledge_admin — should be able to publish articles. Run these tests before Sprint 5 go-live. KB access control errors discovered in production are embarrassing and erode user trust.")],
    adoption_rows=[("We want everyone to be able to edit any article", "Use OOTB author/manager roles. Open edit access produces uncontrolled content that degrades KB quality.", "Open KB editing creates content that is inaccurate, inconsistent in tone, and not reviewed for technical accuracy. The two-role model (author submits, manager publishes) is the minimum governance for a trustworthy KB.", "'Open editing works on Wikipedia because of massive community oversight. In a corporate KB with a small team, it means unreviewed articles get published and stay published until someone notices they're wrong. The author/manager split takes 10 minutes per article — it's the cheapest quality control available.'", "Never open editing for published content. Draft-mode editing (author proposes changes) is acceptable.")],
    snmap_sections=[("Access Control Tables", [("User Criteria", "user_criteria", "Define conditions for KB access restrictions."), ("KB User Criteria", "kb_uc_can_read_mtom", "Links user criteria to KBs — read access."), ("KB Role", "knowledge / knowledge_admin", "OOTB roles for KB authorship and management.")])],
)

wb4 = TabContent(
    workbook_title="04 — Article Workflow & Review Cadence",
    pack_name=PACK_NAME,
    purpose="Defines the OOTB article lifecycle — Draft → Review → Published → Retired — and the review cadence that keeps articles current. The most common KB failure mode is articles that were accurate at go-live but were never reviewed and are now misleading users 18 months later.",
    who_fills="ECS SA defines the workflow configuration; Customer Knowledge Manager agrees the review cadence.",
    sprint_window="Sprint 5 Week 1",
    estimated_effort="1–2 hours",
    related_workbooks=["02 Article Template Standards", "06 Knowledge KPIs"],
    success_criteria=[
        "OOTB article workflow is configured (Draft → Review → Published → Retired).",
        "Review cadence is set per KB (12 months for How-To, 90 days for Known Errors).",
        "KB health report is scheduled to flag articles past their Valid to date.",
        "Knowledge Manager has a monthly review task in their calendar.",
    ],
    process_decisions=[
        ("Should article approval require more than one reviewer?", "One reviewer (the Knowledge Manager) is sufficient for MVP. Second reviewer can be added for compliance-sensitive categories in Phase 2.", "Two reviewers double the time to publication without a proportionate quality benefit for a mid-market KB. The KM role carries the accountability — one reviewer with real ownership is more effective than two reviewers with diffused responsibility."),
        ("What happens to articles that pass their Valid to date?", "OOTB: articles are automatically flagged as 'Needs Review' when Valid to is exceeded. They remain published (not hidden) until the KM reviews and either extends the date or retires the article. Do not auto-retire articles.", "Auto-retiring articles removes content that may still be accurate. The KM review step ensures intentional decisions — not automated actions — determine what stays in the KB."),
        ("How should Known Error articles be handled when the underlying problem is resolved?", "Retire the Known Error article. Create a How-To article if the resolution requires user action, or simply retire if the fix was transparent. Never leave Known Error articles published after the problem is resolved.", "Stale Known Error articles undermine trust in the KB. A user who finds a Known Error workaround for a problem that was fixed 6 months ago loses confidence in all KB content."),
    ],
    dependencies=[("KB Structure (Workbook 01)", "Required", "ECS SA", "Sprint 5 Wk 1", ""),],
    config_sections=[
        ("Article Lifecycle Configuration", [
            ("OOTB workflow states", "Draft → Review → Published → Retired", "Do not add custom states.", False),
            ("Author action", "Author creates Draft, submits for review", "", False),
            ("KM action", "KM reviews, publishes or returns to author with comments", "", False),
            ("Review notification", "OOTB: KM notified when article submitted for review", "", False),
        ]),
        ("Review Cadence", [
            ("How-To articles — Valid to period", "12 months from publish date", "KM receives review reminder 30 days before expiry.", False),
            ("Known Error articles — Valid to period", "90 days", "More frequent review — Known Errors resolve faster.", False),
            ("Monthly KM review task", "KM reviews OOTB 'Needs Review' report on the 1st of each month", "", True),
            ("Stale article threshold (KB Health)", "Valid to exceeded by > 30 days = stale", "Configure in KB Health settings.", False),
        ]),
    ],
    raci_rows=[
        ("Configure OOTB article workflow", "R/A", "I", "ECS SA."),
        ("Set Valid to periods per article type", "R/A", "C", "ECS SA sets defaults; KM can adjust per article."),
        ("Schedule monthly KB review in KM calendar", "I", "R/A", "Customer KM."),
        ("Review and action Needs Review report monthly", "I", "R/A", "Customer KM."),
    ],
    consultant_guide_sections=[("KB health as an engagement metric", "At the end of Sprint 5, set up the OOTB KB Health dashboard and show the customer: article count, average age, % with Valid to dates set, % flagged for review. This gives the KM a clear picture of the health of their KB from day one and establishes the baseline for the monthly review habit.")],
    adoption_rows=[("We want articles to publish immediately without review", "Use OOTB Draft → Review → Publish workflow.", "Unreviewed articles create accuracy risks and erode user trust. The review step is 5–10 minutes per article — the cheapest quality control available.", "'Immediate publishing seems faster until an article with incorrect steps causes users to make mistakes — and they stop trusting the KB entirely. The review step is 10 minutes per article. The KM can batch-review 10 articles in an hour. The trust it builds is worth it.'", "Never remove the review step for published articles.")],
    snmap_sections=[("Article Workflow", [("Article state field", "kb_knowledge.workflow_state", "Draft / Review / Published / Retired."), ("Valid to field", "kb_knowledge.valid_to", "Sets the review date. KB Health reports use this."), ("KB Health Dashboard", "Knowledge > Administration > KB Health", "Monitor article health, stale count, and review queue.")])],
)

wb5 = TabContent(
    workbook_title="05 — Search Optimization",
    pack_name=PACK_NAME,
    purpose="Defines the OOTB search configuration for the Knowledge Base: search source priority, synonyms, and the article field weighting that determines which articles appear at the top of search results. Good search is the single biggest driver of KB adoption — users who can't find what they need in two searches go to the helpdesk instead.",
    who_fills="ECS SA configures; customer Knowledge Manager validates search results for the top 10 expected search terms.",
    sprint_window="Sprint 5 Week 2",
    estimated_effort="2–3 hours (configuration + validation with KM)",
    related_workbooks=["01 KB Structure", "02 Article Template Standards"],
    success_criteria=[
        "OOTB Knowledge search source is configured and indexed.",
        "Short Description field has highest search weight (it is the article title).",
        "Top 10 expected search terms return relevant results.",
        "Search synonyms are configured for common IT terminology variations.",
        "No deprecated or retired articles appear in search results.",
    ],
    process_decisions=[
        ("Which article fields should be indexed for search?", "Short Description (highest weight), Text (article body, medium weight), Keywords/Tags (medium weight). Do not index internal fields like Author or Workflow State.", "The Short Description is effectively the article title — it should have the highest search weight. Article body catches long-tail search terms. Keywords/Tags allow authors to add synonyms for their articles."),
        ("Should we configure search synonyms?", "Yes. Configure OOTB Search Synonyms for the 10 most common terminology variations: VPN = 'remote access', 'password reset' = 'forgot password', 'laptop' = 'computer' = 'device'. Start with 10; expand based on search analytics post-launch.", "Search synonyms prevent users from not finding articles because they used a different word than the author. A user who searches 'forgot password' and gets no results when the article is titled 'Reset your password' gives up and calls the helpdesk."),
        ("How should retired and expired articles be handled in search?", "Retired articles must be excluded from search results immediately upon retirement. Articles past their Valid to date but not yet reviewed should remain in search results — they may still be accurate. OOTB search automatically excludes articles with workflow_state = Retired.", "Users finding retired article links from bookmarks or external search engines should see a redirect to the KB homepage, not a broken page. Configure OOTB redirect on retired articles."),
    ],
    dependencies=[("Articles published in KB (at least MVP set)", "Required", "Customer KMs", "Sprint 5 Wk 2", "Cannot validate search results without published content.")],
    config_sections=[
        ("Search Source Configuration", [
            ("Knowledge search source", "OOTB: sp_search_source for Knowledge", "Configure in Service Portal > Search Sources.", False),
            ("Short Description weight", "10 (highest)", "OOTB default. Do not reduce.", False),
            ("Text (article body) weight", "5 (medium)", "", False),
            ("Keywords/Tags weight", "7 (high)", "Authors use Keywords field to add synonyms for their articles.", False),
            ("Retired articles in search", "Excluded — OOTB (workflow_state filter)", "No configuration needed — OOTB behaviour.", False),
        ]),
        ("Search Synonyms (MVP set — top 10)", [
            ("password reset", "forgot password; locked out; can't log in", "", False),
            ("VPN", "remote access; remote work; connect from home", "", False),
            ("laptop", "computer; device; notebook; MacBook", "", False),
            ("software install", "application; program; app request", "", False),
            ("access request", "permissions; account access; user access", "", False),
            ("Additional synonyms", "[Customer KM to add based on helpdesk ticket language]", "Review the top 20 helpdesk ticket subjects for synonym candidates.", True),
        ]),
    ],
    raci_rows=[
        ("Configure search source and field weights", "R/A", "I", "ECS SA."),
        ("Configure search synonyms (MVP set)", "R/A", "C", "ECS SA configures initial set; KM adds domain-specific terms."),
        ("Validate top 10 search terms return relevant results", "R", "A", "ECS tests; KM validates results are correct.", ),
        ("Review search analytics monthly and add synonyms", "I", "R/A", "Customer KM owns ongoing synonym expansion."),
    ],
    consultant_guide_sections=[("The synonym seed list", "The best source for search synonyms is not a brainstorming session — it is the existing helpdesk ticket short description field. Export the top 50 most common ticket subjects from the last 6 months, identify the language users use for common requests, and configure synonyms that map that language to the KB article titles. This produces immediately relevant synonyms based on actual user behaviour.")],
    adoption_rows=[("We want to use a third-party search engine instead of OOTB", "Use OOTB search with configured weights and synonyms.", "Third-party search engines require integration maintenance and lose OOTB KB Health analytics, Virtual Agent integration, and Now Assist semantic search capabilities.", "'OOTB search with the right field weights and synonyms provides very good results for most corporate KB environments. If you have specific search quality issues at 6 months post-launch, we can revisit with Now Assist semantic search — which is still OOTB, just an upgraded tier.'", "OOTB search first. Now Assist semantic search (if licensed) is the Phase 2 upgrade path, not a custom third-party engine.")],
    snmap_sections=[("Search Configuration", [("Search Source", "sp_search_source", "Configure in Service Portal > Search Sources."), ("Search Synonym", "ts_synonym", "Search synonyms table. Configure in Knowledge > Administration > Search Terms."), ("Typeahead Search", "ts_index_table", "OOTB typeahead suggestions. Populated automatically as users search.")])],
)

wb6 = TabContent(
    workbook_title="06 — Knowledge KPIs & Governance",
    pack_name=PACK_NAME,
    purpose="Defines the Knowledge Management KPIs, the monthly governance cadence, and the process for measuring KB contribution to helpdesk deflection. Without measured outcomes, knowledge management becomes an unfunded activity that degrades over time.",
    who_fills="ECS SA defines the KPI framework; Customer KM and IT Director agree the targets.",
    sprint_window="Sprint 5 Week 2",
    estimated_effort="1–2 hours",
    related_workbooks=["04 Article Workflow"],
    success_criteria=[
        "KB deflection rate is baselined at go-live (helpdesk tickets with KB article linked).",
        "Monthly KB health review is scheduled with named owner.",
        "Article count and freshness targets are agreed.",
        "Search abandon rate is tracked (users who searched and submitted a ticket anyway).",
    ],
    process_decisions=[
        ("What is the primary KPI for Knowledge Management success?", "Deflection rate: % of helpdesk tickets where a KB article was viewed before or during the ticket lifecycle. Secondary: article freshness (% with Valid to date set and not expired).", "Deflection rate directly measures the business value of the KB. Every ticket deflected saves approximately 15–30 minutes of helpdesk time. A KB with 100 articles deflecting 20% of tickets saves more time than a KB with 500 articles that nobody uses."),
        ("How do we measure deflection?", "OOTB: track 'Viewed Knowledge' flag on incident/request records. ServiceNow automatically sets this flag when a user views a KB article before submitting a ticket. Report monthly on: tickets with KB viewed vs. total tickets.", "The OOTB deflection mechanism requires no customisation — it is built into the Service Portal and Employee Center knowledge search. Configure the monthly deflection report in Sprint 5 and baseline it at go-live."),
    ],
    dependencies=[("KB articles published (MVP set)", "Required", "Customer KMs", "Sprint 5 Wk 2", ""), ("Performance Analytics scope (if PA in scope)", "Recommended", "ECS SA", "Sprint 5", "PA dashboards provide richer KB analytics than standard reports.")],
    config_sections=[
        ("KPI Targets", [
            ("Deflection rate target (6 months post-launch)", "15% of tickets have KB article viewed before submission", "Baseline at go-live; review monthly.", True),
            ("Article freshness target", "90% of published articles with Valid to date set and not expired", "", True),
            ("Monthly article review completion", "100% of Needs Review articles actioned within 30 days of expiry", "", True),
            ("New article creation rate", "Minimum 2 new articles per KB per month for first 6 months", "Keeps KB growing; review target at 6 months.", True),
        ]),
        ("Governance Cadence", [
            ("Monthly KB health review", "1st of each month — KM reviews OOTB KB Health report", "", False),
            ("Quarterly deflection review", "KM + IT Director review deflection rate quarterly", "", False),
            ("Annual KB audit", "Full review of all published articles; retire stale content", "", False),
        ]),
    ],
    raci_rows=[
        ("Configure KB deflection report", "R/A", "I", "ECS SA."),
        ("Set KPI targets", "C", "R/A", "Customer KM + IT Director."),
        ("Run monthly KB health review", "I", "R/A", "Customer KM."),
        ("Report KB deflection to IT Director quarterly", "I", "R/A", "Customer KM."),
    ],
    consultant_guide_sections=[("The deflection conversation", "KB deflection rate is the only metric that directly connects Knowledge Management investment to business value. Frame it for the IT Director: 'For every 10% of tickets deflected by the KB, your helpdesk handles 10% fewer tickets for the same cost. At your current ticket volume, that is X tickets per month. At 15 minutes per ticket, that is Y hours saved per month.' Put a number on it in Sprint 5 — it justifies the knowledge management investment and motivates the KM.")],
    adoption_rows=[("We don't have time for a monthly KB review", "Schedule the monthly review as a standing 30-minute calendar appointment for the KM.", "Without a standing review appointment, the KB review happens 'when there's time' — which is never. 30 minutes per month is the minimum investment to prevent KB degradation.", "'30 minutes once a month to review a report and click Extend or Retire on a few articles. That is the entire governance commitment. Without it, the KB is accurate at launch and misleading users within 12 months. With it, the KB gets better every month.'", "Never skip the governance cadence. Simplify it for small teams, but never eliminate it.")],
    snmap_sections=[("KB Analytics", [("Deflection flag", "incident.knowledge_accessed / sc_request.knowledge_accessed", "OOTB flag set when user views KB before submitting."), ("KB Health Dashboard", "Knowledge > Administration > KB Health", "Article freshness, stale count, review queue."), ("Search Analytics", "Knowledge > Administration > Search Analytics", "What users searched for; what they found; where they gave up.")])],
)

def build_readme(out_path):
    doc = EcsDocument(meta=DocMeta(
        eyebrow="ACCELERATOR PACK", title="Knowledge\nAccelerator Pack",
        subtitle="Knowledge Base structure, article standards, access controls, and deflection measurement for the OOTB-first ServiceNow engagement",
        org="ECS Federal · ServiceNow Practice",
        audience="Customer Knowledge Manager, ITSM Process Owner, and IT Director",
        companion_to="Service Catalog Pack · Virtual Agent Pack · Employee Center Pack",
        doc_id="AP-13", version="1.0", status="Released",
        confidentiality="Shared — for the recipient and their organisation",
        running_header_label="Knowledge Accelerator Pack · ECS Federal",
    ))
    doc.add_cover_page(); doc.add_page_break()
    doc.h1("What This Pack Is", numbered=False)
    doc.para("This Accelerator Pack covers the complete Knowledge Management configuration for Sprint 5. Knowledge is a force-multiplier for the ITSM and Service Catalog investments from earlier sprints: a well-structured KB deflects helpdesk tickets, enables Virtual Agent to answer common questions, and powers Now Assist article summaries for agents.")
    doc.para("The six workbooks address the full KM sequence: Knowledge Base structure and audience definition (Workbook 01), article template standards (Workbook 02), access controls (Workbook 03), article lifecycle and review cadence (Workbook 04), search optimization (Workbook 05), and KPI measurement and governance (Workbook 06).")
    doc.h1("The Six Workbooks", numbered=False)
    doc.table(headers=["#", "Workbook", "What It Covers", "Owner", "Sprint"],
        rows=[
            ["01","KB Structure","KB hierarchy, categories, audience, Knowledge Manager assignments","Customer ITSM PO + KM","Sprint 5 Wk 1"],
            ["02","Article Template Standards","How-To and Known Error templates, mandatory fields, OOTB workflow","ECS SA","Sprint 5 Wk 1"],
            ["03","Access Controls","User criteria per KB, itil role restrictions, authorship roles","ECS SA + Customer IT Ops","Sprint 5 Wk 1"],
            ["04","Article Workflow & Review Cadence","Draft/Review/Publish lifecycle, Valid to periods, monthly review cadence","ECS SA + Customer KM","Sprint 5 Wk 1"],
            ["05","Search Optimization","Search source config, field weights, synonyms, search validation","ECS SA + Customer KM","Sprint 5 Wk 2"],
            ["06","Knowledge KPIs & Governance","Deflection rate, freshness targets, monthly governance, quarterly reporting","ECS SA + Customer KM + IT Director","Sprint 5 Wk 2"],
        ])
    doc.h1("Sprint Alignment", numbered=False)
    doc.para("Knowledge Management is configured in Sprint 5 alongside Employee Center and Virtual Agent. The three disciplines are tightly coupled: Employee Center is the user-facing portal that surfaces KB articles, Virtual Agent uses KB content to answer user questions, and Now Assist (Sprint 6) summarises KB articles for agents. All three require a well-structured, current KB to deliver value.")
    doc.save(out_path); print(f"README saved: {out_path}")

if __name__ == "__main__":
    OUT = HERE
    print("Building Knowledge Accelerator Pack...")
    for content, fname in [(wb1,"01_kb_structure.xlsx"),(wb2,"02_article_template_standards.xlsx"),(wb3,"03_access_controls.xlsx"),(wb4,"04_article_workflow.xlsx"),(wb5,"05_search_optimization.xlsx"),(wb6,"06_knowledge_kpis.xlsx")]:
        build_workbook(content, os.path.join(OUT, fname)); print(f"  ✓ {fname}")
    build_readme(os.path.join(OUT, "00_README_Knowledge_Pack.docx"))
    print("\nKnowledge Accelerator Pack complete.")
"\nKnowledge Accelerator Pack complete.")
