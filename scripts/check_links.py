"""Check that every local href, src and srcset in site/ points to an existing file."""
import re, os, glob, sys
root = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site")
bad = []
pages = glob.glob(root + "/**/*.html", recursive=True)
for f in pages:
    s = open(f, encoding="utf-8").read()
    refs = re.findall(r'(?:href|src)="([^"#?]+)', s)
    for m in re.findall(r'srcset="([^"]+)"', s):
        refs += [part.strip().split(" ")[0] for part in m.split(",")]
    for ref in refs:
        if ref.startswith(("http:", "https:", "mailto:", "data:")):
            continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), ref))):
            bad.append(f"{os.path.relpath(f, root)} -> {ref}")
print(f"{len(pages)} pages checked, {len(bad)} broken local references")
for b in bad: print("  " + b)
sys.exit(1 if bad else 0)
