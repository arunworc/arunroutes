# Recruiter outreach sequence — 31 Aug 2026

Cold 3-step sequence to recruitment firm principals, asking whether they hold a matching
candidate. Chosen by judge panel from three independent drafts, then corrected against every
finding from three hostile compliance audits.

**Status: DRAFT. Not loaded, not sent.** Seven pre-send blockers are listed at the bottom and
all of them are real. Per README rule 5, this is worth nothing until it ships.

**Angle:** Sell the one thing a recruiter cannot self-source: a hiring manager who has read their candidate and asked to meet. Give the posting away free, price only the introduction, and volunteer every weakness (cold, brand new, zero placements, likeliest outcome is silence) before they can find it.

**Merge variables:** `{{firstName}}`, `{{firmSpecialism}}`, `{{roleTitleLc}}`, `{{roleTitle}}`, `{{roleDetail}}`, `{{roleVerifiedDate}}`, `{{roleUrl}}`, `{{emailSource}}`

---

## Step 1 — day +0

**Subject:** `cold pitch, {{roleTitleLc}}, $5,000 only if the employer asks to meet`

```
{{firstName}}, your site lists {{firmSpecialism}}, which is why I picked you. Tell me if I have that wrong.

Open posting: {{roleTitle}}, {{roleDetail}}. I last confirmed it live on {{roleVerifiedDate}}. I do not hold it: public posting, no relationship with the employer.

Where I stand: one-person desk, no placements, no candidates on my books.

If you have someone, send one profile with employer, dates and any one-off achievement stripped. It goes to one hiring manager and nobody else, and I delete it if this dies.

I will then approach that hiring manager cold and try to turn it into a real conversation. That is the whole promise.

If they ask to meet your candidate, I introduce your firm and invoice USD 5,000. If they pass, or never reply, which is likeliest, you owe nothing.

Have someone?

Arun

--
Commercial solicitation. [ARUN SURNAME], [trading entity], [street address, city, postcode, country]. [website] | [reply-to address]
Not interested? Reply STOP and I will not email you again, about this role or any other.
I got your work address from {{emailSource}}. I am contacting you on a legitimate-interest basis for business-to-business purposes. You can object at any time and I will erase your details. Privacy notice: [url]
```

## Step 2 — day +3

**Subject:** `{{roleTitleLc}}, what the $5,000 is and is not`

```
Two things I left out.

You can find this posting in one search and go direct. You would owe me nothing. That is a real option and I will not pretend otherwise.

So the USD 5,000 is not for the link and not for access. It is billed once, when I introduce your firm to a hiring manager who has read your candidate's profile and asked to meet. Due on that introduction, not on a hire. Nothing if they pass, nothing if they go quiet, nothing if they already had your candidate by another route.

Worth repeating: no placements yet, no case studies.

Nothing to sign to send me a profile. One page gets signed before I name the company: that number, that trigger, nothing else on it.

I take no share of what you agree with the employer. I also do not know what they pay, or whether they use agencies at all.

Arun

--
Commercial solicitation. [ARUN SURNAME], [trading entity], [street address, city, postcode, country]. [website] | [reply-to address]
Not interested? Reply STOP and I will not email you again, about this role or any other.
I got your work address from {{emailSource}}. I am contacting you on a legitimate-interest basis for business-to-business purposes. You can object at any time and I will erase your details. Privacy notice: [url]
```

## Step 3 — day +8

**Subject:** `{{roleTitleLc}}, last one, and here is the link`

```
Last one from me on this.

No reply is a complete answer and I will not chase it.

The posting is {{roleUrl}}. I last confirmed it open on {{roleVerifiedDate}}, so check it before you spend time. Yours to work directly, no fee, no involvement from me.

That is deliberate. If a link were all I had to sell, I would have nothing to sell.

If someone lands on your bench later, reply here whenever.

Arun

--
Commercial solicitation. [ARUN SURNAME], [trading entity], [street address, city, postcode, country]. [website] | [reply-to address]
Not interested? Reply STOP and I will not email you again, about this role or any other.
I got your work address from {{emailSource}}. I am contacting you on a legitimate-interest basis for business-to-business purposes. You can object at any time and I will erase your details. Privacy notice: [url]
```


---

## Rationale, audit fixes and pre-send blockers

WHICH ANGLE WON: Sequence 3, the free call option. Three reasons.

1. It is the only angle whose economics match the repo's own conclusion. notes/access-model-review-2026-08-31.md ranks four things a recruiter cannot self-source and lands on item 4, "a hiring manager who has already agreed to look at one shortlist," as the product; notes/validated-intro-model-2026-08-31.md says the same, "what is sold is not a job link, it is an employer who has already seen this firm's specific candidate and said yes." Sequences 1 and 2 describe the deliverable but price it vaguely against "the approach." Sequence 3 prices it against the exact scarce asset. That is also why it survives rule 2: it says out loud which of the two products is on offer.

