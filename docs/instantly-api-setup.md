# Instantly v2 API — campaign setup reference

> Compiled 31 Aug 2026. This container cannot reach `api.instantly.ai` (blocked by the
> environment's egress policy), so none of these calls were executed — they are documented
> from Instantly's published API docs for you to run.
>
> Never commit an API key. Export it as `INSTANTLY_API_KEY` in your shell.

---

# Instantly.ai V2 API — creating and launching a campaign by hand

Base URL: `https://api.instantly.ai`. Every V2 path is under `/api/v2`.

Everything below is taken from Instantly's own OpenAPI document (`https://api.instantly.ai/openapi/api_v2.json`, mirrored at `developer.instantly.ai/api-reference/...`) and their help center. Where the docs are silent or self-contradictory I say so explicitly rather than filling the gap — see **Gaps and warnings** at the end.

Set this once in your shell:

```bash
export INSTANTLY_API_KEY="paste-your-v2-key-here"
```

---

## 1. Auth

Bearer token. From `developer.instantly.ai/getting-started/authorization`:

> We are using bearer token authorization.
> Add a new `header` to your request, called `authorization`, with the value: `Bearer {{key}}` — where `key` is your API key.

The OpenAPI security scheme confirms it:

```yaml
components:
  securitySchemes:
    ApiKeyAuth:
      type: http
      scheme: bearer
```

So the exact header is:

```
Authorization: Bearer <your key>
```

Smoke test (from the official Quickstart):

```bash
curl --request GET \
  --url "https://api.instantly.ai/api/v2/accounts?limit=5" \
  --header "Authorization: Bearer $INSTANTLY_API_KEY"
```

Error semantics, quoted from the Quickstart:

> - `401` means the API key is missing or invalid.
> - `403` means the API key does not have the required scope.
> - `429` means the workspace exceeded an API rate limit.

Keys are scoped. Create one in **Settings → Integrations → API Keys**. The endpoints in this doc need:

| Endpoint | Documented required scopes (any one of) |
|---|---|
| `POST /api/v2/campaigns` | `campaigns:create`, `campaigns:all`, `all:create`, `all:all` |
| `PATCH /api/v2/campaigns/{id}` | `campaigns:update`, `campaigns:all`, `all:update`, `all:all` |
| `POST /api/v2/campaigns/{id}/activate` | `campaigns:update`, `campaigns:all`, `all:update`, `all:all` |
| `POST /api/v2/campaigns/{id}/pause` | `campaigns:update`, `campaigns:all`, `all:update`, `all:all` |
| `POST /api/v2/leads/add` | `leads:create`, `leads:all`, `all:create`, `all:all` |

There is also a `402 Payment Required` on essentially every endpoint: "Workspace does not have an active paid plan."

---

## 2. Create a campaign

**`POST /api/v2/campaigns`**

Only two fields are required by the schema:

```yaml
required:
  - name
  - campaign_schedule
additionalProperties: false
```

`additionalProperties: false` matters — a typo'd or invented key is a `400`, not a silent ignore.

### How the sequence is shaped

The `sequences` field carries this warning verbatim in the spec:

> List of sequences (the actual email copy). Even though this field is an array, only the first element is used, so please provide only one array item, and add the steps to that array

So the shape is `sequences[0].steps[]`, and each step requires `type`, `delay`, `variants`.

### How day offsets / delays are represented — read this carefully

There is **no per-step "send on day N" field**. Offsets are expressed only as a relative wait, and the wait hangs off the *previous* step:

```yaml
delay:
  type: number
  description: The delay value before sending the NEXT email.
               The unit is determined by the delay_unit field (defaults to days).
delay_unit:
  type: string
  enum: [minutes, hours, days]
  default: days
```

Consequences you have to get right by hand:

- `delay` on step 1 is the gap **between step 1 and step 2**. It is not a wait before step 1 goes out.
- `delay` is in the `required` list for *every* step, including the last one, where it has nothing to delay. Send a value anyway (`0` or whatever) or the request is rejected.
- To build "day 0, day +3, day +7", set step 1 `delay: 3`, step 2 `delay: 4`, step 3 `delay: 0`. The offsets are cumulative, not absolute.
- `pre_delay` / `pre_delay_unit` look like the "delay before the first email" knob but are not, for campaigns. The spec: *"**Only applicable to subsequences** — this field is ignored for regular campaigns."*

Variant fields:

```yaml
variants:
  items:
    properties:
      subject: {type: string, example: "Hello {{firstName}}"}
      body:
        type: string
        description: Email body HTML. Use `<br/>` tags for delivered email line breaks.
      v_disabled:
        type: boolean
        description: Whether this variant is disabled. By default, all the variants
                     are enabled. Please set this to true if you want to disable this variant
    required: [subject, body]
```

`body` is HTML. Use `<br/>`, not `\n`. A follow-up step with an empty `subject` (`""`) threads under the previous email in the Instantly UI convention; the schema still requires the key to be present.

### How the schedule is set

`campaign_schedule.schedules` is an array (multiple named sending windows are allowed) and each entry requires all four of `name`, `timing`, `days`, `timezone`:

- `timing.from` / `timing.to` — 24-hour `HH:MM`, validated against `^([01][0-9]|2[0-3]):([0-5][0-9])$`. `"09:00"`, not `"9:00"`.
- `days` — an object with string keys `"0"`–`"6"` mapped to booleans. `minProperties: 1`, so you may send a subset, but send all seven to be unambiguous. **Which index is which weekday is not documented — see Gaps below.**
- `timezone` — an IANA string from a closed enum of ~102 values (`America/Chicago`, `America/New_York` is *not* in the list; `America/Detroit` is — check the enum before assuming). Timezone lives **per schedule entry**, not at campaign level.
- `campaign_schedule.start_date` / `end_date` — optional, `YYYY-MM-DD`, and per the spec "Uses the campaign's timezone."

### Full example

```bash
curl --request POST \
  --url "https://api.instantly.ai/api/v2/campaigns" \
  --header "Authorization: Bearer $INSTANTLY_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
  "name": "Q3 Outbound - Ops Leaders",
  "campaign_schedule": {
    "start_date": "2026-09-07",
    "schedules": [
      {
        "name": "Business hours",
        "timing": { "from": "09:00", "to": "17:00" },
        "days": {
          "0": false,
          "1": true,
          "2": true,
          "3": true,
          "4": true,
          "5": true,
          "6": false
        },
        "timezone": "America/Chicago"
      }
    ]
  },
  "sequences": [
    {
      "steps": [
        {
          "type": "email",
          "delay": 3,
          "delay_unit": "days",
          "variants": [
            {
              "subject": "Quick question about {{companyName}}",
              "body": "Hi {{firstName}},<br/><br/>Noticed you run ops at {{companyName}}. We help teams like yours cut onboarding time.<br/><br/>Worth a short call?<br/><br/>Best,<br/>Arun"
            }
          ]
        },
        {
          "type": "email",
          "delay": 4,
          "delay_unit": "days",
          "variants": [
            {
              "subject": "",
              "body": "Hi {{firstName}},<br/><br/>Bumping this in case it slipped past.<br/><br/>Arun"
            }
          ]
        },
        {
          "type": "email",
          "delay": 0,
          "delay_unit": "days",
          "variants": [
            {
              "subject": "",
              "body": "Last note from me, {{firstName | there}} — happy to close the loop if this is not a fit.<br/><br/>Arun"
            }
          ]
        }
      ]
    }
  ],
  "email_list": ["arun@yoursendingdomain.com"],
  "daily_limit": 100,
  "email_gap": 12,
  "random_wait_max": 5,
  "stop_on_reply": true,
  "stop_on_auto_reply": true,
  "link_tracking": false,
  "open_tracking": true,
  "text_only": true,
  "insert_unsubscribe_header": true
}'
```

Returns `200` with the full `Campaign` object. Grab `id` from it — you need it for every step that follows. The campaign does **not** start sending on create; you must call `/activate` (step 5).

Other create-time fields worth knowing (all optional, all `null`-able unless noted):

| Field | Meaning per spec |
|---|---|
| `email_list` | array of strings — "List of accounts to use for sending emails" |
| `daily_limit` | number — "The daily limit for sending emails" |
| `daily_max_leads` | integer, min 0 — "The daily maximum new leads to contact" |
| `email_gap` | number — "The gap between emails in minutes" |
| `random_wait_max` | number — "The maximum random wait time in minutes" |
| `stop_on_reply` / `stop_on_auto_reply` | boolean |
| `stop_for_company` | "stop the campaign for the entire company(domain) when a lead replies" |
| `text_only` / `first_email_text_only` | boolean |
| `link_tracking` / `open_tracking` | boolean |
| `insert_unsubscribe_header` | boolean |
| `match_lead_esp`, `prioritize_new_leads`, `allow_risky_contacts`, `disable_bounce_protect` | boolean |
| `cc_list` / `bcc_list` | arrays of email strings |
| `pl_value` | number — "Value of every positive lead" |
| `is_evergreen` | boolean |
| `auto_variant_select` | `{"trigger": "reply_rate"|"click_rate"|"open_rate"}` |
| `provider_routing_rules` | `[{action: send|do_not_send, recipient_esp: [...], sender_esp: [...]}]` |
| `limit_emails_per_company_override` | `{mode: custom|disabled, daily_limit: n, scope: per_campaign|across_workspace}` |

`status`, `core_variables`, `custom_variables`, `not_sending_status`, `organization`, `timestamp_*` are `readOnly` — do not send them.

Campaign `status` enum, for reading responses:

| Value | Meaning |
|---|---|
| `0` | Draft |
| `1` | Active |
| `2` | Paused |
| `3` | Completed |
| `4` | Running Subsequences |
| `-1` | Accounts Unhealthy |
| `-2` | Bounce Protect |
| `-99` | Account Suspended |

---

## 3. Add leads to a campaign

Two endpoints. Use the bulk one.

### Bulk (preferred) — `POST /api/v2/leads/add`

Doc description, verbatim:

> Adds up to 1000 leads to either a campaign or a list. You must provide a `campaign_id` or a `list_id`, but not both. The endpoint validates emails, checks against blocklists and existing leads.

Required: `leads` (array, `minItems: 1`, `maxItems: 1000`). Each lead object is `additionalProperties: false`, so **arbitrary top-level keys are rejected** — anything that isn't a named field must go inside `custom_variables`.

Named per-lead fields: `email`, `first_name`, `last_name`, `company_name`, `job_title`, `website`, `phone`, `personalization`, `lt_interest_status`, `pl_value_lead`, `assigned_to`, `custom_variables`.

Custom variables, quoted from the schema:

```yaml
custom_variables:
  type: object
  additionalProperties:
    type: [string, number, boolean, 'null']
  description: Custom variables can include any metadata about the lead that is
    relevant to the campaign, the campaign will be updated to allow all the other
    leads in the campaign to have the same custom variables. The custom variables
    will be added to the lead payload field
```

Note the two constraints: values may only be **string, number, boolean, or null** — no nested objects, no arrays; and adding a custom variable to one lead registers it on the campaign for all the others.

```bash
curl --request POST \
  --url "https://api.instantly.ai/api/v2/leads/add" \
  --header "Authorization: Bearer $INSTANTLY_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
  "campaign_id": "PASTE_CAMPAIGN_ID_HERE",
  "skip_if_in_workspace": true,
  "verify_leads_on_import": false,
  "leads": [
    {
      "email": "dana@acme.com",
      "first_name": "Dana",
      "last_name": "Reyes",
      "company_name": "Acme Logistics",
      "job_title": "VP Operations",
      "website": "https://acme.com",
      "phone": "+15125550142",
      "personalization": "loved your talk at ManifestMTL",
      "custom_variables": {
        "city": "Austin",
        "warehouseCount": 4,
        "pastCustomer": false,
        "renewalMonth": "November"
      }
    },
    {
      "email": "sam@northwind.io",
      "first_name": "Sam",
      "last_name": "Okafor",
      "company_name": "Northwind Freight",
      "job_title": "Head of Supply Chain",
      "custom_variables": {
        "city": "Chicago",
        "warehouseCount": 11,
        "pastCustomer": true,
        "renewalMonth": "March"
      }
    }
  ]
}'
```

When you pass `campaign_id`, `email` is mandatory on every lead. (With `list_id` instead, at least one of `email`, `first_name`, `last_name` is enough.)

Dedupe / hygiene flags:

- `skip_if_in_workspace` — "any lead that already exists anywhere in your workspace (in any campaign or list) will be skipped. **This option overrides the other `skip_if` flags.**"
- `skip_if_in_campaign` — skip if already in ANY campaign in the workspace
- `skip_if_in_list` — skip if already in ANY list
- `blocklist_id` — "If omitted, the workspace default blocklist is used."
- `verify_leads_on_import` — spawns a background verification job
- `assigned_to` — user UUID for all imported leads

The `200` response is a reconciliation summary, not a list of leads: `status`, `total_sent`, `leads_uploaded`, `in_blocklist`, `blocklist_used`, `duplicated_leads`, `skipped_count`, `invalid_email_count`, `incomplete_count`, `duplicate_email_count`, `remaining_in_plan`, and `created_leads[]` (each `{index, id, email, first_name, last_name, phone}`, where `index` maps back to your input array position). Read `leads_uploaded` against `total_sent` — a `200` does not mean all your leads landed.

### Single lead — `POST /api/v2/leads`

Same custom-variable semantics, but the campaign key is named `campaign` (not `campaign_id`):

```bash
curl --request POST \
  --url "https://api.instantly.ai/api/v2/leads" \
  --header "Authorization: Bearer $INSTANTLY_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
  "campaign": "PASTE_CAMPAIGN_ID_HERE",
  "email": "dana@acme.com",
  "first_name": "Dana",
  "company_name": "Acme Logistics",
  "custom_variables": {
    "city": "Austin",
    "warehouseCount": 4
  }
}'
```

Per the spec: "When using `campaign`: The `email` field is required."

### Optionally pre-register variable names — `POST /api/v2/campaigns/{id}/variables`

```bash
curl --request POST \
  --url "https://api.instantly.ai/api/v2/campaigns/PASTE_CAMPAIGN_ID_HERE/variables" \
  --header "Authorization: Bearer $INSTANTLY_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{ "variables": ["firstName", "companyName", "city", "warehouseCount"] }'
```

The array items are documented as "Custom or core variable names", example `firstName`. This is the endpoint that makes a variable appear in the campaign's variable dropdown; uploading leads with `custom_variables` also does it implicitly.

---

## 4. Daily send limit and delay between emails

These are plain campaign fields. Send them at create time (as in the example above) or patch them later.

| What you want | Field | Unit / type | Spec description |
|---|---|---|---|
| Daily send cap for the campaign | `daily_limit` | number | "The daily limit for sending emails" |
| Delay between consecutive emails | `email_gap` | number, **minutes** | "The gap between emails in minutes" |
| Jitter on top of that gap | `random_wait_max` | number, **minutes** | "The maximum random wait time in minutes" |
| Cap on *new* leads entered per day | `daily_max_leads` | integer, min 0 | "The daily maximum new leads to contact" |

**`PATCH /api/v2/campaigns/{id}`** — partial update, send only what changes:

```bash
curl --request PATCH \
  --url "https://api.instantly.ai/api/v2/campaigns/PASTE_CAMPAIGN_ID_HERE" \
  --header "Authorization: Bearer $INSTANTLY_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
  "daily_limit": 150,
  "email_gap": 15,
  "random_wait_max": 8,
  "daily_max_leads": 40
}'
```

`daily_limit` is the whole-campaign cap. Per-mailbox daily limits are a property of the **email account**, managed through `PATCH /api/v2/accounts/{email}` — I did not verify that field's exact name, so check the Account schema before setting it.

Also relevant to throughput and documented on the campaign: `limit_emails_per_company_override`, e.g. `{"mode": "custom", "daily_limit": 3, "scope": "per_campaign"}`.

---

## 5. Activate / launch, and pause

Both are `POST`, both take the campaign ID **in the path**, and — this is the part people get wrong — **neither defines a request body**. The OpenAPI entries for both list only a single `in: path` parameter named `id` and have no `requestBody` block at all.

### Launch (also used to resume a paused campaign)

**`POST /api/v2/campaigns/{id}/activate`** — summary in the docs is literally "Activate(start), or resume a campaign".

```bash
curl --request POST \
  --url "https://api.instantly.ai/api/v2/campaigns/PASTE_CAMPAIGN_ID_HERE/activate" \
  --header "Authorization: Bearer $INSTANTLY_API_KEY"
```

### Pause

**`POST /api/v2/campaigns/{id}/pause`** — summary "Stop(or pause) a campaign".

```bash
curl --request POST \
  --url "https://api.instantly.ai/api/v2/campaigns/PASTE_CAMPAIGN_ID_HERE/pause" \
  --header "Authorization: Bearer $INSTANTLY_API_KEY"
```

Both return `200` with the full updated `Campaign` object. Confirm the launch by reading `status` — `1` is Active, `2` is Paused.

If it activates but nothing sends, `GET /api/v2/campaigns/{id}` and read `not_sending_status` (readOnly), whose enum is self-explaining:

| Value | Documented meaning |
|---|---|
| `1` | Campaign is currently not within its sending schedule. |
| `2` | Campaign is currently waiting for a lead to process. |
| `3` | Campaign has reached its daily sending limit. |
| `4` | All sending accounts for this campaign have reached their daily sending limit. |
| `99` | Campaign is currently not sending due to an error. Please contact support for assistance. |

There is also `GET /api/v2/campaigns/{id}/...` sending-status detail endpoint documented as "Returns sending status data explaining why a campaign may not be sending emails or is sending slower than expected."

---

## 6. Merge tag syntax

### Built-in lead variables: camelCase, double braces

`{{firstName}}` — **not** `{{first_name}}`.

Evidence, all from Instantly's own material:

- Sequence variant schema examples: `subject: "Hello {{firstName}}"`, `body: "Hey {{firstName}},<br/><br/>I hope you are doing well."`
- The `Add campaign variables` endpoint's variable-name example: `firstName`
- The `Lead.payload` object ("Lead custom variables") declares its known properties as `firstName`, `lastName`, `companyName`, `jobTitle`, `website`, `phone`, `personalization`
- Spintax help article: `{{firstName}}`, `{{companyName}}`

So the standard tags are:

```
{{firstName}}  {{lastName}}  {{companyName}}  {{jobTitle}}
{{website}}    {{phone}}     {{email}}        {{personalization}}
```

Note the naming shift: the **API request fields** are snake_case (`first_name`, `company_name`, `job_title`), but the **merge tags** that reference them are camelCase. You send `"first_name": "Dana"` and write `{{firstName}}`.

### Custom lead variables: the key name, verbatim

Whatever key you put in `custom_variables` becomes the tag, unchanged:

```json
"custom_variables": { "city": "Austin", "warehouseCount": 4, "renewalMonth": "November" }
```

→ `{{city}}`, `{{warehouseCount}}`, `{{renewalMonth}}`

From the help center:

> Custom Variables: For personalized columns or any additional data not in the predefined list, map them as 'Personalization' or 'Custom variable'. You can then use `{{columnName}}` variable in the campaign. **Custom variables should not be named similarly to the predefined variables.**

> **Are variables case-sensitive?** Yes. The custom variable name must exactly match your column header in the original file.

`{{City}}` will not resolve `city`. Pick a convention and hold it across every lead in the campaign.

### Fallbacks

```
{{variableName | fallback text}}
```

> Company name fallback: `{{companyName | your company}}` — If companyName exists, it uses company name. If missing, it uses `your company`.

Chainable: `{{firstName | lastName | for you}}` tries firstName, then lastName, then the literal.

### Spintax

```
{{RANDOM | Hi | Hello | Hey}} {{firstName}},
```

Variables nest inside spintax and vice versa: `{{RANDOM | Pay-Per-Appointment Meetings, {{companyName}} | Quick question {{firstName | there}}}}`

### Liquid conditionals

```
{% if position == "founder" %} As founder, you have to learn to delegate. {% endif %}
```

Documented system variables available to Liquid: `sendingAccountName`, `sendingAccountFirstName`, `sendingAccountEmail`, `sequence_email_opened` (boolean).

---

## Gaps and warnings — things the docs do not settle

**1. Which weekday is `days.0`? Genuinely undocumented, and the examples conflict.**

The OpenAPI schema gives keys `"0"`–`"6"` as bare booleans with no weekday labels anywhere — not in the property descriptions, not in the schedule docs, not in the help center. The official schema example is `{0:true, 1:true, 2:true, 3:true, 4:true, 5:false, 6:false}`, which reads as Mon–Fri if `0`=Monday. Third-party API mirrors show `{0:false, 1:true … 5:true, 6:false}` labeled "Weekdays", which reads as Mon–Fri only if `0`=Sunday. Those two cannot both be right.

Do not guess. Before your first real send: build one schedule in the Instantly UI with a single distinctive day enabled (say Wednesday only), then `GET /api/v2/campaigns/{id}` and read back which index is `true`. That resolves it in thirty seconds and costs nothing.

**2. Instantly's own docs are inconsistent about `{{first_name}}` vs `{{firstName}}`.**

The `Lead.payload.personalization` field carries the example string `"Hi {{first_name}}, I noticed you work at {{company_name}}..."` — snake_case. Several third-party API mirrors copy that snake_case form into their sequence-body examples too.

My read: that string is an *example of user-authored personalization text*, not a specification of tag names, and it contradicts every place Instantly actually specifies a variable name (all camelCase, listed above). Go with camelCase. But this is worth one empirical check before you launch to a real list — build a step in the UI, use the Variables dropdown to insert first name, and look at what it writes into the editor. Then use the campaign Preview against a real lead to confirm the tag resolves rather than rendering literally.

**3. `delay` on the final step is required but meaningless.** The schema requires it on every step; semantically it is "delay before the NEXT email" and there is no next email. Send `0`.

**4. There is no documented way to delay the first email of a regular campaign.** `pre_delay` exists but the spec states plainly it is subsequence-only and "ignored for regular campaigns." Use `campaign_schedule.start_date` to control when the campaign begins.

**5. `email_list` validation is not documented.** The spec says only "List of accounts to use for sending emails" — it does not state what happens if you pass an address that is not a connected, warmed account in the workspace. Verify your senders with `GET /api/v2/accounts` first.

**6. The `timezone` enum is closed and idiosyncratic.** ~102 IANA values, and it is not the full tz database. `America/New_York` is absent; `America/Detroit` is present. Pull the enum from the create-campaign reference page and pick from it rather than assuming your usual zone string is accepted.

**7. Per-mailbox daily limits** are an Account-level setting, not a campaign one. I did not verify that field name and am not going to name it here.

**8. Rate limits** exist per workspace (`429`) and a few endpoints carry lower-than-default caps — `GET /api/v2/emails` is documented at 20 req/min and `POST /api/v2/emails/test` at 10 req/min. See `developer.instantly.ai/getting-started/rate-limit`.

---

## Order of operations, condensed

```bash
# 1. create (returns id; campaign is not sending yet)
CID=$(curl -s -X POST "https://api.instantly.ai/api/v2/campaigns" \
  -H "Authorization: Bearer $INSTANTLY_API_KEY" \
  -H "Content-Type: application/json" \
  -d @campaign.json | python3 -c 'import sys,json;print(json.load(sys.stdin)["id"])')

# 2. leads
curl -s -X POST "https://api.instantly.ai/api/v2/leads/add" \
  -H "Authorization: Bearer $INSTANTLY_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"campaign_id\":\"$CID\",\"leads\":[...]}"

# 3. adjust limits if not already set at create
curl -s -X PATCH "https://api.instantly.ai/api/v2/campaigns/$CID" \
  -H "Authorization: Bearer $INSTANTLY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"daily_limit":150,"email_gap":15}'

# 4. launch (no body)
curl -s -X POST "https://api.instantly.ai/api/v2/campaigns/$CID/activate" \
  -H "Authorization: Bearer $INSTANTLY_API_KEY"

# 5. verify status == 1
curl -s "https://api.instantly.ai/api/v2/campaigns/$CID" \
  -H "Authorization: Bearer $INSTANTLY_API_KEY"

# pause when needed (no body)
curl -s -X POST "https://api.instantly.ai/api/v2/campaigns/$CID/pause" \
  -H "Authorization: Bearer $INSTANTLY_API_KEY"
```

Reference pages used: `developer.instantly.ai/getting-started/authorization`, `/quickstart`, `/api-reference/campaign/create-campaign`, `/api-reference/campaign/activatestart-or-resume-a-campaign`, `/api-reference/campaign/stopor-pause-a-campaign`, `/api-reference/campaign/add-campaign-variables`, `/api-reference/lead/add-leads-in-bulk-to-a-campaign-or-list`, `/api-reference/lead/create-lead`, plus help.instantly.ai articles 6135930 (variables), 6384663 (spintax and fallbacks), 6687668 (liquid syntax).