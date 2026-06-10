# -*- coding: utf-8 -*-
"""Build: Connection - SharePoint Publishing Blueprint (INTERNAL, start-here AM)."""
import sys, os
REPO="/sessions/eager-epic-davinci/mnt/everforth-ecs-practice"
sys.path.insert(0, os.path.join(REPO,"03_Shared","00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta
LOGO=os.path.join(REPO,"00_Master_Blueprint","assets","everforth_logo.png")
OUT=os.path.join(REPO,"05_Clients","Connection","Connection_SharePoint_Publishing_Blueprint.docx")

d=EcsDocument(meta=DocMeta(
 eyebrow="INTERNAL - SHAREPOINT PUBLISHING BLUEPRINT (OPEN FIRST, AM)",
 title="Connection Execution Library\nSharePoint Publishing Blueprint",
 subtitle="Stand it up on corporate SharePoint - shareable, permissioned, local copy untouched",
 org="ECS Federal - ServiceNow Practice",
 audience="Tim Hislop - internal",
 companion_to="Paste Checklist - Build Guide - Link Map xlsx",
 doc_id="INT-CONN-SPBP-01", version="1.0", status="Draft",
 running_header_label="Internal - SharePoint Publishing Blueprint"), logo_path=LOGO)
d.add_cover_page(); d.page_break()

d.h1("The Goal", numbered=False)
d.para("A permission-controlled home on your corporate SharePoint where each person opens a role-based page and clicks straight to their documents - and you can share it by link. Your local repository copy stays the untouched master and audit baseline. SharePoint is the published mirror, not the place you edit.")

d.h1("The One Thing We Learned Tonight", numbered=True)
d.para("SharePoint renders an uploaded HTML file inside a sandboxed document preview. Scripts run (the role/phase filters work), but link clicks are blocked - so the navigator HTML cannot be the in-SharePoint front door. The durable answer is a native SharePoint page built from web parts, which is not sandboxed. The HTML navigator still works perfectly from a local/synced copy, but Sync is off the table on your devices, so we go native page.")
d.callout("Not a defect, not your structure, not the code-free cleanup, not permissions - just how SharePoint sandboxes uploaded HTML. The native page sidesteps it entirely.")

d.h1("Ground Rules", numbered=True)
d.bullet("Local is master. The repo (05_Clients working copy, 06_Client_Upload static mirror) is the source of truth. Never edit documents directly in SharePoint as the authority.")
d.bullet("Don't touch the local copy to make SharePoint work - the two are independent. SharePoint changes never flow back.")
d.bullet("Everything in the build is manual browser clicks on your work machine - no scripts, no Sync, no admin tooling required.")

d.h1("The Sequence (morning plan)", numbered=True)
d.table(headers=["#","Step","Notes"], rows=[
 ["1","Confirm the library upload","06_Client_Upload/Connection is already in SharePoint with the folder structure intact - verify 00_START_HERE, 01_Onboarding, 02_Delivery are all there"],
 ["2","Lock permissions","On the Connection library/folder: Manage access -> Stop inheriting -> grant your ECS group (and/or client group); remove broad access"],
 ["3","Build the native page","Follow the Paste Checklist: create the page, build the 5 ECS roles first, Publish, then add the 7 client roles"],
 ["4","Add a full-library index (optional)","One Highlighted Content web part scoped to the library = the whole catalog with zero manual links"],
 ["5","Share","Send the published page URL; SharePoint permissions decide who opens what"],
 ["6","Validate","A teammate with access clicks through; someone without access to a file gets access-denied on that card"],
])

d.h1("Keeping It Current Over Time", numbered=True)
d.bullet("When a document changes: edit locally -> re-run the export -> re-upload only the changed file to SharePoint (Upload -> Replace). The page links keep working; you don't rebuild the page.")
d.bullet("If you move or rename the library: the URLs change - tell me the new path and I regenerate the Link Map and Paste Checklist in minutes.")
d.bullet("For a brand-new engagement later: this whole pattern is the reusable baseline - same structure, same export, same page build.")

d.h1("Your Asset Pack (open these in order)", numbered=True)
d.table(headers=["Open","File","Use it to"], rows=[
 ["1st","Connection_SharePoint_Publishing_Blueprint (this doc)","See the whole plan and the ground rules"],
 ["2nd","Connection_Native_Page_PASTE_Checklist","Build the page - checkbox, title, URL per role"],
 ["ref","Connection_Native_SharePoint_Page_Build_Guide","The SharePoint mechanics explained in prose"],
 ["ref","Connection_SharePoint_LinkMap.xlsx","The raw URLs if you'd rather copy from a cell"],
])

d.h1("Fallbacks", numbered=True)
d.bullet("Short on time: publish the ECS-role sections only and add client roles later - the page is editable anytime.")
d.bullet("Want it automated eventually: a PnP PowerShell script can build the page from the Link Map - hand it to your SharePoint admin to run from a managed device (not your personal one).")
d.bullet("Team can't access: check the library/page permissions, not the page itself - access is enforced per file by SharePoint.")

d.callout("Local copy is sacred and stays as-is. SharePoint is the shareable mirror. Build the native page from the checklist, lock permissions, share the link - that is review-ready for your people.")
d.save(OUT)
print("Saved:", OUT)
