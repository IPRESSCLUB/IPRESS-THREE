"""Dependency-free release checks. These do not replace browser layout testing."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
import hashlib
import re
import struct

root = Path(__file__).resolve().parents[1]
public = root if (root / 'index.html').exists() else root / 'dist'
html = (public / 'index.html').read_text()
css = (public / 'styles.css').read_text()

class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

doc = Document()
doc.feed(html)
links = [attrs for tag, attrs in doc.tags if tag == 'a']
expected = [
    'https://workingharde9-ship-it.github.io/IPRESS/',
    'https://chat.whatsapp.com/GarYt66WwYnEFJseaH64WM',
]
assert [link['href'] for link in links] == expected, 'Exactly two destination links required'
for link in links:
    assert link['target'] == '_blank'
    assert set(link['rel'].split()) >= {'noopener', 'noreferrer'}
    assert link.get('aria-labelledby') and link.get('aria-describedby')

ids = [attrs['id'] for tag, attrs in doc.tags if 'id' in attrs]
assert len(ids) == len(set(ids)), 'Duplicate IDs'
for tag, attrs in doc.tags:
    for key in ['aria-labelledby', 'aria-describedby']:
        for identifier in attrs.get(key, '').split():
            assert identifier in ids, f'Missing accessibility target: {identifier}'
    if tag == 'img':
        assert attrs.get('alt') and attrs.get('width') and attrs.get('height')
    if tag == 'svg':
        assert attrs.get('aria-hidden') == 'true'
    for key in ['src', 'href']:
        path = attrs.get(key, '')
        if path.startswith('./'):
            assert (public / path).is_file(), f'Missing asset: {path}'

for asset in re.findall(r'url\([\'"]?([^\)\'\"]+)', css):
    if asset.startswith('./'):
        assert (public / asset).is_file(), f'Missing CSS asset: {asset}'
assert css.count('{') == css.count('}'), 'Unbalanced CSS blocks'
assert '(prefers-reduced-motion:reduce)' in css
assert ':focus-visible' in css
assert '(forced-colors:active)' in css
assert not re.search(r'animation[^;{}]*\binfinite\b', css)
assert not re.search(r'@import|https?://', css), 'CSS must be self-contained'
assert html.count('<main>') == 1 and html.count('<h1>') == 1
assert not re.search(r'<(?:button|form|iframe)\b', html)

metadata = {a.get('property', a.get('name')): a.get('content') for t, a in doc.tags if t == 'meta'}
for field in ['description', 'viewport', 'og:title', 'og:description', 'og:type', 'og:url', 'og:image', 'twitter:card', 'twitter:image']:
    assert metadata.get(field), f'Missing metadata: {field}'
assert metadata['og:image'] == metadata['twitter:image']
assert metadata['og:image'] == metadata['og:url'] + 'assets/social-preview.png'
assert urlparse(metadata['og:url']).scheme == 'https'
assert (public / '.nojekyll').is_file()
png = (public / 'assets/social-preview.png').read_bytes()
assert png[:8] == b'\x89PNG\r\n\x1a\n'
assert struct.unpack('>II', png[16:24]) == (1200, 630)
logo = (public / 'assets/ipress-logo.png').read_bytes()
assert hashlib.sha256(logo).hexdigest() == '244a4daafd21f384e1bbaa777c5664ab366a311c27701edc9bb26e50dc0fcdd6', 'Original logo changed'

def luminance(hex_color):
    channels = [int(hex_color[i:i+2], 16) / 255 for i in (1, 3, 5)]
    rgb = [v/12.92 if v <= .04045 else ((v+.055)/1.055)**2.4 for v in channels]
    return sum(c*w for c, w in zip(rgb, [.2126, .7152, .0722]))

pairs = [
    ('Body copy', '#496b80', '#f8fafc'),
    ('Blue heading', '#0b5384', '#f8fafc'),
    ('Green heading', '#496e34', '#f8fafc'),
    ('Website title', '#ffffff', '#0b5384'),
    ('Website description', '#dceaf4', '#0b5384'),
    ('Community title', '#103952', '#eaf2e5'),
    ('Community description', '#466344', '#eaf2e5'),
    ('Logo caption', '#496b80', '#ffffff'),
]
for name, foreground, background in pairs:
    values = sorted([luminance(foreground), luminance(background)])
    ratio = (values[1]+.05)/(values[0]+.05)
    assert ratio >= 4.5, f'{name} contrast {ratio:.2f}:1 below AA for normal text'
    print(f'PASS {name}: {ratio:.2f}:1 contrast')

critical = ['index.html', 'styles.css', 'script.js', 'assets/ipress-logo.png', 'assets/space-grotesk.woff', 'assets/ibm-plex-mono.woff']
payload = sum((public / p).stat().st_size for p in critical)
print(f'PASS: exactly two destinations, security attributes, image/ARIA labels, local assets, metadata, original logo, reduced motion and CSS structure')
print(f'Initial page resources: {payload:,} bytes before HTTP compression; social preview and source TTFs are not page loads.')
