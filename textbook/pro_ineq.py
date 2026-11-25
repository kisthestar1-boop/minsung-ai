# 고1 이차부등식 — 시중 교재(개념원리·쎈) 수준 편집 + 찰칵 강점(오른쪽 '왜 그럴까?' 원리 노트)
from concept_ineq import para, mini, numline, PK, BL, INK

B = "<span class=blank></span>"
CSS = """<style>
.pr{font-size:9.8pt;line-height:1.72;color:#111827}
.pr .two{display:grid;grid-template-columns:1fr 44mm;gap:0 5mm}
.pr .main{min-width:0}
.pr .side{border-left:1px dashed #C9D3E0;padding-left:3.6mm;font-size:8.4pt;line-height:1.6;color:#374151}
.pr .side .nt{margin-bottom:4mm}
.pr .side .nt b.h{display:inline-block;font-size:7.6pt;font-weight:900;letter-spacing:.04em;color:#fff;background:var(--c1);border-radius:3px;padding:0 1.6mm;margin-bottom:1mm}
.pr .side .nt.why b.h{background:var(--c2)}
.pr .side .nt.why{background:#FFF7F0;border-radius:6px;padding:2mm 2.6mm}
.pr .sh{display:flex;align-items:center;gap:2.4mm;margin:0 0 2mm;border-bottom:1.6px solid var(--c1);padding-bottom:1mm}
.pr .sh i{font-style:normal;font-weight:900;color:#fff;background:var(--c1);border-radius:99px;padding:0 2.6mm;font-size:9pt}
.pr .sh b{font-family:'Noto Sans CJK KR';font-weight:900;font-size:11.4pt;color:var(--d)}
.pr .sh small{margin-left:auto;font-size:7.8pt;color:#6B7280}
.pr .it{margin:0 0 1.2mm}.pr .it b.n{color:var(--c1);margin-right:1.4mm}
.pr .cbx{background:var(--t);border-radius:6px;padding:2mm 3.4mm;margin:1.4mm 0 2mm}
.pr .hl{background:linear-gradient(transparent 55%,#FFE680 55%);font-weight:700}
.pr .tb{width:100%;border-collapse:collapse;font-size:8.9pt;text-align:center;margin:1mm 0 1.6mm}
.pr .tb th,.pr .tb td{border:1px solid #CBD5E1;padding:.8mm 1mm}
.pr .tb thead th{background:#fff;font-weight:700}
.pr .tb tbody th{background:var(--t);white-space:nowrap}
.pr .tb .k{background:#FFF8D6}
.pr .sec{margin-bottom:4.2mm}
/* 필수 예제 */
.pr .ex{border:1.4px solid var(--c1);border-radius:8px;padding:2.4mm 3.6mm;margin-bottom:1.8mm}
.pr .ex .t{display:flex;align-items:center;gap:2mm;font-weight:900;color:var(--d);margin-bottom:.8mm}
.pr .ex .t em{font-style:normal;background:var(--c1);color:#fff;border-radius:4px;padding:0 1.8mm;font-size:8.6pt}
.pr .tg2{text-indent:0;display:inline-block;font-size:7.8pt;font-weight:900;border-radius:3px;padding:0 1.4mm;margin-right:2mm;color:#fff;background:#6B7280}
.pr .tg2.em2{background:var(--c2)}
.pr .sol{padding-left:12mm;text-indent:-12mm;margin:.8mm 0}
.pr .ans{color:#C2335F;font-weight:900}
.pr .chk{display:grid;grid-template-columns:1fr 1fr;gap:2mm 6mm;margin:2mm 0 4mm}
.pr .chk>div{border-top:1px solid #E5E7EB;padding-top:1.2mm;min-height:22mm}
.pr .chk b.n{color:var(--c2);font-family:'Noto Sans CJK KR';margin-right:1.6mm}
.pr .cb{display:inline-block;background:var(--c2);color:#fff;font-size:7.6pt;font-weight:900;border-radius:3px;padding:0 1.6mm;margin-right:1.6mm}
/* 기본 드릴 (2단) */
.pr .drill{column-count:2;column-gap:7mm;column-rule:1px solid #E5E7EB}
.pr .gp{break-inside:avoid;margin-bottom:2.2mm}
.pr .gh{font-size:8.8pt;font-weight:700;color:var(--d);margin-bottom:.8mm}
.pr .gh span{color:var(--c2);font-weight:900;margin-right:1mm}
.pr .dq{break-inside:avoid;min-height:21.5mm}
.pr .dq b{color:var(--c2);font-family:'Noto Sans CJK KR';font-weight:900;margin-right:2mm}
.pr .ref{font-size:7.4pt;color:#9CA3AF;text-align:right}
</style>"""

