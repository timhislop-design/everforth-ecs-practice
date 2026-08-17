# -*- coding: utf-8 -*-
"""
Build: Connection — Communication Plan (client-facing)
Theme: Modernizing the Core. Audience: Connection stakeholders.
Adapted from the library baseline CLT-S0-06 (02_Client/02_Sprint0_Customer_Readiness),
tailored to the Connection Phase 1 cadence (Sprints 0-8 / 4 stages, Go-Live Wk 16,
Hypercare Wks 17-18), the ECS pod role model (EM/SA/BPC-BA Scrum Master hat/TC/PL),
and the Connection delivery artifacts (Weekly Status Report, Executive Health
Dashboard, Governance Triage & RAID, Sprint Demo, Customer Dependency Tracker).
Built via EcsDocument (ecs_template.py). Confidential footer — NOT internal.
"""
import sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
OUT = os.path.join(HERE, "Connection_Communication_Plan.docx")

CONF = "ECS Federal · ServiceNow Practice · Confidential"

doc = EcsDocument(meta=DocMeta(
    eyebrow="CLIENT COMMUNICATION PLAN",
    title="Modernizing the Core\nCommunication Plan",
    subtitle="How we will stay connected across your 18-week reimplementation — every touchpoint, owner, and cadence.",
    org="ECS Federal · ServiceNow Practice",
    audience="Connection — Executive Sponsor, Product Owner, Project Manager, Technical Lead, Process Owners",
    companion_to="Client Onboarding Guide · Governance Charter · 18-Week Project Plan · Weekly Status Report",
    doc_id="CLT-CONN-ONB-02",
    version="1.0",
    status="Draft",
    confidentiality=CONF,
    running_header_label="Connection · Communication Plan",
    footer_left=CONF,
), logo_path=LOGO)


# --- fixed-layout helper: pin tblGrid + layout so widths render as specified ---
def fix_layout(t, widths_in):
    tbl = t._tbl
    tblPr = tbl.tblPr
    for old in tblPr.findall(qn('w:tblLayout')):
        tblPr.remove(old)
    layout = OxmlElement('w:tblLayout')
    layout.set(qn('w:type'), 'fixed')
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
doc.page_break()

# 1. Purpose
doc.h1("Purpose", numbered=True)
doc.para(
    "This plan describes every regular communication Connection will receive from the ECS team "
    "across the 18-week Phase 1 engagement — what it covers, how often it arrives, who leads it, "
    "and who from your organization should be in the room. Our goal is that your leadership never "
    "has to ask “where do things stand?” — the answer is always already in your inbox or on your calendar."
)
doc.para(
    "During Sprint 0 kickoff we will walk through this plan together, confirm the cadence fits "
    "Connection's rhythm, and complete the contact roster in Section 6. Once agreed, this plan "
    "becomes the standing reference for both teams, alongside the Governance Charter."
)
doc.callout(
    "Nothing in this cadence is extra ceremony. Each touchpoint exists to surface decisions early, "
    "keep the baseline protected, and give Connection leadership a simple, reliable view of progress."
)

# 2. Engagement rhythm
doc.h1("The Engagement Rhythm", numbered=True)
doc.para(
    "Phase 1 runs 18 weeks in two-week sprints (Sprints 0–8), organized into four stages. "
    "Communications follow this rhythm — workshop-heavy in the build stages, testing- and "
    "readiness-focused as we approach Go-Live at Week 16."
)
doc.table(
    headers=["Stage", "Sprints / Weeks", "Communication Focus"],
    col_widths_in=[1.8, 1.5, 3.2],
    rows=[
        ["Stage 1 — Initiate & Plan", "Sprints 0–2 · Wks 1–6",
         "Kickoff, governance setup, workshop invitations, data collection via accelerator packs, dependency tracking."],
        ["Stage 2 — Execute", "Sprints 3–5 · Wks 7–12",
         "Workshop and demo cadence at full tempo; council reviews of any requested deviations; weekly status discipline."],
        ["Stage 3 — Deliver", "Sprints 6–7 · Wks 13–16",
         "SIT/UAT coordination, training and knowledge transfer scheduling, Go-Live readiness reviews, cutover go/no-go."],
        ["Stage 4 — Close", "Sprint 8 · Wks 17–18",
         "Hypercare status updates, stabilization triage, closeout and lessons learned, 12-month roadmap discussion."],
    ],
)

