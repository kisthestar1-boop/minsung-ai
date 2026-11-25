# 고1 이차부등식 — 강의 노트형 개념 2쪽 (선생님이 판서하듯 설명하고, 학생은 빈칸을 채우는 구조)
PK, BL, INK, MU = "#E0457B", "#1E5BA8", "#123A6B", "#6B7280"

def para(f, roots, x0, x1, w=330, h=190, ymin=-3, ymax=6, shade="below", labels=True, ticks=None, pt=None):
    """f: 함수, roots: x절편 목록. shade: below/above/none. 반환: svg 문자열"""
    sx = lambda x: 20 + (x - x0) / (x1 - x0) * (w - 40)
    sy = lambda y: 14 + (ymax - y) / (ymax - ymin) * (h - 40)
    n = 120; pts = []
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n; y = f(x)
        if ymin - 1 <= y <= ymax + 1: pts.append(f"{sx(x):.1f},{sy(max(min(y, ymax + .6), ymin - .6)):.1f}")
    ax = sy(0); s = [f'<svg viewBox="0 0 {w} {h}" width="100%" style="display:block">',
         f'<line x1="10" y1="{ax:.1f}" x2="{w-8}" y2="{ax:.1f}" stroke="#334" stroke-width="1.4"/><text x="{w-12}" y="{ax-6:.1f}" font-size="12" fill="#334">x</text>']
    if shade != "none" and len(roots) == 2:
        a, b = roots
        s.append(f'<line x1="{sx(a):.1f}" y1="{ax:.1f}" x2="{sx(b):.1f}" y2="{ax:.1f}" stroke="{PK}" stroke-width="7" stroke-linecap="round" opacity=".85"/>')
        s.append(f'<line x1="14" y1="{ax:.1f}" x2="{sx(a):.1f}" y2="{ax:.1f}" stroke="{BL}" stroke-width="7" opacity=".55"/>')
        s.append(f'<line x1="{sx(b):.1f}" y1="{ax:.1f}" x2="{w-14}" y2="{ax:.1f}" stroke="{BL}" stroke-width="7" opacity=".55"/>')
    s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{INK}" stroke-width="2.4"/>')
    for r in roots:
        s.append(f'<circle cx="{sx(r):.1f}" cy="{ax:.1f}" r="4.5" fill="#fff" stroke="{INK}" stroke-width="2"/>')
    for x, t in (ticks or []):
        s.append(f'<text x="{sx(x):.1f}" y="{ax+18:.1f}" font-size="13" text-anchor="middle" fill="{INK}" font-weight="700">{t}</text>')
    if labels and len(roots) == 2:
        a, b = roots; m = (a + b) / 2
        s.append(f'<text x="{sx(m):.1f}" y="{h-4}" font-size="12.5" text-anchor="middle" fill="{PK}" font-weight="800">y&lt;0 (x축 아래)</text>')
        s.append(f'<text x="{sx(x0)+34:.1f}" y="{ax-10:.1f}" font-size="12.5" text-anchor="middle" fill="{BL}" font-weight="800">y&gt;0</text>')
        s.append(f'<text x="{sx(x1)-34:.1f}" y="{ax-10:.1f}" font-size="12.5" text-anchor="middle" fill="{BL}" font-weight="800">y&gt;0</text>')
    s.append("</svg>"); return "".join(s)

def mini(kind):
    w, h = 150, 74; ax = 50
    if kind == 0: path = "M18 6 Q75 112 132 6"; dots = [52, 98]
    elif kind == 1: path = "M22 4 Q75 96 128 4"; dots = [75]
    else: path = "M24 2 Q75 70 126 2"; dots = []
    s = f'<svg viewBox="0 0 {w} {h}" width="100%" style="display:block"><line x1="6" y1="{ax}" x2="{w-6}" y2="{ax}" stroke="#334" stroke-width="1.2"/>'
    s += f'<path d="{path}" fill="none" stroke="{INK}" stroke-width="2.2"/>'
    lab = {0: ["α", "β"], 1: ["α"], 2: []}[kind]
    for d, l in zip(dots, lab):
        s += f'<circle cx="{d}" cy="{ax}" r="3.6" fill="#fff" stroke="{INK}" stroke-width="1.8"/><text x="{d}" y="{ax+16}" font-size="12" text-anchor="middle" font-weight="700" fill="{INK}">{l}</text>'
    return s + "</svg>"