def graph():
    return para(lambda x: (x - 1) * (x - 4) * 0.9, [1, 4], -0.6, 5.6, w=300, h=150, ymin=-2.8, ymax=4.8, ticks=[(1, "α"), (4, "β")])

C1 = CSS + f"""<div class="pr"><div class="two"><div class="main">
<div class="sec"><div class="sh"><i>01-1</i><b>이차부등식과 이차함수의 그래프</b><small>필수 01 · 유형 01</small></div>
<div class="it">부등식의 모든 항을 좌변으로 옮겨 정리했을 때 (이차식) ＞0, ＜0, ≥0, ≤0 꼴이 되는 부등식을 <b>이차부등식</b>이라 한다.</div>
<div class="row" style="display:grid;grid-template-columns:1fr 1.1fr;gap:4mm;align-items:center"><div>{graph()}</div>
<div class="cbx" style="margin:0">$a>0$, 이차방정식 $ax^2+bx+c=0$의 두 근이 $\\alpha,\\beta\\ (\\alpha<\\beta)$일 때<br>
① $ax^2+bx+c<0$ ⇔ <span class="hl">$\\alpha<x<\\beta$</span> (그래프가 $x$축 아래)<br>
② $ax^2+bx+c>0$ ⇔ <span class="hl">$x<\\alpha$ 또는 $x>\\beta$</span> (위)</div></div>
<div class="it" style="margin-top:1.4mm"><b class="n">풀이 순서</b> ① 우변을 0으로, $x^2$의 계수를 양수로 ② 인수분해(근의 공식)로 두 근 ③ 그래프에서 읽기</div></div>

<div class="sec"><div class="sh"><i>01-2</i><b>판별식과 이차부등식의 해</b><small>필수 01 · 유형 02, 03</small></div>
<div class="it">$a>0$일 때, 이차방정식 $ax^2+bx+c=0$의 판별식을 $D=b^2-4ac$라 하면</div>
<table class="tb"><thead><tr><th style="width:23%"></th><th>$D>0$<br>{mini(0)}</th><th>$D=0$<br>{mini(1)}</th><th>$D<0$<br>{mini(2)}</th></tr></thead>
<tbody><tr><th>$ax^2+bx+c>0$</th><td>$x<\\alpha$ 또는 $x>\\beta$</td><td class="k">$x\\ne\\alpha$인 모든 실수</td><td>모든 실수</td></tr>
<tr><th>$ax^2+bx+c\\ge0$</th><td>$x\\le\\alpha$ 또는 $x\\ge\\beta$</td><td class="k">모든 실수</td><td>모든 실수</td></tr>
<tr><th>$ax^2+bx+c<0$</th><td>$\\alpha<x<\\beta$</td><td class="k">해는 없다.</td><td>해는 없다.</td></tr>
<tr><th>$ax^2+bx+c\\le0$</th><td>$\\alpha\\le x\\le\\beta$</td><td class="k">$x=\\alpha$</td><td>해는 없다.</td></tr></tbody></table>
<div class="cbx">모든 실수 $x$에 대하여 $ax^2+bx+c>0$ ⇔ <span class="hl">$a>0,\\ D<0$</span> &nbsp;·&nbsp; $ax^2+bx+c\\ge0$ ⇔ <span class="hl">$a>0,\\ D\\le0$</span></div></div>

<div class="sec"><div class="sh"><i>01-3</i><b>연립이차부등식</b><small>필수 02 · 유형 04, 05</small></div>
<div class="it">각 부등식의 해를 구한 뒤 <b>수직선 위에 함께 나타내어 공통부분</b>을 구한다. (등호 포함 ●, 불포함 ○)</div>
<div style="display:grid;grid-template-columns:1.5fr 1fr;gap:3mm;align-items:center">{numline()}<div style="font-size:9pt">$\\begin{{cases}}x^2-4x-5<0\\\\x^2-3x\\ge0\\end{{cases}}$<br>→ <span class="hl">$-1<x\\le0$ 또는 $3\\le x<5$</span></div></div></div>
</div>

<div class="side">
<div class="nt why"><b class="h">왜 그럴까?</b><br>$(x-\\alpha)(x-\\beta)<0$은 두 수의 곱이 음수 → 부호가 <b>서로 다르다</b>. $x-\\alpha>0$인데 $x-\\beta<0$인 곳, 즉 <b>두 근 사이</b>뿐이다.</div>
<div class="nt"><b class="h">TIP</b><br>$x^2$의 계수가 음수이면 양변에 $-1$을 곱하고 <b>부등호 방향을 바꾼다</b>.</div>
<div style="height:16mm"></div>
<div class="nt why"><b class="h">왜 그럴까?</b><br>$ax^2+bx+c=a\\left(x+\\frac{{b}}{{2a}}\\right)^2-\\frac{{D}}{{4a}}$<br>꼭짓점의 높이가 $-\\frac{{D}}{{4a}}$이므로 $a>0,\\ D<0$이면 꼭짓점이 $x$축보다 위 → 그래프 전체가 위에 있다.</div>
<div class="nt"><b class="h">주의</b><br>$(x-3)^2>0$의 해는 ‘모든 실수’가 아니라 <b>$x\\ne3$인 모든 실수</b>.</div>
<div class="nt"><b class="h">주의</b><br>$x^2$의 계수에 문자가 있으면 <b>(계수)$=0$</b>인 경우를 먼저 따로 확인한다.</div>
<div style="height:8mm"></div>
<div class="nt"><b class="h">TIP</b><br>정수 해의 개수를 묻는 문제는 끝점이 ●인지 ○인지에서 가장 많이 틀린다.</div>
</div></div></div>"""

