import sys, math; sys.path.insert(0, "/home/claude/tbook")
from engine import build, pdf, M

# ---- 정답 검산 ----
def ang(P, Q, R):  # ∠PQR (도)
    a = (P[0]-Q[0], P[1]-Q[1]); b = (R[0]-Q[0], R[1]-Q[1])
    return math.degrees(math.acos((a[0]*b[0]+a[1]*b[1]) / (math.hypot(*a)*math.hypot(*b))))
def near(a, b): return abs(a - b) < 1e-6
def chain(x, n):  # ∠XAY=x, A에서 시작해 두 반직선을 번갈아 길이 1인 선분을 이어 그림
    u = (1, 0); v = (math.cos(math.radians(x)), math.sin(math.radians(x)))
    P = [(0.0, 0.0)]; t = [0.0, 0.0]; cur = 0
    for i in range(n):
        ray = u if i % 2 == 0 else v; prev = P[-1]
        if i == 0: s = 1.0
        else:  # prev 에서 거리 1, ray 위의 먼 쪽 점
            b = -2*(ray[0]*prev[0]+ray[1]*prev[1]); c = prev[0]**2+prev[1]**2-1
            s = (-b + math.sqrt(b*b-4*c))/2
        P.append((ray[0]*s, ray[1]*s))
    return P
# 유형 01
assert (180-40)/2 == 70
x = 180 - 115; assert 180 - 2*x == 50
assert 180 - (72 + 36) == 72 and 36 + 36 == 72                     # ∠BDC = ∠A + ∠ABD
# 유형 02
assert 16/2 + 90 == 98
assert 90 - 62 == 28 and 48/2 == 24
# 유형 03 (좌표로 검산)
A, B, C, D = chain(25, 3); assert near(ang(C, D, A), 50)            # ∠CDB = 2∠A
A, B, C, D = chain(36, 3); assert near(ang(C, D, A), 72)
A, B, C, D, E = chain(20, 4); assert near(ang(D, E, A), 60)         # ∠DEC = 3∠A
# 유형 04
assert 180 - 110 == 70 and 180 - 70 - 70 == 40                     # ∠B=∠C=70 → AB=AC
assert 180 - 2*36 == 108 and (180-36)/2 == 72                       # AD=BD=BC
# 유형 05 (RHA: AD=CE, AE=BD)
assert 6 + 4 == 10 and (6+4)*10/2 == 50
# 유형 06
assert 13*4/2 == 26 and 2*20/10 == 4 and 90 - 64/2 == 58
# Level 2
assert (180-44)/2 == 68 and 180 - 2*68 == 44 and 68 - 44 == 24
assert 180 - (180-52)/2 == 116
assert 180 - 2*65 == 50
assert 8 + 5 == 13
A, B, C, D, E = chain(15, 4); assert near(ang(C, D, E), 90)        # BOSS: ∠CDE = 180-6x
assert 180 - 6*15 == 90
assert (90 - 24) == 66 and 180 - 2*66 == 48                         # 직각삼각형 빗변 중점 문항
# 서술형
assert 18/2 == 9 and (180 - 2*55)/2 == 35

S = 'font-family="Noto Sans CJK KR" font-size="12"'
def svg(w, h, body, width=None): return f'<svg viewBox="0 0 {w} {h}" width="{width or w}" {S}>{body}</svg>'
def lab(x, y, t, a="middle", c="#1b1f24", fw="700"): return f'<text x="{x}" y="{y}" text-anchor="{a}" fill="{c}" font-weight="{fw}">{t}</text>'
def arc(cx, cy, r, a1, a2, col="#E5475F"):
    p = lambda a: (cx + r*math.cos(math.radians(a)), cy - r*math.sin(math.radians(a)))
    (x1, y1), (x2, y2) = p(a1), p(a2); large = 1 if (a2 - a1) % 360 > 180 else 0
    return f'<path d="M{x1:.1f} {y1:.1f} A{r} {r} 0 {large} 0 {x2:.1f} {y2:.1f}" fill="none" stroke="{col}" stroke-width="1.6"/>'
