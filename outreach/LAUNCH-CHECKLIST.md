# Launch checklist — recruiter campaign

**Status on 31 Aug 2026: NOT CLEARED TO SEND.**

The sequence in `recruiter-sequence-2026-08-31.md` is finished copy. It cannot go out
tonight, and the reasons are not stylistic.

---

## Why it did not launch tonight

Two mechanical, one substantive.

**Instantly is unreachable from the build session.** `api.instantly.ai` and
`app.instantly.ai` are both refused at the egress proxy. Nothing can be pushed
programmatically from here; the campaign has to be pasted into the UI, or the curl calls
in `docs/instantly-api-setup.md` run from a machine with open network.

**Plusvibe is reachable but feature-locked.** The `arunroutes` workspace authenticates
and returns cleanly, but `list_campaigns` and `list_email_accounts` both return
*"You are not authorized to access this feature"*. That is an account permission, not a
bug. Worth fixing, because Plusvibe carries the blocklist and suppression the footer
promises and the Gmail path does not.

**The company-side campaign has nothing true to say yet.** It tells a hiring manager
"here are the candidates." We hold zero. It stays off until profiles exist.

---

## Seven blockers before the first send

Each one was raised by the compliance audits. None can be fixed in copy.

- [ ] **1. Fill six bracketed fields.** Surname, trading entity, street address, website,
      reply-to, privacy notice URL. A $5,000 obligation asserted by a first name is
      neither collectable nor lawful.
- [ ] **2. Build the suppression list.** The footer says "reply STOP and I will not email
      you again." Until that is enforced across every campaign, it is a false statement.
- [ ] **3. Write the one-page introduction fee agreement.** Step 2 promises it exists.
      This is the item `validated-intro-model-2026-08-31.md` flags as the one that gets
      skipped and loses the money.
- [ ] **4. Check employment-agency licensing.** NY and CA; UK Conduct of Employment
      Agencies Regulations for Cipher Cyber and Trident Search.
- [ ] **5. Record where each address came from.** `{{emailSource}}` cannot be populated
      truthfully otherwise, and GDPR Art 14 requires it.
- [ ] **6. Screen for sole traders.** Individual subscribers under PECR need consent, not
      legitimate interest. Altruistic Careers and High Impact Recruitment are one-person
      operations.
- [ ] **7. Use a separate sending domain.** Not the primary.

---

## The list

`inventory/recruiter-contacts-2026-08-31.csv` — 19 named people at 18 firms.

| Confidence | Count | Treatment |
|---|---|---|
| Verified by validation tool | 8 | safe to send |
| Guessed or published-but-unconfirmed | 10 | re-validate before sending |
| Not found | 1 | exclude |

The email-validation tool hit its free-tier daily cap mid-run (resets midnight UTC), which
is why several published-on-their-own-website addresses still read "guessed." Two need
care: `charlee.ryman@tridentsearch.co.uk` came back not-deliverable despite being printed
on his own team page — probably a UK Microsoft 365 tarpit, but re-check it. And
`marcelo.mansur@redbluesecurity.com` conflicts with a RocketReach pattern suggesting
`mmansur@`; `contact@redbluesecurity.com` is the safe fallback.

One live correction the recon turned up: **Cyberstrike's website still lists James
McDonagh as CEO. He stepped down in March 2026** and is now Chair. Solila McDonagh runs it
day to day.

---

## First cell, when cleared

**Role `20764`, AI Cyber Red Teamer at Trajectory Labs → RedBlue Security and Code Red
Partners.** Both High confidence. RedBlue's own live board is exploit developers,
vulnerability researchers and CNO tool developers, which is the requirement almost
verbatim.

Second cell: **`20741` MATS Residency → Thayon and Impact Ops.** Largest fee headroom on
the board at $155k–$285k, and both contacts are tool-verified.

## Rows excluded from the send

On the repo's own grading: `20723` (not a vacancy), `20675` (no search exists), `20698`
(closes 4 Sep, no recruiters matched), `20743` (NewsGuild, no fee to fund the $5,000),
`20684` (employer priced this hire at a $1,500 referral bonus), `20674` (closes 13 Sep,
step 3 would land after close). `20686` goes only to the two apolitical nonprofit firms —
never NRG, Movement Talent or Blueline, who are progressive against an explicitly
nonpartisan employer.

Of 33 matched pairs, 12 are High confidence. **21 must not send.**
