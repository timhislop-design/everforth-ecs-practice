# -*- coding: utf-8 -*-
"""Build: Connection - Native SharePoint Page Build Guide (INTERNAL)."""
import sys, os
REPO="/sessions/eager-epic-davinci/mnt/everforth-ecs-practice"
sys.path.insert(0, os.path.join(REPO,"03_Shared","00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta
LOGO=os.path.join(REPO,"00_Master_Blueprint","assets","everforth_logo.png")
OUT=os.path.join(REPO,"05_Clients","Connection","Connection_Native_SharePoint_Page_Build_Guide.docx")

d=EcsDocument(meta=DocMeta(
 eyebrow="INTERNAL - SHAREPOINT PAGE BUILD GUIDE",
 title="Connection Execution Library\nNative SharePoint Page - Build Guide",
 subtitle="The role-based navigator as a real SharePoint page - no sandbox, no Sync",
 org="ECS Federal - ServiceNow Practice",
 audience="Tim Hislop / SharePoint page owner - internal",
 companion_to="Connection_SharePoint_LinkMap.xlsx (the link source)",
 doc_id="INT-CONN-SPB-01", version="1.0", status="Draft",
 running_header_label="Internal - SharePoint Page Build Guide"), logo_path=LOGO)
d.add_cover_page(); d.page_break()

d.h1("Why a Native Page", numbered=False)
d.para("SharePoint renders an uploaded HTML file inside a sandboxed document preview - scripts run, but link clicks are blocked, so the cards can't open anything. A native SharePoint page is not sandboxed: links are first-class, permissions are automatic, and nobody has to Sync. This guide rebuilds the role-based navigator as a modern SharePoint page using the built-in Quick Links web part. Every link you need is in Connection_SharePoint_LinkMap.xlsx (tab: By Role).")
d.callout("Until this page is built, the working path is Sync: open the navigator from the synced library folder in File Explorer and the cards click through normally.")

d.h1("What You Need", numbered=True)
d.bullet("Edit rights on the team SharePoint site (to create a page).")
d.bullet("Connection_SharePoint_LinkMap.xlsx open beside you - the 'By Role' tab lists each role with its artifacts and SharePoint URLs.")
d.bullet("15-20 minutes. The links are pre-built; this is mostly paste.")

d.h1("Build Steps", numbered=True)
d.bullet("On the site, choose New -> Page -> blank, name it 'Connection Execution Library'.")
d.bullet("Add a Text web part at the top: title, the status snapshot (Backlog 196, 0 gaps, 18/27 deliverables, 18 workshops, 17 dependencies), and a one-line 'find your role below'.")
d.bullet("Add a collapsible Section for each role (or two big sections - ECS team and Connection client - with a Quick Links web part per role inside). Twelve roles total: 5 ECS, 7 client.")
d.bullet("In each role's Quick Links web part, click Add link -> paste the SharePoint URL and the Artifact name from the matching rows in the By Role tab. Repeat for that role's artifacts.")
d.bullet("Set Quick Links layout to 'List' or 'Compact' for dense lists; 'Button' for short ones.")
d.bullet("Optional: add a Highlighted Content web part scoped to the Connection library so the full catalog is one click away.")
d.bullet("Publish. Then use Share / page permissions to scope who sees it (inherits the site, or restrict to your group).")

d.h1("Tips", numbered=True)
d.bullet("The By Role tab is sorted by audience then role - work top to bottom and you build the page in order.")
d.bullet("File links open the document; the three grouped links (Accelerator Packs, Workshops, Demo Scripts) open the SharePoint folder view.")
d.bullet("If you move or rename the library later, the URLs change - tell me the new path and I regenerate the link map in two minutes.")
d.bullet("Want this automated instead of pasted? I can write a PnP PowerShell script that builds the whole page from the link map - hand it to your SharePoint admin to run.")

d.h1("Permissions Recap", numbered=True)
d.para("The page links point at the library; SharePoint enforces access per file. Anyone you grant library access clicks straight through; anyone without access to a given file gets access-denied on that card, not a workaround. Lock the library down once (break inheritance, grant your group) and both the page and the docs respect it.")
d.callout("Tonight: get it working via Sync. Tomorrow: build this page for the no-Sync, in-SharePoint experience. Both use the same library you already uploaded.")

d.save(OUT)
print("Saved:", OUT)