2. The fee is in the subject line of email 1 and framed as risk removal rather than cost. The brief warns that a recruiter who discovers a fee at step 4 disengages and tells people. Sequence 3 makes that impossible.

3. Its defects were wording, not structure. Sequence 2 had a live logical contradiction (step 2 "I hold the company name back" vs step 3 "ask and I will send the link") and a fabricated count ("I hold five others" reconciles to neither inventory file), plus its whole angle rests on a generated {{firmProof}} in line one, in an account with documented fabricated specifics in the July drafts. Sequence 1 was truthful but gave a busy principal the least reason to care.

LINES GRAFTED IN:
- From Sequence 1 step 2, the strongest line in all three sets: "You can take that link and go direct. You would owe me nothing. That is a real option and I am not going to pretend otherwise." Now opens step 2 as "You can find this posting in one search and go direct. You would owe me nothing. That is a real option and I will not pretend otherwise."
- From Sequence 1's audit rewrite of "You cover {{specialism}}": "Your site lists {{specialism}}, which is why I picked you, tell me if I have that wrong." Now the step 1 opener, replacing Sequence 3's flat assertion.
- From Sequence 1's rationale: the two-column {{role_title_lc}} / {{role_title}} trick, adopted as {{roleTitleLc}} (subjects) and {{roleTitle}} (body), so lowercase subjects never force a miscased proper noun in the body.
- From Sequence 2 step 1: the volunteered four-part disclosure, compressed to "Where I stand: one-person desk, no placements, no candidates on my books." Sequence 3 buried a thinner version at the bottom; this moves it above the ask.
- From Sequence 2's audit rewrite: the humility beat "You would know better than I would," compressed into "Tell me if I have that wrong."
- From Sequence 2 step 2's instinct that candour beats concealment, rebuilt as step 3's closer: "That is deliberate. If a link were all I had to sell, I would have nothing to sell."
- Kept from Sequence 3: the free-call-option frame, the fee in the subject, and step 3 publishing the URL unconditionally, which is the single largest credibility purchase available and costs a fee that was never going to be collected from a non-responder.

EVERY FIX FROM THE WINNER'S AUDIT (14 violations):
1. "The $5,000 buys one thing" retired. Now "the USD 5,000 is not for the link and not for access. It is billed once, when I introduce your firm to..." plus the no-relationship and no-guarantee disclosure in step 1.
2. "I approach the hiring manager directly with it" restored to rule 4 verbatim in substance, with "try" back in and the cold admission attached: "I will then approach that hiring manager cold and try to turn it into a real conversation. That is the whole promise."
3. "I hold a live posting" removed everywhere. Now "Open posting: ... I do not hold it: public posting, no relationship with the employer." Verification date moved into email 1, where the freshness claim is actually made.
4. Fee branches corrected: silence added as the named likeliest outcome; the firm, not just the profile, is what gets introduced; currency stated as USD; billed once per introduction; due on introduction, not on a hire.
5. "Nothing to sign to try it" corrected to "Nothing to sign to send me a profile. One page gets signed before I name the company," which aligns the copy to validated-intro-model item 4, the step that note says "gets skipped and loses the money."
6. The word "anonymised" deleted from the entire sequence. All three audits are right that on thin pools this is pseudonymised personal data, not anonymous. Replaced with the operative instruction plus purpose limitation, no onward transfer and retention: "send one profile with employer, dates and any one-off achievement stripped. It goes to one hiring manager and nobody else, and I delete it if this dies."
7. Empty subjects on steps 2 and 3 replaced with real ones. No fake "Re:" on a conversation that never happened.
8. "This is the final email in the sequence, so nothing further arrives from me" deleted. Replaced by an actual invocable mechanism in the footer of all three emails.
9. Verification date reworded to what it really is, plus "check it before you spend time," and a re-verify-before-each-step gate in ops below.
10. {{firmSpecialism}} downgraded from assertion to sourced observation and gated to High-confidence rows only. The matches CSV is 12 High, 17 Medium, 4 Low; 21 of 33 rows must not send.
11. {{roleDetail}} merge discipline specified below.
12. Subject line overclaim fixed by naming it: "cold pitch."
13. Pipeline carve-out added: "nothing if they already had your candidate by another route."
14. The brand-new disclosure now carries into step 2 ("Worth repeating: no placements yet, no case studies") instead of appearing once and being quietly withdrawn.

