# -*- coding: utf-8 -*-
"""
Build: Connection — Your Document Roadmap (client-facing, one-pager + roadmap table)
Tells Connection up front that documents arrive just-in-time by design: five drops,
what's in each, roughly when, and what we ask of them. Ships in Drop 1.
Built via EcsDocument. Confidential footer — NOT internal.
"""
import sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
OUT = os.path.join(HERE, "Connection_Document_Roadmap.docx")

CONF = "ECS Federal · ServiceNow Practice · Confidential"

doc = EcsDocument(meta=DocMeta(
    eyebrow="CLIENT DOCUMENT ROADMAP",
    title="Modernizing the Core\nYour Document Roadmap",
    subtitle="What you'll receive, when it arrives, and why it comes in stages — by design.",
    org="ECS Federal · ServiceNow Practice",
    audience="Connection — Executive Sponsor, Product Owner, Project Manager, Process Owners",
    companion_to="Client Onboarding Guide · Communication Plan · 18-Week Project Plan",
    doc_id="CLT-CONN-ONB-03",
    version="1.0",
    status="Draft",
    confidentiality=CONF,
    running_header_label="Connection · Document Roadmap",
    footer_left=CONF,
), logo_path=LOGO)


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
    tblW.set(qn('w:type'), 'dxa'); tblW.set(qn('w:w'), str(int(sum(widths_in) * 1440)))
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

doc.h1("Documents Arrive When You Need Them — By Design", numbered=False)
doc.para(
    "Over the 18 weeks you will receive five document packages from us, each timed to the phase "
    "it supports. This is deliberate: rather than handing you a large library on day one, we "
    "release each set about a week before you need it, so the material is always relevant, "
    "current, and light enough to actually read. Workshop presentation decks follow a similar "
    "rhythm — you receive the short pre-read before each session, and the full deck right after "
    "it, as the session's standing reference."
)
doc.para(
    "Every package arrives the same way: a short email describing what's inside, then a brief "
    "review meeting where we walk through the documents together and set expectations for how "
    "each one gets used."
)
doc.table(
    headers=["Package", "When", "What's Inside", "What We Ask of You"],
    col_widths_in=[1.35, 1.10, 2.30, 1.75],
    rows=[
        ["1 — Initial Package", "At kickoff",
         "Onboarding guide, communication plan, governance charter, kickoff deck, Sprint 0 checklist, 18-week project plan, dependency tracker, deliverables checklist — and this roadmap.",
         "Skim the onboarding guide and communication plan; bring questions to the kickoff review."],
        ["2 — Foundation & Data", "~Week 2–3",
         "Pre-reads for the foundation workshops (platform, CSDM, CMDB, Discovery) and the data-collection workbooks for your team to complete.",
         "Skim the optional pre-reads if you have ten minutes; start the data workbooks early."],
        ["3 — ITSM Core", "~Week 6",
         "Pre-reads and decision packs for Incident, Major Incident, Problem, Change, and Service Catalog workshops.",
         "Confirm the right process owners attend; the optional pre-reads preview each session's decisions."],
        ["4 — Employee Experience & Analytics", "~Week 10",
         "Pre-reads and decision packs for Employee Center, Virtual Agent, Knowledge, Predictive Intelligence, analytics, and HAM.",
         "Include your communications and employee-experience voices in these sessions."],
        ["5 — Testing, Go-Live & Handoff", "~Week 13",
         "UAT guidebook and test scripts, go-live readiness checklist, cutover runbook, and the knowledge-transfer package for your admins and trainers.",
         "Name your UAT testers early; hold the go/no-go review with us in Week 15."],
    ],
)
doc.callout(
    "Need something sooner? Everything ultimately lives in the shared engagement library — ask "
    "your ECS Engagement Manager and any document can be released early. The staging exists to "
    "protect your team's attention, not to withhold anything."
)

doc.save(OUT)
print(f"Saved: {OUT}")
