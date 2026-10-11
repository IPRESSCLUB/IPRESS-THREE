"""Render the IPRESS clay art direction as a 1200 x 630 social graphic.
This is a sharing graphic, not a screenshot or browser layout test.
Requires Pillow only when regenerating; the website itself is buildless.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

root = Path(__file__).resolve().parents[1]
public = root if (root / 'index.html').exists() else root / 'dist'
assets = public / 'assets'
canvas = Image.new('RGBA', (1200, 630), '#edf5fc')
draw = ImageDraw.Draw(canvas)
blue, ink, green = '#2063b1', '#183e66', '#426f35'
font = lambda size: ImageFont.truetype(str(assets/'bricolage-grotesque.ttf'), size)
body = lambda size: ImageFont.truetype(str(assets/'dm-sans.ttf'), size)

def centered(text, y, face, fill):
    d = ImageDraw.Draw(canvas)
    d.text((600, y), text, font=face, fill=fill, anchor='mt')

def pillow(size, color, edge, radius, rotation):
    w,h = size
    layer = Image.new('RGBA', (w+100,h+100))
    shadow = Image.new('RGBA', layer.size)
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle((42,50,w+52,h+60),radius,fill=edge)
    shadow = shadow.filter(ImageFilter.GaussianBlur(15))
    layer.alpha_composite(shadow)
    d=ImageDraw.Draw(layer)
    d.rounded_rectangle((40,40,w+40,h+46),radius,fill=edge)
    d.rounded_rectangle((40,34,w+40,h+38),radius,fill=color)
    d.arc((48,40,48+radius*2,40+radius*2),180,270,fill=(255,255,255,110),width=3)
    return layer, d

# Original logo, in a soft off-axis identity cushion.
plate,_=pillow((302,96),'#ffffff',(167,191,139,160),30,-4)
logo=Image.open(assets/'ipress-logo.png').convert('RGBA')
logo.thumbnail((246,51),Image.Resampling.LANCZOS)
plate.alpha_composite(logo,(68,58))
plate=plate.rotate(4,resample=Image.Resampling.BICUBIC,expand=True)
canvas.alpha_composite(plate,(600-plate.width//2,-14))
centered('THE CREATIVE MEDIA CLUB · IFMEREE TANGER',169,body(10),ink)

camera=Image.open(assets/'clay-camera.webp').convert('RGBA')
camera.thumbnail((270,270),Image.Resampling.LANCZOS)
camera=camera.rotate(8,resample=Image.Resampling.BICUBIC,expand=True)
canvas.alpha_composite(camera,(47,42))

# Rounded chat sculpture, matching the code-native live-page decoration.
chat=Image.new('RGBA',(246,212))
d=ImageDraw.Draw(chat)
d.rounded_rectangle((100,18,228,110),34,fill='#81ad58')
d.rounded_rectangle((97,12,225,102),34,fill='#a8cf7f')
d.ellipse((133,47,145,59),fill='#edf8e2');d.ellipse((167,47,179,59),fill='#edf8e2')
d.rounded_rectangle((18,67,192,181),40,fill='#c1d6e5')
d.rounded_rectangle((15,60,189,172),40,fill='#ffffff')
for x in (55,92,129):
 d.ellipse((x,106,x+18,125),fill='#2063b1')
chat=chat.rotate(-8,resample=Image.Resampling.BICUBIC,expand=True)
canvas.alpha_composite(chat,(903,72))

centered('Stay curious.',211,font(76),ink)
centered('Create together.',285,font(76),green)
centered('Big ideas. Good stories. Your people.',376,body(18),'#476781')

# The two destinations as tactile invitation cards.
for x,angle,color,edge,title,kicker,tc in [
 (188,3,'#2063b1',(23,77,139,180),'Explore IPRESS','THE IPRESS UNIVERSE','#ffffff'),
 (613,-3,'#d4eab5',(117,153,81,160),'Join our community','THE WHATSAPP COMMUNITY','#26472f')]:
 card,d=pillow((371,124),color,edge,31,angle)
 d.text((67,54),kicker,font=body(9),fill=tc)
 d.text((67,81),title,font=font(26),fill=tc)
 d.rounded_rectangle((354,88,396,130),15,fill='#f8fcf4')
 d.line((366,117,384,100),fill='#245184',width=3)
 d.line((370,100,384,100,384,114),fill='#245184',width=3)
 card=card.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True)
 canvas.alpha_composite(card,(x-43,399))
canvas.convert('RGB').save(assets/'social-preview.png',optimize=True)
print('Saved social-preview.png (1200 × 630)')
