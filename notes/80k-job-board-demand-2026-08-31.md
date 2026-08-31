# 80,000 Hours job board as a demand source

**Built:** 31 Aug 2026
**Source:** https://jobs.80000hours.org
**Files:** `inventory/80k-roles-2026-08-31.csv` (39 roles) ·
`inventory/80k-orgs-2026-08-31.csv` (53 orgs)

---

## How this was collected (and why not by scraper)

Direct scraping was not possible. This container's egress policy blocks all
general web hosts — `jobs.80000hours.org`, `boards.greenhouse.io` and even
`example.com` all fail at the proxy CONNECT with a 403. Puppeteer would not
have reached the site regardless of which scraper we pointed at it.

Two routes did work:

1. **Exa** (`web_fetch_exa`) renders the board's static pages from Exa's own
   infrastructure. `/organisations/` returns the full 53-org table. Job detail
   pages do **not** render — the board loads them client-side, so
   `?jobPk=NNNNN` returns only the React shell.
2. **The Gmail archive.** You are subscribed to the weekly job board digest
   (`team@80000hours.org`), which lists ~20 roles per week with title,
   organisation, location and a `jobPk` link. Two weeks are captured here.

Note on the digests: the plaintext bodies are quoted-printable, so `jobPk=20684`
decodes as `jobPk 684` (the `=20` is an escaped space). Every pk in the CSV has
been reconstructed. Any future extractor must handle this or it will silently
produce 3-digit ids that 404.

---

## Coverage — read this before using the data

The board carried **910 open roles** on 31 Aug. This dataset has **39**.

| Slice | Count | Share of board |
|---|---|---|
| Roles captured here | 39 | 4% |
| Roles across the 53 curated orgs | 294 | 32% |
| Board total | 910 | 100% |

The digests only surface the ~20 roles the editor chose to highlight out of
each week's 88–105 new listings. This is a **sample, not an inventory.**

---

## Data-quality findings

**1. The org page's "open roles" count is stale or filtered.** Five orgs show
"No open roles" on `/organisations/` while appearing in the 31 Aug digest with
a live vacancy: Institute for Law and AI, Safe AI Forum, Talos Network,
Tarbell Center for AI Journalism, The Future Society. Do not use that count as
a freshness signal — the newsletter is fresher than the org page.

**2. The org page is a curated subset, not the board.** Twelve organisations
appear in the digests but not on `/organisations/` at all: OpenAI Foundation,
The New York Times, US Government (NIST), Johns Hopkins Bloomberg School of
Public Health, Renaissance Philanthropy, SL5 Task Force, LASR Labs, AI Digest,
Humans in Control, High Impact Professionals, Trajectory Labs PBC, and the AI
Verification and Evaluation Research Institute. `/organisations/` is scoped to
"places with roles promising for helping AGI go well" — it is a lens, not a
directory.

**3. Two of the 39 roles are themselves recruiting roles** — Founding Recruiter
at Center for AI Safety (`jobPk=20681`) and Recruiter at SL5 Task Force
(`jobPk=20613`). An org hiring its first in-house recruiter is an org that has
just admitted it cannot fill its own pipeline. That is the strongest single
signal in this dataset for a connector desk.

---

## Commercial caveat — most of this demand is not monetisable

Sized by the org page's own employee bands:

| Band | Orgs |
|---|---|
| 101+ | 8 |
| 51–100 | 3 |
| 21–50 | 13 |
| 11–20 | 9 |
| 1–10 | 18 |

**27 of 53 organisations have fewer than 20 employees**, and most are
grant-funded nonprofits. Contingency search fees of 20–25% are not a normal
line item for a 6-person nonprofit spending restricted grant money. Being
listed as hiring is not the same as being willing to pay a placement fee.

The subset that plausibly pays agency fees: Anthropic, OpenAI, Google DeepMind,
The New York Times, RAND Corporation, Johns Hopkins, and the government bodies
(UK Government, US Government/NIST, UK AISI, EU AI Office) — though the
government entities hire through their own civil service processes and are
usually fee-closed too.

Realistically that leaves **6–8 fee-paying targets** in this dataset. Treat the
long tail as relationship and signal value, not as billable demand.

---

## How this maps to the connector model

**Demand** = the role. `inventory/80k-roles-2026-08-31.csv` is the raw material,
in the same shape as `verified-roles-2026-08-29.md`: title, org, location, and
a URL the recipient can check. It satisfies README rule 1 (verify before you
assert) because every row carries its source link.

**Supply** = recruiters who cover the niche. ConnectorOS carries prebuilt supply
packs that match: `executive_search.supply.retained_search` and
`.boutique_search`, and `tech_recruitment.supply.executive_search`. The
`executive_search` market has 267 demand / 238 supply replies banked across the
community — the second-best-evidenced lane on the platform.

**The pitch** ("do you have someone for this?") works only where the role is
genuinely hard. Sortable by that criterion, the best rows here are:

- `20764` AI Cyber Red Teamer, Trajectory Labs PBC — offensive AI security,
  remote global. Thin candidate pool, high urgency.
- `20647` Principal Researcher, AI Risk Management, NIST — federal, cleared,
  senior. Genuinely hard.
- `20648` COO / Director of Operations, Longview Philanthropy — four-city
  posting, which usually means they have not found the person.
- `20674` / `20675` GovAI, two senior seats posted the same week — a team
  scaling, not backfilling.

Do **not** pitch the fellowships and programmes (`20646`, `20673`, `20650`,
`20663`, `20610`, `20723`). Those are candidate-intake programmes, not
vacancies. Pitching a recruiter on a fellowship marks you as someone who did
not read the listing.

---

## Open gap: jobPk 20660

The role you sent (`?jobPk=20660`) could **not** be resolved. It falls in the
21–24 Aug batch (that week's pks run 20588–20673) but was not among the ~20
highlighted in the 24 Aug digest, and the board itself is unreachable from
here. To identify it, either paste the title, or unblock the board.

## Getting to full coverage (910 roles)

Three options, best first:

1. **Ask 80,000 Hours for the spreadsheet.** Their FAQ states: *"You can view
   all the roles in the Search Jobs tab, and also access these in a
   spreadsheet."* An official, structured, sanctioned export beats any scraper
   and carries no terms-of-service exposure. The FAQ link text is there; the
   href did not survive extraction, so open the FAQ page and grab it.
2. **Allowlist `jobs.80000hours.org`** in the environment's network policy.
   Then the board's own Algolia-backed search endpoint is reachable directly
   and a full pull is straightforward.
3. **Keep harvesting the digests.** Roughly 15 more weekly emails are already
   in the Gmail archive, which would add several hundred historical roles —
   but they are stale by construction, and staleness is what kills this pitch.

Option 1 is the only one that gets all 910 fresh and stays inside their terms.