def tick(x1, y1, x2, y2, n=1):  # 같은 길이 표시
    mx, my = (x1+x2)/2, (y1+y2)/2; dx, dy = x2-x1, y2-y1; L = math.hypot(dx, dy); nx, ny = -dy/L*5, dx/L*5; ux, uy = dx/L*3, dy/L*3
    return "".join(f'<path d="M{mx+(i-(n-1)/2)*ux*1.4-nx:.1f} {my+(i-(n-1)/2)*uy*1.4-ny:.1f} l{2*nx:.1f} {2*ny:.1f}" stroke="#1b1f24" stroke-width="1.4"/>' for i in range(n))
LN = '<g fill="none" stroke="#1b1f24" stroke-width="1.6">'

ISO = lambda top, extra="": svg(170, 130, LN + '<path d="M85 15 L20 115 L150 115 Z"/></g>' + tick(85, 15, 20, 115) + tick(85, 15, 150, 115) +
                           lab(85, 11, "A") + lab(12, 122, "B") + lab(158, 122, "C") + extra + (lab(85, 48, top, c="#E5475F") if top else ""), 150)
EXT = svg(200, 130, LN + '<path d="M85 15 L20 115 L150 115 Z M150 115 H195"/></g>' + tick(85, 15, 20, 115) + tick(85, 15, 150, 115) + arc(150, 115, 14, 0, 123) +
          lab(85, 11, "A") + lab(12, 122, "B") + lab(150, 128, "C") + lab(192, 128, "D") + lab(172, 100, "115°", c="#E5475F"), 175)
BIS = svg(170, 135, LN + '<path d="M85 15 L20 115 L150 115 Z"/><path d="M85 15 V115" stroke="#1E5BA8"/></g>' + tick(85, 15, 20, 115) + tick(85, 15, 150, 115) +
          '<path d="M85 105 h10 v10" fill="none" stroke="#1E5BA8" stroke-width="1.3"/>' + lab(85, 11, "A") + lab(12, 122, "B") + lab(158, 122, "C") + lab(85, 130, "D"), 150)
def CHAIN(n, a, d=30):
    P = chain(d, n); k = 60; ox, oy = 15, 120
    pt = [(ox + x*k, oy - y*k) for x, y in P]; nm = "ABCDE"
    rays = f'<path d="M{ox} {oy} H{ox+ max(p[0] for p in pt)-ox+25:.0f}"/><path d="M{ox} {oy} L{ox+ (max(p[0] for p in pt)-ox+25)*math.cos(math.radians(d)):.0f} {oy-(max(p[0] for p in pt)-ox+25)*math.sin(math.radians(d)):.0f}"/>'
    segs = "".join(f'<path d="M{pt[i][0]:.1f} {pt[i][1]:.1f} L{pt[i+1][0]:.1f} {pt[i+1][1]:.1f}"/>' for i in range(1, n))
    W = max(p[0] for p in pt) + 35
    return svg(int(W), 135, LN + rays + segs + '</g>' + "".join(tick(*pt[i], *pt[i+1]) for i in range(n)) +
               "".join(lab(p[0], p[1] + (14 if i % 2 == 1 or i == 0 else -7), nm[i]) for i, p in enumerate(pt)) + arc(ox, oy, 22, 0, d) + lab(ox + 36, oy - 4, a, c="#E5475F"), min(int(W), 230))
TAPE = svg(220, 110, '<rect x="5" y="30" width="210" height="55" fill="#EEF3FB" stroke="#1b1f24" stroke-width="1.4"/>' + LN + '<path d="M70 85 L110 30 L150 85"/></g>' +
           lab(64, 100, "B") + lab(110, 24, "A") + lab(156, 100, "C") + arc(70, 85, 16, 0, 54) + lab(96, 80, "∠x", c="#E5475F"), 190)
