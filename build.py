#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
간다GO · 경기남부 출장마사지 — static site generator.
Produces consistent, differentiated pages sharing one design system,
footer (orange Telegram buttons), floating call button, and JSON-LD schema.
"""
import os, json, html, pathlib

ROOT = pathlib.Path(__file__).parent

# ---- Business / brand constants --------------------------------------------
BRAND      = "간다GO"
SITE_NAME  = "간다GO 경기남부 출장마사지"
BASE       = "https://www.gandago.kr"          # ← replace with real domain
TEL_LABEL  = "0508-202-4719"
TEL_HREF   = "tel:05082024719"
TELEGRAM_BUILD   = "https://t.me/gandago_web"   # 웹사이트 제작문의 (replace handle)
TELEGRAM_PARTNER = "https://t.me/gandago_ad"    # 제휴문의 (replace handle)

def esc(s): return html.escape(s, quote=True)

# ---- Global nav -------------------------------------------------------------
NAV = [
    ("홈", "/"),
    ("수원·광교", "/gyeonggi-south/area/suwon-gwanggyo-yeongtong/"),
    ("분당·판교", "/gyeonggi-south/area/seongnam-bundang-pangyo/"),
    ("용인·수지", "/gyeonggi-south/area/yongin-suji-giheung/"),
    ("동탄·화성", "/gyeonggi-south/area/dongtan-hwaseong/"),
    ("오산·세교", "/gyeonggi-south/area/osan-segyo/"),
    ("평택·고덕", "/gyeonggi-south/area/pyeongtaek-anseong-icheon/"),
    ("안산·시흥", "/gyeonggi-south/area/ansan-siheung-anyang-gwangmyeong/"),
    ("프로그램", "/gyeonggi-south/program/"),
    ("이용 장소", "/gyeonggi-south/use/"),
    ("예약 전 확인", "/gyeonggi-south/check/"),
]

PHONE_SVG = ('<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
             '<path d="M6.6 10.8a15.6 15.6 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.24 11.4 11.4 0 0 0 3.6.58 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.4 11.4 0 0 0 .58 3.6 1 1 0 0 1-.24 1L6.6 10.8Z" '
             'fill="currentColor"/></svg>')

# ---- Layout -----------------------------------------------------------------
def render_nav(active):
    items = []
    for label, href in NAV:
        cls = ' style="color:var(--text)"' if href == active else ""
        items.append(f'<a href="{href}"{cls}>{esc(label)}</a>')
    links = "\n        ".join(items)
    return f'''<header class="site-header">
    <div class="container nav">
      <a class="brand" href="/"><span class="mark">G</span>간다<span class="go">GO</span></a>
      <nav class="nav-links" id="navLinks">
        {links}
      </nav>
      <a class="nav-tel" href="{TEL_HREF}">📞 {TEL_LABEL}</a>
      <button class="nav-toggle" aria-label="메뉴 열기" aria-expanded="false">☰</button>
    </div>
  </header>'''

def render_footer():
    build_links = "\n          ".join(
        f'<li><a href="{h}">{esc(l)}</a></li>' for l, h in [
            ("경기남부 메인", "/"),
            ("마사지 프로그램", "/gyeonggi-south/program/"),
            ("이용 장소 안내", "/gyeonggi-south/use/"),
            ("예약 전 확인사항", "/gyeonggi-south/check/"),
            ("문의하기", "/contact/"),
        ])
    area_links = "\n          ".join(
        f'<li><a href="{h}">{esc(l)}</a></li>' for l, h in [
            ("수원·광교·영통", "/gyeonggi-south/area/suwon-gwanggyo-yeongtong/"),
            ("성남·분당·판교", "/gyeonggi-south/area/seongnam-bundang-pangyo/"),
            ("용인·수지·기흥", "/gyeonggi-south/area/yongin-suji-giheung/"),
            ("동탄·화성", "/gyeonggi-south/area/dongtan-hwaseong/"),
            ("오산·세교", "/gyeonggi-south/area/osan-segyo/"),
            ("안산·시흥·안양·광명", "/gyeonggi-south/area/ansan-siheung-anyang-gwangmyeong/"),
        ])
    return f'''<footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a class="brand" href="/"><span class="mark">G</span>간다<span class="go">GO</span></a>
          <p class="small muted">경기남부 출장마사지·홈타이 지역·프로그램·이용 장소 안내 사이트입니다. 방문 가능 여부는 실제 주소와 예약 조건 확인 후 안내합니다.</p>
          <p class="small">전화예약 <a class="tel-strong" href="{TEL_HREF}">{TEL_LABEL}</a></p>
          <div class="footer-cta">
            <a class="btn btn--orange" href="{TELEGRAM_BUILD}" target="_blank" rel="noopener nofollow">💬 웹사이트 제작문의</a>
            <a class="btn btn--orange" href="{TELEGRAM_PARTNER}" target="_blank" rel="noopener nofollow">🤝 제휴문의</a>
          </div>
        </div>
        <div>
          <h4>바로가기</h4>
          <ul class="footer-links">
          {build_links}
          </ul>
        </div>
        <div>
          <h4>주요 생활권</h4>
          <ul class="footer-links">
          {area_links}
          </ul>
        </div>
      </div>
      <div class="footer-meta">
        <p>상호: {BRAND} · 전화예약: <a class="tel-strong" href="{TEL_HREF}">{TEL_LABEL}</a></p>
        <p>본 사이트는 불법·선정적 서비스를 제공하거나 안내하지 않습니다. 건전한 방문형 웰니스 정보 안내 목적입니다.</p>
        <p>© {BRAND}. 경기남부 출장마사지 지역·프로그램 안내.</p>
      </div>
    </div>
  </footer>'''

def floating_call():
    return (f'<a class="floating-call" href="{TEL_HREF}" aria-label="전화 예약 {TEL_LABEL}">'
            f'<span class="fc-label">전화 예약 {TEL_LABEL}</span>{PHONE_SVG}</a>')

def jsonld(blocks):
    out = []
    for b in blocks:
        out.append('<script type="application/ld+json">' +
                   json.dumps(b, ensure_ascii=False, separators=(",", ":")) + '</script>')
    return "\n  ".join(out)

def organization_schema():
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": BRAND,
        "alternateName": "경기남부 출장마사지",
        "url": BASE + "/",
        "logo": BASE + "/assets/img/logo.png",
        "image": BASE + "/assets/img/og-cover.jpg",
        "telephone": "+82-508-202-4719",
        "areaServed": "경기 남부",
        "contactPoint": {
            "@type": "ContactPoint",
            "telephone": "+82-508-202-4719",
            "contactType": "reservations",
            "areaServed": "KR",
            "availableLanguage": "Korean",
        },
    }

def breadcrumb_schema(trail):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name,
             "item": BASE + href}
            for i, (name, href) in enumerate(trail)
        ],
    }

def webpage_schema(url, title, desc):
    return {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "@id": BASE + url + "#webpage",
        "url": BASE + url,
        "name": title,
        "description": desc,
        "inLanguage": "ko-KR",
        "isPartOf": {"@type": "WebSite", "name": SITE_NAME, "url": BASE + "/"},
        "primaryImageOfPage": {"@type": "ImageObject", "url": BASE + "/assets/img/og-cover.jpg"},
    }

def faq_schema(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }

def breadcrumb_html(trail):
    parts = []
    for i, (name, href) in enumerate(trail):
        if i < len(trail) - 1:
            parts.append(f'<a href="{href}">{esc(name)}</a>')
        else:
            parts.append(f'<span aria-current="page" style="opacity:1;color:var(--text-muted)">{esc(name)}</span>')
    return '<span>›</span>'.join(parts)

def page(url, title, desc, body, trail=None, faqs=None, extra_schema=None, noindex=False):
    """Assemble a full HTML document."""
    assert len(desc) <= 80, f"description too long ({len(desc)}): {desc}"
    trail = trail or [("홈", "/")]
    schema_blocks = [organization_schema(), webpage_schema(url, title, desc), breadcrumb_schema(trail)]
    if faqs:
        schema_blocks.append(faq_schema(faqs))
    if extra_schema:
        schema_blocks.extend(extra_schema)
    canonical = BASE + url
    og_img = BASE + "/assets/img/og-cover.jpg"
    robots = "noindex,follow" if noindex else "index,follow"
    active = url if any(url == h for _, h in NAV) else "/"
    doc = f'''<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <meta name="robots" content="{robots}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{esc(SITE_NAME)}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{og_img}">
  <meta property="og:locale" content="ko_KR">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(desc)}">
  <meta name="twitter:image" content="{og_img}">
  <meta name="theme-color" content="#0c1017">
  <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable.min.css">
  <link rel="stylesheet" href="/assets/css/styles.css">
  {jsonld(schema_blocks)}
</head>
<body>
  {render_nav(active)}
  {body}
  {render_footer()}
  {floating_call()}
  <script src="/assets/js/site.js" defer></script>
</body>
</html>'''
    return doc

def write(url, doc):
    if url.endswith("/"):
        path = ROOT / url.strip("/") / "index.html"
    else:
        path = ROOT / url.lstrip("/")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(doc, encoding="utf-8")
    print("wrote", path.relative_to(ROOT))

# ---- Reusable content blocks ------------------------------------------------
ILLEGAL_NOTICE = ('<div class="notice"><strong>불법·선정적 서비스 불가 안내</strong><br>'
                  f'{BRAND}는 불법·선정적 서비스를 제공하거나 안내하지 않습니다. '
                  '방문 가능 여부는 실제 주소, 건물 출입 조건, 예약 가능 시간 확인 후 안내합니다.</div>')

def whw_block(who, how, why):
    return f'''<section class="section section--tight">
      <div class="container">
        <h2 class="center">Who · How · Why</h2>
        <div class="whw">
          <div class="card"><h3>Who</h3><p>{esc(who)}</p></div>
          <div class="card"><h3>How</h3><p>{esc(how)}</p></div>
          <div class="card"><h3>Why</h3><p>{esc(why)}</p></div>
        </div>
      </div>
    </section>'''

def faq_block(faqs):
    items = "\n        ".join(
        f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in faqs)
    return f'''<section class="section section--tight">
      <div class="container">
        <h2>자주 묻는 질문</h2>
        <div class="faq">
        {items}
        </div>
      </div>
    </section>'''

def cards_grid(cols, cards):
    """cards = list of (tag, title, desc, href)"""
    out = []
    for tag, title, d, href in cards:
        tagline = f'<span class="tag">{esc(tag)}</span>' if tag else ""
        arrow = '<span class="arrow">자세히 보기 →</span>' if href else ""
        if href:
            out.append(f'<a class="card" href="{href}">{tagline}<h3>{esc(title)}</h3>'
                        f'<p>{esc(d)}</p>{arrow}</a>')
        else:
            out.append(f'<div class="card">{tagline}<h3>{esc(title)}</h3><p>{esc(d)}</p></div>')
    return f'<div class="grid grid--{cols}">' + "\n        ".join(out) + '</div>'

# ===========================================================================
#  BUILD
# ===========================================================================
import build_pages  # content lives in a companion module

if __name__ == "__main__":
    build_pages.build(globals())
    print("done.")