def numline():
    # x²-4x-5<0 → -1<x<5 ,  x²-3x≥0 → x≤0 또는 x≥3  → 공통 -1<x≤0, 3≤x<5
    w = 520; X = lambda v: 40 + (v + 3) * 55
    s = [f'<svg viewBox="0 0 {w} 132" width="100%" style="display:block">']
    s.append(f'<rect x="{X(-1)}" y="22" width="{X(0)-X(-1)}" height="72" fill="#FFE680" opacity=".75"/><rect x="{X(3)}" y="22" width="{X(5)-X(3)}" height="72" fill="#FFE680" opacity=".75"/>')
    s.append(f'<line x1="14" y1="100" x2="{w-10}" y2="100" stroke="#334" stroke-width="1.4"/>')
    for v in range(-3, 6):
        s.append(f'<line x1="{X(v)}" y1="96" x2="{X(v)}" y2="104" stroke="#334"/><text x="{X(v)}" y="120" font-size="13" text-anchor="middle" fill="{INK}" font-weight="700">{v}</text>')
    # ① 파랑 -1<x<5 (높이 40)
    s.append(f'<path d="M{X(-1)} 100 V40 H{X(5)} V100" fill="none" stroke="{BL}" stroke-width="2.4"/>')
    s.append(f'<circle cx="{X(-1)}" cy="100" r="5" fill="#fff" stroke="{BL}" stroke-width="2.2"/><circle cx="{X(5)}" cy="100" r="5" fill="#fff" stroke="{BL}" stroke-width="2.2"/>')
    s.append(f'<text x="{X(2)}" y="34" font-size="12.5" text-anchor="middle" fill="{BL}" font-weight="800">① −1＜x＜5</text>')
    # ② 분홍 x≤0, x≥3 (높이 64)
    s.append(f'<path d="M14 64 H{X(0)} V100" fill="none" stroke="{PK}" stroke-width="2.4"/><path d="M{X(3)} 100 V64 H{w-10}" fill="none" stroke="{PK}" stroke-width="2.4"/>')
    s.append(f'<circle cx="{X(0)}" cy="100" r="5" fill="{PK}"/><circle cx="{X(3)}" cy="100" r="5" fill="{PK}"/>')
    s.append(f'<text x="{X(-2.4)}" y="58" font-size="12.5" text-anchor="middle" fill="{PK}" font-weight="800">② x≤0</text><text x="{X(4.55)}" y="58" font-size="12.5" text-anchor="middle" fill="{PK}" font-weight="800">② x≥3</text>')
    s.append("</svg>"); return "".join(s)

def floating():
    return para(lambda x: 0.6 * (x - 1) ** 2 + 1.2, [], -2, 4, w=230, h=150, ymin=-1.5, ymax=6, shade="none", labels=False) \
        .replace("</svg>", f'<text x="115" y="132" font-size="12.5" text-anchor="middle" fill="{BL}" font-weight="800">x축과 만나지 않고 항상 위!</text></svg>')

