#!/usr/bin/env python3
"""Build the SixSense Target Account Map PDF (the asset behind the outreach email)."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether)

INK    = HexColor("#1a2332")
ACCENT = HexColor("#0f4c81")
MUTE   = HexColor("#5a6472")
FAINT  = HexColor("#8a93a0")
RULE   = HexColor("#d8dde4")
BAND   = HexColor("#eef2f6")

W, H = A4
M = 16*mm

def S(name, **kw):
    base = dict(fontName="Helvetica", fontSize=9.5, leading=13, textColor=INK, alignment=TA_LEFT)
    base.update(kw)
    return ParagraphStyle(name, **base)

st_title   = S("title",  fontName="Helvetica-Bold", fontSize=19, leading=23)
st_sub     = S("sub",    fontSize=9, leading=12.5, textColor=MUTE)
st_tier    = S("tier",   fontName="Helvetica-Bold", fontSize=12.5, leading=15, textColor=ACCENT, spaceBefore=7, spaceAfter=2)
st_tiersub = S("tiersub", fontSize=9, leading=12, textColor=MUTE, spaceAfter=6)
st_acct    = S("acct",   fontName="Helvetica-Bold", fontSize=10.5, leading=13.5, spaceBefore=5)
st_meta    = S("meta",   fontSize=9, leading=12, textColor=MUTE)
st_why     = S("why",    fontSize=9.5, leading=12.8, spaceBefore=2)
st_cell    = S("cell",   fontSize=8.6, leading=10.8)
st_cellm   = S("cellm",  fontSize=8.6, leading=10.8, textColor=MUTE)
st_note    = S("note",   fontSize=8.6, leading=11.5, textColor=MUTE)

def link(name, slug):
    if not slug:
        return name
    return f'<a href="https://www.linkedin.com/in/{slug}" color="#0f4c81"><u>{name}</u></a>'

def people_table(rows):
    data = [[Paragraph(link(n, slug), st_cell), Paragraph(r, st_cell), Paragraph(note, st_cellm)]
            for (n, slug, r, note) in rows]
    t = Table(data, colWidths=[38*mm, 52*mm, 88*mm])
    t.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("TOPPADDING", (0,0), (-1,-1), 2), ("BOTTOMPADDING", (0,0), (-1,-1), 2),
        ("LEFTPADDING", (0,0), (-1,-1), 0), ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("LINEBELOW", (0,0), (-1,-2), 0.4, RULE),
    ]))
    return t

def account(name, meta, why, rows=None):
    parts = [Paragraph(name, st_acct), Paragraph(meta, st_meta), Paragraph(why, st_why)]
    if rows:
        parts += [Spacer(1, 3), people_table(rows)]
    return KeepTogether(parts + [Spacer(1, 4)])

story = []
story.append(Paragraph("Target Account Map", st_title))
story.append(Spacer(1, 2))
story.append(Paragraph(
    "Prepared for SixSense &middot; ~30 accounts, tiered by the paths between them &middot; "
    "built from public signals (production starts, expansions, ownership structures, hiring) &middot; 30 Aug 2026",
    st_sub))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "How to read this: the names are the easy part &mdash; the tiers follow the doors each account opens. "
    "Tier 1 carries named people because India's plants are new enough that their yield and quality teams "
    "exist in nobody's CRM yet. Every person below was individually verified on LinkedIn, 29&ndash;30 Aug 2026.",
    st_note))

story.append(Paragraph("Tier 1 &mdash; India, live now", st_tier))
story.append(Paragraph("Four plants entered production in 2026. Inspection workflows are being written this quarter &mdash; whoever gets in first becomes the habit.", st_tiersub))

story.append(account(
    "Tata Electronics / TSAT",
    "Vemagal (Karnataka) shipping now &middot; Jagiroad (Assam) ramping toward 48M chips/day by end-2026 &middot; Dholera 300mm fab (PSMC technology) targets first wafers late 2026",
    "Why now: the Vemagal line is transferring into Jagiroad this quarter &mdash; hundreds of tools moving by September. Standards set now hold for a decade. Their own leadership describes the OSAT as AI-enabled.",
    [("Tim McIntosh", "tim-mcintosh-8212703", "VP, Head of Operations &amp; Mfg Excellence, TSAT", "Runs both Vemagal and Jagiroad; the operations owner"),
     ("Ashish Mishra", "ashish-mishra-70851824", "Head, HVM Manufacturing (OSAT)", "Building Jagiroad; calls it &ldquo;AI enabled&rdquo; in his own bio &mdash; the door is pre-opened"),
     ("Kirubalan Natarajan", "kirubalan-natarajan-60a22238", "GM, Quality Assurance", "Ex-UTAC quality leadership &mdash; knows OSAT quality regimes from Singapore"),
     ("Jagadish Sunderraj", "jagadish-sunderraj-620b76a9", "Sr Manager &mdash; NPI, Test &amp; Quality", "Owns yield/RR triggers and CLCA loops day to day")]))

story.append(account(
    "CG Semi  (CG Power + Renesas + Stars Microelectronics JV)",
    "Commercial at G1 since 4 Jul 2026 &middot; G2 under construction, toward 15M chips/day &middot; first shipments went to Kuala Lumpur",
    "Why now &mdash; and the path: the floor is staffed with Malaysia OSAT veterans, the exact buyer profile SixSense already sells to. And this account is the Renesas door: win Sanand and there is a reason to be in front of Renesas in Japan.",
    [("Mark Gerald Pinlac", "mark-gerald-pinlac-032a3730b", "G1 Plant Operations Head", "Publicly credited by Renesas leadership for the production launch"),
     ("LW Yong", "lw-yong-0850205", "VP Operations (joined Jun 2026)", "40 years in semis; ex-Amkor; has started multiple greenfield sites"),
     ("Gene de Roca", "gene-de-roca-76990551", "QA Test Manager", "16 years of OSAT quality management in Singapore"),
     ("Ricardo Martos", "ricardo-martos-0aa043a2", "Lead Test Equipment Engineer", "14 years at Renesas KL before joining &mdash; the Renesas path in human form")]))

story.append(account(
    "Kaynes Semicon",
    "Producing since 31 Mar 2026 &middot; ramping 1.5M toward 6.3M units/day &middot; headcount up ~870% year on year",
    "Why now: hiring at that rate means inspection is scaling headcount-first &mdash; the exact cost AI-ADC removes. Their own leadership is publishing on quality systems and the smart-factory &ldquo;digital backbone.&rdquo;",
    [("Paul Ilanghovan T.", "paul-ilanghovan-t-80505135", "Head of Operations, Sanand", "30+ years in semiconductor packaging; set up plants from zero before"),
     ("Phaneendra T.S.", "phaneendra-t-s-6517816", "Sr VP, Test Engineering", "Test-side owner as volume ramps"),
     ("Anantha Murthy VR", "vrananthamurthy", "Head &mdash; QMS &amp; System Design", "Fronts their &ldquo;quality as the foundation&rdquo; positioning"),
     ("Gopal Rathore", "", "VP &mdash; IT", "Fronts the digital-backbone / smart-factory push &mdash; the systems budget")]))

story.append(account(
    "Micron &mdash; Sanand ATMP",
    "Commercial since 28 Feb 2026 &middot; tens of millions of units in 2026, hundreds of millions planned for 2027",
    "Why now &mdash; and the path: Sanand is being staffed by transfers from Micron Muar and Singapore, so site decisions mirror the mature-site playbook &mdash; and Micron's new Singapore HBM advanced-packaging fab starts up in 2026. Enter at the greenfield edge of a global account.",
    [("Malini Chokkanathan", "malini-c-016b5a20", "Site Quality Director", "Site-level quality owner since the 2024 build-out"),
     ("Jitender Pratap Singh", "jitender-pratap-singh-jp-9567a8382", "Director, Operations Management", "30 years of ATMP/OSAT plant management"),
     ("Manish Chopra", "manishchoprasemiconductors", "Quality Engineering Manager", "Leading quality engineering for the greenfield project since 2023"),
     ("Mdhakim Abdullah", "mdhakim-abdullah-08327310", "A&amp;T Equipment Engineering Manager", "Moved from Micron Muar in Jul 2026 &mdash; the Malaysia playbook arriving in person")]))

story.append(Paragraph(
    "Seed now, harvest at tool-in: HCL&ndash;Foxconn (Jewar &mdash; display-driver ATMP, under construction) &middot; "
    "SiCSem (Odisha &mdash; SiC fab + ATMP, early build) &middot; Tata Dholera (300mm, first wafers late 2026).",
    st_note))

story.append(Paragraph("Tier 2 &mdash; Paths from wins SixSense already holds", st_tier))
story.append(Paragraph("Five moves where an existing proof point shortens the sales cycle.", st_tiersub))
t2 = [
    ("UMC (Taiwan)", "Wavetek is UMC's subsidiary &mdash; the proof deployed there walks straight up into the parent's specialty fabs."),
    ("Renesas (Japan / Malaysia)", "Via the CG Semi JV. CG Semi already ships to KL, and its equipment staff are Renesas KL alumni."),
    ("PSMC (Taiwan)", "Technology partner to Tata Dholera &mdash; one relationship spans Taiwan and India's first 300mm fab."),
    ("Tong Hsing (Taiwan)", "Live on defect classification &mdash; the expansion is lot disposition and predictive inspection across lines."),
    ("Micron network", "Sanand plus the new Singapore HBM fab: two greenfield edges into one global account."),
]
t2t = Table([[Paragraph(f"<b>{a}</b>", st_cell), Paragraph(b, st_cell)] for a, b in t2],
            colWidths=[46*mm, 132*mm])
t2t.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("TOPPADDING", (0,0), (-1,-1), 2.4), ("BOTTOMPADDING", (0,0), (-1,-1), 2.4),
    ("LEFTPADDING", (0,0), (-1,-1), 0), ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("LINEBELOW", (0,0), (-1,-2), 0.4, RULE),
]))
story.append(t2t)

story.append(Paragraph("Tier 3 &mdash; Expansion lookalikes, each with a live trigger", st_tier))
story.append(Paragraph("Companies that look like the customers SixSense already serves, caught mid-expansion.", st_tiersub))
t3 = [
    ("ASE", "TW / MY / global", "Six plants breaking ground in 2026 &mdash; its biggest construction year; ~3,000 technical hires planned"),
    ("Amkor", "VN / MY / US", "$2.5&ndash;3B capex in 2026; Bac Ninh is its largest advanced-packaging site"),
    ("X-FAB", "Sarawak, MY", "$600M cleanroom opened Sep 2025; 30k to 40k wafers/month; automotive zero-escape regime"),
    ("VIS / VSMC", "Singapore", "Greenfield 300mm JV with NXP &mdash; no legacy systems, on SixSense's home turf"),
    ("Powertech (PTI)", "TW / MY", "Memory and HBM packaging; Malaysia site planned"),
    ("ChipMOS", "Taiwan", "Display-driver and memory packaging; AOI-heavy lines"),
    ("Hana Micron", "Vietnam", "Bac Ninh and Bac Giang expansions running"),
    ("Inari Amertron", "Penang, MY", "RF and optoelectronics (Broadcom chain) &mdash; RF is proven SixSense ground"),
    ("Texas Instruments", "Melaka, MY", "Second assembly/test factory opened Nov 2025 &mdash; 900k sq ft"),
    ("Infineon &mdash; Kulim", "Malaysia", "Largest 200mm SiC power fab ramping; expansion within an existing relationship"),
    ("STMicroelectronics", "SG / MY", "Singapore fab plus Muar backend; automotive-heavy"),
    ("onsemi", "PH / VN / CZ", "SiC push plus a broad backend network"),
    ("Intel Products Vietnam", "Ho Chi Minh City", "Intel's largest assembly-and-test site globally"),
    ("Coherent", "Dong Nai, VN", "New SiC / optoelectronics plant opened Jul 2025"),
    ("WIN Semiconductors", "Taiwan", "World's largest GaAs foundry &mdash; compound ground, like Wavetek and DenseLight"),
    ("CHIPX", "Malaysia", "New 8-inch GaN/SiC fab planned"),
    ("UTAC / Carsem / Unisem", "SG / MY", "Mid-tier OSATs riding friend-shoring volume"),
    ("Tower Semiconductor", "Israel", "Specialty foundry in a market SixSense already operates in"),
    ("SkyWater / Polar", "US", "Specialty fabs matching the stated US expansion push"),
]
rows = [[Paragraph(f"<b>{a}</b>", st_cell), Paragraph(b, st_cellm), Paragraph(c, st_cell)] for a, b, c in t3]
t3t = Table(rows, colWidths=[36*mm, 30*mm, 112*mm], repeatRows=0)
t3t.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("TOPPADDING", (0,0), (-1,-1), 2), ("BOTTOMPADDING", (0,0), (-1,-1), 2),
    ("LEFTPADDING", (0,0), (-1,-1), 0), ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("LINEBELOW", (0,0), (-1,-2), 0.4, RULE),
    ("ROWBACKGROUNDS", (0,0), (-1,-1), [None, BAND]),
]))
story.append(t3t)

story.append(Spacer(1, 6))
story.append(Paragraph(
    "Method &mdash; signals tracked: production starts, capacity expansion, JV and ownership structures, leadership hires, "
    "operator hiring surges, smart-factory announcements. All public sources; account facts checked 29&ndash;30 Aug 2026; "
    "people verified individually on LinkedIn. Corrections welcome &mdash; you will know faster than I would which of these "
    "are already yours, and that conversation is half the point of sharing it.",
    st_note))

def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(RULE); canvas.setLineWidth(0.5)
    canvas.line(M, 12*mm, W-M, 12*mm)
    canvas.setFont("Helvetica", 7.5); canvas.setFillColor(FAINT)
    canvas.drawString(M, 8.5*mm, "Prepared for SixSense - built from public signals")
    canvas.drawRightString(W-M, 8.5*mm, f"Arun  -  +91 89207 12899  -  page {doc.page}")
    canvas.restoreState()

doc = BaseDocTemplate("/home/user/arunroutes/outreach/assets/sixsense-target-account-map.pdf",
                      pagesize=A4, leftMargin=M, rightMargin=M, topMargin=14*mm, bottomMargin=18*mm,
                      title="Target Account Map - prepared for SixSense", author="Arun")
frame = Frame(M, 18*mm, W-2*M, H-14*mm-18*mm, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
doc.addPageTemplates([PageTemplate(id="page", frames=[frame], onPage=footer)])
doc.build(story)
print("built")
