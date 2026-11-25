import sys, math; sys.path.insert(0, "/home/claude/tbook")
from engine import build, pdf, M
from fractions import Fraction as F
from itertools import combinations

# ---- 정답 검산 ----
assert (6, 9) == (6, 9) and 6 + 9 == 15                       # 삼각기둥 교점·교선
assert 6 + 10 == 16 and 8 + 12 == 20                         # 오각뿔, 사각기둥
assert len(list(combinations(range(4), 2))) == 6             # 네 점 직선
assert len(list(combinations(range(5), 2))) == 10
pts = list(range(6)); col = {0, 1, 2}                          # 6점 중 3점 한 직선
lines = set(frozenset(c) if not set(c) <= col else frozenset(col) for c in combinations(pts, 2)); assert len(lines) == 13
AB = 20; AM = AB/2; AN = AM + AM/2; assert AN == 15
AB = 12; MB = 6; MN = 3; AN2 = 6 + 3; assert (MN, AN2) == (3, 9)
x = [x for x in range(0, 181) if 2*x+10 == x+40][0]; assert x == 30
assert 180 - 50 - 70 == 60
assert 90/3 == 30                                             # ∠AOC:∠COB=2:1, ∠AOB=90
x = [x for x in range(0, 91) if (x+20) + 2*x + x == 180][0]; assert x == 40 and 2*x == 80
assert 3*2 == 6                                               # 세 직선 맞꼭지각 쌍
assert abs((30*3+0.5*30) - 6*30) == 75                         # 3시 30분
assert 25 + 50 == 75 and 35 + 45 == 80 and 180 - 110 == 70
t = F(60)/F(11, 2); assert 6*t == 60 + F(1, 2)*t and t == 10 + F(10, 11)  # 2시 이후 처음 겹침
AB = 18; AC = 6; D_ = AC + (AB-AC)/2; assert D_ == 12
x = [x for x in range(0, 91) if 3*x-10 == x+50][0]; assert x == 30

S = 'font-family="Noto Sans CJK KR" font-size="12"'
def svg(w, h, body, width=None): return f'<svg viewBox="0 0 {w} {h}" width="{width or w}" {S}>{body}</svg>'
def lab(x, y, t, a="middle", c="#1b1f24", fw="700"): return f'<text x="{x}" y="{y}" text-anchor="{a}" fill="{c}" font-weight="{fw}">{t}</text>'
def arc(cx, cy, r, a1, a2, col="#E5475F"):
    p = lambda a: (cx + r*math.cos(math.radians(a)), cy - r*math.sin(math.radians(a)))
    (x1, y1), (x2, y2) = p(a1), p(a2); large = 1 if (a2 - a1) % 360 > 180 else 0
    return f'<path d="M{x1:.1f} {y1:.1f} A{r} {r} 0 {large} 0 {x2:.1f} {y2:.1f}" fill="none" stroke="{col}" stroke-width="1.6"/>'

PRISM = svg(150, 110, '<g fill="none" stroke="#1b1f24" stroke-width="1.5"><path d="M20 95 L70 95 L45 55 Z"/><path d="M70 95 L130 65 L105 25 L45 55 M105 25 L45 55"/></g><g fill="none" stroke="#1b1f24" stroke-width="1.3" stroke-dasharray="4 3"><path d="M20 95 L80 65 L130 65 M80 65 L105 25"/></g>', 130)
FOUR = svg(170, 90, '<g fill="#1b1f24">' + "".join(f'<circle cx="{x}" cy="{y}" r="3.5"/>' for x, y in [(30, 70), (75, 20), (140, 35), (115, 80)]) + '</g>' + lab(22, 86, "A") + lab(75, 13, "B") + lab(152, 35, "C") + lab(124, 88, "D"), 150)
SEG = lambda marks: svg(260, 46, '<path d="M15 25 H245" stroke="#1b1f24" stroke-width="1.6"/>' + "".join(f'<circle cx="{x}" cy="25" r="3.2" fill="#1b1f24"/>' + lab(x, 44, t) for x, t in marks), 230)
VERT = svg(170, 110, '<g stroke="#1b1f24" stroke-width="1.6"><path d="M15 95 L155 15"/><path d="M15 25 L155 85"/></g>' + arc(85, 55, 18, 30, 157) + arc(85, 55, 18, 210, 337, "#1E5BA8") +
           lab(85, 28, "(2x＋10)°", c="#E5475F") + lab(85, 92, "(x＋40)°", c="#1E5BA8"), 150)
