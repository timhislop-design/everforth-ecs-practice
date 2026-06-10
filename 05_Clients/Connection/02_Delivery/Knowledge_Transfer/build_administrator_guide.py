import sys, os
REPO="/sessions/eager-epic-davinci/mnt/everforth-ecs-practice"
sys.path.insert(0, os.path.join(REPO,"03_Shared","00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta
LOGO=os.path.join(REPO,"00_Master_Blueprint","assets","everforth_logo.png")
CONF="ECS Federal - ServiceNow Practice - Confidential"
OUT=os.path.join(REPO,"05_Clients","Connection","02_Delivery","Knowledge_Transfer","Connection_Administrator_Guide_and_KT.docx")
d=EcsDocument(meta=DocMeta(eyebrow="CLIENT DELIVERABLE - ADMIN KT",
 title="Connection ServiceNow\nAdministrator Guide & Knowledge Transfer",
 subtitle="Platform administration, update set management, and OOTB governance - Go-Live KT Package",
 org="ECS Federal - ServiceNow Practice",
 audience="Connection platform administrators & IT operations",
 companion_to="SOW v2.0 Sec 11 - Knowledge Transfer Package - Engagement Delivery Guidelines",
 doc_id="DEL-CONN-ADMIN-01", version="1.0 (template)", status="Template",
 confidentiality=CONF, running_header_label="Connection - Administrator Guide & KT", footer_left=CONF), logo_path=LOGO)
d.add_cover_page(); d.page_break()
d.h1("How to Use This Guide", numbered=False)
d.para("This is the administrator reference handed to Connection's platform team at Go-Live, and the backbone for the four Admin Knowledge Transfer (KT) sessions in SOW Section 11. ECS completes the [bracketed] module specifics during the build; the structure is fixed. It keeps the platform OOTB-aligned and upgrade-safe after handover.")
d.h1("Admin KT Session Plan", numbered=True)
d.para("Four remote sessions covering platform administration, update set management, and OOTB governance (SOW Sec 11).")
d.table(headers=["Session","Topic","Who attends"], rows=[
 ["KT-1","Platform administration basics - users, groups, roles, assignment, notifications","Platform admins"],
 ["KT-2","Update set management - capture, promotion dev>test>prod, hygiene","Platform admins + developers"],
 ["KT-3","OOTB governance - Rule of Three, Customization Council, Triage Log, staying upgrade-safe","Admins + platform owner"],
 ["KT-4","Per-module administration + open Q&A","Admins + process owners"],
])
d.h1("Platform Administration", numbered=True)
d.bullet("Users, groups, and roles - provisioning via AD import; OOTB roles (itil, admin, catalog_admin, asset).")
d.bullet("Assignment rules and routing - OOTB assignment configuration per process area.")
d.bullet("Notifications and email - OOTB notification records and templates; inbound/outbound email.")
d.bullet("Schedules, business hours, and system properties - OOTB configuration only.")
d.h1("Update Set Management", numbered=True)
d.bullet("All development happens in sub-production; never build directly in production.")
d.bullet("Capture changes in named update sets; promote dev -> test -> prod with review at each gate.")
d.bullet("Update set hygiene: one logical change per set where practical; review for collisions before promotion.")
d.bullet("Use the OOTB update set preview/commit; resolve conflicts before commit.")
d.h1("OOTB Governance Principles", numbered=True)
d.para("The platform stays valuable because it stays OOTB-aligned. Carry the engagement's discipline forward:")
d.bullet("Rule of Three - meet a need with Configuration, UI Policy, or Flow Designer before treating it as a customization.")
d.bullet("Customization Council + Two-Key decision - any deviation needs a business-need and a technical-path approval.")
d.bullet("Governance Triage Log - keep logging deviation decisions transparently after handover.")
d.bullet("Upgrade safety - avoid changes to protected/OOTB objects; keep customizations documented and minimal.")
d.h1("Per-Module Administration Quick Reference", numbered=True)
d.table(headers=["Module","Common admin tasks","Where"], rows=[
 ["ITSM (Incident/Problem/Change)","Categories, assignment, SLAs, CAB, standard changes","[module admin areas]"],
 ["Service Catalog","Items, variable sets, approvals, fulfillment","Catalog Builder"],
 ["Knowledge","KBs, categories, article workflow, feedback","Knowledge admin"],
 ["Employee Center / VA","Topics, branding, VA topics, AI Search","EC + VA Studio"],
 ["CMDB / CSDM","CI classes, health, reconciliation, Discovery schedules","CMDB Workspace"],
 ["HAM","Stockrooms, asset classes, lifecycle","Asset admin"],
 ["Integrations / CTI","SGC schedules, OpenFrame/Vonage, credentials","Integration admin"],
])
d.h1("Health & Maintenance", numbered=True)
d.bullet("CMDB Health dashboard - monitor completeness, staleness, compliance.")
d.bullet("Scheduled jobs and imports - confirm Discovery/SGC runs and AD imports succeed.")
d.bullet("Platform Analytics - review MTTR, SLA, change-success dashboards.")
d.bullet("Release upgrades - test in sub-prod first; review skipped/ skipped-record reports.")
d.h1("Getting Help & Escalation", numbered=True)
d.para("Level 0-1 support is Connection's Service Desk; Level 2 escalation to ECS during the Hypercare window, then to Connection's platform team and ServiceNow (Level 3) per the Operational Handoff Pack.")
d.callout("This guide pairs with the Train-the-Trainer Toolkit (end-user enablement) to complete the Knowledge Transfer Package.")
d.save(OUT); print("Saved admin")
