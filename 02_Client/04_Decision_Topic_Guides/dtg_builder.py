"""
dtg_builder.py — Shared renderer for all CLT-DT Decision Topic Guides.
Import this from each per-guide build script.

Each guide dict schema:
  doc_id, filename, short_name, title, subtitle, audience, companion_to,
  how_to_use_paras (list of str),
  why_matters (list of {"h2": str, "body": str}),
  signals (list of {"h2": str, "body": str}),
  decisions (list of {"label": str, "body": str, "questions": list[str], "landing": str}),
  good_rows (list of [str, str])  — "What good looks like" vs "Warning sign" table,
  patterns (list of {"label": str, "body": str}),
  workshop_para: str,
  need_bullets: list[str],
  questions: list[str],
  xrefs (list of [str, str, str])  — [Document, Why relevant, Where to find it]
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

FOOTER = "ECS Federal · ServiceNow Practice  ·  Confidential"
CONF   = "Confidential — prepared for the recipient and their organization"


def build_dtg(d: dict) -> str:
    doc = EcsDocument(meta=DocMeta(
        eyebrow=f"DECISION TOPIC GUIDE  ·  {d['short_name'].upper()}",
        title=d["title"],
        subtitle=d["subtitle"],
        audience=d["audience"],
        companion_to=d.get("companion_to", ""),
        doc_id=d["doc_id"],
        version="1.0",
        status="Released",
        confidentiality=CONF,
        running_header_label=f"Decision Topic Guide  ·  {d['short_name']}",
        footer_left=FOOTER,
    ))
    doc.add_cover_page()
    doc.add_page_break()

    # ── Section 0: How to Use ─────────────────────────────────────────────────
    doc.h1("How to Use This Guide", numbered=False)
    for p in d["how_to_use_paras"]:
        doc.para(p)
    doc.callout(
        "The customer is the decider in every section that follows. We frame the decisions, "
        "share what we have seen in similar engagements, and offer recommendations where we "
        "have strong observations. Where you land is your call, and we will partner with you "
        "to implement it."
    )

    # ── Section 1: Why Now ────────────────────────────────────────────────────
    doc.h1(f"Why {d['short_name']} Matters Now")
    for item in d["why_matters"]:
        doc.h2(item["h2"])
        doc.para(item["body"])

    doc.add_page_break()

    # ── Section 2: Signals ────────────────────────────────────────────────────
    doc.h1(f"The Signals That {d['signal_subject']} Needs Work")
    doc.para(
        "You may already sense that something has drifted. The signals below show up "
        "consistently across customers in similar positions. None of them mean the current "
        "state is broken — they mean it has grown into a shape that no longer fits the work "
        "it is being asked to do."
    )
    for s in d["signals"]:
        doc.h2(s["h2"])
        doc.para(s["body"])

    doc.add_page_break()

    # ── Section 3: The Four Decisions ─────────────────────────────────────────
    doc.h1("The Four Decisions")
    doc.para(
        "These are the decisions your team will make in the workshop. They are framed here "
        "with the questions they raise, the trade-offs to weigh, and where we typically see "
        "customers land. The point is not to bring you to our answer — it is to bring you "
        "to your answer with the full picture in view."
    )
    for i, dec in enumerate(d["decisions"], 1):
        doc.h2(f"Decision {i} — {dec['label']}")
        doc.para(dec["body"])
        if dec.get("questions"):
            doc.para("Questions to weigh:", bold=True, space_after=2)
            for q in dec["questions"]:
                doc.bullet(q)
        if dec.get("landing"):
            doc.para(dec["landing"], italic=True, space_before=4)

    doc.add_page_break()

    # ── Section 4: What Good Looks Like ──────────────────────────────────────
    doc.h1("What Good Looks Like")
    doc.para(
        "Good is not a single configuration. It is a set of properties that, together, "
        "signal a healthy and sustainable design. The table below contrasts what we aim for "
        "with the warning signs that suggest a design needs revisiting."
    )
    doc.table(
        headers=["What good looks like", "Warning sign"],
        rows=d["good_rows"],
        col_widths_in=[3.2, 3.2],
    )

    # ── Section 5: Common Patterns ────────────────────────────────────────────
    doc.h1("Common Patterns We Have Seen")
    doc.para(
        "These de-identified examples illustrate how different organizations have approached "
        "this set of decisions. Names and identifying details have been changed."
    )
    for pat in d["patterns"]:
        doc.h2(pat["label"])
        doc.para(pat["body"])

    doc.add_page_break()

    # ── Section 6: How We Will Workshop This ──────────────────────────────────
    doc.h1("How We Will Workshop This Together")
    doc.para(d["workshop_para"])

    # ── Section 7: What We Need ───────────────────────────────────────────────
    doc.h1("What We Will Need from Your Team")
    doc.para(
        "You do not need to prepare formal reports or pull data from every system. "
        "The items below help us move faster and surface the right context in the workshop."
    )
    for b in d["need_bullets"]:
        doc.bullet(b)

    # ── Section 8: Questions to Consider ──────────────────────────────────────
    doc.h1("Questions to Consider Before Our Session")
    doc.para(
        "Bring whatever you have. These are prompts for reflection, not prerequisites. "
        "The workshop is where we work through the answers together."
    )
    for q in d["questions"]:
        doc.bullet(q)

    # ── Section 9: Cross-References ───────────────────────────────────────────
    doc.h1("Cross-References and Next Steps")
    doc.para(
        "This guide sits within a broader set of client materials. The table below "
        "identifies the most relevant companions."
    )
    doc.table(
        headers=["Document", "Why relevant", "Where to find it"],
        rows=d["xrefs"],
        col_widths_in=[2.5, 4.0, 2.06],
    )

    out = os.path.join(HERE, d["filename"])
    doc.save(out)
    print(f"  ✓  {d['doc_id']}  →  {d['filename']}")
    return out
