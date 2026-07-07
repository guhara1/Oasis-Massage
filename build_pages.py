# -*- coding: utf-8 -*-
"""Page content for 간다GO 경기남부 출장마사지. Called by build.py."""

def build(g):
    page      = g["page"]
    write     = g["write"]
    cards     = g["cards_grid"]
    faq_block = g["faq_block"]
    whw_block = g["whw_block"]
    esc       = g["esc"]
    NOTICE    = g["ILLEGAL_NOTICE"]
    TEL_HREF  = g["TEL_HREF"]
    TEL_LABEL = g["TEL_LABEL"]
    BASE      = g["BASE"]

    # -------------------------------------------------------------------
    # Shared data
    # -------------------------------------------------------------------
    AREAS = [
        ("suwon-gwanggyo-yeongtong", "수원·광교·영통권",
         "수원, 광교, 영통, 인계동, 수원역, 매탄, 권선, 장안"),
        ("seongnam-bundang-pangyo", "성남·분당·판교권",
         "성남, 분당, 판교, 정자, 수내, 서현, 야탑, 모란, 위례"),
        ("yongin-suji-giheung", "용인·수지·기흥권",
         "용인, 수지, 죽전, 기흥, 신갈, 보정, 동백, 처인"),
        ("dongtan-hwaseong", "동탄·화성권",
         "동탄, 병점, 향남, 봉담, 화성, 세교 인접"),
        ("osan-segyo", "오산·세교권",
         "오산, 세교, 궐동, 원동, 운암, 오산대역, 오산시청"),
        ("pyeongtaek-anseong-icheon", "평택·안성·이천권",
         "평택, 고덕, 지제, 송탄, 안성, 공도, 이천, 부발"),
        ("ansan-siheung-anyang-gwangmyeong", "안산·시흥·안양·광명권",
         "안산, 고잔, 반월·시화산단, 시흥, 배곧, 정왕, 안양, 평촌, 범계, 광명, 철산"),
    ]

    PROGRAMS = [
        ("swedish", "스웨디시", "부드러운 압과 오일로 전신 릴렉스. 숙소·오피스텔 이용 전 확인사항을 함께 안내합니다."),
        ("thai-massage", "타이마사지", "스트레칭 중심 관리. 공간 확보와 복장, 자택·아파트 이용 기준을 안내합니다."),
        ("aroma-therapy", "아로마테라피", "향·피부 민감도 확인 후 오일 관리. 호텔·오피스텔 이용 기준을 안내합니다."),
        ("sports-massage", "스포츠 마사지", "운동 후 부위별 압 조절 관리. 무리한 압을 지양하는 기준으로 안내합니다."),
        ("foot-massage", "발마사지", "발·종아리 집중 관리. 장시간 보행·여행객 이용자 중심으로 안내합니다."),
    ]

    USES = [
        ("home", "자택·아파트", "방문 주소와 공동현관, 주차, 세대 출입 기준을 예약 전 확인합니다."),
        ("hotel", "호텔·숙소", "숙소 정책, 프런트 확인, 방문자 출입 가능 여부를 먼저 확인합니다."),
        ("officetel", "오피스텔", "공동현관, 관리규정, 방문 등록 방식을 예약 전 확인합니다."),
        ("apartment", "아파트 단지", "단지 출입, 동·호수 확인, 방문 차량 기준을 안내합니다."),
    ]

    CHECKS = [
        ("방문 주소 확인", "정확한 도로명 주소와 상세 위치, 가까운 생활권을 먼저 확인합니다."),
        ("건물 출입 기준", "공동현관·엘리베이터·프런트 등 건물별 출입 방식을 확인합니다."),
        ("예약 가능 시간", "이동 거리와 예약 상황에 따라 방문 가능 시간을 안내합니다."),
        ("예약 변경 기준", "예약 변경·취소는 방문 전 여유를 두고 연락 주시면 조율합니다."),
        ("개인정보 처리", "예약에 필요한 최소 정보만 받고 목적 달성 후 안전하게 파기합니다."),
        ("야간 방문 기준", "‘무조건 24시간’이 아닌 주소·출입·이동 시간 확인 후 안내합니다."),
    ]

    def related_areas(exclude=None):
        return [("생활권", t, r, f"/gyeonggi-south/area/{s}/")
                for s, t, r in AREAS if s != exclude]

    # -------------------------------------------------------------------
    # 세부 생활권(life) — 각 지역 고유 콘텐츠 페이지
    # 도어웨이 회피: 이름만 바꾼 페이지가 아니라 지역별 실제 특성을 서술
    # 필드: (area, slug, tag, title, covers, stations, char, stay, prog)
    # -------------------------------------------------------------------
    LIFE = [
      # ── 수원·광교·영통권 ──────────────────────────────────────────
      ("suwon-gwanggyo-yeongtong","gwanggyo","신도시","광교신도시 생활권",
       "광교, 이의동, 하동, 광교호수공원",
       "광교중앙역·광교역(신분당선)",
       "광교신도시는 광교호수공원을 중심으로 고층 아파트와 주상복합, 오피스텔이 밀집한 계획도시입니다. 갤러리아 광교와 아브뉴프랑 상권, 경기대·법원 업무지구가 함께 있어 주상복합·오피스텔 이용 문의가 특히 많은 생활권입니다.",
       "광교는 주상복합·오피스텔 비중이 높아 공동현관과 방문자 등록, 엘리베이터 카드 방식이 건물마다 다릅니다. 예약 전 정확한 동·호수와 출입 방법을 확인하면 방문이 원활합니다.",
       ["스웨디시","아로마테라피"]),
      ("suwon-gwanggyo-yeongtong","yeongtong-maetan","주거·상권","영통·매탄·망포 생활권",
       "영통동, 매탄동, 망포동, 원천동",
       "영통역·망포역(수인분당선)",
       "영통·매탄은 삼성전자 수원사업장을 배후로 둔 대표 주거·상권 지역입니다. 망포 일대는 신축 대단지 아파트가 이어지고, 영통역 상권과 원천동 주거지가 함께 있어 아파트·오피스텔 이용 문의가 꾸준합니다.",
       "대단지 아파트는 방문 차량 등록과 동별 공동현관 출입이 필요한 경우가 많습니다. 정확한 단지명·동·호수와 지상·지하 주차 여부를 미리 확인합니다.",
       ["스웨디시","스포츠 마사지"]),
      ("suwon-gwanggyo-yeongtong","suwon-station-maesan","역세권·숙소","수원역·매산 생활권",
       "매산동, 고등동, 세류동, 수원역 상권",
       "수원역(1호선·수인분당선 환승)",
       "수원역은 백화점·복합환승센터를 낀 경기남부 최대 교통 결절점입니다. 롯데·AK 백화점과 매산동 상권, 인근 호텔·오피스텔이 밀집해 숙소형 이용 문의가 많은 생활권입니다.",
       "역 인근 호텔·비즈니스 숙소는 프런트 확인과 방문자 출입 정책이 숙소마다 다릅니다. 예약 전 숙소명과 객실, 방문 가능 여부를 먼저 확인합니다.",
       ["아로마테라피","발마사지"]),
      ("suwon-gwanggyo-yeongtong","ingye-cityhall","도심·상권","인계동·수원시청 생활권",
       "인계동, 수원시청, 나혜석거리, 법조타운",
       "수원시청역(수인분당선)",
       "인계동은 나혜석거리를 중심으로 한 수원 최대 번화가이자 상권 밀집 지역입니다. 수원시청·법조타운 업무지구와 오피스텔·주상복합이 함께 있어 도심형 이용 문의가 많습니다.",
       "도심 오피스텔·주상복합은 공동현관 비밀번호나 관리사무소 방문 등록이 필요할 수 있습니다. 정확한 건물명과 출입 방법을 예약 전 확인합니다.",
       ["스웨디시","타이마사지"]),
      ("suwon-gwanggyo-yeongtong","hwaseo-jangan","주거","화서·장안 생활권",
       "화서동, 정자동(수원), 조원동, 장안구청",
       "화서역(1호선)·성균관대역",
       "화서·장안 일대는 화서역세권 개발과 정자동·조원동 대단지 아파트가 이어지는 수원 북부 주거 중심 생활권입니다. 스타필드 수원과 화서역 개발로 주거·상권 수요가 늘고 있습니다.",
       "대단지 아파트가 많아 방문 차량 등록·동별 출입 확인이 중요합니다. 세대 위치와 주차 방식을 미리 확인하면 방문이 원활합니다.",
       ["스웨디시","발마사지"]),

      # ── 성남·분당·판교권 ──────────────────────────────────────────
      ("seongnam-bundang-pangyo","pangyo","업무지구","판교테크노밸리 생활권",
       "판교동, 삼평동, 백현동, 알파돔",
       "판교역(신분당선·경강선)",
       "판교는 국내 대표 IT·게임 기업이 모인 테크노밸리와 알파돔시티 업무·상권이 핵심인 생활권입니다. 백현동 아파트와 오피스텔, 현대백화점 판교점 상권이 함께 있어 업무지구·오피스텔 이용 문의가 많습니다.",
       "오피스·오피스텔 건물은 로비 방문 등록과 출입 게이트, 야간 출입 정책이 건물마다 다릅니다. 정확한 건물명·층·호수와 방문 가능 시간을 확인합니다.",
       ["스포츠 마사지","아로마테라피"]),
      ("seongnam-bundang-pangyo","jeongja-sunae","주거·상권","정자·수내 생활권",
       "정자동, 수내동, 백궁, 카페거리",
       "정자역·수내역(수인분당선·신분당선)",
       "정자동은 카페거리와 주상복합, 수내동은 분당 대표 아파트 상권이 자리한 생활권입니다. 정자역 주변 주상복합 오피스텔과 수내 학원가·상권이 함께 있어 주거·오피스텔 이용 문의가 꾸준합니다.",
       "주상복합 오피스텔은 공동현관 이중 출입과 방문자 등록이 흔합니다. 동·호수와 엘리베이터 이용 방식을 예약 전 확인합니다.",
       ["아로마테라피","스웨디시"]),
      ("seongnam-bundang-pangyo","seohyeon-imae","도심·아파트","서현·이매 생활권",
       "서현동, 이매동, AK플라자, 분당 중앙",
       "서현역·이매역(수인분당선·경강선)",
       "서현동은 AK플라자와 로데오 상권을 중심으로 한 분당의 대표 번화가이며, 이매동은 대단지 아파트 주거지입니다. 상권과 주거가 가까워 도심·아파트 이용 문의가 함께 많은 생활권입니다.",
       "아파트 단지는 방문 차량 등록과 동별 출입, 상가 오피스텔은 공동현관 확인이 필요합니다. 정확한 위치와 출입 방식을 미리 확인합니다.",
       ["스웨디시","스포츠 마사지"]),
      ("seongnam-bundang-pangyo","yatap-moran","교통·구도심","야탑·모란 생활권",
       "야탑동, 성남동, 모란, 성남종합버스터미널",
       "야탑역·모란역(수인분당선·8호선 환승)",
       "야탑은 성남종합버스터미널과 상권, 모란은 8호선 환승과 성남 구시가 상권이 자리한 생활권입니다. 교통 결절점과 오피스텔, 구도심 주거가 함께 있어 이용 유형이 다양합니다.",
       "터미널·역 인근 오피스텔과 구도심 빌라는 출입 방식이 제각각입니다. 건물 유형과 공동현관, 주차 가능 여부를 예약 전 확인합니다.",
       ["스포츠 마사지","타이마사지"]),
      ("seongnam-bundang-pangyo","wirye","신도시","위례신도시 생활권",
       "위례동, 창곡동, 복정 인접",
       "복정역·산성역 인접(8호선)",
       "위례신도시는 성남·하남·송파가 맞닿은 2기 신도시로, 트램 예정 노선과 대단지 아파트, 중심상가가 자리합니다. 신축 아파트·오피스텔 비중이 높아 세대 방문 문의가 많은 생활권입니다.",
       "신도시 대단지는 방문 차량 등록과 지하주차장 세대 출입이 일반적입니다. 정확한 단지·동·호수와 방문자 등록 절차를 미리 확인합니다.",
       ["아로마테라피","스웨디시"]),

      # ── 용인·수지·기흥권 ──────────────────────────────────────────
      ("yongin-suji-giheung","suji-jukjeon","주거","수지·죽전 생활권",
       "수지구청, 풍덕천, 죽전, 신봉, 성복",
       "수지구청역·죽전역(신분당선·수인분당선)",
       "수지·죽전은 신분당선·분당선을 낀 용인 북부 대표 주거 생활권입니다. 죽전 카페거리와 신세계·현대 상권, 성복·신봉 대단지 아파트가 이어져 아파트·오피스텔 이용 문의가 가장 많은 지역입니다.",
       "산지 지형의 대단지 아파트가 많아 동 위치와 주차층, 방문 차량 등록 확인이 중요합니다. 정확한 단지명과 세대 위치를 미리 확인합니다.",
       ["타이마사지","스웨디시"]),
      ("yongin-suji-giheung","giheung-singal","역세권·산업","기흥·신갈 생활권",
       "기흥역세권, 신갈, 구갈, 상갈, 보라",
       "기흥역(수인분당선·에버라인)·신갈역",
       "기흥은 기흥역세권 복합환승과 신축 오피스텔, 신갈은 삼성·기업 배후 주거·상권이 자리한 생활권입니다. 에버라인 환승과 인근 산업시설로 오피스텔·숙소 이용 문의가 꾸준합니다.",
       "역세권 오피스텔은 공동현관과 방문자 등록, 주차 정산 방식이 건물마다 다릅니다. 건물명·호수와 출입 방법을 예약 전 확인합니다.",
       ["스포츠 마사지","스웨디시"]),
      ("yongin-suji-giheung","bojeong-dongbaek","계획주거","보정·동백 생활권",
       "보정동, 동백지구, 초당, 어정",
       "보정역·초당역·동백역(수인분당선·에버라인)",
       "동백지구는 동백호수공원을 낀 계획 주거지, 보정동은 카페거리와 죽전 인접 주거지로 이어지는 생활권입니다. 대단지 아파트와 근린상가가 밀집해 아파트 세대 방문 문의가 많습니다.",
       "계획지구 아파트는 방문 차량 등록과 동별 공동현관 출입이 일반적입니다. 세대 위치와 주차 방식을 미리 확인합니다.",
       ["스웨디시","타이마사지"]),
      ("yongin-suji-giheung","cheoin-jungang","원도심·외곽","처인·용인중앙 생활권",
       "김량장동, 용인중앙시장, 처인구청, 역북",
       "용인중앙시장역·김량장역(에버라인)",
       "처인구 김량장동 일대는 용인중앙시장과 처인구청을 낀 용인의 원도심 생활권입니다. 역북지구 신축 아파트가 늘고 있으나 외곽 범위가 넓어 정확한 위치 확인이 특히 중요합니다.",
       "원도심 빌라·주택과 신축 아파트가 섞여 있어 출입 방식이 다양합니다. 도로명 주소와 건물 유형, 이동 거리를 예약 전 확인합니다.",
       ["타이마사지","발마사지"]),

      # ── 동탄·화성권 ───────────────────────────────────────────────
      ("dongtan-hwaseong","dongtan-newtown","신도시·SRT","동탄신도시 생활권",
       "동탄1·2신도시, 동탄호수공원, 반석산",
       "동탄역(SRT·GTX 예정)",
       "동탄신도시는 SRT 동탄역과 동탄호수공원을 중심으로 한 경기남부 최대 2기 신도시입니다. 고층 아파트와 오피스텔, 트램 예정 노선, 상업지구가 밀집해 신도시 세대·오피스텔 이용 문의가 가장 많은 생활권입니다.",
       "신축 대단지와 오피스텔은 방문 차량 등록·지하주차 세대 출입·공동현관 이중 인증이 흔합니다. 정확한 단지·건물명과 동·호수를 미리 확인합니다.",
       ["아로마테라피","스포츠 마사지"]),
      ("dongtan-hwaseong","byeongjeom-jinan","역세권·주거","병점·진안 생활권",
       "병점동, 진안동, 반정, 능동",
       "병점역(1호선)",
       "병점은 1호선 병점역을 낀 화성 북부의 관문 생활권으로, 동탄과 수원 사이 주거지가 이어집니다. 진안·반정지구 아파트와 병점역 상권이 함께 있어 아파트 이용 문의가 꾸준합니다.",
       "역세권 아파트·빌라가 섞여 있어 공동현관과 주차 방식이 다양합니다. 세대 위치와 방문 차량 등록 여부를 예약 전 확인합니다.",
       ["스웨디시","발마사지"]),
      ("dongtan-hwaseong","hyangnam-bongdam","택지·산단","향남·봉담 생활권",
       "향남읍, 봉담읍, 발안, 제약단지",
       "철도 없음(버스·자차 이동)",
       "향남·봉담은 향남제약단지와 대단지 아파트가 조성된 화성 서남부 신흥 주거권입니다. 철도역이 없어 이동 거리 확인이 중요하며, 봉담 택지지구 아파트 이용 문의가 늘고 있습니다.",
       "산업단지 인접 숙소와 택지 아파트가 함께 있어 정확한 주소와 이동 가능 시간 확인이 필수입니다. 방문 차량과 세대 출입 방식을 미리 확인합니다.",
       ["스포츠 마사지","스웨디시"]),
      ("dongtan-hwaseong","hwaseong-namyang","행정·외곽","화성 남양·시청 생활권",
       "남양읍, 화성시청, 새솔동(송산), 서해안",
       "자차 이동(서해선 인접)",
       "남양읍은 화성시청을 낀 행정 중심이며, 송산그린시티 새솔동 신도시가 서해안권으로 확장 중인 생활권입니다. 외곽 범위가 넓어 이동 기준과 정확한 위치 확인이 특히 중요합니다.",
       "행정 주거지와 신도시 아파트, 해안 숙소가 섞여 있어 이동 거리가 길 수 있습니다. 도로명 주소와 예약 가능 시간을 미리 확인합니다.",
       ["스웨디시","아로마테라피"]),

      # ── 오산·세교권 ───────────────────────────────────────────────
      ("osan-segyo","osan-station-wondong","원도심·상권","오산역·원동 생활권",
       "원동, 오산역 상권, 오산동, 부산동",
       "오산역(1호선)",
       "오산역·원동 일대는 1호선 오산역을 낀 오산의 원도심 상권 중심입니다. 오산역 상가와 원동 번화가, 인근 오피스텔·숙소가 밀집해 교통 접근성이 좋은 생활권입니다.",
       "역 인근 오피스텔·숙소는 공동현관·프런트 확인 방식이 제각각입니다. 정확한 건물명과 호수, 방문자 출입 가능 여부를 예약 전 확인합니다.",
       ["스포츠 마사지","스웨디시"]),
      ("osan-segyo","segyo-newtown","신도시·대학","세교신도시·오산대 생활권",
       "세교1·2지구, 궐동 인접, 오산대역",
       "오산대역(1호선)",
       "세교신도시는 오산대역을 낀 오산의 대표 택지지구로, 신축 대단지 아파트와 오피스텔이 이어집니다. 대학가와 신도시 상가가 함께 있어 세대·오피스텔 이용 문의가 가장 많은 생활권입니다.",
       "신도시 대단지는 방문 차량 등록과 지하주차 세대 출입이 일반적입니다. 정확한 단지·동·호수와 출입 절차를 미리 확인합니다.",
       ["스웨디시","아로마테라피"]),
      ("osan-segyo","gwoldong-unam","행정·주거","궐동·운암·오산시청 생활권",
       "궐동, 운암동, 오산시청, 원동 인접",
       "오산역 인접",
       "궐동은 대학가와 주거가 섞인 지역, 운암동은 오산시청 인접 행정·주거권입니다. 원룸·오피스텔과 아파트가 함께 있어 다양한 세대 유형의 이용 문의가 있는 생활권입니다.",
       "원룸·오피스텔은 공동현관 비밀번호, 아파트는 방문 차량 등록이 필요할 수 있습니다. 건물 유형과 출입 방법을 예약 전 확인합니다.",
       ["발마사지","스웨디시"]),

      # ── 평택·안성·이천권 ─────────────────────────────────────────
      ("pyeongtaek-anseong-icheon","pyeongtaek-jije-godeok","신도시·SRT","평택·지제·고덕 생활권",
       "평택역, 지제역, 고덕국제신도시, 세교동",
       "평택역·지제역(SRT·1호선)",
       "평택 중심권은 SRT 지제역과 고덕국제신도시, 평택역 상권이 이어지는 경기 최남단 핵심 생활권입니다. 삼성전자 평택캠퍼스 배후로 고덕신도시 아파트·오피스텔 수요가 크게 늘고 있습니다.",
       "고덕신도시 신축 단지는 방문 차량 등록·지하주차 세대 출입이 일반적이며, 역세권 오피스텔은 공동현관 확인이 필요합니다. 정확한 단지·건물명을 미리 확인합니다.",
       ["스포츠 마사지","아로마테라피"]),
      ("pyeongtaek-anseong-icheon","songtan-seojeong","상권·주거","송탄·서정리 생활권",
       "송탄, 서정동, 신장동, 지산동",
       "송탄역·서정리역(1호선)",
       "송탄·서정리는 송탄역·서정리역을 낀 평택 북부 상권 중심으로, 국제적 색채의 신장동 상권과 주거지가 자리합니다. 서정리·지제 인접 개발로 오피스텔·주거 수요가 이어지는 생활권입니다.",
       "상권 오피스텔과 주택가 빌라가 섞여 있어 출입 방식이 다양합니다. 건물명·호수와 공동현관, 주차 가능 여부를 예약 전 확인합니다.",
       ["스포츠 마사지","발마사지"]),
      ("pyeongtaek-anseong-icheon","anseong-gongdo","산단·외곽","안성·공도 생활권",
       "안성시내, 공도읍, 봉산동, 대덕",
       "자차·버스 이동",
       "안성은 안성맞춤랜드와 대학이 있는 시내 주거권, 공도읍은 대단지 아파트와 산업단지가 조성된 신흥 주거권입니다. 철도가 없어 이동 거리 확인이 중요한 외곽 생활권입니다.",
       "공도 택지 아파트와 시내 주택이 섞여 있어 정확한 주소와 이동 가능 시간 확인이 필수입니다. 방문 차량과 세대 출입 방식을 미리 확인합니다.",
       ["스포츠 마사지","타이마사지"]),
      ("pyeongtaek-anseong-icheon","icheon-bubal","산단·주거","이천·부발 생활권",
       "이천시내, 부발읍, 증포동, 하이닉스 인접",
       "이천역·부발역(경강선)",
       "이천은 경강선 이천역과 증포지구 아파트, 부발읍은 SK하이닉스 배후 주거·산단이 자리한 생활권입니다. 반도체 산단 인접으로 오피스텔·숙소 장기 이용 문의가 이어집니다.",
       "산단 인접 오피스텔·숙소는 방문자 출입과 주차 정책이 건물마다 다릅니다. 정확한 건물명과 호수, 이동 거리를 예약 전 확인합니다.",
       ["스포츠 마사지","스웨디시"]),

      # ── 안산·시흥·안양·광명권 ────────────────────────────────────
      ("ansan-siheung-anyang-gwangmyeong","ansan-jungang-gojan","상권·주거","안산중앙·고잔 생활권",
       "중앙동, 고잔동, 안산시청, 호수동",
       "중앙역·고잔역(4호선·수인분당선)",
       "안산중앙역 일대는 안산 최대 상권, 고잔·호수동은 안산시청과 화랑유원지를 낀 주거 중심 생활권입니다. 상권 오피스텔과 대단지 아파트가 함께 있어 도심·아파트 이용 문의가 많습니다.",
       "상권 오피스텔은 공동현관 확인, 아파트는 방문 차량 등록이 필요합니다. 정확한 위치와 출입 방식을 예약 전 확인합니다.",
       ["발마사지","스포츠 마사지"]),
      ("ansan-siheung-anyang-gwangmyeong","banwol-sihwa","산업단지","반월·시화산단 생활권",
       "반월산단, 시화산단, 원시동, 초지 인접",
       "원시역·초지역(서해선·4호선)",
       "반월·시화산단은 수도권 대표 산업단지로, 인근에 오피스텔·원룸·비즈니스 숙소가 밀집한 생활권입니다. 서해선 원시역 개발로 산단 배후 주거 수요가 이어집니다.",
       "산단 인접 숙소·오피스텔은 방문자 출입과 야간 출입, 주차 정책이 건물마다 다릅니다. 정확한 주소와 이동 가능 시간을 예약 전 확인합니다.",
       ["스포츠 마사지","발마사지"]),
      ("ansan-siheung-anyang-gwangmyeong","baegot-jeongwang","신도시·오피스텔","배곧·정왕 생활권",
       "배곧신도시, 정왕동, 오이도 인접",
       "정왕역·오이도역(수인분당선·4호선)",
       "배곧신도시는 서울대 시흥캠퍼스와 배곧생명공원을 낀 신흥 아파트 도시, 정왕동은 시화산단 배후 오피스텔·주거권입니다. 신도시 세대와 오피스텔 이용 문의가 함께 많은 생활권입니다.",
       "배곧 신축 단지는 방문 차량 등록과 지하주차 출입, 정왕 오피스텔은 공동현관 확인이 필요합니다. 정확한 단지·건물명을 미리 확인합니다.",
       ["아로마테라피","스포츠 마사지"]),
      ("ansan-siheung-anyang-gwangmyeong","anyang-pyeongchon-beomgye","도심·아파트","안양·평촌·범계 생활권",
       "평촌 학원가, 범계 로데오, 안양역, 인덕원 인접",
       "범계역·평촌역·안양역·인덕원역",
       "평촌신도시는 학원가와 대단지 아파트, 범계역은 로데오 상권, 안양역은 원도심 상권이 자리한 안양 대표 생활권입니다. 상권과 주거가 조밀해 도심·아파트 이용 문의가 가장 많습니다.",
       "대단지 아파트는 방문 차량 등록, 상권 오피스텔은 공동현관 확인이 필요합니다. 정확한 위치와 출입 방식을 예약 전 확인합니다.",
       ["발마사지","스웨디시"]),
      ("ansan-siheung-anyang-gwangmyeong","gwangmyeong-cheolsan","역세권·재건축","광명·철산 생활권",
       "광명역세권, 철산동, 광명사거리, 하안동",
       "광명역(KTX)·철산역(7호선)",
       "광명역세권은 KTX·복합환승과 신축 오피스텔, 철산·광명사거리는 재건축 아파트와 상권이 자리한 생활권입니다. 서울 접경 역세권으로 오피스텔·아파트 이용 문의가 꾸준합니다.",
       "역세권 오피스텔은 공동현관·방문자 등록, 재건축 대단지는 방문 차량 등록이 필요합니다. 건물명·동·호수를 예약 전 확인합니다.",
       ["아로마테라피","발마사지"]),
      ("ansan-siheung-anyang-gwangmyeong","siheung-cityhall-janghyeon","택지·신도시","시흥시청·장현 생활권",
       "장현지구, 시흥시청, 능곡동, 목감 인접",
       "시흥시청역·능곡역(서해선)",
       "시흥시청·장현지구는 서해선 시흥시청역을 낀 신흥 택지 생활권으로, 능곡·장현 대단지 아파트가 이어집니다. 목감지구까지 개발이 확장되며 세대 방문 문의가 늘고 있습니다.",
       "택지지구 신축 단지는 방문 차량 등록과 지하주차 세대 출입이 일반적입니다. 정확한 단지·동·호수와 출입 절차를 미리 확인합니다.",
       ["스웨디시","아로마테라피"]),
    ]

    LIFE_BY_AREA = {}
    for row in LIFE:
        LIFE_BY_AREA.setdefault(row[0], []).append(row)

    # -------------------------------------------------------------------
    # HOME
    # -------------------------------------------------------------------
    home_faqs = [
        ("경기남부 전 지역 방문이 가능한가요?",
         "실제 방문 주소, 가까운 생활권, 예약 가능 시간, 이동 기준을 확인한 뒤 안내합니다."),
        ("어떤 생활권을 안내하나요?",
         "수원·광교, 분당·판교, 용인·수지, 동탄·화성, 오산·세교, 평택·고덕, 안산·시흥·안양·광명 생활권을 안내합니다."),
        ("동탄과 오산은 따로 안내하나요?",
         "네. 동탄은 SRT·신도시·오피스텔 수요가 강하고, 오산은 오산역·세교신도시 중심이라 각각 별도 생활권으로 안내합니다."),
        ("호텔이나 오피스텔에서도 이용할 수 있나요?",
         "숙소 정책, 공동현관, 프런트 확인 방식, 방문자 출입 가능 여부를 먼저 확인해야 합니다."),
        ("야간 예약은 무조건 가능한가요?",
         "무조건 가능하다고 안내하지 않습니다. 주소, 이동 거리, 건물 출입, 예약 가능 시간 확인 후 안내합니다."),
        ("불법·선정적 서비스도 가능한가요?",
         "불법·선정적 서비스는 제공하거나 안내하지 않습니다. 건전한 방문형 웰니스 정보만 제공합니다."),
    ]
    area_cards = [("생활권", t, r, f"/gyeonggi-south/area/{s}/") for s, t, r in AREAS]
    prog_cards = [("프로그램", t, d, f"/gyeonggi-south/program/{s}/") for s, t, d in PROGRAMS]
    use_cards  = [("이용 장소", t, d, f"/gyeonggi-south/use/{s}/") for s, t, d in USES]

    home_body = f'''<main>
    <section class="hero">
      <div class="container">
        <span class="eyebrow">경기남부 출장마사지 · 홈타이 지역 안내</span>
        <h1>경기남부 출장마사지<br><span>수원·분당·용인·동탄</span> 생활권 안내</h1>
        <p class="lead">수원, 광교, 분당, 판교, 용인, 동탄, 오산·세교, 평택, 안산, 시흥, 안양, 광명 등 경기남부 주요 생활권과 호텔·오피스텔·자택 이용 전 확인사항을 안내합니다.</p>
        <div class="cta-row">
          <a class="btn btn--primary" href="{TEL_HREF}">📞 전화 예약 {TEL_LABEL}</a>
          <a class="btn btn--ghost" href="/gyeonggi-south/program/">마사지 프로그램</a>
          <a class="btn btn--ghost" href="/gyeonggi-south/check/">예약 전 확인</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="center">이용 코스와 요금 살펴보기</h2>
        <p class="lead center" style="margin-bottom:32px">60·90·120분 코스별 기준 요금이며, 지역·예약 시간대·이동 거리에 따라 상담 시 최종 확인됩니다.</p>
        <div class="pricing">
          <div class="price-card">
            <h3>60분 코스</h3>
            <div class="amount">90,000<small>원</small></div>
            <div class="dur">60분</div>
            <p class="desc">기본 컨디션·릴렉스 케어</p>
            <a class="btn btn--ghost btn--block" href="{TEL_HREF}">예약 문의</a>
          </div>
          <div class="price-card price-card--featured">
            <div class="price-card__badge">추천</div>
            <h3>90분 코스</h3>
            <div class="amount">150,000<small>원</small></div>
            <div class="dur">90분</div>
            <p class="desc">아로마 포함 추천 구성</p>
            <a class="btn btn--primary btn--block" href="{TEL_HREF}">예약 문의</a>
          </div>
          <div class="price-card">
            <h3>120분 코스</h3>
            <div class="amount">180,000<small>원</small></div>
            <div class="dur">120분</div>
            <p class="desc">전신 집중 프리미엄 케어</p>
            <a class="btn btn--ghost btn--block" href="{TEL_HREF}">예약 문의</a>
          </div>
        </div>
        <p class="center small muted" style="margin-top:18px">지역·예약 시간대·이동 거리에 따라 상담 시 최종 확인됩니다. <a href="/gyeonggi-south/check/" style="color:var(--brand-orange-soft)">상세 요금·확인 안내 보기 →</a></p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <span class="eyebrow">생활권 안내</span>
        <h2>경기남부는 도시보다 생활권 확인이 중요합니다</h2>
        <p class="lead">경기남부는 수원, 성남, 용인, 화성, 평택처럼 도시 단위가 크고, 같은 도시 안에서도 광교·영통, 판교·정자, 동탄·병점, 오산·세교, 고덕·배곧처럼 이용 기준이 달라집니다. 도시명뿐 아니라 생활권, 역세권, 신도시, 산업단지, 숙소 유형을 함께 안내합니다.</p>
        <div style="margin-top:24px">{cards(3, area_cards)}</div>
      </div>
    </section>

    <section class="section" style="background:var(--bg-elevated)">
      <div class="container">
        <span class="eyebrow">프로그램</span>
        <h2>마사지 프로그램 안내</h2>
        <p class="lead">스웨디시·타이·아로마·스포츠·발마사지 등 프로그램별 특징과 숙소·오피스텔·자택 이용 기준을 함께 안내합니다.</p>
        <div style="margin-top:24px">{cards(3, prog_cards)}</div>
        <p style="margin-top:16px"><a class="btn btn--ghost" href="/gyeonggi-south/program/">프로그램 전체 보기 →</a></p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <span class="eyebrow">이용 장소</span>
        <h2>이용 장소별 확인 기준</h2>
        <p class="lead">자택, 호텔·숙소, 오피스텔, 아파트 단지 등 이용 장소에 따라 출입·예약 확인 기준이 다릅니다.</p>
        <div style="margin-top:24px">{cards(4, use_cards)}</div>
      </div>
    </section>

    <section class="section section--tight">
      <div class="container">{NOTICE}</div>
    </section>

    {whw_block(
      "이 콘텐츠는 경기남부 지역 방문형 웰니스 서비스 이용 전, 위치·건물 출입·숙소 정책·예약 기준을 확인할 수 있도록 작성되었습니다.",
      "경기남부 주요 도시와 생활권 구조, 실제 예약 전 확인 항목, 개인정보 처리 기준을 바탕으로 작성하며 최종 문구는 사람이 검수합니다.",
      "검색 순위 조작이 아니라, 자택·호텔·오피스텔·업무지구·산업단지 인접 숙소 이용 전 필요한 확인사항을 이해하기 쉽게 안내하는 것이 목적입니다.")}

    {faq_block(home_faqs)}
  </main>'''

    write("/", page(
        "/",
        "경기남부 출장마사지｜수원·분당·용인·동탄·오산·평택 홈타이 안내 - 간다GO",
        "간다GO 경기남부 출장마사지·홈타이. 수원·분당·용인·동탄·오산·평택 생활권 이용 안내. 예약 0508-202-4719",
        home_body,
        trail=[("홈", "/")],
        faqs=home_faqs,
    ))

    # -------------------------------------------------------------------
    # AREA index
    # -------------------------------------------------------------------
    write("/gyeonggi-south/area/", page(
        "/gyeonggi-south/area/",
        "경기남부 7대 생활권 안내｜수원·분당·용인·동탄·오산·평택·안산 - 간다GO",
        "경기남부 7대 생활권 안내. 수원·분당·용인·동탄·오산·평택·안산 생활권별 이용 기준 안내. 간다GO",
        f'''<main>
    <section class="section">
      <div class="container">
        <div class="breadcrumb">{g["breadcrumb_html"]([("홈","/"),("경기남부 생활권","/gyeonggi-south/area/")])}</div>
        <h1>경기남부 7대 생활권 안내</h1>
        <p class="lead">경기남부는 생활권 단위로 이용 기준이 달라집니다. 아래 7대 생활권에서 가까운 지역을 선택해 확인하세요.</p>
        <div style="margin-top:26px">{cards(2, [("생활권", t, r, f"/gyeonggi-south/area/{s}/") for s, t, r in AREAS])}</div>
      </div>
    </section>
    <section class="section section--tight"><div class="container">{NOTICE}</div></section>
  </main>''',
        trail=[("홈","/"),("경기남부 생활권","/gyeonggi-south/area/")],
    ))

    # -------------------------------------------------------------------
    # AREA detail pages
    # -------------------------------------------------------------------
    AREA_CONTENT = {
        "suwon-gwanggyo-yeongtong": dict(
            title="경기남부 핵심 도시 수원",
            intro="수원은 경기남부 핵심 도시입니다. 광교·영통은 신도시·아파트·오피스텔 중심, 인계동은 상권과 숙소, 수원역은 교통·호텔·오피스텔 중심으로 이용 기준을 확인합니다.",
            prog=["스웨디시","아로마테라피"],
            station="수원역, 수원시청역, 광교중앙역, 영통역",
            desc="수원 출장마사지·홈타이. 광교·영통·인계동·수원역 생활권 이용 기준 안내. 간다GO",
            seo="수원 출장마사지｜광교·영통·인계동·수원역 홈타이 안내 - 간다GO"),
        "seongnam-bundang-pangyo": dict(
            title="IT 업무지구와 신도시, 성남·분당·판교",
            intro="판교는 IT 업무지구·오피스텔·테크노밸리 중심, 분당은 정자·수내·서현·야탑 같은 주거·상권 중심입니다. 업무지구와 주거 생활권을 구분해 이용 기준을 확인합니다.",
            prog=["스포츠 마사지","아로마테라피"],
            station="판교역, 정자역, 서현역, 야탑역, 모란역",
            desc="분당·판교 출장마사지·홈타이. 정자·수내·서현·야탑 생활권 이용 기준 안내. 간다GO",
            seo="분당·판교 출장마사지｜정자·수내·서현·야탑 홈타이 안내 - 간다GO"),
        "yongin-suji-giheung": dict(
            title="넓은 생활권, 용인·수지·기흥",
            intro="용인은 넓어 수지·죽전, 기흥·신갈, 동백·보정, 처인 외곽으로 나눠 확인합니다. 아파트·자택·오피스텔·외곽 이동 기준을 중심으로 안내합니다.",
            prog=["타이마사지","스웨디시"],
            station="죽전역, 기흥역, 신갈역",
            desc="용인·수지 출장마사지·홈타이. 죽전·기흥·신갈·동백 생활권 이용 기준 안내. 간다GO",
            seo="용인·수지 출장마사지｜죽전·기흥·신갈·동백 홈타이 안내 - 간다GO"),
        "dongtan-hwaseong": dict(
            title="SRT·신도시 수요, 동탄·화성",
            intro="동탄은 SRT·신도시·오피스텔·아파트 검색 수요가 강합니다. 화성은 향남·봉담·산단 중심으로, 신도시 생활권과 산업단지 인접 숙소 기준을 구분해 안내합니다.",
            prog=["아로마테라피","스포츠 마사지"],
            station="동탄역(SRT), 병점역",
            desc="동탄·화성 출장마사지·홈타이. 동탄신도시·병점·향남 생활권 이용 기준 안내. 간다GO",
            seo="동탄·화성 출장마사지｜동탄신도시·SRT·병점·향남 홈타이 안내 - 간다GO"),
        "osan-segyo": dict(
            title="동탄·평택 사이 핵심 생활권, 오산·세교",
            intro="오산은 동탄·평택 사이에 있는 경기남부 핵심 생활권입니다. 오산역 주변은 교통·숙소·상권, 세교는 신도시·아파트·오피스텔, 궐동·원동은 주거지와 상권, 오산대역은 대학가·역세권 중심으로 확인합니다.",
            prog=["스포츠 마사지","스웨디시"],
            station="오산역, 오산대역, 세마역",
            desc="오산·세교 출장마사지·홈타이. 오산역·세교신도시·궐동·원동 이용 기준 안내. 간다GO",
            seo="오산 출장마사지｜오산역·세교·궐동·원동 홈타이 지역 안내 - 간다GO"),
        "pyeongtaek-anseong-icheon": dict(
            title="SRT 지제·고덕신도시, 평택·안성·이천",
            intro="평택은 SRT 지제, 고덕신도시, 송탄, 장기 출장 숙소 수요가 있습니다. 안성·이천은 산업단지·물류·외곽 이동 기준을 중심으로 안내합니다.",
            prog=["스포츠 마사지","발마사지"],
            station="평택역, 지제역(SRT), 송탄역",
            desc="평택·고덕 출장마사지·홈타이. 지제·고덕신도시·송탄·안성 이용 기준 안내. 간다GO",
            seo="평택·고덕 출장마사지｜지제·고덕신도시·송탄 홈타이 안내 - 간다GO"),
        "ansan-siheung-anyang-gwangmyeong": dict(
            title="서남부 생활권, 안산·시흥·안양·광명",
            intro="서남부 생활권입니다. 안산·시흥은 산업단지와 해안 숙소, 안양·광명은 서울 접경·역세권·오피스텔·아파트 기준으로 나눠 확인합니다.",
            prog=["발마사지","스포츠 마사지"],
            station="안산중앙역, 정왕역, 안양역, 범계역, 광명역, 철산역",
            desc="안산·시흥·안양·광명 출장마사지·홈타이. 배곧·평촌·범계·철산 이용 안내. 간다GO",
            seo="안산·시흥·안양·광명 출장마사지｜배곧·평촌·범계·철산 안내 - 간다GO"),
    }

    for slug, title, region in AREAS:
        c = AREA_CONTENT[slug]
        url = f"/gyeonggi-south/area/{slug}/"
        area_faqs = [
            ("이 생활권 전 지역 방문이 가능한가요?",
             "실제 방문 주소, 가까운 생활권, 예약 가능 시간, 이동 기준을 확인한 뒤 안내합니다."),
            ("호텔·오피스텔에서도 이용할 수 있나요?",
             "숙소 정책, 공동현관, 프런트 확인, 방문자 출입 가능 여부를 먼저 확인해야 합니다."),
            ("야간 예약은 무조건 가능한가요?",
             "무조건 가능하다고 안내하지 않습니다. 주소·이동 거리·건물 출입·예약 가능 시간 확인 후 안내합니다."),
        ]
        prog_links = " · ".join(
            f'<a href="/gyeonggi-south/program/{s}/" style="color:var(--brand-orange-soft)">{esc(t)}</a>'
            for s, t, _ in PROGRAMS if t in c["prog"])
        rel = related_areas(exclude=slug)
        life_rows = LIFE_BY_AREA.get(slug, [])
        life_cards_list = [(tag, ltitle, covers, f"/gyeonggi-south/life/{lslug}/")
                           for (a, lslug, tag, ltitle, covers, st, ch, sty, pr) in life_rows]
        life_section = (f'''
    <section class="section">
      <div class="container">
        <span class="eyebrow">세부 생활권</span>
        <h2>{esc(title)} 세부 생활권 안내</h2>
        <p class="lead">아래 생활권별로 역세권·신도시·상권·숙소 유형에 맞춘 고유 이용 기준을 확인하세요.</p>
        <div style="margin-top:24px">{cards(3, life_cards_list)}</div>
      </div>
    </section>''' if life_cards_list else "")
        body = f'''<main>
    <section class="section">
      <div class="container">
        <div class="breadcrumb">{g["breadcrumb_html"]([("홈","/"),("경기남부 생활권","/gyeonggi-south/area/"),(title,url)])}</div>
        <span class="eyebrow">{esc(region)}</span>
        <h1>{esc(title)}</h1>
        <p class="lead">{esc(c["intro"])}</p>
        <div class="cta-row" style="margin-top:20px">
          <a class="btn btn--primary" href="{TEL_HREF}">📞 전화 예약 {TEL_LABEL}</a>
          <a class="btn btn--ghost" href="/gyeonggi-south/check/">예약 전 확인</a>
        </div>
      </div>
    </section>

    <section class="section section--tight">
      <div class="container prose">
        <h2>이 지역의 생활권 특징</h2>
        <p>{esc(c["intro"])} 같은 지역 안에서도 아파트 단지, 오피스텔, 상권, 역세권에 따라 방문 주소와 출입 방식이 다르므로, 예약 전에 정확한 위치와 건물 출입 기준을 확인하는 것이 중요합니다.</p>

        <h2>가까운 역세권과 이동 기준</h2>
        <p>대표 역세권은 {esc(c["station"])} 등이 있습니다. 역·터미널 인접 숙소는 이동 거리와 예약 시간대에 따라 방문 가능 여부가 달라지므로, 정확한 주소와 가까운 생활권을 함께 확인합니다.</p>

        <h2>호텔·오피스텔·자택 이용 전 확인</h2>
        <p>호텔·숙소는 프런트 확인과 방문자 출입 정책, 오피스텔은 공동현관과 관리규정, 아파트·자택은 단지 출입과 동·호수 확인이 필요합니다. 자세한 내용은 <a href="/gyeonggi-south/use/">이용 장소 안내</a>에서 확인하세요.</p>

        <h2>마사지 프로그램 선택 기준</h2>
        <p>이 생활권에서는 {prog_links} 등이 자주 문의됩니다. 압 강도, 오일 사용 여부, 공간 확보 조건에 따라 프로그램을 선택하고, 자세한 특징은 <a href="/gyeonggi-south/program/">프로그램 안내</a>에서 확인하세요.</p>

        <h2>예약 전 체크리스트</h2>
        <ul>
          <li>정확한 도로명 주소와 상세 위치, 가까운 생활권</li>
          <li>건물 출입 방식(공동현관·프런트·엘리베이터)</li>
          <li>예약 가능 시간과 이동 거리</li>
          <li>예약 변경·취소 기준</li>
        </ul>
        {NOTICE}
      </div>
    </section>
    {life_section}

    {faq_block(area_faqs)}

    <section class="section section--tight">
      <div class="container">
        <h2>관련 지역 보기</h2>
        <div style="margin-top:16px">{cards(3, rel)}</div>
      </div>
    </section>
  </main>'''
        write(url, page(url, c["seo"], c["desc"], body,
                        trail=[("홈","/"),("경기남부 생활권","/gyeonggi-south/area/"),(title,url)],
                        faqs=area_faqs))

    # -------------------------------------------------------------------
    # LIFE detail pages — 세부 생활권 고유 콘텐츠
    # -------------------------------------------------------------------
    AREA_TITLE = {s: t for s, t, r in AREAS}
    PROG_SLUG = {t: s for s, t, d in PROGRAMS}
    for (a, lslug, tag, ltitle, covers, stations, char, stay, prog) in LIFE:
        lurl = f"/gyeonggi-south/life/{lslug}/"
        area_title = AREA_TITLE[a]
        area_url = f"/gyeonggi-south/area/{a}/"
        prog_links = " · ".join(
            f'<a href="/gyeonggi-south/program/{PROG_SLUG[t]}/" style="color:var(--brand-orange-soft)">{esc(t)}</a>'
            for t in prog if t in PROG_SLUG)
        # sibling life pages in same area (related internal links)
        siblings = [(t2, lt2, cov2, f"/gyeonggi-south/life/{ls2}/")
                    for (a2, ls2, t2, lt2, cov2, s2, c2, st2, p2) in LIFE
                    if a2 == a and ls2 != lslug][:3]
        lfaqs = [
            (f"{ltitle}은 어떤 지역을 포함하나요?",
             f"{covers} 일대를 포함하며, 정확한 방문 주소와 가까운 위치를 확인한 뒤 안내합니다."),
            ("호텔·오피스텔·자택 모두 가능한가요?",
             "숙소 정책, 공동현관, 방문자 출입, 세대 출입 방식을 예약 전 확인한 뒤 안내합니다."),
            ("야간 예약은 무조건 가능한가요?",
             "무조건 가능하다고 안내하지 않습니다. 주소·건물 출입·이동 거리·예약 가능 시간 확인 후 안내합니다."),
        ]
        seo = f"{ltitle} 출장마사지·홈타이 이용 안내 - 간다GO"
        desc = f"{ltitle} 출장마사지·홈타이 이용 기준과 예약 전 확인사항 안내 - 간다GO"
        lbody = f'''<main>
    <section class="section">
      <div class="container">
        <div class="breadcrumb">{g["breadcrumb_html"]([("홈","/"),("경기남부 생활권","/gyeonggi-south/area/"),(area_title,area_url),(ltitle,lurl)])}</div>
        <span class="eyebrow">{esc(tag)} · {esc(covers)}</span>
        <h1>{esc(ltitle)}</h1>
        <p class="lead">{esc(char)}</p>
        <div class="cta-row" style="margin-top:20px">
          <a class="btn btn--primary" href="{TEL_HREF}">📞 전화 예약 {TEL_LABEL}</a>
          <a class="btn btn--ghost" href="{area_url}">{esc(area_title)} 전체 보기</a>
        </div>
      </div>
    </section>
    <section class="section section--tight">
      <div class="container prose">
        <h2>{esc(ltitle)} 특징</h2>
        <p>{esc(char)}</p>
        <h2>가까운 역세권과 이동 기준</h2>
        <p>대표 교통은 {esc(stations)}입니다. 역·터미널 인접 여부와 이동 거리, 예약 시간대에 따라 방문 가능 여부가 달라지므로 정확한 주소와 가까운 위치를 함께 확인합니다.</p>
        <h2>숙소·오피스텔·자택 이용 전 확인</h2>
        <p>{esc(stay)} 이용 장소별 상세 기준은 <a href="/gyeonggi-south/use/">이용 장소 안내</a>에서 확인할 수 있습니다.</p>
        <h2>추천 마사지 프로그램</h2>
        <p>이 생활권에서는 {prog_links} 문의가 많습니다. 압 강도와 오일 사용 여부, 공간 확보 조건에 맞춰 선택하고 자세한 특징은 <a href="/gyeonggi-south/program/">프로그램 안내</a>에서 확인하세요.</p>
        <h2>예약 전 체크리스트</h2>
        <ul>
          <li>정확한 도로명 주소와 상세 위치({esc(covers)})</li>
          <li>건물 출입 방식(공동현관·프런트·방문 차량 등록)</li>
          <li>예약 가능 시간과 이동 거리, 예약 변경 기준</li>
        </ul>
        {NOTICE}
      </div>
    </section>
    {faq_block(lfaqs)}
    <section class="section section--tight">
      <div class="container">
        <h2>같은 지역 다른 생활권</h2>
        <div style="margin-top:16px">{cards(3, siblings)}</div>
      </div>
    </section>
  </main>'''
        write(lurl, page(lurl, seo, desc, lbody,
                         trail=[("홈","/"),("경기남부 생활권","/gyeonggi-south/area/"),(area_title,area_url),(ltitle,lurl)],
                         faqs=lfaqs))

    # -------------------------------------------------------------------
    # OSAN city page (emphasized) — Service schema (used cautiously)
    # -------------------------------------------------------------------
    osan_url = "/gyeonggi-south/osan-si/"
    osan_faqs = [
        ("오산은 어떤 생활권으로 나뉘나요?",
         "오산역·원동 상권, 세교신도시, 궐동·운암 주거권, 오산대역 대학가로 나눠 안내합니다."),
        ("세교신도시도 방문 가능한가요?",
         "세교는 아파트·오피스텔 중심 생활권으로, 공동현관·주차·세대 출입 기준을 확인한 뒤 안내합니다."),
        ("오산 야간 예약은 무조건 가능한가요?",
         "무조건 가능하다고 안내하지 않습니다. 주소·건물 출입·이동 가능 시간·예약 변경 기준을 확인 후 안내합니다."),
    ]
    osan_body = f'''<main>
    <section class="section">
      <div class="container">
        <div class="breadcrumb">{g["breadcrumb_html"]([("홈","/"),("경기남부 생활권","/gyeonggi-south/area/"),("오산·세교","/gyeonggi-south/area/osan-segyo/"),("오산시",osan_url)])}</div>
        <span class="eyebrow">오산역 · 세교 · 궐동 · 원동 · 운암</span>
        <h1>오산 출장마사지 · 오산역·세교 생활권 안내</h1>
        <p class="lead">오산 출장마사지·홈타이 예약 전 오산역, 세교, 궐동, 원동, 운암, 오산대역, 오산시청 인근 생활권과 호텔·오피스텔·자택 이용 기준을 안내합니다.</p>
        <div class="cta-row" style="margin-top:20px">
          <a class="btn btn--primary" href="{TEL_HREF}">📞 전화 예약 {TEL_LABEL}</a>
          <a class="btn btn--ghost" href="/gyeonggi-south/area/osan-segyo/">오산·세교권 보기</a>
        </div>
      </div>
    </section>
    <section class="section section--tight">
      <div class="container prose">
        <h2>오산 생활권 특징</h2>
        <p>오산은 동탄·평택 사이에 있는 경기남부 핵심 생활권입니다. <strong>오산역</strong> 주변은 교통·숙소·상권 중심, <strong>세교신도시</strong>는 아파트·오피스텔 중심, <strong>궐동·원동</strong>은 주거지와 상권, <strong>오산대역</strong>은 대학가·역세권 중심으로 이용 기준이 다릅니다.</p>
        <h2>오산역·원동 상권</h2>
        <p>오산역과 원동 상권은 교통 접근성이 좋아 숙소·오피스텔 이용 문의가 많습니다. 프런트 확인과 방문자 출입 정책을 먼저 확인합니다.</p>
        <h2>세교신도시</h2>
        <p>세교는 오산에서 반드시 따로 확인하는 생활권입니다. 아파트 단지 출입, 오피스텔 공동현관, 주차, 자택 세대 출입 기준을 확인합니다.</p>
        <h2>궐동·운암·오산시청</h2>
        <p>궐동·운암은 오산시청 인접 주거·행정 생활권으로 아파트·빌라·자택 방문 기준을 확인합니다.</p>
        <h2>예약 전 체크리스트</h2>
        <ul>
          <li>정확한 도로명 주소와 가까운 생활권(오산역·세교·궐동·오산대)</li>
          <li>건물 출입 방식과 예약 가능 시간</li>
          <li>이동 거리와 예약 변경 기준</li>
        </ul>
        {NOTICE}
      </div>
    </section>
    {faq_block(osan_faqs)}
    <section class="section section--tight">
      <div class="container">
        <h2>관련 지역 보기</h2>
        <div style="margin-top:16px">{cards(3, related_areas(exclude="osan-segyo"))}</div>
      </div>
    </section>
  </main>'''
    write(osan_url, page(
        osan_url,
        "오산 출장마사지｜오산역·세교·궐동·원동 홈타이 지역 안내 - 간다GO",
        "오산 출장마사지·홈타이. 오산역·세교신도시·궐동·원동·오산대역 생활권 이용 안내. 간다GO",
        osan_body,
        trail=[("홈","/"),("경기남부 생활권","/gyeonggi-south/area/"),("오산·세교","/gyeonggi-south/area/osan-segyo/"),("오산시",osan_url)],
        faqs=osan_faqs))

    # -------------------------------------------------------------------
    # PROGRAM index + detail
    # -------------------------------------------------------------------
    write("/gyeonggi-south/program/", page(
        "/gyeonggi-south/program/",
        "경기남부 마사지 프로그램 안내｜스웨디시·타이·아로마·스포츠·발 - 간다GO",
        "경기남부 마사지 프로그램 안내. 스웨디시·타이·아로마·스포츠·발마사지 특징과 이용 기준. 간다GO",
        f'''<main>
    <section class="section">
      <div class="container">
        <div class="breadcrumb">{g["breadcrumb_html"]([("홈","/"),("프로그램","/gyeonggi-south/program/")])}</div>
        <h1>마사지 프로그램 안내</h1>
        <p class="lead">프로그램별 특징과 압 강도, 오일 사용 여부, 숙소·오피스텔·자택 이용 기준을 함께 안내합니다.</p>
        <div style="margin-top:26px">{cards(3, [("프로그램", t, d, f"/gyeonggi-south/program/{s}/") for s, t, d in PROGRAMS])}</div>
      </div>
    </section>
    <section class="section section--tight"><div class="container">{NOTICE}</div></section>
  </main>''',
        trail=[("홈","/"),("프로그램","/gyeonggi-south/program/")]))

    PROGRAM_BODY = {
        "swedish": "부드러운 압과 오일을 사용한 전신 릴렉스 관리입니다. 오일 사용 여부, 수건 준비, 숙소·오피스텔 이용 전 확인사항을 안내합니다.",
        "thai-massage": "스트레칭 중심의 타이마사지입니다. 공간 확보, 복장, 자택·아파트 이용 기준을 확인합니다.",
        "aroma-therapy": "향과 피부 민감도를 확인한 뒤 진행하는 아로마 오일 관리입니다. 호텔·오피스텔 이용 기준을 안내합니다.",
        "sports-massage": "운동 후 부위별 압을 조절하는 관리입니다. 무리한 압을 지양하며 컨디션에 맞춰 진행합니다.",
        "foot-massage": "발·종아리를 집중 관리합니다. 장시간 보행·여행객 이용자에게 적합하며 이용 기준을 안내합니다.",
    }
    for slug, title, short in PROGRAMS:
        url = f"/gyeonggi-south/program/{slug}/"
        pf = [
            ("어느 지역에서 이용할 수 있나요?",
             "경기남부 수원·분당·용인·동탄·오산·평택·안산 등 주요 생활권에서 이용 기준을 확인 후 안내합니다."),
            ("숙소·오피스텔에서도 가능한가요?",
             "숙소 정책과 공동현관, 방문자 출입 가능 여부를 먼저 확인해야 합니다."),
        ]
        related_prog = [("프로그램", t, d, f"/gyeonggi-south/program/{s}/")
                        for s, t, d in PROGRAMS if s != slug][:3]
        body = f'''<main>
    <section class="section">
      <div class="container">
        <div class="breadcrumb">{g["breadcrumb_html"]([("홈","/"),("프로그램","/gyeonggi-south/program/"),(title,url)])}</div>
        <span class="eyebrow">마사지 프로그램</span>
        <h1>{esc(title)}</h1>
        <p class="lead">{esc(short)}</p>
        <div class="cta-row" style="margin-top:20px">
          <a class="btn btn--primary" href="{TEL_HREF}">📞 전화 예약 {TEL_LABEL}</a>
        </div>
      </div>
    </section>
    <section class="section section--tight">
      <div class="container prose">
        <h2>{esc(title)} 특징</h2>
        <p>{esc(PROGRAM_BODY[slug])}</p>
        <h2>이용 전 확인사항</h2>
        <ul>
          <li>이용 장소 유형(자택·호텔·오피스텔·아파트)과 출입 방식</li>
          <li>공간 확보와 준비물, 압 강도 선호</li>
          <li>예약 가능 시간과 이동 거리</li>
        </ul>
        <p>이용 장소별 기준은 <a href="/gyeonggi-south/use/">이용 장소 안내</a>, 예약 전 확인은 <a href="/gyeonggi-south/check/">예약 전 확인사항</a>에서 볼 수 있습니다.</p>
        {NOTICE}
      </div>
    </section>
    {faq_block(pf)}
    <section class="section section--tight">
      <div class="container"><h2>다른 프로그램 보기</h2>
      <div style="margin-top:16px">{cards(3, related_prog)}</div></div>
    </section>
  </main>'''
        write(url, page(
            url,
            f"경기남부 {title} 출장마사지·홈타이 이용 안내 - 간다GO",
            f"경기남부 {title} 출장마사지·홈타이. 특징과 숙소·오피스텔·자택 이용 기준 안내. 간다GO",
            body,
            trail=[("홈","/"),("프로그램","/gyeonggi-south/program/"),(title,url)],
            faqs=pf))

    # -------------------------------------------------------------------
    # USE index + detail
    # -------------------------------------------------------------------
    write("/gyeonggi-south/use/", page(
        "/gyeonggi-south/use/",
        "경기남부 이용 장소 안내｜자택·호텔·오피스텔·아파트 확인 기준 - 간다GO",
        "경기남부 이용 장소 안내. 자택·호텔·오피스텔·아파트 출입과 예약 확인 기준 안내. 간다GO",
        f'''<main>
    <section class="section">
      <div class="container">
        <div class="breadcrumb">{g["breadcrumb_html"]([("홈","/"),("이용 장소","/gyeonggi-south/use/")])}</div>
        <h1>이용 장소별 확인 기준</h1>
        <p class="lead">이용 장소에 따라 출입·예약 확인 기준이 다릅니다. 아래에서 이용 장소를 선택해 확인하세요.</p>
        <div style="margin-top:26px">{cards(2, [("이용 장소", t, d, f"/gyeonggi-south/use/{s}/") for s, t, d in USES])}</div>
      </div>
    </section>
    <section class="section section--tight"><div class="container">{NOTICE}</div></section>
  </main>''',
        trail=[("홈","/"),("이용 장소","/gyeonggi-south/use/")]))

    USE_BODY = {
        "home": "아파트·자택 방문은 정확한 도로명 주소, 단지·세대 출입 방식, 주차 가능 여부를 예약 전 확인합니다. 공동현관 비밀번호나 출입 방법을 미리 안내받으면 원활합니다.",
        "hotel": "호텔·숙소 이용은 숙소 정책, 프런트 확인, 방문자 출입 가능 여부를 먼저 확인합니다. 숙소에 따라 방문자 등록이 필요할 수 있습니다.",
        "officetel": "오피스텔은 공동현관, 관리규정, 방문자 등록 방식을 예약 전 확인합니다. 건물별 출입 절차가 다르므로 정확한 동·호수를 확인합니다.",
        "apartment": "아파트 단지는 단지 출입, 동·호수 확인, 방문 차량 기준을 안내합니다. 방문 차량 등록이 필요한 단지는 미리 확인합니다.",
    }
    for slug, title, short in USES:
        url = f"/gyeonggi-south/use/{slug}/"
        uf = [
            ("어떤 지역에서 이용할 수 있나요?",
             "경기남부 수원·분당·용인·동탄·오산·평택·안산 등 주요 생활권에서 이용 기준을 확인 후 안내합니다."),
            ("방문 전에 무엇을 준비해야 하나요?",
             "정확한 주소, 건물 출입 방식, 예약 가능 시간을 미리 확인해 주시면 원활합니다."),
        ]
        body = f'''<main>
    <section class="section">
      <div class="container">
        <div class="breadcrumb">{g["breadcrumb_html"]([("홈","/"),("이용 장소","/gyeonggi-south/use/"),(title,url)])}</div>
        <span class="eyebrow">이용 장소 안내</span>
        <h1>경기남부 {esc(title)} 출장마사지 이용 기준</h1>
        <p class="lead">{esc(short)}</p>
      </div>
    </section>
    <section class="section section--tight">
      <div class="container prose">
        <h2>{esc(title)} 이용 전 확인사항</h2>
        <p>{esc(USE_BODY[slug])}</p>
        <ul>
          <li>정확한 도로명 주소와 상세 위치</li>
          <li>건물·세대 출입 방식</li>
          <li>예약 가능 시간과 이동 거리</li>
        </ul>
        <p>예약 전 전체 확인사항은 <a href="/gyeonggi-south/check/">예약 전 확인</a>에서 볼 수 있습니다.</p>
        {NOTICE}
      </div>
    </section>
    {faq_block(uf)}
  </main>'''
        write(url, page(
            url,
            f"경기남부 {title} 출장마사지 이용 기준 안내 - 간다GO",
            f"경기남부 {title} 출장마사지 이용 기준. 출입·예약·방문 확인사항 안내. 간다GO",
            body,
            trail=[("홈","/"),("이용 장소","/gyeonggi-south/use/"),(title,url)],
            faqs=uf))

    # -------------------------------------------------------------------
    # CHECK page
    # -------------------------------------------------------------------
    check_faqs = [
        ("예약할 때 무엇을 먼저 확인하나요?",
         "정확한 방문 주소, 건물 출입 방식, 예약 가능 시간, 이동 거리를 먼저 확인합니다."),
        ("개인정보는 어떻게 처리하나요?",
         "예약에 필요한 최소 정보만 받고, 목적 달성 후 안전하게 파기합니다."),
        ("야간 예약도 되나요?",
         "무조건 가능하다고 안내하지 않습니다. 주소·건물 출입·이동 시간·예약 변경 기준 확인 후 안내합니다."),
    ]
    check_cards = "\n        ".join(
        f'<div class="card"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for t, d in CHECKS)
    write("/gyeonggi-south/check/", page(
        "/gyeonggi-south/check/",
        "경기남부 출장마사지 예약 전 확인사항｜주소·출입·시간 안내 - 간다GO",
        "경기남부 출장마사지 예약 전 확인. 주소·건물 출입·예약 시간·개인정보 처리 안내. 간다GO",
        f'''<main>
    <section class="section">
      <div class="container">
        <div class="breadcrumb">{g["breadcrumb_html"]([("홈","/"),("예약 전 확인","/gyeonggi-south/check/")])}</div>
        <h1>예약 전 확인사항</h1>
        <p class="lead">방문 가능 여부는 실제 주소와 예약 조건 확인 후 안내합니다. 아래 항목을 예약 전에 확인해 주세요.</p>
        <div class="grid grid--3" style="margin-top:26px">
        {check_cards}
        </div>
      </div>
    </section>
    <section class="section section--tight"><div class="container">{NOTICE}</div></section>
    {faq_block(check_faqs)}
  </main>''',
        trail=[("홈","/"),("예약 전 확인","/gyeonggi-south/check/")],
        faqs=check_faqs))

    # -------------------------------------------------------------------
    # CONTACT
    # -------------------------------------------------------------------
    write("/contact/", page(
        "/contact/",
        "문의하기｜간다GO 경기남부 출장마사지 전화·제휴·제작 문의",
        "간다GO 문의하기. 전화예약 0508-202-4719, 웹사이트 제작문의·제휴문의는 텔레그램으로 안내.",
        f'''<main>
    <section class="section">
      <div class="container">
        <div class="breadcrumb">{g["breadcrumb_html"]([("홈","/"),("문의하기","/contact/")])}</div>
        <h1>문의하기</h1>
        <p class="lead">예약·이용 문의는 전화로, 웹사이트 제작·제휴 문의는 텔레그램으로 안내드립니다.</p>
        <div class="grid grid--2" style="margin-top:24px">
          <div class="card">
            <span class="tag">전화 예약</span>
            <h3>{TEL_LABEL}</h3>
            <p>상호: 간다GO · 경기남부 출장마사지 지역 안내</p>
            <a class="btn btn--primary" style="margin-top:14px" href="{TEL_HREF}">📞 전화 걸기</a>
          </div>
          <div class="card">
            <span class="tag">제휴 · 제작</span>
            <h3>텔레그램 문의</h3>
            <p>웹사이트 제작문의 · 제휴문의를 받습니다.</p>
            <div class="cta-row" style="margin-top:14px">
              <a class="btn btn--orange" href="{g["TELEGRAM_BUILD"]}" target="_blank" rel="noopener nofollow">💬 웹사이트 제작문의</a>
              <a class="btn btn--orange" href="{g["TELEGRAM_PARTNER"]}" target="_blank" rel="noopener nofollow">🤝 제휴문의</a>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="section section--tight"><div class="container">{NOTICE}</div></section>
  </main>''',
        trail=[("홈","/"),("문의하기","/contact/")]))

    # -------------------------------------------------------------------
    # PRIVACY
    # -------------------------------------------------------------------
    write("/privacy/", page(
        "/privacy/",
        "개인정보 처리방침｜간다GO 경기남부 출장마사지",
        "간다GO 개인정보 처리방침. 예약에 필요한 최소 정보만 수집·이용하고 목적 달성 후 파기.",
        f'''<main>
    <section class="section">
      <div class="container prose">
        <div class="breadcrumb">{g["breadcrumb_html"]([("홈","/"),("개인정보 처리방침","/privacy/")])}</div>
        <h1>개인정보 처리방침</h1>
        <h2>1. 수집 항목 및 목적</h2>
        <p>예약 상담에 필요한 최소한의 정보(연락처, 방문 지역·주소, 예약 희망 시간)만 수집하며, 예약 확인과 방문 안내 목적으로만 이용합니다.</p>
        <h2>2. 보유 및 파기</h2>
        <p>수집한 정보는 예약 목적 달성 후 지체 없이 안전하게 파기합니다. 별도의 마케팅 목적으로 보관하지 않습니다.</p>
        <h2>3. 제3자 제공</h2>
        <p>법령에 따른 경우를 제외하고 이용자의 동의 없이 개인정보를 제3자에게 제공하지 않습니다.</p>
        <h2>4. 이용자 권리</h2>
        <p>이용자는 본인의 개인정보에 대해 열람·정정·삭제를 요청할 수 있으며, 요청 시 지체 없이 처리합니다.</p>
        <p>문의: <a class="tel-strong" href="{TEL_HREF}">{TEL_LABEL}</a></p>
      </div>
    </section>
  </main>''',
        trail=[("홈","/"),("개인정보 처리방침","/privacy/")]))

    # -------------------------------------------------------------------
    # NOTICE (illegal service policy)
    # -------------------------------------------------------------------
    write("/notice/", page(
        "/notice/",
        "불법·선정적 서비스 불가 안내｜간다GO 경기남부 출장마사지",
        "간다GO는 불법·선정적 서비스를 제공하거나 안내하지 않습니다. 건전한 웰니스 정보 안내 목적.",
        f'''<main>
    <section class="section">
      <div class="container prose">
        <div class="breadcrumb">{g["breadcrumb_html"]([("홈","/"),("서비스 안내","/notice/")])}</div>
        <h1>불법·선정적 서비스 불가 안내</h1>
        <p>간다GO는 경기남부 방문형 웰니스 서비스의 지역·프로그램·이용 장소 정보를 안내하는 사이트입니다. 다음 사항을 명확히 안내합니다.</p>
        <ul>
          <li>불법·선정적 서비스는 제공하거나 안내하지 않습니다.</li>
          <li>방문 가능 여부는 실제 주소와 예약 조건 확인 후 안내합니다.</li>
          <li>‘무조건 24시간 가능’과 같은 표현을 사용하지 않으며, 주소·건물 출입·이동 시간을 확인합니다.</li>
          <li>허위 후기·가짜 별점을 사용하지 않습니다.</li>
        </ul>
        {NOTICE}
      </div>
    </section>
  </main>''',
        trail=[("홈","/"),("서비스 안내","/notice/")]))

    # -------------------------------------------------------------------
    # sitemap.xml + robots.txt
    # -------------------------------------------------------------------
    urls = ["/", "/gyeonggi-south/area/", "/gyeonggi-south/program/",
            "/gyeonggi-south/use/", "/gyeonggi-south/check/",
            "/gyeonggi-south/osan-si/", "/contact/", "/privacy/", "/notice/"]
    urls += [f"/gyeonggi-south/area/{s}/" for s, _, _ in AREAS]
    urls += [f"/gyeonggi-south/life/{r[1]}/" for r in LIFE]
    urls += [f"/gyeonggi-south/program/{s}/" for s, _, _ in PROGRAMS]
    urls += [f"/gyeonggi-south/use/{s}/" for s, _, _ in USES]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f"  <url><loc>{BASE}{u}</loc><changefreq>weekly</changefreq></url>")
    sm.append("</urlset>")
    (g["ROOT"] / "sitemap.xml").write_text("\n".join(sm), encoding="utf-8")
    print("wrote sitemap.xml")

    robots = f"""User-agent: *
Allow: /

Sitemap: {BASE}/sitemap.xml
"""
    (g["ROOT"] / "robots.txt").write_text(robots, encoding="utf-8")
    print("wrote robots.txt")
