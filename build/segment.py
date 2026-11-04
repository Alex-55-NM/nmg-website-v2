"""Shared helpers: split an HTML page into translatable segments and rebuild it.

A *segment* is a run of text and inline tags between block boundaries. Inline
tags become placeholders (<x0>…</x0>, <x1/>) so a translation can reorder words
around them. Attribute texts (alt, title, aria-label, placeholder, meta content)
and selected data-* JSON values are extracted as separate strings.
"""
import re, html, json

INLINE = {"strong", "b", "em", "i", "span", "br", "small", "sup", "sub", "mark", "u", "s", "abbr", "code", "wbr"}
VOID = {"br", "wbr", "img", "input", "meta", "link", "hr", "source"}
TOK = re.compile(r"(<!--.*?-->|<script\b.*?</script\s*>|<style\b.*?</style\s*>|<textarea\b.*?</textarea\s*>|<[^>]+>)", re.S | re.I)
LETTER = re.compile(r"[A-Za-zÀ-ÿ]")
ATTR_RE = re.compile(r'''(\s)(alt|title|aria-label|placeholder|data-label|data-placeholder)="([^"]*)"''')
META_RE = re.compile(r'''<meta\b[^>]*\b(?:name|property)="(?:description|og:title|og:description|twitter:title|twitter:description)"[^>]*>''', re.I)
JSON_ATTR_RE = re.compile(r'''(\s)(data-route-output-map|data-related|data-copy)='([^']*)\'''')

def tagname(t):
    m = re.match(r"</?\s*([a-zA-Z0-9-]+)", t)
    return m.group(1).lower() if m else ""

def is_inline(t):
    if t.startswith("<!--"): return False
    return tagname(t) in INLINE

def tokens(page):
    parts = TOK.split(page)
    out = []
    for i, p in enumerate(parts):
        if p == "": continue
        out.append(("tag" if i % 2 else "text", p))
    return out

def segments(page):
    """Yield (start_index, end_index, encoded_text, tags) over the token list."""
    toks = tokens(page)
    segs = []
    i, n = 0, len(toks)
    while i < n:
        kind, val = toks[i]
        if kind == "text" or (kind == "tag" and is_inline(val)):
            j = i
            while j < n and (toks[j][0] == "text" or is_inline(toks[j][1])):
                j += 1
            run = toks[i:j]
            if any(k == "text" and LETTER.search(html.unescape(v)) for k, v in run):
                segs.append((i, j, run))
            i = j
        else:
            i += 1
    return toks, segs

def encode(run):
    """Turn a token run into (lead_ws, encoded, trail_ws, tagmap)."""
    tagmap, stack, parts, idx = {}, [], [], 0
    for k, v in run:
        if k == "text":
            parts.append(html.unescape(v))
        else:
            name = tagname(v)
            if v.startswith("</"):
                # find matching open
                for pos in range(len(stack) - 1, -1, -1):
                    if stack[pos][0] == name:
                        n = stack.pop(pos)[1]
                        parts.append(f"</x{n}>"); tagmap[f"</x{n}>"] = v
                        break
                else:
                    parts.append(f"<x{idx}/>"); tagmap[f"<x{idx}/>"] = v; idx += 1
            elif name in VOID or v.endswith("/>"):
                parts.append(f"<x{idx}/>"); tagmap[f"<x{idx}/>"] = v; idx += 1
            else:
                stack.append((name, idx)); parts.append(f"<x{idx}>"); tagmap[f"<x{idx}>"] = v; idx += 1
    for name, n in stack:  # unclosed opening tags: make them singletons
        old = f"<x{n}>"; new = f"<x{n}/>"
        parts = [new if p == old else p for p in parts]; tagmap[new] = tagmap.pop(old)
    s = "".join(parts)
    lead = re.match(r"\s*", s).group(0); trail = re.search(r"\s*$", s).group(0)
    core = s[len(lead):len(s) - len(trail)] if trail else s[len(lead):]
    return lead, core, trail, tagmap

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

def decode(translated, tagmap):
    out = []
    for piece in re.split(r"(</?x\d+/?>)", translated):
        if re.fullmatch(r"</?x\d+/?>", piece):
            if piece not in tagmap: raise KeyError(piece)
            out.append(tagmap[piece])
        else:
            out.append(html.escape(piece, quote=False))
    return "".join(out)

def placeholders(s):
    return sorted(re.findall(r"</?x\d+/?>", s))
