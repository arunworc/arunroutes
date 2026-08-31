# Can trustpilot-outreach-automation replace Instantly?

**Assessed:** 31 Aug 2026
**Repo:** https://github.com/dancolta/trustpilot-outreach-automation @ `4d14a92`
**Verdict:** No, not as a swap. It replaces the part of Instantly you were
using least well, and does not replace the parts you actually depend on.

---

## The one-line reason

Instantly's job in your stack was **making sends happen without you**.
This tool's default output is **a Gmail draft you have to open and ship**.

Your own README already names the failure mode: *"~20 outreach emails sat as
unsent Gmail drafts from 14-15 July"* and *"A draft is not a send."* Swapping
an auto-sender for a draft-generator points the tooling directly at the
bottleneck you documented. It is the wrong direction.

---

## Signal mismatch (the bigger problem)

The tool's entire premise is that a 1-2* Trustpilot review is a buying signal.
For a connector desk selling verified-open senior roles, that premise breaks
in two places:

**1. Your targets are not on Trustpilot.** The lens is consumer-facing brands
(retail, telecom, insurance, travel). The four companies in
`inventory/verified-roles-2026-08-29.md` — The Nuclear Company, AEVEX
Aerospace, Guidewheel, Suvoda — are defense, industrial and clinical-trial
B2B. Expect the pipeline to return `Skipped` on essentially all of them.
`TROUBLESHOOTING.md` puts normal skip rate at 30-60% on a consumer list;
a B2B-industrial list is worse than that, not better.

**2. Where the signal exists, it points the wrong way.** Staffing and
recruiting firms *do* have Trustpilot pages — but the 1* reviews are written
by **candidates** ("the recruiter ghosted me"), not by the firm's buyers. The
pain in the corpus is not the pain your offer fixes ("you cannot fill this
seat"). An email citing a candidate's complaint back to a recruiting firm
principal reads as an insult, not a signal.

There is no Outreach Profile that fixes this. The profile is a lens on the
review text; it cannot conjure reviews that do not exist or reframe a
candidate grievance into a hiring-manager problem.

---

## Feature gap vs Instantly (verified against the source, not the README)

| Capability | Instantly | This tool |
|---|---|---|
| Multi-inbox rotation | yes | **no** — single Gmail OAuth, send-as alias only (`src/gmail.js`) |
| Inbox warmup | yes | **no** — the `_warmUp()` in `src/trustpilot.js` is Puppeteer page priming, not email warmup |
| Multi-step follow-up sequences | yes | **no** — zero occurrences of sequence/follow-up logic in `src/` |
| Reply detection / auto-pause on reply | yes | **no** |
| Bounce handling | yes | **no** |
| Unsubscribe link + suppression list | yes | **no** — zero occurrences of unsubscribe/opt-out/blocklist |
| Daily volume cap | yes | **no** — only randomized 15-25 min intervals inside a business-hours window |
| Campaign analytics | yes | a Status column in a Google Sheet |
| Restart durability of scheduled sends | yes | yes — recovery rebuilds the queue from the Sheet (`src/server.js:872-943`) |

Two of these are not merely inconvenient:

- **No follow-up sequences.** Your July numbers were 395 sends -> 2 interested,
  10 plain replies. Single-touch outbound at that volume is how you get 0.6%.
  Losing step 2 and step 3 makes the number worse, not better.
- **No unsubscribe or suppression list.** Instantly was carrying your CAN-SPAM
  and GDPR footing. Sending cold B2B mail from a raw Gmail OAuth connection
  with no opt-out mechanism and no cross-campaign suppression is a compliance
  regression, and one bad list means the reputation hit lands on your primary
  domain rather than a burner sending domain.

---

## What is actually worth taking

Two things, and neither requires adopting the tool:

1. **The prompt architecture in `src/emailGen.js`.** Outreach Profile as an
   injected lens (pain points / offer / tone / focus areas), three structural
   variants generated in parallel (Direct Value, Curiosity Gap, Peer
   Comparison), and hard output constraints — lowercase subjects, under 85
   words, no em dashes, no "I hope this finds you well." That is a good
   framework and it is signal-source agnostic. Your signal is a
   **verified-open posting with a URL**, which is stronger and more checkable
   than a review quote.

2. **Sheet-as-queue plus Gmail-draft staging with restart recovery**
   (`src/sheets.js`, `src/server.js`). If the review step stays in your loop
   by choice rather than by accident, this is a sane way to hold the queue.

The scraper, the Trustpilot resolution logic, and the review-category
taxonomy are dead weight for this business.

---

## Recommendation

**Do not swap.** Three moves instead, in order:

1. **If the goal is dropping the Instantly bill**, the like-for-like candidate
   is Plusvibe, which is already connected to this account and does the things
   in the gap table above — inbox rotation, warmup, sequences, reply
   detection, blocklist. That is a migration, not a rebuild.

2. **If the goal is better copy**, port `emailGen.js`'s profile-lens + 3-variant
   + hard-constraints pattern onto the verified-roles inventory and keep
   whatever sender you use. The signal upgrade (a live posting with a URL the
   recipient can check) is worth more than the platform choice.

3. **Neither of these is the binding constraint.** Sean Fitzmorris said "Sure"
   on 13 Jul and Peter Heyer asked "Did we not have a meeting?" — both drafts
   are written and sitting in Gmail. Two hand-raisers beat 395 cold sends on
   any platform. Ship those before touching the tooling.