RHA = svg(230, 150, LN + '<path d="M10 115 H220"/><path d="M40 115 V30 L115 115 L185 115 V65 Z"/><path d="M40 30 L185 65"/></g>' +
          '<path d="M40 105 h10 v10 M185 105 h-10 v10" fill="none" stroke="#1E5BA8" stroke-width="1.3"/>' + tick(40, 30, 115, 115) + tick(115, 115, 185, 65) +
          lab(40, 22, "B") + lab(195, 62, "C") + lab(40, 132, "D") + lab(115, 132, "A") + lab(185, 132, "E") + lab(215, 110, "l", "start"), 200)
ANGB = svg(200, 130, LN + '<path d="M20 115 H185"/><path d="M20 115 L170 25"/><path d="M20 115 L180 70" stroke="#1E5BA8"/><path d="M128 80 V115 M128 80 L111 61" stroke-dasharray="4 3"/></g>' +
           lab(14, 128, "O") + lab(176, 22, "Y") + lab(190, 125, "X") + lab(186, 68, "P", c="#1E5BA8") + lab(128, 128, "A") + lab(104, 58, "B") + arc(20, 115, 26, 0, 31), 180)
ART = ('<svg viewBox="0 0 360 300" width="100%" font-family="Noto Sans CJK KR" font-weight="900">'
       '<path d="M180 30 L60 250 L300 250 Z" fill="rgba(255,255,255,.16)" stroke="#fff" stroke-width="4"/>'
       '<path d="M180 30 V250" stroke="#FFE680" stroke-width="4" stroke-dasharray="10 8"/>'
       '<path d="M180 232 h18 v18" fill="none" stroke="#FFE680" stroke-width="4"/>'
       '<g stroke="#fff" stroke-width="4"><path d="M112 135 l14 8"/><path d="M248 135 l-14 8"/></g>'
       '<path d="M88 250 A30 30 0 0 0 76 222" fill="none" stroke="#F2683A" stroke-width="5"/><path d="M272 250 A30 30 0 0 1 284 222" fill="none" stroke="#F2683A" stroke-width="5"/>'
       '<text x="180" y="288" fill="#fff" font-size="24" text-anchor="middle" opacity=".9">∠B ＝ ∠C</text></svg>')

def ty(no, name, idea, q, steps, a, us):
    return [("type", dict(no=no, name=name, idea=M(idea), ex=dict(q=M(q), steps=[(f"STEP {i+1}", M(x)) for i, x in enumerate(steps)], a=a)))] + \
           [("q", dict(q=M(qq), ch=[M(c) for c in ch] if ch else None, ans=an, sol=M(so), lv=lv)) for qq, ch, an, so, lv in us]

