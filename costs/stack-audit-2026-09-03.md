# Stack audit — 3 Sep 2026

Applying The Algorithm from Eric Jorgenson's *The Book of Elon* (free edition, 2026)
to every recurring charge in the account. The order of the five steps is the whole
method:

> 1. Make your requirements less dumb.
> 2. Try very hard to delete the part or process.
> 3. Simplify or optimize.
> 4. Accelerate.
> 5. Automate.
>
> *"The most common mistake of smart engineers is to optimize a thing that should
> not exist."*

Every amount below is taken from a receipt or an Axis Bank AutoPay alert in
`arun.worc@gmail.com`. Nothing here is estimated.

---

## Step 1 — The requirement was dumb, and not in the way it looks

The stated requirement is "get cost to zero except Claude Code." That is correct
and it is worth ~$371/mo.

But the requirement underneath it was: **"I need cold-email infrastructure to
reach hiring managers at volume."**

That requirement is false, and the account proves it. Musk's test is that a
requirement must come from a *person* whose name you know. Tracing them:

| Requirement | Real author | Not |
|---|---|---|
| "Run Instantly at volume" | Jordan Platten, Skool *Agency Owners* — "How I Send 3,000 Cold Emails Every Day Using Instantly AI", 27 Jul 2026 | Arun. No customer. |
| "Buy managed MS inboxes" | Saad Belcaid, Sales Systems Mastery — the SSM playbook; ConnectorOS literally bills an "SSM tier" | Arun's own delivery numbers |
| "Route LLM calls through OpenRouter" | Nate Herk, AI Automation Society — "This Stealth Model Makes Claude Code Free", 22 Aug 2026 → card mandate 5 days later | Any workload that needed it |

The counter-evidence was already in the same inbox, unread. Ian Kirk, Skool
*Lead Gen Secrets*, 30 Jul 2026:

> "$450 a month for a machine that had never sent one email. That is what 100
> mailboxes and an Instantly account run you. Mine sat there for nine months."

Arun received the pitch and the warning in the same week and acted on the pitch.

**He had also already written himself the correct instruction.** Todoist P1
recurring task, authored by Arun on 17 Jun 2026, project *Gallium → First Paying
Customer*, still firing every weekday:

> "No email, no messages, no PlusVibe/Apollo/Skool, **NO NEW TOOLS** until the
> block is done… Musk pairing: run The Algorithm in order — question → DELETE →
> simplify → accelerate → automate. Don't optimize a thing that shouldn't exist."

On 6 Aug that task fired at 03:32 UTC. At 05:11 UTC he signed into opencode.ai.
The requirement was not missing. It was overridden.

---

## The bill

Verified recurring spend, excluding the one keep:

| Vendor | Plan | Monthly | Mandate / next charge |
|---|---|---:|---|
| Instantly | Hypergrowth Plan | **$97.00** | AutoPay `YXiu16qptv` · 12 Sep |
| Instantly | Hypergrowth **Inbox Placement** | **$97.00** | AutoPay `YcJSBDAvNU` · 25 Sep |
| ScaledMail (Beanstalk) | SM – Microsoft, 1 domain | $50.00 | cancelled 2 Sep, access to 14 Sep |
| HighSend (Lynth Management S.L.) | 100 inboxes, self-serve | $30.00 | AutoPay `YYGNPHX2am` · 17 Sep |
| Anomaly (anoma.ly) | opencode credits | ~$42.46 | on depletion (fired 2× in Aug) |
| Suno | Premier | ₹2,500 ≈ $25.14 | AutoPay `YYX13mBm6r` · 19 Sep |
| Hostinger | Google Workspace seat, arunroutes.com | ₹879 ≈ $8.84 | 15 Sep |
| OpenRouter | credit auto-reload | $10.80 | AutoPay `YcT0A5WAQv` · on depletion |
| Anthropic | API top-ups (**separate from Max**) | ~$10.00 | on depletion |
| | | **≈ $371/mo** | |

**Keep:** Anthropic Max 5x — $100.00/mo, next 27 Sep. Claude Code is the labour.

### Two things nobody had noticed

1. **Instantly is billed twice.** Two distinct Stripe subscriptions on one
   account (`acct_1JO8bKB3VEKBA0yg`) and two distinct Axis AutoPay mandates.
   Invoice `TKQKMVLG-0002` is "Hypergrowth Plan" (12 Aug–12 Sep, ₹9,646.85);
   invoice `TKQKMVLG-0003` is "Hypergrowth Inbox Placement" (25 Aug–25 Sep,
   ₹9,620.00). That is **$194/mo, not $97**. The second one was added 25 Aug.

2. **Anthropic bills twice too.** The $100 Max plan is one line. API credit
   auto-reload on `acct_1MExQ9BjIQrRQnux` is another, and it fires on depletion.
   Keeping Claude Code does not mean keeping this.

