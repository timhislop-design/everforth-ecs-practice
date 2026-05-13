"""
Build INT-TBV-04 — Bi-Weekly Sponsor Sync Agenda Template
45-minute cadence document for Engagement Managers. Fill-in-the-blank template
for each sync: pre-meeting checklist, agenda sections, notes, and action items.
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

OUT = os.path.join(HERE, "INT-TBV-04_Sponsor_Sync_Agenda_Template.docx")

d = EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL TEMPLATE · TRUST-BUT-VERIFY DISCIPLINE",
    title="Bi-Weekly Sponsor Sync\nAgenda Template",
    subtitle="The 45-minute cadence that keeps sponsors aligned and drift visible before it becomes commitment",
    audience="Engagement Manager (primary) · Solution Architect (attends)",
    companion_to="INT-TBV-01 (Manager Playbook) · INT-TBV-02 (Health Dashboard) · INT-TBV-03 (Variance Tracker)",
    doc_id="INT-TBV-04",
    version="1.0",
    status="Released",
    running_header_label="Internal · Bi-Weekly Sponsor Sync Agenda Template",
))

d.add_cover_page()

d.para(
    "Complete this template before every bi-weekly sponsor sync. Circulate the completed agenda to the sponsor "
    "and ECS attendees 24 hours before the meeting. Do not run the sync without a completed agenda — the "
    "agenda is the mechanism, not the meeting."
)

# ── HOW TO USE ────────────────────────────────────────────────────────────────
d.h1("How to Use This Template", numbered=False)
d.para(
    "This document is a repeating template. Before each sync, the Engagement Manager creates a new copy, "
    "fills in the header block (date, sprint, attendees), completes the pre-meeting checklist, and drafts "
    "the agenda item notes from the Engagement Health Dashboard (INT-TBV-02) and Variance Tracker (INT-TBV-03). "
    "After the sync, the EM records meeting notes in-line and captures action items in the tracker table."
)
d.callout(
    "The three items you must surface every sync regardless of agenda: "
    "(1) any vector currently Yellow or Red with the EM's planned response; "
    "(2) any customization request raised in the last two weeks, even if pre-Council, framed against the OOTB alternative; "
    "(3) any signal from the customer team suggesting 'but our old system did X' is forming as a position."
)
d.para("Anti-patterns to avoid in every sync:", bold=True, space_after=2)
d.bullet("The 'casual catch-up' — running without the agenda template open and the dashboard visible.")
d.bullet("The 'good news only' sync — reporting green vectors and omitting yellow ones to avoid a difficult conversation.")
d.bullet("The 'absorb the ask' sync — verbally agreeing to a customization in the meeting before it goes through the Council.")

d.page_break()

# ── HEADER BLOCK ──────────────────────────────────────────────────────────────
d.h1("Sync Header — Complete Before Circulating", numbered=False)
d.table(
    headers=["Field", "Value"],
    rows=[
        ["Engagement Name",         "[Enter engagement name]"],
        ["Sync Date & Time",        "[Enter date and time]"],
        ["Sprint / Week",           "[e.g., Sprint 3 – Week A]"],
        ["Engagement Manager",      "[Name]"],
        ["Solution Architect",      "[Name]"],
        ["Customer Sponsor",        "[Name and title]"],
        ["Additional Attendees",    "[Names — keep to minimum required for quorum]"],
        ["Variance Band (entering sync)", "[Green / Yellow / Orange / Red — from INT-TBV-02]"],
        ["Council Items Pending",   "[Number of open customization requests awaiting Council decision]"],
    ],
    col_widths_in=[2.4, 6.0],
)

d.page_break()

# ── PRE-MEETING CHECKLIST ─────────────────────────────────────────────────────
d.h1("Pre-Meeting Checklist — Complete 24 Hours Before Sync", numbered=False)
d.para("The EM confirms all items below before circulating the agenda. If an item cannot be confirmed, note the gap.")
d.table(
    headers=["#", "Checklist Item", "Status", "Notes"],
    rows=[
        ["1", "INT-TBV-02 (Health Dashboard) updated for this week's scan", "☐ Done  ☐ Pending", ""],
        ["2", "INT-TBV-03 (Variance Tracker) current — all requests logged through Stage 3 minimum", "☐ Done  ☐ Pending", ""],
        ["3", "Any Yellow or Red vector identified and EM talking-points prepared", "☐ Done  ☐ N/A", ""],
        ["4", "Customization requests raised since last sync summarized with OOTB alternative (at least one line)", "☐ Done  ☐ N/A", ""],
        ["5", "Sponsor's open items from last sync reviewed — response ready", "☐ Done  ☐ N/A", ""],
        ["6", "Decisions required this sprint identified — decision-framing prepared", "☐ Done  ☐ N/A", ""],
        ["7", "Meeting link / room confirmed and agenda sent to all attendees", "☐ Done  ☐ Pending", ""],
    ],
    col_widths_in=[0.4, 3.4, 1.8, 2.8],
)

d.page_break()

# ── AGENDA ────────────────────────────────────────────────────────────────────
d.h1("Agenda — 45 Minutes Total", numbered=False)
d.para(
    "Follow the time blocks as written. If an agenda item is running long, park the detail in the Notes section "
    "and continue — the action item tracker captures what needs follow-up. Do not convert the sponsor's open items "
    "block into another EM-led monologue."
)

d.h2("Block 1 — Build Progress Since Last Sync (10 min)")
d.para("EM-led. Walk the Engagement Health Dashboard at vector level — not line by line, but one sentence per vector.")
d.table(
    headers=["Vector", "Current Band", "Change Since Last Sync", "EM Talking Points"],
    rows=[
        ["Process Adoption",      "[Green/Yellow/Red]", "[Moved up / Stayed / Moved down]", ""],
        ["Configuration Hygiene", "[Green/Yellow/Red]", "[Moved up / Stayed / Moved down]", ""],
        ["Customization Variance","[Green/Yellow/Red]", "[Moved up / Stayed / Moved down]", ""],
        ["Adoption Readiness",    "[Green/Yellow/Red]", "[Moved up / Stayed / Moved down]", ""],
        ["Sentiment & Trust",     "[Green/Yellow/Red]", "[Moved up / Stayed / Moved down]", ""],
        ["Overall Band",          "[Green/Yellow/Red]", "[Moved up / Stayed / Moved down]", ""],
    ],
    col_widths_in=[1.8, 1.2, 1.8, 3.6],
)
d.para("Meeting notes — Block 1:", bold=True, space_after=2)
d.para("[Enter notes here]")

d.h2("Block 2 — Decisions Coming This Sprint (10 min)")
d.para("EM-led. Frame each decision using the two-key model: what is the customer deciding, what is ECS recommending, and what is the Council-decision timeline.")
d.table(
    headers=["Decision Required", "OOTB Recommendation", "Customer's Question / Position", "Target Decision Date"],
    rows=[
        ["[Enter decision 1]", "[OOTB approach + rationale]", "", ""],
        ["[Enter decision 2]", "[OOTB approach + rationale]", "", ""],
        ["[Enter decision 3 if applicable]", "", "", ""],
    ],
    col_widths_in=[2.4, 2.4, 2.0, 1.6],
)
d.para("Meeting notes — Block 2:", bold=True, space_after=2)
d.para("[Enter notes here]")

d.h2("Block 3 — Customization Council Update (10 min)")
d.para(
    "EM-led. What was raised since last sync, what was decided, and what is pending Council. "
    "Every customization request — even brand-new ones — gets named here with its OOTB alternative framing. "
    "Do not allow a customization to exist without the sponsor knowing it is in the deviation lifecycle."
)
d.table(
    headers=["Request ID", "Description", "Stage", "OOTB Alternative (one line)", "Council Date / Decision"],
    rows=[
        ["[CVT-###]", "", "[Stage 1–6]", "", ""],
        ["[CVT-###]", "", "[Stage 1–6]", "", ""],
        ["[CVT-###]", "", "[Stage 1–6]", "", ""],
    ],
    col_widths_in=[0.9, 2.2, 0.8, 2.6, 2.0],
)
d.para("Meeting notes — Block 3:", bold=True, space_after=2)
d.para("[Enter notes here]")

d.h2("Block 4 — Sponsor's Open Items (10 min)")
d.para(
    "Sponsor-led. EM listens. Do not fill this block with EM talking points. "
    "This block exists to surface concerns the sponsor has been holding. "
    "If the sponsor says 'we are fine,' probe once: 'Anything from your team this week about the direction we are taking?'"
)
d.para("Meeting notes — Block 4 (sponsor's concerns / questions):", bold=True, space_after=2)
d.para("[Enter notes here — capture verbatim if possible]")
d.callout(
    "If the sponsor raises a customization request verbally here, do NOT commit in the meeting. "
    "Response: 'That is exactly what the Council process is for — let me log it and get you the OOTB "
    "alternative before we make any commitment.' Then log it in INT-TBV-03 within 24 hours."
)

d.h2("Block 5 — Action Recap and Next Steps (5 min)")
d.para("EM-led. Read the action table back to the group. Confirm owner and due date for each item.")
d.table(
    headers=["#", "Action Item", "Owner", "Due Date", "Status"],
    rows=[
        ["1", "", "", "", "Open"],
        ["2", "", "", "", "Open"],
        ["3", "", "", "", "Open"],
        ["4", "", "", "", "Open"],
        ["5", "", "", "", "Open"],
    ],
    col_widths_in=[0.4, 4.0, 1.4, 1.4, 1.2],
)

d.page_break()

# ── CARRY-FORWARD TRACKER ─────────────────────────────────────────────────────
d.h1("Carry-Forward Items from Prior Syncs", numbered=False)
d.para(
    "Track items from previous syncs that are still open. The EM updates this section at the start of each "
    "new sync cycle. Items not resolved after two sync cycles escalate to the Practice Lead."
)
d.table(
    headers=["Sync Date", "Item", "Owner", "Status", "Escalate?"],
    rows=[
        ["", "", "", "Open", "No"],
        ["", "", "", "Open", "No"],
        ["", "", "", "Open", "No"],
        ["", "", "", "Closed", "N/A"],
    ],
    col_widths_in=[1.0, 4.0, 1.4, 1.0, 1.0],
)

d.h1("Coaching Note for New Engagement Managers", numbered=False)
d.para(
    "The Sponsor Sync fails in one of three predictable ways. The first is running it as a status report — the "
    "sponsor hears what is done and feels informed, but no one surfaces what is at risk. The second is running "
    "it as a relationship call — the conversation is warm but the dashboard is not opened and customization "
    "requests are not named. The third is treating the sponsor's ask as a final answer — the sponsor says "
    "'we want X,' and the EM nods without routing through the Council."
)
d.para(
    "The agenda template prevents all three patterns when it is followed. The discipline is the template. "
    "If you feel the template is making conversations awkward, the solution is more practice, not less structure."
)
d.callout(
    "Pair this template with INT-TBV-01 (Manager Playbook) Section 5 for full context on Sponsor Sync discipline, "
    "and INT-TBV-08 (Course-Correction Playbook) for what to do when a sync reveals a band-crossing."
)

d.save(OUT)
print(f"Saved: {OUT}")
