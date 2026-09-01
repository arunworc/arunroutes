# Campaign — recruiter ask, launch cells

`instantly-import-launch-cells.csv` imports straight into Instantly. Copy lives in
`../outreach/recruiter-sequence-2026-08-31.md`.

## Instantly settings

| Setting | Value | Why |
|---|---|---|
| Daily send limit | 10 | The list is 7. One day's sending. |
| Delay between emails | 15–25 min, randomised | Default hygiene. |
| Sending window | 08:00–17:00 recipient-local | Four of seven are UK. |
| Days | Mon–Thu | Friday sends to recruiters die. |
| Sending domain | **separate from primary** | Do not burn the main domain on a cold test. |
| Stop on reply | **on** | The whole point is the reply. |
| Open/click tracking | **off** | Tracking pixels hurt deliverability and this list is tiny — you will read every reply by hand anyway. |

## Columns

`email` `firstName` `companyName` `emailStatus` `roleTitleLc` `roleTitle` `roleMode` `roleSpec`

Everything except `email`, `firstName` and `emailStatus` is a merge variable used by the copy.
`emailStatus` is for your filtering, not for sending.

## Before you import

- [ ] Re-validate the four `guessed` addresses. The validator was rate-capped when this was
      built; it resets midnight UTC. `charlee.ryman@tridentsearch.co.uk` previously came back
      not-deliverable despite being printed on his own team page — likely a UK Microsoft 365
      tarpit, but check. For RedBlue, `contact@redbluesecurity.com` is the safe fallback if
      `marcelo.mansur@` bounces.
- [ ] Fill `[address]` in the copy footer.
- [ ] Make STOP actually work — it is promised in every send.

## What is deliberately not here

Held back, with reasons, from a 26-firm list:

| Firm | Why |
|---|---|
| Cyberstrike Group | Cleared GovCon only. Wrong niche for a remote contract role. |
| SteadRise | Says it connects people "not via a recruiter" — a network, cannot take a fee. |
| Slone Partners | Exec and leadership skew, not offensive practitioners. |
| CYVANT, Nexo, Tykhe | Generic inbox only. A first-name opener into `info@` reads as a blast. |
| Blackmere, Lateral, Codesearch AI, Higher, Altruistic Careers | No address found yet. |

Lateral is worth chasing once an address exists: founder Rob Infantino recruited at OpenAI and
AWS AI, and the firm was acquired by Riviera Partners in June 2026 — so the approach now reaches
Riviera's reach as well.

The eight nonprofit and media firms in the contact list match no launch cell. They map to the
CAIS, Tarbell and Humans in Control roles, all of which the grading excluded.

---

## Full recruiter campaign — 2026-09-01

`instantly-READY.csv` — 34 firms, one row each, decision-maker email + merge fields.
34 A/B-graded firms with a named contact and a working (or pattern-confirmed) address.
The C-grade firms and three with no findable email are held in `instantly-READY-full.csv`.

`instantly-push.sh` — the exact Instantly v2 API calls (create campaign, add leads, activate).
Runs on YOUR machine; this container cannot reach api.instantly.ai (org egress policy, 403).

### One email per FIRM, not per role
Each firm is asked once about the single best-fit role in its cell. The board's 99 A-tier
roles collapse to three "ask" archetypes (cyber / ai-research / ops-exec) so a recruiter
gets one relevant question, not a list.

### Before running instantly-push.sh
- [ ] Rotate the Instantly API key (the one pasted in chat is compromised) and export the new one.
- [ ] Replace [ADDRESS] in the sequence body with a real postal address (CAN-SPAM).
- [ ] Confirm STOP handling / suppression is on in the workspace.
- [ ] Re-check the 13 `pattern`-status emails; they are inferred, not confirmed. Verify or drop.

### Contact-quality notes from discovery
- Adeptis Group: offensive-desk owner Ryan Virani LEFT to found CyberMoves; MD Hubert Colvin is the fallback.
- Nicoll Curtin / BeecherMadden: entire former cyber leadership departed; Philip Quinn is the live pentest contact.
- Harrington Starr: defensive/regulatory cyber, NOT offensive — weak fit, kept as B only.
- C-Serv: generalist "deployed pods" firm, not a pen-test placer — no personal email found.
- Understanding Recruitment: the discovered email was on a different firm's domain; blanked pending verification.