C2 = CSS + f"""<div class="pr">
<div class="ex"><div class="t"><em>필수 01</em>이차부등식의 풀이</div>다음 이차부등식을 푸시오.<br>(1) $x^2-2x-8\\le0$ &nbsp;&nbsp;&nbsp;&nbsp; (2) $-2x^2+x+3<0$</div>
<div class="sol"><span class="tg2 em2">설명</span>$x^2$의 계수를 양수로 만든 뒤 인수분해하여 두 근을 구하고, 그래프의 위치로 해를 읽는다.</div>
<div class="sol"><span class="tg2">풀이</span>(1) $(x+2)(x-4)\\le0$ &nbsp;∴ <span class="ans">$-2\\le x\\le4$</span></div>
<div class="sol"><span class="tg2" style="visibility:hidden">풀이</span>(2) 양변에 $-1$을 곱하면 $2x^2-x-3>0$, $(x+1)(2x-3)>0$ &nbsp;∴ <span class="ans">$x<-1$ 또는 $x>\\dfrac{{3}}{{2}}$</span></div>
<div class="chk"><div><span class="cb">확인체크</span><b class="n">01</b>$x^2+x-6>0$을 푸시오.</div><div><b class="n">02</b>$-x^2+4x-3\\ge0$을 푸시오.</div></div>

<div class="ex"><div class="t"><em>필수 02</em>모든 실수 $x$에 대하여 성립하는 이차부등식</div>모든 실수 $x$에 대하여 이차부등식 $x^2+2(k-1)x+k+5>0$이 성립하도록 하는 실수 $k$의 값의 범위를 구하시오.</div>
<div class="sol"><span class="tg2 em2">설명</span>$x^2$의 계수가 양수이므로 그래프가 항상 $x$축보다 위에 있으려면 $D<0$이어야 한다.</div>
<div class="sol"><span class="tg2">풀이</span>$\\dfrac{{D}}{{4}}=(k-1)^2-(k+5)=k^2-3k-4<0$, $(k+1)(k-4)<0$ &nbsp;∴ <span class="ans">$-1<k<4$</span></div>
<div class="chk"><div><span class="cb">확인체크</span><b class="n">03</b>모든 실수 $x$에 대하여 $x^2-2kx+4>0$이 성립하도록 하는 $k$의 범위를 구하시오.</div>
<div><b class="n">04</b>모든 실수 $x$에 대하여 $kx^2-4x+k>0$이 성립하도록 하는 실수 $k$의 범위를 구하시오.</div></div>

<div class="ex"><div class="t"><em>필수 03</em>연립이차부등식</div>연립부등식 $\\begin{{cases}}x^2-9\\le0\\\\x^2+2x-8\\ge0\\end{{cases}}$을 푸시오.</div>
<div class="sol"><span class="tg2 em2">설명</span>두 부등식의 해를 수직선 위에 나타내어 공통부분을 구한다.</div>
<div class="sol"><span class="tg2">풀이</span>$x^2-9\\le0$에서 $-3\\le x\\le3$, &nbsp;$x^2+2x-8\\ge0$에서 $(x+4)(x-2)\\ge0$ → $x\\le-4$ 또는 $x\\ge2$ &nbsp;∴ <span class="ans">$2\\le x\\le3$</span></div>
<div class="chk"><div><span class="cb">확인체크</span><b class="n">05</b>연립부등식 $\\begin{{cases}}x^2-x-2<0\\\\x^2-4x+3>0\\end{{cases}}$을 푸시오.</div>
<div><b class="n">06</b>05의 해를 만족시키는 정수 $x$의 개수를 구하시오.</div></div>
<div class="ref">확인체크 정답 — 01 $x<-3$ 또는 $x>2$ · 02 $1\\le x\\le3$ · 03 $-2<k<2$ · 04 $k>2$ · 05 $-1<x<1$ · 06 1개($x=0$)</div>
</div>"""