THREE = svg(180, 110, '<g stroke="#1b1f24" stroke-width="1.6"><path d="M10 80 H170"/><path d="M90 80 L40 10"/><path d="M90 80 L150 15"/></g>' +
            arc(90, 80, 20, 0, 47) + arc(90, 80, 26, 47, 125, "#1E5BA8") + arc(90, 80, 20, 125, 180, "#10997A") + lab(122, 72, "50°") + lab(92, 46, "x°", c="#1E5BA8") + lab(58, 72, "70°"), 160)
PAR = svg(200, 120, '<g stroke="#1b1f24" stroke-width="1.6"><path d="M10 35 H190"/><path d="M10 90 H190"/><path d="M60 115 L140 5"/></g>' + lab(194, 32, "l", "start") + lab(194, 87, "m", "start") +
          arc(118, 35, 16, 54, 180) + lab(92, 24, "110°", c="#E5475F") + arc(80, 88, 16, 0, 54, "#1E5BA8") + lab(104, 82, "x", c="#1E5BA8"), 180)
ZIG = lambda a, b, x: svg(200, 130, '<g stroke="#1b1f24" stroke-width="1.6"><path d="M10 20 H190"/><path d="M10 110 H190"/><path d="M40 20 L130 65 L50 110" fill="none"/></g>' +
                          lab(194, 17, "l", "start") + lab(194, 107, "m", "start") + lab(78, 33, f"{a}°", c="#E5475F") + lab(84, 104, f"{b}°", c="#E5475F") + lab(110, 70, x, c="#1E5BA8"), 180)
BOX = svg(170, 120, '<g fill="none" stroke="#1b1f24" stroke-width="1.5"><path d="M20 100 H110 V40 H20 Z M110 100 L150 75 V15 L110 40 M20 40 L60 15 H150"/><path d="M20 100 L60 75 H150 M60 75 V15" stroke-dasharray="4 3"/></g>' +
          lab(14, 112, "E") + lab(114, 114, "F") + lab(14, 36, "A") + lab(114, 36, "B") + lab(60, 10, "D") + lab(156, 10, "C") + lab(158, 80, "G") + lab(54, 72, "H"), 150)
ART = ('<svg viewBox="0 0 360 300" width="100%" font-family="Noto Sans CJK KR" font-weight="900">'
       '<g stroke="#fff" stroke-width="4" stroke-linecap="round"><path d="M20 230 L340 70" opacity=".9"/><path d="M40 60 L330 250" opacity=".9"/><path d="M10 160 H350" opacity=".45"/></g>'
       '<circle cx="183" cy="150" r="9" fill="#F2683A" stroke="#fff" stroke-width="3"/>'
       '<path d="M222 131 A44 44 0 0 1 225 168" fill="none" stroke="#FFE680" stroke-width="5"/><text x="246" y="155" fill="#FFE680" font-size="22">∠x</text>'
       '<g transform="translate(60 250)"><path d="M0 0 L60 -95 L110 0 Z" fill="rgba(255,255,255,.18)" stroke="#fff" stroke-width="3"/></g>'
       '<text x="280" y="40" fill="#fff" font-size="26" opacity=".9">∥</text></svg>')

def ty(no, name, idea, q, steps, a, us):
    return [("type", dict(no=no, name=name, idea=M(idea), ex=dict(q=M(q), steps=[(f"STEP {i+1}", M(x)) for i, x in enumerate(steps)], a=a)))] + \
           [("q", dict(q=M(qq), ch=[M(c) for c in ch] if ch else None, ans=an, sol=M(so), lv=lv)) for qq, ch, an, so, lv in us]

