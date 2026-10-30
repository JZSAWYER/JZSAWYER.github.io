"""Embed homepage assets in one review HTML file with Busuanzi totals.

Usage: python docs/preview/package_preview.py BUILD_DIRECTORY OUTPUT_HTML
Requires BeautifulSoup and requests. Local previews do not request counts for a
different domain or invent statistics; live Busuanzi counts use the website host.
"""
import base64
import mimetypes
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit, urljoin

from bs4 import BeautifulSoup
import requests

build = Path(sys.argv[1]).resolve()
output = Path(sys.argv[2]).resolve()
public_site = 'https://jzsawyer.github.io/'
cache = {}

def local_path(url, directory=build):
    parsed = urlsplit(url)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    path = (directory / unquote(parsed.path).lstrip('/')).resolve()
    if not path.is_relative_to(build):
        return None
    return path

def data_uri(path):
    if path not in cache:
        mime = mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
        cache[path] = f'data:{mime};base64,' + base64.b64encode(path.read_bytes()).decode('ascii')
    return cache[path]

def inline_css(path):
    def replace(match):
        url = match.group(1).strip(' \t\'\"')
        asset = local_path(url, path.parent)
        if asset and asset.is_file():
            return 'url("' + data_uri(asset) + '")'
        return match.group(0)
    return re.sub(r'url\(([^)]+)\)', replace, path.read_text())

soup = BeautifulSoup((build / 'index.html').read_text(), 'html.parser')
for link in list(soup.select('link[rel~="stylesheet"]')):
    path = local_path(link.get('href', ''))
    if not path or not path.is_file():
        raise ValueError(f'Missing stylesheet: {link.get("href")}')
    style = soup.new_tag('style')
    style.string = inline_css(path)
    link.replace_with(style)

for script in list(soup.find_all('script')):
    src = script.get('src')
    if src:
        if script.get('id') == 'busuanzi-script' and src == 'https://busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js':
            # The downloaded HTML has no website referrer. Only request live
            # statistics when this file is served on the actual homepage host.
            del script['src']
            script.string = """(function () {
  if (location.protocol === 'https:' && location.hostname === 'jzsawyer.github.io') {
    var widget = document.createElement('script');
    widget.async = true;
    widget.src = 'https://busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js';
    document.head.appendChild(widget);
    document.querySelector('.visitor-stats__note').hidden = true;
  }
}());"""
            continue
        path = local_path(src)
        if path and path.is_file():
            del script['src']
            script.string = path.read_text().replace('</script', '<\\/script')
        else:
            # Omit unrelated remote scripts and analytics.
            script.decompose()
    elif script.get('type') == 'text/x-mathjax-config' or any(marker in script.get_text() for marker in ('google_scholar', 'google-scholar-stats', 'gsDataBaseUrl')):
        script.decompose()

for image in list(soup.find_all('img')):
    src = image.get('src', '')
    path = local_path(src)
    if path and path.is_file():
        image['src'] = data_uri(path)
    elif src.startswith(('http:', 'https:', '//')):
        if 'img.shields.io/' in src:
            response = requests.get(src, timeout=20)
            response.raise_for_status()
            mime = response.headers.get('Content-Type', 'image/svg+xml').split(';')[0]
            image['src'] = f'data:{mime};base64,' + base64.b64encode(response.content).decode('ascii')
            image['alt'] = image.get('alt') or 'GitHub stars'
        else:
            raise ValueError(f'Unpackaged external image: {src}')
    else:
        raise ValueError(f'Missing image: {src}')

for link in list(soup.find_all('link')):
    href = link.get('href', '')
    if 'manifest' in link.get('rel', []):
        link.decompose()
        continue
    path = local_path(href)
    if path and path.is_file():
        link['href'] = data_uri(path)

for anchor in soup.select('a[href]'):
    href = anchor['href']
    if href.startswith('/#'):
        href = href[1:]
    if href.startswith('#'):
        anchor['href'] = href
        anchor['target'] = '_self'
    elif not urlsplit(href).scheme and not href.startswith('//'):
        anchor['href'] = urljoin(public_site, href)

# Mark unavailable local totals explicitly instead of displaying sample numbers.
stats = soup.select_one('.visitor-stats')
if stats:
    note = soup.new_tag('p', attrs={'class': 'visitor-stats__note'})
    note.string = 'Preview — live totals appear on the published site.'
    stats.insert(2, note)

# The site uses MathJax only for ordinal numbers in the awards list.
for text in list(soup.find_all(string=re.compile(r'\$\d+\^\{th\}\$'))):
    if text.parent.name not in ('script', 'style'):
        text.replace_with(re.sub(r'\$(\d+)\^\{th\}\$', r'\1th', str(text)))

meta = soup.new_tag('meta', attrs={'name': 'robots', 'content': 'noindex, nofollow'})
soup.head.append(meta)
soup.title.string = 'Haitian Zhong — Homepage Preview'
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text('\n'.join(line.rstrip() for line in str(soup).splitlines()) + '\n', encoding='utf-8')
print(f'Packaged {len(cache)} local assets; HTML size {output.stat().st_size:,} bytes.')
