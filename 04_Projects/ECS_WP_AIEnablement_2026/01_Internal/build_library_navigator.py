"""
build_library_navigator.py — ECS Practice Library Navigator generator
Project: 04_Projects/ECS_WP_AIEnablement_2026

Scans the practice library (00_Master_Blueprint, 01_Internal, 02_Client,
03_Shared), classifies every artifact by lifecycle stage and role, merges the
review verdicts from library_review_status.json, and emits a self-contained
index.html navigator at the repo root. Stage/role is deliberately
methodology-neutral: engagements assemble their kit from these shelves based on
the RFP's objectives, whatever the delivery approach.

Usage (from anywhere inside the repo):
    python build_library_navigator.py                       # relative links (local / GitHub)
    python build_library_navigator.py --sharepoint https://ecsfederal.sharepoint.com/sites/ServiceNowPractice/Shared%20Documents
        -> also writes index_sharepoint.html with absolute links under that base URL
    python build_library_navigator.py --filelist paths.txt  # build from a path list instead of scanning

Review workflow: edit library_review_status.json (stage status + per-artifact
verdicts), re-run this script, commit both. The navigator is generated output —
never hand-edit index.html.
"""
import os, sys, json, html, urllib.parse

# ---------------------------------------------------------------- repo root
def find_repo_root(start):
    d = os.path.abspath(start)
    for _ in range(8):
        if os.path.isdir(os.path.join(d, "00_Master_Blueprint")):
            return d
        d = os.path.dirname(d)
    return None

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = find_repo_root(HERE) or find_repo_root(os.getcwd())

# ---------------------------------------------------------------- taxonomy
ROLES = [
    ("bd", "Capture & Sales Lead", "ecs"),
    ("pl", "Practice Lead", "ecs"),
    ("em", "Engagement Manager / Project Lead", "ecs"),
    ("sa", "Solution Architect", "ecs"),
    ("pc", "Process Consultant / BA (Scrum Master hat)", "ecs"),
    ("tc", "Technical Consultant", "ecs"),
]
STAGES = [
    ("capture",   "Capture & Pre-Sales",      "Phase 0"),
    ("proposal",  "Proposal & SOW",           "Phase 2"),
    ("sprint0",   "Award & Sprint 0",         "Phase 3"),
    ("delivery",  "Delivery (Sprints 1\u20136)", "Phase 4"),
    ("verify",    "Verification & PMO",       "Phase 4"),
    ("close",     "Closeout & Hypercare",     "Phase 5"),
    ("governance","Practice Governance",      "Phase 0"),
]
VERDICTS = {
    "proposed": ("PROPOSED", "#94A3B8"),
    "ratified": ("RATIFIED", "#0D9488"),
    "update":   ("NEEDS UPDATE", "#B45309"),
    "replace":  ("REPLACE", "#B91C1C"),
    "gap":      ("GAP", "#B91C1C"),
}

