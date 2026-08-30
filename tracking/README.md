# Tracking — the deal ledger

If you can't track it, you can't fix it. Every company worked by hand gets
two artifacts, created the day work starts and updated as events happen:

1. **A row in `companies.csv`** — the database. Machine-readable, one row
   per company, used for win/loss analysis.
2. **A case file in `casebook/`** — the story. What we did, why we did it,
   how it ended. Used to find the *reasons* behind the numbers.

Mass campaigns get one row per campaign in `campaigns.csv` so both lanes
produce comparable reply rates.

Run `python3 scripts/report.py` for the current funnel, lane comparison,
and variable breakdowns.

## The operating loop

- **Daily:** work up to 10 companies in the manual lane. Each one gets its
  CSV row and case file the same day. Update rows the moment an event
  happens (sent, bounced, replied) — never from memory later.
- **Weekly:** run the report. Compare manual vs mass reply rates, and
  reply rates by angle / channel / seniority / email status. Kill what
  loses, double what wins, write the change into the next week's work.
- Case files are **append-only logs**, not essays. One dated line per
  event. The "lessons" section gets written when the company reaches a
  terminal stage — not before.

## Stage taxonomy (companies.csv `stage`)

| Stage | Meaning |
|---|---|
| researched | Target and decision-maker identified, no copy yet |
| staged | Copy written and staged (draft exists), not sent |
| sent | First touch delivered |
| replied | Any human response received |
| conversation | Live back-and-forth / call booked |
| deal | Money or signed agreement |
| dead | Terminal loss — set `outcome_reason` |

## Outcome reasons (`outcome_reason`, only when stage=dead)

`bounce` · `no_reply` (after full follow-up sequence) · `not_now` ·
`no_need` · `wrong_person` · `lost_to_competitor` · `we_withdrew` · `other`

## Variables we are testing (CSV columns — fill honestly)

- **lane**: manual | mass
- **channel**: email | linkedin_dm | both
- **dm_seniority**: founder | c_suite | vp | director | manager
- **email_status**: verified | pattern_inferred | unknown
- **angle**: short slug for the pitch construction, e.g. `work-first`
  (built the deliverable before contact), `intro-offer`, `role-inventory`.
  New angle = new slug; keep slugs consistent or the analysis dies.
- **asset**: attached | offered | none — was the work product attached,
  dangled, or absent
- **personalization**: 1 = template + name, 2 = one researched hook,
  3 = deep (their own words/customers/paths in the copy)
- **send_dow / send_hour_local**: recipient-local day and hour

## Rules

1. A row without a case file is a number nobody can explain. A case file
   without a row is a story nobody can count. Always both.
2. Update on event, not on schedule. Stale data is worse than no data —
   it looks like data.
3. Every experiment changes ONE variable when possible. Ten emails with
   ten differences teach nothing.
4. Losses get autopsies with the same care as wins. `no_reply` after a
   full sequence is a result, not an embarrassment.
