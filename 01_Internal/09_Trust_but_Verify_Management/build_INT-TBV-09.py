"""
Build INT-TBV-09 — Consultant Coaching Conversation Templates
Seven one-page operational scripts for the Engagement Manager to run with team members.
Patterns: (A) Smart consultant who agrees too quickly, (B) SME who pulls off-OOTB,
(C) EM who absorbs scope, (D) SA who overengineers, (E) Process Consultant losing the workshop,
(F) Customer developer auditioning, (G) Consultant who avoids the Council.
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

OUT = os.path.join(HERE, "INT-TBV-09_Consultant_Coaching_Conversation_Templates.docx")

d = EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL TEMPLATE · TRUST-BUT-VERIFY DISCIPLINE",
    title="Consultant Coaching\nConversation Templates",
    subtitle="Seven operational scripts for the EM — because drift is a discipline gap, not a performance failure",
    audience="Engagement Manager (leads conversation) · Practice Lead (coaches the EM on use)",
    companion_to="INT-TBV-01 (Manager Playbook) · INT-TBV-06 (Demo Audit) · INT-TBV-08 (Course-Correction Playbook)",
    doc_id="INT-TBV-09",
    version="1.0",
    status="Released",
    running_header_label="Internal · Consultant Coaching Conversation Templates",
))

d.add_cover_page()

d.para(
    "Drift is rarely the consultant's fault. It is almost always a discipline gap that this playbook is "
    "designed to close. The seven conversation templates below give the Engagement Manager operational "
    "language for the most common patterns of drift. Each template is a script, not a suggestion — "
    "use it as written until you have enough experience to adapt it. Improvising these conversations "
    "before you know them well is the most common way they go wrong."
)

d.h1("How to Use These Templates", numbered=False)
d.para(
    "Each template is triggered by a specific observation — usually from the Demo Discipline Audit (INT-TBV-06) "
    "or from the weekly variance scan. The observation triggers the conversation; the template scripts the conversation. "
    "Conversations happen within 48 hours of the observation — not at the next sprint review, not at the retro. "
    "Drift compounds. A coaching conversation on Tuesday prevents a Council meeting on Thursday."
)
d.bullet("Duration: 20–30 minutes. Private, one-on-one. Not in the daily standup, not in Slack.")
d.bullet("Tone: operational, collegial, forward-looking. 'Here is what I observed and here is what I need us to do differently.' Not corrective, not HR-adjacent.")
d.bullet("Record: EM notes the conversation in the engagement record (one line: date, pattern, outcome). Does not go in the consultant's performance file.")
d.callout(
    "If a pattern recurs after two coaching conversations, it is no longer a discipline gap — it is a "
    "role fit question. Route to the Practice Lead at that point, not to a third conversation using this template."
)

d.table(
    headers=["#", "Pattern Name", "Triggered By", "Primary Coaching Point"],
    rows=[
        ["A", "The Smart Consultant Who Agrees Too Quickly", "Customer SME says 'we need X custom.' Consultant nods and starts designing.", "Rehearse the pause — open the OOTB alternative before designing."],
        ["B", "The SME Who Pulls Them Off-OOTB", "Customer SME uses deep domain expertise to override OOTB approach in workshop.", "The routing language — every SME request is a Council item, not a design decision."],
        ["C", "The EM Who Absorbs Scope", "EM verbally commits to a customization in the Sponsor Sync without Council.", "The deflection language — 'let me get the OOTB alternative in front of you first.'"],
        ["D", "The SA Who Overengineers", "SA proposes a technical solution beyond what the customer asked for — technically elegant, OOTB-violating.", "The 'minimum OOTB viable solution' principle — the job is to close the gap, not to architect the ideal."],
        ["E", "The Process Consultant Losing the Workshop", "Customer attendees redirect the workshop into a legacy-system requirements session.", "Workshop authority and agenda discipline — the PC owns the room."],
        ["F", "The Customer Developer Auditioning", "Customer's developer attends a demo or workshop and starts proposing code-based solutions.", "Audience management — the developer is not a build partner, they are a stakeholder."],
        ["G", "The Consultant Who Avoids the Council", "A build artifact is demonstrated that is not in the Variance Tracker and was not Council-approved.", "The Council is not optional — it is the protection, not the obstacle."],
    ],
    col_widths_in=[0.4, 2.4, 2.4, 3.2],
)

d.page_break()

# ── PATTERN A ─────────────────────────────────────────────────────────────────
d.h1("Pattern A — The Smart Consultant Who Agrees Too Quickly")
d.h2("What you observed")
d.para(
    "A technically strong consultant, in a customer workshop or demo, heard a customer SME say 'we need X' and "
    "moved directly into design mode — asking clarifying questions about X, sketching the approach, or saying "
    "'we could probably do that with a client script.' The missing element is the pause: the moment to open the "
    "OOTB alternative analysis before designing anything."
)
d.h2("Why it happens")
d.para(
    "Strong consultants want to solve problems. When they hear a customer need, the instinct is to help — to "
    "show competence by designing fast. The OOTB-first discipline requires a counter-intuitive pause: before "
    "designing, look for the existing solution. Consultants who have not internalized this pause under pressure "
    "will drift in every workshop, even without realizing it."
)
d.h2("Conversation script")
d.bullet("Opening: 'I want to talk through something I observed in [the workshop / the demo] yesterday. When [customer name] asked about [the request], I noticed you moved straight into design mode. I want to make sure we are running the OOTB alternative check before we get there.'")
d.bullet("Establish the principle: 'The reason we do that is not to slow down — it is to protect you. If you design something and then we tell the customer the OOTB way does it, that is a harder conversation than if we show them the OOTB way first. The pause is the customer's friend, not a delay.'")
d.bullet("Rehearse the language: 'Here is what the pause sounds like in the room: When [customer name] says that, you say: \"That is an important need — let me show you how ServiceNow handles that OOTB and we can see if it meets what you are describing.\" Then you pull up the OOTB demo. Do you want to try that now?'")
d.bullet("Set the expectation: 'Next time you hear that kind of request in a workshop, I need the OOTB alternative check to be your first move. If the OOTB way genuinely does not cover it, we surface it to the Council. That is the discipline. Can I count on that from you?'")
d.h2("Follow-up")
d.para("Observe the next workshop or demo. If the pattern recurs, run the conversation once more with the Practice Lead present. Third occurrence: route to Practice Lead as role-fit question.")

d.page_break()

# ── PATTERN B ─────────────────────────────────────────────────────────────────
d.h1("Pattern B — The SME Who Pulls Them Off-OOTB")
d.h2("What you observed")
d.para(
    "A customer Subject Matter Expert — typically someone with deep domain expertise or prior ServiceNow "
    "experience at another organization — used their authority in a workshop to steer the conversation "
    "toward a non-OOTB approach. The consultant felt caught between respecting the SME's expertise and "
    "holding the OOTB-first discipline. The SME's request ended up as an implied design commitment "
    "without going through the Council."
)
d.h2("Why it happens")
d.para(
    "Customer SMEs often have genuine expertise and are genuinely trying to help. They have seen a 'better' "
    "way at a previous organization and they are sharing it. The consultant's instinct is to respect that "
    "expertise. The discipline gap is the missing routing language: the SME's idea is valuable input into "
    "the Council, not a design directive. The consultant needs to receive the idea warmly without treating "
    "it as a build commitment."
)
d.h2("Conversation script")
d.bullet("Opening: 'I want to talk about how we handle it when [SME name] steers us toward a custom approach in the workshop. I noticed in [session] that their suggestion about [the request] ended up feeling like a direction — and I want us to make sure it goes through the Council before anything like that becomes a commitment.'")
d.bullet("Validate the consultant's position: 'I know that situation is uncomfortable. [SME name] knows a lot and you want to respect that. That is exactly right — respect their input, and route it correctly. Those are not in conflict.'")
d.bullet("Give them the language: 'When [SME name] says \"at my last organization we built it this way,\" your response is: \"That is a great data point — that approach is worth evaluating formally. Let me get it into the Council process so we can do a proper OOTB alternative comparison and bring it back to you with a recommendation.\" That sentence does three things: it validates the SME, it takes the idea seriously, and it routes it correctly. Practice it.'")
d.bullet("Set the expectation: 'From now on, any time an SME suggests something that sounds custom, I need you to say something like that — not \"sure, we can do that\" and not \"no, we have to use OOTB.\" Receive it, route it. Can you do that?'")
d.h2("Follow-up")
d.para("Ask the SA to flag if they observe the pattern again during a workshop observation. Brief the SA on the routing language so they can reinforce it in the room.")

d.page_break()

# ── PATTERN C ─────────────────────────────────────────────────────────────────
d.h1("Pattern C — The EM Who Absorbs Scope")
d.h2("What you observed (self-coaching version)")
d.para(
    "This pattern applies to the Engagement Manager, and it is the hardest one to coach because the EM must "
    "coach themselves. The scenario: during a Sponsor Sync, the sponsor floated a customization request. "
    "The EM, under pressure to keep the relationship warm and the meeting moving, verbally agreed — or "
    "said something close enough to agreement that the sponsor left the meeting believing it was committed. "
    "The two-key sign-off did not happen."
)
d.h2("Why it happens")
d.para(
    "Verbal agreement in a sponsor sync is the path of least resistance. The EM feels the sponsor's frustration, "
    "wants to solve the problem, and says 'yes' or 'we'll figure it out' or 'I think we can accommodate that.' "
    "Each of those phrases converts the sync from a discipline mechanism into a scope-expansion mechanism. "
    "The discipline gap is the missing deflection language — a phrase that receives the ask without committing to it."
)
d.h2("The deflection language")
d.para("Memorize these phrases. They are not stalling — they are discipline. Practice them until they come out automatically.")
d.bullet("'That is exactly the kind of thing the Council process was built for. Let me get the OOTB alternative in front of you before we make any commitment.'")
d.bullet("'I hear you — this is important to your team. The right way to honor that is to give it a proper analysis. I will have something for you by [date].'")
d.bullet("'I do not want to say yes to something and then come back with a different answer later. Let me run the OOTB check and bring it back to you within [timeframe].'")
d.bullet("'I cannot commit to that in this meeting — that would require a Council decision. What I can commit to is getting you an OOTB alternative analysis within [timeframe].'")
d.h2("What to do if you already absorbed scope")
d.para("If you made a verbal commitment in a past sync that should not have been made:")
d.bullet("Log it in INT-TBV-03 as a Stage 1 request immediately.")
d.bullet("Do not pretend it did not happen and let the team start building. The unlogged commitment is more damaging than the original error.")
d.bullet("At the next Sponsor Sync, use the framing: 'I want to make sure we do this correctly — I mentioned [the request] last time and I want to formally run it through our Council process before we commit. I am doing that to protect you as much as us.'")
d.bullet("Brief the Practice Lead on what happened and what you are doing to correct it.")

d.page_break()

# ── PATTERN D ─────────────────────────────────────────────────────────────────
d.h1("Pattern D — The SA Who Overengineers")
d.h2("What you observed")
d.para(
    "The Solution Architect proposed a technical solution that was more complex than the business need required — "
    "technically elegant, internally consistent, but extending beyond OOTB in ways that were not driven by "
    "the customer's stated need. The SA may have been excited about the problem, trying to future-proof the "
    "solution, or trying to impress the customer with technical depth. The result was a design that created "
    "customization variance without the customer asking for it."
)
d.h2("Conversation script")
d.bullet("Opening: 'I want to talk through the design you proposed for [the solution]. I could see the technical logic and I think the instinct to future-proof is good. I need us to talk about whether the solution you proposed is the minimum OOTB viable solution or something beyond that.'")
d.bullet("Define the standard: 'The standard we use is: what is the minimum OOTB-aligned configuration that closes the customer's stated business gap? Not the ideal architecture, not the most extensible design — the minimum that closes the gap. Anything above that minimum is variance. Does the design you proposed meet that standard?'")
d.bullet("If the SA acknowledges it went beyond: 'Good. What does the minimum look like? Walk me through it. I want to hear you design the smaller version — that is the OOTB discipline muscle.'")
d.bullet("If the SA pushes back: 'I hear you that it is technically better. I need you to separate technically better from OOTB-aligned. Our job is not to deliver technically optimal. Our job is to deliver OOTB-aligned and AI-ready. If there is a genuine gap that requires going beyond minimum, that gap goes through the Council. Walk me through what the genuine gap is.'")
d.h2("Follow-up")
d.para("Ask the SA to re-present the design using the minimum OOTB viable solution framework. Review with them before the next customer session.")

d.page_break()

# ── PATTERN E ─────────────────────────────────────────────────────────────────
d.h1("Pattern E — The Process Consultant Losing the Workshop")
d.h2("What you observed")
d.para(
    "The Process Consultant was running a workshop and lost control of the agenda — customer attendees "
    "redirected the session into a legacy-system requirements gathering exercise, a feature comparison "
    "with their prior system, or an extended debate about why OOTB does not work the way they expected. "
    "The PC did not bring the session back to the workshop objectives. The workshop outcomes are incomplete "
    "or contaminated with unvalidated legacy requirements."
)
d.h2("Conversation script")
d.bullet("Opening: 'I want to debrief the workshop. Walk me through your read on how it went.' [Let them speak. Listen for self-awareness.]")
d.bullet("If they know it went sideways: 'You saw it. Good. Let's talk about what happened at the moment [the redirect] occurred and what you can do differently next time. You own the room — the customer's job is to redirect, your job is to bring it back.'")
d.bullet("If they think it went fine: 'Here is what I observed from my seat. When [describe the moment], the agenda shifted from [workshop objective] to [what it shifted to]. The rest of the session ran in that new direction. The output we needed — [specific deliverable] — did not get completed. That is the gap I want us to close.'")
d.bullet("Give them the language for the redirect: '\"I want to make sure we capture that — let me add it to the parking lot so we do not lose it.\" [Writes it down. Makes it visible. Customer feels heard.] \"Now I want to bring us back to [the workshop objective] because we need [the output] from this session to keep the build on track. Let's pick up where we were.\"'")
d.bullet("Practice it: 'Let's run it. You are facilitating, I am the customer who is about to redirect to [the legacy system]. Stop me. Use the language.'")
d.h2("Follow-up")
d.para("Attend the next workshop as an observer. Brief the PC on what you will be watching for. Debrief within 24 hours.")

d.page_break()

# ── PATTERN F ─────────────────────────────────────────────────────────────────
d.h1("Pattern F — The Customer Developer Auditioning")
d.h2("What you observed")
d.para(
    "The customer has a developer or technical SME who is attending workshops or demos and actively proposing "
    "code-based solutions to business problems — 'we could write a script to do that,' 'I have done this "
    "before, we just need to add a client script.' This person is often skilled and well-intentioned but is "
    "treating the engagement as a collaborative development project rather than a managed OOTB implementation. "
    "The consultant team is treating them as a build partner rather than as a stakeholder."
)
d.h2("Why this is a risk")
d.para(
    "Customer developers who feel empowered to propose solutions create variance through enthusiasm, not malice. "
    "Their proposals normalize customization in the room. Customer SMEs hear 'we could write a script' and "
    "interpret it as ECS agreement. The developer may also be positioning themselves as the post-go-live admin "
    "and trying to shape the build toward something they can maintain — often a more customized system than OOTB."
)
d.h2("Conversation script — with the consultant team")
d.bullet("Opening: 'I want to talk about [customer developer name]'s role in our sessions. They are engaged and technically capable and that is genuinely useful. I want to make sure we are managing how that engagement plays out.'")
d.bullet("Set the frame: 'Their role is stakeholder, not build partner. When they propose a solution in the room, the team's job is to receive it as input, not as direction. The same routing language applies: \"That is worth evaluating — let me get it into the analysis process.\"'")
d.bullet("Address the auditioning risk directly: 'There is sometimes a scenario where a customer developer is trying to shape the build toward something they can maintain post-go-live. That is a legitimate goal, but the way it gets addressed is through the post-go-live architecture conversation, not by having them drive design decisions during the engagement. Keep that boundary clear.'")
d.h2("If the developer has already influenced a design decision")
d.para("Route the decision through INT-TBV-05 (Council Pre-Read) as if it were any other customization request. Do not let it stand un-documented.")

d.page_break()

# ── PATTERN G ─────────────────────────────────────────────────────────────────
d.h1("Pattern G — The Consultant Who Avoids the Council")
d.h2("What you observed")
d.para(
    "A build artifact was demonstrated in a sprint demo — or discovered in a configuration review — that "
    "represents a customization but is not in INT-TBV-03 (Variance Tracker) and was not Council-approved. "
    "This is the Red audit finding in INT-TBV-06 (C-3 score). The consultant built something custom without "
    "surfacing it to the deviation lifecycle. The pattern may be intentional (the consultant knew it was custom "
    "and avoided the process) or inadvertent (the consultant did not recognize it as a customization)."
)
d.h2("Before coaching: determine intent")
d.para("The conversation is different depending on whether the omission was intentional or inadvertent. Assume inadvertent until you have evidence otherwise.")
d.h2("Conversation script — inadvertent omission")
d.bullet("Opening: 'In the demo audit I found [the artifact]. It looks like a customization — [describe why: custom table, client script, etc.]. I do not see it in the Variance Tracker. Walk me through what it is and how it ended up in the build.'")
d.bullet("[Listen. If it was a misclassification — they thought it was configuration, not customization — correct the classification and log it in INT-TBV-03 immediately.]")
d.bullet("Correction: 'Here is why [the artifact] is a customization rather than a configuration: [explain specifically]. Going forward, when you are unsure which side of the line something falls on, the answer is always to ask me before building. If it turns out to be configuration, no harm done. If it turns out to be customization, we just prevented a Council skip.'")
d.bullet("Set the expectation: 'I need you to use me as the classification check before anything that is even possibly a customization goes into the build. Not after — before. Is that clear?'")
d.h2("Conversation script — intentional omission")
d.bullet("Opening: 'I found [the artifact] in the demo. It is a customization. It is not in the Variance Tracker and there is no Council record. I need to understand whether this was a classification error or a decision to skip the Council process.'")
d.bullet("[Listen. If they confirm they knew it was custom and chose not to surface it — this is now a course-correction event, not just a coaching conversation. Invoke INT-TBV-08 Class 1 and brief the Practice Lead within 24 hours.]")
d.bullet("If they confirm it was intentional, name it clearly: 'Skipping the Council is not a judgment call that any individual on the team can make. The Council is the protection mechanism — for the customer, for ECS, and for you. When you skip it, you are the one carrying the liability for that decision. I am not able to let that stand. Here is what we are going to do: [describe the correction per INT-TBV-08].'")
d.callout(
    "An intentional Council skip followed by a second occurrence is a role-fit question, not a coaching "
    "question. Route to the Practice Lead for a direct conversation about continued engagement on the project."
)

d.page_break()

# ── COACHING CONVERSATION LOG ─────────────────────────────────────────────────
d.h1("Coaching Conversation Log", numbered=False)
d.para(
    "The EM maintains one log per engagement. One line per conversation. Not a performance record — an operational record "
    "for tracking whether patterns are resolving or recurring."
)
d.table(
    headers=["Date", "Consultant", "Pattern", "Outcome", "Follow-Up Due", "Recurring?"],
    rows=[
        ["", "", "[A/B/C/D/E/F/G]", "", "", "No"],
        ["", "", "", "", "", "No"],
        ["", "", "", "", "", "No"],
        ["", "", "", "", "", "No"],
        ["", "", "", "", "", "No"],
        ["", "", "", "", "", "No"],
    ],
    col_widths_in=[1.0, 1.6, 1.0, 3.0, 1.4, 0.8],
)
d.para("Recurring = Yes after two conversations: route to Practice Lead.")

d.save(OUT)
print(f"Saved: {OUT}")
