"""Render entry.png: a broadsheet front page for Thursday 19 November 2026.

Local build tool only (uses Pillow); the graded program is main.py, which
copies the picture this script writes. Every story below was reported on
19 November 2026 (see the day's news wires): Anthropic's record IPO, the
leaders' summit in China, Gaza, Ukraine, US House history, Voyager 1,
the record Van Gogh sale, GTA VI's launch and Cyclone Akvan.

Run:  python3 tools/build_image.py   (writes ../entry.png, 1024x1024)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 243, 233)
INK = (17, 17, 17)
ACCENT = (142, 22, 22)
GREY = (84, 80, 72)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, xy, text, fnt, width, fill=INK, leading=1.25):
    x, y = xy
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += int(fnt.size * leading)
    return y


def story(draw, xy, width, kicker, headline, body, head_size=25):
    x, y = xy
    draw.text((x, y), kicker, font=font(SANS_B, 13), fill=ACCENT)
    y += 19
    y = text_block(draw, (x, y), headline, font(SERIF_B, head_size), width, leading=1.12)
    y += 3
    y = text_block(draw, (x, y), body, font(SERIF, 14), width, leading=1.26)
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    margin = 44
    right = W - margin

    # Masthead
    d.line([(margin, 30), (right, 30)], fill=INK, width=2)
    title = "The World Today"
    tf = font(SERIF_B, 66)
    d.text(((W - d.textlength(title, font=tf)) / 2, 40), title, font=tf, fill=INK)
    dateline = "THURSDAY, 19 NOVEMBER 2026  ·  THE DAY'S WORLD NEWS IN ONE PAGE"
    df = font(SANS_B, 16)
    d.text(((W - d.textlength(dateline, font=df)) / 2, 122), dateline, font=df, fill=ACCENT)
    d.line([(margin, 152), (right, 152)], fill=INK, width=4)
    d.line([(margin, 160), (right, 160)], fill=INK, width=1)

    # Lead story: Anthropic's record IPO
    y = 176
    d.text((margin, y), "BUSINESS  ·  ARTIFICIAL INTELLIGENCE", font=font(SANS_B, 14), fill=ACCENT)
    y += 24
    y = text_block(d, (margin, y), "Anthropic's Record IPO Crowns the AI Boom",
                   font(SERIF_B, 43), right - margin, leading=1.08)
    y += 6
    y = text_block(d, (margin, y),
                   "The maker of Claude raises $81.3 billion in the biggest share sale of all time, "
                   "priced at $83 a share — a market debut that caps a year in which artificial "
                   "intelligence redrew the world's exchanges, even as US senators warn that "
                   "AI-enabled cyber threats are outpacing the defences meant to stop them.",
                   font(SERIF, 17), right - margin, leading=1.3)
    y += 10
    d.line([(margin, y), (right, y)], fill=INK, width=1)
    y += 10

    # Second lead: the summit in China
    y = text_block(d, (margin, y), "Trump, Xi and Putin Shake Hands as Leaders Gather in China",
                   font(SERIF_B, 27), right - margin, leading=1.12)
    y += 4
    y = text_block(d, (margin, y),
                   "The three presidents meet face to face as a US panel urges Congress to punish "
                   "Beijing over its detention of Panama-flagged ships, and Canada's prime minister "
                   "says Ottawa is recalibrating its ties with China while it seeks the right deal "
                   "with Washington.",
                   font(SERIF, 15), right - margin, leading=1.28)
    y += 12
    d.line([(margin, y), (right, y)], fill=INK, width=2)
    y += 14

    # Two columns of the day's other news
    col_w = (right - margin - 28) // 2
    lx, rx = margin, margin + col_w + 28
    ly = story(d, (lx, y), col_w, "MIDDLE EAST",
               "Israeli Tanks Cross Gaza Cease-Fire Line",
               "Israel launches a rare ground operation beyond the Yellow Line as Australia, "
               "Canada, Italy and Britain jointly demand unrestricted aid access for "
               "Palestinians hit by flooding. President Herzog asks former army chief Gadi "
               "Eisenkot to try to form Israel's next government, bypassing Netanyahu.",
               head_size=22)
    ly += 12
    ly = story(d, (lx, ly), col_w, "UKRAINE WAR",
               "Crimean Bridge Attacked Again",
               "Traffic is suspended across the bridge linking Crimea to Russia after a new "
               "attack, and Moscow and Kyiv trade drone strikes amid peace talks in Abu Dhabi. "
               "The EU proposes a €45 billion loan for Ukraine, to be repaid once Russia pays "
               "reparations.", head_size=22)
    ly += 12
    ly = story(d, (lx, ly), col_w, "WEATHER",
               "Cyclone Akvan Bears Down on India's East Coast",
               "The storm is expected to make landfall between Machilipatnam and Puri, with "
               "Andhra Pradesh and Odisha bracing for heavy rain and flooding.", head_size=22)

    ry = story(d, (rx, y), col_w, "UNITED STATES",
               "Jeffries Set to Be First Black House Speaker",
               "Democrats nominate Hakeem Jeffries to lead the House of Representatives — a "
               "first in American history, reported by outlets across the country as the "
               "day's top US story.", head_size=22)
    ry += 12
    ry = story(d, (rx, ry), col_w, "SCIENCE",
               "Voyager 1 Reaches One Light-Day From Home",
               "Nearly 50 years after launch, NASA's farthest probe is believed to have crossed "
               "a distance light itself needs a full day to travel.", head_size=22)
    ry += 12
    ry = story(d, (rx, ry), col_w, "ART & CULTURE",
               "Van Gogh Sells for a Record $190.4 Million",
               "The painting sets a new auction record after a public row over its Nazi-era "
               "history — while gamers worldwide finally enter Vice City as Grand Theft Auto "
               "VI begins its global rollout, 13 years after the last instalment.", head_size=22)

    # Footer strip (must stay inside the page: it starts wherever the taller
    # column ended, and the text is sized so its three lines end above y=1010)
    fy = max(ly, ry) + 12
    d.line([(margin, fy), (right, fy)], fill=INK, width=2)
    fy += 9
    text_block(d, (margin, fy),
               "ALSO TODAY:  Estonia to close its border crossings with Russia from December  ·  "
               "Hundreds of thousands march in Prague for media independence  ·  France's fourth "
               "weekend of cost-of-living protests  ·  Spain's general strike halts ports and "
               "factories  ·  India and Japan review defence ties  ·  North Korea fires ballistic "
               "missiles after US–South Korea–Japan drills  ·  Oil falls as supplies improve",
               font(SANS, 12), right - margin, fill=GREY, leading=1.3)

    out = Path(__file__).resolve().parent.parent / "entry.png"
    img.save(out, optimize=True)
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