CSS = f"""<style>
.ln{{font-size:9.6pt;line-height:1.62;color:#1f2937}}
.ln .row{{display:flex;gap:4mm;align-items:stretch}}
.ln .bx{{border:1.3px solid var(--ln);border-radius:10px;background:#fff;break-inside:avoid;margin-bottom:3.2mm;overflow:hidden}}
.ln .bh{{display:flex;align-items:center;gap:2.5mm;background:var(--t);padding:1.8mm 4mm;font-family:'Noto Sans CJK KR';font-weight:900;color:var(--d);font-size:10.8pt}}
.ln .bh i{{font-style:normal;background:var(--c1);color:#fff;border-radius:6px;padding:0 2.2mm;font-size:9pt}}
.ln .bh small{{margin-left:auto;font-weight:700;color:{MU};font-size:8.2pt}}
.ln .bb{{padding:2.6mm 4mm}}
.ln .fig{{flex:1.05;padding:1mm 0}}
.ln .note{{flex:1;display:flex;flex-direction:column;gap:1.6mm}}
.ln .eq{{background:#F7F9FC;border-radius:8px;padding:1.6mm 3mm;font-size:9.8pt}}
.ln .eq b{{color:{PK}}}
.ln .stp{{display:flex;gap:2mm;align-items:baseline}}
.ln .stp em{{font-style:normal;flex:none;width:5.2mm;height:5.2mm;border-radius:50%;background:var(--c2);color:#fff;font-size:8pt;font-weight:900;display:inline-grid;place-items:center;transform:translateY(-.3mm)}}
.ln .tb{{width:100%;border-collapse:collapse;font-size:9.4pt;text-align:center}}
.ln .tb th,.ln .tb td{{border:1px solid var(--ln);padding:1.3mm 1.5mm}}
.ln .tb thead th{{background:#fff;font-weight:700;color:{INK}}}
.ln .tb tbody th{{background:var(--t);color:var(--d);font-family:'Noto Sans CJK KR';white-space:nowrap}}
.ln .tb .hot{{background:#FFF6CC;font-weight:700}}
.ln .tb .no{{color:{PK};font-weight:800}}
.ln .pt{{position:relative;background:#FFF0F5;border-radius:12px 12px 12px 3px;padding:1.8mm 3.4mm;font-size:9.2pt}}
.ln .pt b{{color:{PK}}}
.ln .pt:before{{content:"선생님 판서 포인트";display:block;font-size:7.6pt;font-weight:900;color:{PK};letter-spacing:.04em}}
.ln .trap{{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm}}
.ln .tr{{border-radius:9px;padding:2.2mm 3mm;background:#fff;border:1.3px solid var(--ln);font-size:8.9pt;break-inside:avoid}}
.ln .tr .x{{color:#C0392B;font-weight:800;display:block}}.ln .tr .o{{color:#11845B;font-weight:800;display:block;margin-top:1mm}}
.ln .tr b.h{{display:block;font-family:'Noto Sans CJK KR';color:var(--d);font-size:9.4pt;margin-bottom:1mm}}
.ln .why{{font-size:8.6pt;color:{MU}}}
.ln .key{{text-align:right;font-size:7.4pt;color:#9CA3AF;margin-top:1mm}}
.ln .blank{{min-width:15mm}}
.ln .mk{{background:linear-gradient(transparent 55%,var(--hl) 55%)}}
.ln .xp{{margin-left:auto;flex:none;background:linear-gradient(135deg,#FFD84D,#FFB020);color:#5A3B00;border-radius:99px;padding:.3mm 2.6mm;font-size:8pt;font-weight:900;box-shadow:0 1px 0 #D18E00}}
.ln .ch{{display:inline-block;background:#123A6B;color:#FFE680;border-radius:6px;padding:0 2mm;font-size:8pt;font-weight:900;margin-right:1.5mm}}
.ln .badge{{display:flex;align-items:center;gap:3mm;border:2px dashed #FFB020;background:#FFFBEA;border-radius:10px;padding:1.6mm 4mm;font-size:9pt;margin-top:2mm}}
.ln .badge .md{{flex:none;width:10mm;height:10mm;border-radius:50%;background:radial-gradient(circle at 35% 30%,#FFF3B0,#FFC53D 60%,#E09B00);display:grid;place-items:center;font-size:13pt;box-shadow:0 1px 0 #B67C00}}
.ln .badge .st{{margin-left:auto;display:flex;gap:1.6mm}}.ln .badge .st i{{width:6mm;height:6mm;border-radius:50%;border:1.5px solid #E0B040;display:inline-block}}
.ln .lvbar{{display:flex;align-items:center;gap:3mm;background:#123A6B;color:#fff;border-radius:10px;padding:1.6mm 4mm;font-size:8.8pt;font-weight:700;margin-top:2mm}}
.ln .lvbar .g{{flex:1;height:3mm;border-radius:9px;background:rgba(255,255,255,.18);overflow:hidden}}.ln .lvbar .g i{{display:block;height:100%;width:35%;background:linear-gradient(90deg,#FFE680,#FFB020)}}
.ln .lvbar b{{color:#FFE680}}
</style>"""

B = "<span class=blank></span>"

