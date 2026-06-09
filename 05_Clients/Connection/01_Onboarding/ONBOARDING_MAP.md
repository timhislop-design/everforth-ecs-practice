# Connection Onboarding Map — Curation Framework

> **DRAFT for Tim's review.** Roles, layering, and the client cut are proposed starting points — adjust freely.

## The Challenge

The OOTB library (00–03) is comprehensive because it was built as the practice's full body of knowledge. Connection is the **first engagement**, so we cannot layer the whole library onto it. Two failure modes to avoid:

1. **Team overwhelm** — handing every consultant the entire library. Fix: each role gets a short, sequenced reading path; everything else is reference.
2. **Client overwhelm** — sending the client internal depth and every decision guide. Fix: the client sees a small, staged, plain-language subset tied to what they need to *do* next.

The principle: **curate, don't copy.** We pull from the library by role and by moment, and reference the rest.

---

## Internal Team — Role-Based Tracks

Each role gets a **Core path** (read before Sprint 0) and **Just-in-time** reference (pulled per sprint). Sources are *referenced by path in the library* — not copied here.

| Role | Core path (read first) | Just-in-time reference |
|---|---|---|
| **Engagement Manager / Delivery Lead** | Delivery Playbook · Internal Governance Operating Guide · Connection SOW (scope/success criteria) | Per-Sprint Facilitator Guides · Trust-but-Verify Management · Lessons Learned |
| **Solution Architect** | Delivery Playbook · Adopt-vs-Reengineer Cheatsheets · relevant Accelerator Pack Blueprints | Discipline How-To Guides · CMDB/CSDM & Integration packs as scoped |
| **Technical Consultant / Developer** | Sprint 0 Setup · Accelerator Packs for in-scope modules | Discipline How-To Guides · Demo Scripts · Sprint Workbooks |
| **Business Analyst / Process Consultant** | Decision Topic Guides (in-scope only) · Workshop Pre-Reads | Per-Sprint Customer Briefs · UAT Test Packs |
| **QA / UAT Lead** | UAT Test Packs · Trust-but-Verify Management | Demo Scripts · UAT Execution materials |

**Sequencing:** Day 1 (orientation: who we are, OOTB-first, the Connection scope) → Sprint 0 (role Core path) → Per sprint (pull only that sprint's facilitator guide + pack).

---

## Client — Staged, Right-Sized Cut

The client gets a **thin, sequenced** set — enough to engage, never the internal library. Audiences and what each sees:

| Client audience | What they get | When | Source |
|---|---|---|---|
| **Executive Sponsor / Steering** | "Why OOTB-First" whitepaper (the narrative) · Governance Charter | Kickoff | `00_Source_Inputs/` (adapt) |
| **Project Sponsor / PM** | Engagement roadmap · Governance Charter · roles & cadence | Kickoff | Governance Charter + sprint schedule |
| **Process owners / SMEs** | Only the Decision Topic Guides + Workshop Pre-Reads for *their* workshop | Per workshop | `02_Client/04` + `05` (curated subset) |
| **Platform team** | Foundation/admin SOPs for their modules | Pre-go-live | Accelerator Pack READMEs |

**Anti-overwhelm rule:** the client never receives the full Decision Topic Guide set at once — only the guide(s) tied to the workshop in front of them.

---

## Onboarding Package — Deliverables to Build

| # | Deliverable | Audience | Builds from |
|---|---|---|---|
| 1 | **Internal Team Onboarding Guide** (role tracks above) | ECS team | Delivery Playbook + this map |
| 2 | **Client Onboarding Guide** (what to expect, roadmap, governance, contacts) | Connection | Why-OOTB whitepaper + Governance Charter |
| 3 | **Kickoff Deck** | Joint | Both of the above |
| 4 | **Onboarding Checklist / Tracker** (tasks both sides, by role) | Both | This map |

---

## Open Decisions for Tim

1. **Roles** — are the five internal roles above the right set for the Connection team? Add/rename?
2. **Scope** — which ServiceNow modules are in Connection's scope? That determines which Accelerator Packs each role pulls.
3. **Build order** — start with the Internal Team Guide, the Client Guide, or the Kickoff Deck?
