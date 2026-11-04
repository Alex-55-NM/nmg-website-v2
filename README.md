# Next Mind Group website, version 2

A second, independent website for Next Mind Group, built from scratch from the Group documents (Group Business Plan 25/07/26, Business Model Canvas, Consulting execution framework, recruitment standards). It runs in parallel with the first site in `Alex-55-NM/nmg-website` so the two can be compared.

## What is different from version 1

- **Organised around the route a client's request takes**: one interface company (Solutions in Italy, Consulting in the UAE), three delivery centres in India, acceptance at the end. The home page shows this as an animated route diagram.
- **The execution framework is published**: six phases (Assess, Design, Plan, Deliver, Measure, Improve), with what the client provides, what Next Mind does and which documents the client receives at each step.
- **Group structure stated as it is in the Business Plan**: Holding in Cyprus, Consulting UAE, Solutions Italy, Platform, Engineering & Production and Trade & Logistics in India, North America hub planned.
- **Honest by default**: no client logos, metrics or certifications that are not in place; the contact form prepares a brief instead of pretending to send it.
- **Visual identity**: IBM Plex Sans (one family, condensed for headings), drafting-paper background, navy ink, cobalt route line. Fonts and photos are self-hosted.

## Pages (17, in English and Italian)

Home, How we work, Services (overview + 6 service pages), Industries, The Group, Working with us, Trust, Careers, Start a project, Credits, 404.

The Italian pages are in `site/it/` and are generated from the English ones: every text, alt text and meta description is looked up in `build/i18n/it.tsv` (`English<TAB>Italian`). The build stops if a string has no translation; `python3 build/build.py --extract` lists the missing ones in `build/i18n/missing_it.txt`. The header has an IT / EN switch and each page declares its other-language version with `hreflang`.

## Structure

```
build/            Python generator: page content and templates
  build.py        entry point: python3 build/build.py
  layout.py       header, footer, shared helpers
  pages_*.py      page content
  i18n.py         builds site/it/ from the English pages
  i18n/it.tsv     Italian translations
  photo_ids.txt   Pexels photos to self-host (fetched by a workflow)
site/             generated website (this is what gets published)
  assets/css/site.css
  assets/js/site.js
  assets/fonts/   IBM Plex Sans subset (SIL OFL)
  assets/img/     logos and Pexels photos (CREDITS.json)
scripts/check_links.py
```

Edit content in `build/pages_*.py`, run `python3 build/build.py`, then commit both `build/` and `site/`. The "Validate site" workflow rebuilds the pages and fails if `site/` is out of date or a local link is broken.

## View locally

```
cd site && python3 -m http.server 8000
```

Then open http://localhost:8000.

## Publish

Run the "Deploy to GitHub Pages" workflow from the Actions tab (enable Pages with source "GitHub Actions" first).

## Open points

- The contact form is not connected to an inbox; it builds a brief the visitor copies or downloads. Connect it once the Group contact address and form backend are decided.
- English and Italian only. Other languages can be added with one more `.tsv` file per language.