DR = [
 ("[0001~0006] 다음 이차부등식을 푸시오.", ["$x^2-3x+2<0$", "$x^2-x-12\\ge0$", "$x^2+4x>0$", "$2x^2-5x-3\\le0$", "$-x^2+2x+8>0$", "$x^2-6x+9\\le0$"]),
 ("[0007~0010] 다음 이차부등식을 푸시오.", ["$x^2-4x+4>0$", "$x^2+2x+3>0$", "$x^2+x+1<0$", "$-x^2+6x-9\\ge0$"]),
 ("[0011~0012] 다음을 만족시키는 상수 $a, b$의 값을 구하시오.", ["$x^2+ax+b<0$의 해가 $2<x<5$", "$ax^2+bx+6>0$의 해가 $-2<x<3$"]),
 ("[0013~0014] 모든 실수 $x$에 대하여 다음이 성립하도록 하는 실수 $k$의 범위를 구하시오.", ["$x^2-2kx+4k-3>0$", "$x^2+(k+1)x+k+1\\ge0$"]),
 ("[0015~0016] 다음 연립부등식을 푸시오.", ["$\\begin{cases}x^2-5x+4\\le0\\\\x^2-2x-3<0\\end{cases}$", "$\\begin{cases}x^2-x-6>0\\\\x^2-16\\le0\\end{cases}$"]),
]
DANS = ["$1<x<2$", "$x\\le-3$ 또는 $x\\ge4$", "$x<-4$ 또는 $x>0$", "$-\\tfrac12\\le x\\le3$", "$-2<x<4$", "$x=3$",
        "$x\\ne2$인 모든 실수", "모든 실수", "해는 없다", "$x=3$", "$a=-7,\\ b=10$", "$a=-1,\\ b=1$", "$1<k<3$", "$-1\\le k\\le3$",
        "$1\\le x<3$", "$-4\\le x<-2$ 또는 $3<x\\le4$"]

def drill():
    h, n = [], 1
    for g, qs in DR:
        h.append(f'<div class="gp"><div class="gh">{g}</div></div>')
        for q in qs:
            h.append(f'<div class="dq"><b>{n:04d}</b>{q}</div>'); n += 1
    return "".join(h)

C3 = CSS + f"""<div class="pr"><div class="drill">{drill()}</div>
<div class="ref">정답 — {" · ".join(f"{i:04d} {a}" for i, a in enumerate(DANS, 1))}</div></div>"""

# ───── 개념 먼저, 쉽게 → 바로 예제 (개념원리식 흐름) ─────
CSS2 = """<style>
.pr .exq{margin:2mm 0 1mm;padding:2mm 3.4mm;border-top:1.4px solid var(--c1);background:#FAFBFD}
.pr .exq .h{font-weight:900;color:var(--c1);margin-right:2mm}
.pr .easy{font-size:10.4pt;line-height:1.85}
.pr .sp{height:3.4mm}
</style>"""

def graph2():
    return para(lambda x: (x + 2) * (x - 5) * 0.45, [-2, 5], -4, 7, w=300, h=150, ymin=-6, ymax=5.6, ticks=[(-2, "−2"), (5, "5")])

def sol(t):
    return f'<div class="sol"><span class="tg2">풀이</span>{t}</div>'