TY = (
 ty("01", "교점과 교선의 개수", "입체도형에서 <b>교점 = 꼭짓점</b>, <b>교선 = 모서리</b>예요.",
    "오른쪽 그림과 같은 삼각기둥에서 교점의 개수를 a, 교선의 개수를 b라 할 때, a＋b의 값을 구하시오.<div class=fig>" + PRISM + "</div>",
    ["교점은 꼭짓점의 개수 → 6", "교선은 모서리의 개수 → 9", "a＋b＝6＋9＝15"], "15",
    [("오각뿔에서 교점의 개수와 교선의 개수의 합을 구하시오.", None, "16", "꼭짓점 6개, 모서리 10개 → 6＋10＝16", 1),
     ("다음 중 교점의 개수와 교선의 개수가 바르게 짝 지어진 것은?", ["삼각뿔 – 4, 4", "사각뿔 – 5, 8", "사각기둥 – 8, 8", "오각기둥 – 10, 10", "육각뿔 – 6, 12"], "②",
      "삼각뿔 4, 6 / 사각뿔 5, 8 / 사각기둥 8, 12 / 오각기둥 10, 15 / 육각뿔 7, 12", 2)]) +
 ty("02", "직선 · 반직선 · 선분의 개수", "두 점마다 직선 1개·선분 1개·반직선 2개. 단, <b>한 직선 위의 점</b>이 있으면 겹치는 것을 빼요.",
    "어느 세 점도 한 직선 위에 있지 않은 네 점 A, B, C, D가 있다. 이 중 두 점을 지나는 서로 다른 직선의 개수를 구하시오.<div class=fig>" + FOUR + "</div>",
    ["두 점을 고르는 방법: AB, AC, AD, BC, BD, CD", "어느 세 점도 한 직선 위에 있지 않으므로 모두 다른 직선 → 6개"], "6",
    [("한 직선 위에 있는 세 점 A, B, C 중 두 점을 이용하여 만들 수 있는 서로 다른 반직선의 개수를 구하시오.<div class=fig>" + SEG([(40, "A"), (130, "B"), (220, "C")]) + "</div>", None, "4",
      "반직선 AB(＝AC), BA, BC, CB(＝CA) → 4개", 2),
     ("어느 세 점도 한 직선 위에 있지 않은 다섯 점 중 두 점을 지나는 서로 다른 직선의 개수를 구하시오.", None, "10", "(5×4)÷2＝10", 1)]) +
 ty("03", "중점과 선분의 길이", "점 M이 선분 AB의 중점이면 <b>AM＝MB＝½AB</b>. 그림에 길이를 적어 가며 풀어요.",
    "선분 AB의 길이가 20 cm이다. 점 M은 선분 AB의 중점이고, 점 N은 선분 MB의 중점일 때, 선분 AN의 길이를 구하시오.<div class=fig>" + SEG([(20, "A"), (130, "M"), (185, "N"), (240, "B")]) + "</div>",
    ["AM＝MB＝20÷2＝10 (cm)", "MN＝10÷2＝5 (cm)", "AN＝AM＋MN＝10＋5＝15 (cm)"], "15 cm",
    [("선분 AB의 길이가 12 cm이고, 점 M은 AB의 중점, 점 N은 MB의 중점이다. 선분 MN의 길이를 구하시오.", None, "3 cm", "MB＝6 cm → MN＝6÷2＝3 cm", 1),
     ("위 문제에서 선분 AN의 길이를 구하시오.", None, "9 cm", "AN＝AM＋MN＝6＋3＝9 cm", 1)]) +
 ty("04", "맞꼭지각", "두 직선이 만나서 생기는 <b>맞꼭지각의 크기는 같아요</b>. 한 직선 위의 각의 합은 180°.",
    "오른쪽 그림에서 x의 값을 구하시오.<div class=fig>" + VERT + "</div>",
    ["두 각은 맞꼭지각이므로 크기가 같다.", "2x＋10＝x＋40 → x＝30"], "30",
    [("오른쪽 그림에서 x의 값을 구하시오.<div class=fig>" + THREE + "</div>", None, "60", "한 직선 위의 각의 합은 180° → x＝180－50－70＝60", 2),
     ("세 직선이 한 점에서 만날 때 생기는 맞꼭지각은 모두 몇 쌍인지 구하시오.", None, "6쌍", "직선 2개를 고를 때마다 2쌍 → 3×2＝6쌍", 2)]) +
 ty("05", "직각과 각의 크기", "∠AOB＝90°처럼 <b>전체 각을 먼저 쓰고</b> 비율대로 나눠요.",
    "∠AOB＝90°이고 점 C가 ∠AOB의 내부에 있다. ∠AOC：∠COB＝2：1일 때, ∠COB의 크기를 구하시오.",
    ["∠AOC＋∠COB＝90°", "비가 2：1이므로 ∠COB＝90°×1/3＝30°"], "30°",
    [("세 점 A, O, B가 한 직선 위에 있고 ∠AOC＝(x＋20)°, ∠COD＝2x°, ∠DOB＝x°일 때, ∠COD의 크기를 구하시오.", None, "80°", "(x＋20)＋2x＋x＝180 → x＝40 → ∠COD＝80°", 2),
     ("3시 30분일 때 시침과 분침이 이루는 각 중 작은 쪽의 크기를 구하시오.", None, "75°", "분침 180°, 시침 3×30＋30×0.5＝105° → 180－105＝75°", 3)]) +
 ty("06", "평행선과 동위각 · 엇각", "l∥m이면 <b>동위각·엇각의 크기가 같아요</b>. 꺾인 선은 꺾인 점을 지나 평행한 보조선을 그어요.",
    "오른쪽 그림에서 l∥m일 때, ∠x의 크기를 구하시오.<div class=fig>" + PAR + "</div>",
    ["l과 만나는 110°의 이웃한 각은 180°－110°＝70°", "l∥m이므로 동위각이 같다 → ∠x＝70°"], "70°",
    [("오른쪽 그림에서 l∥m일 때, ∠x의 크기를 구하시오.<div class=fig>" + ZIG(35, 45, "∠x") + "</div>", None, "80°", "꺾인 점을 지나 l에 평행한 직선을 그으면 엇각 35°, 45° → ∠x＝35°＋45°＝80°", 2),
     ("두 직선 l, m이 다른 한 직선과 만날 때, 엇각의 크기가 같으면 l과 m은 어떤 위치 관계인지 쓰시오.", None, "평행", "엇각의 크기가 같으면 두 직선은 평행하다.", 1)])
)

