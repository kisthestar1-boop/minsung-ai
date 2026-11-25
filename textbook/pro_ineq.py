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