K1 = CSS + CSS2 + f"""<div class="pr"><div class="two"><div class="main">
<div class="sec"><div class="sh"><i>01-1</i><b>이차부등식이란?</b></div>
<div class="easy">$x^2-5x+4<0$, $\\ 2x^2+x-3\\ge0$처럼 모든 항을 좌변으로 옮겨 정리했을 때<br><b>좌변이 $x$에 대한 이차식</b>인 부등식을 <span class="hl">이차부등식</span>이라 한다.</div>
<div class="cbx">이차방정식 $x^2-5x+4=0$의 해 → $x=1,\\ 4$ &nbsp;(<b>점</b> 두 개)<br>이차부등식 $x^2-5x+4<0$의 해 → $1<x<4$ &nbsp;(<b>범위</b>)</div></div>

<div class="sec"><div class="sh"><i>01-2</i><b>이차부등식의 해와 그래프</b></div>
<div style="display:grid;grid-template-columns:1fr 1.15fr;gap:4mm;align-items:center"><div>{graph()}</div>
<div class="cbx" style="margin:0">$a>0$이고 $ax^2+bx+c=0$의 두 근이 $\\alpha,\\beta\\ (\\alpha<\\beta)$일 때<br>
① $ax^2+bx+c<0$의 해 → <span class="hl">$\\alpha<x<\\beta$</span><br>
② $ax^2+bx+c>0$의 해 → <span class="hl">$x<\\alpha$ 또는 $x>\\beta$</span></div></div>
<div class="it" style="margin-top:1.2mm">그래프가 $x$축보다 <b>아래</b>에 있는 부분 → $y<0$ &nbsp;·&nbsp; <b>위</b>에 있는 부분 → $y>0$</div>
<div class="exq"><span class="h">예제</span>다음 이차부등식을 푸시오. &nbsp;(1) $x^2-3x-10<0$ &nbsp;&nbsp;(2) $x^2-3x-10\\ge0$</div>
{sol("$x^2-3x-10=(x+2)(x-5)$이므로 두 근은 $-2,\\ 5$")}
<div style="display:grid;grid-template-columns:1.2fr 1fr;gap:3mm;align-items:center"><div style="padding-left:12mm">(1) 그래프가 $x$축 아래 → <span class="ans">$-2<x<5$</span><br>(2) 그래프가 $x$축 위(또는 위에 닿음) → <span class="ans">$x\\le-2$ 또는 $x\\ge5$</span></div><div>{graph2()}</div></div>
</div></div>

<div class="side">
<div class="nt"><b class="h">참고</b><br>부등식의 해 = 부등식을 참이 되게 하는 $x$의 값 전체</div>
<div style="height:30mm"></div>
<div class="nt why"><b class="h">왜 그럴까?</b><br>$(x-\\alpha)(x-\\beta)<0$은 두 수의 곱이 음수 → 부호가 <b>서로 다르다</b>.<br>$x-\\alpha>0$, $x-\\beta<0$인 곳은 <b>두 근 사이</b>뿐!</div>
<div class="nt"><b class="h">TIP</b><br>등호(≤, ≥)가 있으면 두 근도 해에 <b>포함</b>된다.</div>
</div></div></div>"""

