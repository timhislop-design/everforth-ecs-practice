# -*- coding: utf-8 -*-
"""Build: Connection - Publish to SharePoint & Test Runbook (INTERNAL, start-here).
Built via EcsDocument. Internal Use Only footer (default)."""
import sys, os
REPO="/sessions/eager-epic-davinci/mnt/everforth-ecs-practice"
sys.path.insert(0, os.path.join(REPO,"03_Shared","00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta
LOGO=os.path.join(REPO,"00_Master_Blueprint","assets","everforth_logo.png")
OUT=os.path.join(REPO,"05_Clients","Connection","Connection_SharePoint_Publish_and_Test_Runbook.docx")

d=EcsDocument(meta=DocMeta(
 eyebrow="INTERNAL - PUBLISH & TEST RUNBOOK (OPEN THIS FIRST)",
 title="Connection Execution Library\nPublish to SharePoint & Test",
 subtitle="The sequence and the test steps - so the role-based page works for the team",
 org="ECS Federal - ServiceNow Practice",
 audience="Tim Hislop (publisher) - internal",
 companion_to="Connection Execution Navigator - Execution Guide - Library Index",
 doc_id="INT-CONN-PUB-01", version="1.0", status="Draft",
 running_header_label="Internal - Connection Publish & Test"), logo_path=LOGO)
d.add_cover_page(); d.page_break()

d.h1("What You're Doing Today", numbered=False)
d.para("Publish the static execution library to SharePoint, lock it down by permission, and confirm the team can navigate the docs through the role-based HTML page. The whole point of today's test is to learn one thing: does your tenant render the navigator as a page, or does it download it? The answer decides which path you standardize on. Follow the steps in order; the test steps tell you what each outcome means.")
d.callout("Golden rule: upload the ENTIRE 06_Client_Upload/Connection folder, keeping its structure. The navigator's links are relative - 00_START_HERE, 01_Onboarding, and 02_Delivery must travel together or the links break.")

d.h1("Before You Start", numbered=True)
d.bullet("Push today's changes so GitHub matches what you publish (commands at the end of this doc).")
d.bullet("Know your upload source: the folder 06_Client_Upload/Connection (not the zip, not loose files).")
d.bullet("Decide your audience groups: ECS pod, client team, or both - you'll point permissions at these in Step 3.")

d.h1("The Sequence (do in order)", numbered=True)
d.table(headers=["Step","Action","Why"], rows=[
 ["1","Push the repo (optional but recommended)","Keeps the ECS GitHub baseline in sync with what you upload"],
 ["2","Upload the whole 06_Client_Upload/Connection folder to the target SharePoint library","Preserves structure so the navigator's relative links resolve"],
 ["3","Break inheritance on the library/folder; grant only your chosen group(s)","Locks access by permission; removes broad/everyone access"],
 ["4","Run Test A - does the navigator render or download?","This is the make-or-break test"],
 ["5","If it downloads, run Test B - the Sync fallback","Reliable path that ignores the custom-script setting"],
 ["6","Run Test C - permission check","Confirms the lockdown actually holds"],
 ["7","Decide the path and tell me the result","I finalize the access sheet or build the native page"],
])

d.h1("Test A - Direct Render (the key test)", numbered=True)
d.para("In the SharePoint library, open 00_START_HERE and click Connection_Execution_Navigator.html.")
d.bullet("PASS: it opens as a page. Pick a role and a phase; click a card; the document opens. -> Your tenant allows HTML. Publish as-is and send the team the page link.")
d.bullet("FAIL: the file downloads to your machine instead of opening. -> Custom script is locked down (expected on a federal tenant). This is not broken; go to Test B.")

d.h1("Test B - Sync Fallback", numbered=True)
d.para("Back in the library, click Sync (or Add shortcut to OneDrive).")
d.bullet("Open the synced folder in File Explorer -> 00_START_HERE -> open the navigator.")
d.bullet("Pick a role and phase -> click a card -> confirm the document opens from the synced location.")
d.bullet("PASS: this is your reliable team path. Standardize on it; the team Syncs once and opens the page locally.")

d.h1("Test C - Permission Check", numbered=True)
d.para("Best done with a teammate or a second account.")
d.bullet("Someone WITHOUT access opens the library link -> should be denied.")
d.bullet("Someone WITH access opens the navigator and clicks a card -> should open. (SharePoint enforces access per file, so a card a person can't open returns access-denied, not a leak.)")

d.h1("Decide the Path", numbered=True)
d.table(headers=["Test A result","What you do","Next"], rows=[
 ["Renders in SharePoint","Publish as-is; share the library link + the role page","Send me the base URL if you want cards to deep-link to SharePoint"],
 ["Only works via Sync","Standardize on Sync for the team","I finalize the one-page access sheet (Sync steps)"],
 ["Neither feels clean","Switch to a native SharePoint page (web parts, renders inline, no custom-script needed)","Ping me and I build the starter layout"],
])

d.h1("Send Me After Testing", numbered=True)
d.bullet("Which test passed (A, B, or C) and anything odd you saw.")
d.bullet("The SharePoint base URL - if you want the link-launcher (cards pointing to SharePoint URLs) or the native page version.")

d.h1("Quick Reference - Push Commands", numbered=True)
d.para("Run in PowerShell from the repo before you upload, so GitHub matches:")
d.para("cd C:\\\\Users\\\\timhi\\\\Documents\\\\GitHub\\\\everforth-ecs-practice")
d.para("git add -A")
d.para('git commit -m "Connection: SharePoint publish/test runbook + Scrum Master role updates"')
d.para("git push origin main")
d.callout("Open this doc first tomorrow. Work top to bottom; Test A decides everything else. When you have the result, I'll lock in the team's access path.")

d.save(OUT)
print("Saved:", OUT)