TY = (
 ty("01", "이등변삼각형의 밑각", "AB＝AC이면 <b>∠B＝∠C</b>. 꼭지각을 알면 밑각＝(180°－꼭지각)÷2.",
    "오른쪽 그림에서 AB＝AC이고 ∠A＝40°일 때, ∠B의 크기를 구하시오.<div class=fig>" + ISO("40°") + "</div>",
    ["AB＝AC이므로 ∠B＝∠C", "∠B＋∠C＝180°－40°＝140°", "∠B＝140°÷2＝70°"], "70°",
    [("오른쪽 그림에서 AB＝AC이고 ∠ACD＝115°일 때, ∠A의 크기를 구하시오.<div class=fig>" + EXT + "</div>", None, "50°", "∠ACB＝180°－115°＝65°＝∠B → ∠A＝180°－65°×2＝50°", 1),
     ("AB＝AC, ∠A＝36°인 △ABC에서 ∠B의 이등분선이 AC와 만나는 점을 D라 할 때, ∠BDC의 크기를 구하시오.", None, "72°",
      "∠B＝(180°－36°)÷2＝72° → ∠ABD＝36° → ∠BDC＝∠A＋∠ABD＝36°＋36°＝72° (삼각형의 외각)", 2)]) +
 ty("02", "꼭지각의 이등분선", "이등변삼각형의 꼭지각의 이등분선은 <b>밑변을 수직이등분</b>해요. → BD＝CD, AD⊥BC",
    "AB＝AC인 △ABC에서 ∠A의 이등분선이 BC와 만나는 점을 D라 하자. BC＝16 cm일 때, BD＝x cm, ∠ADC＝y°라 하면 x＋y의 값을 구하시오.<div class=fig>" + BIS + "</div>",
    ["꼭지각의 이등분선은 밑변을 이등분 → x＝16÷2＝8", "밑변과 수직 → y＝90", "x＋y＝8＋90＝98"], "98",
    [("위 그림에서 ∠B＝62°일 때, ∠BAD의 크기를 구하시오.", None, "28°", "△ABD에서 ∠ADB＝90° → ∠BAD＝180°－90°－62°＝28°", 1),
     ("위 그림에서 △ABC의 넓이가 48 cm²일 때, △ABD의 넓이를 구하시오.", None, "24 cm²", "BD＝CD이고 높이 AD가 같으므로 △ABD＝48÷2＝24 cm²", 2)]) +
 ty("03", "이어 붙인 이등변삼각형", "같은 길이 선분이 이어지면 이등변삼각형이 줄줄이! <b>외각＝이웃하지 않은 두 내각의 합</b>으로 x, 2x, 3x…",
    "오른쪽 그림에서 AB＝BC＝CD이고 ∠A＝25°일 때, ∠CDB의 크기를 구하시오.<div class=fig>" + CHAIN(3, "25°") + "</div>",
    ["△ABC는 BA＝BC → ∠BCA＝∠A＝25°", "∠CBD는 △ABC의 외각 → 25°＋25°＝50°", "△BCD는 CB＝CD → ∠CDB＝∠CBD＝50°"], "50°",
    [("위 그림과 같은 모양에서 AB＝BC＝CD이고 ∠CDB＝72°일 때, ∠A의 크기를 구하시오.", None, "36°", "∠CDB＝2∠A → ∠A＝72°÷2＝36°", 2),
     ("오른쪽 그림에서 AB＝BC＝CD＝DE이고 ∠A＝20°일 때, ∠DEC의 크기를 구하시오.<div class=fig>" + CHAIN(4, "20°", 20) + "</div>", None, "60°",
      "∠CBD＝40°, ∠DCE＝∠A＋∠ADC＝20°＋40°＝60°, DC＝DE이므로 ∠DEC＝60°", 3)]) +
 ty("04", "이등변삼각형이 되는 조건", "<b>두 내각의 크기가 같으면</b> 이등변삼각형 → 그 두 각의 대변의 길이가 같아요.",
    "△ABC에서 ∠A＝40°, ∠C의 외각의 크기가 110°이고 AC＝9 cm일 때, AB의 길이를 구하시오.",
    ["∠ACB＝180°－110°＝70°", "∠B＝180°－40°－70°＝70°", "∠B＝∠C이므로 AB＝AC＝9 cm"], "9 cm",
    [("폭이 일정한 종이 테이프를 오른쪽 그림과 같이 접었다. AB＝7 cm일 때, AC의 길이를 구하시오.<div class=fig>" + TAPE + "</div>", None, "7 cm",
      "테이프의 두 변이 평행하므로 엇각 ∠ACB＝∠x, 접은 각 ∠ABC＝∠x → ∠ABC＝∠ACB → AB＝AC＝7 cm", 2),
     ("AB＝AC, ∠A＝36°인 △ABC에서 ∠B의 이등분선이 AC와 만나는 점을 D라 하자. BC＝5 cm일 때, AD의 길이를 구하시오.", None, "5 cm",
      "∠ABD＝∠A＝36° → DA＝DB, ∠BDC＝72°＝∠C → BD＝BC＝5 cm → AD＝5 cm", 3)]) +
 ty("05", "직각삼각형의 합동", "빗변이 같은 두 직각삼각형: <b>RHA</b>(빗변＋한 예각) 또는 <b>RHS</b>(빗변＋다른 한 변)이면 합동.",
    "∠BAC＝90°, AB＝AC인 직각이등변삼각형의 꼭짓점 A를 지나는 직선 l에 두 점 B, C에서 내린 수선의 발을 D, E라 하자. BD＝6 cm, CE＝4 cm일 때, DE의 길이를 구하시오.<div class=fig>" + RHA + "</div>",
    ["∠BAD＋∠CAE＝90°, ∠BAD＋∠ABD＝90° → ∠ABD＝∠CAE", "빗변 AB＝CA, 한 예각이 같으므로 △ABD≡△CAE (RHA)", "AD＝CE＝4, AE＝BD＝6 → DE＝10 cm"], "10 cm",
    [("위 문제에서 사각형 DBCE의 넓이를 구하시오.", None, "50 cm²", "사다리꼴: (6＋4)×10÷2＝50 cm²", 2),
     ("다음 중 서로 합동인 두 직각삼각형이 <b>아닐 수도 있는</b> 경우는?", ["빗변과 한 예각이 각각 같다.", "빗변과 다른 한 변이 각각 같다.", "두 예각의 크기가 각각 같다.",
      "빗변이 아닌 두 변이 각각 같다.", "빗변이 아닌 한 변과 그 양 끝 각이 각각 같다."], "③", "세 각이 같아도 크기가 다를 수 있다 (닮음일 뿐).", 1)]) +
 ty("06", "각의 이등분선의 성질", "각의 이등분선 위의 점에서 두 변까지의 <b>거리는 같아요</b> (RHA). 거꾸로, 두 변까지 거리가 같은 점은 이등분선 위에.",
    "∠C＝90°인 △ABC에서 ∠A의 이등분선이 BC와 만나는 점을 D라 하자. AB＝13 cm, CD＝4 cm일 때, △ABD의 넓이를 구하시오.",
    ["점 D에서 AB에 수선의 발 E를 내리면 DE＝DC＝4 cm", "△ABD의 밑변 AB＝13, 높이 DE＝4", "넓이＝13×4÷2＝26 cm²"], "26 cm²",
    [("∠C＝90°인 △ABC에서 ∠A의 이등분선이 BC와 만나는 점을 D라 하자. AB＝10 cm, △ABD의 넓이가 20 cm²일 때, CD의 길이를 구하시오.", None, "4 cm",
      "D에서 AB까지의 거리＝2×20÷10＝4 cm＝CD", 2),
     ("오른쪽 그림에서 점 P에서 두 변 OX, OY에 내린 수선의 발이 A, B이고 PA＝PB이다. ∠XOY＝64°일 때, ∠APO의 크기를 구하시오.<div class=fig>" + ANGB + "</div>", None, "58°",
      "PA＝PB → OP는 ∠XOY의 이등분선 → ∠AOP＝32° → ∠APO＝90°－32°＝58°", 2)])
)

