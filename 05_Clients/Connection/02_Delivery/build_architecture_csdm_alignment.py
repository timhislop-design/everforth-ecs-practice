import sys, os
REPO="/sessions/eager-epic-davinci/mnt/everforth-ecs-practice"
sys.path.insert(0, os.path.join(REPO,"03_Shared","00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta
LOGO=os.path.join(REPO,"00_Master_Blueprint","assets","everforth_logo.png")
CONF="ECS Federal - ServiceNow Practice - Confidential"
OUT=os.path.join(REPO,"05_Clients","Connection","02_Delivery","Connection_Platform_Architecture_and_CSDM_Alignment.docx")
d=EcsDocument(meta=DocMeta(eyebrow="CLIENT DELIVERABLE - ARCHITECTURE",
 title="Connection ServiceNow\nPlatform Architecture & CSDM Alignment",
 subtitle="The target platform topology and the CSDM-aligned data foundation - Month 1 deliverable",
 org="ECS Federal - ServiceNow Practice",
 audience="Connection Project Sponsor, Technical Lead & Platform Team; ECS Delivery",
 companion_to="SOW v2.0 - CSDM & CMDB workshop decks - CMDB_CSDM accelerator pack",
 doc_id="DEL-CONN-ARCH-01", version="1.0 (template)", status="Template",
 confidentiality=CONF, running_header_label="Connection - Architecture & CSDM Alignment", footer_left=CONF), logo_path=LOGO)
d.add_cover_page(); d.page_break()
d.h1("How to Use This Document", numbered=False)
d.para("This is the Month 1 architecture deliverable. The Solution Architect completes it from the CSDM and CMDB workshop decisions and the CMDB_CSDM accelerator pack. It records the target platform topology and the CSDM-aligned data foundation that everything downstream depends on. Replace [bracketed] placeholders and insert the diagrams where noted.")
d.callout("A healthy, CSDM-aligned CMDB from day one is the prerequisite for CI-based change risk scoring and trustworthy AI ROI. This document is where that foundation is defined and signed off.")
d.h1("Architecture Overview", numbered=True)
d.para("Connection is exiting a domain-separated shared instance and standing up a dedicated, governed platform. The target is OOTB-aligned, upgrade-friendly, and AI-ready.")
d.bullet("Dedicated instance (exit domain separation) with sub-production and production environments.")
d.bullet("SSO (SAML 2.0) with Connection's IdP; users/groups via AD/LDAP scheduled import.")
d.bullet("MID Server for integrations and Discovery; OOTB Service Graph Connectors for SCCM and Intune.")
d.bullet("[Insert architecture topology diagram here].")
d.h1("Platform Topology", numbered=True)
d.table(headers=["Component","Detail","Notes"], rows=[
 ["Production instance","[instance URL]","Governed; cutover Week 16"],
 ["Sub-production instance(s)","[dev / test URLs]","Build + UAT"],
 ["Identity / SSO","SAML 2.0 - [IdP]","See SSO accelerator pack"],
 ["Directory import","AD / LDAP scheduled import","Users, groups, departments"],
 ["MID Server","[host]","Discovery + integrations"],
 ["Service Graph Connectors","SCCM, Intune","CI data into CMDB"],
 ["Telephony / CTI","Vonage via OpenFrame + Interactions","Phase 1 inbound voice"],
])
d.h1("CSDM Alignment", numbered=True)
d.para("Configuration follows the Common Service Data Model (CSDM 5.0). The table below records the in-scope domains and the service taxonomy agreed in the CSDM workshop.")
d.table(headers=["CSDM Domain","In scope for Phase 1","Notes / decisions"], rows=[
 ["Foundation","Yes","Core companies, locations, users, groups"],
 ["Design","Yes","Business/Application services, service taxonomy"],
 ["Manage Technical / Build","Yes","CI classes, relationships from Discovery/SGC"],
 ["Sell / Consume","[as needed]","Service offerings where applicable"],
])
d.h2("In-scope CI classes & relationships")
d.table(headers=["CI Class","Source","Key relationships"], rows=[
 ["[Server / Computer]","SCCM / Discovery","Runs on, Depends on, Hosted on"],
 ["[Application / Service]","Workshop / CSDM","Depends on, Used by"],
 ["[Network / other]","Discovery","[ ]"],
])
d.h1("CMDB & Data Sources", numbered=True)
d.bullet("Discovery: leverage existing configuration where it does not introduce technical debt.")
d.bullet("Service Graph Connectors: SCCM and Intune as the authoritative CI sources for in-scope classes.")
d.bullet("IRE / reconciliation rules govern multi-source CI data; CI ownership and stewardship per OOTB fields.")
d.bullet("CMDB Health: completeness, staleness, and compliance thresholds set to support risk scoring.")
d.h1("Change Risk Scoring Readiness", numbered=True)
d.para("With a CSDM-aligned CMDB, change requests inherit CI context, enabling CI-based change risk scoring and a more targeted CAB. This section records the data conditions required and confirms readiness.")
d.h1("AI Readiness", numbered=True)
d.para("The OOTB, CSDM-aligned foundation established here is the architectural prerequisite for the AI capabilities Connection has invested in (Predictive Intelligence in Phase 1; Now Assist and Agentic AI in later phases). No customization that compromises upgradeability is introduced to reach it.")
d.h1("Architecture Decisions Log", numbered=True)
d.table(headers=["Decision","Option chosen","Rationale"], rows=[
 ["[e.g., CSDM reference model]","[chosen]","[why]"],
 ["[ ]","[ ]","[ ]"],
])
d.callout("Sign-off: this document is reviewed and accepted by the Connection Technical Lead and Project Sponsor before Month 2 build proceeds.")
d.save(OUT); print("Saved arch")
