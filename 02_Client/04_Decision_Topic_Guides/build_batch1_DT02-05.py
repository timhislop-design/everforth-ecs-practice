"""Build CLT-DT-02 through CLT-DT-05."""
from dtg_builder import build_dtg

GUIDES = [

# ═══════════════════════════════════════════════════════════════════════════════
# CLT-DT-02  Category Structure Simplification
# ═══════════════════════════════════════════════════════════════════════════════
{
"doc_id": "CLT-DT-02",
"filename": "Category_Structure_Simplification_Decision_Guide_CLIENT.docx",
"short_name": "Category Structure Simplification",
"signal_subject": "your category structure",
"title": "Category Structure\nSimplification",
"subtitle": "A decision guide for shaping the taxonomy that routes and classifies your service delivery work",
"audience": "Service Owners, Catalog Owners, Process Managers, Service Desk Leadership",
"companion_to": "Catalog Item Rationalization Decision Guide · Workshop Pre-Read: Category Structure",
"how_to_use_paras": [
    "Every ticket submitted in ServiceNow carries a category. That category determines routing, "
    "SLA selection, reporting, and — once Predictive Intelligence is active — whether the platform "
    "routes it for you. The decisions in this guide shape that taxonomy: how many levels it has, "
    "what each level means, and how it stays coherent as your catalog and your organization evolve.",
    "Read this alongside the Catalog Item Rationalization guide. Catalog rationalization addresses "
    "what users can request; category structure addresses how those requests and incidents are "
    "classified after they arrive. The two reinforce each other — a rationalized catalog produces "
    "cleaner categories, and clean categories make a rationalized catalog easier to maintain.",
    "This is one of the decisions where organizations most commonly over-engineer the first draft "
    "and regret it by the end of the engagement. The questions below are designed to help you "
    "arrive at the simplest structure that is genuinely sufficient — not the most comprehensive "
    "one imaginable.",
],
"why_matters": [
    {"h2": "Category is the primary routing signal for every ticket",
     "body": "When an incident or request arrives, category is what tells ServiceNow which assignment "
             "group to route it to, which SLA to apply, and which reports to count it in. A category "
             "taxonomy that does not match how your teams actually organize work produces routing errors, "
             "SLA miscalculations, and reporting that nobody trusts. The category taxonomy is not a "
             "label — it is the routing engine for your entire service delivery operation."},
    {"h2": "Predictive Intelligence trains on your category data",
     "body": "When you activate Predictive Intelligence, the platform trains a machine learning model "
             "on your historical incident and request records. The model predicts the category of "
             "incoming tickets before an agent touches them. A category taxonomy with too many levels, "
             "too many near-synonyms, or inconsistent usage produces a model that predicts poorly — "
             "and an AI capability that agents learn to ignore. The quality of your category structure "
             "is the quality ceiling for your AI routing."},
    {"h2": "CSDM and Service Graph absorb context that used to live in categories",
     "body": "Many category structures grew large because they were doing double duty — carrying "
             "routing logic AND service context. ServiceNow's Common Service Data Model (CSDM) and "
             "CMDB now carry that service context directly, connected to the CI. This creates a real "
             "opportunity: categories can be simplified to pure routing taxonomy because the service "
             "context has a better home. Organizations that make this connection arrive at a "
             "two-level category structure that is dramatically simpler than what they started with."},
],
"signals": [
    {"h2": "Categories and subcategories number in the hundreds",
     "body": "A category taxonomy with more than 50–80 combined categories and subcategories is a "
             "signal that the structure has accumulated rather than been designed. Most routing "
             "requirements can be met with 20–40 categories and a matching set of subcategories. "
             "When the count is in the hundreds, the taxonomy is typically doing work that belongs "
             "elsewhere — in the CI, in the service classification, or in a custom field."},
    {"h2": "Agents categorize the same issue differently",
     "body": "If two agents handle the same type of incident and assign different categories, the "
             "taxonomy is ambiguous. Ambiguous categories produce a dataset that Predictive Intelligence "
             "cannot train on reliably, because the 'right' answer is inconsistent. This is the "
             "single strongest signal that a rationalization is needed before AI enablement."},
    {"h2": "Subcategory options change depending on category",
     "body": "Many legacy taxonomies implement dependent picklists — the subcategory options change "
             "based on the category selected. When this logic becomes complex (more than two or three "
             "levels of dependency), it becomes difficult to maintain and creates gaps when new "
             "categories are added. A flat two-level structure with clear definitions consistently "
             "outperforms complex dependent hierarchies for both usability and AI performance."},
    {"h2": "Reports show a long tail of rarely used categories",
     "body": "Pulling a report of incident volume by category almost always shows a small set of "
             "categories handling 80% of volume, and a large tail of categories that each account "
             "for fewer than 1% of tickets. The long tail is not necessarily wrong — some legitimate "
             "services are low volume — but categories with zero tickets in the past six months are "
             "strong retirement candidates."},
],
"decisions": [
    {"label": "What is the right taxonomy depth — one level, two, or more?",
     "body": "The most common OOTB-aligned answer is a two-level taxonomy: Category (the service "
             "domain or team, e.g., 'Network') and Subcategory (the type of issue within that "
             "domain, e.g., 'VPN Connectivity'). Three or more levels are occasionally warranted "
             "but require a clear rationale — typically a large organization where routing decisions "
             "genuinely require that specificity.",
     "questions": [
         "Can your assignment rules be expressed with two levels? If yes, two levels is sufficient.",
         "Does any routing decision require a third-level field, or can that context come from the CI?",
         "What does the taxonomy look like if you limit yourself to 30 categories and 5 subcategories each?",
     ],
     "landing": "Where customers usually land: a two-level structure with 20–40 categories and 3–8 "
                "subcategories per category. Organizations that try to keep three levels typically "
                "simplify to two after their first review cycle."},
    {"label": "What does each level mean — categorization, identification, or routing?",
     "body": "Categories should answer one question: which team or service domain is responsible? "
             "Subcategories should answer: what type of work is this within that domain? If a "
             "category or subcategory is carrying other context — the specific application affected, "
             "the affected business unit, the priority driver — that context belongs on a different "
             "field, not embedded in the taxonomy.",
     "questions": [
         "For each category, can you state in one sentence what routing decision it drives?",
         "Are there categories that are really CI types or application names rather than service domains?",
         "Are there subcategories that encode urgency or business impact rather than work type?",
     ],
     "landing": "Clean definitions: Category = service domain / owning team. Subcategory = work type "
                "within that domain. Everything else belongs in a CI field, a custom attribute, or CSDM."},
    {"label": "How does CSDM absorb what the taxonomy used to carry?",
     "body": "If your current category structure includes application names, business service names, "
             "or technology-stack identifiers, those are candidates for migration to CSDM data — "
             "specifically to the Business Application or Technical Service layer. This is the move "
             "that most enables taxonomy simplification: once CSDM carries service context, "
             "categories can return to being pure routing taxonomy.",
     "questions": [
         "Which of your current categories are really application names (e.g., 'SAP', 'Salesforce')?",
         "Which are really business service names ('Payroll', 'HR Systems')?",
         "Do you have a CSDM configuration in flight, or is this being built concurrently?",
     ]},
    {"label": "How do you sustain the simplification over time?",
     "body": "Category taxonomies grow for a reason: new services get stood up and someone needs "
             "a place to put their tickets. Without a governance process, a simplified taxonomy will "
             "re-accumulate over 12–18 months. The workshop will define the governance model: who "
             "owns the taxonomy, what process approves a new category, and what triggers a periodic "
             "review.",
     "questions": [
         "Who owns the category taxonomy today — and is that person empowered to reject additions?",
         "Is there a process for requesting a new category, or do they get added ad hoc?",
         "How frequently should the taxonomy be reviewed for unused entries?",
     ],
     "landing": "Most organizations designate a Process Manager as taxonomy owner with a quarterly "
                "review cycle. New categories require a brief business case reviewed by the owner."},
],
"good_rows": [
    ["Two-level structure with clear, distinct categories", "Three or more levels with ambiguous boundaries between them"],
    ["Category names reflect service domains and owning teams", "Category names reflect application names, technology stacks, or business units"],
    ["Agents agree on category assignment for the same issue type", "Agents categorize the same issue differently depending on who handles it"],
    ["Unused categories retired on a regular schedule", "Long tail of categories with zero or near-zero volume carried indefinitely"],
    ["New category requests go through a defined approval process", "Categories added ad hoc by anyone with access to the configuration"],
    ["Subcategory options are consistent and not context-dependent", "Subcategory options change based on upstream selections in complex ways"],
],
"patterns": [
    {"label": "Pattern A — Federal agency with 340-category legacy taxonomy",
     "body": "An agency carried a 340-category, four-level taxonomy from a legacy ITSM tool. "
             "Sixty percent of categories had fewer than 10 tickets in the prior year. Working through "
             "the four-decision framework, they identified that 180 of the 340 categories were "
             "application names that belonged in their CMDB Application CI class. After removing those "
             "and consolidating near-synonyms, the taxonomy reduced to 42 categories across two levels. "
             "Predictive Intelligence accuracy improved from 61% to 84% in the first three months "
             "after go-live on the simplified taxonomy."},
    {"label": "Pattern B — Healthcare system adding a third routing level",
     "body": "A healthcare IT organization initially designed a three-level taxonomy to distinguish "
             "clinical systems incidents from administrative systems incidents within each service domain. "
             "After building the CMDB with clinical vs. administrative CI classification, they realized "
             "the third level was redundant — the CI classification carried the distinction they needed. "
             "They simplified to two levels and retained the clinical/administrative distinction through "
             "CI data rather than category structure."},
    {"label": "Pattern C — Higher education adopting CSDM-first sequencing",
     "body": "A university delayed category simplification until their CSDM Business Application "
             "mapping was partially complete. This sequencing worked well: by the time they simplified "
             "categories, they had a clear view of which category entries were application names (which "
             "migrated to CSDM) and which were genuine service domains (which became categories). "
             "The result was a 28-category taxonomy built on a clean foundation rather than a "
             "simplified taxonomy that would need revisiting when CSDM arrived."},
],
"workshop_para": (
    "In the workshop, we will start by pulling your current category volume report and walking through "
    "it together. We will identify the long tail, the near-synonyms, and the categories that are "
    "carrying context that belongs elsewhere. From there, we will draft the target taxonomy on a "
    "whiteboard — working through the four decisions in sequence. By the end of the session, you will "
    "have a draft two-level taxonomy, a mapping from legacy categories to new ones, and a set of "
    "open items for teams whose categories need a separate conversation."
),
"need_bullets": [
    "Category and subcategory volume report from your current tool — incidents by category for the last 12 months",
    "Current category list (export or screenshot) with any dependent subcategory logic documented",
    "Assignment group mapping — which categories currently route to which teams",
    "CSDM status — whether Business Application or Technical Service data is in flight or planned",
],
"questions": [
    "How many categories does your current system have? Have you ever pulled a volume report by category?",
    "Are there categories that you already know are redundant or unused?",
    "Which teams would need to be involved in approving a taxonomy change that affects their routing?",
    "Is there a service catalog rationalization happening in parallel that will affect category design?",
    "Who has the authority to retire a category that is no longer needed?",
],
"xrefs": [
    ["Catalog Item Rationalization Decision Guide", "Companion guide — catalog rationalization and category simplification are designed together", "02_Client/04_Decision_Topic_Guides/"],
    ["Workshop Pre-Read: Category Structure", "15-minute background read for workshop participants", "02_Client/05_Workshop_Pre-Reads/"],
    ["CSDM Workshop Pre-Read", "Explains how CSDM absorbs service context that currently lives in category fields", "02_Client/05_Workshop_Pre-Reads/"],
    ["Predictive Intelligence Pre-Read", "Explains why category data quality is the AI training data quality ceiling", "02_Client/05_Workshop_Pre-Reads/"],
],
},

# ═══════════════════════════════════════════════════════════════════════════════
# CLT-DT-03  SLA Discipline
# ═══════════════════════════════════════════════════════════════════════════════
{
"doc_id": "CLT-DT-03",
"filename": "SLA_Discipline_Decision_Guide_CLIENT.docx",
"short_name": "SLA Discipline",
"signal_subject": "your SLA configuration",
"title": "SLA Discipline",
"subtitle": "A decision guide for configuring service level agreements that are accurate, trusted, and actionable",
"audience": "Service Desk Leadership, Incident Managers, Process Owners, IT Leadership",
"companion_to": "Incident Management Workshop Pre-Read · Assignment Rules Decision Guide",
"how_to_use_paras": [
    "SLAs are the operational contract between IT and the business. When configured correctly, they "
    "produce metrics that everyone trusts and dashboards that drive behavior. When configured "
    "incorrectly — or, more commonly, accumulated without discipline — they produce numbers that "
    "the team games around and leadership stops reading.",
    "Most organizations arrive at a ServiceNow implementation carrying SLA configurations that were "
    "built under different requirements, at different times, and by different people. The result is "
    "often a set of SLA definitions that measure different things depending on the ticket type, produce "
    "metrics that are technically correct but operationally misleading, and are defended more by habit "
    "than by design.",
    "This guide will help you approach the SLA conversation with a clear framework. The four decisions "
    "below are where the work lives. Bring them to the workshop with a view on each — even a "
    "provisional one — and the session will move much faster.",
],
"why_matters": [
    {"h2": "SLA data is the foundation for performance conversations",
     "body": "Every leadership report that references response times, resolution times, or breach rates "
             "draws on SLA data. If the SLA configuration is inconsistent — measuring different things "
             "for different ticket types, or including pause logic that few people understand — the "
             "numbers it produces will be questioned every time they appear in a deck. Correct SLA "
             "configuration produces numbers that survive scrutiny because they measure what "
             "they claim to measure."},
    {"h2": "SLAs drive agent behavior in real time",
     "body": "ServiceNow's SLA engine shows agents how much time remains on each ticket. When the "
             "SLA configuration is trusted, agents use that timer to prioritize their queue. When it "
             "is not trusted — because the definition includes pauses that reset unrealistically, "
             "or because the targets were set aspirationally and are breached almost universally — "
             "agents stop looking at the timer and prioritize by instinct instead. The SLA stops "
             "being a management tool and becomes a compliance checkbox."},
    {"h2": "AI capabilities use SLA context for prioritization",
     "body": "Predictive Intelligence and Now Assist both have access to SLA data when making "
             "recommendations. A ticket that is approaching SLA breach is a signal the platform "
             "uses to adjust recommendation priority. If your SLA definitions are inconsistent, "
             "that signal is noise. If they are clean and accurate, it becomes a meaningful input "
             "to every automated routing and prioritization decision."},
],
"signals": [
    {"h2": "SLA compliance rates are consistently near 100% or near 0%",
     "body": "A compliance rate that hovers near 100% suggests the targets were set too conservatively "
             "— the SLA is measuring a bar the team clears without effort, and provides no signal about "
             "performance pressure. A compliance rate near 0% suggests the targets are aspirational and "
             "have become irrelevant. Meaningful SLA targets should produce compliance rates that "
             "fluctuate with workload — typically in the 85–95% range for a healthy operation."},
    {"h2": "Different teams report different numbers for the same metric",
     "body": "When the service desk reports a 92% SLA compliance rate and the business reports that "
             "responses take too long, the SLA definition and the business expectation have diverged. "
             "This almost always means the SLA definition includes pauses, exclusions, or measurement "
             "start points that do not match how the business experiences time-to-response."},
    {"h2": "SLA pause logic is complex and inconsistently understood",
     "body": "SLA pause logic — pausing the timer when a ticket is awaiting customer response, "
             "awaiting a vendor, or in a particular state — is a legitimate and useful feature. But "
             "when pause conditions accumulate over time without review, they can substantially "
             "deflate apparent response times. When new team members cannot explain the pause logic "
             "from memory, it has become too complex to be trustworthy."},
    {"h2": "Too many SLA definitions covering similar scenarios",
     "body": "A common pattern is an SLA definition per priority level, plus additional definitions "
             "per service area, plus additional definitions for specific customer groups — resulting "
             "in 30 or 40 active SLA definitions. When SLA definitions multiply, gaps appear: "
             "tickets fall through definition gaps and are measured by no SLA at all, or measured "
             "by the wrong one. The minimum effective set is usually 4–8 definitions for most organizations."},
],
"decisions": [
    {"label": "Which SLAs will you formalize in ServiceNow?",
     "body": "The most important SLA design question is scope: which commitments will you formally "
             "configure in ServiceNow, and which will you leave unmeasured or measured externally? "
             "The recommendation is to start with the SLAs you are already held accountable to — "
             "your existing service level targets — and configure exactly those. Add new targets "
             "only when there is an explicit business requirement.",
     "questions": [
         "What SLA targets is your team currently measured against? Are they documented?",
         "Are there targets you aspire to but do not currently meet consistently?",
         "Are there customer-specific commitments that differ from your standard targets?",
     ],
     "landing": "Most organizations configure 4–8 SLA definitions: one per priority level for Incident "
                "(P1–P4), plus a small number for specific service areas with distinct commitments."},
    {"label": "How will you set targets — based on current performance or desired performance?",
     "body": "Setting SLA targets is a choice between descriptive (what we currently achieve) and "
             "aspirational (what we want to achieve). Aspirational targets are legitimate, but they "
             "require explicit acknowledgment that initial compliance rates will be low and a plan for "
             "closing the gap. Targets set without that acknowledgment tend to be quietly abandoned "
             "when breaches become normalized.",
     "questions": [
         "Do you know your current average response and resolution times by priority?",
         "Are there business commitments (contracts, MOUs) that mandate specific targets?",
         "If you set targets at your current performance level, would that be acceptable to leadership?",
     ]},
    {"label": "What pause logic, if any, is appropriate?",
     "body": "Pause conditions should be used for time periods where the IT team genuinely cannot "
             "progress the ticket: awaiting a mandatory response from the user to continue, "
             "outside contracted support hours, or awaiting a third-party vendor with no workaround. "
             "Pauses should not be used to manufacture compliance on tickets that are simply "
             "deprioritized or waiting in a queue.",
     "questions": [
         "Do you have contracted support hours that should affect SLA measurement?",
         "Are there ticket types where user response is genuinely required before IT can proceed?",
         "How is 'awaiting vendor' currently handled — and is it legitimate to pause the SLA clock?",
     ],
     "landing": "Simplest working approach: pause only for out-of-hours (if you have contracted hours) "
                "and awaiting-mandatory-user-response. Everything else keeps the clock running."},
    {"label": "How will breaches be managed and reported?",
     "body": "SLA breach management — who is notified when a ticket is approaching breach, who owns "
             "the escalation, what happens in reporting — is as important as the SLA definition "
             "itself. ServiceNow's OOTB SLA engine sends configurable notifications at configurable "
             "thresholds (e.g., 50%, 75%, 90% of time elapsed). The workshop will define the "
             "notification matrix and the breach reporting cadence.",
     "questions": [
         "Who should be notified when a Priority 1 ticket is approaching breach?",
         "Is there an escalation path for P1/P2 tickets that are at risk?",
         "How frequently should SLA compliance reports be reviewed — daily, weekly?",
     ]},
],
"good_rows": [
    ["4–8 SLA definitions covering all in-scope scenarios", "30+ SLA definitions with gaps and overlaps between them"],
    ["Targets reflect actual or explicitly agreed performance goals", "Targets set aspirationally without a gap-closure plan"],
    ["Compliance rates in the 85–95% range, fluctuating with volume", "Compliance near 100% or near 0% — both indicate a miscalibrated target"],
    ["Pause logic is simple, documented, and understood by the team", "Complex pause conditions that few people can explain from memory"],
    ["SLA metrics appear in leadership reviews and are discussed", "SLA reports are produced but rarely referenced in performance conversations"],
    ["Breach notifications go to the right people at the right threshold", "Breaches are discovered after the fact rather than flagged in advance"],
],
"patterns": [
    {"label": "Pattern A — Agency with 47 active SLA definitions",
     "body": "A federal agency carried 47 SLA definitions built across multiple years and organizational "
             "changes. Analysis showed that 22 of the definitions covered scenarios already handled by "
             "other definitions, and 11 were attached to ticket types that had been retired. Working "
             "through the four-decision framework, the agency reduced to 6 definitions — one per priority "
             "level — and saw a 40% reduction in tickets that fell through SLA gaps. Leadership "
             "reporting became a single dashboard that everyone understood."},
    {"label": "Pattern B — Healthcare system with near-zero compliance",
     "body": "A hospital IT team had aspirational SLA targets that produced a 12% compliance rate. "
             "Rather than lower targets, the team analyzed the gap: 60% of breaches occurred in P3 "
             "tickets that waited more than 48 hours before first touch. The root cause was queue "
             "management, not target setting. They kept the targets, changed the P3 queue management "
             "process, and compliance rose to 78% within two sprints — without changing a single "
             "SLA definition."},
    {"label": "Pattern C — Technology company simplifying pause logic",
     "body": "A software company had accumulated 14 pause conditions across their SLA definitions, "
             "including pauses for 'awaiting architecture review' and 'pending budget approval.' "
             "Auditing the pause conditions revealed that 9 of the 14 were used to park tickets "
             "that were deprioritized, not genuinely blocked. Removing those pauses doubled their "
             "apparent breach rate in month one — but gave leadership an accurate picture of queue "
             "health for the first time. The ensuing conversation about P3 staffing was overdue."},
],
"workshop_para": (
    "In the workshop, we will start with your current SLA definitions — pulling a list and reviewing "
    "volume, compliance rates, and pause usage per definition. From that baseline, we will work through "
    "the four decisions: which SLAs to keep, what targets to set, what pause logic to retain, and "
    "how breaches will be managed. By the end of the session you will have a draft SLA definition set "
    "and a notification matrix ready for configuration."
),
"need_bullets": [
    "Current SLA definition list (export from existing system) with targets per definition",
    "SLA compliance report for the last 6–12 months — by priority level and by service area",
    "Any existing SLA documentation from service contracts, MOUs, or IT policy",
    "List of current breach notification recipients and escalation paths",
],
"questions": [
    "How many active SLA definitions does your current system have?",
    "What is your current SLA compliance rate by priority level?",
    "Are there contractual SLA commitments that are non-negotiable?",
    "Does your team currently use pause logic, and do you understand when it applies?",
    "When was the last time your SLA targets were reviewed and updated?",
],
"xrefs": [
    ["Incident Management Workshop Pre-Read", "SLA configuration is part of the Incident Management sprint", "02_Client/05_Workshop_Pre-Reads/"],
    ["Assignment Rules Decision Guide", "SLA selection often depends on assignment group — the two are designed together", "02_Client/04_Decision_Topic_Guides/"],
    ["Performance Analytics Pre-Read", "SLA data is a primary input to PA dashboards", "02_Client/05_Workshop_Pre-Reads/"],
],
},

# ═══════════════════════════════════════════════════════════════════════════════
# CLT-DT-04  Assignment Rules
# ═══════════════════════════════════════════════════════════════════════════════
{
"doc_id": "CLT-DT-04",
"filename": "Assignment_Rules_Decision_Guide_CLIENT.docx",
"short_name": "Assignment Rules",
"signal_subject": "your assignment rule configuration",
"title": "Assignment Rules",
"subtitle": "A decision guide for routing tickets to the right team automatically — without building a maze",
"audience": "Process Managers, Service Desk Leadership, Assignment Group Owners, IT Operations",
"companion_to": "Category Structure Simplification Decision Guide · SLA Discipline Decision Guide",
"how_to_use_paras": [
    "Assignment rules are the logic that tells ServiceNow which team gets a ticket when it arrives. "
    "Done well, they are invisible — tickets land in the right queue and work begins immediately. "
    "Done poorly, they become the source of the most common service desk complaint: the wrong team "
    "got this, and now someone has to reassign it.",
    "Most organizations arrive at implementation with assignment logic that has been tuned over years: "
    "a rule for this application, a rule for this customer, a rule for this location. Each rule made "
    "sense when it was added. Together, they often form a web of overlapping conditions that no one "
    "person fully understands — and that ServiceNow's rule engine applies in unpredictable order.",
    "The four decisions in this guide address how to design assignment rules that are simple enough "
    "to maintain, accurate enough to be trusted, and structured to improve as Predictive Intelligence "
    "takes over more of the routing work over time.",
],
"why_matters": [
    {"h2": "Routing accuracy directly determines mean time to resolution",
     "body": "Every reassignment adds latency. A ticket that is correctly routed on first submission "
             "reaches resolution faster than one that bounces through two queues first. In high-volume "
             "environments, even a 10% reduction in reassignment rates produces measurable MTTR "
             "improvement — without changing staffing or processes. Assignment rule quality is a "
             "direct lever on your service delivery speed."},
    {"h2": "Rule complexity compounds maintenance cost",
     "body": "Every assignment rule is a configuration artifact that needs to be maintained as your "
             "organization changes. When a team is renamed, split, or absorbed, every rule that "
             "references that team requires an update. Organizations with 200+ assignment rules "
             "find that operational changes consume disproportionate administrative effort — not "
             "because the changes are complex, but because they touch so many rules."},
    {"h2": "Predictive Intelligence makes simple rules more valuable, not redundant",
     "body": "When Predictive Intelligence is active, it provides assignment group suggestions based "
             "on ML patterns in historical data. Simple, consistent assignment rules produce cleaner "
             "historical data — which produces better ML predictions. The relationship is compounding: "
             "good rules today produce better AI tomorrow. Complex, inconsistent rules produce noisy "
             "historical data that limits how accurate Predictive Intelligence can become."},
],
"signals": [
    {"h2": "Reassignment rate is above 15–20%",
     "body": "A reassignment rate above 15–20% is a reliable signal that initial assignment accuracy "
             "is low — either because the rules do not match the actual team structure, or because "
             "agents are manually reassigning tickets that arrived in the right queue but were "
             "then re-categorized. Either way, the rules need review."},
    {"h2": "Nobody can explain what triggers a specific rule",
     "body": "If the team cannot answer 'why did this ticket go to that group?' without checking "
             "the rule configuration, the rules have become opaque. Opaque rules are not just "
             "a maintenance problem — they are a trust problem. When agents do not understand "
             "routing logic, they route manually rather than relying on the system."},
    {"h2": "Rules fire in unexpected order",
     "body": "ServiceNow processes assignment rules in order of their configured sequence. When "
             "many rules overlap in their conditions, the effective order is difficult to predict "
             "without testing. Organizations that have added rules incrementally without reviewing "
             "the overall sequence often find that early rules in the order prevent later, more "
             "specific rules from firing."},
    {"h2": "Assignment group names do not match organizational team names",
     "body": "When the assignment groups in ServiceNow no longer match the names your teams use "
             "for themselves — because of reorganizations, renaming, or mergers — the routing "
             "configuration falls out of sync with operational reality. This is one of the most "
             "common post-implementation drift patterns."},
],
"decisions": [
    {"label": "What criteria should drive assignment — category alone, or category plus CI?",
     "body": "The simplest assignment rule model routes based on category and subcategory alone: "
             "'Network / VPN Connectivity' goes to the Network team. The more powerful model adds "
             "the Configuration Item (CI) as a routing signal: 'the application affected is the "
             "Payroll system, which is owned by the ERP team.' CMDB-based routing produces higher "
             "accuracy but requires CMDB data to be reliable.",
     "questions": [
         "Is your CMDB current enough to trust as a routing signal?",
         "Are there ticket types where the right team depends on which system is affected, not just the category?",
         "Are there routing cases today where category alone is ambiguous?",
     ],
     "landing": "Most organizations start with category-based routing and add CI-based rules incrementally "
                "as CMDB data matures. Starting with CI-based routing before the CMDB is reliable produces "
                "routing errors that undermine trust in the system."},
    {"label": "How many rules do you need, and in what order?",
     "body": "The target is the minimum rule set that correctly routes all in-scope ticket types. "
             "A working starting point: one rule per category-subcategory combination that maps to "
             "a distinct owning team. This produces a rule count roughly equal to your number of "
             "categories — typically 20–50 rules rather than hundreds.",
     "questions": [
         "How many assignment groups do you have?",
         "For each category, is there one clear owning team, or do multiple teams share a category?",
         "Are there conditions beyond category (caller location, VIP status) that legitimately change routing?",
     ]},
    {"label": "What is the fallback when no rule matches?",
     "body": "Every assignment rule design needs a defined fallback: the group that receives tickets "
             "when no specific rule applies. This is typically the service desk or a triage group. "
             "The fallback volume is a useful metric — high fallback volume means the rule set has "
             "coverage gaps that need addressing.",
     "questions": [
         "Which team should receive tickets that no rule matches?",
         "Is there a monitoring process for fallback queue volume?",
     ]},
    {"label": "Who owns the rules post-go-live, and what is the change process?",
     "body": "Assignment rules require ongoing maintenance as teams change, categories are added, "
             "and new services are onboarded. Without clear ownership, rules accumulate without review "
             "and the rule set gradually decouples from operational reality. The workshop will "
             "define an owner and a lightweight change process.",
     "questions": [
         "Who has authority to add, modify, or retire assignment rules today?",
         "Is there a documented process for requesting a routing change?",
         "How will new services be onboarded — is there a step in the service design process for assignment rule creation?",
     ]},
],
"good_rows": [
    ["One rule per category/subcategory with a clear owning team", "Hundreds of rules with overlapping conditions and unpredictable firing order"],
    ["Reassignment rate below 10%", "Reassignment rate above 20% indicating systematic routing errors"],
    ["All team members can explain why a ticket was routed the way it was", "Routing logic is opaque — agents route manually because they do not trust rules"],
    ["Fallback queue is monitored and coverage gaps are closed promptly", "Fallback queue is a dumping ground that nobody monitors"],
    ["Assignment group names match current organizational team names", "Group names reflect a previous org structure that no longer exists"],
    ["Rules owned by a named administrator with a defined change process", "Rules modified ad hoc by anyone with admin access"],
],
"patterns": [
    {"label": "Pattern A — Agency reducing 340 rules to 38",
     "body": "A federal agency entered implementation with 340 assignment rules accumulated across "
             "eight years. Analysis found that 210 rules were for organizational units that no longer "
             "existed, 60 were redundant with other rules, and 30 were never firing due to rule order "
             "issues. Working through the four decisions, they rebuilt the rule set from scratch with "
             "38 category-based rules. Reassignment rate dropped from 28% to 9% in the first month."},
    {"label": "Pattern B — Phased CI-based routing",
     "body": "A technology company wanted CI-based routing from day one, routing tickets to application "
             "owners based on the affected CI rather than category. The CMDB was not yet fully "
             "populated, so they implemented category-based rules as an interim measure and flagged "
             "each rule for review once the relevant CI class was populated. Six months post-go-live, "
             "30% of rules had been upgraded to CI-based routing as CMDB data matured."},
    {"label": "Pattern C — Shared categories with conditional routing",
     "body": "A higher education IT organization had categories shared across multiple teams — "
             "'Network' was handled by two different teams depending on whether the campus was "
             "residential or academic. They solved this with a caller-location field on the incident "
             "form and a two-condition rule: category + location. The rule set remained simple, and "
             "routing accuracy for the shared categories improved from 68% to 94%."},
],
"workshop_para": (
    "The workshop will start with your current assignment group list and a sample of recent reassignment "
    "data. We will map categories to owning teams, identify shared categories that need conditional "
    "logic, define the fallback, and establish the minimum rule set. The output is a documented rule "
    "set ready for configuration, and a rule ownership assignment."
),
"need_bullets": [
    "Current assignment group list — all active groups with current team leads",
    "Reassignment rate data for the last 6 months (from current tool if available)",
    "Category-to-team mapping — which categories does each team own?",
    "Any location, VIP, or other conditions that currently affect routing",
],
"questions": [
    "How many assignment groups do you currently have, and do they match your current team structure?",
    "What is your current reassignment rate — do you have data on this?",
    "Are there routing decisions that genuinely require conditions beyond category (location, customer, CI)?",
    "Who currently has access to modify assignment rules?",
    "Is there any category that is shared between two or more teams depending on context?",
],
"xrefs": [
    ["Category Structure Simplification Decision Guide", "Assignment rules depend on category structure — design them together", "02_Client/04_Decision_Topic_Guides/"],
    ["SLA Discipline Decision Guide", "SLA selection often depends on assignment group — the two are designed in parallel", "02_Client/04_Decision_Topic_Guides/"],
    ["CMDB Workshop Pre-Read", "CI-based routing requires reliable CMDB data — understand the maturity sequence", "02_Client/05_Workshop_Pre-Reads/"],
],
},

# ═══════════════════════════════════════════════════════════════════════════════
# CLT-DT-05  Approval Discipline
# ═══════════════════════════════════════════════════════════════════════════════
{
"doc_id": "CLT-DT-05",
"filename": "Approval_Discipline_Decision_Guide_CLIENT.docx",
"short_name": "Approval Discipline",
"signal_subject": "your approval configuration",
"title": "Approval Discipline",
"subtitle": "A decision guide for configuring approvals that are necessary, traceable, and no more burdensome than they need to be",
"audience": "Process Managers, Service Owners, IT Leadership, Catalog Owners, Change Managers",
"companion_to": "Service Catalog Decision Guide · Change Management Workshop Pre-Read",
"how_to_use_paras": [
    "Approvals exist to ensure that changes to IT assets or services have appropriate oversight "
    "before they proceed. In theory, every approval adds value. In practice, unnecessary approvals "
    "are one of the most common drivers of two expensive behaviors: abandonment (users give up and "
    "ask someone verbally) and routing-around (users use channels that bypass the approval entirely).",
    "ServiceNow's approval engine is powerful and configurable. It can implement sequential approvals, "
    "parallel approvals, group approvals, threshold-based approvals, and auto-approvals — each with "
    "its own timeout, escalation, and notification logic. That power makes the design decision more "
    "important: a well-designed approval structure is invisible to users who get approved quickly "
    "and visible only when oversight genuinely matters.",
    "The four decisions in this guide address how to identify which approvals are necessary, "
    "how to implement them with minimum friction, and how to prevent approval accumulation "
    "from re-occurring after go-live.",
],
"why_matters": [
    {"h2": "Unnecessary approvals create workarounds that bypass the system entirely",
     "body": "When approval chains are too long or too slow, users learn to route around them. "
             "They ask managers verbally, they use personal email to request access, they have "
             "a colleague submit the ticket on their behalf. Each workaround removes a record "
             "from the system that should be there — reducing the data quality that AI and "
             "reporting depend on, and creating audit gaps that surface as findings."},
    {"h2": "Approval friction concentrates in the highest-volume, lowest-risk requests",
     "body": "The requests that generate the most approval traffic are usually the most routine: "
             "standard software licenses, basic access requests, hardware replacements. These are "
             "also the requests where the business case for approval is weakest. Concentrating "
             "approval governance on high-risk, non-standard requests — while pre-approving routine "
             "work — is the design principle that produces the best ratio of control to friction."},
    {"h2": "Auto-approval and Standard Change logic directly reduce CAB burden",
     "body": "For change management, the single highest-leverage design decision is how many changes "
             "qualify as Standard (pre-approved). Every change that qualifies as Standard removes "
             "one item from the CAB agenda, reduces the time between change request and implementation, "
             "and gives the team executing the change a cleaner record. The Standard Change library "
             "is the most direct path to a lighter CAB workload."},
],
"signals": [
    {"h2": "Requests sit in approval queues for days",
     "body": "When the average time-in-approval exceeds 24–48 hours for routine requests, either "
             "the approval chain is too long, approvers are not receiving effective notifications, "
             "or approvers are approving in batches rather than on receipt. All three are solvable "
             "through configuration — but the first step is identifying which is the cause."},
    {"h2": "Approvers are not sure what they are approving",
     "body": "When an approver receives an approval notification but cannot tell from the "
             "notification what they are being asked to review, they either approve reflexively "
             "(defeating the purpose) or open the full record to investigate (adding friction "
             "for every approval). Approval notifications should include enough context for an "
             "informed decision without requiring a click-through."},
    {"h2": "Multiple approvals are required for the same request across different systems",
     "body": "In organizations that have not rationalized their approval architecture, a single "
             "user request may require approval in ServiceNow, in an Active Directory management "
             "tool, and via an email to a team lead — three separate approvals for what is "
             "effectively the same business decision. Centralizing approval in ServiceNow "
             "eliminates this duplication and produces a single audit record."},
    {"h2": "Approval chains grow with every new catalog item",
     "body": "When each new catalog item is built with a bespoke approval chain rather than "
             "shared approval templates, the approval configuration grows in complexity with "
             "every new item. Within 12–18 months, the total approval configuration becomes "
             "difficult to audit and maintain."},
],
"decisions": [
    {"label": "Which requests and changes genuinely require human approval?",
     "body": "Start with a clean-sheet question: if you were designing this approval architecture "
             "today, with full knowledge of your audit requirements and business risk, which "
             "transactions would require a human being to explicitly authorize before proceeding? "
             "The answer should be grounded in policy, audit requirement, or specific risk — "
             "not in historical practice.",
     "questions": [
         "Are there audit or compliance requirements (FedRAMP, FISMA, SOC 2) that mandate specific approval steps?",
         "Which categories of request carry real financial, security, or compliance risk if approved incorrectly?",
         "Which approvals exist by habit rather than by policy — and what would happen if they were removed?",
     ],
     "landing": "High-risk access grants, budget-impacting purchases above a threshold, non-standard "
                "changes, and externally-mandated approvals. Routine access, standard software, "
                "hardware replacements within budget — these are pre-approval candidates."},
    {"label": "What approval model — sequential, parallel, or group?",
     "body": "Sequential approval requires each approver to act in order. Parallel approval sends "
             "to all approvers simultaneously and moves forward when all approve. Group approval "
             "sends to a group and moves forward when any one member approves. For most catalog "
             "items, group approval (any member of the relevant team) is the fastest and most "
             "resilient model — it avoids single-approver bottlenecks without sacrificing oversight.",
     "questions": [
         "Are there approvals that legally or contractually require a specific named individual?",
         "Are there cases where approval requires inputs from multiple parties simultaneously?",
         "What happens to approvals when the designated approver is on leave?",
     ]},
    {"label": "What thresholds trigger a higher approval tier?",
     "body": "Many organizations tier their approvals by value or risk: requests under $500 "
             "are approved by a team lead, requests over $500 require a director, requests over "
             "$5,000 require an executive. Encoding these thresholds in ServiceNow produces "
             "consistent approval routing without requiring the requester or the service desk "
             "to make a judgment call.",
     "questions": [
         "Do you have existing financial authorization thresholds documented?",
         "Are there risk-based thresholds (e.g., access to sensitive data systems) that should trigger elevated approval?",
     ]},
    {"label": "What qualifies as Standard Change (pre-approved)?",
     "body": "Standard Changes are changes that have been pre-approved as low-risk and routine: "
             "patching a standard server within the maintenance window, deploying a pre-tested "
             "configuration change, resetting a service account password. Building a Standard "
             "Change library of 15–25 common change types dramatically reduces CAB volume and "
             "accelerates routine change delivery.",
     "questions": [
         "What are the most common changes your team performs that follow a known, tested process?",
         "Which changes have a documented rollback procedure and a history of no failures?",
         "Is there a CAB member or change manager who can sponsor the initial Standard Change library?",
     ]},
],
"good_rows": [
    ["Approval required only where there is a documented policy or risk rationale", "Approvals added to new items by default without review of whether they are needed"],
    ["Group approval model with backup approvers defined", "Single named approver with no backup — approvals stall when that person is unavailable"],
    ["Standard Change library covers the top 15–25 routine change types", "All changes go through CAB regardless of risk level or routine nature"],
    ["Approval notifications include enough context for an informed decision", "Approvers must open the full record to understand what they are approving"],
    ["Time-in-approval monitored and reported; SLA on approval response", "Approval queue monitored only when a user complains about delay"],
    ["Approval configuration uses shared templates rather than per-item logic", "Each catalog item has bespoke approval logic that duplicates configuration"],
],
"patterns": [
    {"label": "Pattern A — Agency removing 40% of approval steps",
     "body": "A government agency audited its approval configuration and found that 40% of approval "
             "steps had no documented policy basis — they had been added when individual managers "
             "wanted visibility into specific request types and never removed. Removing those steps "
             "reduced average catalog request fulfillment time from 4.2 days to 1.8 days. No audit "
             "finding resulted from the change because none of the removed approvals were "
             "policy-mandated."},
    {"label": "Pattern B — Building a 22-item Standard Change library",
     "body": "A technology company entered implementation with no Standard Change definition and a "
             "CAB that met twice weekly to review an average of 60 changes per session. Working "
             "through their change history, they identified 22 change types that qualified as "
             "Standard — representing 55% of their change volume. After implementation, CAB volume "
             "dropped to an average of 27 changes per session, and meeting duration was cut in half."},
    {"label": "Pattern C — Threshold-based approval for procurement",
     "body": "A healthcare organization implemented tiered approval for hardware procurement: under "
             "$1,000 approved by IT team lead (automated notification, 24-hour response SLA), "
             "$1,000–$10,000 requires IT director approval, over $10,000 requires CFO approval. "
             "Previously all procurement approvals went to the IT director regardless of amount. "
             "IT director approval volume dropped 70%, and approval cycle time for sub-$1,000 "
             "requests dropped from 3.2 days to 6 hours."},
],
"workshop_para": (
    "The workshop will review your current catalog items and change types with approval logic attached. "
    "For each, we will ask: is this approval policy-required, risk-based, or habitual? We will draft "
    "a simplified approval matrix, define Standard Change candidates, and configure shared approval "
    "templates that can be reused across catalog items rather than rebuilt for each one."
),
"need_bullets": [
    "Current catalog item list with approval chains documented (or a sample of the most common items)",
    "Change management policy and current CAB membership",
    "Any financial authorization thresholds in policy documents",
    "Compliance or audit requirements that mandate specific approval steps",
],
"questions": [
    "Are there compliance or audit requirements that mandate specific approval chains?",
    "What is the current average time-in-approval for your most common request types?",
    "Have you identified which change types in your environment are routine and low-risk?",
    "Who is authorized to waive or reduce an approval step — and under what conditions?",
    "Do you currently have a Standard Change catalog or pre-approved change list?",
],
"xrefs": [
    ["Service Catalog & Request Workshop Pre-Read", "Approval design is part of the Catalog & Request sprint", "02_Client/05_Workshop_Pre-Reads/"],
    ["Change Management Workshop Pre-Read", "Standard Change library design is covered in the Change workshop", "02_Client/05_Workshop_Pre-Reads/"],
    ["Custom-vs-OOTB Decision Framework", "Approval logic is a common customization target — understand when OOTB is sufficient", "02_Client/04_Decision_Topic_Guides/"],
],
},

]  # end GUIDES

if __name__ == "__main__":
    print(f"\nBuilding {len(GUIDES)} Decision Topic Guides (batch 1: DT-02 to DT-05)...\n")
    for g in GUIDES:
        build_dtg(g)
    print(f"\n✅  Batch 1 complete.\n")
