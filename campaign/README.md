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