L2 = [
 dict(q="여섯 개의 점 중 세 점 A, B, C만 한 직선 위에 있고, 나머지는 어느 세 점도 한 직선 위에 있지 않다. 두 점을 지나는 서로 다른 직선의 개수는?", ch=["11", "12", "13", "14", "15"], ans="③",
      sol="(6×5)÷2＝15에서 A, B, C로 만든 3개는 모두 같은 직선 → 15－3＋1＝13", trap="세 점이 한 직선 위에 있으면 직선 3개가 아니라 1개예요.", ty="02", tags=["빈출"]),
 dict(q="오른쪽 그림의 직육면체에서 모서리 AB와 꼬인 위치에 있는 모서리의 개수는?<div class=fig>" + BOX + "</div>", ch=["2", "3", "4", "5", "6"], ans="③",
      sol="AB와 평행한 모서리 3개, 만나는 모서리 4개를 빼면 12－1－3－4＝4 → CG, DH, EH, FG", trap="평행하지도 만나지도 않는 모서리만 꼬인 위치예요.", ty="01"),
 dict(q="오른쪽 그림에서 l∥m일 때, ∠x의 크기는?<div class=fig>" + ZIG(25, 50, "∠x") + "</div>", ch=["65°", "70°", "75°", "80°", "85°"], ans="③",
      sol="꺾인 점을 지나 l에 평행한 보조선 → ∠x＝25°＋50°＝75°", ty="06", tags=["빈출"]),
 dict(q="선분 AB 위에 두 점 M, N이 있다. 점 M은 AB의 중점, 점 N은 AM의 중점이고 NB＝18 cm일 때, AB의 길이는? (단위: cm)", ch=["20", "22", "24", "26", "28"], ans="③",
      sol="AB＝4k라 하면 AN＝k, NB＝3k＝18 → k＝6 → AB＝24 cm", trap="NB는 AB의 3/4이에요.", ty="03"),
 dict(q="다음 중 옳은 것은?", ch=["반직선 AB와 반직선 BA는 같다.", "두 점을 지나는 직선은 2개이다.", "맞꼭지각의 크기는 항상 같다.", "평각의 크기는 90°이다.", "한 평면 위의 두 직선은 항상 만난다."], ans="③", opcls="v",
      sol="① 시작점과 방향이 달라 다른 반직선 ② 1개 ④ 180° ⑤ 평행하면 만나지 않는다.", ty="04"),
 dict(q="2시와 3시 사이에 시침과 분침이 처음으로 겹치는 시각은?", ch=["2시 10분", "2시 $10\\frac{8}{11}$분", "2시 $10\\frac{10}{11}$분", "2시 11분", "2시 $11\\frac{1}{11}$분"], ans="③",
      sol="t분 후 분침 6t°, 시침 60°＋0.5t° → 6t＝60＋0.5t → t＝120/11＝$10\\frac{10}{11}$", trap="시침도 1분에 0.5°씩 움직여요.", ty="05", tags=["BOSS"]),
]
for p in L2:
    p["q"] = M(p["q"]); p["sol"] = M(p["sol"])
