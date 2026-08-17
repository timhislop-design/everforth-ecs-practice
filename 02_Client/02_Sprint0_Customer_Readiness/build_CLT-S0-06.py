"""
Build CLT-S0-06 — Communication Plan (Client-Facing)
Adapted from INT-S0-07 Communication Plan Template (internal). Partnership-toned:
describes the full engagement communication cadence from the customer's seat —
what they receive, who leads it, and what is asked of their team. Internal
template IDs stripped; Governance Triage Log referenced by name as a feature.

Sections: Purpose · Communication Cadence · Roles & Responsibilities ·
Escalation Path · Contact Roster (fill-in at Sprint 0 kickoff).
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT  = os.path.join(HERE, "CLT-S0-06_Communication_Plan.docx")
LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")

doc = EcsDocument(
    meta=DocMeta(
        eyebrow="CLIENT · SPRINT 0 READINESS",
        title="Communication Plan",
        subtitle="How we will stay connected across your 18-week ServiceNow engagement",
        org="ECS Federal · ServiceNow Practice",
        audience="Project Sponsor, IT Director, Process Owners, Customer PM",
        companion_to="CLT-S0-01 Customer Readiness Checklist · CLT-S0-04 SME Time-Commitment Calendar",
        doc_id="CLT-S0-06",
        version="1.0",
        status="Released",
        confidentiality="Confidential — prepared for the recipient and their organization",
        running_header_label="Client · CLT-S0-06 Communication Plan",
        footer_left="ECS Federal · ServiceNow Practice  ·  Confidential",
    ),
    logo_path=LOGO,
)


# --- fixed-layout helper: pin tblGrid + layout so widths render as specified ---
def fix_layout(t, widths_in):
    tbl = t._tbl
    tblPr = tbl.tblPr
    for old in tblPr.findall(qn('w:tblLayout')):
        tblPr.remove(old)
    layout = OxmlElement('w:tblLayout')
    layout.set(qn('w:type'), 'fixed')
    # schema order: tblLayout must precede tblCellMar/tblLook
    _after = ['tblCellMar', 'tblLook', 'tblCaption', 'tblDescription']
    _ins = None
    for child in list(tblPr):
        if child.tag.split('}')[-1] in _after:
            _ins = child
            break
    if _ins is not None:
        tblPr.insert(list(tblPr).index(_ins), layout)
    else:
        tblPr.append(layout)
    tblW = tblPr.find(qn('w:tblW'))
    if tblW is None:
        tblW = OxmlElement('w:tblW'); tblPr.append(tblW)
    total = int(sum(widths_in) * 1440)
    tblW.set(qn('w:type'), 'dxa'); tblW.set(qn('w:w'), str(total))
    for old in tbl.findall(qn('w:tblGrid')):
        tbl.remove(old)
    grid = OxmlElement('w:tblGrid')
    for w in widths_in:
        gc = OxmlElement('w:gridCol'); gc.set(qn('w:w'), str(int(w * 1440)))
        grid.append(gc)
    tbl.insert(list(tbl).index(tblPr) + 1, grid)


_orig_table = doc.table
def table_fixed(**kw):
    t = _orig_table(**kw)
    if kw.get('col_widths_in'):
        fix_layout(t, kw['col_widths_in'])
    return t
doc.table = table_fixed

doc.add_cover_page()
doc.add_page_break()

# 1. Purpose
doc.h1("Purpose")
doc.para(
    "This plan describes every regular communication you will receive from the ECS team during "
    "your 18-week engagement — what it covers, how often it arrives, who leads it, and who from "
    "your organization should be in the room. Our goal is that your leadership never has to ask "
    "“where do things stand?” — the answer is always already in your inbox or on your calendar."
)
doc.para(
    "During Sprint 0 kickoff, we will walk through this plan together, confirm the cadence fits "
    "your organization's rhythm, and complete the contact roster in Section 5. Once agreed, this "
    "plan becomes the standing reference for both teams."
)
doc.callout(
    "Nothing in this cadence is extra ceremony. Each touchpoint exists to surface decisions early, "
    "keep the baseline protected, and give your leadership a simple, reliable view of progress."
)

# 2. Communication Cadence
doc.h1("Communication Cadence")
doc.para(
    "The table below is the complete cadence for the engagement — Sprint 0 through Hypercare. "
    "“Led by” names who initiates and runs each communication; your role is described in "
    "the final column."
)
doc.table(
    headers=["Communication", "Frequency", "Led By", "Format", "What You Can Expect"],
    col_widths_in=[1.30, 0.95, 1.05, 0.90, 2.30],
    rows=[
        ["Weekly Status Report", "Weekly (Friday)", "ECS Engagement Manager", "Email",
         "One-page snapshot for your IT Director and process owners: progress against the sprint plan, decisions needed from you, and risks with owners."],
        ["Sponsor Sync", "Every 2 weeks", "ECS EM + Lead Consultant", "60-min meeting",
         "Working session with your Project Sponsor: milestone health, upcoming decision points, and anything needing executive attention."],
        ["Customization Council", "Every 2 weeks", "ECS Lead Consultant", "60-min meeting",
         "Council review of any requests that deviate from the baseline, using the Governance Triage Log. Pre-read arrives one business day ahead."],
        ["Sprint Workshop Invitations", "Per sprint schedule", "ECS Engagement Manager", "Calendar invitation",
         "Invitations to your process owners and SMEs for each sprint's workshops, aligned to the SME Time-Commitment Calendar."],
        ["Sprint Demo Invitation", "Per sprint schedule", "ECS Engagement Manager", "Calendar invitation",
         "Open demo of working functionality at the end of each sprint — your IT Director and all interested stakeholders are welcome."],
        ["Governance Triage Log Update", "After each sprint", "ECS Engagement Manager", "Email with attachment",
         "Current log of every requested deviation from the baseline, its rationale, and its disposition — your standing record of scope decisions."],
        ["Escalation", "As needed", "ECS Engagement Manager", "Email + call",
         "Issues that cannot be resolved at the working level move promptly through the path in Section 4 — nothing waits for the next meeting."],
        ["Go-Live Announcement", "Go-live week", "Your Comms Lead + ECS EM", "Email / intranet",
         "Jointly drafted announcement to all staff: what is changing, when, and where to get help. ECS drafts; your team owns the send."],
        ["Hypercare Status Update", "Weekly during Hypercare", "ECS Lead Consultant", "Email",
         "Post-go-live health summary for your IT Director and Service Desk Manager: ticket trends, open items, stabilization progress."],
    ],
)

# 3. Roles & Responsibilities
doc.h1("Communication Roles and Responsibilities")
doc.para(
    "Clear ownership keeps the cadence lightweight. These are the standing communication "
    "responsibilities on each side of the partnership."
)
doc.h2("Your team")
doc.table(
    headers=["Role", "Communication Responsibility"],
    col_widths_in=[1.7, 4.8],
    rows=[
        ["Project Sponsor",
         "Attends the bi-weekly Sponsor Sync; makes or delegates escalated decisions within two business days; champions the engagement to your leadership."],
        ["IT Director",
         "Reviews the Weekly Status Report; attends Sponsor Syncs and sprint demos; first point of contact for escalations on your side."],
        ["Customer PM",
         "Day-to-day counterpart to the ECS Engagement Manager; confirms workshop attendance; distributes communications internally."],
        ["Process Owners & SMEs",
         "Attend the workshops and demos for their process areas; respond to decision requests within the agreed turnaround (typically two business days)."],
        ["Communications Lead",
         "Owns staff-facing messaging for go-live, using ECS-provided draft language; coordinates intranet and email distribution."],
    ],
)
doc.h2("ECS team")
doc.table(
    headers=["Role", "Communication Responsibility"],
    col_widths_in=[1.7, 4.8],
    rows=[
        ["Engagement Manager",
         "Owns the cadence end to end: status reports, meeting facilitation, triage log updates, and escalation management. Your single point of contact."],
        ["Lead Consultant",
         "Runs the Customization Council and Hypercare updates; co-leads Sponsor Syncs; brings configuration recommendations to every decision discussion."],
        ["ECS Practice Lead",
         "Engaged at the final escalation tier; joins Sponsor Syncs periodically to confirm the engagement is delivering the outcomes you expected."],
    ],
)

# 4. Escalation Path
doc.h1("Escalation Path")
doc.para(
    "Most issues resolve inside the normal cadence. When one cannot, it follows this path — "
    "each step has a named owner and a clock, so nothing stalls."
)
doc.table(
    headers=["Step", "Who Is Involved", "Target Timeframe"],
    col_widths_in=[2.9, 2.3, 1.3],
    rows=[
        ["1. Raise at the working level — flag to the ECS Engagement Manager or your Customer PM",
         "ECS EM + Customer PM", "Same day"],
        ["2. Joint review — the EM and your IT Director assess impact and options",
         "ECS EM + IT Director", "2 business days"],
        ["3. Executive resolution — escalated jointly with a written summary and recommendation",
         "ECS Practice Lead + Project Sponsor", "3 business days"],
    ],
)
doc.para(
    "Escalation is a healthy part of delivery, not a failure signal. Raising an issue early is "
    "always the right call, and no escalation will ever be held against the person who raised it."
)

# 5. Contact Roster
doc.h1("Contact Roster")
doc.para(
    "Complete this roster at Sprint 0 kickoff and keep it current throughout the engagement. "
    "The ECS Engagement Manager maintains the master copy and redistributes it whenever it changes."
)
doc.h2("Your team")
doc.table(
    headers=["Role", "Name", "Email", "Phone", "Preferred Contact Method"],
    col_widths_in=[1.3, 1.2, 1.6, 1.1, 1.3],
    rows=[
        ["Project Sponsor", "", "", "", ""],
        ["IT Director", "", "", "", ""],
        ["Customer PM", "", "", "", ""],
        ["Communications Lead", "", "", "", ""],
        ["Service Desk Manager", "", "", "", ""],
    ],
    alt_shading=False,
)
doc.h2("ECS team")
doc.table(
    headers=["Role", "Name", "Email", "Phone", "Preferred Contact Method"],
    col_widths_in=[1.3, 1.2, 1.6, 1.1, 1.3],
    rows=[
        ["Engagement Manager", "", "", "", ""],
        ["Lead Consultant", "", "", "", ""],
        ["ECS Practice Lead", "", "", "", ""],
    ],
    alt_shading=False,
)
doc.callout(
    "Questions about anything in this plan? Your ECS Engagement Manager is the front door — "
    "one contact, every topic, always."
)

doc.save(OUT)
print(f"Saved: {OUT}")