PAGE1 = CSS + f"""<div class="ln">
<div class="bx"><div class="bh"><i>강의 1</i>이차부등식은 ‘그래프가 x축의 어디에 있나’를 묻는 문제<span class="xp">⭐ +10 XP</span></div>
<div class="bb row"><div class="fig">{para(lambda x:(x-1)*(x-4)*0.9,[1,4],-0.6,5.6,h=176,ymin=-3.4,ymax=5.2,ticks=[(1,"1"),(4,"4")])}
<div style="text-align:center;font-size:9pt;font-weight:700;color:{INK}">$y=x^2-5x+4=(x-1)(x-4)$</div></div>
<div class="note">
<div class="eq"><span class="ch">⏱ 3초 컷</span>$x^2-5x+4<0$ ⇔ 그래프가 x축 {B} ⇔ <b>$1<x<4$</b></div>
<div class="eq">$x^2-5x+4>0$ ⇔ 그래프가 x축 {B} ⇔ {B}</div>
<div class="stp"><em>1</em><span>우변을 0으로 만들고, $x^2$ 계수를 <b>양수</b>로 맞춘다.</span></div>
<div class="stp"><em>2</em><span>$=0$으로 놓고 두 근 $\\alpha,\\beta$를 구한다. (인수분해·근의 공식)</span></div>
<div class="stp"><em>3</em><span>그래프를 그려 <b>아래면 ‘사이’</b>, <b>위면 ‘바깥’</b>을 읽는다.</span></div>
<div class="pt">외우지 말고 <b>매번 그려서 읽기!</b> ＜0이면 두 근 <b>사이</b>, ＞0이면 두 근 <b>바깥</b>.</div>
</div></div></div>

<div class="bx"><div class="bh"><i>강의 2</i>판별식으로 한눈에 — 이차부등식의 해 총정리 <span style="font-weight:700;font-size:9pt">($a>0$)</span><span class="xp">⭐ +10 XP · 시험 단골</span></div>
<div class="bb"><table class="tb"><thead><tr><th style="width:24%">$D=b^2-4ac$</th><th>$D>0$<br>{mini(0)}서로 다른 두 근 $\\alpha<\\beta$</th><th>$D=0$<br>{mini(1)}중근 $\\alpha$ (x축에 접함)</th><th>$D<0$<br>{mini(2)}x축과 만나지 않음</th></tr></thead>
<tbody><tr><th>$ax^2+bx+c>0$</th><td>$x<\\alpha$ 또는 $x>\\beta$</td><td class="hot">$x\\ne\\alpha$인 모든 실수</td><td>모든 실수</td></tr>
<tr><th>$ax^2+bx+c\\ge0$</th><td>$x\\le\\alpha$ 또는 $x\\ge\\beta$</td><td class="hot">모든 실수</td><td>모든 실수</td></tr>
<tr><th>$ax^2+bx+c<0$</th><td>$\\alpha<x<\\beta$</td><td class="hot no">해는 없다</td><td class="no">해는 없다</td></tr>
<tr><th>$ax^2+bx+c\\le0$</th><td>$\\alpha\\le x\\le\\beta$</td><td class="hot">$x=\\alpha$ (하나뿐)</td><td class="no">해는 없다</td></tr></tbody></table>
<div class="row" style="margin-top:2.4mm;gap:3mm"><div class="pt" style="flex:1.2">노란 칸(중근)이 제일 많이 틀려요. $(x-2)^2>0$은 ‘모든 실수’가 아니라 <b>$x\\ne2$인 모든 실수</b>!</div>
<div class="eq" style="flex:1"><b>$a<0$일 때는?</b> 양변에 $-1$을 곱해 $a>0$으로 바꾸고 <b>부등호 방향도 뒤집기</b>.<br>예) $-x^2+x+6>0$ → $x^2-x-6<0$ → {B}</div></div>
</div></div>

<div class="row" style="gap:2.4mm;align-items:center;margin-bottom:2mm;font-size:9.2pt">
<span style="font-weight:900;color:var(--d);white-space:nowrap">방정식은 ‘점’,<br>부등식은 ‘구간’</span>
<div class="eq" style="flex:1;text-align:center">$x^2-5x+4=0$<br><b style="color:#123A6B">$x=1,\ 4$</b></div>
<div class="eq" style="flex:1;text-align:center">$x^2-5x+4<0$<br><b>$1<x<4$</b></div>
<div class="eq" style="flex:1;text-align:center">$x^2-5x+4>0$<br><b style="color:#1E5BA8">$x<1$ 또는 $x>4$</b></div></div>
<div class="key">빈칸 정답 — 아래 · 위 · $x<1$ 또는 $x>4$ · $-2<x<3$</div>
</div>"""