### Lapsed, but confirm they are actually closed

Not counted above — no live charge — but the account objects may still exist:

- **PlusVibe.ai** — $77/mo, a *third* cold-email platform. Last charge failed
  12 Jul 2026. It had expired once before, on 3 Jun, and was re-bought on 4 Jun.
- **ScaledMail $199/mo** — the original, larger plan. Lapsed on ignored card
  confirmations May–Jun 2026 rather than being cancelled.

---

## Step 2 — Delete

Everything in the table above is deleted, not replaced. There is no free
cold-email stack to migrate to, because the requirement it served is being
withdrawn.

The replacement for the entire outbound apparatus is one line:

> **`arun.worc@gmail.com`, sent one at a time, by a Claude Code session driving
> the Gmail MCP that is already connected.**

Free Gmail sends 500 recipients/day. July's peak was 395 sends in the whole
month — about 13/day, or 2.6% of one free mailbox. The infrastructure was never
serving a volume constraint.

Deleted with no replacement at all: **Suno** (₹2,500/mo, zero business use — no
audio artefact has ever been produced or sent), **OpenRouter** and **Anomaly
opencode credits** (both buy inference already bought at $100/mo), **Zapier**
(re-authorised 3 Sep; the Gmail MCP already does the job), **Skool digests**
(set all groups to Never — they are the source of the requirements being deleted).

## Step 3 — Simplify: what actually stays, at $0

| Need | Tool | Cost |
|---|---|---|
| Write, send, read replies | Gmail MCP → `arun.worc@gmail.com` | $0 |
| Verify a role is really open | `WebFetch` on the company's own ATS JSON (`boards-api.greenhouse.io/v1/boards/{token}/jobs`) — this *is* the primary source outreach rule 1 demands | $0 |
| Find a named contact | Apollo free (175 lead credits, **0 ever used**) | $0 |
| Inbound on the domain, if ever needed | Cloudflare Email Routing — 200 addresses, no message cap | $0 |
| Scheduling | Google Calendar MCP (already authorised) | $0 |
| Repo, history, cron | GitHub | $0 |

## Step 4 — Accelerate

Deleting the stack shortens the loop from *idea → hiring manager's inbox*,
because the cold inboxes were the latency: replies landed in mailboxes nobody
opened (see below). One mailbox that Arun actually reads is faster than 100 he
does not.

## Step 5 — Automate: not yet

Nothing gets automated until the manual loop has produced one paying customer.
Automating first is the Tesla-Fremont mistake. The one exception, later, is a
daily Claude Code job that reads the inbox and surfaces unanswered replies —
and only because that is the exact failure that already cost seven leads.

---

## Do it in this order — the sequencing is load-bearing

**Cancelling first destroys the leads.** Seven positive replies are sitting in
Instantly's Unibox and in ScaledMail/HighSend inboxes. Cancel those vendors and
the threads go with them. ScaledMail access already ends **14 Sep**.

1. **Harvest the replies first.** See `outreach/missed-replies-2026-09-03.md`.
   Answer all seven from `arun.worc@gmail.com`. This is today's work.
2. **Then** cancel, in renewal-date order:
   - Hostinger Workspace seat — before **15 Sep**
   - HighSend — before **17 Sep**
   - Suno — before **19 Sep**
   - Instantly Hypergrowth Plan — before **12 Sep**
   - Instantly Inbox Placement — before **25 Sep**
   - Export the Unibox before either Instantly cancellation.
3. **Kill the mandates at the bank, not just the vendor.** Axis AutoPay survives
   an in-app cancellation. Revoke `YXiu16qptv`, `YcJSBDAvNU`, `YYGNPHX2am`,
   `YYX13mBm6r`, `YcT0A5WAQv` directly.
4. **Turn off auto-reload** on Anthropic API, OpenRouter and Anomaly. These have
   no renewal date — they fire on depletion, which is why they are easy to miss.
5. Confirm PlusVibe and the legacy $199 ScaledMail plan are genuinely closed.

## Deliberately not cut

Musk's rule is that if you never add anything back, you did not delete enough.
Three lines survive on evidence, not sentiment:

- **Anthropic Max 5x, $100** — the labour that replaces all of the above.
- **Google One / Google AI Pro** — saves nothing (no charge evidenced) and
  downgrading drops the account to 15 GB shared. Over quota, Gmail stops
  *receiving* and mail is returned to sender. Do not touch it blind; check
  storage first.
- **Apollo free, Calendly free** — $0 already. Calendly in particular is still
  linked inside live Instantly sequence copy; deleting the account 404s a link
  a prospect may still click. Retire it only after the campaigns are stopped.

- **`arunroutes.com`** — worth its ~$10/yr as the brand. `getarunroutes.com`,
  `arunroutess.com` and `creativitymaxing.com` can lapse; they exist only to
  serve the cold-email pattern being deleted.