K2 = CSS + CSS2 + f"""<div class="pr"><div class="two"><div class="main">
<div class="sec"><div class="sh"><i>01-3</i><b>판별식과 이차부등식의 해</b></div>
<div class="easy">$x^2$의 계수 $a>0$일 때, 이차방정식 $ax^2+bx+c=0$의 판별식 $D=b^2-4ac$의 부호에 따라 그래프와 $x$축의 위치가 정해진다.</div>
<table class="tb"><thead><tr><th style="width:23%"></th><th>$D>0$<br>{mini(0)}</th><th>$D=0$<br>{mini(1)}</th><th>$D<0$<br>{mini(2)}</th></tr></thead>
<tbody><tr><th>$ax^2+bx+c>0$</th><td>$x<\\alpha$ 또는 $x>\\beta$</td><td class="k">$x\\ne\\alpha$인 모든 실수</td><td>모든 실수</td></tr>
<tr><th>$ax^2+bx+c\\ge0$</th><td>$x\\le\\alpha$ 또는 $x\\ge\\beta$</td><td class="k">모든 실수</td><td>모든 실수</td></tr>
<tr><th>$ax^2+bx+c<0$</th><td>$\\alpha<x<\\beta$</td><td class="k">해는 없다.</td><td>해는 없다.</td></tr>
<tr><th>$ax^2+bx+c\\le0$</th><td>$\\alpha\\le x\\le\\beta$</td><td class="k">$x=\\alpha$</td><td>해는 없다.</td></tr></tbody></table>
<div class="exq"><span class="h">예제</span>다음 이차부등식을 푸시오. &nbsp;(1) $x^2-6x+9>0$ &nbsp;&nbsp;(2) $x^2+2x+5<0$ &nbsp;&nbsp;(3) $x^2-2x+2>0$</div>
{sol("(1) $(x-3)^2>0$ → <span class='ans'>$x\\ne3$인 모든 실수</span>")}
<div style="padding-left:12mm">(2) $\\dfrac{{D}}{{4}}=1-5<0$이므로 그래프가 $x$축보다 항상 위 → <span class="ans">해는 없다.</span><br>(3) $\\dfrac{{D}}{{4}}=1-2<0$ → <span class="ans">모든 실수</span></div></div>

<div class="sec"><div class="sh"><i>01-4</i><b>모든 실수 $x$에 대하여 성립하는 이차부등식</b></div>
<div class="cbx">모든 실수 $x$에 대하여 $ax^2+bx+c>0$ ⇔ <span class="hl">$a>0,\\ D<0$</span><br>모든 실수 $x$에 대하여 $ax^2+bx+c\\ge0$ ⇔ <span class="hl">$a>0,\\ D\\le0$</span></div>
<div class="exq"><span class="h">예제</span>모든 실수 $x$에 대하여 $x^2+kx+4>0$이 성립하도록 하는 실수 $k$의 값의 범위를 구하시오.</div>
{sol("$D=k^2-16<0$, $(k+4)(k-4)<0$ &nbsp;∴ <span class='ans'>$-4<k<4$</span>")}
</div></div>

<div class="side">
<div class="nt"><b class="h">참고</b><br>$D>0$: 서로 다른 두 실근<br>$D=0$: 중근<br>$D<0$: 서로 다른 두 허근</div>
<div class="nt"><b class="h">주의</b><br>$(x-3)^2>0$은 ‘모든 실수’가 아니라 <b>$x\\ne3$인 모든 실수</b>.</div>
<div style="height:22mm"></div>
<div class="nt why"><b class="h">왜 그럴까?</b><br>$ax^2+bx+c=a\\left(x+\\frac{{b}}{{2a}}\\right)^2-\\frac{{D}}{{4a}}$<br>꼭짓점의 높이가 $-\\frac{{D}}{{4a}}$ → $a>0,\\ D<0$이면 꼭짓점이 $x$축보다 위에 있어서 그래프 전체가 위!</div>
<div class="nt"><b class="h">주의</b><br>$x^2$의 계수에 문자가 있으면 (계수)$=0$인 경우부터 확인한다.</div>
</div></div></div>"""

K3 = CSS + CSS2 + f"""<div class="pr"><div class="two"><div class="main">
<div class="sec"><div class="sh"><i>01-5</i><b>연립이차부등식</b></div>
<div class="easy">두 개 이상의 부등식을 한 쌍으로 묶어 놓은 것을 <b>연립부등식</b>이라 하고, 그중 차수가 가장 높은 부등식이 이차부등식인 것을 <span class="hl">연립이차부등식</span>이라 한다.</div>
<div class="cbx"><b>푸는 순서</b> ① 각 부등식의 해를 구한다. ② 수직선 위에 함께 나타낸다. ③ <b>공통부분</b>을 구한다.</div>
<div class="exq"><span class="h">예제</span>연립부등식 $\\begin{{cases}}x^2-4x-5<0\\\\x^2-3x\\ge0\\end{{cases}}$을 푸시오.</div>
{sol("$x^2-4x-5<0$에서 $(x+1)(x-5)<0$ → $-1<x<5$ &nbsp;⋯⋯ ①")}
<div style="padding-left:12mm">$x^2-3x\\ge0$에서 $x(x-3)\\ge0$ → $x\\le0$ 또는 $x\\ge3$ &nbsp;⋯⋯ ②</div>
<div style="margin:1.6mm 0">{numline()}</div>
<div style="padding-left:12mm">①, ②의 공통부분 &nbsp;∴ <span class="ans">$-1<x\\le0$ 또는 $3\\le x<5$</span></div></div>

<div class="sec"><div class="sh"><i>개념 확인</i><b>배운 개념을 바로 확인해 보자</b></div>
<div class="chk" style="grid-template-columns:1fr 1fr"><div><b class="n">01</b>$x^2-9\\le0$을 푸시오.</div><div><b class="n">02</b>$x^2+4x+4>0$을 푸시오.</div>
<div><b class="n">03</b>$x^2-x+1<0$을 푸시오.</div><div><b class="n">04</b>$\\begin{{cases}}x^2-1>0\\\\x^2-4x\\le0\\end{{cases}}$을 푸시오.</div></div>
<div class="ref">정답 — 01 $-3\\le x\\le3$ · 02 $x\\ne-2$인 모든 실수 · 03 해는 없다 · 04 $1<x\\le4$ │ 단원 들어가기: $-5t^2+15t+2>12$ → $t^2-3t+2<0$ → 1초 후부터 2초 후까지</div></div>
</div>
<div class="side">
<div class="nt"><b class="h">참고</b><br>수직선에서 <b>●</b>는 그 점을 포함, <b>○</b>는 포함하지 않음을 뜻한다.</div>
<div style="height:40mm"></div>
<div class="nt why"><b class="h">왜 그럴까?</b><br>연립부등식의 해는 <b>두 부등식을 동시에</b> 만족해야 하므로 겹치는 부분(공통부분)만 남는다.</div>
<div class="nt"><b class="h">TIP</b><br>정수 해의 개수를 묻는 문제는 끝점의 ●○에서 가장 많이 틀린다.</div>
</div></div></div>"""

