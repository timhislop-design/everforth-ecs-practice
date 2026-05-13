"""
build_AP17_PI.py -- AP-17 Predictive Intelligence Accelerator Pack
Covers: OOTB PI scope, category classification, similar incidents,
assignment intelligence, and continuous improvement KPIs.
Sprint window: Month 2-3 (Sprint 4-5)
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from accelerator_pack_builder import TabContent, build_workbook
from ecs_template import EcsDocument, DocMeta

PACK_DIR = HERE
PACK_NAME = "Predictive Intelligence Accelerator Pack"

wb1 = TabContent(
    workbook_title="01 -- PI Scope & Readiness Decisions",
    pack_name=PACK_NAME,
    purpose="Confirm which OOTB Predictive Intelligence models to activate, verify training data volume requirements, and establish the sprint sequence for model training and go-live.",
    who_fills="ECS Architect leads. Customer IT Manager and Service Desk Lead provide data volume confirmation.",
    sprint_window="Sprint 4 -- decisions complete by end of Week 8",
    estimated_effort="2-3 hours with Customer IT Manager",
    related_workbooks=["02 Category Classification", "03 Similar Incident", "04 Assignment Intelligence", "AP-12 Discovery", "AP-CAT Service Catalog"],
    success_criteria=[
        "PI models in scope confirmed (category, similar incident, assignment).",
        "Training data volume verified (1,000+ incidents minimum for classification).",
        "Existing category/subcategory structure confirmed stable before PI activation.",
        "Customer named PI Admin for ongoing model management.",
        "Model retraining cadence agreed (weekly OOTB default).",
    ],
    process_decisions=[
        ("Which PI models should be activated at go-live?",
         "All three OOTB models: Category Classification, Similar Incident, and Assignment Intelligence.",
         "All three ship OOTB with Now Platform. They share the same training pipeline. Activating all three in Sprint 4 maximizes AI realization value. Defer 'Predictive Fields' (additional custom fields) to Phase 2."),
        ("How much historical incident data is required?",
         "Minimum 1,000 closed incidents with category and assignment group populated. Target 5,000+ for reliable accuracy.",
         "ServiceNow's ML engine requires sufficient training examples per class. Below 1,000 records, accuracy is too low for production use. Customer must confirm data volume before Sprint 4 model training begins."),
        ("Should PI be activated before or after catalog normalization?",
         "After catalog normalization (AP-CAT). Category and subcategory values must be stable before PI trains on them.",
         "PI Category Classification trains on the current category taxonomy. If categories change after training, the model predictions become unreliable. Finalize the category structure first."),
        ("How often should models retrain?",
         "Weekly retraining (OOTB default schedule). Do not increase to daily -- excessive retraining adds compute load without accuracy improvement.",
         "Weekly captures new incidents at an appropriate pace. Models stabilize after 4-6 weeks of weekly retraining cycles."),
        ("Should PI suggestions be auto-applied or agent-reviewed?",
         "Agent-reviewed at go-live. Auto-apply is Phase 2 after accuracy exceeds 80% for 30 consecutive days.",
         "OOTB supports both modes. Starting with suggestions (not auto-apply) builds agent trust and surfaces accuracy issues safely."),
    ],
    dependencies=[
        ("1,000+ closed incidents with populated category and assignment", "Required", "Customer", "Before Sprint 4 training", "PI model cannot be trained without sufficient historical data."),
        ("Stable category/subcategory taxonomy (AP-CAT)", "Required", "ECS", "Sprint 3 close", "Categories must not change after PI model training begins."),
        ("Assignment groups fully populated in ServiceNow", "Required", "Customer", "Sprint 2 close", "Assignment Intelligence needs populated group records to predict correctly."),
        ("Now Platform licensed for PI (Intelligent Experiences)", "Required", "Customer", "Before Sprint 4", "PI is licensed separately. Customer must confirm entitlement."),
    ],
    config_sections=[
        ("PI Model Activation", [
            ("Category Classification model", "Activate -- Sprint 4 Week 1", "Predicts incident category and subcategory from short description", False),
            ("Similar Incident model", "Activate -- Sprint 4 Week 1", "Surfaces related past incidents to reduce resolution time", False),
            ("Assignment Intelligence model", "Activate -- Sprint 4 Week 2", "Predicts assignment group from category and short description", False),
            ("Predictive Fields (additional)", "Defer to Phase 2", "Custom field prediction requires additional configuration scope", False),
        ]),
        ("Training Data Thresholds", [
            ("Minimum incidents for training", "1,000 closed incidents", "Below this threshold PI accuracy is unreliable", False),
            ("Target incidents for high accuracy", "5,000+ closed incidents", "Customer to confirm count before Sprint 4 kickoff", True),
            ("Minimum examples per category", "50 incidents per category/subcategory", "Categories with fewer examples will have low prediction confidence", False),
            ("Retraining schedule", "Weekly (OOTB default -- every Sunday at midnight)", "Do not change retraining frequency in 18-week scope", False),
        ]),
        ("Suggestion Mode", [
            ("Initial mode at go-live", "Suggest only -- agent must confirm before applying", "Build agent trust before enabling auto-apply", False),
            ("Auto-apply threshold", "80% model accuracy for 30 consecutive days", "Customer PI Admin and ECS review before enabling", True),
            ("Confidence threshold for display", "0.70 (OOTB default)", "Suggestions below 0.70 confidence are suppressed from agent view", False),
        ]),
    ],
    raci_rows=[
        ("Confirm PI license entitlement", "I", "R/A", "Customer IT Director."),
        ("Confirm historical incident data volume", "I", "R/A", "Customer Service Desk Lead."),
        ("Activate PI models in ServiceNow", "R/A", "I", "ECS Architect."),
        ("Monitor model accuracy post-activation", "R", "A", "ECS monitors first 4 weeks; Customer PI Admin takes over."),
        ("Approve auto-apply threshold (Phase 2)", "R (advise)", "A (decide)", "Customer IT Director decides with ECS recommendation."),
    ],
    consultant_guide_sections=[
        ("Data quality gate", "Before activating PI, run a data quality check: query incidents for null category, null assignment_group, and null short_description. If more than 20% of training records have null categories, PI accuracy will be poor. Work with the customer to backfill or exclude dirty records from the training set."),
        ("Category stability rule", "PI Category Classification is extremely sensitive to taxonomy changes. If the customer changes categories after training, the model will predict old categories that no longer exist. Enforce a category freeze before Sprint 4 training. Document any planned future category changes as Phase 2."),
        ("Agent trust-building", "The biggest risk to PI adoption is agents ignoring suggestions because the first few are wrong. Coach the Service Desk Lead to frame PI as a 'second opinion, not an order.' After 4 weeks, pull the suggestion acceptance rate from PI Analytics. If below 40%, schedule an accuracy review."),
        ("Confidence threshold calibration", "If agents report too many irrelevant suggestions, raise the confidence threshold to 0.80 in PI Solution settings. If agents report that PI is too silent (few suggestions), lower to 0.65. Do not go below 0.60 -- below this threshold suggestions are essentially random."),
    ],
    adoption_rows=[
        ("We want PI to auto-assign tickets without agent review",
         "Suggest mode at go-live; auto-apply after accuracy validated.",
         "Auto-apply without validated accuracy creates mis-routed tickets that damage help desk trust in the AI platform.",
         "Auto-assignment is the goal -- we just need to earn it. Starting with suggestions lets agents correct wrong predictions, which improves the model faster. Once accuracy holds above 80% for a month, we enable auto-apply and the agents get the full benefit without the routing risk.",
         "After 30 consecutive days at 80%+ accuracy."),
        ("Train PI on our custom fields, not just category",
         "OOTB category, subcategory, and assignment group at go-live. Custom fields in Phase 2.",
         "Custom field prediction requires creating additional PI Solutions -- each adds configuration scope. OOTB fields cover the highest-value predictions.",
         "Custom field prediction is absolutely on the roadmap -- it is a Phase 2 item once the baseline models are proven. Adding custom fields to the training set before the baseline is stable would make it harder to diagnose accuracy issues.",
         "Phase 2 -- after baseline models exceed 80% acceptance rate."),
    ],
    snmap_sections=[
        ("PI Core Tables", [
            ("ml_solution", "PI Solution record -- one per active model (category, similar, assignment)", "ml_solution"),
            ("ml_capability", "Capability record linking PI solution to a table (incident)", "ml_capability"),
            ("ml_input_output", "Defines input fields (short_description) and output fields (category) for each model", "ml_input_output"),
        ]),
        ("Agent Experience", [
            ("Incident form PI widget", "OOTB widget on Incident form showing PI suggestions inline", "incident (form layout)"),
            ("PI Analytics dashboard", "OOTB -- model accuracy, acceptance rate, suggestion volume", "ml_analytics"),
        ]),
    ],
)

wb2 = TabContent(
    workbook_title="02 -- Category Classification Configuration",
    pack_name=PACK_NAME,
    purpose="Configure the OOTB Category Classification PI model to predict incident category and subcategory from the short description field.",
    who_fills="ECS Architect configures. Customer Service Desk Lead reviews prediction accuracy during UAT.",
    sprint_window="Sprint 4 -- model active and tested by end of Week 8",
    estimated_effort="4-6 hours including training run and accuracy review",
    related_workbooks=["01 PI Scope & Readiness", "AP-CAT Service Catalog (category taxonomy)"],
    success_criteria=[
        "Category Classification model trained and published.",
        "Minimum 70% prediction accuracy on test set.",
        "OOTB suggestions visible on Incident form for agents.",
        "Confidence threshold set to 0.70.",
        "Agent UAT completed -- at least 20 test incidents reviewed.",
    ],
    process_decisions=[
        ("Which fields should PI use as input for category prediction?",
         "Short description only (OOTB default). Do not add description body -- it adds noise and slows training.",
         "Short description is the field agents complete first and it contains the most predictive signal. Description body is often templated boilerplate."),
        ("Should subcategory prediction be enabled alongside category?",
         "Yes -- enable both category and subcategory prediction in a single PI Solution.",
         "OOTB supports hierarchical prediction. Training on both simultaneously is more efficient than two separate models."),
        ("What happens when PI confidence is below threshold?",
         "Suppress the suggestion -- do not show low-confidence predictions to agents.",
         "Showing low-confidence predictions trains agents to distrust the system. Suppression below threshold maintains signal quality."),
        ("How long does model training take?",
         "Initial training: 2-4 hours for 5,000 records. Subsequent weekly retraining: 30-60 minutes.",
         "Schedule initial training at off-peak hours. ServiceNow runs ML training jobs asynchronously -- the instance remains available during training."),
    ],
    dependencies=[
        ("Category taxonomy frozen (AP-CAT)", "Required", "ECS", "Sprint 3 close", "Cannot train on a changing taxonomy."),
        ("1,000+ closed incidents with non-null category", "Required", "Customer", "Sprint 4 Wk 1", "Training data threshold."),
        ("PI license active", "Required", "Customer", "Sprint 4 Wk 1", "Cannot activate model without entitlement."),
    ],
    config_sections=[
        ("ML Solution Configuration", [
            ("Solution name", "ECS_Category_Classifier", "Do not use spaces -- ServiceNow ML solution name is a technical identifier", False),
            ("Source table", "incident", "Train on incident table only", False),
            ("Input field", "short_description", "Primary predictive input", False),
            ("Output field 1", "category", "Primary prediction target", False),
            ("Output field 2", "subcategory", "Secondary prediction -- hierarchical", False),
            ("Training filter", "state=7 (Closed) AND short_description IS NOT NULL AND category IS NOT NULL", "Only clean, closed records used for training", False),
            ("Confidence threshold", "0.70", "Suppress suggestions below this score", False),
            ("Retraining schedule", "Weekly -- Sunday 00:00 instance timezone", "OOTB default -- do not modify", False),
        ]),
        ("Accuracy Targets", [
            ("Category accuracy target (go-live)", "70% on held-out test set", "ServiceNow auto-splits training data 80/20 train/test", False),
            ("Category accuracy target (30 days)", "75%", "With weekly retraining cycles", False),
            ("Subcategory accuracy target (go-live)", "60%", "Subcategory is harder to predict -- lower initial threshold acceptable", False),
            ("Auto-apply threshold", "80% category accuracy sustained for 30 days", "Customer decision -- ECS recommendation", True),
        ]),
    ],
    raci_rows=[
        ("Create and configure ML Solution record", "R/A", "I", "ECS Architect."),
        ("Run initial model training", "R/A", "I", "ECS runs; Customer IT Manager notified."),
        ("Review training accuracy results", "R", "A", "ECS presents; Customer Service Desk Lead approves go-live."),
        ("UAT -- review 20 test incident predictions", "R", "A", "ECS and Service Desk Lead jointly review."),
        ("Enable suggestions on Incident form", "R/A", "I", "ECS enables; Customer confirms visibility."),
        ("Monitor weekly accuracy reports", "R (first 4 weeks)", "A (ongoing)", "Customer PI Admin takes over after sprint close."),
    ],
    consultant_guide_sections=[
        ("Training filter discipline", "Always filter training data to closed incidents with non-null category AND non-null short_description. Null values in training data corrupt the model. Run the query manually before training to confirm record count and null rate."),
        ("Accuracy review with customer", "When presenting accuracy results, use plain language: 'For every 10 tickets, PI correctly predicts the category 7 times.' Percentages are abstract -- incidents-per-10 is concrete. This sets honest expectations before agents start using suggestions."),
        ("Low accuracy root cause", "If accuracy is below 60%: (1) check for categories with fewer than 50 training examples -- merge or exclude them. (2) Check for inconsistent category assignment in historical data -- agents may have used the wrong category. (3) Consider excluding the lowest-frequency categories from prediction scope."),
    ],
    adoption_rows=[
        ("Agents are ignoring PI suggestions",
         "Monitor acceptance rate in PI Analytics. If below 30%, run accuracy review.",
         "Low acceptance usually means low accuracy -- agents learn quickly when suggestions are wrong.",
         "Low acceptance is data, not a failure. We pull the PI Analytics acceptance rate report and review the most-rejected suggestions. Usually 2-3 category pairs are causing most of the rejections. We adjust the training filter to exclude ambiguous records and the acceptance rate improves within 2 retraining cycles.",
         "If acceptance rate is below 20% after 60 days -- escalate to ServiceNow Support."),
    ],
    snmap_sections=[
        ("ML Solution", [
            ("ml_solution", "PI Solution record -- training config, schedule, status", "ml_solution"),
            ("ml_input_output", "Input/output field mapping for the solution", "ml_input_output"),
            ("ml_training_run", "Each training execution -- accuracy metrics logged here", "ml_training_run"),
            ("Incident form widget", "OOTB PI suggestion widget on incident.category field", "incident form layout"),
        ]),
    ],
)

wb3 = TabContent(
    workbook_title="03 -- Similar Incident & Problem Intelligence",
    pack_name=PACK_NAME,
    purpose="Configure the OOTB Similar Incident PI model to surface related past incidents and known errors to agents during incident resolution.",
    who_fills="ECS Architect configures. Customer Service Desk Lead and Problem Manager review during UAT.",
    sprint_window="Sprint 4 -- model active by end of Week 8",
    estimated_effort="3-4 hours including training and UAT",
    related_workbooks=["01 PI Scope & Readiness", "AP-13 Knowledge Management"],
    success_criteria=[
        "Similar Incident model trained and suggestions visible on Incident form.",
        "Similar incident panel shows top 3-5 related incidents OOTB.",
        "Known error (Problem) link surfaces in similar incident results.",
        "Agent UAT completed -- at least 10 test incidents reviewed.",
        "Average time-to-resolution baseline recorded for 30-day comparison.",
    ],
    process_decisions=[
        ("Should Similar Incident search across all incidents or just closed?",
         "Closed incidents only (OOTB default). Open incidents may have incorrect diagnoses.",
         "Searching open incidents surfaces unresolved records that may lead agents down the wrong path. Closed incidents have confirmed resolutions."),
        ("How many similar incidents should be displayed?",
         "Top 5 (OOTB default). Do not increase -- cognitive overload reduces agent usage.",
         "Research shows agents engage with the first 3 results most frequently. Showing 5 provides enough options without overwhelming."),
        ("Should Similar Incident link to Problem records?",
         "Yes -- enable OOTB known error link. If a related Problem exists, it surfaces above similar incidents.",
         "Known errors from Problem Management are higher quality than individual incident resolutions. OOTB links them automatically."),
        ("Which fields drive similarity matching?",
         "Short description + description (OOTB semantic similarity). Do not add custom fields.",
         "OOTB semantic model uses NLP to match meaning, not just keywords. Custom fields dilute the signal."),
    ],
    dependencies=[
        ("1,000+ closed incidents", "Required", "Customer", "Sprint 4 Wk 1", "Same data requirement as Category Classification."),
        ("Problem Management active", "Recommended", "ECS", "Sprint 2 close", "Known error links only appear if Problem records exist with known error flag set."),
        ("KB articles published (AP-13)", "Recommended", "ECS", "Sprint 4 Wk 1", "Similar Incident can also surface KB articles -- requires published articles."),
    ],
    config_sections=[
        ("Similar Incident ML Solution", [
            ("Solution name", "ECS_Similar_Incident", "", False),
            ("Source table", "incident", "Closed incidents only", False),
            ("Similarity fields", "short_description, description", "OOTB semantic NLP matching", False),
            ("Training filter", "state=7 (Closed) AND short_description IS NOT NULL", "", False),
            ("Results displayed", "5 (OOTB default)", "Top 5 by similarity score", False),
            ("Known error surfacing", "Enabled -- OOTB Problem Management link", "Known errors rank above similar incidents", False),
            ("KB article surfacing", "Enabled -- requires published KB articles", "Surfaces relevant KB articles alongside incidents", False),
        ]),
        ("Agent Experience", [
            ("Panel location", "Incident form -- right column (OOTB placement)", "Do not move or restyle panel", False),
            ("Panel header label", "Similar Incidents & Known Errors (OOTB)", "", False),
            ("Resolution copy action", "OOTB -- agent can copy resolution notes from similar incident with one click", "Coach agents to use this to reduce typing time", False),
        ]),
    ],
    raci_rows=[
        ("Create and configure Similar Incident ML Solution", "R/A", "I", "ECS Architect."),
        ("Run model training", "R/A", "I", "ECS runs training job."),
        ("UAT -- review similar incident suggestions on test tickets", "R", "A", "ECS + Service Desk Lead jointly."),
        ("Enable known error link in Problem Management", "R/A", "I", "ECS enables; Problem Manager confirms."),
        ("Record resolution time baseline", "R", "A", "ECS pulls baseline MTTR report before go-live."),
    ],
    consultant_guide_sections=[
        ("Resolution time impact", "Similar Incident is the PI feature with the fastest measurable impact. Pull MTTR (mean time to resolve) for the 30 days before go-live. At 30-day post-launch review, compare. Customers typically see 10-15% MTTR reduction from the copy-resolution action alone."),
        ("Known error setup", "For the known error link to work, Problem records must have the Known Error flag checked and a Workaround field populated. If Problem Management is new, coach the Problem Manager to set these flags as they close root cause analysis."),
        ("Low relevance complaints", "If agents say suggestions are not relevant, check the training filter. Common cause: incidents with boilerplate short descriptions (e.g., 'User called' or 'Please help') are polluting training data. Add a character-length filter: short_description.length > 15 to exclude one-liners."),
    ],
    adoption_rows=[
        ("Agents do not use the similar incident panel",
         "Track panel interaction in PI Analytics. Run 30-day champion exercise.",
         "Low usage usually means agents are not aware the copy-resolution feature exists.",
         "We run a 30-day champion exercise: identify 2-3 agents who use similar incidents most, have them share a before/after story with the team. Peer testimony drives adoption faster than manager instruction. We will have the data from PI Analytics to find the champions.",
         "If usage is below 20% at 60 days -- run a 1-hour team refresher with live demos."),
    ],
    snmap_sections=[
        ("ML Solution", [
            ("ml_solution (Similar Incident)", "PI Solution record for semantic similarity matching", "ml_solution"),
            ("problem (known error)", "Problem record with known_error=true and workaround populated", "problem"),
            ("kb_knowledge", "Published KB articles surfaced alongside similar incidents", "kb_knowledge"),
        ]),
    ],
)

wb4 = TabContent(
    workbook_title="04 -- Assignment Intelligence Configuration",
    pack_name=PACK_NAME,
    purpose="Configure the OOTB Assignment Intelligence PI model to predict the correct assignment group for new incidents based on category and short description.",
    who_fills="ECS Architect configures. Customer Service Desk Lead and IT Manager review during UAT.",
    sprint_window="Sprint 4-5 -- model active and tested by end of Week 9",
    estimated_effort="4-5 hours including training, accuracy review, and UAT",
    related_workbooks=["01 PI Scope & Readiness", "02 Category Classification", "AP-01 Foundation Data (groups)"],
    success_criteria=[
        "Assignment Intelligence model trained and suggestions visible on Incident form.",
        "Minimum 65% assignment group prediction accuracy on test set.",
        "Assignment suggestions suppressed below 0.70 confidence threshold.",
        "Agent UAT: 20 test incidents reviewed for assignment accuracy.",
        "Average first-assignment accuracy baseline recorded.",
    ],
    process_decisions=[
        ("Which fields should drive assignment prediction?",
         "Category + subcategory + short description (OOTB combination). This is more accurate than short description alone.",
         "Category provides strong signal for routing -- the model learns that 'Network' category incidents route to Network Ops, regardless of short description wording."),
        ("Should Assignment Intelligence predict individual agent or just group?",
         "Assignment group only at go-live. Individual agent assignment is Phase 2.",
         "Group-level prediction has much higher accuracy. Individual agent prediction requires far more training data per agent and is highly sensitive to agent turnover."),
        ("Should suggestions be shown on ticket creation or after categorization?",
         "After categorization -- assignment suggestion appears once category is set.",
         "Category is the strongest input signal. Showing assignment suggestions before category is set produces low-quality predictions."),
        ("What happens to mis-assigned tickets during the suggestion period?",
         "Agents correct the assignment manually. Each correction is captured as training feedback for the next retraining cycle.",
         "OOTB PI captures agent overrides as negative feedback. The model improves with each correction cycle."),
    ],
    dependencies=[
        ("Assignment groups populated in ServiceNow (AP-01)", "Required", "Customer", "Sprint 1 close", "Groups must exist for PI to predict them."),
        ("Category Classification active (WB2)", "Required", "ECS", "Sprint 4 Wk 1", "Assignment Intelligence uses category as input -- category model must be active first."),
        ("1,000+ closed incidents with populated assignment group", "Required", "Customer", "Sprint 4 Wk 1", "Training data requirement."),
    ],
    config_sections=[
        ("Assignment Intelligence ML Solution", [
            ("Solution name", "ECS_Assignment_Intelligence", "", False),
            ("Source table", "incident", "Closed incidents only", False),
            ("Input fields", "category, subcategory, short_description", "Combined input for highest accuracy", False),
            ("Output field", "assignment_group", "Predict group only -- not individual agent", False),
            ("Training filter", "state=7 AND assignment_group IS NOT NULL AND category IS NOT NULL", "", False),
            ("Confidence threshold", "0.70", "Suppress below this score", False),
            ("Suggestion display trigger", "After category field is populated", "OOTB event-driven suggestion", False),
        ]),
        ("Accuracy Targets", [
            ("Go-live accuracy target", "65% first-assignment accuracy", "Measured against closed incident ground truth", False),
            ("30-day target", "70%", "With weekly retraining incorporating corrections", False),
            ("Groups to exclude from prediction", "[Customer: list groups with fewer than 50 historical incidents]", "Too few examples = unreliable predictions for that group", True),
        ]),
    ],
    raci_rows=[
        ("Create and configure Assignment Intelligence ML Solution", "R/A", "I", "ECS Architect."),
        ("Run model training", "R/A", "I", "ECS runs job; Customer IT Manager notified."),
        ("Review accuracy report by assignment group", "R", "A", "ECS presents; IT Manager approves go-live."),
        ("UAT -- 20 test incident assignment review", "R", "A", "ECS + Service Desk Lead."),
        ("Record first-assignment accuracy baseline", "R", "A", "ECS pulls baseline metric before go-live."),
        ("Monitor accuracy and retraining cycles", "R (4 weeks)", "A (ongoing)", "Customer PI Admin takes over at sprint close."),
    ],
    consultant_guide_sections=[
        ("First-assignment rate baseline", "Before go-live, pull a first-assignment rate metric from the past 90 days: what percentage of incidents were assigned correctly on the first assignment attempt? This is your baseline. At 30 and 90 days post-launch, compare. A good Assignment Intelligence deployment improves first-assignment rate by 15-25%."),
        ("Groups with too few records", "If any assignment group has fewer than 50 historical incidents, Assignment Intelligence cannot predict it reliably. Options: (1) exclude it from prediction scope, (2) merge it with a similar group in the training filter, or (3) accept low confidence for that group and let agents manually assign. Discuss options with the IT Manager."),
        ("Override as training signal", "Reinforce to agents: every time they override an incorrect assignment suggestion, they are improving the model. This reframes corrections from 'the AI is broken' to 'I am training it.' Increases agent engagement with the correction workflow."),
    ],
    adoption_rows=[
        ("We want PI to auto-assign tickets to individual agents",
         "Group-level assignment at go-live; agent-level in Phase 2.",
         "Agent-level prediction requires 10x more training data and is sensitive to agent turnover, workload, and specialization changes.",
         "Group assignment is the 80% solution. Once the group accuracy is proven, we look at agent-level assignment in Phase 2 using workload data alongside the PI model. Agent-level is the right destination -- group-level is the right starting point.",
         "Phase 2 -- after group accuracy exceeds 75% for 60 days."),
    ],
    snmap_sections=[
        ("Assignment Intelligence", [
            ("ml_solution (Assignment)", "PI Solution for assignment group prediction", "ml_solution"),
            ("sys_user_group", "Assignment groups -- must be populated for prediction", "sys_user_group"),
            ("incident (assignment_group)", "Target field for prediction output", "incident.assignment_group"),
            ("PI Analytics", "OOTB first-assignment rate, accuracy by group", "ml_analytics"),
        ]),
    ],
)

wb5 = TabContent(
    workbook_title="05 -- PI KPIs & Continuous Improvement",
    pack_name=PACK_NAME,
    purpose="Define the KPIs, review cadence, and continuous improvement process for Predictive Intelligence post-go-live.",
    who_fills="ECS Architect sets up OOTB dashboards. Customer PI Admin owns ongoing monitoring and improvement.",
    sprint_window="Sprint 5 -- KPI baseline set at go-live; 30/60/90-day review cadence established",
    estimated_effort="2 hours for dashboard setup and review cadence agreement",
    related_workbooks=["01 PI Scope", "02 Category Classification", "03 Similar Incident", "04 Assignment Intelligence", "AP-19 Performance Analytics"],
    success_criteria=[
        "OOTB PI Analytics dashboard accessible to Customer PI Admin.",
        "KPI baseline recorded for all three models on go-live day.",
        "30/60/90-day review meetings scheduled.",
        "Customer PI Admin trained on pulling and interpreting PI accuracy reports.",
        "Continuous improvement process documented and handed over.",
    ],
    process_decisions=[
        ("What are the primary KPIs for Predictive Intelligence?",
         "Category accuracy %, similar incident acceptance rate %, and first-assignment accuracy %.",
         "These three metrics directly measure the value of each PI model in operational terms the help desk can understand."),
        ("How often should PI performance be reviewed?",
         "30/60/90-day reviews with ECS during engagement. Monthly self-review by Customer PI Admin post-stabilization.",
         "PI models improve continuously with retraining. Quarterly reviews catch model drift early."),
        ("What triggers a model retraining review?",
         "Any model dropping below its accuracy target for 2 consecutive weekly retraining cycles.",
         "Two cycles rules out noise. A sustained drop indicates data drift or taxonomy change that requires investigation."),
    ],
    dependencies=[
        ("All three PI models active", "Required", "ECS", "Sprint 5 Wk 1", "Cannot measure KPIs without active models."),
        ("PI Analytics access for Customer PI Admin", "Required", "ECS", "Sprint 5 Wk 1", "Admin must have ml_analyst role."),
        ("Go-live baseline date recorded", "Required", "ECS PM", "Sprint 4 close", "KPI clock starts on model activation date."),
    ],
    config_sections=[
        ("KPI Targets", [
            ("Category Classification accuracy -- go-live", "70%", "ServiceNow ML benchmark for OOTB category prediction", False),
            ("Category Classification accuracy -- 90 days", "80%", "With 12 weekly retraining cycles", False),
            ("Similar Incident acceptance rate -- 30 days", "40%", "% of suggestions agents click to view", False),
            ("Similar Incident acceptance rate -- 90 days", "55%", "With agent familiarity and KB article growth", False),
            ("First-assignment accuracy -- go-live", "65%", "Baseline improvement from pre-PI rate", False),
            ("First-assignment accuracy -- 90 days", "75%", "With weekly retraining and agent correction feedback", False),
        ]),
        ("Review Cadence", [
            ("30-day review", "ECS + Customer PM + PI Admin -- compare all 3 KPIs to targets", "ECS schedules before Sprint 5 close", False),
            ("60-day review", "Customer PI Admin + IT Manager -- confirm retraining schedule healthy", "Customer-led; ECS advisory only", False),
            ("90-day review", "ECS + Customer PM -- stabilization assessment; Phase 2 scope", "Marks end of ECS PI obligations", False),
            ("Accuracy alert threshold", "Any model dropping below 50% for 2 cycles -- ECS review call", "ECS available during hypercare period", False),
        ]),
        ("Dashboard Access", [
            ("PI Analytics location", "Predictive Intelligence > Analytics (OOTB)", "No custom PA indicators in 18-week scope", False),
            ("Access role", "ml_analyst (OOTB)", "Customer PI Admin must have this role at go-live", True),
        ]),
    ],
    raci_rows=[
        ("Activate PI Analytics dashboard", "R/A", "Verify access", "ECS enables; Customer PI Admin confirms."),
        ("Record go-live KPI baseline", "R", "A", "ECS records all three model baselines."),
        ("30-day PI review", "R", "A", "ECS presents; Customer PM and IT Manager review."),
        ("Monthly accuracy monitoring (ongoing)", "N/A", "R/A", "Customer PI Admin owns post-stabilization."),
        ("Model drift investigation", "R (during hypercare)", "A", "ECS investigates during 2-week hypercare window."),
    ],
    consultant_guide_sections=[
        ("Framing success for the customer", "Present PI results in business terms: 'Category Classification reduced mis-categorized tickets by 25%. Assignment Intelligence cut first-assignment failures from 35% to 18%.' These numbers resonate with IT leadership far more than raw accuracy percentages."),
        ("Model drift early warning", "The most common cause of model drift is a taxonomy change (new category added, group renamed) without retraining. Build a checklist: any time the customer changes a category or renames a group, the affected PI model must be retrained. Add this to the Customer PI Admin runbook."),
        ("Phase 2 readiness", "At the 90-day review, if all three models are above target, introduce Phase 2 PI options: (1) Predictive Fields for additional incident fields, (2) agent-level assignment, (3) PI for change request categorization. Document as Phase 2 scope items with effort estimates."),
    ],
    adoption_rows=[
        ("PI models are trained but nobody uses the suggestions",
         "Monitor acceptance rates. Run champion exercise and refresher training.",
         "Low usage in week 1 is normal -- agents are cautious. Low usage at week 6 needs investigation.",
         "We pull the acceptance rate by agent from PI Analytics. The agents using PI most become our internal advocates. We ask them to share a time the similar incident suggestion saved them 30 minutes -- that story drives more adoption than any policy.",
         "If acceptance below 20% at 60 days -- structured refresher training required."),
    ],
    snmap_sections=[
        ("PI Analytics", [
            ("ml_analytics dashboard", "OOTB PI Analytics -- accuracy, acceptance rate, suggestion volume by model", "ml_analytics"),
            ("ml_training_run", "Training run log -- accuracy metrics per cycle", "ml_training_run"),
            ("ml_analyst role", "Grants Customer PI Admin access to PI Analytics dashboard", "sys_user_role"),
        ]),
    ],
)

def build_readme():
    meta = DocMeta(
        eyebrow="ACCELERATOR PACK",
        title="Predictive Intelligence\nAccelerator Pack",
        subtitle="OOTB PI -- Category Classification, Similar Incident, Assignment Intelligence, KPIs",
        doc_id="AP-17",
        version="1.0",
        status="Released",
        audience="ECS Consultants (Internal) + Customer IT Manager / Service Desk Lead (selected tabs)",
        running_header_label="Predictive Intelligence Accelerator Pack · ECS Federal",
        confidentiality="Internal Use Only · Confidential",
    )
    doc = EcsDocument(meta=meta)
    doc.add_cover_page()
    doc.h1("Pack Overview")
    doc.para(
        "AP-17 guides the ECS team through activating and configuring the three OOTB "
        "Predictive Intelligence models during Month 2-3 (Sprint 4-5) of the 18-week engagement. "
        "The pack covers PI scope and readiness, Category Classification, Similar Incident, "
        "Assignment Intelligence, and KPI measurement. All work is OOTB -- no custom ML models, "
        "no Python scripts, no external APIs. PI trains on historical incident data and improves "
        "automatically through weekly retraining cycles."
    )
    doc.h1("Workbook Inventory")
    doc.table(
        headers=["#", "Workbook", "Owner", "Sprint"],
        rows=[
            ("WB1", "PI Scope & Readiness Decisions", "ECS + Customer IT Manager", "Sprint 4"),
            ("WB2", "Category Classification Configuration", "ECS Architect", "Sprint 4"),
            ("WB3", "Similar Incident & Problem Intelligence", "ECS Architect", "Sprint 4"),
            ("WB4", "Assignment Intelligence Configuration", "ECS Architect", "Sprint 4-5"),
            ("WB5", "PI KPIs & Continuous Improvement", "ECS + Customer PI Admin", "Sprint 5"),
        ],
    )
    doc.h1("Key OOTB Decisions")
    doc.para(
        "Models: All three OOTB models activated (Category, Similar Incident, Assignment Group). "
        "Data requirement: 1,000+ closed incidents minimum; 5,000+ recommended. "
        "Suggestion mode: Agent-reviewed at go-live; auto-apply only after 80% accuracy for 30 days. "
        "Confidence threshold: 0.70 for all models (suppress below). "
        "Category freeze: taxonomy must be stable before training begins. "
        "KPI targets: 70% category accuracy, 40% similar incident acceptance, 65% first-assignment at go-live."
    )
    out = os.path.join(PACK_DIR, "00_README_Predictive_Intelligence_Pack.docx")
    doc.save(out)
    print(f"README saved: {out}")

if __name__ == "__main__":
    print("Building Predictive Intelligence Accelerator Pack...")
    workbooks = [
        ("01_pi_scope_readiness.xlsx", wb1),
        ("02_category_classification.xlsx", wb2),
        ("03_similar_incident.xlsx", wb3),
        ("04_assignment_intelligence.xlsx", wb4),
        ("05_pi_kpis.xlsx", wb5),
    ]
    for filename, content in workbooks:
        build_workbook(content, os.path.join(PACK_DIR, filename))
        print(f"  check {filename}")
    build_readme()
    print("Predictive Intelligence Accelerator Pack complete.")
