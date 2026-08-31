---
name: odyssey
description: The complete, searchable text of Homer's Odyssey (Samuel Butler's public-domain prose translation), split into its 24 books, with a scene index and a character-name map. Use this skill for ANY task that touches the Odyssey or its world — quoting or verifying a passage, checking a plot fact, literary analysis or essays, retellings and adaptations, teaching materials, trivia, or allusion-hunting. Trigger on mentions of the Odyssey, Homer, Odysseus/Ulysses, Penelope, Telemachus, the Cyclops/Polyphemus, Sirens, Circe, Calypso, Ithaca, or "Greek epic", even when the user doesn't ask for the text itself — grounding answers in the actual text beats recalling it from memory.
---

# The Odyssey (Butler translation)

This skill packages the full text of the Odyssey — Samuel Butler's 1900 prose
translation, ~117,000 words, sourced from Project Gutenberg eBook #1727 (public
domain) — so that claims about the poem can be grounded in the poem, not in
memory. Memory of famous texts is exactly where confident misquotation happens:
half-remembered wording, scenes attributed to the wrong book, lines from one
translation blended with another. When the text is at hand, check it.

## What's in here

```
references/
├── index.md                — structure of the poem, per-book summaries,
│                             and a "where the famous episodes are" table
├── characters.md           — who's who, and the Butler↔Greek name map
├── operating-patterns.md   — five decision/failure shapes named after episodes
│                             (Sirens, Scylla, cattle of the Sun, the bed test,
│                             sizing an ask), each tied to its passage
├── text/book-01.md … book-24.md — the full text, one file per book
├── footnotes.md            — Butler's 187 footnotes ([n] markers in the text)
└── translator-preface.md   — Butler's two prefaces (his "Authoress of the
                              Odyssey" theory and translation choices)
```

Never load all 24 text files at once — that's the whole point of the split.
Use `index.md` to find the right book, then read or search only that file.

## The one thing that trips everyone up: names

Butler uses **Roman god-names and his own spellings**: Ulysses (not Odysseus),
Jove (not Zeus), Minerva (not Athena), Neptune (not Poseidon), Teiresias,
Euryclea. A search for "Odysseus" or "Athena" in these files returns nothing.
Before searching, check the name map in `references/characters.md`.

## How to work

**Locating a scene or checking a plot fact** — read `references/index.md`;
its episode table maps famous scenes (Cyclops, Sirens, the bow contest, the
bed test…) to their book file. Then read that file. Book files run 3,300–8,000
words each, so reading one whole book is cheap; reading ten is not.

**Quoting** — always Grep the `references/text/` files for the passage
(remember: Butler's names) and quote verbatim from the file. Each paragraph is
one long line, so grep output often truncates; use grep to get the line
number, then Read the file at that line. Cite as
"Book IX" / "Bk. IX" — book numbers are the standard scholarly reference and
are stable across translations; there are no line numbers in prose. Strip the
bracketed footnote markers like `[88]` from quotations. If a user quotes
wording that isn't in these files, say so plainly: it's likely another
translation (Fagles, Fitzgerald, Lattimore, Wilson…) — Butler is one prose
rendering among many, and this skill can only verify Butler.

**Analysis, essays, teaching** — ground every textual claim in a book file you
actually opened this session. The index's structural notes (Telemachy, the
flashback books IX–XII, the revenge arc) are the skeleton for essays on
structure. Butler's footnotes and prefaces are themselves quotable primary
material about Victorian reception — his theory that the poem was written by a
young Sicilian woman is in `translator-preface.md`.

**Retellings and adaptations** — take plot, sequence, and character detail
from the text files rather than memory; small invented details (who was where,
who said what) are the tell of an adaptation that never touched its source.
Butler's diction is public domain: reuse or rework it freely.

**Naming a decision or a failure** — the poem is also a compact catalogue of
decision shapes: precommitment, bounded loss, unsupervised drift, verifiable
proof, sizing an ask. `references/operating-patterns.md` names five, each tied
to its passage. Useful when a project postmortem or a judgment call needs a
precise name rather than a vague one. Keep these for internal reasoning — using
them as borrowed authority in outward-facing copy is its own kind of
unevidenced claim.

## Honesty about scope

This is the Butler translation only. For questions about the Greek text,
meter, or wording differences between translations, the skill can establish
what Butler says — not what Homer's Greek says. Say which when it matters.
