# -*- coding: utf-8 -*-
"""
Build: Connection — Staged Rollout Email Templates (ECS internal working aid)
One ready-to-send cover email per document drop. Tone: warm, partnership-oriented,
explicitly welcoming questions; pre-reads framed as optional refreshers, never
homework. Every email closes the same way: next step is a short review meeting to
walk through the documents together and set expectations.

Outputs:
1. Internal_Release_Kit/Drop_Email_Templates_INTERNAL.docx — all five, with usage notes.
2. Client_Drops/<Drop_Name>_EMAIL.docx — one per drop, named to match its zip
   (Drop_01_Initial_Package.zip ↔ Drop_01_Initial_Package_EMAIL.docx) so the EM
   always knows which email text pairs with which package.
"""
import sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

LOGO = os.path.join(REPO, "00_Master_Blueprint", "assets", "everforth_logo.png")
ROLLOUT = os.path.join(REPO, "06_Client_Upload", "Connection_Staged_Rollout")
KIT = os.path.join(ROLLOUT, "Internal_Release_Kit")
DROPS_DIR = os.path.join(ROLLOUT, "Client_Drops")

GREET = "Hello Neveena,"
SIGN = "Best regards,\n-Tim"

# (drop folder name, display title, subject, [body paragraphs])
EMAILS = [
    ("Drop_01_Initial_Package", "Drop 1 — Initial Package",
     "Your Connection engagement package — how the project will run",
     [
      GREET,
      "Ahead of our kickoff, I'm sharing the initial document package for the engagement. These nine "
      "documents are your orientation to how the project will run — nothing here requires action yet, "
      "and you don't need to read everything at once.",
      "If you read just two things, make them the Client Onboarding Guide (what to expect across the "
      "18 weeks, in plain terms) and the Communication Plan (every touchpoint you'll receive from us — "
      "what, when, and from whom). Alongside those you'll find the Governance Charter, the kickoff "
      "presentation, the Sprint 0 checklist, the 18-week project plan, the dependency tracker showing "
      "what Connection owns, and the deliverables checklist — every commitment in the SOW and where "
      "it stands (your running scoreboard for the whole engagement). The Document Roadmap ties it all "
      "together: it shows every package you'll receive across the 18 weeks and when — documents "
      "arrive just-in-time by design, so your team is never buried.",
      "You will likely have questions — that's exactly what we want. No question is too small, and "
      "the early ones tend to be the most valuable. Jot them down as you skim, or just bring "
      "yourself — either works.",
      "I am finalizing team assignments and as a next step, I'd like to schedule a 45-minute "
      "review meeting to walk through the package together, answer whatever comes up, and set "
      "expectations for how we'll use each of these documents. Let me know what works for your "
      "schedule, I can be flexible.",
      "Looking forward to getting started together.",
      SIGN,
     ]),
    ("Drop_02_Foundation_and_Data", "Drop 2 — Foundation & Data",
     "Stage 1 materials — foundation workshops and data collection",
     [
      GREET,
      "With Sprint 0 wrapping up, here is the material for Stage 1 — the platform foundation and "
      "data-model work in Weeks 3–6. This package has two kinds of content: short pre-reads for "
      "each upcoming workshop, and the data-collection packs (users, locations, groups, service "
      "taxonomy, discovery scope, and integration details). Each workshop's full deck follows "
      "right after its session, as the standing reference.",
      "A word on the pre-reads: each one is a short refresher on what the process is and why we're "
      "modernizing it — nobody is expected to study them, and there's no homework here. If someone "
      "has ten minutes before their session, it's a helpful way to see the out-of-the-box goals "
      "we'll be working toward together; if not, we cover everything in the workshop. The data "
      "packs are where we'd love Connection to start early: the sooner real data is in the system, "
      "the sooner the demos you see are your demos.",
      "None of this needs to be figured out alone. If a spreadsheet asks a question your team "
      "isn't sure how to answer, that's normal — flag it and we'll work through it together in "
      "the workshop or a quick call.",
      "As a next step, let's get a 30-minute review meeting on the calendar to walk through this "
      "package, agree which workshops need which people, and set expectations on the data-pack "
      "timing. Let me know what works for your schedule, I can be flexible.",
      SIGN,
     ]),
    ("Drop_03_ITSM_Core", "Drop 3 — ITSM Core",
     "ITSM workshop materials — Incident, Problem, Change, and Catalog",
     [
      GREET,
      "The foundation work is in motion, so here is the package for the ITSM Core build — the heart "
      "of the engagement, covering Weeks 7–10. It contains pre-reads for Incident, Major Incident, "
      "Problem, Change (including the modernized CAB process), and Service Catalog, plus the "
      "process-decision packs where your process owners record how Connection wants each process "
      "to work. As always, each workshop's full deck arrives right after its session.",
      "These workshops are where your team shapes the platform most directly, so the right people in "
      "the room matters more than in any other stage. The pre-reads are there as a no-pressure "
      "refresher — what each process is, why we're modernizing it, and the out-of-the-box goals "
      "the session works toward. Reading them isn't required, but a ten-minute skim helps each "
      "process owner see the decisions coming their way. If any of those raise internal debate "
      "before the workshop, that's a good sign, not a problem — bring the debate with you and "
      "we'll resolve it together with the baseline as the starting point.",
      "Questions before then are always welcome, however small — a two-minute email now often saves "
      "a workshop hour later.",
      "As a next step, I'd like a 30-minute review meeting to walk through the package, confirm the "
      "workshop schedule and attendees, and set expectations for the process decisions ahead. "
      "Let me know what works for your schedule, I can be flexible.",
      SIGN,
     ]),
    ("Drop_04_Employee_Experience_and_Analytics", "Drop 4 — Employee Experience & Analytics",
     "Employee experience materials — Employee Center, Virtual Agent, and analytics",
     [
      GREET,
      "Here is the package for the employee-experience and analytics stage, Weeks 11–14 — the part "
      "of the project your end users will actually see and feel. It covers Employee Center, Virtual "
      "Agent and AI Search, Knowledge Management, Predictive Intelligence, Performance Analytics, and "
      "the HAM foundations, each with a pre-read and a decision pack (decks follow each session, "
      "as usual).",
      "This stage rewards a slightly wider audience: alongside your process owners, consider "
      "including the people who own internal communications and the employee experience — the "
      "Employee Center and Virtual Agent decisions land better with their voice in the room. The "
      "pre-reads are an optional, friendly refresher on what's being decided and why it matters "
      "for the experience goals — useful for anyone joining these sessions for the first time, "
      "but never required reading.",
      "As always, questions are welcome at any point — especially the “is it too late to ask about…” "
      "kind. It almost never is, and asking now is precisely how we keep it that way.",
      "As a next step, let's hold a 30-minute review meeting to walk through the package, confirm "
      "attendees for each session, and set expectations for what go-live will look like for your "
      "employees. Let me know what works for your schedule, I can be flexible.",
      SIGN,
     ]),
    ("Drop_05_Testing_GoLive_and_Handoff", "Drop 5 — Testing, Go-Live & Handoff",
     "The home stretch — UAT, go-live readiness, and handoff materials",
     [
      GREET,
      "We're entering the home stretch, and this final package covers everything from testing "
      "through ownership: the UAT Guidebook (written for first-time testers — genuinely, no prior "
      "experience needed), the end-to-end test scripts, the gated Go-Live Readiness Checklist we'll "
      "review together before cutover, the Cutover Runbook, and the knowledge-transfer set — the "
      "Administrator Guide, Train-the-Trainer Toolkit, and Operational Handoff Pack.",
      "Two things worth saying plainly. First, UAT is where your testers' honest feedback matters "
      "most — finding issues now is the system working, not failing, and the guidebook shows exactly "
      "how to log what they see. Second, the go/no-go decision is a joint one: the readiness "
      "checklist makes the criteria explicit so there are no surprises in that conversation.",
      "Your testers and admins will have questions as they get hands-on — please funnel them "
      "straight to us, however small. During this stage especially, fast answers are our job.",
      "As a next step, I'd like a 45-minute review meeting to walk through this package, set "
      "expectations for the UAT window and the go/no-go review, and confirm the knowledge-transfer "
      "schedule for your admin team. Let me know what works for your schedule, I can be flexible.",
      SIGN,
     ]),
]