# 3. Communication cadence
doc.h1("Communication Cadence", numbered=True)
doc.para(
    "The table below is the complete cadence for the engagement. “Led by” names who initiates and "
    "runs each communication; what Connection can expect is described in the final column."
)
doc.table(
    headers=["Communication", "Frequency", "Led By", "Format", "What You Can Expect"],
    col_widths_in=[1.30, 0.95, 1.05, 0.90, 2.30],
    rows=[
        ["Weekly Status Report", "Weekly (Friday)", "ECS Engagement Manager", "Email",
         "One-page snapshot for your Sponsor, PM, and process owners: RAG status by workstream, progress against the sprint plan, decisions needed, and risks with owners."],
        ["Sponsor Sync + Executive Health Dashboard", "Every 2 weeks", "ECS EM + Practice Lead (periodic)", "45–60-min meeting",
         "Working session with your Executive Sponsor anchored by the one-page Executive Health Dashboard: sprint health, story completion, deliverables on track, and anything needing executive attention."],
        ["Sprint Demo", "End of each sprint (every 2 weeks)", "BPC/BA (Scrum Master) + ECS EM", "60-min meeting",
         "Working functionality demonstrated live at the end of every sprint — your Product Owner and process owners confirm what was built matches what was decided. All interested stakeholders welcome."],
        ["Sprint Planning & Stand-ups", "Per sprint / daily during build", "BPC/BA (Scrum Master)", "Ceremonies",
         "Your Product Owner and PM join sprint planning; daily 15-minute stand-ups are open to your PM. This is where the day-to-day rhythm lives."],
        ["Workshop Invitations", "Per sprint schedule (Stages 1–2)", "ECS Engagement Manager", "Calendar invitation",
         "Invitations to your process owners and SMEs for each module's design workshops, with pre-reads ahead of every session so no one walks in cold."],
        ["Customization Council", "As needed (typically bi-weekly)", "ECS EM (chair)", "60-min meeting",
         "Review of any request that deviates from the baseline, using the Governance Triage & RAID log. Every deviation gets an OOTB alternative presented first, and Sponsor sign-off before any custom work."],
        ["Dependency Check", "Weekly (within status cadence)", "ECS EM + Connection PM", "Working review",
         "Review of the Customer Dependency Tracker — the data, access, and decisions Connection owns, with timing and impact-if-late, so nothing surprises either team."],
        ["UAT Coordination", "Sprints 6–7", "BPC/BA + Product Owner", "Sessions + email",
         "Test scripts, the UAT Guidebook, tester scheduling, and daily defect triage during UAT cycles."],
        ["Go-Live Go/No-Go", "Week 15–16", "ECS EM + Executive Sponsor + Product Owner", "Gated review",
         "Joint review of the Go-Live Readiness Checklist — gated criteria across configuration, data, integrations, testing, training, and support before cutover proceeds."],
        ["Go-Live Announcement", "Week 16", "Connection Comms + ECS EM", "Email / intranet",
         "Jointly drafted announcement to all staff: what is changing, when, and where to get help. ECS drafts; Connection owns the send."],
        ["Hypercare Status Update", "Weekly (Wks 17–18)", "ECS EM", "Email + triage",
         "Stabilization summary for your PM, Technical Lead, and Platform Admin: ticket trends, open items, and progress toward formal closeout and the 12-month roadmap."],
    ],
)

