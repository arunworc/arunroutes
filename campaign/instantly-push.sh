#!/usr/bin/env bash
# Run this ON YOUR MACHINE (not the build container - its network cannot reach api.instantly.ai).
# Prereq: export INSTANTLY_API_KEY="...your key..."   (rotate the one pasted in chat first)
set -euo pipefail
: "${INSTANTLY_API_KEY:?set INSTANTLY_API_KEY first}"
BASE="https://api.instantly.ai/api/v2"
AUTH="Authorization: Bearer $INSTANTLY_API_KEY"

# 1) create the campaign with the 3-step sequence + schedule (Mon-Thu, 09:00-17:00, 15-25min gaps)
CID=$(curl -sS -X POST "$BASE/campaigns" -H "$AUTH" -H 'Content-Type: application/json' -d '{
  "name": "Arun Routes - recruiter ask - 2026-09",
  "campaign_schedule": {
    "schedules": [{
      "name": "biz-hours",
      "timing": { "from": "09:00", "to": "17:00" },
      "days": { "1": true, "2": true, "3": true, "4": true },
      "timezone": "America/New_York"
    }]
  },
  "daily_limit": 40,
  "email_gap": 20,
  "sequences": [{ "steps": [
    { "type":"email","delay":0,"variants":[{"subject":"{{roleTitleLc}} — do you have someone?","body":"{{firstName}},\n\nLooking for a {{roleTitle}}. {{roleMode}}.\n{{roleSpec}}.\n\nDo you have someone?\n\nArun\n\nArun Routes · [ADDRESS] · reply STOP and I'\''ll leave you alone."}]},
    { "type":"email","delay":3,"variants":[{"subject":"","body":"{{firstName}} — a no is just as useful to me as a yes.\n\nArun\n\nArun Routes · [ADDRESS] · reply STOP and I'\''ll leave you alone."}]},
    { "type":"email","delay":5,"variants":[{"subject":"","body":"Taking that as a no, {{firstName}}. Won'\''t chase.\n\nIf someone lands on your bench later, reply here whenever.\n\nArun\n\nArun Routes · [ADDRESS] · reply STOP and I'\''ll leave you alone."}]}
  ]}]
}' | python3 -c "import sys,json;print(json.load(sys.stdin)['id'])")
echo "campaign: $CID"

# 2) add each lead from the CSV with its merge variables
tail -n +2 campaign/instantly-READY.csv | while IFS=, read -r email firstName companyName roleTitleLc roleTitle roleMode roleSpec; do
  curl -sS -X POST "$BASE/leads" -H "$AUTH" -H 'Content-Type: application/json' -d "$(python3 - "$email" "$firstName" "$companyName" "$roleTitleLc" "$roleTitle" "$roleMode" "$roleSpec" "$CID" <<'PY'
import sys,json
e,fn,co,rl,rt,rm,rs,cid=sys.argv[1:9]
print(json.dumps({"campaign":cid,"email":e,"first_name":fn,"company_name":co,
  "custom_variables":{"roleTitleLc":rl,"roleTitle":rt,"roleMode":rm,"roleSpec":rs}}))
PY
)" >/dev/null && echo "  + $email"
done

# 3) activate
curl -sS -X POST "$BASE/campaigns/$CID/activate" -H "$AUTH" >/dev/null && echo "ACTIVATED $CID"
echo "Done. Open Instantly to confirm before it sends on schedule."
