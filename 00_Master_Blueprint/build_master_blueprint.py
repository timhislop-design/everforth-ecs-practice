"""
Build ECS_OOTB_Collateral_Blueprint.docx from blueprint_catalog.json
using the canonical ecs_template module.

The JSON is treated as the source of truth for the Master Blueprint catalog.
Re-run any time the catalog is updated (e.g., status flips from Plan → Built).
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta, Brand

JSON_PATH = os.path.join(HERE, "blueprint_catalog.json")
OUT_PATH  = os.path.join(HERE, "ECS_OOTB_Collateral_Blueprint.docx")

with open(JSON_PATH) as f:
    data = json.load(f)

# ---------- Build cover meta from JSON top-level fields ----------
doc = EcsDocument(meta=DocMeta(
    eyebrow=data.get("label", "INTERNAL BLUEPRINT"),
    title=f"{data.get('title','ECS OOTB Practice')}\n{data.get('subtitle','Collateral Blueprint')}",
    subtitle=data.get("tagline", ""),
    audience="ECS Federal ServiceNow Practice — Practice Lead, Engagement Managers, Solution Architects, Process Consultants",
    companion_to="ECS Internal Governance Operating Guide · Manager's Trust-But-Verify Playbook · OOTB Delivery Playbook",
    doc_id="MB-00",
    version="1.0",
    status="Living Document",
    running_header_label=f"Internal · {data.get('subtitle','Collateral Blueprint')}",
))

doc.add_cover_page()

# ---------- Heuristic for picking column widths ----------
# Total content width = 9.36 inches at standard margins.
PREF_WIDTHS = {
    2: [3.5, 5.86],
    3: [1.8, 4.0, 3.56],
    4: [1.2, 3.4, 1.5, 3.26],
    5: [1.2, 3.4, 1.2, 1.4, 2.16],
    6: [1.0, 2.4, 1.0, 1.4, 1.6, 1.96],
}

def col_widths_for(n_cols, headers):
    # Special-case known table shapes by header text
    if headers == ["ID", "Artifact", "Audience", "Format", "Build Status"]:
        return [1.0, 4.4, 1.2, 0.96, 1.8]
    if headers == ["ID", "Pack", "Audience", "Status"]:
        return [1.0, 5.5, 1.2, 1.66]
    if headers == ["#", "Artifact", "Why Now", "Output Folder"]:
        return [0.4, 3.0, 4.0, 1.96]
    if headers == ["Existing Document", "Role in Library", "Maintenance"]:
        return [2.8, 3.5, 3.06]
    return PREF_WIDTHS.get(n_cols, [9.36 / n_cols] * n_cols)

# ---------- Walk JSON sections ----------
# A simple rule for page breaks: insert one before each H1 except the very first.
first_h1_seen = False

# Force a page break out of the cover into content
doc.page_break()

for sec in data["sections"]:
    kind = sec.get("kind")
    if kind == "h1":
        if first_h1_seen:
            doc.page_break()
        else:
            first_h1_seen = True
        doc.h1(sec["text"], numbered=False)  # The blueprint uses natural section names, not numeric
    elif kind == "h2":
        doc.h2(sec["text"])
    elif kind == "h3":
        doc.h3(sec["text"])
    elif kind == "prose":
        for paragraph in sec.get("paragraphs", []):
            doc.para(paragraph)
    elif kind == "table":
        headers = sec.get("columns", [])
        rows    = sec.get("rows", [])
        if not headers:
            continue
        widths = col_widths_for(len(headers), headers)
        doc.table(headers=headers, rows=[[str(c) for c in r] for r in rows],
                  col_widths_in=widths)
    elif kind == "bullet":
        doc.bullet(sec.get("text", ""))
    elif kind == "callout":
        doc.callout(sec.get("text", ""))
    else:
        # Unknown kind — render as plain prose so nothing is silently lost
        txt = sec.get("text") or "\n".join(sec.get("paragraphs", []))
        if txt:
            doc.para(txt)

# Closing callout
doc.callout(
    "This Blueprint is a living document. As artifacts move from Plan → Next → Built, update "
    "blueprint_catalog.json directly, then re-run build_master_blueprint.py to regenerate this .docx. "
    "The JSON is the source of truth; this document is the rendered view."
)

doc.save(OUT_PATH)
print(f"Saved: {OUT_PATH}")
