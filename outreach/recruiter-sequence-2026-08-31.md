# Recruiter outreach sequence — 31 Aug 2026

One question. Nothing else.

The email's only job is to get a yes or a no. If it's a yes, there's a conversation, and
the conversation is where anything else gets explained. Nothing about fees, nothing asking
for profiles, nothing explaining how the desk works.

**Merge variables:** `{{firstName}}` `{{roleTitleLc}}` `{{company}}` `{{roleTitle}}`
`{{roleMode}}` `{{roleSpec}}` `{{roleUrl}}`

---

## Step 1 — day 0

**Subject:** `{{roleTitleLc}} — do you have someone?`

```
{{firstName}},

{{company}} is hiring a {{roleTitle}}. {{roleMode}}.
{{roleSpec}}.

That looked like your territory rather than mine.

Do you have someone?

Arun

Arun Routes · [address] · reply STOP and I'll leave you alone.
```

## Step 2 — day +3

**Subject:** _(in-thread, empty)_

```
{{firstName}} — a no is just as useful to me as a yes.

Arun

Arun Routes · [address] · reply STOP and I'll leave you alone.
```

## Step 3 — day +8

**Subject:** _(in-thread, empty)_

```
Taking that as a no, {{firstName}}. Won't chase.

Posting's here if it's useful to you directly: {{roleUrl}}

Arun

Arun Routes · [address] · reply STOP and I'll leave you alone.
```

---

## Worked example — Trajectory Labs to RedBlue Security

**Subject:** `ai cyber red teamer — do you have someone?`

```
Marcelo,

Trajectory Labs is hiring an AI Cyber Red Teamer. Remote, contract.
Frontier-model jailbreaks, offensive security background, CTF results or published CVEs.

That looked like your territory rather than mine.

Do you have someone?

Arun

Arun Routes · [address] · reply STOP and I'll leave you alone.
```

38 words.

---

## Merge values for the two launch cells

| Field | Trajectory Labs `20764` | MATS Research `20741` |
|---|---|---|
| `{{company}}` | Trajectory Labs | MATS Research |
| `{{roleTitle}}` | AI Cyber Red Teamer | Residency |
| `{{roleTitleLc}}` | ai cyber red teamer | ai safety residency |
| `{{roleMode}}` | Remote, contract | London, Berkeley or DC. $155k–$285k |
| `{{roleSpec}}` | Frontier-model jailbreaks, offensive security background, CTF results or published CVEs | Senior researchers with a substantial body of work, moving into or already in AI safety |
| `{{roleUrl}}` | https://www.trajectorylabs.com/careers/ai-cyber-red-teamer | https://www.matsprogram.org/residency |

---

## What happens on a yes

Not in the email. On the reply.

1. Ask what they've got. Their format, their pace.
2. Ask which employers they're already engaged with — as a standing list, not tied to this
   role, so the question doesn't point at the target.
3. Terms come up when they ask, or before anything reaches the employer. Never before.

## Still required before sending

Only two things, down from seven — the rest fell away with the copy that needed them.

- [ ] Fill `[address]` — a postal address is required in commercial email.
- [ ] Make STOP actually work. It's a promise in every send.
