# Company outreach sequence — STAGED, DO NOT SEND

**This campaign must stay switched off until we physically hold candidate profiles.**

It tells a hiring manager we have candidates for their open role. We currently hold zero. Sending
it before profiles exist repeats the July failure that README rules 1 and 3 exist to prevent.

**Angle:** The only thing a hiring manager cannot get from their own job board is a pre-screened shortlist that costs them nothing to look at, so the email leads with the profiles, discloses the cold and unproven position up front, and asks for one number or a no.

**Merge variables:** `{{first_name}}`, `{{role_title}}`, `{{role_title_lower}}`, `{{candidate_count}}`, `{{candidate_block}}`, `{{candidate_1}}`, `{{candidate_2}}`, `{{candidate_3}}`, `{{candidate_4}}`, `{{candidate_5}}`, `{{role_url}}`, `{{source_verified_date}}`

---

## Step 1 — day +0

**Subject:** `{{candidate_count}} anonymised profiles for your {{role_title_lower}} role`

```
{{first_name}}, I saw your {{role_title}} posting. Cold email, no referral, we have not met.

New one person desk, no placements yet. I source through specialist recruitment firms. {{candidate_count}} of their candidates, anonymised, as the firms describe them:

{{candidate_block}}

Which one, if any, should I try to introduce you to? One number, or none. You pay nothing, ever. My fee comes from the recruiting side.

Arun
```

## Step 2 — day +4

**Subject:** _(in-thread, empty)_

```
{{first_name}}, one follow up, then I stop.

The {{candidate_count}} anonymised profiles I sent for {{role_title}} are all I hold. If one is worth a conversation, reply with its number and I will ask the firm that holds them to make the introduction. If none are, no reply needed. Silence closes this and I will not write again.

Arun
```


---

## Rationale, audit fixes and pre-send blockers

WHAT THE COPY DOES AND DOES NOT CLAIM. Step 1 discloses three things in its first fourteen words that most cold email hides: this is cold, nobody referred me, we have not met (README rule 2). It then states the position plainly, \"new one person desk, no placements yet\", so no reader can infer a track record we do not have (rule 3). Nothing anywhere in either step contains a placement count, a revenue figure, a client name, a testimonial, or a named candidate detail. The only promise made is \"should I try to introduce you to\" and \"I will ask the firm that holds them to make the introduction\" (rule 4, mirrored for the demand side: we can attempt an introduction, we cannot guarantee a candidate says yes). \"As the firms describe them\" attributes the profile claims to their actual source, since we do not independently verify a recruiter's description of their own candidate. \"You pay nothing, ever. My fee comes from the recruiting side\" is true and is the whole reason looking is costless. Step 2 is an in-thread reply with an empty subject, it names silence as an acceptable answer, and it commits to stopping, so a non-reply is honoured rather than punished.

MERGE VARIABLE STRUCTURE. candidate_1 through candidate_5 are the CSV columns holding one anonymised one-liner each. Three are required, four and five are optional and must be uploaded as empty strings when unused. candidate_block is the assembled, numbered block that renders in the body, built at upload from whichever slots are filled, so an unused slot cannot leave a stray blank line or a dangling number. candidate_count must be set to the number of filled slots and must be validated equal, or the email says three and shows four. role_title_lower keeps the subject genuinely lowercase, since {{role_title}} renders with capitals. role_url and source_verified_date are QA columns, not rendered, carried so any row can be re-checked against its primary source before send.

WORD COUNT. The authored copy is 65 words in step 1 and 58 in step 2, both under 90, no em dashes, lowercase subject, no pleasantries. The profile block is payload on top of that. Cap each one-liner at 10 words and the rendered step 1 stays near 90 at three profiles. At five profiles it will exceed 90. Default to three, treat four or five as a deliberate, logged exception. Step 2 must be sent as a threaded reply with the original quoted, though the wording stands alone if quoting fails.

WHAT MUST EXIST BEFORE THIS CAMPAIGN MAY BE SWITCHED ON. This is staged, not sent, and today it is unsendable, because we hold zero candidate profiles. Every item below must be true per lead row, not in general.

1. Profiles in hand. At least three anonymised one-liners per row, supplied in writing by a named specialist recruitment firm, for a real candidate who is currently open to this kind of role and who has consented to anonymised circulation. No row ships with a slot we wrote ourselves.
2. Anonymisation cleared. Each one-liner passes the standard in notes/validated-intro-model-2026-08-31.md: employer stripped, tenure dates stripped, no single-instance achievement that names the person by implication. This binds hardest on the Trajectory Labs red teamer, where the pool is thin enough that one bragging line identifies an individual. Any profile that cannot be safely shown is dropped, not softened.
3. Conflict check done. The firm's standing list of employers it is already engaged with has been collected and checked, so we are not presenting a candidate who is already in that company's pipeline directly or through another agency.
4. Role re-verified on the send date. The posting must be confirmed live at role_url that morning, with source_verified_date stamped. Nothing sends against a stale posting. The GovAI DC Research Manager closes 13 Sep 2026 and must be removed from the list after that date.
5. Named human recipient. first_name must be a real, verified hiring manager or hiring lead at that company with a checkable address. No info@, no guessed role owner, no generic inbox.
6. Row integrity check. candidate_count equals the number of filled slots, candidate_block renders correctly, role_title_lower is populated, and a human has read every assembled row before launch.
7. The fee instrument exists. \"My fee comes from the recruiting side\" describes a fee we currently have no signed instrument for. The one page introduction fee agreement (item 4 of \"what to build next\") must exist and be signed with the supplying firm before we tell an employer how we get paid.
8. Sending hygiene. Suppression list, unsubscribe path, reply detection and auto-pause on reply, sender domain and warmup all in place, per notes/instantly-replacement-2026-08-31.md.

Until items 1 through 8 are true, this sequence sits paused. A draft is not a send, and a send without profiles behind it would be the exact fabrication rule 3 was written to stop.