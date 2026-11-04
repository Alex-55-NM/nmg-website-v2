"""Italian version of the site, generated from the English pages.

Every translatable string of the English pages (text runs, image alt text, aria labels,
titles, meta descriptions) is looked up in build/i18n/it.tsv:  <English>\t<Italian>.
Inline tags inside a text run are written as placeholders <x0>...</x0> / <x1/>.
Run `python3 build/build.py --extract` to list strings that still need a translation.
"""
import os, re, html, posixpath
from segment import segments, encode, decode, norm, tokens, ATTR_RE, META_RE, LETTER

HERE = os.path.dirname(os.path.abspath(__file__))
TSV = os.path.join(HERE, "i18n", "it.tsv")
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)

def load():
    table = {}
    if os.path.exists(TSV):
        for line in open(TSV, encoding="utf-8"):
            line = line.rstrip("\n")
            if line and not line.startswith("#") and "\t" in line:
                en, it = line.split("\t", 1)
                table[en] = it
    return table

def strings(page):
    """All translatable English strings of one page, in order."""
    out = []
    toks, segs = segments(page)
    for i, j, run in segs:
        out.append(norm(encode(run)[1]))
    for kind, v in tokens(page):
        if kind != "tag" or v.lower().startswith(("<script", "<style", "<!--")):
            continue
        for m in ATTR_RE.finditer(v):
            val = norm(html.unescape(m.group(3)))
            if LETTER.search(val): out.append(val)
        if META_RE.match(v):
            m = re.search(r'content="([^"]*)"', v)
            if m: out.append(norm(html.unescape(m.group(1))))
    return out

AUTO = [(re.compile(r"^Pexels photo (\d+)$"), r"Foto Pexels \1")]

def _lookup(table, s, missing):
    for rx, rep in AUTO:
        if rx.match(s):
            return rx.sub(rep, s)
    t = table.get(s)
    if t is None:
        missing.add(s)
        return None
    return t

def translate(path, page, table, missing):
    """Return the Italian page for site/it/<path>."""
    toks, segs = segments(page)
    vals = [v for _, v in toks]
    for i, j, run in reversed(segs):
        lead, core, trail, tagmap = encode(run)
        t = _lookup(table, norm(core), missing)
        if t is not None:
            vals[i:j] = [lead + decode(t, tagmap) + trail]
    page = "".join(vals)
    out = []
    for kind, v in tokens(page):
        if kind == "tag" and not v.lower().startswith(("<script", "<style", "<!--")):
            def attr(m):
                val = norm(html.unescape(m.group(3)))
                if not LETTER.search(val): return m.group(0)
                t = _lookup(table, val, missing)
                return m.group(0) if t is None else f'{m.group(1)}{m.group(2)}="{html.escape(t, quote=True)}"'
            v = ATTR_RE.sub(attr, v)
            if META_RE.match(v):
                def meta(m):
                    t = _lookup(table, norm(html.unescape(m.group(1))), missing)
                    return m.group(0) if t is None else f'content="{html.escape(t, quote=True)}"'
                v = re.sub(r'content="([^"]*)"', meta, v, count=1)
        out.append(v)
    page = "".join(out)
    depth = path.count("/")
    base = posixpath.dirname(path)
    # links into assets/ need one more level, page links stay inside it/
    def fix(m):
        ref = m.group(2)
        if ref.startswith(("http:", "https:", "mailto:", "data:", "#")): return m.group(0)
        target = posixpath.normpath(posixpath.join(base, ref.split("?")[0].split("#")[0]))
        return f'{m.group(1)}"../{ref}"' if target.startswith("assets/") else m.group(0)
    page = re.sub(r'((?:href|src)=)"([^"]+)"', fix, page)
    page = re.sub(r'srcset="([^"]+)"', lambda m: 'srcset="' + ", ".join("../" + p.strip() for p in m.group(1).split(",")) + '"', page)
    up = "../" * (depth + 1)
    page = page.replace('<html lang="en">', '<html lang="it">', 1)
    page = re.sub(r'<link rel="alternate" hreflang="en" href="[^"]*">\n<link rel="alternate" hreflang="it" href="[^"]*">\n<link rel="alternate" hreflang="x-default" href="[^"]*">',
                  f'<link rel="alternate" hreflang="en" href="{up}{path}">\n<link rel="alternate" hreflang="it" href="{posixpath.basename(path)}">\n<link rel="alternate" hreflang="x-default" href="{up}{path}">', page, count=1)
    page = re.sub(r'<a class="lang-switch" href="[^"]*" hreflang="it" lang="it" aria-label="Italiano">IT</a>',
                  f'<a class="lang-switch" href="{up}{path}" hreflang="en" lang="en" aria-label="English">EN</a>', page)
    page = re.sub(r'<a class="lang-switch" href="[^"]*" hreflang="it" lang="it">Italiano</a>',
                  f'<a class="lang-switch" href="{up}{path}" hreflang="en" lang="en">English</a>', page)
    return page