# 4. Roles & responsibilities
doc.h1("Communication Roles and Responsibilities", numbered=True)
doc.para(
    "Clear ownership keeps the cadence lightweight. These are the standing communication "
    "responsibilities on each side of the partnership, consistent with the Governance Charter and RACI Matrix."
)
doc.h2("Connection team")
doc.table(
    headers=["Role", "Communication Responsibility"],
    col_widths_in=[1.7, 4.8],
    rows=[
        ["Executive Sponsor",
         "Attends the bi-weekly Sponsor Sync; signs off on any approved deviation from the baseline; makes or delegates escalated decisions within two business days."],
        ["Product Owner",
         "Attends sprint planning and every sprint demo; approves acceptance criteria before build and confirms Definition of Done at close; first voice on scope questions."],
        ["Project Manager",
         "Day-to-day counterpart to the ECS Engagement Manager; joins stand-ups as desired; keeps the Dependency Tracker current on Connection-owned items; distributes communications internally."],
        ["Technical Lead",
         "Reviews architecture and integration communications; attends cutover planning; first technical point of contact for escalations on your side."],
        ["Process Owners & SMEs",
         "Attend the workshops and demos for their process areas; respond to decision requests within the agreed turnaround (typically two business days)."],
        ["UAT Testers",
         "Participate in UAT cycles (Sprints 6–7) using the UAT Guidebook; log defects promptly with reproduction steps."],
        ["Platform Admin",
         "Attends Admin knowledge-transfer sessions and Hypercare triage; receives the Administrator Guide & KT materials at Go-Live."],
    ],
)
doc.h2("ECS team")
doc.table(
    headers=["Role", "Communication Responsibility"],
    col_widths_in=[1.7, 4.8],
    rows=[
        ["Engagement Manager",
         "Owns the cadence end to end: status reports, Sponsor Syncs, dependency reviews, triage log updates, and escalation management. Chairs the Customization Council. Your single point of contact."],
        ["Solution Architect",
         "Leads architecture and CSDM communications; presents the OOTB alternative for every deviation request; owns technical workshop content."],
        ["BPC/BA (Scrum Master)",
         "Runs the sprint ceremonies — planning, stand-ups, demos, retros — and owns the sprint-health signals that feed the Executive Health Dashboard; facilitates workshops and UAT coordination."],
        ["Technical Consultant(s)",
         "Support workshops and demos for their build areas; surface build questions through the sprint ceremonies rather than side channels."],
        ["Practice Lead",
         "Engaged at the final escalation tier; joins Sponsor Syncs periodically to independently confirm the engagement is delivering the outcomes Connection expected."],
    ],
)

# 5. Escalation path
doc.h1("Escalation Path", numbered=True)
doc.para(
    "Most issues resolve inside the normal cadence. When one cannot, it follows this path — each "
    "step has a named owner and a clock, so nothing stalls. Scope and deviation requests are not "
    "escalations: they route through the Customization Council and the PCR process."
)
doc.table(
    headers=["Step", "Who Is Involved", "Target Timeframe"],
    col_widths_in=[2.9, 2.3, 1.3],
    rows=[
        ["1. Raise at the working level — flag to the BPC/BA (Scrum Master), the ECS Engagement Manager, or your Project Manager",
         "ECS EM + Connection PM", "Same day"],
        ["2. Joint review — the EM and your PM (with the Technical Lead where technical) assess impact and options",
         "ECS EM + Connection PM / Technical Lead", "2 business days"],
        ["3. Executive resolution — escalated jointly with a written summary and recommendation",
         "ECS Practice Lead + Executive Sponsor", "3 business days"],
    ],
)
doc.para(
    "Escalation is a healthy part of delivery, not a failure signal. Raising an issue early is "
    "always the right call, and no escalation will ever be held against the person who raised it."
)

# 6. Contact roster
doc.h1("Contact Roster", numbered=True)
doc.para(
    "Complete this roster at Sprint 0 kickoff and keep it current throughout the engagement. "
    "The ECS Engagement Manager maintains the master copy and redistributes it whenever it changes."
)
doc.h2("Connection team")
doc.table(
    headers=["Role", "Name", "Email", "Phone", "Preferred Contact Method"],
    col_widths_in=[1.3, 1.2, 1.6, 1.1, 1.3],
    rows=[
        ["Executive Sponsor", "", "", "", ""],
        ["Product Owner", "", "", "", ""],
        ["Project Manager", "", "", "", ""],
        ["Technical Lead", "", "", "", ""],
        ["Communications Lead", "", "", "", ""],
        ["Platform Admin", "", "", "", ""],
    ],
    alt_shading=False,
)
doc.h2("ECS team")
doc.table(
    headers=["Role", "Name", "Email", "Phone", "Preferred Contact Method"],
    col_widths_in=[1.3, 1.2, 1.6, 1.1, 1.3],
    rows=[
        ["Engagement Manager", "", "", "", ""],
        ["Solution Architect", "", "", "", ""],
        ["BPC/BA (Scrum Master)", "", "", "", ""],
        ["Technical Consultant", "", "", "", ""],
        ["Practice Lead", "", "", "", ""],
    ],
    alt_shading=False,
)
doc.callout(
    "Questions about anything in this plan? Your ECS Engagement Manager is the front door — "
    "one contact, every topic, always."
)

doc.save(OUT)
print(f"Saved: {OUT}")
