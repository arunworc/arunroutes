# The $5,000 access model — review against live inventory

> **Superseded in part, 31 Aug 2026.** This review assumed the product was
> access to a job posting. It is not: the product is a warm introduction to an
> employer who has already seen and shortlisted a specific recruiter's
> candidate. That answers the central objection below. See
> `notes/validated-intro-model-2026-08-31.md`. The economics tables and the
> disintermediation and payment-trigger notes still hold.


**Reviewed:** 31 Aug 2026 · Source: whiteboard, 31 Aug
**Tested against:** `inventory/80k-top10-scraped-2026-08-31.csv`

---

## The model as drawn

Demand (job boards) → we hold it → access gated on qualification → 10 vetted
recruitment firms each submit profiles → the winning profile's firm pays
**$5,000 for access to the demand**.

One structural point first, because it is easy to lose: **the fee comes from
the supply side.** That retires the objection in
`notes/80k-job-board-demand-2026-08-31.md` that most 80k orgs are grant-funded
nonprofits who will not pay agency fees. Under this model they pay nothing.
The recruiter pays. That is a better design than what I was assuming.

---

## The arithmetic is fine

$5,000 against a notional 20% placement fee, on the six of ten roles with
published bands:

| Role | Org | Mid | 20% fee | $5k as % |
|---|---|---|---|---|
| Residency | MATS Research | $220,000 | $44,000 | **11%** |
| Business Correspondent | The New York Times | $157,490 | $31,498 | 16% |
| Social Media & Community Mgr | CAIS | $140,000 | $28,000 | 18% |
| Head of Partnerships | Tarbell | $141,000 | $28,200 | 18% |
| DC Research Manager | GovAI | $127,500 | $25,500 | 20% |
| Entrepreneur-in-Residence | GovAI | $125,000 | $25,000 | 20% |
| Digital Campaigns Mgr | Humans in Control | $87,500 | $17,500 | 29% |

Six clear 25%. The price is not the problem.

---

## The problem is the word "access"

**Every role in our inventory is a public URL.** I found all ten source
postings from a cold start in two rounds of search, for free, in about four
minutes. MATS's residency page, Trajectory's careers page, CAIS's Greenhouse
board — all open, all indexed, all one query away.

A recruiter will not pay $5,000 for a link. "Access locked unless they are
qualified" only creates value if what is behind the lock is genuinely
unobtainable. Right now what is behind the lock is a Greenhouse URL.

Your own README already draws this line, rule 2:

> Never imply a warm relationship that does not exist. "Verified-open posting"
> and "intro" are different products. Say which one is on offer.

The whiteboard is priced as **intro**. The inventory is **verified-open
posting**. That gap is the whole review.

---

## What the recruiter actually cannot self-source

Four things, in ascending order of what they are worth:

1. That the role exists — worth **$0**, it is on the board.
2. That the role is genuinely open and not stale — worth a little.
3. A named hiring manager with a direct line — worth something.
4. **A hiring manager who has already agreed to look at one shortlist** —
   this is the product. It is the only item a recruiter cannot manufacture,
   and it is exactly what README rule 4 promises: *"I will approach the hiring
   manager directly and try to turn this into a real conversation for you."*

That inverts the build order. Today's order is: collect demand → find
recruiters → sell access. The order that supports a $5,000 price is: collect
demand → **win the hiring manager's yes** → sell the slot you now own.

The outreach has to happen before the sale, not after it. The scarce asset is
the yes.

---

## Second filter: does the employer pay the recruiter anything?

The recruiter can only fund $5,000 out of a fee they expect to earn. Of the six
that clear the arithmetic:

- **CAIS** — posting carries a **$1,500 referral bonus**. An org that has
  priced this hire at $1,500 will not sign a $28,000 fee agreement. Dead.
- **The New York Times** — NewsGuild-represented, "submit resume and 5–7
  clips." Newsrooms do not pay contingency for correspondents. Dead.
- **GovAI Entrepreneur-in-Residence** — selection is a two-page pitch for what
  you would build. There is no search. Dead.
- **GovAI DC Research Manager** — plausible, but the deadline was 13 Sep.
  Timing, not fit.
- **Tarbell** — 1–10 person nonprofit. Possible, unproven.
- **MATS Residency** — 30 hires/year at $155k–$285k against an explicitly thin
  pool. The best candidate on the list, with the caveat that they run a
  structured application round closing 31 Oct rather than a search.

**One to two of ten survive both filters.** Not six.

---

## The reframe that makes the thin demand valuable again

There is a second reason a recruiter pays for access, and it is stronger than
placement economics: **business development.**

A boutique AI-safety recruiter does not want one $28,000 fee from Tarbell. They
want Anthropic, DeepMind, OpenAI and GovAI as logos. A warm, qualified
introduction to a hiring manager at a name they have been trying to reach for a
year is worth $5,000 on its own, independent of whether that particular role
closes.

That flips the economics of the small-nonprofit tail. Under a placement-fee
frame, a 6-person nonprofit is worthless. Under a BD frame, an introduction to
the Head of Talent at a recognised AI safety org is a door the recruiter cannot
open cold, and the fee is priced against the relationship, not the requisition.

If you sell BD access rather than fee-share, the qualifying question changes
from *"will this employer pay 20%?"* to *"is this a logo a recruiter wants?"* —
and far more of the 910 board roles pass that test.

---

## Two mechanics that need fixing

**1. Payment is triggered by an event you do not control.** "Whatever profile
gets accepted" makes the fee contingent on the hiring company's decision. You
control neither the quality of the ten submitted profiles nor the hire. You do
the work of sourcing demand, qualifying ten firms and running the process, and
get paid only if someone else's candidate lands. Charge for the slot you
secured, not the outcome you cannot influence.

**2. Disintermediation.** The moment you name the company and the role, the
recruiter can go direct. A $5,000 invoice arriving after they already have the
hiring manager's email is an invoice that does not get paid. This is the same
problem as point 1 and has the same fix: sell the introduction, take the fee at
the point of introduction, and let the placement be their business.

---

## On "connect 10 recruitment firms"

We are finding five per role and already reusing eight firms across seven jobs.
At ten per role the pool exhausts inside roughly twenty roles — faster in AI
safety, where there is no established search-firm market at all (see the supply
note in `notes/80k-top10-matching-2026-08-31.md`).

Ten firms per role is also ten relationships to service for one $5,000 event.
Consider three to five qualified firms per role, with the gate doing more work.

---

## What is right about the board and should not change

- **Gating on qualification.** This is the load-bearing idea. It is precisely
  what lets you promise a hiring manager a clean shortlist instead of spam, and
  therefore what earns the yes in the first place.
- **A flat $5,000.** Far easier to sell than a percentage — no fee agreement,
  no negotiation, no dependence on the employer's terms.
- **Competition between firms.** Good mechanism, and it makes the slot scarce,
  which is what justifies charging for it.

The structure is sound. What it is missing is the step that creates the thing
being sold.
