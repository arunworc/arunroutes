#!/usr/bin/env python3
"""Win/loss report over tracking/companies.csv + tracking/campaigns.csv.

Usage: python3 tracking/scripts/report.py   (from repo root or anywhere)
Stdlib only. Prints funnel, lane comparison, and per-variable reply rates.
"""
import csv, os, sys
from collections import Counter, defaultdict
from datetime import date, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
TRACK = os.path.dirname(HERE)

STAGES = ["researched", "staged", "sent", "replied", "conversation", "deal", "dead"]
REPLIED_STAGES = {"replied", "conversation", "deal"}
SENT_STAGES = REPLIED_STAGES | {"sent", "dead"}  # dead implies it was worked/sent or bounced

def load(name):
    path = os.path.join(TRACK, name)
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return [row for row in csv.DictReader(f) if any(v.strip() for v in row.values())]

def pct(n, d):
    return f"{100*n/d:.1f}%" if d else "-"

def days_since(s):
    try:
        return (date.today() - datetime.strptime(s, "%Y-%m-%d").date()).days
    except Exception:
        return None

def main():
    rows = load("companies.csv")
    camps = load("campaigns.csv")

    print("=" * 62)
    print("MANUAL LANE — funnel")
    print("=" * 62)
    by_stage = Counter(r["stage"] for r in rows)
    for s in STAGES:
        if by_stage.get(s):
            print(f"  {s:<13} {by_stage[s]}")
    sent = [r for r in rows if r["stage"] in SENT_STAGES]
    replied = [r for r in rows if r["stage"] in REPLIED_STAGES]
    dead = [r for r in rows if r["stage"] == "dead"]
    print(f"\n  worked: {len(rows)}   sent: {len(sent)}   replied: {len(replied)}"
          f"   reply rate: {pct(len(replied), len(sent))}")
    if dead:
        print("  loss reasons: " +
              ", ".join(f"{k}={v}" for k, v in Counter(r["outcome_reason"] or "unset" for r in dead).items()))

    def breakdown(field, label):
        groups = defaultdict(lambda: [0, 0])  # field_value -> [sent, replied]
        for r in rows:
            if r["stage"] in SENT_STAGES and r.get(field, "").strip():
                groups[r[field]][0] += 1
                if r["stage"] in REPLIED_STAGES:
                    groups[r[field]][1] += 1
        if not groups:
            return
        print(f"\n  reply rate by {label}:")
        for k, (s_, r_) in sorted(groups.items(), key=lambda kv: -(kv[1][1]/kv[1][0] if kv[1][0] else 0)):
            print(f"    {k:<22} {r_}/{s_}  ({pct(r_, s_)})")

    for f, lbl in [("angle", "angle"), ("channel", "channel"),
                   ("dm_seniority", "seniority"), ("email_status", "email status"),
                   ("asset", "asset"), ("personalization", "personalization depth"),
                   ("send_dow", "send day"), ("segment", "segment")]:
        breakdown(f, lbl)

    stale = [r for r in rows
             if r["stage"] in {"staged", "sent"}
             and (days_since(r.get("send_date") or r.get("started") or "") or 0) >= 4]
    if stale:
        print("\n  NEEDS ACTION (>=4 days without a state change):")
        for r in stale:
            print(f"    {r['id']} {r['company']:<20} stage={r['stage']}  since={r.get('send_date') or r['started']}")

    if camps:
        print("\n" + "=" * 62)
        print("MASS LANE — campaigns")
        print("=" * 62)
        tot_s = tot_r = tot_p = 0
        for c in camps:
            s_ = int(c["sends"] or 0); r_ = int(c["replies"] or 0); p_ = int(c["positive"] or 0)
            tot_s += s_; tot_r += r_; tot_p += p_
            print(f"  {c['campaign_id']:<26} sends={s_:<6} replies={r_:<4} ({pct(r_, s_)})"
                  f"  positive={p_} ({pct(p_, s_)})")
        print(f"\n  mass totals: sends={tot_s}  replies={tot_r} ({pct(tot_r, tot_s)})"
              f"  positive={tot_p} ({pct(tot_p, tot_s)})")
        m_sent, m_rep = len(sent), len(replied)
        if m_sent and tot_s:
            print(f"\n  LANE COMPARISON: manual reply {pct(m_rep, m_sent)} vs mass reply {pct(tot_r, tot_s)}")

    print()

if __name__ == "__main__":
    sys.exit(main())
