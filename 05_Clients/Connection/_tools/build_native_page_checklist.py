# -*- coding: utf-8 -*-
"""Build: Connection - Native SharePoint Page PASTE CHECKLIST (INTERNAL).
Per-role copy/paste tables (checkbox | title | URL) generated from the navigator registry."""
import sys, os, re, json
from urllib.parse import quote
REPO="/sessions/eager-epic-davinci/mnt/everforth-ecs-practice"
sys.path.insert(0, os.path.join(REPO,"03_Shared","00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta
LOGO=os.path.join(REPO,"00_Master_Blueprint","assets","everforth_logo.png")
OUT=os.path.join(REPO,"05_Clients","Connection","Connection_Native_Page_PASTE_Checklist.docx")

nav=open(os.path.join(REPO,"06_Client_Upload/Connection/00_START_HERE/Connection_Execution_Navigator.html"),encoding="utf-8").read()
ROLES=json.loads(re.search(r"var ROLES=(\[.*?\]);",nav,re.S).group(1))
A=json.loads(re.search(r"var A=(\[.*?\]);",nav,re.S).group(1))
HOST="https://itecsfederal.sharepoint.com"
SR="/teams/MissionSolutions/ISM/BD/Accounts/Commercial/Connection"
FORMS=HOST+"/teams/MissionSolutions/ISM/BD/Forms/AllItems.aspx?id="
def url_for(p): return (FORMS+quote(SR+"/"+p[:-1])) if p.endswith("/") else HOST+SR+"/"+p

d=EcsDocument(meta=DocMeta(
 eyebrow="INTERNAL - SHAREPOINT PAGE PASTE CHECKLIST",
 title="Connection Execution Library\nNative Page - Paste Checklist",
 subtitle="Build the role-based page by hand - check off each link as you paste it",
 org="ECS Federal - ServiceNow Practice",
 audience="Tim Hislop / page builder - internal",
 companion_to="Native SharePoint Page Build Guide - Connection_SharePoint_LinkMap.xlsx",
 doc_id="INT-CONN-SPC-01", version="1.0", status="Draft",
 running_header_label="Internal - SharePoint Page Paste Checklist"), logo_path=LOGO)
d.add_cover_page(); d.page_break()

d.h1("How to Use This", numbered=False)
d.para("Everything here is done by hand in the SharePoint browser UI on your work machine - no scripts, no admin tools. Do the one-time Page Setup, then work down each role section: add a collapsible section, drop in a Quick Links web part, and paste the Title and URL for each row. Tick the box as you go. You can publish after the ECS roles and add the client roles later - the page is editable anytime.")

d.h1("Page Setup (do once)", numbered=True)
d.bullet("Team site -> + New -> Page -> Blank. Name it: Connection Execution Library.")
d.bullet("Add a Text web part at top: a heading plus the snapshot line - Backlog 196 | 0 open gaps | 18 of 27 deliverables | 18 workshops | 17 dependencies | and 'Find your role below.'")
d.bullet("For each role below: hover the left edge, click the circled + to add a Section; open its settings (pencil) and turn on 'Make this section collapsible'; name it the role.")
d.bullet("Inside the section, click + -> Quick links. For each row in that role's table: + Add link -> From a link -> paste the URL -> set the display text to the Title -> Add.")
d.bullet("When done, click Publish (top right). Copy the page URL and send it to the team.")

d.h1("Optional - Instant Full-Library Index", numbered=True)
d.para("If you want the entire catalog on the page with zero manual links, add one Highlighted Content web part and scope it to this document library (the Connection folder). It auto-lists every document and needs no paste. Use it as a catch-all beneath the curated role sections.")

d.h1("Role Sections - Paste These", numbered=True)
d.para("Tables are grouped by role and ordered ECS team first, then Connection (client). 'Title' is the display text; 'URL' is what you paste under From a link.")

aud_label={"ecs":"ECS team","client":"Connection (client)"}
for rid,label,aud in ROLES:
    items=[a for a in A if rid in a[4]]
    if not items: continue
    d.h2(f"{label}  -  {aud_label[aud]}")
    d.para(f"Add a collapsible section named \"{label}\", add a Quick Links web part, then paste these {len(items)} links:")
    rows=[["[  ]", a[0], url_for(a[3])] for a in items]
    d.table(headers=["Done","Title (paste as display text)","URL (paste under From a link)"], rows=rows)

d.callout("Build the ECS roles first and Publish - you'll have a working page in minutes. Add the client roles in a second pass. If the library ever moves, send me the new path and I regenerate every URL.")
d.save(OUT)
print("Saved:", OUT, "| total link rows:", sum(1 for r in ROLES for a in A if r[0] in a[4]))
