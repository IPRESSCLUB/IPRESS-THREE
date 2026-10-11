"""Rebuild the exact 1200 x 630 social graphic. Runtime site needs no Python."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

root = Path(__file__).resolve().parents[1]
public = root if (root / 'index.html').exists() else root / 'dist'
assets = public / 'assets'
im = Image.new('RGB', (1200, 630), '#f8fafc')
draw = ImageDraw.Draw(im)
blue, ink, green, muted = '#0b5384', '#103952', '#496e34', '#496b80'
display = lambda size: ImageFont.truetype(str(assets / 'space-grotesk.ttf'), size)
mono = lambda size: ImageFont.truetype(str(assets / 'ibm-plex-mono.ttf'), size)
draw.line((64, 90, 1136, 90), fill='#d4e2eb', width=1)
draw.text((64, 46), 'THE CREATIVE MEDIA CLUB', fill=muted, font=mono(13))
draw.text((945, 46), 'IFMEREE TANGER', fill=blue, font=mono(13))
for text, y, color in [('Create.', 122, blue), ('Capture.', 219, blue), ('Connect.', 316, green)]:
    draw.text((59, y), text, fill=color, font=display(104), stroke_width=0)
for bounds in [(704, 129, 1078, 503), (727, 152, 1055, 480), (758, 183, 1024, 449)]:
    draw.ellipse(bounds, outline='#ccdce6', width=1)
draw.arc((704, 129, 1078, 503), 288, 327, fill='#80a947', width=3)
draw.ellipse((735, 421, 745, 431), fill=blue)
draw.ellipse((1028, 190, 1036, 198), fill=green)
draw.rounded_rectangle((711, 236, 1071, 386), radius=13, fill='white', outline='#d4e2eb', width=1)
# Composite the original bitmap at its native resolution, without editing it.
logo = Image.open(assets / 'ipress-logo.png').convert('RGBA')
im.paste(logo, (743, 267), logo)
draw.text((770, 348), 'A COLLECTIVE POINT OF VIEW', fill=muted, font=mono(10))
draw.text((64, 490), 'One creative community. Two ways in.', fill=muted, font=display(22))
draw.line((64, 560, 1136, 560), fill='#d4e2eb', width=1)
draw.text((64, 585), 'EXPLORE OUR WEBSITE', fill=blue, font=mono(13))
draw.text((889, 585), 'JOIN OUR COMMUNITY', fill=green, font=mono(13))
im.save(assets / 'social-preview.png', optimize=True)
print(f'Saved {assets / "social-preview.png"} (1200 x 630)')