# Per-drop distribution guidance — Neveena (Connection PM) is the primary recipient
# of every package; these lines tell her who gets what on her side and how they use it.
DIST = {
    "Drop_01_Initial_Package": (
        "A quick word on distribution — this first package is mostly governing documents, so no "
        "action is needed from your team until we work through them together:",
        ["For you: the Communication Plan, Sprint 0 checklist, project plan, and dependency "
         "tracker are your working set — we'll complete the contact roster and confirm dates "
         "together at the review meeting, then finalize these as our operating baseline.",
         "For your Executive Sponsor and leadership: the Client Onboarding Guide and the "
         "Document Roadmap are the two worth forwarding now — a ten-minute orientation to how "
         "the project runs and what arrives when.",
         "For process owners and SMEs: nothing needed yet. Their material starts arriving with "
         "Package 2, and each future email will tell you exactly who needs what."]),
    "Drop_02_Foundation_and_Data": (
        "Who needs what on your side:",
        ["Workshop attendees (IT leads, data and platform owners): forward each pre-read to the "
         "people attending that session — optional ten-minute refresher, nothing more.",
         "Data owners and your Technical Lead: the accelerator workbooks (users, locations, "
         "groups, service taxonomy, discovery scope, integrations) — the one set that benefits "
         "from an early start; we'll agree due dates at the review.",
         "For you and your Sponsor: the RACI matrix — confirm the ownership mapping matches "
         "your org before the workshops begin."]),
    "Drop_03_ITSM_Core": (
        "Who needs what on your side:",
        ["Each process owner: their own pre-read (Incident, Major Incident, Problem, Change, "
         "Service Catalog) — an optional preview of the decisions their session covers.",
         "Process owners with you: the process-decision packs — no need to fill these ahead; "
         "we complete them together in the workshops.",
         "For you: the workshop calendar coordination — this stage needs the right people in "
         "the room more than any other."]),
    "Drop_04_Employee_Experience_and_Analytics": (
        "Who needs what on your side:",
        ["Session attendees: their pre-reads — and for Employee Center and Virtual Agent, "
         "consider adding your internal communications and employee-experience voices.",
         "Service desk and knowledge owners: the Knowledge and analytics materials.",
         "For you: attendee confirmations, and start thinking about UAT tester names — "
         "Package 5 will need them."]),
    "Drop_05_Testing_GoLive_and_Handoff": (
        "Who needs what on your side:",
        ["Your UAT testers: the UAT Guidebook and end-to-end test scripts — written for "
         "first-timers, no prior experience needed.",
         "Your Technical Lead: the Cutover Runbook and Go-Live Readiness Checklist.",
         "Your platform admins and trainers: the Administrator Guide & KT plan and the "
         "Train-the-Trainer Toolkit — KT sessions get scheduled at the review.",
         "Your Executive Sponsor: the readiness checklist ahead of the joint go/no-go."]),
}

