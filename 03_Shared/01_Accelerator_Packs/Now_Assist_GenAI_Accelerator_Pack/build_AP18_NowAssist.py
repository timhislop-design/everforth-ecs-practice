"""
build_AP18_NowAssist.py -- AP-18 Now Assist / GenAI Accelerator Pack
Covers: Now Assist for ITSM -- text summarization, search augmentation,
resolution notes generation, and admin configuration.
Sprint window: Month 3 (Sprints 5-6)
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "03_Shared", "00_Templates_and_Branding"))
from accelerator_pack_builder import TabContent, build_workbook
from ecs_template import EcsDocument, DocMeta

PACK_DIR = HERE
PACK_NAME = "Now Assist / GenAI Accelerator Pack"

wb1 = TabContent(
    workbook_title="01 -- Now Assist Scope & Entitlement",
    pack_name=PACK_NAME,
    purpose="Confirm Now Assist for ITSM entitlement, define which GenAI skills to activate at go-live, and establish the OOTB-first boundaries for the 18-week scope.",
    who_fills="ECS Consultant leads. Customer IT Director and ITSM Process Owner confirm entitlement and scope decisions.",
    sprint_window="Sprint 5 -- scope locked by end of Week 9",
    estimated_effort="2-3 hours with Customer IT Director",
    related_workbooks=["02 Text Summarization", "03 Search Augmentation", "04 Resolution Notes", "AP-16 Virtual Agent", "AP-17 Predictive Intelligence"],
    success_criteria=[
        "Now Assist for ITSM license confirmed and activated.",
        "GenAI skills to activate at go-live agreed (max 3 for 18-week scope).",
        "Now Assist Admin named (can be same as VA Admin).",
        "Data privacy and content filtering settings reviewed with customer.",
        "AI Search index scope confirmed.",
    ],
    process_decisions=[
        ("Which Now Assist skills should be activated at go-live?",
         "Three OOTB skills: (1) Incident Summarization, (2) Resolution Notes Generation, (3) Now Assist Search (AI Search). Virtual Agent (AP-16) is separately scoped.",
         "These three deliver the highest immediate agent productivity value with the lowest configuration overhead. Case Summarization (CSM) and GenAI for Change are Phase 2."),
        ("Should Now Assist generate content automatically or on agent demand?",
         "On agent demand only (OOTB default). Agent clicks Generate to trigger AI output.",
         "On-demand preserves agent control and avoids unwanted AI content appearing in records. Automatic generation is a Phase 2 setting after agents are comfortable with quality."),
        ("How should AI-generated content be labeled in the UI?",
         "OOTB AI badge is enabled -- all AI-generated text is visibly labeled. Do not disable the badge.",
         "Regulatory and policy environments (especially federal) require clear disclosure of AI-generated content. The OOTB badge satisfies this requirement."),
        ("Should Now Assist Search replace or augment the existing search bar?",
         "Augment -- AI Search results appear alongside standard search results (OOTB). Do not disable standard search.",
         "AI Search improves relevance but can miss exact-match queries where keyword search excels. Both run in parallel OOTB."),
        ("What data does Now Assist send to the AI model?",
         "Only field values from the incident/request record in scope. No external data leaves the instance unless explicitly configured.",
         "ServiceNow Now Assist uses a managed LLM (Azure OpenAI via ServiceNow's infrastructure). Customer data is not used to train the base model. Review with Customer CISO before Sprint 5."),
    ],
    dependencies=[
        ("Now Assist for ITSM license", "Required", "Customer", "Before Sprint 5", "Cannot activate any Now Assist skill without entitlement confirmed."),
        ("Now Platform Tokyo or later (Washington DC recommended)", "Required", "Customer IT", "Before Sprint 5", "Now Assist skills require Washington DC release minimum."),
        ("CISO/Privacy review of Now Assist data handling", "Required", "Customer CISO", "Before Sprint 5", "Federal customers must confirm AI data handling complies with their ATO/privacy policy."),
        ("Published KB articles (AP-13)", "Required", "ECS", "Sprint 5 Wk 1", "AI Search indexes published KB articles -- without them search has nothing to augment."),
        ("Incidents with resolution notes in history", "Recommended", "Customer", "Sprint 5 Wk 1", "Resolution Notes Generation quality improves with a corpus of past good resolution notes."),
    ],
    config_sections=[
        ("Now Assist Activation", [
            ("Now Assist for ITSM skill -- Incident Summarization", "Activate Sprint 5 Wk 1", "Summarizes incident work notes and comments for agents and stakeholders", False),
            ("Now Assist for ITSM skill -- Resolution Notes Generation", "Activate Sprint 5 Wk 1", "Generates draft resolution notes from incident history", False),
            ("Now Assist Search (AI Search)", "Activate Sprint 5 Wk 1", "Semantic search across KB, catalog, and incidents", False),
            ("Case Summarization (CSM)", "Defer to Phase 2", "Out of scope for ITSM-focused 18-week engagement", False),
            ("GenAI for Change", "Defer to Phase 2", "Change assessment generation needs mature Change process first", False),
        ]),
        ("Governance Settings", [
            ("AI badge on generated content", "Enabled (OOTB default -- do not disable)", "Required for transparency and federal compliance", False),
            ("On-demand vs. automatic generation", "On-demand (agent clicks Generate)", "Preserves agent control; automatic is Phase 2", False),
            ("Content filtering", "Enabled -- OOTB responsible AI filters active", "Do not disable content filtering in any federal deployment", False),
            ("Data sent to LLM", "Incident fields in scope only -- no PII beyond what is in the record", "Review with Customer CISO before activation", True),
        ]),
    ],
    raci_rows=[
        ("Confirm Now Assist license entitlement", "I", "R/A", "Customer IT Director."),
        ("CISO data handling review", "I (provide documentation)", "R/A", "Customer CISO."),
        ("Activate Now Assist skills in instance", "R/A", "I", "ECS Consultant."),
        ("Name Now Assist Admin", "I", "R/A", "Customer IT Director."),
        ("Communicate AI tool availability to agents", "Review", "R/A", "Customer IT Manager sends comms."),
    ],
    consultant_guide_sections=[
        ("Federal CISO conversation", "Many federal customers have ATO requirements that need to be reviewed before any AI tool is enabled. ServiceNow publishes a Now Assist Security and Privacy whitepaper -- share this with the Customer CISO before Sprint 5. Do not activate Now Assist without written confirmation from the CISO or their delegate."),
        ("Three skill limit rationale", "Three OOTB skills in 2 sprints is the right scope ceiling. Each skill needs configuration, agent training, and UAT. More than three skills in the 18-week window spreads attention too thin and produces lower adoption across all skills."),
        ("AI badge requirement", "Never advise disabling the AI badge. The OOTB disclosure badge is not optional for responsible deployment -- especially in federal environments where AI-generated content in records may have downstream legal or audit implications."),
    ],
    adoption_rows=[
        ("We want Now Assist to automatically update records",
         "On-demand at go-live; auto-generation after agent trust is established.",
         "Auto-generation in Sprint 5 means AI content appears before agents understand its quality. Trust must be built first.",
         "Starting on-demand means every agent sees Now Assist in action before anything is automatically written to a record. Once agents trust the output quality -- which typically takes 3-4 weeks -- we can enable automatic generation for specific skills like resolution notes. We do not skip the trust-building phase.",
         "After 30 days of on-demand use with positive agent feedback."),
    ],
    snmap_sections=[
        ("Now Assist Core", [
            ("sn_now_assist", "Now Assist skill configuration table", "sn_now_assist"),
            ("sn_now_assist_skill", "Individual skill records (summarize, generate, search)", "sn_now_assist_skill"),
            ("Now Assist Admin Console", "OOTB admin console -- skill activation, monitoring, content filtering", "Now Assist > Admin Console"),
        ]),
    ],
)

wb2 = TabContent(
    workbook_title="02 -- Incident & Case Summarization",
    pack_name=PACK_NAME,
    purpose="Configure the OOTB Now Assist Incident Summarization skill to generate concise summaries of incident work notes and comments for agents and stakeholders.",
    who_fills="ECS Consultant configures. Customer Service Desk Lead and agents review during UAT.",
    sprint_window="Sprint 5 -- skill active and tested by end of Week 10",
    estimated_effort="3-4 hours including configuration and agent UAT",
    related_workbooks=["01 Now Assist Scope", "04 Resolution Notes Generation"],
    success_criteria=[
        "Incident Summarization skill active on Incident form.",
        "Generate Summary button visible to agents on open incidents.",
        "Summary output tested on at least 10 real incidents.",
        "AI badge visible on all generated summaries.",
        "Agent UAT sign-off from Service Desk Lead.",
    ],
    process_decisions=[
        ("What should the summary include?",
         "OOTB: most recent 5 work notes + caller description + current state. Do not customize the prompt template in 18-week scope.",
         "The OOTB prompt is tuned for incident context. Custom prompts require testing and iteration that is not scoped for Sprint 5."),
        ("Who can generate a summary -- agents only or also customers?",
         "Agents and IT staff only (OOTB default). Do not expose summary generation to the employee portal in 18-week scope.",
         "Customer-facing summarization adds content review requirements. Agent-facing is the safe starting point."),
        ("Should summaries be saved to the incident record?",
         "Optional -- agent can copy summary to work notes. Do not auto-write to resolution field.",
         "Auto-write to resolution field bypasses agent review. Agent copy-and-edit preserves accountability and improves summary quality through light editing."),
        ("Should major incident stakeholders receive AI summaries?",
         "Yes for Major Incidents (P1/P2) -- enable the OOTB Major Incident Stakeholder Summary feature.",
         "This is one of the highest-value use cases: automatically drafting stakeholder update emails during a major incident saves the incident manager 15-30 minutes per update cycle."),
    ],
    dependencies=[
        ("Now Assist for ITSM activated (WB1)", "Required", "ECS", "Sprint 5 Wk 1", "Summarization skill requires Now Assist active."),
        ("Incidents with 3+ work notes in history", "Recommended", "Customer", "Sprint 5 Wk 1", "Summarization quality requires sufficient work note history to summarize."),
    ],
    config_sections=[
        ("Summarization Skill Configuration", [
            ("Skill", "Summarize Incident (OOTB Now Assist skill)", "Select from Now Assist skill library -- no custom LLM prompt", False),
            ("Trigger", "On-demand -- agent clicks Generate Summary button", "Button appears on Incident form header", False),
            ("Input scope", "Work notes (last 5) + short description + description", "OOTB default input scope", False),
            ("Output placement", "Inline summary panel below incident header (OOTB)", "Do not add a custom field for summary storage", False),
            ("AI badge", "Enabled (OOTB -- do not disable)", "All generated summaries display AI badge", False),
            ("Auto-save to record", "Disabled -- agent copies manually if desired", "Preserves agent review and accountability", False),
        ]),
        ("Major Incident Stakeholder Summary", [
            ("Enable for P1/P2", "Yes -- OOTB Major Incident Stakeholder Update feature", "Generates draft stakeholder email from current incident state", False),
            ("Recipient list", "IT Director, affected business owners", "Customer to confirm distribution list", True),
            ("Cadence", "On-demand -- Major Incident Manager generates at each update cycle", "Typically every 30-60 minutes during active P1", False),
        ]),
    ],
    raci_rows=[
        ("Configure Incident Summarization skill", "R/A", "I", "ECS Consultant."),
        ("Enable Major Incident stakeholder summary", "R/A", "Confirm P1/P2 distribution list", "ECS configures; Customer IT Manager provides list."),
        ("UAT -- 10 incident summaries reviewed by agents", "R", "A", "ECS facilitates; Service Desk Lead signs off."),
        ("Agent briefing on summarization skill", "R/A", "Attend", "ECS delivers 30-min briefing with live demo."),
    ],
    consultant_guide_sections=[
        ("UAT selection criteria", "Choose UAT incidents that vary in length and complexity: 2 short incidents (1-2 work notes), 4 medium (3-5 work notes), 4 long (10+ work notes). Long incidents show the highest summarization value and are most convincing for agents who are skeptical."),
        ("Major Incident pitch", "The major incident stakeholder summary is often the single most compelling Now Assist demo for IT leadership. Run a live demo during Sprint 5 kickoff: pull a real historical P1, click Generate, show the stakeholder email draft. Leadership buys in immediately."),
        ("Quality calibration", "Now Assist summaries are drafts. Coach agents that light editing is expected -- the AI saves 80% of the writing time, not 100%. Agents who expect perfection become disappointed; agents who expect a strong draft become advocates."),
    ],
    adoption_rows=[
        ("We want summaries emailed automatically to managers",
         "On-demand Major Incident summary with agent review before send.",
         "Auto-email without review risks sending inaccurate AI content to leadership. Review step is mandatory.",
         "The Major Incident Manager reviews the AI draft -- which takes 30 seconds -- and clicks Send. We save the writing time and preserve the human verification step. That combination is exactly what responsible AI use looks like in a federal environment.",
         "Never auto-send AI-generated content to stakeholders without review."),
    ],
    snmap_sections=[
        ("Summarization", [
            ("sn_now_assist_skill (Summarize)", "Now Assist summarization skill record", "sn_now_assist_skill"),
            ("incident (work_notes)", "Source field for summarization input", "incident.work_notes"),
            ("Major Incident Management", "OOTB MIM module -- stakeholder update feature", "em_alert, major_incident_state"),
        ]),
    ],
)

wb3 = TabContent(
    workbook_title="03 -- Now Assist Search (AI Search Augmentation)",
    pack_name=PACK_NAME,
    purpose="Configure OOTB Now Assist Search to augment the ServiceNow search experience with semantic AI results across KB articles, catalog items, and incidents.",
    who_fills="ECS Consultant configures search index scope. Customer KB Admin confirms content quality for indexing.",
    sprint_window="Sprint 5 -- AI Search active and tested by end of Week 10",
    estimated_effort="3-4 hours including index configuration and search quality UAT",
    related_workbooks=["01 Now Assist Scope", "AP-13 Knowledge Management", "AP-CAT Service Catalog", "AP-15 Employee Center"],
    success_criteria=[
        "Now Assist Search active in Employee Center and Service Portal.",
        "Search index includes KB articles, catalog items, and incidents (read-only).",
        "AI-generated answer panel appears above standard results for relevant queries.",
        "No-results fallback configured (VA or help desk link).",
        "UAT: 20 search queries tested across IT and HR topics.",
    ],
    process_decisions=[
        ("What content should AI Search index?",
         "KB articles (all published) + catalog items (all published) + incidents (closed, for agent search only).",
         "Published content ensures quality. Closed incidents are indexed only for agent-facing search -- not for employee portal. Draft or unpublished content must not be indexed."),
        ("Should AI Search appear in the employee portal or only for agents?",
         "Both -- employee-facing in Employee Center, agent-facing in Service Portal and Agent Workspace.",
         "Employee Center search is the primary deflection channel. AI Search improves first-click resolution rates significantly."),
        ("Should AI Search display a generated answer or just results?",
         "Generated answer panel (OOTB) appears above search results when confidence is high. Always show underlying source links.",
         "Generated answers without source links create trust issues. OOTB always shows the source article alongside the AI answer."),
        ("What happens when AI Search finds no relevant results?",
         "OOTB no-results fallback: display a link to Virtual Agent or a Create Ticket catalog item.",
         "Dead-end searches increase help desk call volume. VA or ticket creation as fallback preserves the deflection opportunity."),
    ],
    dependencies=[
        ("Now Assist for ITSM activated (WB1)", "Required", "ECS", "Sprint 5 Wk 1", "AI Search requires Now Assist active."),
        ("KB articles published (AP-13)", "Required", "ECS + Customer", "Sprint 5 Wk 1", "Empty KB = empty AI Search results."),
        ("Employee Center live (AP-15)", "Required", "ECS", "Sprint 5 Wk 1", "AI Search is embedded in the Employee Center search bar."),
        ("Catalog items published (AP-CAT)", "Required", "ECS", "Sprint 5 Wk 1", "Catalog items must be published to appear in AI Search results."),
    ],
    config_sections=[
        ("Search Index Scope", [
            ("KB articles", "All published articles -- all indexed knowledge bases", "Draft articles excluded automatically", False),
            ("Catalog items", "All published catalog items", "Unpublished items excluded", False),
            ("Incidents (agent search)", "Closed incidents -- agent-facing only", "Employee portal does not surface incident records", False),
            ("Employee portal incident access", "Disabled -- employees cannot search incident records", "Privacy and data segregation requirement", False),
        ]),
        ("Search UI Configuration", [
            ("AI answer panel", "Enabled -- appears above results when confidence is high (OOTB)", "Source article link always shown alongside AI answer", False),
            ("Confidence threshold for AI answer", "0.75 (OOTB default)", "Below this threshold, AI answer panel is suppressed", False),
            ("No-results fallback", "Link to Virtual Agent OR Create Ticket catalog item", "Customer to confirm preferred fallback action", True),
            ("Search bar location", "Employee Center global search bar (OOTB integration)", "No custom search widget needed", False),
        ]),
    ],
    raci_rows=[
        ("Configure Now Assist Search index scope", "R/A", "I", "ECS Consultant."),
        ("Verify KB article quality before indexing", "I", "R/A", "Customer KB Admin confirms article quality."),
        ("Enable AI Search in Employee Center", "R/A", "I", "ECS enables; Customer PM witnesses."),
        ("UAT -- 20 search queries tested", "R", "A", "ECS facilitates; Customer Service Desk Lead and HR rep validate."),
        ("Configure no-results fallback", "R/A", "Confirm fallback preference", "ECS configures; Customer decides VA vs. Create Ticket."),
    ],
    consultant_guide_sections=[
        ("Content quality is everything", "AI Search is only as good as the content it indexes. Before activating, audit the KB: remove articles with broken links, outdated procedures, or placeholder text. One bad article surfaced prominently in AI Search does more damage to adoption than no AI Search at all."),
        ("UAT query design", "Write 20 UAT queries that mirror real employee search language: 'how do I reset my password', 'request a new laptop', 'who is my HR contact', 'VPN not working', 'onboarding checklist'. Use actual phrasing from help desk tickets, not technical terms. This tests real-world relevance."),
        ("Source link discipline", "Coach the team: AI Search answers are always drafts that cite a source. The answer gets the employee 80% of the way there. The source link provides the authoritative detail. Never frame AI Search as replacing the KB article -- frame it as surfacing it faster."),
    ],
    adoption_rows=[
        ("Replace our SharePoint knowledge base with AI Search",
         "Index ServiceNow KB articles only. SharePoint migration is out of scope.",
         "SharePoint indexing requires a custom connector not in OOTB Now Assist. It is a Phase 2 integration project.",
         "AI Search works on what is in ServiceNow. The best accelerator for AI Search quality is migrating your top 20 most-searched articles from SharePoint into the ServiceNow KB. We scoped that migration in AP-13. Phase 2 can bring in the full SharePoint corpus once the ServiceNow KB is the primary destination.",
         "Phase 2 -- SharePoint connector after KB migration is proven."),
    ],
    snmap_sections=[
        ("AI Search", [
            ("sn_ais_search", "AI Search configuration -- index scope, confidence settings", "sn_ais_search"),
            ("kb_knowledge", "KB articles indexed by AI Search", "kb_knowledge"),
            ("sc_cat_item", "Catalog items indexed by AI Search", "sc_cat_item"),
            ("Employee Center search bar", "AI Search integrated into EC global search OOTB", "sp_search_source"),
        ]),
    ],
)

wb4 = TabContent(
    workbook_title="04 -- Resolution Notes & Work Note Generation",
    pack_name=PACK_NAME,
    purpose="Configure the OOTB Now Assist Resolution Notes Generation skill to help agents draft resolution notes and work note updates from incident history.",
    who_fills="ECS Consultant configures. Customer Service Desk Lead reviews quality during UAT.",
    sprint_window="Sprint 5-6 -- skill active by end of Week 11",
    estimated_effort="2-3 hours including configuration and UAT",
    related_workbooks=["01 Now Assist Scope", "02 Incident Summarization"],
    success_criteria=[
        "Resolution Notes Generation skill active on Incident form.",
        "Generate Resolution Notes button visible when incident is in Resolved state.",
        "Output quality reviewed on 10 test incidents by Service Desk Lead.",
        "AI badge visible on all generated resolution notes.",
        "Agent coaching delivered -- 'draft, not final' framing established.",
    ],
    process_decisions=[
        ("When should the Generate Resolution Notes button appear?",
         "Only when incident is in Resolved or Pending state. Not on open incidents.",
         "Resolution notes are written at close. Showing the button on open incidents creates confusion about when to use it."),
        ("Should generated notes auto-populate the Resolution Notes field?",
         "No -- generated notes appear in a preview panel. Agent copies and edits before saving.",
         "Auto-populate bypasses agent review. Given federal audit requirements, agents must own the resolution note content."),
        ("Should the skill also generate work note updates during resolution?",
         "Yes -- enable the Work Note Draft skill as a companion to Resolution Notes.",
         "Mid-resolution work notes benefit from summarization too. The OOTB skill supports both use cases."),
        ("How should the resolution note quality improve over time?",
         "Agent edits are captured as implicit feedback. No explicit rating system needed in 18-week scope.",
         "OOTB implicit feedback from agent edits is sufficient for quality improvement. Explicit rating UI adds configuration scope."),
    ],
    dependencies=[
        ("Now Assist for ITSM activated (WB1)", "Required", "ECS", "Sprint 5 Wk 1", "Resolution Notes skill requires Now Assist active."),
        ("Incident Summarization active (WB2)", "Recommended", "ECS", "Sprint 5 Wk 1", "Summarization and Resolution Notes share the same LLM call pattern -- activate together."),
        ("Incidents with good historical resolution notes", "Recommended", "Customer", "Sprint 5 Wk 1", "The LLM uses incident work notes as input -- richer work notes = better generated output."),
    ],
    config_sections=[
        ("Resolution Notes Generation Skill", [
            ("Skill", "Generate Resolution Notes (OOTB Now Assist skill)", "", False),
            ("Trigger state", "Resolved or Pending (OOTB event-based display)", "Button hidden on Open/In Progress incidents", False),
            ("Input scope", "All work notes + short description + category + resolution code", "More context = better generated notes", False),
            ("Output placement", "Preview panel -- agent copies to Resolution Notes field", "Do not auto-populate the field", False),
            ("AI badge", "Enabled (OOTB -- do not disable)", "Visible on all generated content", False),
        ]),
        ("Work Note Draft Skill", [
            ("Enable work note draft", "Yes -- OOTB companion skill to Resolution Notes", "Helps agents draft progress updates mid-resolution", False),
            ("Trigger", "On-demand -- agent clicks Draft Work Note", "Available on all open incidents", False),
        ]),
        ("Quality Coaching", [
            ("Agent framing", "Now Assist generates a draft -- agents review, edit, and own the final note", "Establish this framing in agent briefing before go-live", False),
            ("Edit expectation", "Agents should expect to edit 20-40% of generated content", "Editing is not a failure -- it is the intended workflow", False),
        ]),
    ],
    raci_rows=[
        ("Configure Resolution Notes Generation skill", "R/A", "I", "ECS Consultant."),
        ("Configure Work Note Draft skill", "R/A", "I", "ECS Consultant."),
        ("UAT -- 10 resolution note generations reviewed", "R", "A", "ECS + Service Desk Lead."),
        ("Agent briefing -- draft-not-final framing", "R/A", "Attend", "ECS delivers 20-min briefing; Service Desk Lead reinforces."),
        ("Monitor resolution note quality post-go-live", "N/A", "R/A", "Customer Service Desk Lead owns ongoing quality review."),
    ],
    consultant_guide_sections=[
        ("Input quality lever", "The quality of generated resolution notes is directly proportional to work note richness. Before go-live, coach agents to write more detailed work notes during the resolution process. Even a sentence per work note significantly improves Now Assist output."),
        ("UAT test case design", "Select 10 closed incidents that vary in resolution complexity: 3 simple (password reset), 4 medium (software install, access request), 3 complex (network troubleshooting). Complex incidents show the highest value -- the AI draft saves the most time for long resolutions."),
        ("Audit trail note", "For federal customers with audit requirements: AI-generated resolution notes that are agent-reviewed and saved are the agent's responsibility. The AI badge in the record shows the content was AI-assisted. This is compliant with NIST AI RMF guidance on human oversight of AI systems."),
    ],
    adoption_rows=[
        ("Agents refuse to use AI-generated resolution notes because they feel accountable for AI errors",
         "Frame as draft tool with explicit agent ownership.",
         "Agent accountability concern is valid and must be addressed in training, not dismissed.",
         "The agent is always the author of the resolution note -- Now Assist just provides the first draft. The audit trail shows the agent saved it, which means the agent reviewed and accepted it. We frame this in the briefing: you are the author, Now Assist is your research assistant. The AI badge in the record shows it was AI-assisted, which is transparent and compliant.",
         "If accountability concern persists -- escalate to Customer CISO for AI governance clarification."),
    ],
    snmap_sections=[
        ("Resolution Notes Generation", [
            ("sn_now_assist_skill (Resolution Notes)", "Now Assist skill for resolution note generation", "sn_now_assist_skill"),
            ("incident (resolution_notes)", "Target field -- agent copies generated draft here", "incident.resolution_notes"),
            ("incident (work_notes)", "Primary input to resolution note generation", "incident.work_notes"),
        ]),
    ],
)

wb5 = TabContent(
    workbook_title="05 -- Now Assist Adoption & KPI Measurement",
    pack_name=PACK_NAME,
    purpose="Define the KPIs, OOTB dashboards, and 30/60/90-day review cadence for measuring Now Assist GenAI adoption and productivity impact.",
    who_fills="ECS Consultant configures OOTB dashboards. Customer IT Manager and Now Assist Admin own ongoing reporting.",
    sprint_window="Sprint 6 -- KPIs baseline at go-live; review cadence established",
    estimated_effort="2 hours for dashboard setup and KPI agreement",
    related_workbooks=["01 Now Assist Scope", "AP-19 Performance Analytics", "AP-20 Reporting & Stabilization"],
    success_criteria=[
        "Now Assist Admin Console analytics accessible to Customer Admin.",
        "KPI baselines recorded on go-live day.",
        "30/60/90-day review meetings scheduled.",
        "Agent adoption rate target agreed.",
        "Continuous improvement process documented and handed over.",
    ],
    process_decisions=[
        ("What are the primary KPIs for Now Assist?",
         "Skill usage rate (% of agents using each skill weekly), handle time delta, and resolution note completion rate.",
         "These three measure adoption and productivity impact in terms IT leadership understands."),
        ("What is a realistic adoption target?",
         "50% of agents actively using at least one Now Assist skill within 60 days.",
         "50% active use at 60 days is realistic for a team that received proper UAT and briefing. 100% adoption in 18 weeks is not a realistic target."),
        ("How do we measure handle time improvement?",
         "Compare average incident handle time 30 days before go-live vs. 30 days after. OOTB incident report provides this.",
         "Handle time is the most tangible productivity metric. A 5-10% reduction is typical for teams actively using summarization and resolution note generation."),
    ],
    dependencies=[
        ("All three Now Assist skills active", "Required", "ECS", "Sprint 5 close", "Cannot measure adoption without active skills."),
        ("Now Assist Admin Console access for Customer Admin", "Required", "ECS", "Sprint 6 Wk 1", "Admin Console is the OOTB analytics source."),
        ("Handle time baseline pulled before go-live", "Required", "ECS", "Sprint 5 close", "Need pre-go-live baseline for 30-day comparison."),
    ],
    config_sections=[
        ("KPI Targets", [
            ("Skill usage rate -- 30 days", "30% of agents use at least one skill per week", "Early adoption benchmark", False),
            ("Skill usage rate -- 60 days", "50% of agents active weekly", "Target for mature adoption", False),
            ("Handle time improvement -- 60 days", "5% reduction vs. pre-go-live baseline", "Conservative; 10% is achievable with active use", False),
            ("Resolution note completion rate", "Increase by 15% vs. baseline (more incidents closed with notes)", "Now Assist lowers the barrier to writing good resolution notes", False),
            ("AI Search deflection contribution", "10% of employee searches result in no ticket creation (self-service)", "Measured via AI Search analytics", False),
        ]),
        ("Review Cadence", [
            ("30-day review", "ECS + Customer IT Manager -- skill usage vs. 30% target; handle time delta", "ECS schedules before Sprint 6 close", False),
            ("60-day review", "Customer IT Manager + Now Assist Admin -- confirm 50% adoption; identify low adopters", "Customer-led; ECS advisory", False),
            ("90-day review", "ECS + Customer PM -- stabilization assessment; Phase 2 GenAI scope", "Marks end of ECS Now Assist obligations", False),
        ]),
        ("Dashboard Access", [
            ("Now Assist Admin Console", "Now Assist > Admin Console > Analytics (OOTB)", "No custom PA indicators in 18-week scope", False),
            ("Incident handle time report", "OOTB Reports -- Incident > Average resolution time by period", "Pull manually for 30/60/90-day comparison", False),
            ("Access role", "sn_now_assist.admin (OOTB)", "Customer Admin must have this role at go-live", True),
        ]),
    ],
    raci_rows=[
        ("Pull handle time baseline before go-live", "R/A", "I", "ECS pulls and records baseline."),
        ("Configure Now Assist Admin Console access", "R/A", "Verify access", "ECS configures; Customer Admin confirms."),
        ("30-day adoption review", "R", "A", "ECS presents; Customer IT Manager reviews."),
        ("Identify and coach low adopters", "I (advise)", "R/A", "Customer IT Manager owns agent coaching."),
        ("Phase 2 GenAI scope discussion", "R (propose)", "A (decide)", "ECS proposes at 90-day review; Customer decides."),
    ],
    consultant_guide_sections=[
        ("Handle time measurement method", "Use the OOTB Reports module: Reports > New > Incident > group by month > metric = average resolve time. Run for the 30 days before go-live. Save the report. At 30 and 60 days post-launch, rerun for the same metric and compare. A simple percentage change table is all the customer needs."),
        ("Low adopter identification", "The Now Assist Admin Console shows skill usage by user. At the 60-day review, identify agents with zero usage. Common causes: (1) did not attend briefing, (2) do not know the feature exists, (3) tried it once and got a poor result. Each cause has a different intervention. Zero usage is the metric to watch."),
        ("Phase 2 GenAI pipeline", "At the 90-day review, present the Phase 2 GenAI roadmap: (1) GenAI for Change (change assessment generation), (2) Case Summarization (if CSM is in scope), (3) AI Search corpus expansion (SharePoint connector), (4) Proactive AI suggestions for problem management. Frame these as the next layer of value on the foundation built in Sprint 5-6."),
    ],
    adoption_rows=[
        ("Why is adoption only 50% -- we expected everyone to use it",
         "50% at 60 days is the realistic OOTB target; 80% is achievable at 6 months.",
         "Technology adoption follows a standard curve. 50% at 60 days represents early majority adoption. Late majority follows with peer influence and demonstrated productivity gains.",
         "50% adoption at 60 days means half your team is already working faster with AI assistance. The other half will follow as they see their colleagues' results. We have the usage data by agent -- we can identify the low adopters and do targeted coaching. Getting to 80% by month 6 is very achievable with that approach.",
         "If adoption below 20% at 90 days -- structured re-training required."),
    ],
    snmap_sections=[
        ("Analytics", [
            ("Now Assist Admin Console", "OOTB skill usage analytics -- usage rate, skill breakdown, user activity", "sn_now_assist"),
            ("Incident report (handle time)", "OOTB incident report -- average resolve time by period", "incident (resolved_at, opened_at)"),
            ("AI Search analytics", "OOTB AI Search usage and deflection metrics", "sn_ais_search"),
        ]),
    ],
)

def build_readme():
    meta = DocMeta(
        eyebrow="ACCELERATOR PACK",
        title="Now Assist / GenAI\nAccelerator Pack",
        subtitle="OOTB Now Assist for ITSM -- Summarization, AI Search, Resolution Notes, Adoption",
        doc_id="AP-18",
        version="1.0",
        status="Released",
        audience="ECS Consultants (Internal) + Customer IT Manager / Now Assist Admin (selected tabs)",
        running_header_label="Now Assist / GenAI Accelerator Pack · ECS Federal",
        confidentiality="Internal Use Only · Confidential",
    )
    doc = EcsDocument(meta=meta)
    doc.add_cover_page()
    doc.h1("Pack Overview")
    doc.para(
        "AP-18 guides the ECS team through activating and configuring ServiceNow Now Assist "
        "GenAI skills during Month 3 (Sprints 5-6) of the 18-week engagement. The pack covers "
        "entitlement and scope decisions, Incident Summarization, AI Search augmentation, "
        "Resolution Notes Generation, and adoption KPIs. All work is OOTB -- no custom LLM "
        "prompts, no external API integrations, and no custom skill development. "
        "Federal compliance (AI badge, on-demand mode, CISO review) is built into every workbook."
    )
    doc.h1("Workbook Inventory")
    doc.table(
        headers=["#", "Workbook", "Owner", "Sprint"],
        rows=[
            ("WB1", "Now Assist Scope & Entitlement", "ECS + Customer IT Director", "Sprint 5"),
            ("WB2", "Incident & Case Summarization", "ECS Consultant", "Sprint 5"),
            ("WB3", "Now Assist Search (AI Search Augmentation)", "ECS Consultant", "Sprint 5"),
            ("WB4", "Resolution Notes & Work Note Generation", "ECS Consultant", "Sprint 5-6"),
            ("WB5", "Now Assist Adoption & KPI Measurement", "ECS + Customer IT Manager", "Sprint 6"),
        ],
    )
    doc.h1("Key OOTB Decisions")
    doc.para(
        "Skills at go-live (3 max): Incident Summarization, AI Search, Resolution Notes Generation. "
        "Mode: On-demand only -- agent clicks Generate. No auto-generation in 18-week scope. "
        "AI badge: Always enabled -- non-negotiable for federal deployments. "
        "CISO review: Required before activation -- provide Now Assist Security whitepaper. "
        "KPI targets: 30% agent adoption at 30 days; 50% at 60 days; 5% handle time reduction at 60 days."
    )
    out = os.path.join(PACK_DIR, "00_README_Now_Assist_GenAI_Pack.docx")
    doc.save(out)
    print(f"README saved: {out}")

if __name__ == "__main__":
    print("Building Now Assist / GenAI Accelerator Pack...")
    workbooks = [
        ("01_now_assist_scope.xlsx", wb1),
        ("02_incident_summarization.xlsx", wb2),
        ("03_ai_search_augmentation.xlsx", wb3),
        ("04_resolution_notes.xlsx", wb4),
        ("05_adoption_kpis.xlsx", wb5),
    ]
    for filename, content in workbooks:
        build_workbook(content, os.path.join(PACK_DIR, filename))
        print(f"  check {filename}")
    build_readme()
    print("Now Assist / GenAI Accelerator Pack complete.")
