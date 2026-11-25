# 고1 이차부등식 — 연구 기반 '1회차 = 펼친 2쪽' 시안
# 원리: 떠올리기 → 궁금증(예상) → 실험 → 아하 → 그림 옆 정리 │ 풀이 예제 → 빈칸 따라 하기 → 혼자 풀기 → 쉬운 마무리 + 내 말로 한 줄
from concept_ineq import para, face, PK, BL, INK, MU

B = "<span class=blank></span>"
CSS = """<style>
.ls{font-size:10pt;line-height:1.7;color:#1f2937}
.ls .sec{margin:0 0 4.2mm}
.ls .lb{display:flex;align-items:baseline;gap:2.4mm;margin-bottom:1.6mm}
.ls .lb b{font-family:'Noto Sans CJK KR';font-weight:900;color:var(--d);font-size:11.2pt}
.ls .lb span{font-size:8.4pt;font-weight:800;color:var(--c2);letter-spacing:.06em}
.ls .lb small{margin-left:auto;font-size:8pt;color:#9CA3AF}
.ls .rule{border-left:3px solid var(--c1);padding-left:4mm}
.ls .warm{background:#F6F8FB;border-radius:8px;padding:2mm 4mm;display:grid;grid-template-columns:1fr 1fr;gap:1mm 6mm;font-size:9.6pt}
.ls .q{font-size:11pt;font-weight:700;color:#111827;margin:.6mm 0 1.4mm}
.ls .pick{display:flex;gap:5mm;font-size:9.6pt}.ls .pick i{font-style:normal;display:inline-flex;align-items:center;gap:1.4mm}
.ls .pick i:before{content:"";width:3.8mm;height:3.8mm;border:1.4px solid #6B7280;border-radius:50%}
.ls table.lab{width:100%;border-collapse:collapse;font-size:9.8pt;text-align:center;margin-top:2mm}
.ls .lab th,.ls .lab td{border-bottom:1px solid #E5E7EB;padding:1.2mm 1mm}
.ls .lab thead th{color:#6B7280;font-weight:700;font-size:9pt;border-bottom:1.6px solid #9CA3AF}
.ls .lab tbody th{text-align:left;color:var(--d)}
.ls .lab .sg{font-weight:900}
.ls .aha{position:relative;background:#FFF8D6;border-radius:10px;padding:2.4mm 4mm 2.4mm 13mm;font-size:10.2pt;margin-top:3mm}
.ls .aha:before{content:"💡";position:absolute;left:4mm;top:2.2mm;font-size:14pt}
.ls .aha b{background:linear-gradient(transparent 60%,#FFD84D 60%)}
.ls .key{display:grid;grid-template-columns:1.15fr 1fr;gap:5mm;align-items:center}
.ls .big{font-size:11.2pt;line-height:2}
.ls .big b{color:#C2335F}
.ls .tk{display:flex;gap:2.4mm;align-items:center;margin:0 0 2.4mm}
.ls .tk .bu{background:#FFF0F5;border-radius:3px 12px 12px 12px;padding:1.6mm 3.6mm;font-size:9.6pt}
.ls .wx{border:1.3px solid #D5DCE6;border-radius:10px;padding:3mm 4mm}
.ls .wx .wh{font-weight:900;color:var(--d);margin-bottom:1mm}
.ls .st{display:grid;grid-template-columns:6mm 1fr;gap:1mm 2mm;align-items:baseline;font-size:10pt}
.ls .st em{font-style:normal;width:5mm;height:5mm;border-radius:50%;background:var(--c1);color:#fff;font-size:8pt;font-weight:900;display:inline-grid;place-items:center}
.ls .fade em{background:#fff;color:var(--c1);border:1.4px solid var(--c1)}
.ls .tp{font-size:9pt;color:#4B5563;background:#F6F8FB;border-radius:8px;padding:1.4mm 3mm;margin-top:1.6mm}
.ls .two{display:grid;grid-template-columns:1fr 1fr;gap:5mm}
.ls .pb{border:1.3px solid #E5E7EB;border-radius:10px;padding:2.6mm 4mm;min-height:62mm}
.ls .pb .n{font-weight:900;color:var(--c1);margin-right:1.6mm}
.ls .end{display:grid;grid-template-columns:1fr 1.2fr;gap:5mm;align-items:stretch}
.ls .win{border:1.6px dashed #F2A100;border-radius:10px;padding:2.4mm 4mm;background:#FFFCF2}
.ls .mine{border-radius:10px;padding:2.4mm 4mm;background:#F0F6FF}
.ls .mine .ln{border-bottom:1.3px solid #9CB4D8;height:7mm}
.ls .prog{display:flex;align-items:center;gap:3mm;margin-top:3.6mm;font-size:8.6pt;color:#6B7280}
.ls .prog .d{display:flex;gap:1.6mm}.ls .prog .d i{width:4mm;height:4mm;border-radius:50%;border:1.4px solid #9CA3AF}.ls .prog .d i.on{background:var(--c1);border-color:var(--c1)}
.ls .blank{min-width:14mm}
</style>"""