PAGE2 = CSS + f"""<div class="ln">
<div class="row">
<div class="bx" style="flex:1"><div class="bh"><i>강의 3</i>해가 주어지면 ‘거꾸로’<span class="xp">⭐ +10</span></div>
<div class="bb"><div class="eq" style="margin-bottom:1.6mm">해가 $\\alpha<x<\\beta$ ⇔ $(x-\\alpha)(x-\\beta)<0$<br>해가 $x<\\alpha$ 또는 $x>\\beta$ ⇔ $(x-\\alpha)(x-\\beta)>0$</div>
<div style="font-weight:800;color:{INK};margin-bottom:.6mm">예) $x^2+ax+b<0$의 해가 $-1<x<3$일 때 $a,b$</div>
<div class="stp"><em>1</em><span>해 → 식: $(x+1)(x-3)<0$</span></div>
<div class="stp"><em>2</em><span>전개: $x^2-2x-3<0$</span></div>
<div class="stp"><em>3</em><span>계수 비교: $a=$ {B}, $b=$ {B}</span></div>
<div class="pt" style="margin-top:1.6mm">$x^2$ 계수가 <b>음수</b>로 주어지면 부등호가 <b>반대</b>로 바뀌는 것까지 확인!</div></div></div>
<div class="bx" style="flex:1"><div class="bh"><i>강의 4</i>‘모든 실수 x’ = 항상 성립<span class="xp">⭐ +10</span></div>
<div class="bb"><div class="row" style="gap:2mm;align-items:center"><div style="flex:1">{floating()}</div>
<div style="flex:1.1"><div class="eq">$ax^2+bx+c>0$ 항상 ⇔ <b>$a>0,\\ D<0$</b></div><div class="eq" style="margin-top:1.2mm">$ax^2+bx+c\\ge0$ 항상 ⇔ <b>$a>0,\\ D\\le0$</b></div></div></div>
<div style="font-weight:800;color:{INK};margin:1.2mm 0 .4mm">예) $x^2-2kx+k+2>0$이 항상 성립</div>
<div>$\\dfrac{{D}}{{4}}=k^2-k-2<0$ → $(k+1)(k-2)<0$ → {B}</div>
<div class="pt" style="margin-top:1.4mm">$x^2$ 계수에 문자가 있으면 <b>$a=0$인 경우부터</b> 따로 확인!</div></div></div>
</div>

<div class="bx"><div class="bh"><i>강의 5</i>연립이차부등식 = 수직선 위의 공통부분<small style="margin-left:auto">●포함 · ○불포함</small><span class="xp" style="margin-left:2mm">⭐ +10 XP</span></div>
<div class="bb row" style="align-items:center"><div style="flex:1.45">{numline()}</div>
<div class="note"><div class="eq">① $x^2-4x-5<0$ → $-1<x<5$</div><div class="eq">② $x^2-3x\\ge0$ → $x\\le0$ 또는 $x\\ge3$</div>
<div class="eq" style="background:#FFF6CC">공통부분: <b>$-1<x\\le0$ 또는 $3\\le x<5$</b><br>정수 해: {B} → 모두 {B}개</div></div></div></div>

<div class="bx"><div class="bh"><i>함정 피하기</i>학교 시험에서 점수가 새는 곳 TOP 3<span class="xp">⭐ 3개 다 피하면 +15 XP</span></div>
<div class="bb trap">
<div class="tr"><b class="h">① 끝점 포함</b><span class="x">✕ $x^2-4\\le0$ → $-2<x<2$</span><span class="o">○ $-2\\le x\\le2$</span><span class="why">등호가 있으면 끝점 ●</span></div>
<div class="tr"><b class="h">② 중근</b><span class="x">✕ $(x-3)^2>0$ → 모든 실수</span><span class="o">○ $x\\ne3$인 모든 실수</span><span class="why">$x=3$이면 $0>0$ 거짓</span></div>
<div class="tr"><b class="h">③ 음수 계수</b><span class="x">✕ $-x^2+1<0$ → $-1<x<1$</span><span class="o">○ $x<-1$ 또는 $x>1$</span><span class="why">$-1$ 곱하면 부등호도 뒤집기</span></div>
</div></div>
<div class="bx"><div class="bh"><i>미니 퀘스트</i>그래프를 그려서 빈칸 채우기 · 2분<span class="xp">🏅 4개 다 맞히면 배지!</span></div>
<div class="bb" style="display:grid;grid-template-columns:1fr 1fr;gap:1.6mm 6mm">
<div>① $x^2-9\\le0$ ⇔ {B}</div><div>② $x^2+2x+1>0$ ⇔ {B}</div>
<div>③ $x^2-6x+10<0$ ⇔ {B}</div><div>④ $-x^2+4x\\ge0$ ⇔ {B}</div></div></div>
<div class="lvbar"><span>🎮 개념 STAGE</span><div class="g"><i></i></div><span>강의 5개 + 퀘스트 = <b>최대 65 XP</b> → 다음은 <b>대표 유형 LEVEL 1</b> ▶</span></div>
<div class="key">빈칸 정답 — 강의3: $a=-2$, $b=-3$ │ 강의4: $-1<k<2$ │ 강의5: $0, 3, 4$ → 3개 │ 바로 확인: ① $-3\\le x\\le3$ ② $x\\ne-1$인 모든 실수 ③ 해는 없다 ④ $0\\le x\\le4$</div>
</div>"""
