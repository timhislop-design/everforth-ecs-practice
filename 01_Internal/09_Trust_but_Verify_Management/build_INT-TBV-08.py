"""
Build INT-TBV-08 — Engagement Course-Correction Playbook
Decision tree + four course-correction class playbooks.
Each class has a paired communication template: internal team brief,
sponsor talking-points sheet, and ECS-leadership status update.
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

OUT = os.path.join(HERE, "INT-TBV-08_Engagement_Course-Correction_Playbook.docx")

d = EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL PLAYBOOK · TRUST-BUT-VERIFY DISCIPLINE",
    title="Engagement Course-Correction\nPlaybook",
    subtitle="The decision tree and class playbooks that turn a band-crossing into a recoverable event",
    audience="Engagement Manager · Practice Lead · Solution Architect",
    companion_to="INT-TBV-01 (Manager Playbook) · INT-TBV-02 (Health Dashboard) · INT-TBV-03 (Variance Tracker)",
    doc_id="INT-TBV-08",
    version="1.0",
    status="Released",
    running_header_label="Internal · Engagement Course-Correction Playbook",
))

d.add_cover_page()

d.para(
    "When an engagement crosses into the orange or red variance band — or when a Red audit item is found "
    "in INT-TBV-06 — the Engagement Manager invokes one of four course-correction classes. This playbook "
    "provides the decision tree, the class-level action protocols, and the communication templates. "
    "The most common course-correction failure is the EM ad-libbing the sponsor conversation and accidentally "
    "conceding more than the playbook allows. Using these templates is non-optional."
)

d.h1("How to Use This Playbook", numbered=False)
d.para(
    "Read Section 1 first to determine which course-correction class applies. A single trigger maps to one class. "
    "Multiple simultaneous triggers mean the engagement is in genuine trouble — the Practice Lead takes ownership "
    "of all affected classes in parallel. Then go directly to that class's section for the action protocol "
    "and communication templates. Do not improvise the sequence."
)
d.callout(
    "Course-correction is timely, factual, and forward-looking. Effective course-correction language: "
    "'Here is what we observed, here is what we are doing about it, here is what we need from you.' "
    "Ineffective: 'We have a problem.' Catastrophic: silence."
)

d.page_break()

# ── SECTION 1: DECISION TREE ──────────────────────────────────────────────────
d.h1("Section 1 — Course-Correction Decision Tree")
d.para("Use the trigger column to identify the class. Select the first match.")
d.table(
    headers=["Class", "Trigger Condition", "Primary Owner", "Escalation", "Go to"],
    rows=[
        ["1 — Discipline Reset",
         "Engagement moved to Yellow or Orange band due to missed cadence events (weekly scans missed, variance scan not run, Sponsor Sync running without agenda template)",
         "Engagement Manager",
         "Practice Lead informed within 24 hrs",
         "Section 2"],
        ["2 — Council Realignment",
         "Customizations were approved that should not have been approved (Council not properly convened, two-key sign-off not obtained, or decision documented incorrectly)",
         "Practice Lead",
         "Practice Lead leads — EM executes",
         "Section 3"],
        ["3 — Scope Reset (PCR)",
         "Customer-driven scope expansion exceeds SOW envelope. Band crossed due to PCR-class requests or cumulative variance >15% of total engagement capacity",
         "Practice Lead + Sales Lead",
         "ECS Practice Director briefed within 48 hrs",
         "Section 4"],
        ["4 — Sponsor Realignment",
         "Sponsor disengaged, actively challenging OOTB-first principle, or bypassing the consultant team to lobby ECS leadership directly",
         "Practice Lead",
         "ECS Practice Director — sponsor-to-sponsor conversation",
         "Section 5"],
    ],
    col_widths_in=[1.6, 3.4, 1.6, 1.4, 0.8],
)

d.h2("Multiple simultaneous triggers")
d.para(
    "If two or more triggers are active simultaneously, the engagement is at elevated risk. Protocol: "
    "the Practice Lead takes direct ownership and runs all applicable class protocols in parallel. "
    "The EM does not run multiple course-corrections independently. ECS Practice Director is briefed "
    "within 24 hours when two or more classes are active."
)

d.page_break()

# ── SECTION 2: DISCIPLINE RESET ───────────────────────────────────────────────
d.h1("Section 2 — Class 1: Discipline Reset")
d.h2("When to invoke")
d.para(
    "The engagement drifted because the management cadence was not being run consistently — weekly variance "
    "scans were missed, Sponsor Syncs ran without the agenda template, or the Demo Discipline Audit was not "
    "completed within 24 hours of a sprint demo. The fix is simple and fast: re-anchor the cadence. "
    "This class does not require a sponsor conversation unless the dashboard shows a Yellow band vector."
)

d.h2("Action protocol")
d.table(
    headers=["Step", "Action", "Owner", "Timeline"],
    rows=[
        ["1", "EM identifies which cadence events were missed and reconstructs the gap (what was not caught, what may have drifted undetected)", "EM", "Same day trigger identified"],
        ["2", "EM runs a retroactive variance scan using INT-TBV-03 to identify any unlogged customization requests in the gap period", "EM", "Within 24 hrs"],
        ["3", "EM updates INT-TBV-02 with accurate scores for the gap period. If a vector moves to Yellow or Red retroactively, escalate to Class 2 or 3 as appropriate.", "EM", "Within 24 hrs"],
        ["4", "EM restarts the cadence in writing — sends a cadence-reset note to the SA and Process Consultant naming the dates for the next three events", "EM", "Within 48 hrs"],
        ["5", "Practice Lead briefed with a one-paragraph status: what was missed, what was found, what is now running", "EM → PL", "Within 48 hrs"],
        ["6", "If a Yellow vector was identified in the retroactive scan, invoke Sponsor Sync using INT-TBV-04 within the current sprint", "EM", "Within current sprint"],
    ],
    col_widths_in=[0.5, 4.0, 1.5, 2.4],
)

d.h2("Internal team brief — Class 1 (copy and complete)")
d.callout(
    "Send to: Solution Architect, Process Consultant(s) on the engagement.\n\n"
    "Subject: Engagement Cadence Reset — [Engagement Name] — [Date]\n\n"
    "Team — I am resetting our Trust-But-Verify cadence for [Engagement Name]. We missed [identify events] "
    "between [dates]. I have run a retroactive variance scan and found [summarize findings — 'no unlogged "
    "customizations' or 'the following items need to be logged']. Our next cadence events are: "
    "[Weekly variance scan: date], [Sponsor Sync: date], [Demo Audit: date]. "
    "Please flag anything you have observed in the gap period that did not make it into the Variance Tracker. "
    "— [EM name]"
)

d.page_break()

# ── SECTION 3: COUNCIL REALIGNMENT ───────────────────────────────────────────
d.h1("Section 3 — Class 2: Council Realignment")
d.h2("When to invoke")
d.para(
    "A customization was committed to or built without proper Council process — either the Council was not "
    "convened, the two-key sign-off was not obtained, or the decision was documented incorrectly. "
    "This class is more serious than Class 1 because a build commitment may already exist. The Practice Lead "
    "takes direct ownership."
)

d.h2("Action protocol")
d.table(
    headers=["Step", "Action", "Owner", "Timeline"],
    rows=[
        ["1", "Practice Lead reviews the specific decision(s) that were made incorrectly. Determines what was approved that should not have been.", "Practice Lead", "Within 24 hrs of trigger"],
        ["2", "If the build has not yet started: halt build. If the build is in progress: pause and document current state. If the build is complete: document as variance.", "EM", "Immediately upon PL direction"],
        ["3", "Practice Lead re-convenes the Council for the specific decision(s). New pre-read prepared using INT-TBV-05 reflecting the corrected analysis.", "Practice Lead + SA", "Within 5 business days"],
        ["4", "EM updates INT-TBV-03 with corrected decision records. Retroactively documents the gap.", "EM", "Within 24 hrs of re-Council"],
        ["5", "If the decision reversal changes the sponsor's expectations, EM conducts a Sponsor Sync (INT-TBV-04) to communicate the change. Use talking points below.", "EM", "Within current sprint"],
        ["6", "Practice Lead files a Class 2 record (this completed section) in the engagement's SharePoint.", "Practice Lead", "Within 5 business days"],
    ],
    col_widths_in=[0.5, 4.0, 1.5, 2.4],
)

d.h2("Sponsor talking points — Class 2")
d.para("Use these points in the Sponsor Sync if the Council realignment changes what the sponsor was expecting.")
d.bullet(
    "Opening framing: 'I want to be transparent with you about a process step we are tightening. "
    "We identified that [describe the decision] was made without the full two-key Council process. "
    "We are re-running the Council decision using the correct process.'"
)
d.bullet(
    "If the decision reverses: 'The corrected analysis shows [OOTB alternative]. "
    "This means [outcome for the customer]. We know this is not what was discussed, and I want to "
    "walk you through why the OOTB path is the right one for your AI realization goals.'"
)
d.bullet(
    "If the decision stands: 'The good news is the Council decision stands — [what was approved] is still "
    "moving forward. What changes is how it is formally documented in our variance record.'"
)
d.bullet(
    "Close: 'I am documenting this conversation in our Sponsor Sync record. The Council pre-read and "
    "decision record will be in your SharePoint folder by [date].'"
)

d.page_break()

# ── SECTION 4: SCOPE RESET (PCR) ─────────────────────────────────────────────
d.h1("Section 4 — Class 3: Scope Reset (PCR)")
d.h2("When to invoke")
d.para(
    "Customer-driven scope expansion has exceeded the SOW envelope, or cumulative approved customizations "
    "have pushed variance above 15% of total engagement capacity. A PCR — Project Change Request — "
    "is required before any additional customization build commitment is made. The Practice Lead and "
    "Sales Lead own this class jointly."
)

d.h2("Action protocol")
d.table(
    headers=["Step", "Action", "Owner", "Timeline"],
    rows=[
        ["1", "Practice Lead declares Class 3 and notifies the EM to halt all non-OOTB build activities immediately. No new customization commitments until PCR is signed.", "Practice Lead", "Same day as trigger"],
        ["2", "EM documents the specific requests that are driving the PCR trigger. Builds a scope-delta summary: what was sold, what has been approved, what is now being requested beyond that.", "EM", "Within 24 hrs"],
        ["3", "Practice Lead and Sales Lead review the scope-delta summary and determine PCR scope, pricing, and timeline.", "PL + Sales", "Within 3 business days"],
        ["4", "Practice Lead briefs ECS Practice Director with: what triggered the PCR, current engagement health, commercial impact estimate, and recommended path.", "Practice Lead", "Within 48 hrs of trigger"],
        ["5", "Sales Lead initiates PCR conversation with the customer's commercial contact (not the Sponsor — this is a commercial conversation).", "Sales Lead", "Within 5 business days"],
        ["6", "EM uses the Sponsor talking points below to keep the Sponsor informed without committing to scope.", "EM", "Within current sprint"],
        ["7", "If PCR is declined by the customer: Practice Lead and ECS Practice Director determine engagement options. Options include: continue OOTB-only, reduce scope, or exit discussion.", "PL + Director", "As needed"],
    ],
    col_widths_in=[0.5, 4.0, 1.5, 2.4],
)

d.h2("Sponsor talking points — Class 3")
d.bullet(
    "Opening framing: 'I want to give you early visibility into something before it becomes a larger "
    "conversation. The requests we have received in the last [timeframe] have collectively moved us outside "
    "of the original engagement scope. I want to be straightforward with you rather than let this surface "
    "as a surprise later.'"
)
d.bullet(
    "Frame the PCR as a feature, not a failure: 'This is exactly how a disciplined engagement should work — "
    "we identify the scope delta early, we document it accurately, and we make a conscious decision together "
    "about how to handle it. The alternative — quietly absorbing scope — is what creates problems at go-live.'"
)
d.bullet(
    "What the sponsor should not do: 'I want to make sure we do not make any new commitments until the "
    "commercial conversation has had a chance to happen. If your team raises additional requests in the "
    "next few weeks, please route them to me before any discussion about building them.'"
)
d.bullet(
    "Do not quote commercial numbers to the sponsor — that is the Sales Lead's role. The Sponsor Sync "
    "is about alignment, not negotiation."
)

d.h2("ECS leadership status update — Class 3 (one paragraph)")
d.para("[Practice Lead completes and sends to ECS Practice Director]")
d.para(
    "Engagement: [Name] | Sprint: [Current] | Class 3 Course-Correction invoked: [Date].\n"
    "Trigger: [Describe what triggered the PCR threshold — total variance or specific request]. "
    "Current variance band: [Orange/Red]. "
    "Estimated PCR scope: [Rough estimate in hours and commercial range if known]. "
    "Next action: [Sales Lead initiates commercial conversation by date]. "
    "Engagement health otherwise: [One sentence — sponsor relationship, team morale, build quality]. "
    "Leadership support needed: [Specific ask or 'monitoring only at this stage']."
)

d.page_break()

# ── SECTION 5: SPONSOR REALIGNMENT ────────────────────────────────────────────
d.h1("Section 5 — Class 4: Sponsor Realignment")
d.h2("When to invoke")
d.para(
    "The customer sponsor is disengaged, actively challenging the OOTB-first principle, or has bypassed "
    "the consultant team to lobby ECS leadership directly for a customization. This class is rare but "
    "high-stakes — a misaligned sponsor can unravel three sprints of discipline in a single executive conversation."
)

d.h2("Diagnosing the sponsor's position")
d.para("Before invoking Class 4, the Practice Lead should diagnose which pattern is present — the intervention differs significantly.")
d.table(
    headers=["Pattern", "Signs", "Root Cause (usually)", "Intervention"],
    rows=[
        ["Disengaged sponsor",
         "Sponsor stops attending Syncs, delegates everything to a SME, stops reading pre-reads",
         "The engagement is running smoothly from their view — no visible problems — so they have mentally moved on",
         "Re-engagement conversation: bring them back to the strategic value case (AI realization). Make the Sync shorter and more executive-relevant."],
        ["Challenging sponsor",
         "Sponsor questions OOTB rationale repeatedly, privately or publicly; starts using language like 'the system should work the way we work'",
         "The OOTB approach is creating real friction for their team and they are not seeing the long-term value case clearly",
         "Sponsor-level value case conversation led by Practice Lead. Bring the AI realization outcome story — what they paid for, what the OOTB baseline enables."],
        ["Bypassing sponsor",
         "Sponsor or their proxy contacts ECS leadership directly to request a customization or express dissatisfaction",
         "They do not believe the normal channel will get them what they want — or they are trying to create an end-run around the Council process",
         "Immediate PL → ECS Director briefing. Sponsor-to-sponsor reset. The Director re-closes the channel: 'All engagement decisions go through the EM and Practice Lead.'"],
    ],
    col_widths_in=[1.4, 2.0, 2.0, 3.0],
)

d.h2("Action protocol")
d.table(
    headers=["Step", "Action", "Owner", "Timeline"],
    rows=[
        ["1", "Practice Lead diagnoses the pattern (table above) and selects the intervention.", "Practice Lead", "Within 24 hrs of signal"],
        ["2", "Practice Lead briefs ECS Practice Director: what the sponsor is saying, what pattern it matches, what intervention is planned.", "Practice Lead", "Within 48 hrs"],
        ["3", "Practice Lead conducts the sponsor conversation directly — not through the EM. The EM attends but does not lead.", "Practice Lead", "Within 5 business days"],
        ["4", "Practice Lead documents the conversation outcome and files in the engagement record.", "Practice Lead", "Within 24 hrs of conversation"],
        ["5", "If the sponsor-to-sponsor reset is required (bypassing pattern): ECS Director initiates a call with the customer's executive sponsor. The conversation resets the engagement channel.", "ECS Director", "As needed"],
        ["6", "Following the realignment, the EM schedules an out-of-cycle Sponsor Sync (INT-TBV-04) to re-establish the normal cadence with the realigned sponsor.", "EM", "Within 2 weeks of reset"],
    ],
    col_widths_in=[0.5, 4.0, 1.5, 2.4],
)

d.h2("Practice Lead talking points — sponsor realignment conversation")
d.bullet(
    "Return to the value case: 'Let me remind you of what we came here to do together. The reason we "
    "chose an OOTB-first approach was specifically to make you AI-ready — to give you the clean baseline "
    "that allows Now Assist and Predictive Intelligence to work without rework. Every deviation we make "
    "from that baseline is a step away from what we sold you.'"
)
d.bullet(
    "Name the risk explicitly: 'If we customize [the specific request], we are accepting that [AI feature] "
    "will require rework before it can be deployed. That rework is not in this engagement's scope — it "
    "becomes the next engagement's starting point. I want to make sure you are making that tradeoff "
    "consciously, not accidentally.'"
)
d.bullet(
    "Offer the right path: 'Here is what I can offer you. We take this through the Council process — "
    "ECS and your team both formally assess it. If the business case is strong enough to justify the "
    "deviation, we make the decision with eyes open. If the OOTB alternative covers the need, we "
    "document why and close the ticket. Either way, it is a governed decision, not a gap.'"
)

d.page_break()

# ── SECTION 6: EXECUTIVE ESCALATION ──────────────────────────────────────────
d.h1("Section 6 — Executive Escalation Protocol")
d.para(
    "Executive escalation — the ECS Practice Director and the customer's CIO or equivalent — is invoked "
    "in three specific situations. This is not a general escalation path for difficult conversations; "
    "it is a specific mechanism for situations that require authority above the Practice Lead level."
)
d.table(
    headers=["Situation", "Who Initiates", "Who Is Briefed (ECS)", "Who Is Contacted (Customer)", "Timing"],
    rows=[
        ["Class 3 PCR with material commercial impact (estimated >20% SOW value)", "Practice Lead", "ECS Practice Director + Sales Lead + Legal if required", "Customer commercial contact (not sponsor)", "Within 48 hrs of trigger"],
        ["Class 4 sponsor-to-sponsor reset (bypassing pattern)", "ECS Practice Director", "ECS CEO or equivalent if needed", "Customer's C-suite (CIO, CISO, or equivalent)", "Within 5 business days of trigger"],
        ["Engagement at risk of failing AI Realization outcomes (core SOW commitment)", "Practice Lead", "ECS Practice Director + Sales Lead", "Customer Sponsor + CIO", "Within 48 hrs of determination"],
    ],
    col_widths_in=[2.6, 1.4, 1.8, 1.8, 0.8],
)

d.h2("What executive escalation is not")
d.para(
    "Executive escalation is not a threat, not a last resort, and not an admission of failure. "
    "It is the timely involvement of the right level of authority to protect both ECS and the customer. "
    "The earlier it is invoked, the more options both sides have. Waiting until the engagement is in "
    "crisis before escalating removes all options except damage control."
)
d.callout(
    "The one sentence that prevents most executive escalations: 'Let me get the Council to review this "
    "formally before we make any commitment.' Run the Council process. Escalation is what happens "
    "when the Council process is bypassed and the consequences arrive later."
)

d.save(OUT)
print(f"Saved: {OUT}")