# Rules: (path prefix, stage(s), roles, pill) — first match wins. Overrides by filename below.
RULES = [
    ("01_Internal/01_Consultant_Handbook",            ["governance"], ["pl","em","sa","pc","tc"]),
    ("01_Internal/02_Sales_and_PreEngagement",        ["capture"],    ["bd","pl","em"]),
    ("01_Internal/03_Sprint0_Setup",                  ["sprint0"],    ["em","sa","pl"]),
    ("01_Internal/04_Per_Sprint_Facilitator_Guides",  ["delivery"],   ["pc","sa"]),
    ("01_Internal/05_Discipline_How-To_Guides",       ["delivery"],   ["tc","sa"]),
    ("01_Internal/06_Adopt_vs_Reengineer_Cheatsheets",["delivery"],   ["sa","pc"]),
    ("01_Internal/07_Demo_Scripts",                   ["delivery"],   ["pc","tc"]),
    ("01_Internal/08_UAT_Test_Packs",                 ["verify"],     ["pc","tc","em"]),
    ("01_Internal/09_Trust_but_Verify_Management",    ["verify"],     ["em","pl"]),
    ("01_Internal/10_Delivery_App_Blueprint",         ["governance"], ["pl","em","sa"]),
    ("01_Internal/10_Lessons_Learned",                ["close"],      ["em","pl"]),
    ("01_Internal/11_Practice_Onboarding",            ["governance"], ["pl","em","sa","pc","tc"]),
    ("01_Internal/11_SOW_Draft",                      ["proposal"],   ["bd","em","pl"]),
    ("02_Client/01_Engagement_Overview",              ["sprint0"],    ["em","pc"]),
    ("02_Client/02_Sprint0_Customer_Readiness",       ["sprint0"],    ["em","pc"]),
    ("02_Client/03_Per_Sprint_Customer_Briefs",       ["delivery"],   ["em","pc"]),
    ("02_Client/04_Decision_Topic_Guides",            ["delivery"],   ["pc","sa"]),
    ("02_Client/05_Workshop_Pre-Reads",               ["delivery"],   ["pc","sa"]),
    ("02_Client/06_UAT_Execution",                    ["verify"],     ["pc","em"]),
    ("02_Client/07_Closeout_and_Hypercare",           ["close"],      ["em"]),
    ("03_Shared/01_Accelerator_Packs",                ["delivery"],   ["tc","sa"]),
    ("03_Shared/02_Project_Plans",                    ["sprint0"],    ["em"]),
    ("03_Shared/04_Sprint_Workbooks",                 ["delivery"],   ["sa","pc"]),
    ("03_Shared/05_Workshop_Presentations",           ["delivery"],   ["pc","sa"]),
    ("00_Master_Blueprint",                           ["governance"], ["pl","em"]),
]
# Filename-level overrides: substring -> (stages, roles)
OVERRIDES = {
    "ECS_SOW_Scope_Classification": (["proposal"], ["bd","em","pl"]),
    "INT-SP-04_SOW_Scope_Checklist": (["proposal"], ["bd","em","pl"]),
    "INT-SP-06_Proposal_Narrative_Blocks": (["proposal"], ["bd","pl"]),
    "INT-SP-07_Engagement_Pricing_Framework": (["proposal"], ["bd","pl"]),
    "ECS_Internal_Governance_Operating_Guide": (["governance"], ["pl","em","sa","pc","tc"]),
    "Foundation_Accelerator_Pack": (["sprint0","delivery"], ["tc","sa"]),
    "ECS_JIT_Baseline_Stories": (["delivery"], ["sa","pc","tc"]),
    "ECS_18Week_Baseline_Project_Plan": (["sprint0","delivery"], ["em"]),
}
EXT_PILL = {".docx":"doc", ".pptx":"deck", ".xlsx":"sheet", ".mpp":"sheet", ".dotx":"doc"}
SKIP_DIRS = {"versions", "__pycache__", "assets", "00_Templates_and_Branding"}
EXTS = (".docx", ".pptx", ".xlsx", ".mpp")

def collect_paths():
    paths = []
    for top in ("00_Master_Blueprint","01_Internal","02_Client","03_Shared"):
        base = os.path.join(ROOT, top)
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for f in filenames:
                if f.lower().endswith(EXTS) and not f.startswith("~$"):
                    paths.append(os.path.relpath(os.path.join(dirpath, f), ROOT).replace(os.sep, "/"))
    return sorted(paths)

def load_filelist(fp):
    with open(fp) as fh:
        return sorted(l.strip().replace("\\","/") for l in fh
                      if l.strip() and l.strip().lower().endswith(EXTS)
                      and "/versions/" not in l and "00_Templates_and_Branding" not in l
                      and not os.path.basename(l.strip()).startswith("~$"))

def classify(path):
    stages, roles = ["governance"], ["pl"]
    for prefix, st, rl in RULES:
        if path.startswith(prefix):
            stages, roles = list(st), list(rl)
            break
    for key, (st, rl) in OVERRIDES.items():
        if key in path:
            stages, roles = list(st), list(rl)
            break
    return stages, roles

def titleize(path):
    name = os.path.splitext(os.path.basename(path))[0]
    for suf in ("_INTERNAL","_CLIENT"):
        if name.endswith(suf): name = name[:-len(suf)]
    return name.replace("_"," ").replace("-"," \u2013 ", 0) or name

