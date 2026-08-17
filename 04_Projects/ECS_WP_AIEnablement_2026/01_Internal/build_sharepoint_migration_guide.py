"""
build_sharepoint_migration_guide.py — ECS-AIE-02
SharePoint Migration Recommendation Guide (Internal)
Built with EcsDocument from ecs_template.py per practice build rules.
Project: 04_Projects/ECS_WP_AIEnablement_2026
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ecs_template import EcsDocument, DocMeta, Brand

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(HERE, "everforth_logo.png")

doc = EcsDocument(
    meta=DocMeta(
        eyebrow="INTERNAL RECOMMENDATION GUIDE",
        title="Moving the Practice Library\nto ECS SharePoint",
        subtitle="Recommended site structure, metadata model, permissions, and a migration path that follows the review program",
        org="ECS Federal · ServiceNow Practice",
        audience="Practice leadership and the AI capability working group",
        companion_to="AI Enablement Guidebook (ECS-AIE-01) · Library Navigator (index.html)",
        doc_id="ECS-AIE-02",
        version="1.0",
        status="Draft for working-group review",
        confidentiality="Internal Use Only · Confidential",
        running_header_label="Internal · SharePoint Migration Guide",
    ),
    logo_path=LOGO,
)

doc.add_cover_page()
doc.add_page_break()

doc.h1("Recommendation Summary", numbered=False)
doc.para("Move the practice library's published documents to an ECS SharePoint site organized by lifecycle stage and driven by metadata — while keeping GitHub as the working source of truth where documents are built, versioned as code, and regenerated. SharePoint becomes where the team and, selectively, clients consume the library; GitHub remains where it is made. Never let the two drift: published documents are read-only outputs, and every change flows through the build scripts and republish.")
doc.callout("Two-tier model: GitHub = build and baseline (scripts, catalog, navigator generator). SharePoint = publish and consume (documents, metadata views, search, sharing). Documents are never edited in place on SharePoint.")
doc.para("Three principles drive every recommendation in this guide. First, lifecycle-and-role organization, not methodology organization: not every engagement runs the same delivery model — the shape of an engagement follows the RFP's objectives — so the structure is stage-based (capture through closeout) and engagement kits are assembled from those shelves per pursuit, with delivery approach carried as metadata rather than folder hierarchy. Second, audience separation is a hard boundary: internal collateral and client-facing collateral live in different libraries with different permissions, so an 'Internal Use Only' footer can never leak. Third, the migration follows the review program: what gets published advances with the stage-by-stage team reviews from the AI Enablement Guidebook, and the review verdict is visible metadata on every document.")

doc.h1("Site Architecture")
doc.para("One practice site, four document libraries, plus separate per-engagement sites when a client needs shared access. Keep the practice site flat — SharePoint works best with more libraries and metadata, not deep folder trees.")
doc.table(
    headers=["Library", "Contents", "Access"],
    rows=[
        ["01 Practice Library (Internal)", "All internal collateral: handbook, sales and pre-engagement, Sprint 0 setup, facilitator guides, how-tos, cheatsheets, demo scripts, UAT packs, Trust-But-Verify, lessons learned", "Practice team only"],
        ["02 Client-Ready Library", "Client-facing artifacts only, with the client footer: engagement overviews, readiness packs, briefs, decision guides, pre-reads, UAT execution, closeout pack", "Practice team; individual docs shared outward only via engagement sites"],
        ["03 Shared Delivery Assets", "Accelerator packs, project plan templates, sprint workbooks, workshop decks", "Practice team"],
        ["04 Governance & Standards", "Brand standard, template specs, governance operating guide, decision rights, the AI-effort documents (guidebook, this guide), review scoreboard exports", "Practice team; edit restricted to owners"],
        ["Per-engagement sites", "The tailored kit for one client, assembled from ratified shelves per the RFP's objectives — copies, never links into the practice libraries", "That engagement's ECS team + invited client users"],
    ],
    col_widths_in=[1.7, 3.4, 1.4],
)
doc.h2("Inside each library")
doc.para("Mirror the repo's numbered top-level scheme as one level of folders (for familiarity and clean sync), and stop there — no nesting beyond the category folder except packaged sets like accelerator packs. Everything else a person needs to find a document comes from metadata and views, and from the Library Navigator as the front door.")

doc.h1("Metadata Model")
doc.para("Metadata is what makes one library serve many audiences, roles, and delivery models at once. Define these as site columns once, apply them to all four libraries, and populate them at publish time (the publish script can stamp most of them automatically from the catalog and navigator data).")
doc.table(
    headers=["Column", "Type", "Values / purpose"],
    rows=[
        ["Doc ID", "Text", "Catalog ID (INT-SP-02, CLT-CO-04, AP-06) — the join key to blueprint_catalog.json"],
        ["Audience", "Choice", "Internal / Client-facing / Shared"],
        ["Lifecycle Stage", "Choice", "Capture & Pre-Sales / Proposal & SOW / Award & Sprint 0 / Delivery / Verification & PMO / Closeout & Hypercare / Practice Governance"],
        ["Role", "Multi-choice", "Capture & Sales Lead / Practice Lead / EM-PL / Solution Architect / Process Consultant-BA / Technical Consultant"],
        ["Discipline", "Choice", "Process area (Incident, Catalog, CMDB, HAM, ...) where applicable"],
        ["Delivery Approach", "Multi-choice", "OOTB-First / Modernization / Custom-Hybrid / Any — engagements filter by what the RFP calls for; most artifacts tag 'Any'"],
        ["Review Verdict", "Choice", "Proposed / Ratified / Needs Update / Replace / Gap — mirrors library_review_status.json"],
        ["Review Owner", "Person", "Accountable reviewer role-holder for the artifact's stage"],
        ["Version / Published", "Text / Date", "Library version at publish; the publish date"],
    ],
    col_widths_in=[1.4, 1.0, 4.1],
)
doc.h2("Views to create on day one")
doc.bullet("By Stage (grouped by Lifecycle Stage) — the default browse experience, matching the navigator.")
doc.bullet("My Role (filtered by Role) — one saved view per role, matching the navigator's role filter.")
doc.bullet("Review Board (grouped by Review Verdict) — the standing scoreboard for the baseline review program; leadership checks this, not a spreadsheet.")
doc.bullet("Client-Ready + Ratified (Client-Ready Library, Verdict = Ratified) — the only view an engagement kit may be assembled from.")

doc.h1("Permissions and Data Protection")
doc.bullet("Site owners: Sr. Director and Practice Lead. Members: practice team (contribute to working areas, read-only on published libraries). Publishing rights: the named publisher role only.")
doc.bullet("The internal library is never shared externally — no guest links, no exceptions. Client access happens only on per-engagement sites, containing copies of ratified client-ready artifacts tailored for that engagement.")
doc.bullet("Apply sensitivity labels if the ECS tenant supports them (Internal Use Only on libraries 01/03/04; per-engagement labeling on client sites). Disable 'Anyone with the link' sharing at the site level.")
doc.bullet("Pursuit and engagement working content (04_Projects, client folders) stays out of the practice site — pursuits carry their own access control and often their own CUI handling constraints, consistent with the data-handling rule from the AI Enablement plan's Phase 0.")
doc.bullet("Version history on (major versions at publish); require check-out off — documents are read-only outputs, and the no-edit-in-place rule is enforced by permissions, not discipline.")

doc.h1("Publishing Pipeline")
doc.para("The pipeline keeps GitHub and SharePoint honest with each other. It is deliberately boring: build, review, publish, regenerate the navigator.")
doc.table(
    headers=["#", "Step", "Who / what"],
    rows=[
        ["1", "Change is made in GitHub: edit the build script or source, rebuild the artifact, update blueprint_catalog.json", "Artifact owner"],
        ["2", "Stage review verdict recorded in library_review_status.json (ratify / update / replace / gap)", "Stage's lead reviewer"],
        ["3", "Publish: upload the rebuilt document to the correct SharePoint library; stamp metadata (script-assisted from catalog + navigator data)", "Publisher role"],
        ["4", "Regenerate the navigator: run build_library_navigator.py — for SharePoint, with --sharepoint <site base URL> so index_sharepoint.html links resolve to the published copies", "Publisher role"],
        ["5", "Surface it: navigator embedded on the site home page (or linked as the front door); metadata views stay current automatically", "One-time setup, then automatic"],
    ],
    col_widths_in=[0.35, 4.2, 1.95],
)
doc.h2("A note on the navigator in SharePoint")
doc.para("Modern SharePoint will not execute a raw uploaded .html file in the browser for security reasons — it downloads instead. Three workable options, in order of preference: embed the navigator on a site page using the Embed or File Viewer web part pointing at the generated file; host the generated file from the GitHub repo (GitHub Pages) and link it from the site navigation; or rebuild the front door natively as the metadata views above, using the navigator only locally. The generator's --sharepoint flag exists so that whichever option carries the navigator, its links resolve to the published SharePoint copies. Decide this during Wave 1 with whoever administers the ECS tenant.")

doc.h1("Migration Plan — Waves Aligned to the Review Program")
doc.para("Publication follows ratification. Nothing forces a big-bang migration, and publishing unreviewed content to a shiny new site would just relaunch the baseline problem in a new location. Each wave is small enough to fit the working group's side-of-desk capacity.")
doc.table(
    headers=["Wave", "When", "What happens"],
    rows=[
        ["1 — Foundations", "AI plan Phase 0 (Month 1)", "Site + four libraries created; site columns and views configured; permissions and sharing lockdown; navigator hosting decision; publisher named"],
        ["2 — Proposed baseline up", "Phase 0–1", "Full library published to the internal libraries with Verdict = Proposed — visible, searchable, honestly labeled as awaiting review"],
        ["3 — Capture shelf ratified", "Phase 1 (Months 2–4)", "Capture & pre-sales review verdicts land; first Ratified content appears; capture team starts working from SharePoint, not file shares"],
        ["4 — Stage by stage", "Phases 2–5", "Each stage review flips its shelf's verdicts; Client-Ready Library populates only with ratified client artifacts; per-engagement site pattern piloted on one live engagement"],
        ["5 — Cutover", "After Phase 4", "SharePoint declared the consumption home; old copies and shares retired; quarterly audit begins (verdict drift, permission review, stale-copy sweep)"],
    ],
    col_widths_in=[1.5, 1.4, 3.6],
)

doc.h1("Rules That Keep It Working")
doc.bullet("Documents are never edited in place on SharePoint. Change flows through GitHub and republish — the same rule the practice already lives by with build scripts.")
doc.bullet("Doc IDs travel everywhere. The catalog ID is the join key across GitHub, the catalog, the navigator, and SharePoint metadata.")
doc.bullet("Client-facing means client footer, ratified verdict, and Client-Ready Library — all three, checked at publish.")
doc.bullet("Engagement kits are copies assembled per the RFP's objectives, never links into the practice libraries — a client must never see the library evolving behind their kit.")
doc.bullet("The navigator and the Review Board view must agree; both regenerate from the same status file, so if they diverge, a publish step was skipped.")
doc.bullet("Quarterly audit: permissions, sharing links, verdict drift, and stale copies — thirty minutes on the practice management monthly review's cadence, once a quarter.")

doc.h1("Decisions Needed to Start")
doc.table(
    headers=["Decision", "Owner", "Needed by"],
    rows=[
        ["Site location and name on the ECS tenant (and who administers it)", "Sr. Director + ECS IT", "Wave 1"],
        ["Publisher role assignment (who runs publish + regenerate)", "Working group", "Wave 1"],
        ["Sensitivity label availability and policy on the tenant", "ECS IT", "Wave 1"],
        ["Navigator hosting option (embed web part / GitHub Pages / native views)", "Working group + ECS IT", "Wave 1"],
        ["Per-engagement site template and client-invite policy", "Practice Lead", "Before Wave 4 pilot"],
    ],
    col_widths_in=[3.3, 1.8, 1.4],
)
doc.para("Once the Wave 1 decisions are made, standing up the site and publishing the proposed baseline is one to two working-group increments — it fits inside the AI plan's Phase 0–1 without adding a new workstream.", italic=True)

out = os.path.join(HERE, "ECS_SharePoint_Migration_Guide_v1.0.docx")
doc.save(out)
print("Saved:", out)
