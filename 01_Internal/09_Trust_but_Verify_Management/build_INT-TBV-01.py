"""
Build INT-TBV-01 — Manager's Trust-But-Verify Playbook
Refactored to use the canonical ecs_template module so all branding decisions live
in one place. Re-run this any time content needs updating.
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

OUT = os.path.join(HERE, "Managers_Trust-But-Verify_Playbook_INTERNAL.docx")

d = EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL MANAGEMENT PLAYBOOK · TRUST-BUT-VERIFY DISCIPLINE",
    title="Manager's Trust-But-Verify\nPlaybook",
    subtitle="How ECS practice management catches OOTB-first drift before it becomes the next engagement's technical debt",
    audience="Practice Lead, Engagement Managers, Solution Architects, Process Consultants",
    companion_to="ECS Internal Governance Operating Guide · Consultant Handbook (INT-CH-01) · OOTB Delivery Playbook",
    doc_id="INT-TBV-01",
    version="1.0",
    status="Released",
    running_header_label="Internal · Manager's Trust-But-Verify Playbook",
))

# ---------- COVER ----------
d.add_cover_page()

# Brief opener after cover (still on page 1, below the meta block)
d.para(
    "The OOTB-first model only survives when management can see drift before the customer sees it. "
    "This playbook is the operating manual for that vigilance — the cadence, the signals, the "
    "templates, and the course-correction levers that make the discipline portable across the practice. "
    "It is not a sales artifact, not a customer document, and not optional reading. Every Engagement "
    "Manager runs from this book.",
)

# ---------- HOW TO USE ----------
d.h1("How to Use This Playbook", numbered=False)
d.para(
    "The playbook serves three uses. First, it onboards new Engagement Managers and Practice Leads onto the "
    "Trust-But-Verify discipline so the team converges on a single management approach across engagements. "
    "Second, it provides the operating cadence — what is reviewed weekly, bi-weekly, monthly, and quarterly — "
    "and the templates that anchor each cadence event. Third, it catalogs the eight companion artifacts in "
    "the Trust-But-Verify pack (INT-TBV-02 through INT-TBV-09) and shows where each one fits in the cadence."
)
d.para("Read order by role:", bold=True, space_after=2)
d.bullet("Practice Lead — read in full; you own the monthly review and cross-engagement pattern-spotting (Sections 1, 2, 8, 9).")
d.bullet("Engagement Manager — read in full; you run the weekly variance scan, bi-weekly sponsor sync, and own the customization council (Sections 1, 2, 4, 5, 6, 9).")
d.bullet("Solution Architect — Sections 1, 4, 6, 7. You feed the variance signal upward and run the demo-discipline audit downward.")
d.bullet("Process Consultant — Sections 1, 7, 10. You see the daily evidence; the playbook tells you what to escalate and how.")

d.callout(
    "If you are new to the practice, pair this playbook with the ECS Internal Governance Operating Guide. "
    "That guide describes the deviation lifecycle, the two-key decision, and the Customization Council mechanics. "
    "This playbook describes how management uses those mechanics to catch drift early."
)

d.page_break()

# ---------- 1. THE DISCIPLINE ----------
d.h1("The Trust-But-Verify Discipline")
d.h2("Why the discipline exists")
d.para(
    "ECS sells an OOTB-first delivery model whose value propositions are accelerated AI realization and "
    "systematic technical-debt elimination. Both depend on the same operational truth: customizations creep in "
    "not because anyone decided to customize, but because no one had the OOTB defense ready in the moment. "
    "The drift is silent. By the time the SOW reads 'OOTB-aligned' and the sprint demo shows a customized form, "
    "the discipline gap has already become a build commitment."
)
d.para(
    "Trust-But-Verify is the management posture that catches drift while it is still cheap to reverse. "
    "We trust the consultant team to run the model. We verify weekly that what is being built matches what was sold."
)

d.h2("The two failure modes management must catch")
d.para("Drift in an OOTB-first engagement takes one of two recognizable shapes. Both are catchable. Neither is rare.")
d.h3("Failure Mode A — Silent custom drift")
d.para(
    "The team builds custom artifacts under OOTB-first branding. Each individual change passes the smell test ("
    "'just one client script,' 'just a small UI policy,' 'just a workflow tweak') but the cumulative weight pushes "
    "the engagement off the OOTB baseline. The sprint demo looks great. The technical debt roadmap looks fine. "
    "Six months post-go-live, the customer cannot adopt a Now Assist update without rework. This is the most common "
    "failure mode and the one Trust-But-Verify is primarily designed to prevent."
)
d.h3("Failure Mode B — OOTB compliance theater")
d.para(
    "The team builds nothing custom and ships an unusable product. The configuration is technically OOTB, but the "
    "categories were not rationalized, the SLAs were not aligned to real operating hours, the catalog has 800 items "
    "instead of 80, and the customer's service experience is worse than what they had. This failure mode is rarer "
    "but more damaging to the practice's reputation. The playbook covers it under Section 7 (Demo Discipline Audit) "
    "and Section 10 (Coaching)."
)

d.h2("The Five Health Vectors")
d.para(
    "Every active engagement is scored along five vectors at the weekly cadence. The vectors are deliberately "
    "operational — what changed in the build, not what people felt about the meeting. Sentiment matters, but it lags "
    "the leading indicators. The Engagement Health Dashboard (INT-TBV-02) is structured around these five vectors."
)
d.table(
    headers=["Vector", "What it measures", "Primary signal source"],
    rows=[
        ["Process Adoption",       "Are the configured processes (Incident, Change, Catalog, etc.) running through OOTB tables and states without custom routing?", "Sprint demo + Configuration Audit"],
        ["Configuration Hygiene",  "Are catalog items, categories, assignment rules, SLAs, approvals, and notifications within OOTB-defensible counts and patterns?", "Sprint demo + Variance Tracker"],
        ["Customization Variance", "How many customizations have been raised, classified, decided, and built relative to the SOW baseline?", "Customization Variance Tracker (INT-TBV-03)"],
        ["Adoption Readiness",     "Is the customer team running OOTB-aligned operating procedures, not custom workarounds?", "Workshop notes + UAT pre-reads"],
        ["Sentiment & Trust",      "Is the customer sponsor aligned, neutral, or already invoking 'but our old system did X'?", "Bi-weekly Sponsor Sync (INT-TBV-04)"],
    ],
    col_widths_in=[1.6, 4.2, 2.6],
)

d.h2("What manager-level vigilance looks like")
d.para(
    "Trust-But-Verify is a posture, not a checklist. The Engagement Manager spends roughly an hour each week running "
    "the variance scan and dashboard review. The Practice Lead spends roughly two hours each month rolling up across "
    "engagements. The Solution Architect contributes the configuration evidence. None of this is heavy. What makes it "
    "work is consistency: the same three signals reviewed at the same cadence in the same template every week."
)

d.page_break()

# ---------- 2. CADENCE ----------
d.h1("The Management Cadence")
d.para(
    "The cadence is the operating skeleton of Trust-But-Verify. Skipping a cadence event is the single most common "
    "way drift goes undetected. The table below summarizes; sections that follow detail each event."
)
d.table(
    headers=["Cadence", "Event", "Owner", "Companion Template", "Time"],
    rows=[
        ["Weekly",        "Variance Scan + Dashboard Review",     "Engagement Manager", "INT-TBV-02 / INT-TBV-03",     "60 min"],
        ["Bi-weekly",     "Sponsor Sync",                         "Engagement Manager", "INT-TBV-04",                  "45 min"],
        ["Bi-weekly",     "Customization Council (as needed)",    "Practice Lead",      "INT-TBV-05",                  "30–60 min"],
        ["End-of-sprint", "Sprint Demo Discipline Audit",         "Solution Architect", "INT-TBV-06",                  "30 min"],
        ["Monthly",       "Practice Management Review",           "Practice Lead",      "INT-TBV-07",                  "90 min"],
        ["Quarterly",     "Practice Retro + Collateral Refresh",  "Practice Lead",      "INT-LL-04 (Lessons-Learned)", "Half-day"],
    ],
    col_widths_in=[1.2, 2.6, 1.6, 2.0, 1.0],
)
d.h2("Weekly — Variance Scan + Dashboard Review")
d.para(
    "Every Friday morning the Engagement Manager opens the Engagement Health Dashboard (INT-TBV-02) and the "
    "Customization Variance Tracker (INT-TBV-03). The scan answers three questions: which vector moved this week, "
    "what was the trigger, and does the trigger require a Customization Council. If the answer to the third question "
    "is yes, the EM creates the Council pre-read by Monday using INT-TBV-05."
)
d.para(
    "The weekly variance scan is the single highest-leverage management activity in the practice. An hour invested "
    "weekly prevents the cumulative drift that becomes a six-figure rework problem at go-live."
)
d.h2("Bi-weekly — Sponsor Sync")
d.para(
    "The Sponsor Sync is the customer-facing half of Trust-But-Verify. It surfaces three things: (1) what changed in "
    "the build since last sync, (2) what decisions are coming up that the sponsor needs to weigh in on, and (3) any "
    "early signals of 'but our old system did X' from the customer team. The agenda template (INT-TBV-04) is the "
    "discipline; running a 'casual catch-up' instead is the most common failure pattern."
)
d.h2("Bi-weekly (as needed) — Customization Council")
d.para(
    "The Council is the formal two-key decision body for any deviation from OOTB. It convenes only when a "
    "Customization Variance ticket has been raised through the deviation lifecycle and is ready for decision. "
    "Section 6 details composition, authority, and pre-read discipline."
)
d.h2("End-of-sprint — Sprint Demo Discipline Audit")
d.para(
    "Within 24 hours after each sprint demo, the Solution Architect completes the audit (INT-TBV-06). The audit "
    "answers: did the demo show OOTB-aligned configuration; did the demo language match the discipline (no 'we just '); "
    "did any customization slip through unannounced. Section 7 details the audit's structure."
)
d.h2("Monthly — Practice Management Review")
d.para(
    "The Practice Lead rolls up the dashboards across all active engagements and runs the cross-engagement review. "
    "This is where pattern-spotting happens: the same drift in three engagements at sprint 3 is not three problems, "
    "it is one collateral gap. Section 8 details the review."
)
d.h2("Quarterly — Practice Retro + Collateral Refresh")
d.para(
    "The retro feeds the practice's collateral library. Lessons-learned (INT-LL-01) become updates to the "
    "Adopt-vs-Re-engineer cheatsheets, the Discipline How-To Guides, and where appropriate, the sales objection "
    "handling pack. The Master Blueprint catalog is updated to reflect newly-built or revised artifacts."
)

d.page_break()

# ---------- 3. HEALTH SIGNALS ----------
d.h1("The Engagement Health Signals")
d.h2("Leading vs lagging indicators")
d.para(
    "Most engagement reporting is lagging — schedule variance, defect counts, sponsor satisfaction surveys. By the "
    "time those signals turn red, the rework window has closed. Trust-But-Verify is anchored in leading indicators: "
    "the configuration objects being built this sprint, the language being used in workshops, the variance against the "
    "SOW baseline. Leading indicators are noisier but actionable. The dashboard (INT-TBV-02) presents both, weighted "
    "toward leading."
)
d.h2("The Five Health Vectors in detail")
d.h3("Process Adoption")
d.para(
    "Measures whether configured processes route through OOTB tables, states, and workflows. Yellow signals: a custom "
    "state on Incident, a custom UI policy on Change, a custom approval on Catalog item. Red signals: a custom table, a "
    "custom workflow that mirrors an OOTB workflow, a custom routing engine in place of Assignment Rules. The audit "
    "evidence is the configuration export plus the sprint demo."
)
d.h3("Configuration Hygiene")
d.para(
    "Measures whether the configured object counts and patterns are within OOTB-defensible bounds. Examples of yellow: "
    "more than 200 catalog items pre-rationalization, more than 30 categories at any level, assignment rules that "
    "reference more than three conditions per rule, SLAs that span more than two distinct schedules. Red: catalog "
    "exceeding 500 items at sprint 3 with no rationalization plan; categories nesting four-plus levels deep; SLAs "
    "still using the old system's 24-7 default for an 8-5 customer."
)
d.h3("Customization Variance")
d.para(
    "Measures the count and aggregate effort of customizations raised, decided, and built relative to the SOW baseline. "
    "Variance bands are detailed in Section 4. The Variance Tracker (INT-TBV-03) is the system of record."
)
d.h3("Adoption Readiness")
d.para(
    "Measures whether the customer team is preparing to operate the OOTB-aligned model. Yellow signals: customer "
    "process owners drafting SOPs that reference custom workarounds; UAT scenarios written against custom paths; "
    "training material describing the old system's flow with screenshots from the new. Red: customer leadership "
    "talking openly about 'after go-live we will customize X.'"
)
d.h3("Sentiment & Trust")
d.para(
    "Measures sponsor and SME alignment with the OOTB-first principle. Tracked qualitatively in the Sponsor Sync "
    "notes (INT-TBV-04). Yellow: sponsor stops asking 'why OOTB' and starts asking 'why not custom.' Red: sponsor or "
    "SME bypassing the consultant to lobby ECS leadership for a customization."
)
d.h2("Yellow / Red threshold reference")
d.table(
    headers=["Vector", "Yellow threshold", "Red threshold"],
    rows=[
        ["Process Adoption",       "1 custom UI policy or 1 custom client script in the sprint",         "Any custom table, workflow, or routing engine"],
        ["Configuration Hygiene",  "Any object class >120% of OOTB-defensible count at sprint 3",         "Any class >150% at sprint 4 with no rationalization plan"],
        ["Customization Variance", "Aggregate Council-approved customizations >5% of sprint capacity",   ">10% of sprint capacity OR an unannounced build"],
        ["Adoption Readiness",     "Customer SOP draft references a workaround",                          "Customer leadership planning post-go-live customization"],
        ["Sentiment & Trust",      "Sponsor questioning OOTB rationale repeatedly in a single sync",     "Sponsor or SME escalating around the consultant"],
    ],
    col_widths_in=[1.7, 3.4, 3.3],
)
d.h2("Where each signal lives")
d.para(
    "All five vectors roll up in INT-TBV-02 (Engagement Health Dashboard). The dashboard is a single Excel workbook "
    "with one tab per vector and a roll-up tab the Practice Lead reviews monthly. Engagement Managers update weekly. "
    "The Variance Tracker (INT-TBV-03) feeds the Customization Variance vector directly via cell references."
)

d.page_break()

# ---------- 4. CUSTOMIZATION VARIANCE ----------
d.h1("Customization Variance — The Master Signal")
d.h2("What variance is")
d.para(
    "Customization Variance is the cumulative count and effort of customizations the engagement has committed to "
    "build, expressed relative to the SOW baseline. The SOW baseline is zero customizations beyond the OOTB-first "
    "scope; every Council-approved customization adds to variance. Rejected requests do not add. Customizations "
    "discovered after the fact (i.e., built without going through the Council) add and trigger a separate "
    "course-correction (Section 9)."
)
d.h2("How to track it")
d.para(
    "The Variance Tracker (INT-TBV-03) is a single workbook with one row per customization request. Required columns: "
    "request ID, sprint raised, requester, OOTB alternative analysis link, Council decision, decision date, sprint "
    "approved-for-build, estimated effort (hours), actual effort, post-go-live owner. The variance dashboard "
    "calculates aggregate effort against sprint capacity in real time."
)
d.h2("Variance bands and intervention triggers")
d.table(
    headers=["Band", "Aggregate variance", "Intervention"],
    rows=[
        ["Green",  "0–5% of total sprint capacity",  "No intervention. Continue weekly scan."],
        ["Yellow", "5–10% of capacity",              "EM raises in next bi-weekly Sponsor Sync. Add to Practice Lead monthly review."],
        ["Orange", "10–15% of capacity",             "Practice Lead joins next Sponsor Sync. Customization Council reviews backlog."],
        ["Red",    ">15% of capacity OR unannounced build detected", "Course-correction protocol invoked (Section 9). Possible PCR."],
    ],
    col_widths_in=[1.0, 3.0, 4.4],
)
d.h2("Reading variance over the 18-week arc")
d.para(
    "Variance is not flat across the 18 weeks. Some sprints structurally generate more legitimate customization pressure "
    "(Sprint 2 Catalog and Sprint 4 CMDB are the perennial peaks). The dashboard plots variance week-over-week against "
    "the practice's reference curve so the EM can distinguish a normal sprint-2 spike from genuine drift. The reference "
    "curve is recalibrated at the quarterly retro using actuals across all engagements."
)

d.page_break()

# ---------- 5. SPONSOR SYNC ----------
d.h1("The Bi-Weekly Sponsor Sync")
d.h2("Why bi-weekly")
d.para(
    "Weekly is too frequent for a sponsor — they tune out and stop reading the pre-read. Monthly is too infrequent — "
    "drift becomes visible only after it is committed. Bi-weekly is the sweet spot: long enough to have substance, "
    "short enough that any signal of 'but our old system did X' surfaces while it is still a question rather than a "
    "demand."
)
d.h2("Standard agenda")
d.para("The 45-minute agenda (template: INT-TBV-04) is structured as:")
d.bullet("Build progress since last sync — 10 min, EM-led, walk the dashboard at vector level")
d.bullet("Decisions coming this sprint — 10 min, EM-led, frame the two-key decisions the sponsor will weigh in on")
d.bullet("Customization Council update — 10 min, EM-led, what was raised, what was decided, what is pending")
d.bullet("Sponsor's open items — 10 min, sponsor-led, surface any concerns from their organization")
d.bullet("Action recap and next steps — 5 min, EM-led, document in the sync notes")
d.h2("The three things you must surface every sync")
d.para(
    "Regardless of agenda, the EM ensures three items surface in every Sponsor Sync. Skipping any of them is the most "
    "common reason drift becomes visible only after it is committed."
)
d.bullet("Any vector currently in yellow or red, with the EM's planned response.")
d.bullet("Any customization request raised in the last two weeks, even if pre-Council, framed by OOTB alternative.")
d.bullet("Any signal from the customer team that suggests 'but our old system did X' is forming as a position.")
d.h2("Anti-patterns to avoid")
d.para(
    "The Sponsor Sync degrades into ineffectiveness in three predictable ways. First, the 'casual catch-up' — the "
    "EM runs the meeting without the agenda template, the dashboard is not opened, and the meeting becomes status "
    "theater. Second, the 'good news only' sync — the EM reports green vectors and omits yellow ones to avoid a "
    "difficult conversation. Third, the 'absorb the ask' sync — the sponsor floats a customization, the EM "
    "verbally agrees in the meeting without routing through the Council. All three patterns convert the sync from a "
    "drift-detection mechanism into a drift-amplification mechanism."
)

d.page_break()

# ---------- 6. CUSTOMIZATION COUNCIL ----------
d.h1("The Customization Council")
d.h2("Composition and authority")
d.para(
    "The Council is the two-key decision body defined in the ECS Internal Governance Operating Guide. Two keys are "
    "required for any customization commitment: the customer sponsor signs the business-need key; the ECS Practice "
    "Lead signs the technical-path key. Either key alone is insufficient. The EM facilitates; the Solution Architect "
    "presents the OOTB Alternative Analysis; the Process Consultant presents the Adoption Impact."
)
d.h2("When to convene")
d.para(
    "The Council convenes only when a customization request has completed the deviation lifecycle through Stage 4 "
    "(Recommend) per the Governance Guide. Stages 1 through 4 are documentation discipline; the Council is decision "
    "discipline. Convening prematurely wastes the Council; convening too late lets the team start building before the "
    "decision is final."
)
d.h2("Pre-read discipline")
d.para(
    "Every Council meeting requires a pre-read circulated 48 hours in advance using the Council Pre-Read Template "
    "(INT-TBV-05). The pre-read includes: the Customization Request, the OOTB Alternative Analysis, the Business "
    "Outcome Alignment, the Contract Risk Assessment, and the Solution Architect's recommendation. Sponsors who arrive "
    "without having read the pre-read are rescheduled — the Council does not double as the reading session."
)
d.h2("Decision routing")
d.para(
    "Council decisions route in one of four directions. Approved-for-sprint customizations enter the sprint backlog "
    "and are added to the Variance Tracker. Approved-for-product-backlog customizations are deferred for post-go-live "
    "consideration. Rejected customizations are documented in the Triage Log with reasoning so the same request does "
    "not recur. PCR-triggered customizations route to a contract change request before any build commitment."
)

d.page_break()

# ---------- 7. DEMO DISCIPLINE AUDIT ----------
d.h1("Sprint Demo Discipline Audit")
d.h2("Why demos are the truth")
d.para(
    "The sprint demo is where stated discipline meets actual configuration. A team that has been silently drifting "
    "cannot hide it during the demo — the configured artifacts speak for themselves. The Demo Discipline Audit "
    "(INT-TBV-06) is the mechanism for capturing what the demo revealed and converting it into management action."
)
d.h2("What to look for")
d.para(
    "The audit asks the Solution Architect to score each demo against six items. Three are configuration items: "
    "are the demonstrated processes running through OOTB tables and states; are the demonstrated catalog and category "
    "structures within hygiene bounds; are the demonstrated workflows OOTB or pre-Council-approved. Three are language "
    "items: did the consultant defend OOTB when challenged; did the consultant frame customization requests through the "
    "deviation lifecycle; did the consultant avoid 'we just' minimization language. The score feeds the dashboard."
)
d.h2("Coaching the team after the demo")
d.para(
    "Audit findings that are not coaching opportunities are wasted findings. Within 48 hours of the demo, the EM and "
    "Solution Architect debrief the team using the Coaching Conversation Templates (INT-TBV-09). The debrief is "
    "operational — what the team observed, what the team will do differently next sprint — not punitive. Drift is a "
    "discipline gap, not a performance failure; treating it as the latter accelerates it."
)

d.page_break()

# ---------- 8. PRACTICE MGMT REVIEW ----------
d.h1("The Practice Management Monthly Review")
d.h2("Cross-engagement view")
d.para(
    "Once a month the Practice Lead reviews the rolled-up dashboards across all active engagements. The roll-up tab in "
    "INT-TBV-02 presents one row per engagement and one column per vector. The view answers a single question: where "
    "is the practice as a whole, not where is any one engagement."
)
d.h2("The Practice Health Tile")
d.para(
    "The Practice Lead synthesizes the cross-engagement view into a one-page Practice Health Tile (INT-TBV-07). The "
    "Tile is the artifact the Practice Lead presents to ECS leadership monthly. It surfaces (1) the count of "
    "engagements at each variance band, (2) any engagement that moved bands in the last month, (3) any pattern "
    "appearing in two or more engagements, and (4) the planned course-correction or collateral response."
)
d.h2("Pattern-spotting questions")
d.para(
    "The cross-engagement view exists to surface patterns the single-engagement view cannot. The Practice Lead asks "
    "the same five pattern-spotting questions every month. The same yellow vector in three engagements at the same "
    "sprint number — is this a coincidence, a discipline gap in the team, a missing piece of collateral, a customer "
    "industry pattern, or a ServiceNow product-side change. The answer routes to one of four responses: coaching, "
    "collateral build, sales positioning update, or product-feedback escalation to ServiceNow."
)
d.h2("What gets escalated")
d.para(
    "Three classes of finding escalate from the monthly review to ECS leadership: any engagement that crossed into "
    "the red band; any pattern appearing in three or more engagements; any sponsor-relationship signal that suggests "
    "renewal or expansion is at risk. Escalation is not an alarm — it is an early-warning so leadership can offer "
    "support, deploy a senior consultant, or open a sponsor-to-sponsor conversation."
)

d.page_break()

# ---------- 9. COURSE-CORRECTION ----------
d.h1("Course-Correction Playbook")
d.h2("The four classes of course-correction")
d.para(
    "When an engagement crosses into the orange or red band, the EM invokes one of four course-correction classes. "
    "The class is determined by what triggered the crossing, not by how bad the dashboard looks."
)
d.table(
    headers=["Class", "Trigger", "Action", "Owner"],
    rows=[
        ["Discipline Reset",       "Drift accumulating from missed cadence events",                "Re-anchor team on cadence; restart variance scan; coaching debrief.",       "EM"],
        ["Council Realignment",    "Customizations approved that should not have been",            "Re-Council the recent decisions; re-classify; rebuild OOTB Alternative.",   "Practice Lead"],
        ["Scope Reset (PCR)",      "Customer-driven scope expansion exceeds SOW envelope",         "Pause sprint; PCR drafted; sponsor-to-sponsor conversation.",                "Practice Lead + Sales"],
        ["Sponsor Realignment",    "Sponsor disengaged or shifted away from OOTB-first",           "Direct sponsor-to-Practice-Lead conversation; reset on principle.",         "Practice Lead"],
    ],
    col_widths_in=[1.7, 2.8, 3.0, 1.0],
)
d.h2("Decision tree")
d.para(
    "The Course-Correction Playbook (INT-TBV-08) provides the decision tree that maps trigger to class. The EM uses "
    "the tree at the moment a band-crossing is detected — usually the same week — and selects one class. Multiple "
    "classes simultaneously means the engagement is in genuine trouble; in that case the Practice Lead takes ownership "
    "of all four course-corrections in parallel."
)
d.h2("Communication templates")
d.para(
    "Each class has a paired communication template: an internal team brief, a sponsor talking-points sheet, and (where "
    "applicable) an ECS-leadership status update. The templates are in INT-TBV-08. Using them is non-optional — the most "
    "common course-correction failure is the EM ad-libbing the sponsor conversation and accidentally conceding more "
    "than the playbook allows."
)
d.h2("When to invoke executive escalation")
d.para(
    "Executive escalation — the ECS Practice Director and the customer's CIO — is invoked when (1) a Scope Reset "
    "requires a PCR with material commercial impact, (2) sponsor realignment requires a sponsor-to-sponsor reset, or "
    "(3) the engagement is at risk of failing to achieve the AI License Realization outcomes that anchor the SOW. "
    "Escalation is timely, factual, and forward-looking — what we observed, what we are doing, what we need from "
    "leadership."
)

d.page_break()

# ---------- 10. COACHING ----------
d.h1("Coaching the Consultant")
d.para(
    "Drift is rarely the consultant's fault. It is almost always a discipline gap that the playbook is designed to "
    "close. The four most common discipline gaps each have a paired coaching conversation in INT-TBV-09."
)
d.h2("Pattern: the smart consultant who agrees too quickly")
d.para(
    "Strong technical consultants want to be helpful. When a customer SME says 'we need a custom client script for X,' "
    "the consultant's instinct is to nod and start writing. The discipline gap is the missing pause — the moment to "
    "open the OOTB alternative analysis and walk the customer through it. The coaching conversation is about "
    "rehearsing the pause, not about chastising the customization."
)
d.h2("Pattern: the SME who pulls them off-OOTB")
d.para(
    "Some customer SMEs treat the engagement as a chance to recreate the system they built at their last employer. "
    "The consultant feels caught between the SME's expertise and the OOTB-first principle. The discipline gap is "
    "the missing escalation — the SME's request is a Council item, not a sprint backlog item. Coaching focuses on "
    "the routing language: 'that is exactly the kind of decision the Council was set up for, let me put it on the "
    "agenda.'"
)
d.h2("Pattern: the engagement manager who absorbs scope")
d.para(
    "EMs under sponsor pressure sometimes absorb customization commitments verbally to keep the relationship warm. "
    "The discipline gap is the missing structure — every customization is a two-key decision, and verbal commitment "
    "from the EM is not a key. Coaching focuses on the deflection language: 'I hear you; let me get the OOTB "
    "alternative in front of you before we commit.'"
)
d.h2("Templates")
d.para(
    "INT-TBV-09 contains the conversation templates for all four patterns plus three additional patterns "
    "(Solution Architect overengineering, Process Consultant losing the workshop, and the customer's developer "
    "auditioning to be the post-go-live admin). Each template is a one-page operational script the EM can run with "
    "the team member directly."
)

d.page_break()

# ---------- 11. COMPANION INDEX ----------
d.h1("Companion Artifact Index — Trust-But-Verify Pack")
d.para(
    "This playbook is the master document for the Trust-But-Verify pack. The eight companion artifacts below operationalize "
    "what this playbook describes. Build status reflects the practice's current collateral library at the time of this "
    "release; refer to the Master Blueprint catalog for live status."
)
d.table(
    headers=["ID", "Artifact", "Format", "Cadence", "Owner"],
    rows=[
        ["INT-TBV-02", "Engagement Health Dashboard (template)",        "xlsx", "Weekly",          "EM"],
        ["INT-TBV-03", "Customization Variance Tracker",                "xlsx", "Weekly",          "EM"],
        ["INT-TBV-04", "Bi-Weekly Sponsor Sync Agenda Template",        "docx", "Bi-weekly",       "EM"],
        ["INT-TBV-05", "Customization Council Pre-Read Template",       "docx", "As needed",       "Solution Architect"],
        ["INT-TBV-06", "Sprint Demo Discipline Audit",                  "docx", "End-of-sprint",   "Solution Architect"],
        ["INT-TBV-07", "Practice Management Monthly Review Template",   "docx", "Monthly",         "Practice Lead"],
        ["INT-TBV-08", "Engagement Course-Correction Playbook",         "docx", "On invocation",   "EM / Practice Lead"],
        ["INT-TBV-09", "Consultant Coaching Conversation Templates",    "docx", "On observation",  "EM"],
    ],
    col_widths_in=[1.0, 3.4, 0.7, 1.5, 1.6],
)

# ---------- 12. CROSS-REFS ----------
d.h1("Cross-References to the Practice Library")
d.para(
    "Trust-But-Verify is a discipline embedded in the broader ECS practice library. The artifacts below are the "
    "essential cross-references; consultants and managers should read each in service of this playbook."
)
d.bullet("ECS Internal Governance Operating Guide — defines the deviation lifecycle, two-key decision, and Council mechanics this playbook operates against.")
d.bullet("Consultant Handbook (INT-CH-01) — master playbook for the practice; includes the OOTB-Defense Discipline this playbook complements.")
d.bullet("ECS OOTB Delivery Playbook — the engagement-spine playbook; this playbook adds the management vigilance layer.")
d.bullet("ECS Accelerator Pack Blueprint — defines the workbook architecture that anchors each sprint's OOTB-aligned configuration evidence.")
d.bullet("Adopt-vs-Re-engineer Cheatsheets (INT-AR-01 through INT-AR-16) — discipline-specific OOTB defense the consultant uses in the workshop; this playbook is what the manager uses when the cheatsheet was not deployed in time.")
d.bullet("Sales Objection Handling — Top 20 (INT-SP-06) — the sales-side companion; many drift triggers begin in the sales conversation.")
d.bullet("Engagement Lessons-Learned (INT-LL-01) — the quarterly retro feeds updates back to this playbook.")

d.callout(
    "This playbook is reviewed at every quarterly practice retro and updated based on lessons learned across all "
    "active engagements. Send updates and field experience to the Practice Lead. The discipline only gets sharper "
    "if the practice keeps writing it down."
)

d.save(OUT)
print(f"Saved: {OUT}")