L2 = [
 dict(q="AB＝AC, ∠A＝44°인 △ABC의 변 AC 위에 BC＝BD가 되도록 점 D를 잡을 때, ∠ABD의 크기는?", ch=["20°", "24°", "28°", "32°", "36°"], ans="②",
      sol="∠C＝68° → △BCD에서 ∠BDC＝68°, ∠DBC＝44° → ∠ABD＝68°－44°＝24°", trap="△BCD도 이등변삼각형(BC＝BD)이에요.", ty="01", tags=["빈출"]),
 dict(q="AB＝AC, ∠A＝52°인 △ABC에서 ∠B, ∠C의 이등분선의 교점을 P라 할 때, ∠BPC의 크기는?", ch=["112°", "114°", "116°", "118°", "120°"], ans="③",
      sol="∠B＝∠C＝64° → ∠PBC＝∠PCB＝32° → ∠BPC＝180°－64°＝116°", ty="01"),
 dict(q="폭이 일정한 종이 테이프를 접었더니 접힌 선과 테이프의 변이 이루는 각 ∠x가 65°였다. 겹쳐진 삼각형에서 나머지 한 각의 크기는?<div class=fig>" + TAPE + "</div>",
      ch=["40°", "45°", "50°", "55°", "60°"], ans="③", sol="", trap="접은 각과 엇각이 같아 이등변삼각형이 생겨요.", ty="04"),
 dict(q="다음 중 옳은 것은?", ch=["이등변삼각형의 꼭지각의 이등분선은 밑변과 수직으로 만나지 않는다.", "두 내각의 크기가 같은 삼각형은 정삼각형이다.", "두 변의 길이가 같은 두 직각삼각형은 항상 합동이다.",
      "정삼각형은 이등변삼각형이 아니다.", "빗변의 길이와 한 예각의 크기가 각각 같은 두 직각삼각형은 합동이다."], ans="⑤", opcls="v",
      sol="① 수직이다 ② 이등변삼각형 ③ 같은 두 변이 빗변인지에 따라 다름 ④ 정삼각형도 이등변삼각형", ty="05"),
 dict(q="∠BAC＝90°, AB＝AC인 △ABC의 꼭짓점 A를 지나는 직선 l에 B, C에서 내린 수선의 발을 D, E라 하자. BD＝8 cm, CE＝5 cm일 때, DE의 길이는? (단위: cm)",
      ch=["11", "12", "13", "14", "15"], ans="③", sol="△ABD≡△CAE (RHA) → AD＝5, AE＝8 → DE＝13 cm", ty="05", tags=["빈출"]),
 dict(q="",
      ch=["10°", "12°", "15°", "18°", "20°"], ans="③", sol="", ty="03", tags=["BOSS"]),
]
# BOSS 문항 발문 정리 (그림의 이름 A~E 규칙에 맞춤)
L2[-1].update(q="오른쪽 그림처럼 ∠XAY의 두 변 위에 번갈아 점을 잡아 AB＝BC＝CD＝DE가 되도록 했다. ∠CDE＝90°일 때, ∠A의 크기는?<div class=fig>" + CHAIN(4, "x", 15) + "</div>",
              sol="∠A＝x라 하면 ∠DEC＝∠DCE＝3x → ∠CDE＝180°－6x＝90° → x＝15°", trap="밑각이 x, 2x, 3x로 늘어나는 규칙을 먼저 찾아요.")
