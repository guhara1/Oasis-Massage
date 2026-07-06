# 간다GO · 경기남부 출장마사지 안내 사이트

경기남부(수원·분당·용인·동탄·오산·평택·안산 등) 출장마사지·홈타이 지역·프로그램·이용 장소
안내를 위한 정적 웹사이트입니다.

- **상호:** 간다GO
- **전화예약:** 0508-202-4719
- **프리미엄 팔레트 + Pretendard** 기반 디자인 토큰 / 컴포넌트 오버레이 (`assets/css/styles.css`)
- 모든 페이지에 **모바일 우측 하단 애니메이션 전화 아이콘**(터치 시 전화 연결, 오렌지)
- 푸터에 **웹사이트 제작문의 / 제휴문의** 오렌지 버튼(텔레그램 링크)
- **구조화 데이터(JSON-LD):** Organization · WebPage · BreadcrumbList · FAQPage
  (실제 매장·리뷰가 없으므로 LocalBusiness / Review / AggregateRating 미사용)
- 메타 디스크립션 80자 이내, canonical/OG/robots/sitemap 포함

## 페이지 생성

정적 HTML은 파이썬 제너레이터로 생성합니다. 콘텐츠 수정 후 아래를 실행하세요.

```bash
python3 build.py
```

- `build.py` — 레이아웃(헤더·푸터·플로팅 콜·스키마) 및 공통 컴포넌트
- `build_pages.py` — 페이지별 본문 콘텐츠

## 배포 전 교체 항목

`build.py` 상단 상수를 실제 값으로 교체하세요.

- `BASE` — 실제 도메인 (canonical/OG/sitemap에 사용)
- `TELEGRAM_BUILD`, `TELEGRAM_PARTNER` — 실제 텔레그램 핸들
- `assets/img/og-cover.jpg`, `assets/img/logo.png` — OG 커버·로고 이미지