def build_items(paths, status):
    """Accelerator packs collapse to one card per pack; everything else is per-file."""
    items, seen_packs = [], set()
    verdicts = status.get("artifacts", {})
    for p in paths:
        parts = p.split("/")
        if p.startswith("03_Shared/01_Accelerator_Packs/") and len(parts) >= 4:
            pack = parts[2]
            if pack in seen_packs: continue
            seen_packs.add(pack)
            pack_dir = "/".join(parts[:3])
            stages, roles = classify(p)
            items.append(dict(title=pack.replace("_"," "), pill="pack", path=pack_dir + "/",
                              cat="Accelerator Pack (workbook set)", stages=stages, roles=roles,
                              audience="shared", verdict=verdicts.get(pack_dir, "proposed")))
            continue
        stages, roles = classify(p)
        aud = "client" if ("02_Client/" in p or "_CLIENT" in p) else ("shared" if p.startswith("03_Shared") else "internal")
        cat = parts[1].replace("_"," ") if len(parts) > 2 else parts[0].replace("_"," ")
        items.append(dict(title=titleize(p), pill=EXT_PILL.get(os.path.splitext(p)[1].lower(),"doc"),
                          path=p, cat=cat, stages=stages, roles=roles, audience=aud,
                          verdict=verdicts.get(p, "proposed")))
    return items