L2[2]["sol"] = "테이프의 두 변이 평행 → 엇각이 같아 ∠ABC＝∠ACB＝65° → 180°－130°＝50°"
for p in L2:
    p["q"] = M(p["q"]); p["sol"] = M(p["sol"])

SVQ = [dict(ty="02", q=M("AB＝AC인 △ABC에서 ∠A의 이등분선이 BC와 만나는 점을 D라 하자. BC＝18 cm, ∠B＝55°일 때, BD의 길이와 ∠BAD의 크기를 구하는 과정을 서술하시오."),
            ans="9 cm, 35°", rb=[("꼭지각의 이등분선이 밑변을 수직이등분함을 쓰기", "30 %"), (M("BD＝18÷2＝9 cm"), "30 %"), (M("∠ADB＝90° → ∠BAD＝180°－90°－55°＝35°"), "40 %")],
            sol=M("BD＝CD＝9 cm, AD⊥BC → ∠BAD＝35°"), h=50),
       dict(ty="05", q=M("AB＝AC인 △ABC에서 BC의 중점을 M, 점 M에서 AB, AC에 내린 수선의 발을 각각 D, E라 하자. MD＝3 cm일 때, ME의 길이를 구하는 과정을 서술하시오."),
            ans="3 cm", rb=[(M("∠B＝∠C, BM＝CM, ∠BDM＝∠CEM＝90° 찾기"), "40 %"), (M("△BDM≡△CEM (RHA) 쓰기"), "40 %"), (M("ME＝MD＝3 cm"), "20 %")],
            sol=M("빗변 BM＝CM, 한 예각 ∠B＝∠C → RHA 합동 → ME＝MD＝3 cm"), h=50)]

