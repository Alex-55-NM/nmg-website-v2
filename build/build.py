"""Generate the Next Mind Group v2 website into ../site.

Usage: python3 build/build.py
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
SITE = os.path.join(os.path.dirname(HERE), "site")

import pages_home, pages_approach, pages_services, pages_other as o
import i18n

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
    table = i18n.load()
    if "--extract" in sys.argv:
        seen, todo = set(), []
        for html in pages.values():
            for st in i18n.strings(html):
                if st not in seen and st not in table and not any(rx.match(st) for rx, _ in i18n.AUTO):
                    seen.add(st); todo.append(st)
        out = os.path.join(HERE, "i18n", "missing_it.txt")
        open(out, "w", encoding="utf-8").write("\n".join(todo) + "\n")
        print(f"{len(todo)} strings without Italian translation written to {out}")
        return
    missing = set()
    for path, html in pages.items():
        write("it/" + path, i18n.translate(path, html, table, missing))
    if missing:
        sys.exit(f"{len(missing)} strings have no Italian translation; run build.py --extract")
    print(f"Built {len(pages)} pages in English and Italian into {SITE}")

if __name__ == "__main__":
    main()
