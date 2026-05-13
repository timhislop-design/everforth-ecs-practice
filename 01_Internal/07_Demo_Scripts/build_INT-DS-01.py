"""
Build INT-DS-01 — Incident Management Demo Script
Internal audience — prescriptive, click-by-click.
Any consultant can deliver a clean OOTB Incident demo without prior rehearsal.
Covers: pre-demo setup, demo narrative + click flow, common Q&A, recovery notes.
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

OUT = os.path.join(HERE, "INT-DS-01_Incident_Management_Demo_Script_INTERNAL.docx")

doc = EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL · DEMO SCRIPT",
    title="Incident Management\nDemo Script",
    subtitle="Click-by-click OOTB demo flow for Incident Management — pre-demo setup, narrative, Q&A, and recovery notes",
    audience="ECS Delivery Consultants, Solution Architects",
    companion_to="INT-FG-01 Sprint 1 Facilitator Guide · Sprint 1 Incident Workbook · CLT-WP-02 Incident Pre-Read",
    doc_id="INT-DS-01",
    version="1.0",
    status="Released",
    running_header_label="Internal · Incident Management Demo Script",
), logo_path=LOGO)

doc.add_cover_page()
doc.page_break()

# =============================================================================
# How to Use This Script
# =============================================================================
doc.h1("How to Use This Script", numbered=False)
doc.para(
    "This script lets any ECS consultant run a clean, compelling OOTB Incident Management demo "
    "without prior rehearsal of this specific instance. The script is written to be followed "
    "verbatim if needed, but the experienced consultant will use it as a guide and adapt the "
    "narrative to the customer's language and situation."
)
doc.para(
    "Read the full script once before the demo. Complete the pre-demo setup checklist before the "
    "meeting starts — do not set up in front of the customer. The demo runs 18-22 minutes with Q&A; "
    "plan for 30 minutes total."
)
doc.callout(
    "Demo discipline rule (from INT-TBV-06): every ServiceNow screen shown in the demo must be "
    "OOTB configuration — no custom fields, no custom workflows, no non-standard navigation. If "
    "a screen has been customized on the demo instance, do not show it. Navigate around it and "
    "note what the OOTB version looks like. Never demo a custom build as if it were OOTB."
)
doc.page_break()

# =============================================================================
# 1. Pre-Demo Setup
# =============================================================================
doc.h1("Pre-Demo Setup")
doc.para(
    "Complete all setup items before the meeting starts. Expect 15 minutes of setup time. "
    "If you are using a shared demo instance, verify the demo data has not been modified since "
    "your last prep session."
)

doc.h2("Instance configuration — verify before every demo")
doc.table(
    headers=["Item", "Expected state", "How to verify"],
    rows=[
        ["Demo incident records", "At least 10 open incidents in various states (New, In Progress, On Hold, Resolved)", "Incident > All Incidents — confirm count and state spread"],
        ["Assignment groups", "At minimum: Service Desk, Desktop Support, Network Operations, Security Operations", "User Administration > Groups — search for each"],
        ["Priority matrix", "P1 through P4 defined with visible response/resolution targets on each incident record", "Open any incident — confirm Priority field has 4 options"],
        ["SLA indicators", "SLA stoplight visible on incident list (green/amber/red indicators)", "Incident list — confirm SLA column shows colored indicators"],
        ["CSDM service map", "At least 5 Business Services with child Technical Services", "Configuration > Services — confirm hierarchy"],
        ["Major Incident flag", "One incident pre-flagged as Major Incident", "Filter incident list for Major Incident = true"],
        ["Knowledge base", "At least 3 published Knowledge Articles linked to incidents", "Self-Service > Knowledge — confirm articles exist and are published"],
    ],
    col_widths_in=[2.2, 3.4, 3.76],
)

doc.h2("Browser and screen setup")
doc.bullet("Open tabs before the meeting: Incident list, one open P1 incident, one resolved incident, Knowledge base homepage, OOTB dashboard (Incident Overview)")
doc.bullet("Set browser zoom to 100%. ServiceNow renders best at full size — zooming in distorts the form layout.")
doc.bullet("Close all non-demo applications. Hide your taskbar or dock. Customers notice cluttered desktops.")
doc.bullet("If screen sharing: use 'Share screen' not 'Share window' — window sharing can clip the ServiceNow header navigation.")
doc.bullet("Confirm your demo account has the ITSM role, not admin — you want to show the user experience, not the admin configuration view.")

doc.h2("Opening framing — say this before starting the demo")
doc.para(
    "Say: 'Before I show you the screens, let me frame what you are about to see. Everything in "
    "this demo is OOTB ServiceNow. No custom code, no custom workflows, no modifications. The "
    "forms, the routing logic, the SLA indicators, the knowledge integration — this is what "
    "ServiceNow ships with. Our job in the workshops is to configure it to your specifics, not "
    "to build something new. What you are about to see is the destination.'"
)
doc.page_break()

# =============================================================================
# 2. Demo Narrative and Click Flow
# =============================================================================
doc.h1("Demo Narrative and Click Flow")
doc.para(
    "The demo tells a single story: a P2 incident comes in, gets routed correctly, gets resolved "
    "with Knowledge Base support, and leaves a clean audit trail. Run the story linearly. Do not "
    "jump around — jumping around makes it look like you are hiding something."
)

doc.h2("Act 1 — The incident dashboard (2 minutes)")
doc.para("Opening line: 'This is the Incident Management dashboard — the first thing your service desk team sees every morning.'")
doc.bullet("Navigate to: Incident > Incident Overview (OOTB PA dashboard)")
doc.bullet("POINT at the 'Open Incidents by Priority' widget. Say: 'Your team sees at a glance how many P1, P2, P3, P4 incidents are open right now. No report to run, no export needed.'")
doc.bullet("POINT at the 'SLA Breach Risk' widget. Say: 'These are the incidents approaching their SLA window — amber is within 25%, red is breached. Your team lead knows exactly where to focus attention.'")
doc.bullet("POINT at the 'Mean Time to Resolve' trend line. Say: 'This trend is your operational health indicator. It updates daily automatically.'")
doc.bullet("Talking point: 'This dashboard is OOTB. Your team will see their own data here within weeks of go-live.'")

doc.h2("Act 2 — Creating a new incident (4 minutes)")
doc.para("Transition: 'Let me show you how an incident comes into the system.'")
doc.bullet("Navigate to: Incident > Create New")
doc.bullet("Fill in the form as you talk. Use real-sounding but fictional data.")
doc.bullet("Caller: Type 'Alex'. Select 'Alex Demo' (Finance dept). Say: 'The caller field pulls from your Active Directory — the user is already in ServiceNow from your AD integration.'")
doc.bullet("Category: Select 'Software'. Sub-category: Select 'Email'. Say: 'Category drives routing. When I set Category to Software / Email, watch what happens to the Assignment Group.'")
doc.bullet("Assignment Group: POINT to the field — it auto-populated to 'Desktop Support'. Say: 'Assignment happened automatically based on category. No one had to read the ticket and route it manually.'")
doc.bullet("Priority: Set Impact to 'Medium', Urgency to 'High'. Say: 'ServiceNow calculates Priority from Impact and Urgency using your priority matrix. This is P2 — High.'")
doc.bullet("POINT to the SLA section at the bottom of the form. Say: 'The SLA clock started the moment I set the priority. Response due in 4 hours, resolution due in 8 hours. The customer does not need to know how to calculate that — ServiceNow does it.'")
doc.bullet("Click Submit. The incident record saves and assigns an INC number.")
doc.bullet("Talking point: 'From submission to routed and tracked took 30 seconds. No email, no spreadsheet, no manual routing.'")

doc.h2("Act 3 — Working the incident (4 minutes)")
doc.para("Transition: 'Now let me show you what the assigned engineer sees when they open this incident.'")
doc.bullet("Open the newly created incident.")
doc.bullet("POINT to the Work Notes field. Say: 'Work notes are internal — the caller never sees them. The engineer uses this to document what they tried.'")
doc.bullet("Type a brief work note: 'Confirmed email client not launching. Checking Exchange connectivity.'")
doc.bullet("Click the Knowledge icon (or navigate to the Related Knowledge section). Say: 'ServiceNow searches the knowledge base automatically based on category and description. Watch this.'")
doc.bullet("SHOW a matching knowledge article appearing. Say: 'There is an article for this exact issue. The engineer does not need to remember the fix — ServiceNow surfaces it.'")
doc.bullet("Click 'Attach to Incident'. Show the article linked to the incident record.")
doc.bullet("Change State to 'In Progress'. POINT to the SLA indicator — it should still show green.")
doc.bullet("Talking point: 'The engineer has the fix in front of them, the SLA clock is visible, and the work is being documented in real time.'")

doc.h2("Act 4 — Resolving and closing (3 minutes)")
doc.para("Transition: 'The engineer applies the fix. Now let me show you resolution.'")
doc.bullet("Change State to 'Resolved'.")
doc.bullet("Resolution Code: Select 'Known Error'. Resolution Notes: Type 'Applied Exchange reconnect procedure from KB article KBA0023.'")
doc.bullet("Click Update. The incident moves to Resolved state. POINT to the resolved timestamp and SLA result — 'Resolved within SLA: Yes'.")
doc.bullet("POINT to the audit trail at the bottom of the record. Say: 'Every state change, every note, every assignment change is timestamped and recorded here. If your auditor asks who touched this ticket and when, this is the answer — automatically generated, no manual logging.'")
doc.bullet("Talking point: 'The caller will receive an automated notification that their issue is resolved. We configure that notification content and timing — OOTB handles the delivery.'")

doc.h2("Act 5 — Major Incident (3 minutes)")
doc.para("Transition: 'Let me show you one more scenario — a Major Incident. This is where ServiceNow really differentiates.'")
doc.bullet("Open the pre-prepared Major Incident record.")
doc.bullet("POINT to the Major Incident flag and the Major Incident Workbench button. Click it.")
doc.bullet("SHOW the Major Incident Workbench: affected services, impacted CIs, communication log, stakeholder notification list.")
doc.bullet("Say: 'When a P1 is flagged as a Major Incident, ServiceNow opens a dedicated workbench. Your incident commander can see affected services from the CSDM, the CIs that are down from the CMDB, and the stakeholder communication log — all in one view.'")
doc.bullet("POINT to the Communications section. Say: 'Stakeholder notifications go out from here — templated, logged, timestamped. No separate email chain. No one wonders who was notified.'")
doc.bullet("Talking point: 'Major Incident management is one of the highest-stakes operational moments your team faces. OOTB ServiceNow handles it without a single custom build.'")

doc.h2("Closing (2 minutes)")
doc.para(
    "Closing line: 'What you just saw — creation, routing, knowledge integration, SLA tracking, "
    "resolution, audit trail, Major Incident workbench — is 100% OOTB ServiceNow. The Sprint 1 "
    "Incident workshops we are about to start are where we take what you just saw and configure it "
    "to your priority matrix, your assignment groups, your categories, and your SLA targets. "
    "The platform does the work. We configure the specifics. Let me pause here — what questions "
    "do you have about what you just saw?'"
)
doc.page_break()

# =============================================================================
# 3. Common Questions and Answers
# =============================================================================
doc.h1("Common Questions and Answers")
doc.para(
    "These are the questions that surface in nearly every Incident demo. Have these answers ready. "
    "The goal is to answer the question and redirect to OOTB capability, not to concede that "
    "customization is needed."
)

doc.table(
    headers=["Question", "Answer"],
    rows=[
        [
            "Can we have more than four priority levels?",
            "You can — OOTB supports as many levels as you define. Our recommendation is four because fewer tiers means faster routing decisions and simpler SLA management. If there is a specific use case that four tiers cannot handle, tell me what it is and we will work through it."
        ],
        [
            "Can we change the form fields — add our own or remove the ones we do not use?",
            "OOTB fields can be hidden, reordered, and relabeled without customization. Adding new fields is a dictionary extension — low-risk but it does count as a modification. Before we add any new fields, let us walk through the 40+ OOTB fields to confirm we actually need something new."
        ],
        [
            "How does a caller submit an incident if they are not in the IT system?",
            "Walk-in, phone, or the Employee Center self-service portal. The demo showed the agent-created path; the Employee Center demo in Sprint 2 will show the self-service path. Both routes create the same incident record with the same routing and SLA logic."
        ],
        [
            "Can incidents automatically escalate after a certain time?",
            "Yes — OOTB SLA escalation engine sends notifications at configurable thresholds (e.g., 50% of SLA window, 75%, at breach). The escalation can notify the engineer, the group manager, or the IT director. We configure that matrix in the Sprint 1 SLA workshop."
        ],
        [
            "What happens to email-submitted incidents? Can we still use email?",
            "Yes. ServiceNow OOTB email-to-incident processing creates an incident record from an inbound email automatically. The sender's AD record populates the Caller field. Category and priority are set by routing rules. Email channel is still available — it just lands in ServiceNow instead of a shared mailbox."
        ],
        [
            "Can we connect this to our monitoring tools so alerts create incidents automatically?",
            "Yes. ServiceNow Event Management integrates with monitoring tools (SolarWinds, Dynatrace, Splunk, etc.) to auto-create incidents from alerts. That is Sprint 5 scope — we design the integration pattern in the Platform Foundation workshops and build it in Sprint 5."
        ],
        [
            "What about the knowledge base — do we have to build all those articles before go-live?",
            "No. The knowledge base can launch with zero articles and populate through the resolution workflow — every time an engineer resolves an incident using a work note, ServiceNow can prompt them to publish that note as a Knowledge Article. Articles accumulate automatically as the team works. We set the publishing workflow in Sprint 3."
        ],
    ],
    col_widths_in=[3.2, 6.16],
)
doc.page_break()

# =============================================================================
# 4. Recovery Notes
# =============================================================================
doc.h1("Recovery Notes — When Things Go Wrong")
doc.para(
    "Demo environments break. Data gets changed. Something does not render as expected. These "
    "recovery notes tell you what to do when the common problems occur. Stay calm. The customer "
    "does not know what the demo is supposed to look like."
)

doc.table(
    headers=["Problem", "Recovery"],
    rows=[
        [
            "SLA indicators are not showing on the incident list",
            "Say: 'The SLA display is a configuration setting — on your production instance, we configure this to match your SLA visibility preferences. Let me show you the SLA on the individual record instead.' Navigate to a single incident and point to the SLA section on the form."
        ],
        [
            "Assignment did not auto-populate when you changed Category",
            "Say: 'The auto-assignment rule is driven by configuration — we configure the category-to-group mapping in your Sprint 1 workshops. Let me manually assign it so you can see what the assignment looks like.' Manually assign the group and continue."
        ],
        [
            "Knowledge base returns no results for the demo incident",
            "Say: 'Knowledge search works on article content — the more articles your team publishes, the better the results. Let me show you the article directly so you can see the format.' Navigate to the knowledge base and open a published article manually."
        ],
        [
            "Major Incident Workbench is not available or throws an error",
            "Skip the Major Incident act. Say: 'I will save the Major Incident workbench for the Sprint 1 Incident workshop where we will look at it in detail with your process owner.' Move directly to the closing."
        ],
        [
            "Customer asks to see a feature not on the demo script",
            "Say: 'That is a great question — let me add it to our workshop agenda so we can walk through it with your process owner at the table.' Do not improvise off-script mid-demo. Park the request and address it in the appropriate workshop."
        ],
        [
            "Demo instance is slow or unresponsive",
            "Say: 'Environments sometimes have latency — your production instance will be properly sized for your user count. While we wait, let me describe what we will see.' Narrate the next step, then proceed when the screen catches up. Do not repeatedly click — it makes the problem worse."
        ],
    ],
    col_widths_in=[2.6, 6.76],
)

doc.callout(
    "Post-demo rule: after every demo, update the demo data to its baseline state. Reset any "
    "incidents you created to avoid cluttering the demo instance for the next run. If you added "
    "test records, close or delete them. A cluttered demo instance is an unprofessional demo "
    "instance."
)

doc.save(OUT)
print(f"Saved: {OUT}")