CC = [("이등변삼각형", "두 변의 길이가 같은 삼각형. 같은 두 변이 만드는 각이 <span class=mk>꼭지각</span>, 마주 보는 변이 <b>밑변</b>, 밑변의 양 끝 각이 <span class=mk>밑각</span>.", "AB＝AC → ∠A 꼭지각, BC 밑변, ∠B·∠C 밑각"),
      ("성질 ① 밑각", "이등변삼각형의 <span class=mk>두 밑각의 크기는 같다.</span> (∠A의 이등분선을 그어 SAS 합동으로 증명)", "밑각＝(180°－꼭지각)÷2"),
      ("성질 ② 꼭지각의 이등분선", "꼭지각의 이등분선은 <span class=mk>밑변을 수직이등분</span>한다.", "BD＝CD, AD⊥BC"),
      ("이등변삼각형이 되는 조건", "<b>두 내각의 크기가 같은 삼각형</b>은 이등변삼각형. 종이 테이프 접기·각의 이등분선과 평행선에서 자주 나와요.", "∠B＝∠C → AB＝AC"),
      ("직각삼각형의 합동 조건", "빗변의 길이와 한 예각의 크기가 각각 같다 → <span class=mk>RHA 합동</span>. 빗변과 다른 한 변의 길이가 각각 같다 → <span class=mk>RHS 합동</span>.", "R: 직각, H: 빗변, A: 각, S: 변"),
      ("각의 이등분선의 성질", "각의 이등분선 위의 한 점에서 두 변까지의 <b>거리는 같다</b>. 거꾸로 두 변에서 같은 거리에 있는 점은 그 각의 이등분선 위에 있다.", "PA＝PB ⇔ ∠AOP＝∠BOP")]

