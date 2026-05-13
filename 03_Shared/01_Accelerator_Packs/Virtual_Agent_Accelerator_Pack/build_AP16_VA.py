"""
build_AP16_VA.py — AP-16 Virtual Agent Accelerator Pack
Covers: OOTB Now Assist VA scope, NLU topic design, handoff config,
analytics KPIs, and go-live readiness.
Sprint window: Month 3 (Sprints 5-6)
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
TEMPLATES = os.path.join(REPO, "03_Shared", "00_Templates_and_Branding")
sys.path.insert(0, TEMPLATES)
from accelerator_pack_builder import TabContent, build_workbook
from ecs_template import EcsDocument, DocMeta

PACK_DIR = os.path.dirname(os.path.abspath(__file__))
PACK_NAME = "Virtual Agent Accelerator Pack"

# =============================================================================
# WB1 — VA Scope & Channel Decisions
# =============================================================================
wb1 = TabContent(
    workbook_title="01 — VA Scope & Channel Decisions",
    pack_name=PACK_NAME,
    purpose="Establish which channels, languages, and business domains the OOTB Now Assist Virtual Agent will serve at go-live. Decisions here gate topic design (WB2) and handoff configuration (WB3).",
    who_fills="ECS Consultant completes Tabs 2, 4, 6, 7, 8. Customer Product Owner + IT Lead complete Tab 2 process decisions and Tab 4 yellow cells.",
    sprint_window="Sprint 5 — complete by end of Week 10",
    estimated_effort="2-3 hours with Customer PM and IT Lead",
    related_workbooks=["02 Topic Design & NLU Intent Library", "03 Handoff & Escalation", "AP-15 Employee Center", "AP-13 Knowledge Management"],
    success_criteria=[
        "Primary channel confirmed (portal, Teams, Slack).",
        "Business domains in scope agreed (IT, HR, other).",
        "Language support decision made.",
        "Live-agent handoff requirement confirmed.",
        "Customer VA Admin named and engaged.",
    ],
    process_decisions=[
        ("Which channel should Virtual Agent launch on first?",
         "Employee Center portal (web) — Teams/Slack deferred to Phase 2.",
         "Teams adds OAuth app registration complexity. The portal widget is zero-dependency and immediately available once Employee Center is live (AP-15)."),
        ("Which business domains should VA cover at go-live?",
         "IT (incidents, requests, password reset) + HR FAQ (read-only knowledge deflection) only.",
         "Limiting to 2 domains keeps the topic set manageable in a 2-sprint window. HR FAQ is read-only — no fulfillment workflow, just KB deflection."),
        ("Should VA support multiple languages?",
         "English only at go-live. Multi-language is Phase 2.",
         "Each additional locale requires separate NLU training utterances. Deferring ensures go-live quality in English is high before expanding."),
        ("Is live-agent handoff required?",
         "Yes — OOTB Connect Chat → Agent Workspace (IT Tier 1 queue).",
         "OOTB native handoff. No third-party ACD (Genesys, Five9) integration in the 18-week scope."),
        ("Who owns VA topic maintenance post-go-live?",
         "Customer VA Admin (trained by ECS in Sprint 6).",
         "ECS trains 1-2 customer admins during Sprint 6. Customer owns utterance tuning and new topic builds post-stabilization."),
    ],
    dependencies=[
        ("Employee Center published (AP-15)", "Required", "ECS + Customer", "Sprint 5 Wk 1", "VA widget is embedded in EC — EC must be live before VA can be launched."),
        ("Knowledge Base published (AP-13)", "Required", "ECS + Customer", "Sprint 5 Wk 1", "HR FAQ and IT KB topics require published articles to deflect to."),
        ("Service Catalog items published (AP-CAT)", "Required", "ECS + Customer", "Sprint 5 Wk 1", "VA fulfillment topics (password reset, equipment request) link to published catalog items."),
        ("Now Assist for ITSM license confirmed", "Required", "Customer", "Before Sprint 5", "Customer must confirm Now Assist entitlement before topic build begins."),
        ("Agent Workspace queue configured", "Required", "ECS", "Sprint 5 Wk 1", "Live-agent handoff requires at least one active IT queue in Agent Workspace."),
    ],
    config_sections=[
        ("Channel & Access", [
            ("Primary channel", "Employee Center portal embedded widget", "OOTB CSM Portal widget — no custom CSS", False),
            ("Secondary channel", "Microsoft Teams (Phase 2 only)", "Defer until portal containment baseline is established", False),
            ("Authentication", "Authenticated users only — no anonymous access", "VA personalizes greetings and prefills user context from sys_user", False),
            ("Widget placement", "Bottom-right persistent launcher (OOTB default)", "Do not move or restyle the launcher widget", False),
        ]),
        ("Conversation Settings", [
            ("Greeting message", "Hi, I'm your IT Help Assistant. How can I help you today?", "Customer to approve exact wording", True),
            ("Fallback message", "I'm not sure how to help with that. Let me connect you to a live agent.", "Triggers on 2 consecutive unrecognized intents", False),
            ("Session timeout (minutes)", "15", "OOTB default — do not reduce below 10", False),
            ("Max unresolved turns before handoff offer", "3", "After 3 unresolved turns VA proactively offers live agent", False),
        ]),
        ("Scope", [
            ("Business domains", "IT Service Management + HR (read-only FAQ)", "Limit entitlement to ITSM + HR domains", False),
            ("Go-live topic count (max)", "15", "Recommend 6-topic MVP; 15 is the ceiling for a 2-sprint window", False),
            ("Language", "English only", "Multi-language deferred to Phase 2", False),
        ]),
    ],
    raci_rows=[
        ("Confirm Now Assist license entitlement", "I", "R/A", "Customer IT Director."),
        ("Define in-scope VA topics and channels", "R/A", "I", "ECS Architect."),
        ("Approve go-live channel and domain scope", "I", "R/A", "Customer PM sign-off."),
        ("Name and engage Customer VA Admin", "I", "R/A", "Customer to identify admin before Sprint 5."),
        ("Configure VA widget in Employee Center", "R/A", "I", "ECS configures; Customer UATs."),
    ],
    consultant_guide_sections=[
        ("Channel defer rationale", "If the customer pushes for Teams on Day 1: Teams requires an Azure AD app registration, bot channel configuration in Azure, and VA bot configuration in ServiceNow. This is a 2-3 day setup. Portal widget is zero-dependency and delivers the identical NLU experience. Establish baseline, then expand."),
        ("Domain limit rationale", "Two domains (IT + HR FAQ) is the ceiling for Sprint 5 topic build. Each additional domain adds fulfillment complexity. HR FAQ is deliberately read-only — no HR record creates or approvals in scope."),
        ("VA Admin engagement", "The Customer VA Admin must be identified before Sprint 5 starts. They will add utterances during UAT, own the weekly unhandled intent review post-go-live, and build Phase 2 topics. Without this person named, the go-live is at risk."),
    ],
    adoption_rows=[
        ("We want Teams and Slack on Day 1",
         "Start with portal; add Teams/Slack in Phase 2 after baseline.",
         "Portal widget delivers identical NLU experience with zero additional configuration. Multi-channel at launch doubles setup scope.",
         "The portal widget and Teams bot use the same NLU engine and the same topics. Starting with portal lets us go live faster and prove containment before adding channels. We'll build Teams in Phase 2 with real adoption data to guide it.",
         "When portal containment exceeds 20% and customer has Azure AD bot registration resources available."),
        ("We need to cover all 10 of our business domains",
         "2 domains (IT + HR FAQ) at go-live; phase additional domains quarterly.",
         "Each domain adds topic build, utterance training, UAT, and handoff configuration. 10 domains in 2 sprints is not achievable at acceptable quality.",
         "We want every domain to work well, not have 10 domains working poorly. The OOTB pattern is to launch with the highest-volume use cases, prove the model, then expand. Your top 2 domains will cover the majority of your employees' needs.",
         "Never — always phase by domain, even post-go-live."),
    ],
    snmap_sections=[
        ("Now Assist Virtual Agent Studio", [
            ("Topic designer", "OOTB topic builder — conversation flows, panels, NLU intents", "va_topic_block, va_panel_choice, va_panel_text"),
            ("NLU Workbench", "Intent training interface — utterances stored per intent", "ml_intent, ml_solution"),
            ("VA Analytics Dashboard", "Containment rate, handoff rate, top topics, unhandled intents", "sn_va_analytics, va_conversation_log"),
        ]),
        ("Channel & Handoff", [
            ("Employee Center widget", "Embedded launcher — OOTB, placed via EC page editor", "sp_widget (VA launcher sys_id)"),
            ("Connect Chat", "Real-time handoff bridge from VA to Agent Workspace", "chat_message, chat_session, chat_queue"),
            ("Agent Workspace", "Live-agent handoff destination — OOTB queue routing", "awa_session, chat_queue"),
        ]),
    ],
)

# =============================================================================
# WB2 — Topic Design & NLU Intent Library
# =============================================================================
wb2 = TabContent(
    workbook_title="02 — Topic Design & NLU Intent Library",
    pack_name=PACK_NAME,
    purpose="Define the go-live topic set, NLU intents, sample utterances, and fulfillment actions for each VA topic in Now Assist Studio.",
    who_fills="ECS Consultant drafts topic library. Customer VA Admin reviews utterances and approves conversation scripts during Sprint 5 UAT.",
    sprint_window="Sprint 5 — topic build and NLU training complete by end of Week 10",
    estimated_effort="3-4 hours per topic (design, utterances, configure, test). 6 topics = ~1.5 days.",
    related_workbooks=["01 VA Scope & Channel Decisions", "03 Handoff & Escalation", "AP-CAT Service Catalog", "AP-13 Knowledge Management"],
    success_criteria=[
        "All go-live topics built and published in Now Assist Studio.",
        "Each topic has at least 10 NLU training utterances.",
        "Every topic passes conversation simulator test with no unhandled fallbacks.",
        "Fulfillment actions confirmed (catalog item, incident create, or KB link).",
        "UAT sign-off from Customer VA Admin on all topics.",
    ],
    process_decisions=[
        ("Topic 1: Password Reset",
         "OOTB Forgot Password catalog item as fulfillment — link directly to published catalog item.",
         "No custom LDAP reset flow. The catalog item invokes the standard password reset process already in scope."),
        ("Topic 2: Incident Create",
         "OOTB incident record producer — VA prefills caller, category, and description.",
         "Customer must confirm category/subcategory values match the agreed catalog structure (AP-CAT)."),
        ("Topic 3: Check Ticket Status",
         "OOTB sys_user open incidents lookup — display last 3 open tickets with state and assignment group.",
         "Read-only. No update action. Users can view their incidents without calling the help desk."),
        ("Topic 4: IT Equipment Request",
         "OOTB catalog item — Hardware Request — launched from VA panel.",
         "Only items published in the Service Catalog at go-live are eligible for VA fulfillment."),
        ("Topic 5: HR FAQ Deflection",
         "KB article search → return excerpt and link — no fulfillment workflow.",
         "Read-only HR knowledge deflection. HR team must publish and maintain the KB article."),
        ("Topic 6: Onboarding Checklist",
         "OOTB KB article link for new employee checklist.",
         "HR team owns the article. VA links to it — no custom onboarding workflow in scope."),
        ("Topics 7-15 (Phase 2)",
         "Prioritized from 30-day unhandled intent report after go-live.",
         "Data-driven expansion. Customer VA Admin pulls top-5 weekly unhandled intents to identify Phase 2 candidates."),
    ],
    dependencies=[
        ("Published KB articles (Topics 5, 6)", "Required", "Customer HR + IT", "Sprint 5 Wk 1", "KB articles must be published before NLU topic testing — VA links to live articles."),
        ("Published catalog items (Topics 1, 4)", "Required", "ECS", "Sprint 5 Wk 1", "Catalog items must be published before VA fulfillment actions can be configured."),
        ("Incident category list agreed (Topic 2)", "Required", "ECS + Customer", "Sprint 5 Wk 1", "Category/subcategory list must match the agreed catalog structure (AP-CAT)."),
        ("Agent Workspace queue active (all topics)", "Required", "ECS", "Sprint 5 Wk 1", "Fallback handoff on all topics requires at least one active IT queue."),
    ],
    config_sections=[
        ("NLU Standards", [
            ("Utterances per intent — minimum", "10", "ServiceNow recommends 15-20; 10 is minimum viable for sprint", False),
            ("Utterances per intent — target", "20", "Customer VA Admin to add 5-10 utterances from real user language during UAT", True),
            ("NLU confidence threshold", "0.70", "Below threshold → clarification prompt, not auto-fulfillment", False),
            ("Clarification prompt max retries", "2", "After 2 clarification attempts, offer live-agent handoff", False),
            ("NLU training wait time", "2-4 hours after publishing utterances", "NLU model retrains asynchronously — allow lead time before testing", False),
        ]),
        ("Topic Build Order", [
            ("Step 1", "Password Reset (simplest fulfillment — catalog link)", "Build simplest topics first to establish NLU baseline", False),
            ("Step 2", "Check Ticket Status (read-only lookup)", "No fulfillment action — fast to build", False),
            ("Step 3", "Incident Create (record producer)", "Requires category list confirmed", False),
            ("Step 4", "Equipment Request (catalog item launch)", "Requires catalog item published", False),
            ("Step 5", "HR FAQ Deflection (KB search)", "Requires HR KB article published", False),
            ("Step 6", "Onboarding Checklist (KB link)", "Requires onboarding KB article published", False),
        ]),
        ("UAT Criteria", [
            ("Conversation simulator", "100% of go-live topics must pass with no unhandled fallbacks", "Use Now Assist Studio built-in conversation simulator", False),
            ("Live portal test — minimum flows", "Password reset (end-to-end), incident create, KB deflection (HR FAQ), unrecognized input → handoff trigger", "Customer VA Admin performs live tests in portal", True),
            ("Topic test coverage", "All 6 go-live topics signed off by Customer VA Admin before publish", "", False),
        ]),
    ],
    raci_rows=[
        ("Define topic list and fulfillment actions", "R/A", "I", "ECS Architect leads; Customer PM approves."),
        ("Write initial NLU utterances", "R/A", "I", "ECS writes first 10 per intent."),
        ("Add domain-specific utterances from user language", "I", "R/A", "Customer VA Admin adds 5-10 per intent during UAT."),
        ("Configure conversation flow panels in Studio", "R/A", "I", "ECS configures; Customer reviews flow diagrams."),
        ("UAT — conversation simulator testing", "R", "A", "ECS leads; Customer VA Admin signs off."),
        ("UAT — live end-to-end portal testing", "I", "R/A", "Customer performs live portal UAT."),
        ("Approve go-live topic set", "I", "R/A", "Customer PM sign-off required."),
    ],
    consultant_guide_sections=[
        ("Build in Studio, not XML", "Always build topics using Now Assist Studio UI. Importing topic XML from other instances causes NLU model mismatch errors. Even if the customer has a sandbox with existing topics, rebuild in the production instance using Studio."),
        ("Utterance diversity principle", "Utterances must vary in phrasing, not just keywords. 'reset my password', 'I forgot my password', 'can't log in', 'locked out' are four distinct surface forms for the same intent. Synonyms and variations are more valuable than repeating the same phrasing."),
        ("Three OOTB fulfillment types", "Now Assist Studio supports three fulfillment action types OOTB: (1) Open catalog item, (2) Create record (incident/request), (3) Search knowledge base. Do not use scripted actions or REST calls in Sprint 5 — those are Phase 2 patterns."),
        ("Unhandled intent report", "After go-live, the VA Analytics > Unhandled Intents report shows what users asked that VA could not handle. Pull this weekly for the first 90 days. This is the Phase 2 topic backlog source. Coach the Customer VA Admin to review and flag candidates monthly."),
    ],
    adoption_rows=[
        ("Our users talk differently — the NLU won't work",
         "Add customer-specific utterances during UAT — OOTB NLU adapts.",
         "OOTB NLU is pre-trained on general English business language. Customer utterances added during UAT tune it for local vocabulary. No custom model is needed.",
         "The NLU model learns from examples — that is exactly what the UAT utterance process is for. Your VA Admin adds the phrases your team actually uses, and the model adjusts. We have done this for similar IT environments and seen 70%+ NLU accuracy after UAT tuning.",
         "If NLU accuracy is below 60% at 90 days despite 20 utterances per intent — escalate to ServiceNow Support for NLU model review."),
        ("We need the bot to handle 20 topics at go-live",
         "6-topic MVP; Phase 2 data-driven expansion.",
         "20 topics with 10 utterances each will have low NLU accuracy. 6 topics with 20 utterances each will outperform on containment.",
         "Quality beats quantity for NLU containment. Six well-trained topics will deflect more tickets than twenty undertrained ones. We build the Phase 2 topic backlog from real unhandled intent data — every topic added after go-live is backed by evidence.",
         "Never — always launch with fewer, better-trained topics."),
    ],
    snmap_sections=[
        ("Now Assist Studio", [
            ("va_topic_block", "Top-level topic record — one per intent group", "va_topic_block"),
            ("va_panel_choice", "Decision panel — presents options to user", "va_panel_choice"),
            ("va_panel_text", "Information panel — displays text response", "va_panel_text"),
            ("va_panel_live_agent", "Handoff panel — routes to Connect Chat queue", "va_panel_live_agent"),
        ]),
        ("NLU", [
            ("ml_intent", "NLU intent record — stores utterances", "ml_intent"),
            ("ml_solution", "NLU solution — links topic to trained intent model", "ml_solution"),
            ("VA Analytics", "OOTB dashboard — containment, unhandled intents, handoff rate", "sn_va_analytics, va_conversation_log"),
        ]),
    ],
)

# =============================================================================
# WB3 — Live-Agent Handoff & Escalation Configuration
# =============================================================================
wb3 = TabContent(
    workbook_title="03 — Live-Agent Handoff & Escalation Configuration",
    pack_name=PACK_NAME,
    purpose="Configure the OOTB Connect Chat handoff from Virtual Agent to Agent Workspace. Covers trigger conditions, queue routing, context transfer, and after-hours handling.",
    who_fills="ECS Consultant configures. Customer IT Lead validates queue names and confirms agent availability during UAT.",
    sprint_window="Sprint 5 — handoff configured and tested alongside VA topic UAT",
    estimated_effort="4-6 hours including Agent Workspace queue setup and UAT",
    related_workbooks=["01 VA Scope & Channel Decisions", "02 Topic Design & NLU Intent Library"],
    success_criteria=[
        "Live-agent handoff triggers correctly from all 3 escalation conditions.",
        "Conversation transcript transfers to agent on handoff.",
        "After-hours message displays correctly when queue is closed.",
        "At least 2 agents tested in Agent Workspace to receive VA handoffs.",
        "Queue wait time display confirmed in portal.",
    ],
    process_decisions=[
        ("What should trigger a live-agent handoff?",
         "Three triggers: (1) explicit user request, (2) 2 consecutive unrecognized intents, (3) 3 clarification retries exhausted.",
         "OOTB Now Assist supports all three trigger types natively. Single-trigger (explicit only) misses users who are frustrated but do not ask for a person."),
        ("Which Agent Workspace queue should VA route to?",
         "Single IT Tier 1 Support queue for all topics in the 18-week scope.",
         "Multi-queue routing by topic adds configuration complexity. Single queue is the OOTB pattern for initial deployment. Topic-based routing is Phase 2."),
        ("What context should be transferred to the agent?",
         "Last 5 VA conversation turns + user identity (name, email, dept) + open incident numbers (last 3).",
         "OOTB Connect Chat passes conversation transcript as a prepended message. User identity is pulled from sys_user automatically."),
        ("How should after-hours requests be handled?",
         "Display business hours message + create an incident for next-day follow-up. Do not route to voicemail or email callback.",
         "Incident creation is the OOTB after-hours pattern. Voicemail and email callback require integrations outside the 18-week scope."),
        ("Should queue wait time be displayed?",
         "Yes — OOTB Agent Workspace queue position estimate displayed in portal.",
         "Transparent wait time reduces user frustration and repeat handoff requests."),
    ],
    dependencies=[
        ("Agent Workspace enabled", "Required", "ECS", "Sprint 5 Wk 1", "Must be enabled and at least one IT queue configured before VA handoff can be tested."),
        ("At least 2 agents available for UAT", "Required", "Customer", "Sprint 5 UAT week", "At least 2 agents must be set to Available in Agent Workspace during UAT testing."),
        ("Business hours schedule", "Required", "Customer", "Sprint 5 Wk 1", "Customer must provide business hours (e.g. M-F 8am-5pm) and timezone for after-hours message config."),
        ("VA handoff panel added to each topic", "Required", "ECS", "Sprint 5 Wk 2", "Every topic's conversation flow must include a terminal handoff panel as the escalation path."),
    ],
    config_sections=[
        ("Handoff Configuration", [
            ("Handoff mechanism", "OOTB Connect Chat — Live Agent Handoff panel in Now Assist Studio", "Native VA panel — no scripting required", False),
            ("Target queue", "IT Tier 1 Support", "Customer to confirm exact queue name from Agent Workspace", True),
            ("Trigger 1 — explicit request", "User says 'talk to a person', 'live agent', 'human', etc.", "OOTB NLU engine recognizes handoff intent natively", False),
            ("Trigger 2 — unrecognized intents", "2 consecutive unrecognized intents → auto-escalation", "Prevents frustration loops before user must ask explicitly", False),
            ("Trigger 3 — clarification exhausted", "3 clarification retries → proactive handoff offer", "Topic-level escalation after clarification loop fails", False),
        ]),
        ("Context Transfer", [
            ("Conversation turns transferred", "5 (last 5 turns)", "Sent as prepended message to agent in Connect Chat", False),
            ("User identity transferred", "Name, email, department, open incidents (last 3)", "Pulled from sys_user and incident table automatically", False),
            ("Agent briefing instruction", "Agents must read the first Connect Chat message (VA transcript) before greeting the user", "Coach agents during handoff training session", False),
        ]),
        ("After-Hours & Queue", [
            ("Business hours", "[Customer: e.g. Monday-Friday, 8:00am-5:00pm Central]", "Customer to confirm hours and timezone", True),
            ("After-hours message", "Our team is available Monday-Friday, 8am-5pm [timezone]. I've created an incident — someone will follow up with you next business day.", "Customer to approve wording and confirm timezone", True),
            ("Queue wait time display", "Enabled — OOTB queue position estimate shown in portal", "Agent Workspace exposes queue depth OOTB", False),
            ("Handoff confirmation message", "Connecting you now. An agent will be with you shortly.", "Customer to approve wording", True),
        ]),
    ],
    raci_rows=[
        ("Configure Agent Workspace queue", "R/A", "Provide queue name + agent assignments", "ECS configures; Customer confirms queue membership."),
        ("Add handoff panels to all VA topics", "R/A", "I", "ECS adds; Customer reviews in Studio."),
        ("Configure after-hours schedule", "R/A", "Provide business hours details", "Customer confirms hours; ECS configures cmn_schedule."),
        ("UAT — trigger all 3 handoff conditions", "R", "A", "ECS leads; Customer agent performs receipt test."),
        ("UAT — validate transcript transfer to agent", "R", "A", "Both parties confirm transcript appears in agent session."),
        ("Train agents on receiving VA handoffs", "R (overview)", "A (ongoing)", "ECS delivers 30-min agent briefing in Sprint 6."),
    ],
    consultant_guide_sections=[
        ("Single queue discipline", "For the 18-week scope, route all VA handoffs to one IT Tier 1 queue. Multi-queue routing by topic adds configuration scope and routing logic that is not warranted in Sprint 5. Log topic-based routing as a Phase 2 item if the customer raises it."),
        ("After-hours test method", "Test after-hours handling by temporarily changing the business hours schedule (cmn_schedule) to a closed window. Confirm the after-hours message displays in portal. Revert the schedule immediately after testing."),
        ("Transcript format coaching", "The OOTB transcript appears as the first message in the agent's Connect Chat session, prepended automatically. Coach agents: 'The first message in every VA transfer is the conversation history — read it before saying hello.' This prevents agents from asking users to repeat what they already told the bot."),
        ("ACD integration pushback", "If the customer has Genesys, Five9, or another ACD and insists on routing there: this is a post-go-live integration project. It requires middleware, custom event payloads, and ACD-side bot routing configuration. None of this is OOTB and none is in 18-week scope. Log as Phase 2."),
    ],
    adoption_rows=[
        ("Route handoffs to our existing ACD (Genesys / Five9)",
         "OOTB Connect Chat → Agent Workspace is the certified handoff target.",
         "Third-party ACD integration requires middleware, custom event payloads, and license coordination — not OOTB and not achievable in 18-week sprint.",
         "Agent Workspace is ServiceNow's certified real-time chat handoff platform. ACD integration is a Phase 2 project we can scope once go-live is stable. Your agents use Agent Workspace for all ServiceNow work anyway — the VA handoff lands in the same place.",
         "Post-go-live Phase 2 project with dedicated integration sprint."),
        ("Different queues per topic",
         "Single IT Tier 1 queue at go-live; topic-based routing in Phase 2.",
         "Multi-queue routing in Sprint 5 doubles handoff configuration scope. Single-queue is the OOTB-aligned initial deployment pattern.",
         "One queue at go-live means every handoff lands where your best agents are. Topic-based routing is a Phase 2 enhancement — once we know which topics generate the most handoffs, we can route them intelligently. Guessing now adds complexity without data.",
         "Phase 2 — after 90 days of handoff volume data."),
    ],
    snmap_sections=[
        ("Connect Chat & Agent Workspace", [
            ("Connect Chat session", "Real-time messaging bridge — VA to agent", "chat_session, chat_message"),
            ("Chat queue", "Agent Workspace queue — receives VA handoffs", "chat_queue"),
            ("AWA session", "Agent Workspace live-agent session record", "awa_session"),
            ("VA handoff panel", "OOTB Now Assist Studio panel — drops into Connect Chat", "va_panel_live_agent"),
        ]),
        ("Scheduling & After-Hours", [
            ("Business hours schedule", "OOTB cmn_schedule used for after-hours logic in VA flow", "cmn_schedule, cmn_schedule_span"),
            ("After-hours incident creation", "OOTB incident record producer triggered by after-hours VA flow", "incident"),
        ]),
    ],
)

# =============================================================================
# WB4 — VA Analytics & Adoption Measurement
# =============================================================================
wb4 = TabContent(
    workbook_title="04 — VA Analytics & Adoption Measurement",
    pack_name=PACK_NAME,
    purpose="Define KPIs, OOTB dashboards, and review cadence for measuring Virtual Agent containment and adoption post-go-live.",
    who_fills="ECS Consultant configures OOTB dashboards in Sprint 6. Customer VA Admin owns ongoing reporting after go-live.",
    sprint_window="Sprint 6 — KPI baseline set at go-live; 30/60/90-day targets defined here",
    estimated_effort="2 hours for dashboard activation and KPI baseline setup",
    related_workbooks=["01 VA Scope & Channel Decisions", "02 Topic Design & NLU Intent Library", "05 Go-Live Readiness"],
    success_criteria=[
        "OOTB VA Analytics dashboard accessible to Customer VA Admin at go-live.",
        "Containment rate baseline established on Day 1.",
        "30/60/90-day KPI targets agreed with Customer PM.",
        "Weekly unhandled intent review cadence established.",
        "30-day review meeting scheduled before go-live.",
    ],
    process_decisions=[
        ("What is the primary KPI for Virtual Agent success?",
         "Containment rate — percentage of sessions resolved without live-agent handoff.",
         "OOTB VA Analytics tracks containment natively. It is the single most meaningful measure of VA effectiveness."),
        ("What are realistic containment targets?",
         "15% at 30 days; 30% at 90 days.",
         "15% is realistic for a 6-topic MVP. 30% at 90 days is achievable with utterance tuning and 2-3 Phase 2 topics added. Overpromising creates stakeholder risk."),
        ("How often should VA analytics be reviewed?",
         "Weekly for first 90 days (Customer VA Admin); 30/60/90-day reviews with ECS.",
         "Weekly cadence catches NLU quality issues before they compound. ECS reviews at 30/60/90 days to assess Phase 2 topic candidates."),
        ("Should custom Performance Analytics indicators be built?",
         "No — use OOTB VA Analytics for the entire 18-week scope.",
         "OOTB VA Analytics provides containment, handoff rate, session volume, and unhandled intents. Custom PA indicators add configuration scope not warranted in Sprint 6."),
        ("What triggers a Phase 2 topic build?",
         "A single unhandled intent concept exceeding 20 sessions per week for 2 consecutive weeks.",
         "Data-driven threshold. Prevents guessing about what topics to add next."),
    ],
    dependencies=[
        ("Now Assist VA Analytics entitlement", "Required", "Customer", "Before Sprint 6", "Confirm Now Assist Analytics module is included in license before go-live."),
        ("Go-live date confirmed", "Required", "Customer PM", "Sprint 6 Wk 1", "KPI clock starts on Day 1 of production launch. Baseline date must be recorded."),
        ("Customer VA Admin identified and trained", "Required", "Customer", "Sprint 6", "Admin must know how to pull OOTB analytics reports before handover."),
    ],
    config_sections=[
        ("KPI Targets", [
            ("Primary KPI", "Containment rate (% sessions resolved without handoff)", "OOTB VA Analytics tracks natively", False),
            ("Secondary KPI", "Average session duration (minutes)", "High duration = low NLU confidence — investigate if >5 min avg", False),
            ("Tertiary KPI", "Unhandled intent volume — top 5 weekly", "Phase 2 topic backlog source", False),
            ("Target — 30 days", "15% containment", "Based on 6-topic MVP go-live set with 10-20 utterances", False),
            ("Target — 60 days", "22% containment", "With utterance tuning post-30-day review", False),
            ("Target — 90 days", "30% containment", "With utterance tuning + 2-3 Phase 2 topics", False),
        ]),
        ("Review Cadence", [
            ("Weekly review (Customer)", "VA Admin pulls OOTB top-5 unhandled intents report every Monday", "Customer VA Admin owns — no ECS involvement in weekly pull", True),
            ("30-day review", "ECS + Customer PM + VA Admin — containment vs. 15% target; Phase 2 topic candidates", "ECS schedules before Sprint 6 close", False),
            ("60-day review", "Customer PM + VA Admin — adjust utterances; confirm Phase 2 topic builds started", "Customer-led; ECS advisory only", False),
            ("90-day review", "ECS + Customer PM — Phase 2 assessment; stabilization sign-off", "Marks end of ECS hypercare obligations", False),
            ("High-handoff alert", ">70% handoff rate in any week triggers ECS review call", "ECS + Customer VA Admin troubleshoot NLU coverage", False),
        ]),
        ("Dashboard Access", [
            ("OOTB dashboard location", "Now Assist > Virtual Agent Analytics", "No custom PA indicators — OOTB only for 18-week scope", False),
            ("Access role required", "sn_va_analyst (OOTB)", "Customer VA Admin must have this role before go-live", True),
        ]),
    ],
    raci_rows=[
        ("Activate VA Analytics dashboard", "R/A", "Verify access", "ECS activates; Customer VA Admin confirms visibility."),
        ("Record go-live baseline date", "R", "A", "ECS records; Customer PM confirms."),
        ("Pull weekly unhandled intent report", "N/A", "R/A", "Customer VA Admin owns weekly pull."),
        ("30-day containment review", "R", "A", "ECS presents analysis; Customer PM decides Phase 2 scope."),
        ("Phase 2 topic prioritization", "I (advise)", "R/A (decide)", "Customer decides with ECS input from unhandled intent data."),
        ("Ongoing monthly reporting (post-90 days)", "N/A", "R/A", "Customer VA Admin owns post-stabilization."),
    ],
    consultant_guide_sections=[        ("Why 15% at 30 days is right", "A 6-topic VA with 10-20 utterances each will not cover the full vocabulary of a user base at launch. 15% is a credible, achievable target. Setting it at 30% or higher on day 1 creates stakeholder risk when the inevitable dip in week 2 (as novelty fades) occurs. Under-promise, over-deliver."),
        ("Utterance tuning lever", "The fastest way to improve containment after go-live is to add utterances from the weekly unhandled intent report. Coach the Customer VA Admin to identify the top 3 unhandled phrasing variants each week and add them as utterances to the relevant topic. This alone can move containment 5-10 points between 30 and 90 days."),
        ("Phase 2 topic trigger discipline", "The 20-sessions/2-weeks threshold prevents the customer from adding topics based on gut feel or a single complaint. Data-driven topic expansion is the OOTB pattern. When a threshold is crossed, add it to the Phase 2 backlog -- not necessarily to the current sprint."),
        ("Redirect PA requests", "Customers with existing PA deployments will ask for VA PA indicators. Redirect to OOTB VA Analytics for the 90-day stabilization period. PA indicator configuration adds a sprint of work. The OOTB dashboard is sufficient to prove or disprove containment at the scale of an 18-week engagement."),
    ],
    adoption_rows=[
        ("The 30% target is too low -- we expect 60% by month 3",
         "15% at 30 days; 30% at 90 days -- industry-aligned for a 6-topic OOTB deployment.",
         "Containment scales with topic count and utterance quality. A 6-topic set cannot reliably contain 60% of diverse IT requests at 90 days.",
         "A 30% containment rate means 30% of employees resolve their issue without calling the help desk -- that is hundreds of saved tickets per month for a 1,000-person organization. The OOTB pattern is to land at 30% and grow to 50%+ over 6-12 months as the topic library expands. We deliver the foundation; Phase 2 delivers the scale.",
         "When topic library exceeds 15 and utterance coverage is validated across all topics."),
        ("We need a custom PA scorecard for VA",
         "OOTB VA Analytics covers all 18-week reporting needs.",
         "Custom PA indicators add sprint scope and are not needed until baseline is established at 90 days.",
         "The OOTB VA Analytics dashboard shows everything you need to manage VA health: containment rate, handoff rate, top topics, and unhandled intents. Once you have 90 days of baseline data, we can design a PA scorecard in Phase 2 grounded in real patterns rather than assumptions.",
         "Phase 2 -- after 90-day stabilization baseline established."),
    ],
    snmap_sections=[
        ("VA Analytics", [
            ("VA Analytics dashboard", "OOTB Now Assist module -- containment, handoff, session volume, top topics, unhandled intents", "sn_va_analytics"),
            ("Conversation log", "Raw session data -- queryable for custom reporting post-go-live", "va_conversation_log"),
            ("VA Analyst role", "sn_va_analyst -- grants access to VA Analytics dashboard", "sys_user_role"),
        ]),
        ("Phase 2 Reference", [
            ("Performance Analytics indicators (Phase 2)", "Custom KPI indicators for executive scorecard -- out of scope for 18-week", "pa_indicator, pa_scorecard"),
        ]),
    ],
)

# =============================================================================
# WB5 -- VA Go-Live Readiness & Rollout Plan
# =============================================================================
wb5 = TabContent(
    workbook_title="05 -- VA Go-Live Readiness & Rollout Plan",
    pack_name=PACK_NAME,
    purpose="Define the pre-launch UAT checklist, rollout approach, and communication plan for Virtual Agent go-live at the end of Sprint 6.",
    who_fills="ECS PM + Customer PM jointly complete. ECS confirms technical checklist items; Customer confirms comms and change management items.",
    sprint_window="Sprint 6 -- complete by end of Week 12",
    estimated_effort="3-4 hours across ECS PM and Customer PM",
    related_workbooks=["01 VA Scope & Channel Decisions", "04 VA Analytics & Adoption Measurement", "AP-15 Employee Center Go-Live"],
    success_criteria=[
        "All 6 go-live topics pass UAT (simulator + live portal).",
        "Agent Workspace queue active with at least 2 available agents.",
        "VA Analytics dashboard accessible to Customer VA Admin.",
        "Go-live communication sent to all employees 5 days before launch.",
        "IT Director + ECS PM sign-off completed.",
        "VA widget published to Employee Center production.",
    ],
    process_decisions=[
        ("Full launch or phased rollout?",
         "Full employee base at go-live. No phased rollout by department.",
         "VA widget is passive -- users choose to engage. No forced adoption risk. Phased rollout by department adds access control configuration with no meaningful risk reduction."),
        ("When should go-live communication be sent?",
         "IT leadership email + intranet post 5 business days before go-live.",
         "5 days gives help desk agents time to prepare and gives employees a preview. Same-day announcements reduce adoption in week 1."),
        ("Should there be a pilot group?",
         "Optional: 10-person IT team pilot 3 days before full launch. Not required.",
         "Useful for customers with strong change management culture. Not required if UAT was thorough."),
        ("Who signs off on go-live?",
         "Customer IT Director + ECS PM must both sign UAT completion before widget is published.",
         "Dual sign-off prevents premature publication and protects the ECS team if post-launch issues arise."),
        ("What is the hypercare scope and duration?",
         "2 weeks post-go-live. ECS available for utterance tuning and NLU adjustments only.",
         "Hypercare covers: utterance additions, NLU threshold adjustment, handoff queue corrections. New topic builds are billable Phase 2 work."),
    ],
    dependencies=[
        ("Employee Center live (AP-15)", "Required", "ECS", "Before Sprint 6 go-live", "VA widget embedded in EC -- EC must be published to production before VA launch."),
        ("All 6 topics UAT passed", "Required", "ECS + Customer", "Sprint 6 Wk 1", "Every topic must pass simulator AND live portal test before widget is published."),
        ("Agent Workspace queue active", "Required", "ECS + Customer", "Sprint 6 Wk 1", "At least 2 agents must be available during go-live week to handle handoff spikes."),
        ("VA Analytics accessible", "Required", "ECS", "Sprint 6 Wk 1", "Customer VA Admin must access analytics on Day 1."),
        ("Go-live communication sent", "Required", "Customer comms team", "5 business days before launch", "IT leadership email and intranet post must be sent before widget is published."),
    ],
    config_sections=[
        ("Go-Live Schedule", [
            ("Target go-live date", "End of Sprint 6 (Week 12)", "Customer to confirm -- must avoid change freeze windows", True),
            ("Communication send date", "5 business days before go-live", "Customer IT Director sends email; comms team posts to intranet", True),
            ("Widget activation method", "Employee Center page editor -- set VA widget Published flag to True", "ECS publishes; Customer PM witnesses", False),
        ]),
        ("Post-Launch Monitoring", [
            ("ECS monitoring window", "Daily VA Analytics review for first 5 business days", "ECS flags anomalies to Customer PM within 4 business hours", False),
            ("Hypercare scope", "Utterance tuning, NLU threshold adjustment, handoff queue corrections only", "New topic builds are billable Phase 2 -- not included in hypercare", False),
            ("Hypercare duration", "2 weeks post-go-live", "Beyond 2 weeks is T&M or support contract", False),
            ("30-day review", "ECS + Customer PM + VA Admin -- scheduled before Sprint 6 close", "Review containment vs. 15% target; agree Phase 2 backlog", False),
        ]),
        ("UAT Sign-Off Checklist", [
            ("Topic 1 Password Reset -- simulator pass", "[ECS to initial]", "No unhandled fallback in simulator", True),
            ("Topic 2 Incident Create -- simulator pass", "[ECS to initial]", "", True),
            ("Topic 3 Check Status -- simulator pass", "[ECS to initial]", "", True),
            ("Topic 4 Equipment Request -- simulator pass", "[ECS to initial]", "", True),
            ("Topic 5 HR FAQ -- simulator pass", "[ECS to initial]", "", True),
            ("Topic 6 Onboarding -- simulator pass", "[ECS to initial]", "", True),
            ("Live portal -- password reset end-to-end", "[Customer VA Admin to initial]", "Must complete fulfillment in portal", True),
            ("Live portal -- handoff trigger confirmed", "[Customer VA Admin to initial]", "Unrecognized input triggers handoff offer", True),
            ("Agent Workspace receipt confirmed", "[Customer agent to initial]", "Agent receives VA transcript in Connect Chat", True),
            ("IT Director sign-off", "[Customer IT Director signature]", "", True),
            ("ECS PM sign-off", "[ECS PM signature]", "", True),
        ]),
    ],
    raci_rows=[
        ("Complete UAT sign-off checklist", "R", "A", "ECS confirms technical; Customer IT Director signs."),
        ("Draft go-live communication", "Review + edit", "R/A", "Customer comms team drafts; ECS reviews for accuracy."),
        ("Send IT leadership email", "N/A", "R/A", "Customer IT Director sends."),
        ("Publish VA widget to EC production", "R/A", "Witness", "ECS publishes; Customer PM witnesses."),
        ("Monitor analytics -- Days 1-5", "R/A", "N/A", "ECS daily review during hypercare."),
        ("Schedule 30-day review", "R", "A", "ECS PM schedules before Sprint 6 close."),
    ],
    consultant_guide_sections=[
        ("UAT pass criteria", "All 6 topics must complete end-to-end in the conversation simulator with no unhandled fallbacks. Minimum live portal tests: password reset (full fulfillment), incident create, KB deflection (HR FAQ), and unrecognized input to handoff trigger. These 4 live flows represent the highest-volume VA interaction patterns."),
        ("Widget publish risk", "Publishing the VA widget is instant and affects all portal users. There is no staging preview for portal users. Do a final simulator test immediately before publishing. If possible, publish on a Tuesday or Wednesday morning (lower traffic) so the team can respond to early feedback."),
        ("Hypercare scope protection", "Be explicit before go-live: hypercare covers tuning existing topics (utterances, thresholds, queue names). Building new topics is Phase 2 billable work. Log any new topic requests to the Phase 2 backlog during hypercare."),
        ("Communication content guide", "The go-live email must include: (1) what VA does and does not do, (2) portal link, (3) the 6 topics it handles, (4) how to reach a live agent. Avoid overselling. Users who feel VA was oversold become hostile; users who feel it was accurately described become advocates."),
    ],
    adoption_rows=[
        ("Launch to one department first",
         "Full employee base on Day 1 -- VA widget is passive.",
         "No meaningful risk difference between phased and full launch for a passive widget. Phased rollout adds access control configuration and slows adoption data collection.",
         "The VA widget is like a help button in the portal corner -- no one is forced to use it. Full launch gives us real adoption data from day 1 across all user types. A phased rollout means we only see one department vocabulary and miss the patterns that drive Phase 2 topics.",
         "Never for VA -- phased rollout adds configuration without meaningful risk reduction."),
        ("Delay go-live until we have 20 topics",
         "6 well-trained topics at go-live; expand via Phase 2.",
         "20 under-trained topics will produce lower containment than 6 well-trained ones. Go-live quality is about utterance coverage, not topic count.",
         "More topics is not better if the training data is thin. Six topics with 20 utterances each will outperform twenty topics with 8 utterances each on every containment metric. We go live with what is proven and grow the library from unhandled intent data.",
         "Never -- always prioritize topic quality over quantity at go-live."),
    ],
    snmap_sections=[
        ("Go-Live Actions", [
            ("Employee Center page editor", "VA widget publication -- set Published flag to activate in portal", "sp_page, sp_widget"),
            ("VA Analytics baseline", "Record first session date as go-live baseline", "sn_va_analytics"),
        ]),
        ("Change Management (Optional)", [
            ("Change Request", "Customer may require RFC for VA widget activation -- coordinate with CAB if applicable", "change_request"),
        ]),
    ],
)

# =============================================================================
# README
# =============================================================================
def build_readme():
    meta = DocMeta(
        eyebrow="ACCELERATOR PACK",
        title="Virtual Agent\nAccelerator Pack",
        subtitle="OOTB Now Assist VA -- Scope, NLU Design, Handoff, Analytics, Go-Live",
        doc_id="AP-16",
        version="1.0",
        status="Released",
        audience="ECS Consultants (Internal) + Customer IT Lead / VA Admin (selected tabs)",
        running_header_label="Virtual Agent Accelerator Pack · ECS Federal",
        confidentiality="Internal Use Only · Confidential",
    )
    doc = EcsDocument(meta=meta)
    doc.add_cover_page()
    doc.h1("Pack Overview")
    doc.para(
        "AP-16 guides the ECS team through configuring the ServiceNow OOTB Now Assist "
        "Virtual Agent during Month 3 (Sprints 5-6) of the 18-week engagement. The pack "
        "covers channel and scope decisions, NLU topic design, live-agent handoff via "
        "Connect Chat and Agent Workspace, analytics KPIs, and go-live readiness. "
        "All deliverables are OOTB -- no custom ML models, no third-party ACD integration, "
        "and no JavaScript scripting within topic flows."
    )
    doc.h1("Workbook Inventory")
    doc.table(
        headers=["#", "Workbook", "Owner", "Sprint"],
        rows=[
            ("WB1", "VA Scope & Channel Decisions", "ECS + Customer PM", "Sprint 5"),
            ("WB2", "Topic Design & NLU Intent Library", "ECS + Customer VA Admin", "Sprint 5"),
            ("WB3", "Live-Agent Handoff & Escalation Configuration", "ECS + Customer IT Lead", "Sprint 5"),
            ("WB4", "VA Analytics & Adoption Measurement", "ECS + Customer VA Admin", "Sprint 6"),
            ("WB5", "VA Go-Live Readiness & Rollout Plan", "ECS PM + Customer PM", "Sprint 6"),
        ],
    )
    doc.h1("Key OOTB Decisions")
    doc.para(
        "Channel: Employee Center portal at go-live; Teams/Slack deferred to Phase 2. "
        "Topics: 6-topic MVP recommended; 15 is the ceiling for a 2-sprint window. "
        "NLU: OOTB Now Assist Studio -- 10-20 utterances per intent; confidence threshold 0.70. "
        "Handoff: OOTB Connect Chat to Agent Workspace IT Tier 1 queue. "
        "After-hours: display message and create incident -- no ACD callback. "
        "Analytics: OOTB VA Analytics dashboard only -- no custom PA in 18-week scope. "
        "KPI targets: 15% containment at 30 days; 30% at 90 days."
    )
    doc.save(os.path.join(PACK_DIR, "00_README_Virtual_Agent_Pack.docx"))
    print(f"README saved: {os.path.join(PACK_DIR, '00_README_Virtual_Agent_Pack.docx')}")

# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    print("Building Virtual Agent Accelerator Pack...")
    workbooks = [
        ("01_va_scope_channel.xlsx", wb1),
        ("02_topic_design_nlu.xlsx", wb2),
        ("03_handoff_escalation.xlsx", wb3),
        ("04_va_analytics.xlsx", wb4),
        ("05_golive_readiness.xlsx", wb5),
    ]
    for filename, content in workbooks:
        out_path = os.path.join(PACK_DIR, filename)
        build_workbook(content, out_path)
        print(f"  check {filename}")
    print("Virtual Agent Accelerator Pack complete.")