def render(items, status, base_url=None):
    counts = {k: 0 for k in VERDICTS}
    for it in items: counts[it["verdict"]] = counts.get(it["verdict"], 0) + 1
    stages_done = sum(1 for s,_,_ in STAGES if status.get("stages",{}).get(s,{}).get("status")=="complete")
    cur = html.escape(status.get("current_phase","Phase 0 \u2014 Foundations"))
    def link(p):
        if base_url:
            return base_url.rstrip("/") + "/" + urllib.parse.quote(p)
        return p
    data = [[it["title"], it["pill"], it["cat"], link(it["path"]), it["roles"], it["stages"], it["audience"], it["verdict"]] for it in items]
    stage_status = {s: status.get("stages",{}).get(s,{}).get("status","not_started") for s,_,_ in STAGES}
    return """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>ECS ServiceNow Practice \u2014 Library Navigator</title>
<style>
:root{--navy:#0B1F3A;--teal:#14B8A6;--tealdk:#0D9488;--blue:#2E74B5;--slate:#475569;--bg:#F7F9FC;--card:#fff;--bd:#E2E8F0;--amber:#B45309;--red:#B91C1C}
*{box-sizing:border-box} body{margin:0;font-family:Calibri,Segoe UI,Arial,sans-serif;color:#1A1A1A;background:var(--bg);line-height:1.5}
.wrap{max-width:1120px;margin:0 auto;padding:28px 22px}
h1{color:var(--navy);font-size:26px;margin:0 0 4px} .sub{color:var(--slate);font-size:14px;margin:0 0 18px}
.plan{background:#fff;border:1px solid var(--bd);border-left:4px solid var(--teal);border-radius:10px;padding:10px 16px;margin-bottom:16px;font-size:13px;color:var(--slate)}
.plan b{color:var(--navy)}
.flare{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin-bottom:18px}
.metric{background:#fff;border:1px solid var(--bd);border-radius:10px;padding:12px 16px}
.metric .l{font-size:12px;color:var(--slate)} .metric .n{font-size:24px;font-weight:bold;color:var(--navy)} .metric .s{font-size:11px;color:#94A3B8}
.controls{display:flex;gap:14px;flex-wrap:wrap;margin-bottom:12px} .controls>div{flex:1;min-width:180px}
label{display:block;font-size:12px;color:var(--slate);margin-bottom:5px} select{width:100%;padding:9px 10px;border:1px solid var(--bd);border-radius:8px;font-size:14px;background:#fff}
.count{font-size:13px;color:var(--slate);margin:6px 0 12px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(255px,1fr));gap:12px}
.c{background:var(--card);border:1px solid var(--bd);border-radius:12px;padding:13px 15px;border-left:4px solid var(--teal)}
.c.client{border-left-color:var(--blue)}
.c .h{display:flex;align-items:center;gap:7px;margin-bottom:5px;flex-wrap:wrap}
.c .pill{font-size:10px;font-weight:bold;letter-spacing:.5px;padding:2px 7px;border-radius:5px;color:#fff;background:var(--tealdk)}
.pill.sheet{background:var(--blue)} .pill.deck{background:var(--navy)} .pill.pack{background:var(--amber)}
.c a{font-weight:bold;font-size:14px;color:var(--navy);text-decoration:none} .c a:hover{text-decoration:underline}
.c .p{font-size:12px;color:var(--slate)}
.v{font-size:9px;font-weight:bold;letter-spacing:.5px;padding:2px 6px;border-radius:4px;color:#fff;margin-left:auto}
.foot{margin-top:24px;font-size:11px;color:#94A3B8}
.legend{font-size:12px;color:var(--slate);margin-bottom:14px} .legend b{color:var(--tealdk)} .legend .cl{color:var(--blue)}
.stagebar{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:16px}
.st{font-size:11px;padding:4px 10px;border-radius:14px;border:1px solid var(--bd);background:#fff;color:var(--slate)}
.st.complete{background:var(--tealdk);color:#fff;border-color:var(--tealdk)}
.st.in_review{background:#FEF3C7;border-color:var(--amber);color:var(--amber)}
</style></head><body><div class="wrap">
<h1>ECS ServiceNow Practice \u2014 Library Navigator</h1>
<p class="sub">Every artifact in the practice library, by role and lifecycle stage. Pull what fits the engagement \u2014 kits are assembled per the RFP's objectives, not one fixed delivery model. This is the proposed baseline: verdicts flip as each stage's team review completes (AI Enablement Guidebook \u00a710).</p>
<div class="plan"><b>Project plan now: __CUR__.</b> &nbsp;Each stage below is reviewed in the phase shown on its chip \u2014 ratify, update, or replace before we automate on top of it.</div>
<div class="flare">
<div class="metric"><div class="l">Artifacts</div><div class="n">__TOTAL__</div><div class="s">indexed in library</div></div>
<div class="metric"><div class="l">Ratified</div><div class="n">__RAT__</div><div class="s">team-reviewed &amp; accepted</div></div>
<div class="metric"><div class="l">Proposed</div><div class="n">__PROP__</div><div class="s">awaiting review</div></div>
<div class="metric"><div class="l">Needs work</div><div class="n">__WORK__</div><div class="s">update / replace / gap</div></div>
<div class="metric"><div class="l">Stage reviews</div><div class="n">__STG__ / 7</div><div class="s">complete</div></div>
</div>
<div class="stagebar" id="stagebar"></div>
<div class="legend"><b>&#9632; Internal / shared</b> &nbsp; <span class="cl">&#9632; Client-facing</span> &nbsp;|&nbsp; verdicts live in <code>library_review_status.json</code> \u2014 update it and re-run the generator.</div>
<div class="controls">
<div><label for="role">Your role</label><select id="role"></select></div>
<div><label for="phase">Lifecycle stage</label><select id="phase"></select></div>
<div><label for="verdict">Review status</label><select id="verdict"></select></div>
</div>
<div class="count" id="count"></div>
<div class="grid" id="cards"></div>
<p class="foot">Generated by 04_Projects/ECS_WP_AIEnablement_2026/01_Internal/build_library_navigator.py \u2014 do not hand-edit. Source of truth for build status: 00_Master_Blueprint/blueprint_catalog.json. Regenerate with --sharepoint &lt;base-url&gt; after migration to the ECS SharePoint site.</p>
</div>
<script>
var ROLES=__ROLES__;
var STAGES=__STAGES__;
var STAGE_STATUS=__STAGE_STATUS__;
var VER={proposed:["PROPOSED","#94A3B8"],ratified:["RATIFIED","#0D9488"],update:["NEEDS UPDATE","#B45309"],replace:["REPLACE","#B91C1C"],gap:["GAP","#B91C1C"]};
var A=__DATA__;
var rs=document.getElementById('role'),ps=document.getElementById('phase'),vs=document.getElementById('verdict'),cards=document.getElementById('cards'),count=document.getElementById('count'),sb=document.getElementById('stagebar');
var o=document.createElement('option');o.value='all';o.textContent='All roles';rs.appendChild(o);
ROLES.forEach(function(r){var x=document.createElement('option');x.value=r[0];x.textContent=r[1];rs.appendChild(x)});
var p0=document.createElement('option');p0.value='all';p0.textContent='All stages';ps.appendChild(p0);
STAGES.forEach(function(p){var x=document.createElement('option');x.value=p[0];x.textContent=p[1]+' \u00b7 review in '+p[2];ps.appendChild(x)});
[['all','All'],['proposed','Proposed (awaiting review)'],['ratified','Ratified'],['update','Needs update'],['replace','Replace'],['gap','Gap']].forEach(function(v){var x=document.createElement('option');x.value=v[0];x.textContent=v[1];vs.appendChild(x)});
STAGES.forEach(function(s){var d=document.createElement('span');var st=STAGE_STATUS[s[0]]||'not_started';d.className='st '+st;d.textContent=s[1]+' \u00b7 '+s[2]+(st==='complete'?' \u2713':st==='in_review'?' \u00b7 reviewing':'');sb.appendChild(d)});
function render(){var r=rs.value,ph=ps.value,vv=vs.value;
var list=A.filter(function(a){return (r==='all'||a[4].indexOf(r)>-1)&&(ph==='all'||a[5].indexOf(ph)>-1)&&(vv==='all'||a[7]===vv)});
count.textContent=list.length+' artifact'+(list.length===1?'':'s')+' shown';
cards.innerHTML='';
if(!list.length){cards.innerHTML='<div style="color:#475569;font-size:14px">No artifacts match these filters.</div>';return}
list.forEach(function(a){var d=document.createElement('div');d.className='c'+(a[6]==='client'?' client':'');
var v=VER[a[7]]||VER.proposed;
d.innerHTML='<div class="h"><span class="pill '+a[1]+'">'+a[1].toUpperCase()+'</span><a href="'+a[3]+'">'+a[0]+'</a><span class="v" style="background:'+v[1]+'">'+v[0]+'</span></div><div class="p">'+a[2]+'</div>';
cards.appendChild(d)})}
rs.value='all';ps.value='all';vs.value='all';rs.onchange=render;ps.onchange=render;vs.onchange=render;render();
</script></body></html>""" \
    .replace("__CUR__", cur) \
    .replace("__TOTAL__", str(len(items))) \
    .replace("__RAT__", str(counts.get("ratified",0))) \
    .replace("__PROP__", str(counts.get("proposed",0))) \
    .replace("__WORK__", str(counts.get("update",0)+counts.get("replace",0)+counts.get("gap",0))) \
    .replace("__STG__", str(stages_done)) \
    .replace("__ROLES__", json.dumps([[r[0],r[1]] for r in ROLES])) \
    .replace("__STAGES__", json.dumps([[s[0],s[1],s[2]] for s in STAGES])) \
    .replace("__STAGE_STATUS__", json.dumps(stage_status)) \
    .replace("__DATA__", json.dumps(data))

def main():
    global ROOT
    args = sys.argv[1:]
    filelist = None; base_url = None; outdir = None
    while args:
        a = args.pop(0)
        if a == "--filelist": filelist = args.pop(0)
        elif a == "--sharepoint": base_url = args.pop(0)
        elif a == "--out": outdir = args.pop(0)
    status_path = os.path.join(HERE, "library_review_status.json")
    status = json.load(open(status_path)) if os.path.exists(status_path) else {}
    paths = load_filelist(filelist) if filelist else collect_paths()
    if not paths:
        sys.exit("No library files found — run from inside the repo or pass --filelist.")
    items = build_items(paths, status)
    outdir = outdir or ROOT or HERE
    out = os.path.join(outdir, "index.html")
    open(out, "w", encoding="utf-8").write(render(items, status))
    print("Wrote", out, "(%d artifacts)" % len(items))
    if base_url:
        out2 = os.path.join(outdir, "index_sharepoint.html")
        open(out2, "w", encoding="utf-8").write(render(items, status, base_url))
        print("Wrote", out2)

if __name__ == "__main__":
    main()
