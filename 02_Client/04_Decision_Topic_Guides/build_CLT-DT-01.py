"""
Build CLT-DT-01 — Decision Topic Guide: Catalog Item Rationalization
Client-facing artifact. Partnership-toned. Educates the customer decision-maker
without prescribing. The customer is the decider; ECS is the framer.

Reference tone: 02_Client/05_Workshop_Pre-Reads/Category_Realignment_Customer_WhitePaper.docx
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "03_Shared", "00_Templates_and_Branding"))
from ecs_template import EcsDocument, DocMeta

OUT = os.path.join(HERE, "Catalog_Item_Rationalization_Decision_Guide_CLIENT.docx")

doc = EcsDocument(meta=DocMeta(
    eyebrow="DECISION TOPIC GUIDE · CATALOG ITEM RATIONALIZATION",
    title="Catalog Item\nRationalization",
    subtitle="A decision guide for what to keep, what to combine, and what to retire as you reshape your service catalog",
    audience="Service Owners, Catalog Owners, Process Managers, Service Desk Leadership",
    companion_to="The Workshop Pre-Read for Catalog Rationalization · The four-decision template",
    doc_id="CLT-DT-01",
    version="1.0",
    status="Released",
    confidentiality="Confidential — prepared for the recipient and their organization",
    running_header_label="Decision Topic Guide · Catalog Item Rationalization",
    footer_left="ECS Federal · ServiceNow Practice  ·  Confidential",
))

doc.add_cover_page()

# =============================================================================
# Section 0 — How to use this guide (unnumbered, conversational opener)
# =============================================================================
doc.h1("How to Use This Guide", numbered=False)
doc.para(
    "If your IT team is preparing for a ServiceNow reimplementation, the conversation about the service "
    "catalog will surface early and matter more than most. The items, the variants, the templated requests "
    "that have accumulated over the years — they didn't grow that way by accident. They grew because they "
    "had to. They were doing important work that needed doing, with the tools available at the time."
)
doc.para(
    "This guide exists because the conversation about rationalizing that catalog is uncomfortable, and the "
    "discomfort is rational. It can feel, on first description, like discarding years of work by people who "
    "were trying to make the operation run. It is not. It is a different question entirely: now that "
    "ServiceNow has substantially different capabilities than it had three or five or ten years ago — and "
    "now that your users have substantially different expectations — what is the right shape for your "
    "catalog today, and what changes for your team if we adjust it?"
)
doc.para(
    "Read this before our first workshop on the topic. The intent is not to convince you of anything you "
    "will see for the first time in the workshop. It is to give you the conceptual map so the workshop "
    "conversation is about your specifics rather than the foundational ideas. By the time we sit down "
    "together, you will already know the four decisions on the table, the trade-offs each one carries, and "
    "the kinds of answers customers in your position have arrived at."
)
doc.para("Who should read this:", bold=True, space_after=2)
doc.bullet("Service Owners — you will hold the decisions for your service area")
doc.bullet("Catalog Owner — you are the throughline across services and the primary decision-maker on the structure")
doc.bullet("Process Managers — your team's daily workflow depends on the answers")
doc.bullet("Service Desk Leadership — your team is the first to feel the consequences of any change to the user-facing surface")

doc.callout(
    "The customer is the decider in every section that follows. We frame the decisions, share what we have "
    "seen in similar engagements, and offer recommendations where we have strong observations. Where you "
    "land is your call, and we will partner with you to implement whatever shape you choose."
)

doc.page_break()

# =============================================================================
# Section 1 — Why now
# =============================================================================
doc.h1("Why Catalog Rationalization Matters Now")
doc.para(
    "Most ServiceNow customers we work with have somewhere between 200 and 2,000 unique catalog items in "
    "their existing instance. That is not unusual. It is the predictable outcome of operating a service "
    "delivery function over years — every new application brought a new request type, every new edge case "
    "earned its own variant, and the catalog accumulated the way any well-used operational asset does. The "
    "items themselves are not the problem. The problem is that the catalog has now grown large enough that "
    "the people meant to use it cannot find what they need, and the people meant to fulfill it spend more "
    "time routing than helping."
)
doc.para(
    "Three changes in the broader landscape make this the right moment to revisit the catalog rather than "
    "carry it forward as-is."
)
doc.h2("Users now expect a search-and-browse experience")
doc.para(
    "Five years ago a service catalog with hundreds of items felt thorough. Today the same catalog feels "
    "like a labyrinth. Employee Center, the modern user-facing surface in ServiceNow, is built for "
    "search-and-browse — not for browsing a five-level menu. Catalogs designed for the old experience "
    "underperform on the new one not because either is wrong, but because the design constraints are "
    "different. The catalog that performs well on Employee Center is rationalized to a quarter or less of "
    "what a comprehensive five-level menu would hold."
)
doc.h2("Virtual Agent and Now Assist need a manageable surface to work against")
doc.para(
    "The newer AI-assisted experiences in ServiceNow — Virtual Agent topics, Now Assist for service "
    "request creation, predictive intelligence for request routing — all perform substantially better when "
    "the catalog they read is rationalized. They are not magic; they are pattern-matching engines, and "
    "pattern-matching engines perform best on smaller surfaces with stronger patterns. A catalog with 1,500 "
    "items containing 400 near-duplicates is a difficult surface for AI; the same catalog after "
    "rationalization to 150-300 distinct items is straightforward."
)
doc.h2("Operational support cost scales with the catalog, not with request volume")
doc.para(
    "The hidden cost of a large catalog is the maintenance burden — every item needs its form, its "
    "workflow, its approval, its assignment rule, its SLA, its notifications. Each one of these accumulates "
    "configuration debt. When a request type changes (and they all change eventually), the maintenance "
    "effort scales with the number of items, not with the number of requests. Customers who carry their "
    "legacy catalog forward generally find that their first six months of support burden is dominated by "
    "small adjustments across many similar items. Customers who rationalize first find the same support "
    "burden concentrated in 100-300 items they can actually maintain."
)

doc.page_break()

# =============================================================================
# Section 2 — The signal
# =============================================================================
doc.h1("The Signals That the Catalog Needs Work")
doc.para(
    "You may already be looking at the catalog and sensing that something has drifted. The signs we have "
    "seen show up consistently across customers, and you may recognize some of them in your own operation. "
    "None of them mean the catalog is broken. They mean it has grown into a shape that no longer matches "
    "the work it is being asked to do."
)
doc.h2("Search returns near-duplicates")
doc.para(
    "When users search for \"new laptop\" and see four results — \"Request New Laptop,\" \"New Hire "
    "Laptop,\" \"Laptop Replacement,\" \"Hardware Request - Laptop\" — that is the most common "
    "rationalization signal. Each item earned its place for a reason in the past; today they overlap "
    "enough that users do not know which to use, and the result is that they pick one inconsistently."
)
doc.h2("Fulfillment teams re-route items frequently")
doc.para(
    "If your service desk regularly receives requests that came in through the wrong catalog item and need "
    "to be reassigned, the catalog's routing logic has become decoupled from how work actually flows. "
    "Re-routing is not a process problem — it is a catalog-design problem surfacing as a process symptom."
)
doc.h2("Many items are submitted rarely or never")
doc.para(
    "Most legacy catalogs have a long tail. Pulling the request volume by item often shows that the top "
    "20% of items handle 80% of the volume, and the bottom 40% handle effectively none. The unused items "
    "are not free — they are still in the navigation, still in search results, still carrying their "
    "approval and SLA configuration. The question worth asking is not \"should we delete the long tail\" "
    "— it is \"do those items still represent valid requests, and if so, can they be consolidated with "
    "active items?\""
)
doc.h2("Forms ask for more than the fulfiller actually uses")
doc.para(
    "A catalog item form that asks the requester twelve questions but only three of which the fulfiller "
    "looks at is a form that grew in response to old requirements that have since changed. Long forms "
    "depress submission rates and make users prefer email or chat over the catalog. The right "
    "rationalization question is which questions are still load-bearing for fulfillment, not how to make "
    "the existing twelve render more nicely."
)
doc.h2("Service owners cannot easily describe their items")
doc.para(
    "If a service owner has to look up their own catalog items to remember what each one does, the catalog "
    "has grown beyond the human capacity to hold a clear model of it. The rationalization goal is a "
    "catalog where every service owner can name and describe every item they own without looking."
)

doc.page_break()

# =============================================================================
# Section 3 — The Four Decisions
# =============================================================================
doc.h1("The Four Decisions")
doc.para(
    "Rationalizing a catalog comes down to four decisions. They are independent of each other in principle "
    "but reinforce each other in practice — answering one well makes the others easier. Each decision is "
    "framed below with the questions it raises, the trade-offs to weigh, and where we typically see "
    "customers land. The point is not to bring you to our answer; it is to bring you to your answer."
)

doc.h2("Decision 1 — What population of services merits a catalog item?")
doc.para(
    "Not every service in your organization needs to be requestable through a catalog item. Some services "
    "are consumed automatically (you do not request access to email — you have email), some are managed "
    "through different channels (HR services through Workday, building services through facilities "
    "ticketing), and some are infrequent enough that a generic request form serves better than a dedicated "
    "item. The first decision is which services rise to the level of meriting a catalog item of their own."
)
doc.para("Questions to weigh:", bold=True, space_after=2)
doc.bullet("Which services have predictable, repeatable requests? Those are catalog candidates.")
doc.bullet("Which services have requests but where each request is bespoke? Those may be better served by a generic intake form.")
doc.bullet("Which services are consumed automatically by virtue of role or location? Those do not need catalog items.")
doc.bullet("Which services have ambiguous ownership today, and would benefit from the discipline of a catalog item to anchor the conversation?")
doc.para(
    "Where customers usually land: a meaningful reduction from the legacy catalog, driven by removing items "
    "for services that are auto-provisioned, services that have no actual request workflow, and services "
    "whose requests are too infrequent to warrant a dedicated item. The hard cases are services that "
    "produce occasional requests but whose request pattern is not standardized — these we typically "
    "consolidate into a generic catalog item per service domain."
)

doc.h2("Decision 2 — What does \"one catalog item\" mean?")
doc.para(
    "Once you decide a service merits a catalog item, the next decision is granularity. Does \"request a "
    "laptop\" mean one item with options for laptop type, or three items (one per laptop type)? Does "
    "\"access request\" mean one item with role selection, or one item per role? The granularity decision "
    "is the most consequential one in the rationalization because it determines both the user experience "
    "and the maintenance burden."
)
doc.para("Questions to weigh:", bold=True, space_after=2)
doc.bullet("How different is the fulfillment workflow across the variants? Variants that share the same workflow consolidate cleanly into one item with options; variants with different workflows often deserve different items.")
doc.bullet("How different is the approval path? Different approval paths usually mean different items; same approval path means same item.")
doc.bullet("How different are the SLAs? Significantly different SLAs usually mean different items.")
doc.bullet("How does the user think about it? If users mentally treat the variants as one thing (\"I need a laptop\"), the catalog should match that mental model; if users distinguish them (\"I need a developer workstation, that's different from a regular laptop\"), the catalog should too.")
doc.para(
    "Where customers usually land: a level of consolidation that surprises them. The default human instinct "
    "is to preserve distinctions; the catalog rationalization instinct should be to consolidate by default "
    "and split only when the workflow / approval / SLA / mental model truly diverges. We have not yet seen "
    "an engagement where this principle led the customer to regret the consolidation; we have seen many "
    "where over-splitting was the source of ongoing maintenance pain."
)

doc.h2("Decision 3 — Front-of-house and back-of-house")
doc.para(
    "What the user sees in the catalog is not the same as what the fulfillment process executes behind it. "
    "Several user-facing items can map to the same fulfillment workflow; one user-facing item can branch "
    "into several fulfillment workflows depending on options. The decision is where to draw the line "
    "between the simplifying front-of-house view and the operationally faithful back-of-house process."
)
doc.para("Questions to weigh:", bold=True, space_after=2)
doc.bullet("Which user-facing items can share a back-of-house workflow without making the workflow harder to maintain? Those are good consolidation candidates.")
doc.bullet("Which workflows are sufficiently different that they need to be separate even when the front-of-house experience is the same? Identify those before consolidating.")
doc.bullet("How do you want fulfillers to see the work? If fulfillers benefit from seeing different items even though the work is the same, that's a real cost to balance against the front-of-house simplification.")
doc.bullet("Which routing decisions can be encoded in the workflow rather than in the catalog item?")
doc.para(
    "Where customers usually land: a meaningful reduction in user-facing items, with the back-of-house "
    "complexity preserved or even slightly increased. The catalog rationalization mostly happens at the "
    "front-of-house layer; the back-of-house workflows often remain similar in count but become better "
    "structured. This is the most counterintuitive of the four decisions and the one where workshop "
    "discussion adds the most value."
)

doc.h2("Decision 4 — Lifecycle and retirement")
doc.para(
    "Catalogs accumulate because no one retires items. Every item that gets added stays; every item that "
    "is no longer used stays. The fourth decision is how the catalog will avoid that fate going forward. "
    "This is a governance decision rather than a structural one — it does not affect what the catalog "
    "looks like at go-live, but it determines what the catalog looks like two years from now."
)
doc.para("Questions to weigh:", bold=True, space_after=2)
doc.bullet("Who owns each item's continued relevance? Without a named owner per item, no one notices when items become stale.")
doc.bullet("On what cadence will catalog items be reviewed? Annually is the minimum we have seen work; quarterly for high-volume items is better.")
doc.bullet("What signal triggers a review outside the cadence? A change in fulfillment team, a drop in submission volume, a complaint pattern from users.")
doc.bullet("What is the retirement workflow? Items should sunset gracefully — hidden from new submissions, in-flight requests honored, eventually archived.")
doc.para(
    "Where customers usually land: a lightweight governance model with named item owners, an annual review "
    "cadence, and a clear retirement workflow. The investment is small; the payback is enormous over the "
    "two-to-three year window when accumulation otherwise compounds."
)

doc.page_break()

# =============================================================================
# Section 4 — What good looks like
# =============================================================================
doc.h1("What Good Looks Like")
doc.para(
    "It helps to have a concrete picture of the destination before we work through the path. A "
    "well-rationalized catalog has a few consistent properties — none of them dramatic, but together they "
    "produce a catalog the user trusts and the fulfillment team can sustain."
)
doc.h2("The user can find what they need in three navigations or fewer")
doc.para(
    "Search returns one obvious result for common requests; browse navigation reaches any item in three "
    "categorical clicks or fewer. The user is never left scanning a long list of near-similar items to "
    "find the one they want."
)
doc.h2("Service owners can name every item they own without looking")
doc.para(
    "Each service owner holds the mental model of the items in their domain. That is the natural test that "
    "the catalog has been rationalized to a sustainable human scale — when the owners themselves can "
    "describe what they own."
)
doc.h2("Forms ask only what fulfillment actually needs")
doc.para(
    "Every question on every form is load-bearing for fulfillment. Questions that fulfillers do not look "
    "at are removed, even if they were once useful. Forms read shorter than they used to, and submission "
    "rates rise accordingly."
)
doc.h2("Each item has a named owner")
doc.para(
    "Every item has a service owner who is accountable for its continued relevance. When the item changes, "
    "the owner approves the change; when the item becomes stale, the owner retires it. No item is "
    "ownerless."
)
doc.h2("New requests have an obvious home")
doc.para(
    "When a new request type arrives, there is a clear question: does it fit an existing item or warrant a "
    "new one? The answer is usually the existing item — and that is by design. The catalog grew "
    "responsibly because the team has a default of consolidation rather than addition."
)
doc.h2("The catalog is forecastable")
doc.para(
    "Looking at the catalog gives you a reliable picture of what services your organization consumes and "
    "how it consumes them. That visibility is the strategic value of catalog rationalization beyond "
    "operational efficiency."
)

doc.page_break()

# =============================================================================
# Section 5 — Common patterns we've seen
# =============================================================================
doc.h1("Common Patterns We Have Seen")
doc.para(
    "Three customer engagements from the past few years illustrate the decisions in practice. None of these "
    "customers had the same starting point; none arrived at the same end state. What they shared was the "
    "approach — naming the four decisions, working through them as a team, and arriving at a catalog they "
    "could sustain. The customer names are removed; the situations are real."
)

doc.h2("Pattern A — A healthcare customer consolidating two legacy catalogs")
doc.para(
    "A regional healthcare system had recently merged two hospital networks, each with its own ServiceNow "
    "instance and catalog. The combined catalog had 1,400 items; many were near-duplicates from the two "
    "legacy systems. The customer's initial inclination was to keep both versions of each near-duplicate "
    "and let users self-select, on the grounds that the workflows had small but real differences."
)
doc.para(
    "Through the four-decision workshop, the team made a different call. On Decision 2 (granularity), they "
    "consolidated 1,400 items down to 320 by treating the workflow differences as options within unified "
    "items rather than as separate items. On Decision 3 (front-of-house vs. back-of-house), they preserved "
    "the back-of-house workflow distinctions where they mattered to fulfillment, so the fulfillment teams "
    "did not lose their working models. On Decision 4 (governance), they assigned a single owner across "
    "the merged organization for each consolidated item, removing the duplicate-ownership pattern that had "
    "carried over from the merger. The user-facing catalog dropped to 320 items, submission accuracy "
    "improved measurably, and fulfillment teams reported the back-of-house complexity stayed manageable."
)

doc.h2("Pattern B — A federal agency simplifying for AI readiness")
doc.para(
    "A federal civilian agency was preparing to deploy Virtual Agent and wanted the catalog rationalized "
    "to make the deployment effective. The starting catalog had 850 items, accumulated over a decade of "
    "operations. The customer's instinct was to leave the catalog as-is and let Virtual Agent learn the "
    "patterns over time."
)
doc.para(
    "The workshop reframed the question. On Decision 1 (in-scope population), the team identified that "
    "roughly a third of the items were for services that had been replaced by other tools (HR services "
    "moved to Workday, security incident reporting moved to a SIEM workflow) — those items were retired. "
    "On Decision 2 (granularity), the remaining items were consolidated where the requester's mental model "
    "treated variants as a single thing. The catalog landed at 240 items. Virtual Agent's topic coverage "
    "model worked substantially better against the 240-item surface than it would have against 850, and "
    "the deployment delivered value in months rather than the year-plus the customer had originally budgeted."
)

doc.h2("Pattern C — A higher-education customer with chronic catalog drift")
doc.para(
    "A large university had a catalog of 600 items and an explicit governance problem: every academic "
    "department was independently requesting new catalog items, and the central IT team had no mechanism "
    "to push back. The catalog had grown by roughly 40 items per year for the past five years and the "
    "trajectory was unsustainable."
)
doc.para(
    "The workshop focused heavily on Decision 4 (governance). The team's catalog structure was actually "
    "reasonable — the items themselves were fit for purpose. The problem was that there was no "
    "responsibility model for sustaining it. The team established a Catalog Stewardship group with "
    "representatives from each major department, an annual review cadence, and a default-no posture for "
    "new item requests that pushed requesters to first attempt consolidation with an existing item. The "
    "catalog stabilized within a year. The structural rationalization in Decisions 1-3 was relatively "
    "modest — about 90 items consolidated; the governance change was what produced the durable result."
)

doc.callout(
    "What these three patterns have in common: each customer started with an instinct that the work would "
    "be primarily structural and ended discovering that the governance and ownership questions in Decision "
    "4 were as consequential as the structural changes in Decisions 1-3. We have not yet seen a "
    "rationalization engagement where Decision 4 was the easy part."
)

doc.page_break()

# =============================================================================
# Section 6 — How we'll workshop this
# =============================================================================
doc.h1("How We Will Workshop This Together")
doc.para(
    "Catalog rationalization happens in a sequenced series of workshops over the first two sprints of the "
    "engagement. The shape below is what we typically use; we will adapt to your operating rhythm and the "
    "specifics of your catalog."
)
doc.h2("Workshop 1 — Catalog Inventory and Signal Review")
doc.para(
    "We start by looking at your current catalog together — the inventory by service area, the submission "
    "volume by item, the patterns of fulfillment routing. The intent is shared situational awareness "
    "before any decision is taken. Most of the rationalization signal becomes visible just from looking at "
    "the data with the right framing."
)
doc.h2("Workshop 2 — Decisions 1 and 2 (In-scope population, Granularity)")
doc.para(
    "The structural decisions. We go service area by service area through the in-scope population question, "
    "then move to granularity. By the end of this workshop you will have a draft target catalog at the "
    "item level — what stays, what consolidates, what retires, and what the new structure looks like."
)
doc.h2("Workshop 3 — Decisions 3 and 4 (Front-vs-back, Lifecycle)")
doc.para(
    "The operational decisions. We work through the front-of-house vs. back-of-house split for each "
    "consolidated item, then design the governance model that will keep the catalog sustainable going "
    "forward. The output is a complete target-state design ready for build."
)
doc.h2("Workshop 4 — Walk-through and Sign-off")
doc.para(
    "We bring the target-state catalog back to a broader stakeholder group, walk it through, capture "
    "feedback, and align on sign-off. The build begins after this workshop with the catalog design locked."
)

doc.page_break()

# =============================================================================
# Section 7 — What we'll need from your team
# =============================================================================
doc.h1("What We Will Need From Your Team")
doc.para(
    "The work of rationalization is collaborative; the answers come from your team. We provide the "
    "structure, the questions, the comparison patterns, and the platform expertise. Here is what we will "
    "ask for from your side, and roughly when in the workshop sequence we will ask for it."
)
doc.h2("Before Workshop 1")
doc.bullet("A current-state export of your catalog items (we can pull this from your ServiceNow instance with read-only access)")
doc.bullet("Twelve-month submission volume by item (same instance access)")
doc.bullet("Named participants from each major service area for the workshop series")
doc.h2("During Workshops 2 and 3")
doc.bullet("Service owners empowered to make in-scope and consolidation decisions for their service area in the workshop room")
doc.bullet("A Catalog Owner with authority to break ties across service areas when consolidation crosses boundaries")
doc.bullet("Realistic openness to consolidation — the workshops produce more value when participants arrive ready to combine items than when they arrive ready to defend each one")
doc.h2("Before Workshop 4")
doc.bullet("Internal alignment within your team on the draft target catalog before the walk-through")
doc.bullet("Stakeholder list for the broader walk-through — typically Service Owners, IT leadership, and one or two service desk representatives")

doc.callout(
    "The single biggest determinant of how well the workshops go is who is in the room. Service owners "
    "with authority to decide for their area make the decisions in the workshop; service owners without "
    "that authority require an additional round of internal alignment that extends the timeline. We will "
    "work with you on the participant list before Workshop 2."
)

doc.page_break()

# =============================================================================
# Section 8 — Questions to consider
# =============================================================================
doc.h1("Questions to Consider Before Our Session")
doc.para(
    "These are not questions you need to answer in writing or bring to the workshop with a position on. "
    "They are questions to turn over in your own thinking so that when the workshop conversation opens, "
    "you have already begun the internal work that makes the conversation efficient."
)
doc.h2("On the current catalog")
doc.bullet("If you had to describe your catalog in three sentences to a peer at another organization, what would you say?")
doc.bullet("Which catalog items get praise from users? Which generate complaints?")
doc.bullet("Which catalog items do your service desk colleagues route around (suggest a different channel) rather than embrace?")
doc.h2("On the future state")
doc.bullet("If your catalog had a quarter as many items, which items would be the keepers? Which would consolidate naturally?")
doc.bullet("What does the right size feel like — is it 100 items, 300, 500? Where do you arrive when you imagine sustaining the catalog two years from now?")
doc.bullet("Which decisions are you comfortable making in the workshop room, and which require additional internal alignment first?")
doc.h2("On governance")
doc.bullet("Who in your organization is currently the implicit owner of catalog quality? Is that the right ownership for the future state, or does it need to evolve?")
doc.bullet("If new catalog item requests have been growing, what is your team's current default response — accept, push back, evaluate?")
doc.bullet("What would a sustainable annual review cadence look like in your operating rhythm?")

doc.page_break()

# =============================================================================
# Section 9 — Cross-references and next steps
# =============================================================================
doc.h1("Cross-References and Next Steps")
doc.para(
    "This guide is one of a small set of decision topic guides we provide ahead of the structural "
    "workshops in the engagement. Each guide follows the same pattern — frame the decisions, share what we "
    "have seen, equip you to arrive at the workshop with the conceptual map already in hand."
)
doc.h2("Related guides in this series")
doc.bullet("Category Structure Simplification — companion topic; rationalizing the categorization taxonomy alongside the catalog itself")
doc.bullet("SLA Discipline — the Service Level Agreement structure that supports the rationalized catalog")
doc.bullet("Assignment Rules — the routing logic that the rationalized catalog feeds into")
doc.bullet("Approval Discipline — the approval patterns that the consolidated items will follow")
doc.h2("After this guide")
doc.para(
    "After you have read this guide, the next step is the catalog inventory and signal review workshop "
    "(Workshop 1 above). We will schedule that within the first two weeks of the engagement; the workbook "
    "and the data extract will be circulated three business days before the session so your team has time "
    "to review."
)
doc.h2("Questions before the workshop")
doc.para(
    "Please reach out to your ECS Engagement Manager with any questions ahead of the workshop. If "
    "something in this guide does not match your situation or raises a question we have not addressed, "
    "that is exactly the conversation we want to have before the formal session — calibrating the guide "
    "to your specifics is part of the preparation."
)

doc.callout(
    "The work that produced your current catalog was the right work for the tools and conditions at the "
    "time. The work ahead is calibrating to the tools and expectations of the next chapter. We are looking "
    "forward to doing it with you."
)

doc.save(OUT)
print(f"Saved: {OUT}")
"forward to doing it with you."
)

doc.save(OUT)
print(f"Saved: {OUT}")