SVQ = [dict(ty="03", q=M("선분 AB의 길이가 18 cm이다. 점 C는 AB를 삼등분하는 점 중 A에 가까운 점이고, 점 D는 선분 CB의 중점일 때, 선분 AD의 길이를 구하는 과정을 서술하고 답을 구하시오."),
            ans="12 cm", rb=[(M("AC＝18÷3＝6 cm 구하기"), "30 %"), (M("CB＝12 cm, CD＝6 cm 구하기"), "40 %"), (M("AD＝6＋6＝12 cm"), "30 %")], sol=M("AC＝6, CB＝12, CD＝6 → AD＝12 cm"), h=50),
       dict(ty="06", q=M("두 직선 l, m이 평행하고, 다른 한 직선과 만나서 생긴 엇각의 크기가 각각 (3x－10)°, (x＋50)°일 때, x의 값과 이 엇각의 크기를 구하는 과정을 서술하시오."),
            ans="x＝30, 80°", rb=[("엇각의 크기가 같음을 이용해 식 세우기", "40 %"), (M("x＝30 구하기"), "30 %"), (M("엇각의 크기 80° 구하기"), "30 %")], sol=M("3x－10＝x＋50 → x＝30 → 30＋50＝80°"), h=50)]

CC = [("점 · 선 · 면", "점이 움직이면 선, 선이 움직이면 면이 돼요. 선과 선(또는 면)이 만나는 점이 <span class=mk>교점</span>, 면과 면이 만나는 선이 <span class=mk>교선</span>.", "입체도형: 교점의 개수＝꼭짓점, 교선의 개수＝모서리"),
      ("직선 · 반직선 · 선분", "직선 AB는 양쪽 끝없이, 반직선 AB는 A에서 시작해 B 쪽으로 끝없이, 선분 AB는 A부터 B까지.", "반직선 AB와 반직선 BA는 <b>다른</b> 반직선"),
      ("두 점 사이의 거리 · 중점", "두 점을 잇는 선 중 가장 짧은 선분 AB의 길이가 두 점 사이의 거리. 선분을 이등분하는 점이 <span class=mk>중점</span>.", "M이 AB의 중점 → AM＝MB＝½AB"),
      ("각과 맞꼭지각", "평각 180°, 직각 90°, 예각은 0°보다 크고 90°보다 작은 각, 둔각은 90°보다 크고 180°보다 작은 각. <span class=mk>맞꼭지각의 크기는 같다.</span>", "두 직선이 만나면 맞꼭지각 2쌍"),
      ("수직과 수선", "두 직선이 직각으로 만나면 서로 수직. 점 P에서 직선 l에 내린 수선의 발 H에 대해 <b>PH가 점과 직선 사이의 거리</b>.", "AB⊥CD"),
      ("위치 관계 · 평행선", "공간에서 두 직선: 한 점에서 만난다 / 평행하다 / <b>꼬인 위치</b>. 평행선에서는 <span class=mk>동위각·엇각의 크기가 같다.</span>", "엇각이 같으면 두 직선은 평행")]

