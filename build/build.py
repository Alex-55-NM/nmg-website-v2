"""Generate the Next Mind Group v2 website into ../site.

Usage: python3 build/build.py
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
SITE = os.path.join(os.path.dirname(HERE), "site")

import pages_home, pages_approach, pages_services, pages_other as o

def write(path, html):
    full = os.path.join(SITE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)

def main():
    pages = {
        "index.html": pages_home.build(),
        "approach.html": pages_approach.build(),
        "group.html": o.group(),
        "industries.html": o.industries(),
        "working-with-us.html": o.working(),
        "trust.html": o.trust(),
        "careers.html": o.careers(),
        "contact.html": o.contact(),
        "credits.html": o.credits(SITE),
        "404.html": o.notfound(),
    }
    pages.update(pages_services.build())
    for path, html in pages.items():
        write(path, html)
    print(f"Built {len(pages)} pages into {SITE}")

if __name__ == "__main__":
    main()