def base_meta(**over):
    m = dict(
        eyebrow="INTERNAL · STAGED ROLLOUT",
        title="Document Drop\nEmail Templates",
        subtitle="Ready-to-personalize cover emails for each staged document release to Connection",
        org="ECS Federal · ServiceNow Practice",
        audience="ECS Engagement Manager",
        companion_to="Staged_Rollout_Guide.xlsx · Connection Communication Plan",
        doc_id="INT-CONN-ROLL-01",
        version="1.0",
        status="Released",
        confidentiality="Internal Use Only · Confidential",
        running_header_label="Internal · Drop Email Templates",
    )
    m.update(over)
    return DocMeta(**m)


def write_email_body(doc, folder, subject, paragraphs):
    doc.para("Subject: " + subject, bold=True)
    intro, bullets = DIST.get(folder, (None, []))
    # closing block = everything from the "questions" paragraph onward; keep dist just before it
    n_close = 3 if folder != "Drop_01_Initial_Package" else 4
    head, tail = paragraphs[:-n_close], paragraphs[-n_close:]
    for p in head:
        doc.para(p)
    if intro:
        doc.para(intro)
        for b in bullets:
            doc.bullet(b)
    for p in tail:
        doc.para(p)


# ---- 1) Combined reference document (with cover + usage notes) ----
os.makedirs(KIT, exist_ok=True)
doc = EcsDocument(meta=base_meta(), logo_path=LOGO)
doc.add_cover_page()
doc.page_break()
doc.h1("How to Use These Templates", numbered=False)
doc.para(
    "One email per drop, in release order. Every package goes to Neveena, Connection's Project "
    "Manager and our primary document recipient — each email includes a distribution section "
    "telling her exactly who on her side gets what and how they'll use it, so internal routing "
    "is her call but never her guesswork. Trim anything that doesn't fit the moment. Three rules "
    "hold across every email: questions are always explicitly welcomed (no question is too small, "
    "and asking early is framed as helping the project); scheduling stays flexible — offer to "
    "work around their calendar rather than proposing a fixed date; and the next step is always "
    "a short review meeting to walk through the documents together and set expectations — we "
    "never drop documents and walk away."
)
doc.para(
    "Each drop's email also exists as a standalone file in Client_Drops/, named to match its zip "
    "(e.g., Drop_01_Initial_Package.zip pairs with Drop_01_Initial_Package_EMAIL.docx) — attach "
    "the zip, send the matching email text."
)
doc.callout(
    "The review meeting is the point. The documents support the conversation — the conversation "
    "is where alignment actually happens."
)
for folder, title, subject, paragraphs in EMAILS:
    doc.h1(title, numbered=True)
    write_email_body(doc, folder, subject, paragraphs)
out = os.path.join(KIT, "Drop_Email_Templates_INTERNAL.docx")
doc.save(out)
print(f"Saved: {out}")

# ---- 2) Per-drop standalone email docs, named to match the zips ----
os.makedirs(DROPS_DIR, exist_ok=True)
for folder, title, subject, paragraphs in EMAILS:
    d = EcsDocument(meta=base_meta(
        title=title.replace(" — ", "\n") + "\nCover Email",
        subtitle=f"Send this text with {folder}.zip — personalize [bracketed] fields first.",
        running_header_label=f"Internal · {title} Cover Email",
    ), logo_path=LOGO)
    # No cover page — this is a short copy-paste aid.
    d.h1(f"Email for {folder}.zip", numbered=False)
    write_email_body(d, folder, subject, paragraphs)
    d.callout(
        "Attach or link: " + folder + ".zip · After sending: book the review meeting within one "
        "week and log the release date in Staged_Rollout_Guide.xlsx."
    )
    p = os.path.join(DROPS_DIR, folder + "_EMAIL.docx")
    d.save(p)
    print(f"Saved: {p}")