def g1():
    return para(lambda x: (x - 1) * (x - 4) * 0.9, [1, 4], -0.6, 5.6, w=300, h=170, ymin=-3.2, ymax=5.2, ticks=[(1, "1"), (4, "4")])

def g2():
    # 2x²-x-3 ≤ 0 : -1 ≤ x ≤ 3/2 (등호 포함 → 색칠 점)
    s = para(lambda x: (2 * x - 3) * (x + 1) * 0.55, [-1, 1.5], -2.3, 2.8, w=220, h=120, ymin=-2.2, ymax=3.6, labels=False, ticks=[(-1, "−1"), (1.5, "3/2")])
    return s.replace('fill="#fff" stroke="#123A6B"', f'fill="{PK}" stroke="{PK}"')

L1A = CSS + f"""<div class="ls">
<div class="sec"><div class="lb"><span>WARM-UP</span><b>지난 시간 떠올리기</b><small>1분 · 기억나는 만큼만</small></div>
<div class="warm"><div>① $x^2-5x+4=0$의 두 근: {B}, {B}</div><div>② $y=x^2-5x+4$는 아래로 볼록? 위로 볼록? {B}</div></div></div>

<div class="sec"><div class="lb"><span>QUESTION</span><b>오늘의 궁금증</b></div>
<div class="tk">{face("s")}<div class="bu">방정식은 답이 ‘점’이었는데, 부등식은 답이 어떻게 생겼을까?</div></div>
<div class="q">$x^2-5x+4<0$을 만족하는 $x$는 어디에 있을까? 먼저 예상해 보세요.</div>
<div class="pick"><i>$x<1$</i><i>$1<x<4$</i><i>$x>4$</i><i>모르겠다</i></div></div>

<div class="sec rule"><div class="lb"><span>EXPERIMENT</span><b>직접 넣어 보기</b><small>계산기 없이</small></div>
<table class="lab"><thead><tr><th style="width:24%"></th><th>$x=0$</th><th>$x=2$</th><th>$x=3$</th><th>$x=5$</th></tr></thead>
<tbody><tr><th>$x-1$</th><td>$-1$</td><td>{B}</td><td>$2$</td><td>{B}</td></tr>
<tr><th>$x-4$</th><td>$-4$</td><td>{B}</td><td>$-1$</td><td>{B}</td></tr>
<tr><th>곱의 부호</th><td class="sg" style="color:{BL}">＋</td><td>{B}</td><td class="sg" style="color:{PK}">－</td><td>{B}</td></tr></tbody></table>
<div class="aha">곱이 음수가 되려면 두 수의 <b>부호가 달라야</b> 해요. $x-1$은 이미 양수인데 $x-4$는 아직 음수인 곳 — <b>1과 4 사이</b>!</div></div>

<div class="sec"><div class="lb"><span>KEY IDEA</span><b>그림 하나로 정리</b></div>
<div class="key"><div>{g1()}</div>
<div class="big">$x^2-5x+4<0$<br>⇔ 그래프가 x축 <b>아래</b><br>⇔ 두 근 <b>사이</b> : $1<x<4$<br><span style="font-size:9.6pt;color:#4B5563">＞0이면 x축 <b style="color:{BL}">위</b> ⇔ 두 근 <b style="color:{BL}">바깥</b></span></div></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:3mm;margin-top:3mm;text-align:center;font-size:9.8pt">
<div class="warm" style="display:block">$x^2-5x+4=0$<br><b style="color:#123A6B">$x=1,\ 4$</b><br><small style="color:#6B7280">방정식 → 점 두 개</small></div>
<div class="warm" style="display:block;background:#FFF0F5">$x^2-5x+4<0$<br><b style="color:#C2335F">$1<x<4$</b><br><small style="color:#6B7280">부등식 → 사이 구간</small></div>
<div class="warm" style="display:block;background:#EEF4FF">$x^2-5x+4>0$<br><b style="color:#1E5BA8">$x<1$ 또는 $x>4$</b><br><small style="color:#6B7280">부등식 → 바깥 구간</small></div></div></div>
</div>"""

