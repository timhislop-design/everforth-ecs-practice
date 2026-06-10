# -*- coding: utf-8 -*-
"""Build: Connection - Workshop Scope Notes (INTERNAL). Per-module Phase 1 nuances."""
import sys, os
REPO="/sessions/eager-epic-davinci/mnt/everforth-ecs-practice"
sys.path.insert(0, os.path.join(REPO,"03_Shared","00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta
LOGO=os.path.join(REPO,"00_Master_Blueprint","assets","everforth_logo.png")
OUT=os.path.join(REPO,"05_Clients","Connection","02_Delivery","Workshops","Connection_Workshop_Scope_Notes.docx")
doc=EcsDocument(meta=DocMeta(
    eyebrow="INTERNAL - WORKSHOP SCOPE NOTES",
    title="Connection Engagement\nWorkshop Scope Notes",
    subtitle="Per-module Phase 1 nuances - so we tailor light but miss nothing",
    org="ECS Federal - ServiceNow Practice",
    audience="ECS facilitators - Process Consultant, Solution Architect",
    companion_to="Connection workshop decks (02_Delivery/Workshops) - SOW v2.0 - Workshop Facilitation Guide",
    doc_id="DEL-CONN-WSN-01", version="1.2", status="Draft",
    running_header_label="Internal - Connection Workshop Scope Notes",
), logo_path=LOGO)
doc.add_cover_page(); doc.page_break()
doc.h1("How to Use These Notes", numbered=False)
doc.para("The Connection workshop decks are the principle-driven, module-specific library decks - they already carry the OOTB-first approach and the configuration-vs-customization line. Keep tailoring light. These notes capture only the Connection-specific Phase 1 nuances (from SOW v2.0) so a facilitator walks into each workshop knowing the in-scope shape for this client. Confirm exact counts with the Sponsor/Product Owner in the room.")
doc.callout("Source of truth is SOW v2.0. Anything beyond the nuances below is a deviation - route it to the Customization Council and the Governance Triage Log.")
doc.h1("Phase 1 Scope Nuances by Module", numbered=True)
doc.table(headers=["Module / Deck", "Connection Phase 1 nuance", "Workshop deck"], rows=[
 ["Platform Foundation", "SAML SSO with Connection IdP; AD/LDAP import; sub-prod + prod; MID Server; exit domain separation to a dedicated instance.", "Connection_Platform_Foundation_Workshop"],
 ["CSDM", "Foundational CSDM alignment; CI relationship standards; service taxonomy from day one (prereq for change risk scoring + AI ROI).", "Connection_CSDM_Workshop"],
 ["CMDB", "CSDM-aligned CMDB; CI-based change risk scoring; CMDB health sufficient for AI ROI.", "Connection_CMDB_Workshop"],
 ["Discovery", "Leverage existing Discovery configuration where it does not introduce technical debt.", "Connection_Discovery_Workshop"],
 ["Service Graph Connectors", "MS SCCM and Intune connectors (current existing integrations).", "Connection_Service_Graph_Connectors_Workshop"],
 ["Incident", "Run in the Service Operations Workspace.", "Connection_Incident_Workshop"],
 ["Major Incident (MIM)", "In scope as part of ITSM Core. Deck uses the older (narrower) template - cosmetic only; content correct.", "Connection_Major_Incident_Workshop"],
 ["Problem", "Service Operations Workspace; Known Error / KEDB.", "Connection_Problem_Workshop"],
 ["Change", "CAB Workbench + 2-3 well-defined standard changes; CI-driven change risk scoring; SO Workspace.", "Connection_Change_Workshop"],
 ["Service Catalog", "Top 10-15 highest-impact existing items + 2-3 generic catch-all request items; leverage existing catalog where no tech debt.", "Connection_Service_Catalog_Workshop"],
 ["Knowledge", "KM taxonomy + article structure; baseline content ported from the legacy platform.", "Connection_Knowledge_Workshop"],
 ["Employee Center", "Connection-specific branding; AI Search configured for the knowledge base.", "Connection_Employee_Center_Workshop"],
 ["Virtual Agent", "5 baseline topic configurations.", "Connection_Virtual_Agent_Workshop"],
 ["Performance Analytics", "Track MTTR, SLA attainment, change success rate; Data Visualization + Benchmarks on.", "Connection_Performance_Analytics_Workshop"],
 ["Predictive Intelligence (PI)", "Turn on Predictive Intelligence + Task Intelligence. Deck uses the older (narrower) template - cosmetic only; content correct.", "Connection_Predictive_Intelligence_Workshop"],
 ["HAM", "Enable Stockrooms + foundational HAM config to keep CSDM aligned ahead of Phase 2.", "Connection_HAM_Workshop"],
 ["Integrations", "AD/SSO, MS SCCM, Intune - leverage existing config where best-practice-aligned. Vonage CTI via Interactions - see the dedicated deck + pack.", "Connection_Integrations_Workshop"],
])
doc.h1("Platform Baselines Without a Dedicated Deck", numbered=True)
doc.para("Configured in Phase 1 but no standalone workshop deck - fold into Platform Foundation / Analytics sessions:")
doc.bullet("Subscription Management - license visibility baseline; set up groups + basic training.")
doc.bullet("Security Center - baseline posture visibility from day one.")
doc.h1("Vonage + Interactions (Phase 1 - inbound voice)", numbered=True)
doc.para("Delivered for Phase 1 (inbound voice): a dedicated Interactions & Vonage CTI workshop deck (Workshops/) and accelerator pack (Integration_Accelerator_Pack/05_vonage_cti_interactions.xlsx, 8 tabs incl. Developer Notes + Port from Legacy). Vonage is the telephony; ServiceNow Interactions is the OOTB record that captures the call via OpenFrame. Chat/email through Interactions remain later-phase.")
doc.callout("Approach: use Connection\u0027s existing Vonage setup as the spec and rebuild on OOTB OpenFrame + the Vonage connector - no custom telephony middleware (see the pack\u0027s Port from Legacy + Developer Notes tabs).")
doc.save(OUT); print("scope notes v1.1 saved")
