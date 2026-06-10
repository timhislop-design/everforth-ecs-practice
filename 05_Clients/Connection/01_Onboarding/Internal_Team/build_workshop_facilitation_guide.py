# -*- coding: utf-8 -*-
"""Build: Connection - Workshop Facilitation Guide (INTERNAL).
Built via EcsDocument. Internal Use Only footer (default). Grounded in OOTB Delivery Playbook Section 2."""
import sys, os
REPO = "/sessions/eager-epic-davinci/mnt/everforth-ecs-practice"
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta
LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
OUT = os.path.join(REPO, "05_Clients", "Connection", "01_Onboarding", "Internal_Team",
                   "Connection_Workshop_Facilitation_Guide.docx")

doc = EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL - WORKSHOP FACILITATION",
    title="Connection Engagement\nWorkshop Facilitation Guide",
    subtitle="How we run OOTB-first workshops - and end each one with a signed-off story",
    org="ECS Federal - ServiceNow Practice",
    audience="ECS delivery team - Process Consultant (lead), Solution Architect, Engagement Manager",
    companion_to="Team Onboarding & Vision - Engagement Delivery Guidelines - OOTB Delivery Playbook (Sec. 2)",
    doc_id="INT-CONN-WSF-01", version="1.0", status="Draft",
    running_header_label="Internal - Connection Workshop Facilitation",
), logo_path=LOGO)

doc.add_cover_page()
doc.page_break()

doc.h1("How to Use This Guide", numbered=False)
doc.para(
    "Workshops are where the OOTB-first discipline is enforced in practice - the moment a process owner with ten years "
    "of legacy customization either accepts the OOTB pattern or doesn't. Done well, a workshop ends with a signed-off "
    "user story headed straight to the sprint. Done badly, it ends with a list of \"things to think about\" that come "
    "back as customization requests two weeks later. This guide is the pattern that makes the difference. The Process "
    "Consultant leads; the Solution Architect supports on architecture and deviation calls.")
doc.callout("A workshop that doesn't reach its sign-off output didn't end - it got rescheduled. Protect the sign-off.")

doc.h1("The Five-Tier Workshop Framework", numbered=True)
doc.para("Every workshop is one of five tiers. Know which tier you are running and what its sign-off output is before you walk in.")
doc.table(headers=["Tier", "What it covers", "Sign-off output"], rows=[
    ["Accelerator Pack", "Foundation data - users, groups, locations, assignment rules, catalog taxonomy", "Validated workbook ready for build"],
    ["CSDM", "Service taxonomy, design domains, lifecycle, CI relationship standards, class hierarchy", "Signed-off CSDM-aligned data model"],
    ["Reporting", "OOTB Performance Analytics, dashboards, standard reports vs. business objectives", "Confirmed OOTB reports + gaps for backlog"],
    ["Process OOTB Alignment", "End-to-end demo of each in-scope process (Incident, Request, Change...) vs. OOTB", "Signed-off user stories for the process"],
    ["Integration", "Integration patterns, data contracts, OOTB Spoke / IntegrationHub usage", "Documented integration design + data contract"],
])

doc.h1("The Six-Beat Facilitation Pattern", numbered=True)
doc.para("Every workshop runs the same six beats. Routine workshops: 90 minutes. CSDM and Process OOTB Alignment: 120 minutes.")
doc.table(headers=["Beat", "Time", "What happens"], rows=[
    ["1. Pre-work", "1 wk before", "SMEs receive OOTB demo materials + a pre-workshop questionnaire. Decisions are pre-warmed, not introduced cold."],
    ["2. Open", "5 min", "Re-state the OOTB-first frame, the workshop goal, and the named decisions required. Set the expectation: decisions are made in the room."],
    ["3. Demo", "20-30 min", "The platform shows the work first - against real Connection data, never Lorem ipsum."],
    ["4. Decisions", "30-45 min", "Focused conversation on the narrow decision set. Capture live. No \"we'll get back to you\" - if a decision needs more thought, name the owner and the return date."],
    ["5. Sign-off", "10 min", "Explicit sign-off by the named process owner, recorded in workshop notes."],
    ["6. Backlog & PCR", "5 min", "Deferred items captured with rationale; anything that triggered a PCR conversation flagged for the EM."],
])

doc.h1("Decision-Forcing Techniques", numbered=True)
doc.para("Tactical moves that keep a workshop from spiraling into open-ended discussion:")
doc.bullet("Show, don't tell - demo OOTB doing the work; seeing it beats talking about it.")
doc.bullet("Customer data, not Lorem ipsum - \"oh, this is OUR data\" is the moment OOTB starts to feel real.")
doc.bullet("Two options, both OOTB - on pushback, force a choice between Option A and Option B, never OOTB vs custom.")
doc.bullet("What's the business outcome? - redirect a demand for a specific implementation to the outcome it serves.")
doc.bullet("Defer to backlog, don't argue - capture nice-to-haves without an OOTB-vs-custom debate today.")
doc.bullet("Name the customization explicitly - if it genuinely is one, say so and route it to the Council; never build one by accident.")

doc.h1("\"But Our Old Platform Did X\" - Rebuttal Patterns", numbered=True)
doc.para("These conversations happen in every workshop. Redirect without making the SME feel dismissed.")
doc.table(headers=["When they say...", "You respond..."], rows=[
    ["\"Our old workflow had 7 approval steps\"", "\"Let's look at what each step prevented. If OOTB delivers the same control with fewer steps, that's a win. If a specific step prevents something OOTB doesn't, that's a Council candidate - let's walk through them.\""],
    ["\"We've always used custom Script Includes for this\"", "\"Show me what the script does - what's the business behavior? We'll see if Flow Designer or a Decision Table does the same OOTB and saves the maintenance burden. If not, we bring it to the Council.\""],
    ["\"Our users won't accept the new portal\"", "\"Adoption is real. Let's pilot the OOTB Employee Center with a small group and measure feedback before we commit to changing it.\""],
    ["\"We need this or [bad thing] will happen\"", "\"Let's document the bad thing. If it's a material business impact, it goes to the Council. If it's a preference or a workaround, it goes to backlog. Walk me through it.\""],
    ["\"Just make it work like the old system\"", "\"That's the trap we're rebuilding away from - the old system has the debt blocking AI and modern features. Let me show you what OOTB does against the same outcome.\""],
])

doc.h1("Capturing Deviations & Protecting Sign-off", numbered=True)
doc.para(
    "When a requirement genuinely fails the Rule of Three, name it as a customization out loud and route it - do not "
    "absorb it into the build. The Solution Architect drafts the impact assessment; the request goes to the "
    "Customization Council and the two-key decision; every entry is logged in the Governance Triage Log within 24 "
    "hours. Deferred nice-to-haves go to the backlog with rationale. Then close on the sign-off the workshop was "
    "called to produce.")
doc.callout("End-state test: did we leave with the tier's sign-off output and a signed-off story (or a named decision-maker and date)? If not, it isn't done - reschedule and note why.")

doc.save(OUT)
print("Saved:", OUT)