# ───── 단원 도입 쪽 (사진 + 궁금증 하나 + 배울 것) ─────
def opener(img):
    return CSS + f"""<style>
.opx .oph{{position:relative;border-radius:10px;overflow:hidden;height:128mm;background:#eee url({img}) center/cover}}
.opx .oph .ott{{position:absolute;left:6mm;bottom:6mm;color:#0B2545;background:rgba(255,255,255,.88);border-radius:8px;padding:2.4mm 5mm}}
.opx .oph .ott small{{display:block;font-size:8.6pt;font-weight:900;color:var(--c2);letter-spacing:.1em}}
.opx .oph .ott b{{font-family:'Noto Sans CJK KR';font-weight:900;font-size:22pt;line-height:1.2}}
.opx .oq{{margin:5mm 0 4mm;border-left:4px solid var(--c2);background:#FFF7F0;border-radius:0 10px 10px 0;padding:3.4mm 5mm;font-size:10.6pt;line-height:1.85}}
.opx .oq b.oh{{display:block;font-size:9pt;color:var(--c2);font-weight:900;letter-spacing:.06em}}
.opx .otoc{{display:grid;grid-template-columns:repeat(5,1fr);gap:2.4mm;margin-top:2mm}}
.opx .otoc div{{border:1.3px solid #D5DCE6;border-radius:8px;padding:2.2mm 2.4mm;font-size:9pt;line-height:1.45;background:#fff}}
.opx .otoc i{{font-style:normal;display:block;font-weight:900;color:var(--c1);font-size:8.4pt}}
.opx .oln{{display:grid;grid-template-columns:1fr auto 1fr auto 1fr;gap:2mm;align-items:center;margin-top:5mm;font-size:9pt;text-align:center}}
.opx .oln span{{background:var(--t);border-radius:99px;padding:1.4mm 2mm}}.opx .oln span.on{{background:var(--c1);color:#fff;font-weight:900}}
</style><div class="pr opx">
<div class="oph"><div class="ott"><small>공통수학1 · Ⅱ. 방정식과 부등식</small><b>이차부등식</b></div></div>
<div class="oq"><b class="oh">이 단원을 마치면 풀 수 있어요</b>던진 농구공의 $t$초 후 높이가 $h=-5t^2+15t+2\\,(\\text{{m}})$일 때,<br>공이 <b>12 m보다 높이</b> 떠 있는 것은 몇 초 후부터 몇 초 후까지일까?</div>
<div style="font-weight:900;color:var(--d);font-size:10.6pt">이 단원에서 배울 것</div>
<div class="otoc"><div><i>01-1</i>이차부등식이란?</div><div><i>01-2</i>해와 그래프</div><div><i>01-3</i>판별식과 해</div><div><i>01-4</i>항상 성립하는 부등식</div><div><i>01-5</i>연립이차부등식</div></div>
<div class="oln"><span>이차방정식 · 판별식</span>→<span>이차함수의 그래프</span>→<span class="on">이차부등식</span></div>
</div>"""