spec = dict(
    brand=dict(academy="새봄수학학원", mark="봄", slogan="장유 · 한 명 한 명 끝까지", teacher="원장 선생님"),
    meta=dict(theme="math", subject="math", grade="중학교 2학년", unit="2학기 도형의 성질 · 이등변삼각형",
              title="이등변삼각형<br>그림으로 끝내기", sub="밑각·꼭지각의 이등분선부터 RHA·RHS 합동까지 — 2학기 도형의 첫 관문", curri="2022 개정 교육과정 · 중학교 수학 2", art=ART,
              inside=[("개념 6", "그림으로 정리"), ("유형 6", "예제 보고 따라 풀기"), ("실전 6", "학평형 + BOSS"), ("해설", "오답 함정까지")]),
    plan=dict(goals=["이등변삼각형의 <span class=mk>두 성질</span>(밑각, 꼭지각의 이등분선)을 이용해 각과 길이를 구할 수 있다.", "두 각이 같은 삼각형이 이등변삼각형임을 알고 활용할 수 있다.",
                     "직각삼각형의 합동 조건 <b>RHA·RHS</b>와 각의 이등분선의 성질을 설명할 수 있다."],
              link=("이어지는 공부", "중1 삼각형의 합동 → <b>이등변삼각형 · 직각삼각형의 합동</b> → 삼각형의 외심·내심 → 사각형의 성질"),
              map=[[("이등변삼각형", "꼭지각 · 밑각 · 밑변", 0)], [("성질 ①", "두 밑각이 같다", 0), ("성질 ②", "꼭지각의 이등분선 ⊥ 밑변", 0)],
                   [("되는 조건", "두 각이 같으면", 1)], [("직각삼각형 합동", "RHA · RHS", 0), ("각의 이등분선", "두 변까지 거리 같음", 0)], [("다음 단원", "외심과 내심", 1)]],
              rows=[("개념 정리 + 개념 확인", "개념"), ("Level 1 대표 유형 01~06", "대표 유형"), ("Level 2 실전 · Level 3 서술형", "실전"), ("스스로 점검 · 오답 노트", "자기 평가"), ("정답과 해설로 채점하기", "정답과 해설")],
              msg="도형 문제는 <b>같은 길이에 표시부터!</b> 같은 변 표시가 두 개 보이면 ‘이등변삼각형 → 밑각이 같다’를 바로 떠올려요. 문제 번호 아래 □□□에 회독 체크!"),
    next=[("Level 1 틀림", "개념 그림에 같은 변·같은 각 표시를 직접 해 보고 예제 다시 풀기"), ("Level 2 3개↓", "‘오답 함정’을 읽고 같은 유형 1개 더 풀기"),
          ("Level 3 감점", "채점 기준표에서 빠진 근거(합동 조건 등)를 오답 노트에 쓰기"), ("모두 맞힘", "다음 단원 ‘삼각형의 외심과 내심’으로 GO!")],
    teacher=dict(
        sessions=[("1회차", "이등변삼각형의 뜻·성질 ①② → 유형 01~02", "유형 01~02 따라 풀기"),
                  ("2회차", "이어 붙인 이등변삼각형 · 되는 조건(테이프 접기) → 유형 03~04", "유형 03~04 따라 풀기"),
                  ("3회차", "RHA·RHS · 각의 이등분선 → 유형 05~06 · Level 2 · BOSS", "서술형 2문항 · 오답 노트 · 자기 평가")],
        levels=[("기초반", "같은 변·같은 각 표시 연습 + Level 1 중심 · Level 2는 1·3·5번만"), ("기본반", "Level 1 숙제 → Level 2 전체 · 서술형 1문항"),
                ("심화반", "Level 1은 숙제로 · 수업은 Level 2~3 + BOSS 풀이 발표 · 성질 ① 증명 직접 쓰기")],
        tips=["모든 문제는 찰칵출판사가 새로 만든 문항이며, 정답은 계산(좌표 검산 포함)으로 전부 확인했습니다.",
              "학원 이름·로고·선생님 말씀은 원하시는 대로 바꿔 드립니다. 학교 시험 범위에 맞춘 챕터도 만들어 드립니다.",
              "문제 번호 아래 □□□는 학생 3회독 체크, 쪽 아래 ‘확인’ 칸은 선생님 도장 자리입니다.",
              "자기 평가 쪽의 ‘학부모 확인’ 칸으로 상담·학부모 연락에 바로 쓰실 수 있습니다."]),
    pages=[
        dict(sec="개념", head=[("band", "CONCEPT", "개념 정리 · 이등변삼각형")], blocks=[
            ("hook", "지붕 모양, 옷걸이, 접은 종이비행기의 앞날개… 왜 양쪽 기울기가 똑같을까?", "두 변이 같으면 두 각도 같아요 — 이 단원이 끝나면 <b>표시 두 개만 보고 각을 바로</b> 구할 수 있어요!"),
            ("grid", [("concept", dict(no=str(i), t=t, body=M(b), eg=M(e))) for i, (t, b, e) in enumerate(CC, 1)]),
            ("check", [("이등변삼각형의 두 <span class=blank></span>의 크기는 같다.", "밑각"), ("꼭지각의 이등분선은 밑변을 <span class=blank></span>한다.", "수직이등분"),
                       (M("AB＝AC, ∠A＝80°이면 ∠B＝<span class=blank></span>°이다."), "50"), ("빗변과 다른 한 변의 길이가 각각 같은 두 직각삼각형은 <span class=blank></span> 합동이다.", "RHS")])]),
        dict(sec="대표 유형", cols=True, head=[("lv", 1, "대표 유형 익히기 · 예제 보고 따라 풀기", "모두 맞히기")], blocks=list(TY)),
        dict(sec="실전", head=[("lv", 2, "학력평가 수준 실전 문제", "6문제 중 5개 이상")], cols=True,
             blocks=[("endtype",)] + [("q", p) for p in L2] + [("group", [("lv", 3, "풀이 과정을 쓰는 서술형", "채점 기준 80%↑"), ("essay", SVQ[0])]), ("essay", SVQ[1])]),
        dict(kind="selfcheck"), dict(kind="answers"), dict(kind="teacher"),
    ])

if __name__ == "__main__":
    qa = pdf(build(spec), "/home/claude/tbook/out/중2수학_이등변삼각형.pdf")
    for r in qa: print(r)
