# MindMapPro — EdrawMind Authority Site

**Live:** https://brightlane.github.io/edrawmind/  
**Affiliate:** https://www.linkconnector.com/ta.php?lc=007949115400004532&atid=edrawmindweb  
**Pages:** 65 · **Languages:** 10 · **Build:** `python3 build.py`

---

## Quick Start

```bash
git clone https://github.com/brightlane/edrawmind.git
cd edrawmind
python3 build.py
# → docs/ is ready to deploy
```

---

## Deploy to GitHub Pages

1. Add `build.py` to repo root
2. Add `deploy.yml` to `.github/workflows/deploy.yml`
3. Go to **Settings → Pages → Source → GitHub Actions**
4. Push to `main` — or go to **Actions → Run workflow** to trigger manually

---

## What's Inside

### Pages (65 total)

| Language | Count | Pages |
|----------|-------|-------|
| 🇺🇸 English | 28 | Home, Review, 5× vs-comparisons, Pricing, AI Features, Mind Map Maker, Templates, Collaboration, Gantt, 4 use-case pages, Brainstorming, Concept Map, Flowchart, Presentation Mode, Export, Download, Deals, Free vs Paid, 3 guide pages |
| 🇪🇸 Spanish | 6 | Home, vs-XMind, Mind Map, Students, Pricing, AI |
| 🇫🇷 French | 6 | Home, vs-XMind, Mind Map, Students, Pricing, AI |
| 🇩🇪 German | 6 | Home, vs-XMind, Mind Map, Students, Pricing, AI |
| 🇧🇷 Portuguese | 5 | Home, vs-XMind, Mind Map, Students, Pricing |
| 🇯🇵 Japanese | 4 | Home, vs-XMind, Mind Map, Pricing |
| 🇨🇳 Chinese | 4 | Home, vs-XMind, Mind Map, Pricing |
| 🇰🇷 Korean | 2 | Home, Mind Map |
| 🇮🇹 Italian | 2 | Home, Mind Map |
| 🇳🇱 Dutch | 2 | Home, Mind Map |

### Static Files

| File | Purpose |
|------|---------|
| `sitemap.xml` | All 65 pages with priorities and lastmod |
| `robots.txt` | Allows all crawlers including GPTBot and Claude-Web |
| `404.html` | Branded error page with CTA |
| `llms.txt` | AI crawler index — site summary + all page links |
| `humans.txt` | Build metadata |

---

## SEO on Every Page

- Unique `<title>` and `<meta description>`
- `<link rel="canonical">`
- Full `hreflang` set (10 languages + `x-default`)
- **WebPage** JSON-LD schema on every page
- **SoftwareApplication** schema on homepage
- **BreadcrumbList** on all non-home pages
- **FAQPage** schema on all FAQ sections
- **HowTo** schema on all use-case and guide pages
- `rel="nofollow sponsored"` on all affiliate links
- `max-snippet:-1` robots meta for rich snippets

---

## Repo Structure

```
edrawmind/
├── build.py                         # Entire site generator — edit this
├── docs/                            # Generated output — do not edit
│   ├── index.html
│   ├── review.html
│   ├── vs-xmind.html
│   ├── vs-mindmeister.html
│   ├── vs-miro.html
│   ├── vs-mindmanager.html
│   ├── vs-coggle.html
│   ├── pricing.html
│   ├── ai-features.html
│   ├── mind-map-maker.html
│   ├── templates.html
│   ├── collaboration.html
│   ├── gantt-chart.html
│   ├── for-students.html
│   ├── for-teachers.html
│   ├── for-business.html
│   ├── for-project-management.html
│   ├── brainstorming.html
│   ├── concept-map.html
│   ├── flowchart.html
│   ├── presentation-mode.html
│   ├── export-options.html
│   ├── download.html
│   ├── deals.html
│   ├── free-vs-paid.html
│   ├── mind-mapping-guide.html
│   ├── study-techniques.html
│   ├── note-taking.html
│   ├── es/  fr/  de/  pt/  ja/  zh/  ko/  it/  nl/
│   ├── sitemap.xml
│   ├── robots.txt
│   ├── 404.html
│   ├── llms.txt
│   └── humans.txt
└── .github/
    └── workflows/
        └── deploy.yml
```

---

## How to Edit

Everything is in `build.py`. Clearly marked sections:

| What | Where |
|------|-------|
| Affiliate link | `AFF = "..."` — top of file |
| Base URL | `BASE = "..."` — top of file |
| Add/remove pages | `PAGES` list |
| All styles | `css()` function |
| Nav, footer, `<head>` | `layout()` function |
| English page content | `page_*()` functions |
| Multilingual content | `page_*_es/fr/de/...()` functions |
| Page router | `FN_MAP` dict |

### Change the affiliate link

```python
AFF = "https://your-new-link-here"
```

Propagates to every button, nav CTA, ticker, and sticky bar on next build.

### Add a new English page

**1. Add to PAGES:**
```python
{"slug":"new-topic", "lang":"en",
 "title":"New Topic 2026 | EdrawMind Guide",
 "desc":"Description for search engines.",
 "fn":"page_new_topic", "priority":"0.85"},
```

**2. Write the function:**
```python
def page_new_topic():
    return f"""
<section class="hero">...</section>
<section class="bg2">
  <div class="container">
    {feat_grid(...)}
  </div>
</section>"""
```

**3. Register in FN_MAP:**
```python
"page_new_topic": page_new_topic,
```

**4. Build:** `python3 build.py`

---

## Design System

Dark teal/blue technical theme.

| Token | Value |
|-------|-------|
| Background | `#060912` |
| Surface | `#0a0f1e` |
| Teal (primary) | `#00c9a7` |
| Blue (accent) | `#3b82f6` |
| Amber (CTA) | `#f59e0b` |
| Emerald (positive) | `#10b981` |
| Body font | Inter |
| Display font | Fraunces (serif) |
| Mono font | JetBrains Mono |

### Component helpers

```python
feat_grid(("emoji","Title","Description"), ..., variant="teal")
steps(("Step Title","Description"), ...)
testimonials(("Quote","Name","Role","🇺🇸","5"), ...)
faq(("Question?","Answer"), ..., schema=True)
score_bars(("Label", 95, "4.6/5"), ...)
cmp_table(rows, c1="EdrawMind", c2="XMind")
cta_band("Heading", "Subtext", "Button text")
trust_strip()
lang_hero(pill, badge, h1, h1em, sub, cta)

# Multilingual builder helpers:
_home(pill, badge, h1, h1em, sub, cta, feats, testis, faqs, vs_rows)
_vs(pill, badge, h1, h1em, sub, cta, rows, faqs)
_mindmap(pill, badge, h1, h1em, sub, cta, feats, faqs)
_students(...)   _pricing(...)   _ai(...)
```

---

## Key Selling Points to Emphasise

The core EdrawMind narrative is **AI + completeness**:

- Only major mind mapper with **one-click AI generation** of complete multi-level maps
- **700+ templates** vs ~100 in XMind, ~50 in MindMeister
- **Gantt chart view** built in — unique feature, no competitor matches it
- **Perpetual license** (~$118) vs subscription-only competitors
- **Linux support** — rare in this category
- Works on every platform: Windows, Mac, Linux, iOS, Android, browser
- ~$59/year vs MindMeister's ~$78/year and MindManager's ~$349/year

---

## License

Content © 2026 MindMapPro. Independent EdrawMind affiliate site. Not affiliated with Wondershare Technology.  
EdrawMind is a trademark of Wondershare Technology Group Co., Ltd.
