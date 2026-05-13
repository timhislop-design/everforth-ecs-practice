"""Build CLT-DT-06 through CLT-DT-09."""
from dtg_builder import build_dtg

GUIDES = [

# ═══════════════════════════════════════════════════════════════════════════════
# CLT-DT-06  State & Lifecycle Discipline
# ═══════════════════════════════════════════════════════════════════════════════
{
"doc_id": "CLT-DT-06",
"filename": "State_Lifecycle_Decision_Guide_CLIENT.docx",
"short_name": "State & Lifecycle Discipline",
"signal_subject": "your record lifecycle configuration",
"title": "State & Lifecycle\nDiscipline",
"subtitle": "A decision guide for defining record states that reflect real operational stages — and keep your data trustworthy",
"audience": "Process Managers, Service Desk Leadership, Incident and Change Managers, Reporting Owners",
"companion_to": "Incident Management Pre-Read · Change Management Pre-Read · Performance Analytics Pre-Read",
"how_to_use_paras": [
    "Every ServiceNow record — incident, request, change, problem — moves through a lifecycle: "
    "it is created, worked, resolved, and closed. The states in that lifecycle are not cosmetic. "
    "They determine which SLAs are running, which workflow steps are triggered, which fields "
    "are editable, and what appears in every dashboard and report your team produces.",
    "Lifecycle design is one of the most consequential decisions in an ITSM implementation, and "
    "one of the least visible until something goes wrong. When states are well-defined, record "
    "data accurately reflects operational reality and reports can be trusted. When states are "
    "vague or inconsistently used, records accumulate in limbo states, metrics mislead, and "
    "the dashboard becomes an exercise in interpretation rather than measurement.",
    "The four decisions below give you the framework for approaching lifecycle design "
    "deliberately — starting with the OOTB state model and adding only what your process "
    "genuinely requires.",
],
"why_matters": [
    {"h2": "States determine what SLAs measure",
     "body": "SLA clocks start, pause, and stop based on state changes. If the state model does "
             "not accurately reflect when work has actually started and stopped, the SLA data will "
             "not accurately reflect actual performance. The most common example: tickets parked "
             "in 'In Progress' while waiting for a vendor response — the SLA clock runs while no "
             "one is actually progressing the work. The correct fix is a state ('Awaiting Vendor') "
             "that pauses the SLA, not a workaround in the SLA pause logic."},
    {"h2": "State data drives every operational report",
     "body": "How many tickets are open? How long has this one been open? What is the queue depth "
             "by state? Every operational question draws on state data. When agents use states "
             "inconsistently — parking tickets in 'New' because 'In Progress' feels like a commitment, "
             "or closing tickets before the user confirms resolution — the state data stops reflecting "
             "operational reality, and reports stop being useful for management."},
    {"h2": "State transitions can enforce data quality",
     "body": "ServiceNow allows mandatory fields to be required at specific state transitions — "
             "an agent cannot close a ticket without entering a resolution note, or cannot move "
             "a Change to 'Implement' without a test plan attached. This is one of the most "
             "effective data quality enforcement tools in the platform, and it only works when "
             "the state model is clean enough to make those mandatory fields meaningful."},
],
"signals": [
    {"h2": "Large volumes of tickets sitting in intermediate states for extended periods",
     "body": "When a significant portion of your open tickets are in 'In Progress,' 'Pending,' "
             "or 'On Hold' for more than 5–7 days without activity, the states are being used as "
             "parking lots rather than progress indicators. This is almost always a state definition "
             "problem — the available states do not distinguish between 'actively being worked' and "
             "'waiting for something external.'"},
    {"h2": "Resolution and closure are treated as the same state",
     "body": "In many legacy configurations, tickets jump directly from 'In Progress' to 'Closed' "
             "without a 'Resolved' state. This skips the resolution confirmation window — the period "
             "during which the user can confirm the issue is fixed before the ticket is formally "
             "closed. Without it, reopened tickets appear as new tickets rather than as resolutions "
             "that failed, making reopen rates invisible."},
    {"h2": "Agents disagree on when to use a specific state",
     "body": "If you ask three agents what 'Pending' means, and get three different answers, the "
             "state is not defined operationally. Vague state definitions are always a data quality "
             "problem in disguise: the metric 'number of pending tickets' means different things "
             "on different days, depending on who moved what into 'Pending' for what reason."},
    {"h2": "Custom states were added for specific workflows and never cleaned up",
     "body": "Custom states are occasionally legitimate. More often, they were added to handle "
             "a specific scenario that could have been handled with a field value, a category, or "
             "an existing state used correctly. Custom states that exist for a single process area "
             "create confusion across teams that do not use that process area but see the state "
             "in their views."},
],
"decisions": [
    {"label": "Which OOTB states to adopt, and what each one means operationally",
     "body": "ServiceNow's OOTB Incident lifecycle — New, In Progress, On Hold, Resolved, Closed — "
             "covers the overwhelming majority of operational scenarios. The workshop will define "
             "exactly what each state means in operational terms: what is happening (or not happening) "
             "to a ticket in each state, and who is responsible for the next action.",
     "questions": [
         "Does 'In Progress' mean an agent is actively working, or that the ticket has been assigned?",
         "What does 'On Hold' mean — awaiting user response, awaiting vendor, or something else?",
         "Is there a 'Resolved' state where the fix has been applied but the user has not confirmed?",
     ],
     "landing": "The OOTB state set covers most scenarios. The key design work is defining each state "
                "operationally — not adding states, but agreeing on what each existing state means."},
    {"label": "What mandatory fields are required at each state transition?",
     "body": "For each state transition that produces meaningful data — specifically resolution "
             "and closure — define the minimum fields that must be populated before the transition "
             "is allowed. For Incident resolution: Resolution Code and Resolution Notes. For "
             "Incident closure: user confirmation or auto-close timer. These fields are the "
             "raw material for your knowledge base and your AI training data.",
     "questions": [
         "What information does your team need to capture at resolution to make that data useful?",
         "Is there a resolution code taxonomy that needs to be defined or imported?",
         "What is your auto-close policy — how long after resolution is a ticket closed if the user does not respond?",
     ]},
    {"label": "How will auto-closure be configured?",
     "body": "Auto-closure is the timer that moves a Resolved ticket to Closed after a defined "
             "period without user activity. The OOTB configuration supports a configurable number "
             "of days (typically 3–7). The workshop will calibrate this based on your user "
             "population and service level expectations.",
     "questions": [
         "How long should users have to reopen a resolved ticket before it auto-closes?",
         "Should auto-closure timing differ by priority — shorter for P4, longer for P1?",
         "What notification should users receive before auto-closure?",
     ]},
    {"label": "Which process areas need non-OOTB state additions, and why?",
     "body": "Before adding any state, the workshop will ask: can this scenario be handled "
             "with an existing OOTB state plus a field value? In most cases, the answer is yes. "
             "Custom states should be approved only when an existing state would create genuinely "
             "misleading data — not simply because the existing label feels imprecise.",
     "questions": [
         "Are there process steps that have no corresponding OOTB state?",
         "If a custom state were added, which teams would it affect — just the requesting team, or all teams?",
         "Could a 'substate' field accomplish the same goal without modifying the core lifecycle?",
     ]},
],
"good_rows": [
    ["Each state has a documented operational definition that agents can recite", "State definitions are vague or vary by team"],
    ["Tickets move through states in proportion to actual work progress", "Large pools of tickets parked in intermediate states for weeks"],
    ["Resolved and Closed are distinct states with a user-confirmation window", "Tickets jump directly from In Progress to Closed with no confirmation step"],
    ["Mandatory fields at closure produce complete, usable resolution data", "Closure allows empty resolution fields — data is missing for knowledge and AI"],
    ["Custom states are rare, documented, and process-area-specific", "Custom states accumulate without review across multiple process areas"],
    ["Auto-closure timer is configured and users are notified before it fires", "Auto-closure is not configured — tickets sit in Resolved indefinitely"],
],
"patterns": [
    {"label": "Pattern A — Reducing 14 custom states to 2",
     "body": "A federal agency had added 14 custom states across three process areas over five years. "
             "Auditing each one, they found that 12 of the 14 could be handled by the OOTB state "
             "set combined with a 'substate' field that did not affect SLA logic or reporting. "
             "They retained 2 custom states that represented genuinely distinct operational phases "
             "with different responsible parties, and retired the other 12. Agent confusion about "
             "state usage dropped immediately — the training materials became a single page."},
    {"label": "Pattern B — Defining 'On Hold' consistently across 6 teams",
     "body": "A healthcare IT organization found that 'On Hold' was interpreted differently across "
             "six resolver teams — ranging from 'awaiting user callback' to 'deprioritized for now.' "
             "They produced a one-page On Hold decision guide defining three valid On Hold reasons "
             "(awaiting user, awaiting vendor, approved exception) with specific field requirements "
             "for each. Within 30 days of publishing, 'On Hold' queue accuracy improved enough for "
             "management to trust the state count in dashboards for the first time."},
    {"label": "Pattern C — Mandatory resolution notes as knowledge source",
     "body": "A technology company implemented mandatory Resolution Notes and Resolution Code at "
             "incident closure as part of their state lifecycle design. In the first 90 days post "
             "go-live, their knowledge management team identified 40 article candidates directly "
             "from resolution notes — articles that would previously have required an agent to "
             "proactively author them. Now Assist for Knowledge was then used to draft those "
             "articles from the resolution notes, reducing authoring time by over 60%."},
],
"workshop_para": (
    "The workshop will define the operational meaning of each OOTB state for your primary process "
    "areas (Incident, Request, Change), configure mandatory field requirements at each key transition, "
    "set the auto-closure timer, and review any proposed custom states against the 'can OOTB cover "
    "this?' test. The output is a lifecycle design document ready for configuration."
),
"need_bullets": [
    "Current state list for Incident, Request, and Change — including any custom states",
    "Current auto-closure configuration (if any)",
    "Resolution code taxonomy if one exists",
    "Any process documentation that references specific states or state transitions",
],
"questions": [
    "Do your agents have a shared understanding of what each state means, or does it vary by team?",
    "What percentage of your open incidents are in 'On Hold' or 'Pending' at any given time?",
    "Do you currently require agents to enter resolution notes before closing a ticket?",
    "Have you added custom states beyond the OOTB set? If so, which process areas use them?",
    "What is your current auto-closure policy?",
],
"xrefs": [
    ["Incident Management Workshop Pre-Read", "State lifecycle is configured during the Incident Management sprint", "02_Client/05_Workshop_Pre-Reads/"],
    ["SLA Discipline Decision Guide", "State transitions drive SLA pause and stop logic — design them together", "02_Client/04_Decision_Topic_Guides/"],
    ["Knowledge Article Curation Decision Guide", "Resolution notes at closure feed the knowledge base — the connection is direct", "02_Client/04_Decision_Topic_Guides/"],
],
},

# ═══════════════════════════════════════════════════════════════════════════════
# CLT-DT-07  Knowledge Article Curation
# ═══════════════════════════════════════════════════════════════════════════════
{
"doc_id": "CLT-DT-07",
"filename": "Knowledge_Article_Curation_Decision_Guide_CLIENT.docx",
"short_name": "Knowledge Article Curation",
"signal_subject": "your knowledge management practice",
"title": "Knowledge Article\nCuration",
"subtitle": "A decision guide for building and maintaining a knowledge base that agents trust and users find",
"audience": "Knowledge Managers, Service Desk Leadership, Content Owners, Process Managers",
"companion_to": "Knowledge Management Workshop Pre-Read · Virtual Agent Decision Guide",
"how_to_use_paras": [
    "A knowledge base is worth precisely as much as users trust it. A knowledge base full of "
    "articles that are outdated, duplicated, or too generic to be actionable is not a resource — "
    "it is a search problem. Agents who learn that the knowledge base rarely has what they need "
    "stop searching it. Users who find outdated answers stop trusting it.",
    "The decisions in this guide are not about whether to have a knowledge base — they are about "
    "how to build one that stays useful. Every decision here compounds over time: good article "
    "standards set early produce a knowledge base that improves with each new article. Poor "
    "standards produce a knowledge base that becomes harder to maintain with each passing month.",
    "This guide pairs naturally with the Virtual Agent and Now Assist materials. Both AI "
    "capabilities draw on your knowledge articles — which means article quality is a direct "
    "input to AI quality. The time invested in curation discipline before go-live pays forward "
    "into every AI capability you activate.",
],
"why_matters": [
    {"h2": "Knowledge articles are the primary training data for your AI capabilities",
     "body": "Virtual Agent searches knowledge articles to answer user questions. Now Assist in "
             "Virtual Agent generates responses grounded in knowledge content. Now Assist for "
             "Knowledge drafts new articles from resolution notes. Every one of these capabilities "
             "performs in proportion to article quality: clear, current, well-structured articles "
             "produce useful AI outputs; vague, outdated, duplicated articles produce outputs "
             "that agents and users learn to distrust."},
    {"h2": "First-contact resolution depends on accessible, accurate knowledge",
     "body": "Agents who can find a clear resolution procedure in the knowledge base resolve tickets "
             "at first contact more often than agents who rely on memory or colleague consultation. "
             "The difference compounds: high first-contact resolution reduces contact volume, which "
             "gives agents more time per ticket, which improves resolution quality. The knowledge "
             "base is not a nice-to-have; it is the lever that determines whether your team's "
             "expertise is portable or locked in individuals."},
    {"h2": "Self-service deflection requires knowledge that users can act on",
     "body": "When users search the Employee Center portal or ask Virtual Agent a question, the "
             "knowledge base is what they get back. An article titled 'VPN Issue' with two sentences "
             "of general guidance does not deflect the call — it delays it. An article titled "
             "'How to reconnect to VPN after a password change' with step-by-step instructions "
             "and a screenshot deflects it. Deflection is a function of article specificity "
             "and actionability, not article volume."},
],
"signals": [
    {"h2": "Agents say 'the knowledge base is never helpful'",
     "body": "This is the most direct signal of a curation problem. When agents routinely skip "
             "the knowledge base and go straight to a colleague, the knowledge base has lost "
             "their trust. Trust is lost when articles are consistently outdated, too generic, "
             "or absent for the most common issues. Rebuilding trust requires a visible "
             "commitment to a curated, maintained article set — not just more articles."},
    {"h2": "Search returns many results for every query, but none is the right one",
     "body": "When the search for 'password reset' returns 12 articles — some for Windows, some "
             "for specific applications, some outdated, some duplicates — users stop trusting "
             "search and start calling. Article deduplication and clear titling are "
             "the most impactful quick wins for search performance."},
    {"h2": "No article review process exists",
     "body": "Articles that were accurate when published become inaccurate as systems change. "
             "Without a scheduled review process, the knowledge base drifts from reality over "
             "time. The typical pattern: articles are accurate for the first 6 months, then "
             "30% are outdated by month 12, and 60% by month 24. A review cadence prevents "
             "this drift from becoming a trust problem."},
    {"h2": "Knowledge base is used only internally, not by end users",
     "body": "If your knowledge base is visible only to IT agents and not accessible to end "
             "users through the portal, you are capturing one benefit (faster agent resolution) "
             "and missing the larger one (self-service deflection). The question is not whether "
             "all articles should be user-visible, but whether the ones that could be user-visible are."},
],
"decisions": [
    {"label": "What is the minimum quality standard for a publishable article?",
     "body": "Before the first article is published, the team needs a shared definition of what "
             "'good enough to publish' means. This prevents the common failure mode: an initial "
             "migration of hundreds of articles from a SharePoint wiki, none of which meet a "
             "quality bar, followed by a knowledge base that is technically large but practically "
             "worthless.",
     "questions": [
         "What template will articles follow — How-To, FAQ, Known Error, Reference?",
         "What is the minimum required content for each template?",
         "Who reviews and approves articles before they are published?",
         "What is the maximum allowed age for an article before it must be reviewed?",
     ],
     "landing": "Minimum bar: accurate title, correct template, reviewed by a named knowledge owner, "
                "actionable content (a user or agent reading it can take a next step). Anything below "
                "this bar stays in Draft until it meets the standard."},
    {"label": "What is the review and retirement cadence?",
     "body": "Knowledge articles need a scheduled review cycle and a defined retirement trigger. "
             "ServiceNow supports configurable review reminders — you define how many days after "
             "publish a review notification fires, and who receives it. You also define what "
             "happens to articles that are not reviewed in time: they can be automatically flagged "
             "or automatically retired.",
     "questions": [
         "How frequently should each article be reviewed — every 6 months, every 12 months?",
         "Who is responsible for reviewing articles in each service area?",
         "What happens to an article that misses its review window — flag it, or auto-retire?",
     ]},
    {"label": "Which articles should be user-visible versus agent-only?",
     "body": "User-visible articles appear in Employee Center search results and in Virtual Agent "
             "responses. Agent-only articles appear only in the agent workspace. The design "
             "question is the default: do you start with all articles user-visible (with explicit "
             "flagging for agent-only) or all articles agent-only (with explicit promotion for "
             "user-visible)?",
     "questions": [
         "Are there categories of content that should never reach end users (e.g., internal runbooks, vendor credentials)?",
         "What is your appetite for user-facing content — do you want to optimize for deflection or for internal efficiency first?",
     ],
     "landing": "Start with user-visible as the default for How-To and FAQ articles. Reserve agent-only "
                "for Known Error runbooks and internal process guides."},
    {"label": "How will articles be migrated from existing sources?",
     "body": "Most organizations have existing knowledge scattered across SharePoint, wikis, "
             "email threads, and individuals. The migration decision is: bulk import everything, "
             "selective import of high-quality content, or start fresh with new articles. The "
             "bulk import approach feels faster but typically imports existing quality problems. "
             "Selective migration — bringing only current, accurate, well-structured content — "
             "produces a smaller but trusted knowledge base at launch.",
     "questions": [
         "Where does your current knowledge live? Is it structured or unstructured?",
         "Do you have existing articles that you would consider high-quality today?",
         "Is there a team member who can lead a structured migration review?",
     ]},
],
"good_rows": [
    ["Articles have clear, searchable titles that match how users describe the issue", "Article titles are generic ('Network Issue') or use internal codes users do not know"],
    ["Every article follows a template with defined required sections", "Articles vary in structure — some are a paragraph, some are 10 pages"],
    ["Review reminders fire on a defined schedule; owners respond within SLA", "Articles published and never reviewed — accuracy degrades without detection"],
    ["Search for a common issue returns 1–3 relevant articles, not 15", "Search returns many near-duplicate results for every common query"],
    ["User-visible articles are actionable — a user can follow them to resolution", "User-visible articles are general background — users still need to call"],
    ["Article effectiveness tracked via feedback and view-to-resolution data", "No data on which articles are useful — curation decisions made by instinct"],
],
"patterns": [
    {"label": "Pattern A — Selective migration producing a trusted knowledge base",
     "body": "A federal agency had 800 articles in a SharePoint wiki. Rather than bulk-importing "
             "them, they ran a structured review: two knowledge leads spent two weeks classifying "
             "each article as 'migrate,' 'rewrite,' or 'retire.' Of 800 articles, 210 migrated "
             "as-is, 120 were rewritten, and 470 were retired as outdated or duplicates. The "
             "resulting 330-article knowledge base had a user satisfaction rating of 4.2/5 within "
             "60 days of go-live. The agency that had done a bulk import of all 800 articles "
             "reported a 2.1/5 rating — because users kept finding outdated content."},
    {"label": "Pattern B — Now Assist drafting articles from resolution notes",
     "body": "A technology company implemented a process using Now Assist for Knowledge: at ticket "
             "closure, if the resolution note met a minimum length and the issue category was "
             "flagged as 'knowledge candidate,' Now Assist drafted an article that went to the "
             "knowledge queue for review. In the first quarter, 85 articles were drafted and "
             "45 were published after review — more than the knowledge team had published manually "
             "in the prior year. Agent review time was approximately 10 minutes per article."},
    {"label": "Pattern C — Tiered visibility for security-sensitive content",
     "body": "A healthcare organization maintained two parallel knowledge bases: one user-visible "
             "with How-To and FAQ content, one agent-only with runbooks and known error procedures "
             "that included system credentials and internal configurations. The tiered approach "
             "let them publish aggressively to the user-facing base without security review, "
             "while keeping sensitive operational content fully controlled."},
],
"workshop_para": (
    "In the workshop, we will define your article templates, quality standards, review cadence, "
    "and visibility model. We will also assess your existing knowledge sources and develop a "
    "migration plan — identifying what migrates as-is, what needs rewriting, and what should "
    "not be migrated. The output is a knowledge management governance document and an initial "
    "article backlog ready for the Knowledge sprint."
),
"need_bullets": [
    "Inventory of existing knowledge sources (SharePoint sites, wiki pages, shared drives with process documentation)",
    "List of the top 20 issues your team resolves repeatedly — these are your first article targets",
    "Current knowledge base (if any) with article count and last-updated dates",
    "Team member who will lead knowledge management post-go-live",
],
"questions": [
    "Does your team currently use a knowledge base? If so, what is the agent satisfaction with it?",
    "Where does institutional knowledge live today — in documents, in people's heads, in email threads?",
    "Who would own the article review and publication process post-go-live?",
    "Are there topics that are sensitive enough to require restricted visibility?",
    "What is the most common reason users contact the service desk — is there existing documentation for those issues?",
],
"xrefs": [
    ["Knowledge Management Workshop Pre-Read", "Background reading for the Knowledge Management sprint workshop", "02_Client/05_Workshop_Pre-Reads/"],
    ["Virtual Agent Topic Selection Decision Guide", "VA topics need corresponding knowledge articles — design them together", "02_Client/04_Decision_Topic_Guides/"],
    ["Now Assist/GenAI Workshop Pre-Read", "Now Assist drafts knowledge articles from resolution notes — understand the connection", "02_Client/05_Workshop_Pre-Reads/"],
],
},

# ═══════════════════════════════════════════════════════════════════════════════
# CLT-DT-08  Virtual Agent Topic Selection
# ═══════════════════════════════════════════════════════════════════════════════
{
"doc_id": "CLT-DT-08",
"filename": "Virtual_Agent_Topic_Selection_Decision_Guide_CLIENT.docx",
"short_name": "Virtual Agent Topic Selection",
"signal_subject": "your Virtual Agent deployment",
"title": "Virtual Agent\nTopic Selection",
"subtitle": "A decision guide for choosing which topics Virtual Agent handles — and designing each one to actually resolve",
"audience": "IT Leadership, Service Desk Leadership, Knowledge Managers, Process Owners",
"companion_to": "Virtual Agent Workshop Pre-Read · Knowledge Article Curation Decision Guide",
"how_to_use_paras": [
    "Virtual Agent's value is entirely proportional to its containment rate — the percentage of "
    "conversations that reach a resolution without transferring to a human agent. A VA that "
    "handles 80% of its conversations without escalation delivers deflection. A VA that "
    "escalates 70% of conversations to live agents delivers frustration.",
    "Containment rate is driven by topic selection, not topic volume. Organizations that launch "
    "with 5 well-designed, fully-resolving topics consistently outperform organizations that "
    "launch with 30 topics that each end with 'let me connect you to an agent.' The design "
    "principle is: complete what you start.",
    "This guide helps you identify the right starting topics for your organization, design each "
    "topic for maximum containment, and build a sustainable expansion roadmap. Read it alongside "
    "the Knowledge Article Curation guide — the two are deeply connected. Topics that cannot "
    "resolve without knowledge articles need the knowledge base to be ready first.",
],
"why_matters": [
    {"h2": "Each fully-contained VA conversation is a service desk contact that does not happen",
     "body": "Password reset is the canonical example: a fully-contained VA password reset topic "
             "handles the user request without any agent involvement. If your service desk handles "
             "500 password reset contacts per month, a VA topic with 70% containment eliminates "
             "350 of them. The math is straightforward; the design work is ensuring 'fully "
             "contained' means the user actually got what they needed — not just that VA "
             "closed the conversation."},
    {"h2": "VA is the front door to your entire self-service experience",
     "body": "Users who have a good VA experience return to VA for subsequent requests. Users who "
             "have a bad VA experience — who type a question and get 'I didn't understand that, "
             "let me connect you to an agent' — do not return. First impressions from the first "
             "few topics your VA handles determine whether it builds a user base or becomes "
             "an abandoned feature."},
    {"h2": "Now Assist in VA extends coverage without additional topic configuration",
     "body": "Now Assist in Virtual Agent allows VA to generate answers to questions it was "
             "not explicitly programmed for — by searching your knowledge base and generating "
             "a contextual response. This means a high-quality knowledge base extends VA "
             "coverage automatically. Topics handle the procedural interactions (reset a "
             "password, check a ticket status, submit a request); Now Assist handles the "
             "informational questions."},
],
"signals": [
    {"h2": "VA escalates more than 50% of conversations",
     "body": "If more than half of VA conversations end with a transfer to a live agent, the "
             "topics are either handling the wrong use cases (cases that require human judgment) "
             "or are designed to escalate rather than resolve. A 50%+ escalation rate means "
             "the VA is adding a step to the contact process — the user had to go through VA "
             "to get to the agent — rather than reducing contacts."},
    {"h2": "Topic list was driven by what was technically possible, not by user volume",
     "body": "VA topic selection is often driven by 'what can we automate?' rather than 'what "
             "do users ask most?' The two lists rarely overlap perfectly. Building topics for "
             "high-automatable but low-volume use cases underperforms building topics for "
             "high-volume use cases even when those require slightly more design work."},
    {"h2": "Topics exist but have zero usage",
     "body": "Topics that are live but never invoked are typically a discoverability problem: "
             "the topic exists but users do not phrase their request in a way that matches the "
             "NLU training phrases. Every topic without usage is a topic that needs more training "
             "phrases or a different entry point."},
],
"decisions": [
    {"label": "Which topics will launch at go-live?",
     "body": "Start with the contacts that are highest-volume AND fully resolvable without human "
             "judgment. Password reset, ticket status inquiry, software access request, VPN "
             "connectivity help, and new hire equipment request are the most common starting set. "
             "For each candidate topic, ask: can VA resolve this end-to-end, or does it always "
             "require a human to do something?",
     "questions": [
         "What are your top 10 service desk contact reasons by volume?",
         "Of those 10, which ones are fully resolvable without a human action (e.g., password reset via API)?",
         "Which ones require a human action but could be accelerated by VA pre-collecting information?",
     ],
     "landing": "Most organizations launch with 5–8 topics. The first three should be password reset, "
                "ticket status, and a high-volume request type specific to the organization."},
    {"label": "Full resolution vs. assisted triage — which design applies to each topic?",
     "body": "Full resolution: VA completes the outcome without agent involvement (password reset, "
             "ticket status, knowledge search). Assisted triage: VA collects structured information "
             "and creates a pre-populated ticket for faster agent handling. Assisted triage is "
             "the right design for topics where human judgment is required but information "
             "gathering can be automated.",
     "questions": [
         "Which of your candidate topics can be fully resolved by VA without any agent action?",
         "Which require an agent action, but where pre-collecting information from the user would save time?",
         "Are there topics where the right answer depends on data VA can retrieve from ServiceNow?",
     ]},
    {"label": "How will topics be integrated — portal only, or also Microsoft Teams?",
     "body": "VA can operate inside Employee Center and inside Microsoft Teams. Teams integration "
             "increases adoption significantly because users do not need to leave their primary "
             "work tool. However, it requires an approved Teams app and coordination with your "
             "Microsoft tenant administrator.",
     "questions": [
         "Is Microsoft Teams the primary collaboration tool for your employee population?",
         "Is there an existing Microsoft tenant administrator who can support Teams app approval?",
         "Is there a security or compliance review required for a new Teams app?",
     ]},
    {"label": "What is the NLU training strategy?",
     "body": "The OOTB NLU model covers standard IT language. For your organization's specific "
             "terminology — system names, internal acronyms, department-specific vocabulary — "
             "training phrases need to be added to each topic. More training phrases means "
             "better intent recognition, which means fewer failed intents that escalate to agents.",
     "questions": [
         "What internal system names or acronyms do your users commonly use that might not be in a standard NLU model?",
         "Are there department-specific ways of phrasing common requests?",
         "Who will own NLU training ongoing — adding phrases based on failed intent data?",
     ]},
],
"good_rows": [
    ["Containment rate above 60% for each live topic", "Containment rate below 40% — VA is routing most users to agents"],
    ["Topics selected based on contact volume data", "Topics selected based on what was easiest to configure"],
    ["Each topic fully resolves or fully pre-populates for triage", "Topics end with 'I'll transfer you to an agent' without doing anything first"],
    ["NLU training phrases cover internal terminology and common phrasings", "OOTB NLU only — fails on organization-specific language"],
    ["Unused topics identified and retrained within 30 days of go-live", "Unused topics left live without investigation"],
    ["Now Assist in VA extends coverage to informational questions", "VA covers only explicitly configured topics — knowledge is not connected"],
],
"patterns": [
    {"label": "Pattern A — Five topics, 62% containment rate in month one",
     "body": "A federal agency launched VA with exactly five topics: password reset, ticket status, "
             "remote access help (VPN), software request, and new hire equipment request. They "
             "spent the first two weeks adding organization-specific NLU training phrases. In "
             "month one, the five topics handled 1,200 conversations with a 62% containment rate "
             "— 744 contacts that did not reach the service desk. The agency had been targeting "
             "30% containment as a first-year goal. They exceeded it in month one."},
    {"label": "Pattern B — Assisted triage design for access requests",
     "body": "A technology company determined that access requests required an IT security review "
             "before approval — full VA resolution was not possible. They designed an assisted "
             "triage topic: VA collected the requested system, the justification, the user's "
             "manager, and the target access level, then created a pre-populated incident. "
             "Agent handling time for access requests dropped from an average of 12 minutes "
             "to 4 minutes. The VA did not deflect the contact but substantially reduced its cost."},
    {"label": "Pattern C — Now Assist extending coverage to policy questions",
     "body": "A healthcare organization found that 30% of their VA conversations were informational "
             "questions about IT policies — 'can I install this software?', 'what is the VPN "
             "policy for personal devices?' — that did not match any configured topic. After "
             "activating Now Assist in VA and publishing 15 policy knowledge articles, VA began "
             "generating contextual answers to policy questions using the knowledge content. "
             "The informational escalation rate dropped from 30% to 8% within 60 days."},
],
"workshop_para": (
    "The workshop will start with your contact volume data and work through the topic selection "
    "decision together. For each candidate topic, we will determine the design pattern "
    "(full resolution vs. assisted triage), map the required system integrations "
    "(password reset requires an AD/Entra integration, for example), and identify the NLU "
    "training phrase set needed to cover your organization's specific language. The output "
    "is a prioritized topic roadmap with design specifications for the launch set."
),
"need_bullets": [
    "Top 20 service desk contact reasons by volume (last 6–12 months)",
    "Microsoft Teams environment details if Teams integration is in scope",
    "Active Directory or Entra ID integration status — required for password reset topic",
    "Knowledge base readiness assessment — which articles are ready for VA search?",
],
"questions": [
    "What are your top 10 service desk contact reasons, and do you have volume data for each?",
    "Which of those contacts are fully resolvable without a human agent action?",
    "Do your employees primarily work in a browser portal or in Microsoft Teams?",
    "Do you currently have any VA or chatbot deployment? If so, what is the containment rate?",
    "Who will own VA topic configuration and NLU training post-go-live?",
],
"xrefs": [
    ["Virtual Agent Workshop Pre-Read", "Background reading for the Virtual Agent sprint workshop", "02_Client/05_Workshop_Pre-Reads/"],
    ["Knowledge Article Curation Decision Guide", "VA topics rely on knowledge articles — curation discipline and topic selection are designed together", "02_Client/04_Decision_Topic_Guides/"],
    ["Now Assist/GenAI Workshop Pre-Read", "Now Assist extends VA coverage beyond configured topics — understand the connection", "02_Client/05_Workshop_Pre-Reads/"],
],
},

# ═══════════════════════════════════════════════════════════════════════════════
# CLT-DT-09  Predictive Intelligence Readiness
# ═══════════════════════════════════════════════════════════════════════════════
{
"doc_id": "CLT-DT-09",
"filename": "Predictive_Intelligence_Readiness_Decision_Guide_CLIENT.docx",
"short_name": "Predictive Intelligence Readiness",
"signal_subject": "your Predictive Intelligence configuration",
"title": "Predictive Intelligence\nReadiness",
"subtitle": "A decision guide for assessing data quality, selecting use cases, and governing ML models in ServiceNow",
"audience": "IT Leadership, Incident Managers, Service Desk Leadership, Data and Analytics Owners",
"companion_to": "Predictive Intelligence Workshop Pre-Read · Category Structure Simplification Decision Guide",
"how_to_use_paras": [
    "Predictive Intelligence (PI) is one of the most directly measurable AI capabilities in "
    "ServiceNow. When it works well, incoming tickets are categorized and routed automatically "
    "before a human touches them. When it is misconfigured — trained on inconsistent data or "
    "applied to the wrong use cases — it makes suggestions agents learn to ignore, and the "
    "capability quietly disappears from adoption.",
    "The difference between those two outcomes is almost entirely in the preparation. PI is "
    "a machine learning model: it learns from your historical data and applies what it learns "
    "to new records. Feed it clean, consistent data and it produces accurate predictions. "
    "Feed it noisy data and it produces noise. The data decisions you make now — in category "
    "structure, in closure discipline, in assignment accuracy — are the PI training investment.",
    "Read this alongside the Category Structure Simplification guide. Category consistency "
    "is the single most important PI prerequisite, and the two conversations belong together.",
],
"why_matters": [
    {"h2": "Every miscategorized ticket is a PI training error",
     "body": "PI trains on the category and assignment group recorded in closed tickets. When "
             "agents categorize the same issue type differently across the team, the training "
             "data contains contradictions: the same description leads to different categories "
             "in the historical record. The model cannot learn a reliable pattern from contradictory "
             "data. Data consistency is not a precondition of PI — it IS PI training."},
    {"h2": "Routing accuracy from PI compounds over time",
     "body": "When PI makes a prediction and the agent confirms it (accepts the suggested category "
             "without changing it), that confirmation reinforces the model. When the agent changes "
             "the prediction, that correction adjusts the model. A PI model in an environment "
             "with high categorization consistency improves continuously. A model in an "
             "inconsistent environment oscillates and does not improve."},
    {"h2": "PI readiness is an organizational discipline, not a technical configuration",
     "body": "Organizations that treat PI readiness as a data quality project — auditing their "
             "historical data, retraining categories, enforcing closure discipline — achieve "
             "meaningful prediction accuracy in the first 60 days of activation. Organizations "
             "that treat PI as a feature to turn on without data preparation rarely see prediction "
             "accuracy above 50% — below the threshold where agents trust and use the predictions."},
],
"signals": [
    {"h2": "Category consistency rate below 70%",
     "body": "If you pull your incident records for the last 12 months and find that similar "
             "descriptions are categorized the same way less than 70% of the time, PI will "
             "struggle to learn from that data. The threshold for meaningful PI accuracy is "
             "roughly 75–80% training data consistency within each category."},
    {"h2": "Fewer than 1,000 closed records per category in the training window",
     "body": "PI models need volume to find reliable patterns. Categories with fewer than "
             "1,000 closed records in the training window produce low-confidence predictions. "
             "Low-confidence predictions that are set to auto-apply produce errors; "
             "low-confidence predictions that are set to suggest and require agent confirmation "
             "add a step without adding value."},
    {"h2": "High reassignment rate in the current tool",
     "body": "A high reassignment rate in the current ITSM tool is a signal that initial "
             "categorization and assignment are frequently wrong. If human agents are wrong "
             "30% of the time, the training data contains 30% incorrect labels — which means "
             "the PI model will learn to replicate the errors. Improving assignment accuracy "
             "before activating PI is the investment that pays forward into model accuracy."},
],
"decisions": [
    {"label": "Which PI use cases to activate first?",
     "body": "Category prediction and assignment group prediction for Incident records are "
             "the highest-volume, highest-impact starting use cases. They apply to every "
             "incoming ticket and address the most common routing friction points. Extend "
             "to Request and Change records after Incident model accuracy is validated.",
     "questions": [
         "What is your current monthly incident volume? Does it provide enough data for model training?",
         "Are there specific category families with consistently clean data that could serve as a PI pilot?",
         "Is the priority prediction use case relevant — do you have clear, consistent priority assignment today?",
     ]},
    {"label": "What is the data quality remediation approach?",
     "body": "Before activating PI on historical data, the team should assess data quality for "
             "the training window (typically last 12–24 months). If consistency is below 70%, "
             "a targeted remediation is needed: re-categorizing a sample of high-volume "
             "incorrectly-categorized records, or limiting the training window to the most "
             "recent period when categorization discipline was highest.",
     "questions": [
         "Do you have a way to assess category consistency in your current tool's export?",
         "Is there a team or analyst who could lead a focused data quality audit?",
         "Should we exclude data from before a certain date if categorization practices changed?",
     ]},
    {"label": "What confidence threshold before predictions are auto-applied?",
     "body": "PI produces a confidence score for each prediction (0–100%). You configure whether "
             "predictions above a certain confidence are applied automatically, or whether all "
             "predictions are surfaced as suggestions for agent review. The recommended starting "
             "configuration is 'suggest only' — show the prediction, let agents confirm or "
             "correct — until model accuracy is validated at 80%+.",
     "questions": [
         "Is your organization comfortable with auto-applied predictions in the first 90 days?",
         "What is the tolerance for prediction errors — how many wrong auto-categorizations per day would be acceptable?",
         "How will prediction accuracy be monitored and reported?",
     ],
     "landing": "Start with 'suggest only' at any confidence level. Move to auto-apply above 85% "
                "confidence after 90 days of accuracy monitoring. Revisit thresholds quarterly."},
    {"label": "Who governs the PI models post-activation?",
     "body": "PI models require ongoing governance: monitoring prediction accuracy, scheduling "
             "retraining as new data accumulates, and adjusting confidence thresholds as accuracy "
             "improves. Without a named owner, PI models drift — they stop improving and agents "
             "stop trusting them. The workshop will assign governance responsibility and define "
             "the minimum monitoring cadence.",
     "questions": [
         "Who will monitor PI prediction accuracy — the process manager, a data analyst, the service desk lead?",
         "How frequently will models be retrained — monthly, quarterly?",
         "What is the 'accuracy floor' below which a model is suspended and retrained?",
     ]},
],
"good_rows": [
    ["Category consistency above 75% in the training window", "Agents categorize the same issue type differently — training data is contradictory"],
    ["1,000+ closed records per category in the training dataset", "Thin categories with fewer than 500 records — predictions are low-confidence"],
    ["'Suggest only' mode for first 90 days post-activation", "Auto-apply activated immediately — errors undermine agent trust before accuracy is validated"],
    ["Named PI model owner with a quarterly accuracy review cadence", "PI activated and left unmonitored — model accuracy drifts without anyone noticing"],
    ["Agent correction data used to improve model — feedback loop active", "Agent corrections not monitored — model not learning from corrections"],
    ["Prediction accuracy reported to service desk leadership monthly", "Accuracy not tracked — leadership cannot see whether PI is delivering value"],
],
"patterns": [
    {"label": "Pattern A — 90-day accuracy improvement curve",
     "body": "A federal agency activated PI in suggest-only mode with a category consistency rate "
             "of 72% at training time. In month one, prediction accuracy was 64%. They ran a "
             "targeted remediation: agents were coached on the category definitions that had the "
             "most inconsistency, and 3,000 historical records were re-categorized. By month three, "
             "training data consistency had reached 81%, and prediction accuracy was 83%. They "
             "moved to auto-apply for the top three categories at that point."},
    {"label": "Pattern B — Piloting PI on highest-volume categories first",
     "body": "A technology company had 35 incident categories, but five of them represented 60% "
             "of volume and had the most consistent historical data. They activated PI only on "
             "those five categories initially — with auto-apply above 90% confidence — and ran "
             "the remaining categories through manual categorization. After 60 days, they expanded "
             "PI to the remaining categories as data quality improved across the board."},
    {"label": "Pattern C — PI as a change management conversation",
     "body": "A healthcare organization found that activating PI required as much change management "
             "as technical configuration. Agents were initially skeptical of AI suggestions and "
             "routinely overrode correct predictions. They ran a 30-day 'trust the suggestion' "
             "program: tracking which agents overrode suggestions, reviewing whether the override "
             "was correct, and sharing the accuracy data with the team. Override rates dropped "
             "from 45% to 18% — and agent-confirmed predictions improved model accuracy faster."},
],
"workshop_para": (
    "The workshop will assess your historical data quality, select PI use cases, configure the "
    "confidence threshold model, and assign governance ownership. We will also review your category "
    "taxonomy alongside the PI readiness assessment — the two conversations are inseparable. "
    "The output is a PI activation plan with a phased rollout timeline and accuracy milestones."
),
"need_bullets": [
    "Incident export from current tool (last 12–24 months) with category, subcategory, assignment group, and resolution date",
    "Category volume report — tickets per category per month",
    "Current reassignment rate data if available",
    "Contact for the person who will own PI model governance post-go-live",
],
"questions": [
    "How many incidents does your environment process per month?",
    "Is your current incident categorization consistent across the team, or does it vary by agent?",
    "Have you run any data quality assessment on your historical incident records?",
    "What is your comfort level with AI-applied predictions versus AI-suggested predictions?",
    "Who would own Predictive Intelligence model governance and accuracy monitoring?",
],
"xrefs": [
    ["Predictive Intelligence Workshop Pre-Read", "Background reading for the PI workshop session", "02_Client/05_Workshop_Pre-Reads/"],
    ["Category Structure Simplification Decision Guide", "Category consistency is the primary PI prerequisite — design the two together", "02_Client/04_Decision_Topic_Guides/"],
    ["Now Assist/GenAI Workshop Pre-Read", "Understand how PI and Now Assist work together in the AI layer", "02_Client/05_Workshop_Pre-Reads/"],
],
},

]  # end GUIDES

if __name__ == "__main__":
    print(f"\nBuilding {len(GUIDES)} Decision Topic Guides (batch 2: DT-06 to DT-09)...\n")
    for g in GUIDES:
        build_dtg(g)
    print(f"\n✅  Batch 2 complete.\n")