import base64 as _b64, pathlib as _pl
OPEN = opener("data:image/jpeg;base64," + _b64.b64encode(_pl.Path("/home/claude/tbook/assets/opener_ball.jpg").read_bytes()).decode())

# ───── 선생님 1분 사용 안내 (맛보기·선생님용에만) ─────
GUIDE = CSS + """<style>
.gd .lead{font-size:10.6pt;line-height:1.8;margin-bottom:4mm}
.gd .flow{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm;margin-bottom:4.4mm}
.gd .fl{border:1.4px solid var(--c1);border-radius:10px;overflow:hidden}
.gd .fl b{display:block;background:var(--c1);color:#fff;padding:1.4mm 3mm;font-size:10pt}
.gd .fl div{padding:2.2mm 3mm;font-size:9.4pt;line-height:1.7}
.gd .fl small{color:#6B7280}
.gd table{width:100%;border-collapse:collapse;font-size:9.6pt;margin-bottom:4.4mm}
.gd th,.gd td{border-bottom:1px solid #E5E7EB;padding:1.8mm 2mm;text-align:left;vertical-align:top}
.gd th{width:30%;color:var(--d);background:var(--t)}
.gd .lv{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm}
.gd .lv div{background:#F7F9FC;border-radius:8px;padding:2.2mm 3mm;font-size:9.2pt;line-height:1.6}
.gd .lv b{display:block;color:var(--c2)}
.gd .gft{margin-top:4.4mm;border-radius:10px;background:#FFF7F0;padding:2.6mm 4mm;font-size:9.4pt;line-height:1.7}
</style><div class="pr gd">
<div class="lead"><b>개념원리·쎈과 같은 순서(개념 → 예제 → 확인 → 유형 → 실전)</b>라서 따로 익히실 것 없이 평소 수업 그대로 쓰시면 됩니다.<br>이 한 장만 보시면 바로 수업하실 수 있어요.</div>
<div style="font-weight:900;color:var(--d);margin-bottom:1.6mm">수업 흐름 (3회차 예시)</div>
<div class="flow">
<div class="fl"><b>1회차 · 개념</b><div>단원 들어가기 → 개념원리 이해 01-1~01-5 → 개념 확인<br><small>숙제: 필수 예제 확인체크</small></div></div>
<div class="fl"><b>2회차 · 예제·기본</b><div>필수 예제 01~03 → 기본 다지기 16문제<br><small>숙제: 대표 유형 01~05</small></div></div>
<div class="fl"><b>3회차 · 실전</b><div>실전·서술형·BOSS → 스스로 점검·오답 노트<br><small>숙제: 틀린 문제 다시 풀기</small></div></div></div>
<table>
<tr><th>개념 상자(파란 바탕)</th><td>그대로 판서하시면 되는 핵심 정리입니다.</td></tr>
<tr><th>오른쪽 ‘왜 그럴까?’</th><td>학생이 “왜요?” 할 때 1분 설명용 멘트입니다. 외우게 하지 않고 이해시키는 부분이에요.</td></tr>
<tr><th>예제 바로 아래 풀이</th><td>개념 직후 바로 확인하는 쉬운 예제입니다. 학생 스스로 읽어도 이해되게 썼어요.</td></tr>
<tr><th>정답 위치</th><td>각 쪽 맨 아래 작은 글씨(확인 문제) · 책 뒤 ‘정답과 해설’(유형·실전, 오답 함정·서술형 채점 기준 포함)</td></tr>
<tr><th>학생용 / 선생님용</th><td>학생용 파일에는 정답과 이 안내가 빠져 있습니다. 바로 인쇄해 나눠 주시면 돼요.</td></tr></table>
<div style="font-weight:900;color:var(--d);margin-bottom:1.6mm">수준별로 이렇게 쓰세요</div>
<div class="lv"><div><b>기초반</b>개념원리 이해 + 개념 확인 + 기본 다지기 위주</div><div><b>기본반</b>필수 예제 + 대표 유형 전체 + 실전 일부</div><div><b>심화반</b>실전 · 서술형 · BOSS 집중, 개념은 ‘왜 그럴까?’로 빠르게</div></div>
<div class="gft">📩 학교·교과서 출판사·시험 범위를 알려 주시면 <b>그 범위에 맞춘 챕터</b>로 만들어 드려요. 학원 이름·로고·문구도 원하시는 대로 바꿔 드립니다.</div>
</div>"""