L1B = CSS + f"""<div class="ls">
<div class="sec"><div class="lb"><span>EXAMPLE</span><b>풀이 예제 — 선생님과 함께</b></div>
<div class="wx"><div class="wh">$2x^2-x-3\\le0$을 풀어라.</div>
<div style="display:grid;grid-template-columns:1.25fr 1fr;gap:4mm;align-items:center"><div class="st">
<em>1</em><span>인수분해: $(2x-3)(x+1)\\le0$</span>
<em>2</em><span>두 근: $x=-1,\\ \\dfrac{{3}}{{2}}$</span>
<em>3</em><span>x축 <b>아래(또는 위에 닿음)</b> → 두 근 사이, 등호 있으니 끝점 ● 포함</span>
<span></span><span style="font-weight:900;color:#C2335F">∴ $-1\\le x\\le\\dfrac{{3}}{{2}}$</span></div>
<div>{g2()}</div></div></div></div>

<div class="sec"><div class="lb"><span>YOUR TURN</span><b>빈칸 따라 하기</b><small>예제와 똑같은 순서</small></div>
<div class="wx"><div class="wh">$x^2+2x-8>0$을 풀어라.</div><div class="st fade">
<em>1</em><span>인수분해: $(x+4)(x-2)>0$</span>
<em>2</em><span>두 근: $x=$ {B}, {B}</span>
<em>3</em><span>x축 {B} → 두 근 {B} → $x<$ {B} 또는 $x>$ {B}</span></div></div></div>

<div class="sec"><div class="lb"><span>ON YOUR OWN</span><b>혼자 풀기</b><small>순서 ①②③ 떠올리며</small></div>
<div class="two"><div class="pb"><span class="n">1</span>$x^2-x-6<0$</div>
<div class="pb"><span class="n">2</span>$-x^2+3x+10\\ge0$<div class="tp">$x^2$ 앞이 음수면? 양변에 $-1$을 곱하고 <b>부등호도 뒤집기</b></div></div></div></div>

<div class="end"><div class="win"><b style="color:#B7791F">✔ 기분 좋게 마무리</b><br>$x^2-9<0$ ⇔ {B}</div>
<div class="mine"><b style="color:{BL}">✎ 오늘 배운 것을 내 말로 한 줄</b><div class="ln"></div></div></div>
<div class="prog"><span>이차부등식</span><div class="d"><i class="on"></i><i></i><i></i><i></i></div><span>1회차 완료! 다음: 판별식으로 한눈에 보기</span></div>
<div style="text-align:right;font-size:7.4pt;color:#9CA3AF;margin-top:1mm">정답 — 떠올리기: 1, 4 · 아래로 볼록 │ 실험: x=2 → 1, −2, － · x=5 → 4, 1, ＋ │ 따라 하기: −4, 2 · 위 · 바깥 · −4, 2 │ 혼자: ① $-2<x<3$ ② $-2\\le x\\le5$ │ 마무리: $-3<x<3$</div>
</div>"""
