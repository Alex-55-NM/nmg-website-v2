"""Shared page shell for the v2 site: head, header, footer."""
import html

SITE = "Next Mind Group"
NAV = [
    ("services/index.html", "Services"),
    ("approach.html", "How we work"),
    ("industries.html", "Industries"),
    ("group.html", "The Group"),
    ("working-with-us.html", "Working with us"),
    ("trust.html", "Trust"),
]

def esc(s):
    return html.escape(s, quote=True)

def photo(pre, pid, alt, cls="photo", sizes="(max-width: 900px) 100vw, 50vw", caption=None, eager=False):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    cap = f"<figcaption>{caption}</figcaption>" if caption else ""
    return (f'<figure class="{cls}"><img src="{pre}assets/img/photos/pexels-{pid}-1600.jpg" '
            f'srcset="{pre}assets/img/photos/pexels-{pid}-800.jpg 800w, {pre}assets/img/photos/pexels-{pid}-1600.jpg 1600w" '
            f'sizes="{sizes}" width="1600" height="1067" alt="{esc(alt)}" decoding="async" {load}>{cap}</figure>')

def page(path, title, description, body, current=None):
    depth = path.count("/")
    pre = "../" * depth
    nav = "".join(
        f'<a href="{pre}{href}"{" aria-current=\"page\"" if current == href else ""}>{label}</a>'
        for href, label in NAV)
    menu = "".join(f'<a href="{pre}{href}">{label}</a>' for href, label in NAV)
    full_title = title if title.endswith(SITE) else f"{title} | {SITE}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(description)}">
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#0A1A33">
<link rel="icon" href="{pre}assets/img/favicon-official.png">
<link rel="preload" href="{pre}assets/fonts/ibm-plex-sans-var.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="{pre}assets/css/site.css">
<script src="{pre}assets/js/site.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{pre}index.html"><img src="{pre}assets/img/next-mind-logo-2026.webp" width="160" height="40" alt="Next Mind Group, home"></a>
    <nav class="nav" aria-label="Main">{nav}<a class="btn" href="{pre}contact.html">Start a project</a></nav>
    <details class="menu"><summary>Menu</summary><div class="menu-panel">{menu}<a class="btn" href="{pre}contact.html">Start a project</a></div></details>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <img src="{pre}assets/img/next-mind-logo-on-dark-2026.webp" width="160" height="40" alt="Next Mind Group">
        <p>Strategy, digital, engineering, production and trade capabilities, coordinated as one route from your need to an accepted result.</p>
      </div>
      <div><h2>Services</h2><ul>
        <li><a href="{pre}services/strategy-growth.html">Strategy &amp; Growth</a></li>
        <li><a href="{pre}services/digital-operations.html">Digital Operations</a></li>
        <li><a href="{pre}services/engineering-industrialisation.html">Engineering &amp; Industrialisation</a></li>
        <li><a href="{pre}services/production.html">Production</a></li>
        <li><a href="{pre}services/trade-logistics.html">Trade &amp; Logistics</a></li>
        <li><a href="{pre}services/integrated-programmes.html">Integrated Programmes</a></li>
      </ul></div>
      <div><h2>Company</h2><ul>
        <li><a href="{pre}approach.html">How we work</a></li>
        <li><a href="{pre}group.html">The Group</a></li>
        <li><a href="{pre}industries.html">Industries</a></li>
        <li><a href="{pre}careers.html">Careers</a></li>
      </ul></div>
      <div><h2>Engage</h2><ul>
        <li><a href="{pre}working-with-us.html">Working with us</a></li>
        <li><a href="{pre}trust.html">Trust and data</a></li>
        <li><a href="{pre}contact.html">Start a project</a></li>
      </ul></div>
    </div>
    <div class="foot-base">
      <span>&copy; 2026 Next Mind Group. Connecting minds, building futures.</span>
      <span>Photos: Pexels License, see <a href="{pre}credits.html">credits</a>.</span>
    </div>
  </div>
</footer>
</body>
</html>
"""