spec = dict(
    brand=dict(academy="새봄수학학원", mark="봄", slogan="장유 · 한 명 한 명 끝까지", teacher="원장 선생님"),
    meta=dict(theme="math", subject="math", grade="중학교 1학년", unit="2학기 Ⅴ. 기본 도형",
              title="기본 도형<br>그림으로 끝내기", sub="점·선·면부터 맞꼭지각·평행선까지 — 2학기 첫 시험의 기초", curri="2022 개정 교육과정 · 중학교 수학 1", art=ART,
              inside=[("개념 6", "그림으로 정리"), ("유형 6", "예제 보고 따라 풀기"), ("실전 6", "학평형 + BOSS"), ("해설", "오답 함정까지")]),
    plan=dict(goals=["점·선·면, 직선·반직선·선분을 구별하고 <span class=mk>개수를 셀 수 있다</span>.", "중점·맞꼭지각·직각을 이용해 길이와 각의 크기를 구할 수 있다.",
                     "평행선에서 <b>동위각·엇각</b>을 찾아 각의 크기를 구할 수 있다."],
              link=("이어지는 공부", "초등 각도·평면도형 → <b>기본 도형</b> → 작도와 합동 → 평면도형의 성질"),
              map=[[("점·선·면", "교점 · 교선", 0), ("직선·반직선·선분", "개수 세기", 0)], [("각", "평각 · 직각 · 맞꼭지각", 1)],
                   [("수직·수선", "점과 직선 사이 거리", 0), ("위치 관계", "평행 · 꼬인 위치", 0), ("평행선", "동위각 · 엇각", 0)], [("다음 단원", "작도와 합동", 1)]],
              rows=[("개념 정리 + 개념 확인", "개념"), ("Level 1 대표 유형 01~06", "대표 유형"), ("Level 2 실전 · Level 3 서술형", "실전"), ("스스로 점검 · 오답 노트", "자기 평가"), ("정답과 해설로 채점하기", "정답과 해설")],
              msg="기본 도형은 <b>그림에 숫자를 적는 습관</b>이 전부예요! 각은 보이는 대로 표시하고, 평행선이 나오면 동위각·엇각부터 찾아요. 문제 번호 아래 □□□에 회독 체크!"),
    next=[("Level 1 틀림", "개념 그림을 직접 다시 그려 보고 대표 예제 다시 풀기"), ("Level 2 3개↓", "‘오답 함정’을 읽고 같은 유형 1개 더 풀기"),
          ("Level 3 감점", "채점 기준표에서 빠진 단계를 오답 노트에 쓰기"), ("모두 맞힘", "다음 단원 ‘작도와 합동’으로 GO!")],
    teacher=dict(
        sessions=[("1회차", "점·선·면 · 직선·반직선·선분 · 중점 → 유형 01~03", "유형 01~03 따라 풀기 (01~06)"),
                  ("2회차", "각 · 맞꼭지각 · 평행선 → 유형 04~06 (보조선 긋기 연습)", "유형 04~06 따라 풀기 (07~12)"),
                  ("3회차", "Level 2 실전 13~18 · BOSS 18 함께 도전", "서술형 19~20 · 오답 노트 · 자기 평가")],
        levels=[("기초반", "그림 그리기 + Level 1 중심 · Level 2는 15·17만"), ("기본반", "Level 1 숙제 → Level 2 전체 · 서술형 1문항"),
                ("심화반", "Level 1은 숙제로 · 수업은 Level 2~3 + BOSS 풀이 발표")],
        tips=["모든 문제는 찰칵출판사가 새로 만든 문항이며, 정답은 계산으로 전부 검산했습니다.",
              "학원 이름·로고·선생님 말씀은 원하시는 대로 바꿔 드립니다. 학교 시험 범위에 맞춘 챕터도 만들어 드립니다.",
              "문제 번호 아래 □□□는 학생 3회독 체크, 쪽 아래 ‘확인’ 칸은 선생님 도장 자리입니다.",
              "자기 평가 쪽의 ‘학부모 확인’ 칸으로 상담·학부모 연락에 바로 쓰실 수 있습니다."]),
    pages=[
        dict(sec="개념", head=[("band", "CONCEPT", "개념 정리 · 기본 도형")], blocks=[
            ("hook", "가위 날 두 개가 만나는 각, 철길 두 줄과 침목… 우리 주변 도형 속에 숨은 같은 각을 찾을 수 있을까?", "가위 날의 맞꼭지각, 철길의 동위각 — 이 단원이 끝나면 <b>보이지 않던 같은 각</b>이 보여요!"),
            ("grid", [("concept", dict(no=str(i), t=t, body=M(b), eg=M(e))) for i, (t, b, e) in enumerate(CC, 1)]),
            ("check", [("사각뿔의 교선의 개수는 <span class=blank></span>이다.", "8"), ("맞꼭지각의 크기는 서로 <span class=blank></span>.", "같다"),
                       (M("평각의 크기는 <span class=blank></span>°이다."), "180"), ("공간에서 평행하지도 만나지도 않는 두 직선은 <span class=blank></span>에 있다.", "꼬인 위치")])]),
        dict(sec="대표 유형", cols=True, head=[("lv", 1, "대표 유형 익히기 · 예제 보고 따라 풀기", "모두 맞히기")], blocks=list(TY)),
        dict(sec="실전", head=[("lv", 2, "학력평가 수준 실전 문제", "6문제 중 5개 이상")], cols=True,
             blocks=[("endtype",)] + [("q", p) for p in L2] + [("group", [("lv", 3, "풀이 과정을 쓰는 서술형", "채점 기준 80%↑"), ("essay", SVQ[0])]), ("essay", SVQ[1])]),
        dict(kind="selfcheck"), dict(kind="answers"), dict(kind="teacher"),
    ])

if __name__ == "__main__":
    qa = pdf(build(spec), "/home/claude/tbook/out/중1수학_기본도형.pdf")
    for r in qa: print(r)