FIXES CARRIED ACROSS FROM THE LOSING AUDITS:
- Seq 1: "roles I am holding" possession framing eliminated sequence-wide. Seq 1's step-3 removal promise replaced with a real mechanism. Seq 1's definite-article subject ("the X role") avoided.
- Seq 1 and Seq 2: "Whatever you agree with the employer is yours" / "Your fee with the employer stays yours" both spoke for a third party we have never contacted. Replaced with "I take no share of what you agree with the employer. I also do not know what they pay, or whether they use agencies at all."
- Seq 2: identical fee-trigger wording now used in steps 1 and 2 (employer asks to meet), so the trigger cannot be read two ways.
- Seq 2: the withheld-name contradiction is gone. This sequence never claims a withholding policy; step 2 concedes the posting is one search away and step 3 hands it over, so the two are consistent.

COMPLIANCE BLOCK, in the footer of all three emails: commercial-solicitation identification, sender identity, physical postal address, an opt-out mechanism in every message rather than only the last, GDPR Art 13 controller identity, Art 14 source disclosure via {{emailSource}}, the legitimate-interest basis, an Art 21 right-to-object sentence presented separately, and a privacy-notice link.

HARD PRE-SEND BLOCKERS I CANNOT FIX IN COPY. These are real and the sequence must not launch until they are cleared. Inventing values for them would itself break rule 1, so they ship as visible brackets:
1. Fill [ARUN SURNAME], [trading entity], [street address], [website], [reply-to address], [privacy notice url]. Six brackets. A $5,000 obligation from a first name is not collectable and not lawful.
2. Build the suppression list before the first send. notes/instantly-replacement-2026-08-31.md records the current Gmail-draft path has zero unsubscribe, opt-out or blocklist and no cross-campaign suppression. Route through Plusvibe, which that same note recommends and which is already connected and carries blocklist, sequences and reply detection. Until STOP is actually enforced across every campaign, the footer sentence is a false statement.
3. Write the one-page introduction fee agreement. Step 2 now promises it exists.
4. Clear employment-agency licensing (NY, CA; UK Conduct of Employment Agencies Regulations for UK-based firms such as Cipher Cyber and Trident Search).
5. Record a legitimate-interests assessment and the per-row source of every address, or {{emailSource}} cannot be populated truthfully.
6. Screen the list for sole traders and unincorporated partnerships, who are individual subscribers under PECR and need consent. Impact Ops, Altruistic Careers and High Impact Recruitment are flagged in the matching note as one-person operations.
7. Use a separate sending domain, not the primary.

MERGE DISCIPLINE, enforced as pre-send validation that blocks any row with an empty field:
- {{firmSpecialism}}: literal phrase from the firm's own site, with the source URL stored on the row. High-confidence rows only.
- {{roleDetail}}: company-stated facts only, about twelve words. Any estimated band must read "estimate, not company-stated" (AEVEX's band in verified-roles-2026-08-29.md is a Salary.com estimate). Contract engagements must say "contract, not a permanent placement," which matters most for Trajectory Labs, where the recruiter earns margin on rate and $5,000 is a bigger bite than the placement-fee arithmetic assumes.
- {{roleVerifiedDate}}: re-checked immediately before each of the three steps fires, with the row suppressed if the posting closed. Verification decays, and the inventory already contains a pull-and-repost (Suvoda, pulled 22 Jul, back).
- {{roleTitleLc}} lowercase; {{roleTitle}} properly cased.

ROWS EXCLUDED FROM THE SEND, on the repo's own grading: 20723 Institute for Law & AI (not a vacancy), 20675 GovAI EiR (no search exists), 20698 Encode (closes 4 Sep, zero recruiters matched), 20743 NYT (NewsGuild, direct application, no contingency fee to fund the $5,000), 20684 CAIS (priced at a $1,500 referral bonus), 20674 GovAI DC (closes 13 Sep; step 3 would land after close). 20686 Humans in Control only to the two apolitical nonprofit firms, never NRG, Movement Talent or Blueline Fellows, who are progressive against an explicitly nonpartisan employer.

LAUNCH CELL: 20764 Trajectory Labs AI Cyber Red Teamer to RedBlue Security and Code Red Partners, both High confidence, the pairing validated-intro-model names as the best first cycle. Second cell 20741 MATS Residency to Thayon and Impact Ops, the largest fee headroom at $155k to $285k.

ONE DELIBERATE TRADEOFF, flagged rather than hidden. The three source rationales all targeted under 90 words. This lands at 136 / 155 / 75 body words plus a fixed 66-word footer. The 90-word target is a style heuristic ported from emailGen.js; the honesty rules are hard constraints. Where they collided I kept the constraint, because the shorter version of these emails is the version that lies. Every added sentence is a specific audit fix, not decoration.

REPLY HANDLING, since the copy sets expectations the desk must meet: on a yes, collect which employers the firm is already engaged with as a standing list rather than per-role, per validated-intro-model leak 2, so the question does not reveal the target. Strip employer, tenure dates and single-instance achievements before showing anything to an employer, and accept that on the Trajectory seat some profiles cannot be safely shown at all.

Per rule 5, this is a draft. It is worth nothing until the seven blockers are cleared and it is loaded and launched.