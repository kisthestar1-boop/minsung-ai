# 찰칵출판사 교재 공통 템플릿 엔진
# 학년·과목과 상관없이 같은 뼈대: 표지 → 학습 계획 → 개념 → 대표 유형 → Level 1·2·3 → 자기 평가·오답 노트 → 정답과 해설
# 사용: html = build(spec); pdf(html, "out.pdf")  (spec 형식은 아래 build() 참고)
import html as _h, json, re, subprocess, os, pathlib

KATEX = "/home/claude/textbook/node_modules/katex/dist"
NUM = "①②③④⑤"

THEMES = {  # c1 메인, c2 포인트, t 옅은 바탕, d 진한 글자
    "math":  dict(c1="#1E5BA8", c2="#F2683A", t="#EAF1FA", d="#123A6B", hl="#FFE680"),
    "elem":  dict(c1="#10997A", c2="#FF8A3D", t="#E6F6F0", d="#0B5C4A", hl="#FFE680"),
    "eng":   dict(c1="#4A3DB0", c2="#E5475F", t="#EEEDFB", d="#2C2470", hl="#FFE680"),
    "kor":   dict(c1="#8A3B12", c2="#2E8B57", t="#F8EFE8", d="#5A240A", hl="#FFE680"),
    "sci":   dict(c1="#0E7C86", c2="#E0A800", t="#E5F4F5", d="#0A5158", hl="#FFE680"),
}

CSS = r"""
@page{size:A4;margin:0}*{box-sizing:border-box;margin:0;padding:0}
:root{--c1:%(c1)s;--c2:%(c2)s;--t:%(t)s;--d:%(d)s;--hl:%(hl)s;--ln:#D5DCE6}
body{font-family:%(body)s;color:#1b1f24;font-size:%(fs)s;line-height:1.75;word-break:keep-all;-webkit-print-color-adjust:exact}
.sans,.h,.chip,.qn,.lvb,.tag,.ft,.hd{font-family:'Noto Sans CJK KR',sans-serif}
.pg{width:210mm;height:297mm;position:relative;page-break-after:always;overflow:hidden;background:#fff}
.pg.flow .body{display:flex;flex-direction:column}
.body{position:absolute;left:15mm;right:15mm;top:24mm;bottom:17mm;overflow:hidden}
/* 머리말·꼬리말 */
.hd{position:absolute;left:15mm;right:15mm;top:9mm;height:9mm;display:flex;align-items:center;gap:8px;border-bottom:1.6px solid var(--c1);font-size:8.6pt;color:#4b5563}
.logo{width:22px;height:22px;border-radius:50%%;background:var(--c1);color:#fff;display:grid;place-items:center;font-weight:900;font-size:10pt;flex:none;overflow:hidden}
.logo img{width:100%%;height:100%%;object-fit:cover}
.hd .ac{font-weight:900;color:var(--d);font-size:10pt}.hd .un{margin-left:auto}
.hd .sc{background:var(--c1);color:#fff;font-weight:800;padding:1px 10px;border-radius:999px;font-size:8.4pt}
.ft{position:absolute;bottom:7mm;left:15mm;right:15mm;display:flex;align-items:center;font-size:7.6pt;color:#8a94a3}
.ft .no{font-weight:900;font-size:10pt;color:#fff;background:var(--c1);min-width:26px;text-align:center;border-radius:6px;padding:1px 6px}
.pg.even .ft{flex-direction:row-reverse}.pg.even .ft .mid{text-align:right}.ft .mid{flex:1;padding:0 8px}
/* 제목 띠 */
.band{display:flex;align-items:center;gap:10px;margin-bottom:4mm}
.band .k{font-family:'Noto Sans CJK KR';font-weight:900;font-size:9pt;color:var(--c2);letter-spacing:.12em}
.band h2{font-family:'Noto Sans CJK KR';font-weight:900;font-size:17pt;color:var(--d);letter-spacing:-.5px;line-height:1.3}
.band .bar{flex:1;height:3px;background:linear-gradient(90deg,var(--c1),transparent)}
.mk{background:linear-gradient(transparent 55%%,var(--hl) 55%%);padding:0 2px;font-weight:700}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:3mm 4mm}
.cols{column-count:2;column-gap:9mm;column-rule:.6px solid var(--ln);column-fill:auto;height:100%%}
.cols.one{column-count:1}.cols.one .ps{font-size:10.6pt;line-height:1.78}.cols.one .q .qb{padding-right:2mm}
.cols.bal{column-fill:balance;height:auto}
/* 표지 */
.cover{position:absolute;inset:0;background:var(--c1);color:#fff;overflow:hidden}
.cover .wave{position:absolute;left:0;right:0;bottom:0;height:84mm;background:#fff;border-radius:60%% 60%% 0 0/16mm 16mm 0 0}
.cover .top{position:absolute;left:18mm;right:18mm;top:18mm;display:flex;align-items:center;gap:10px;font-family:'Noto Sans CJK KR'}
.cover .top .logo{width:46px;height:46px;font-size:20pt;background:#fff;color:var(--c1)}
.cover .acn{font-size:23pt;font-weight:900;letter-spacing:-.5px}.cover .acs{font-size:9.5pt;opacity:.85}
.cover .ttl{position:absolute;left:18mm;right:18mm;top:62mm;font-family:'Noto Sans CJK KR'}
.cover .gr{display:inline-block;background:var(--c2);color:#fff;font-weight:900;font-size:11pt;padding:3px 14px;border-radius:999px}
.cover h1{font-size:40pt;font-weight:900;line-height:1.18;margin:5mm 0 3mm;letter-spacing:-1.5px}
.cover .st{font-size:12.5pt;opacity:.92;max-width:112mm}
.cover .art{position:absolute;right:12mm;top:124mm;width:100mm}
.cover .low{position:absolute;left:18mm;right:18mm;bottom:20mm;font-family:'Noto Sans CJK KR';color:#1b1f24}
.cover .in{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm;margin-bottom:8mm}
.cover .in div{border:1.4px solid var(--ln);border-radius:10px;padding:3mm;font-size:8.6pt;color:#4b5563}
.cover .in b{display:block;font-size:10.5pt;color:var(--d)}
.cover .nm{display:flex;gap:6mm;font-size:11pt;font-weight:700;color:#374151}.cover .nm span{flex:1;border-bottom:1.4px solid #9aa4b2;padding-bottom:2mm}
.cover .pub{margin-top:6mm;display:flex;justify-content:space-between;font-size:8.6pt;color:#8a94a3}
/* 학습 계획 */
.goal{border:2px solid var(--c1);border-radius:12px;padding:4mm 5mm;margin-bottom:5mm}
.goal h3{font-family:'Noto Sans CJK KR';font-size:11pt;color:var(--c1);margin-bottom:1.5mm}
.goal li{list-style:none;padding-left:18px;position:relative;margin:1mm 0}
.goal li:before{content:"";position:absolute;left:2px;top:.55em;width:9px;height:9px;border-radius:3px;background:var(--c2)}
table.plan{width:100%%;border-collapse:collapse;font-family:'Noto Sans CJK KR';font-size:9pt}
table.plan th{background:var(--c1);color:#fff;padding:2mm;font-weight:800}table.plan td{border-bottom:1px solid var(--ln);padding:2.4mm 2mm;text-align:center}
table.plan td:first-child{text-align:left;font-weight:700;color:var(--d)}
.face{display:inline-flex;gap:5px}.face i{width:16px;height:16px;border:1.3px solid #9aa4b2;border-radius:50%%;display:inline-block;font-style:normal;font-size:8pt;line-height:14px;color:#9aa4b2}
.box{display:inline-block;width:13px;height:13px;border:1.3px solid #9aa4b2;border-radius:3px;vertical-align:-2px}
.tchr{display:flex;gap:4mm;align-items:flex-start;margin-top:6mm}
.tchr .who{flex:none;text-align:center;font-family:'Noto Sans CJK KR';font-size:8pt;color:#6b7280;width:20mm}
.tchr .who .logo{width:44px;height:44px;margin:0 auto 1mm;font-size:17pt}
.tchr .bub{flex:1;background:var(--t);border-radius:4px 16px 16px 16px;padding:4mm 5mm;font-size:10pt;position:relative}
.tchr .bub b{color:var(--d)}
/* 한눈에 보기 */
.map{border:1.4px solid var(--ln);border-radius:12px;padding:4mm;margin:5mm 0;background:linear-gradient(180deg,#fff,var(--t))}
.map .h{font-weight:900;color:var(--d);font-size:10.5pt;margin-bottom:3mm}
.mrow{display:flex;align-items:center;gap:7mm}.mc{flex:1;display:flex;flex-direction:column;gap:2.5mm;position:relative}
.mc:not(:last-child):after{content:"";position:absolute;right:-6mm;top:50%%;border:6px solid transparent;border-left:8px solid var(--c2);transform:translateY(-50%%)}
.mn{background:#fff;border:1.5px solid var(--c1);border-radius:10px;padding:2mm 3mm;text-align:center;font-family:'Noto Sans CJK KR'}
.mn b{display:block;color:var(--d);font-size:9.6pt}.mn small{font-size:8pt;color:#6b7280}
.mn.k{background:var(--c1)}.mn.k b,.mn.k small{color:#fff}
/* 개념 */
.cc{border:1.3px solid var(--ln);border-radius:10px;overflow:hidden;break-inside:avoid;margin-bottom:3mm;background:#fff}
.cc h4{font-family:'Noto Sans CJK KR';background:var(--t);color:var(--d);font-size:10.5pt;padding:1.8mm 4mm;display:flex;gap:6px;align-items:center}
.cc h4 em{font-style:normal;background:var(--c1);color:#fff;border-radius:5px;padding:0 6px;font-size:8.6pt}
.cc .in{padding:2.2mm 3.5mm;line-height:1.65}
.cc .eg{margin-top:1.4mm;font-size:9.3pt;color:#374151;border-top:1px dashed var(--ln);padding-top:2mm}
.cc .eg b{font-family:'Noto Sans CJK KR';color:var(--c2);font-size:8.4pt;margin-right:4px}
.tip{break-inside:avoid;border-left:4px solid var(--c2);background:#FFF6EF;padding:2.5mm 4mm;border-radius:0 8px 8px 0;font-size:9.4pt;margin-bottom:4mm}
.tip b.h{color:var(--c2);margin-right:6px;font-family:'Noto Sans CJK KR'}
.chk{break-inside:avoid;border:1.6px dashed var(--c1);border-radius:10px;padding:3mm 4mm;margin-bottom:4mm}
.chk .h{font-weight:900;color:var(--c1);font-size:10pt;margin-bottom:1mm}
.chk ol{padding-left:0;list-style:none;counter-reset:c;columns:2;column-gap:6mm}.chk li{break-inside:avoid;counter-increment:c;display:flex;gap:6px;margin:1.2mm 0;font-size:9.6pt}
.chk li:before{content:counter(c);font-family:'Noto Sans CJK KR';font-weight:900;color:#fff;background:var(--c1);border-radius:50%%;width:17px;height:17px;flex:none;text-align:center;font-size:8pt;line-height:17px;margin-top:2px}
.blank{display:inline-block;min-width:16mm;border-bottom:1.3px solid #6b7280;margin:0 2px}
/* 유형 */
.ty{break-inside:avoid;margin-bottom:3mm}
.ty .tt{font-family:'Noto Sans CJK KR';display:flex;align-items:center;gap:6px;font-weight:900;color:var(--d);font-size:11pt;border-bottom:2px solid var(--c1);padding-bottom:1mm;margin-bottom:2mm}
.ty .tt em{font-style:normal;white-space:nowrap;flex:none;background:var(--c2);color:#fff;border-radius:5px;padding:0 7px;font-size:8.6pt}
.ty .idea{font-size:9.2pt;color:#374151;margin-bottom:2mm}
.ex{break-inside:avoid;background:var(--t);border-radius:10px;padding:3.5mm 4mm;margin-bottom:4mm}
.ex .lb{font-family:'Noto Sans CJK KR';font-weight:900;color:var(--c1);font-size:9pt;margin-right:5px}
.steps{margin-top:2mm;background:#fff;border-radius:8px;padding:2.5mm 3.5mm;font-size:9.4pt}
.steps p{display:flex;gap:6px;margin:.6mm 0}.steps p i{font-style:normal;font-family:'Noto Sans CJK KR';font-weight:900;color:var(--c2);flex:none;font-size:8.6pt;margin-top:1px}
.steps .an{text-align:right;font-family:'Noto Sans CJK KR';font-weight:900;color:var(--d);font-size:9pt}
.steps .an span{background:var(--hl);padding:0 8px;border-radius:4px;margin-left:4px}
/* 문제 */
.q{break-inside:avoid;display:flex;gap:7px}
.q .qn{flex:none;width:30px;text-align:center}
.q .qn b{display:block;font-size:11pt;font-weight:900;color:var(--c1);line-height:1.5}
.q .qn .rd{display:flex;gap:1px;justify-content:center;margin-top:1px}.q .qn .rd i{width:8px;height:8px;border:1px solid #b6bec9;border-radius:2px}
.q .qb{flex:1;min-width:0}
.lvb{font-size:7.6pt;font-weight:800;color:#9aa4b2;margin-left:3px;letter-spacing:-.5px;white-space:nowrap}.lvb b{color:var(--c2)}
.tag{display:inline-block;font-size:7.6pt;font-weight:900;border-radius:4px;padding:0 5px;margin-right:4px;vertical-align:1px;color:#fff;background:var(--c1)}
.tag.hot{background:var(--c2)}.tag.hard{background:#1b1f24}
.op{display:grid;grid-template-columns:repeat(5,auto);justify-content:space-between;margin-top:1.6mm;gap:0 4px}
.op.v{grid-template-columns:1fr;justify-content:start}.op.v2{grid-template-columns:1fr 1fr;justify-content:start}
.op i{font-style:normal}
.fig{text-align:center;margin:2mm 0}.fig svg{max-width:100%%}
.bogi{border:1px solid #6b7280;padding:4.5mm 3.5mm 2mm;margin:3mm 0 1mm;position:relative;font-size:9.6pt}
.bogi .bt{position:absolute;top:-9px;left:50%%;transform:translateX(-50%%);background:#fff;padding:0 6px;font-family:'Noto Sans CJK KR';font-size:8.6pt}
.say{display:flex;gap:5px;margin:2mm 0}.say div{flex:1;text-align:center}.say p{border:1px solid #6b7280;border-radius:10px;padding:3px 5px;font-size:9pt;min-height:44px;text-align:left}.say b{font-family:'Noto Sans CJK KR';font-size:8.4pt}
/* 영어 지문 */
.ps{font-family:'Lora','Noto Serif CJK KR',serif;font-size:10.3pt;line-height:1.72;text-align:justify;hyphens:auto;margin:1.5mm 0 1mm;word-break:normal}
.ps u{text-decoration:none;border-bottom:1.3px solid #1b1f24}
.ps .bk{display:inline-block;min-width:34mm;border-bottom:1.3px solid #1b1f24}
.gl{font-size:8pt;color:#6b7280;font-family:'Noto Sans CJK KR';margin-top:.5mm}
.op.en{font-family:'Lora',serif;font-size:9.8pt;grid-template-columns:1fr;gap:.3mm}
.voc{break-inside:avoid;border:1.3px solid var(--ln);border-radius:10px;padding:2.5mm 4mm;margin-bottom:4mm;font-size:9pt}
.voc .h{font-weight:900;color:var(--c1)}.voc table{width:100%%;border-collapse:collapse}.voc td{padding:.7mm 1mm;border-bottom:1px dotted var(--ln)}
.voc td:first-child{font-family:'Lora',serif;font-weight:700;color:var(--d);white-space:nowrap}
/* Level 머리 */
.lvh{break-inside:avoid;display:flex;align-items:center;gap:8px;margin:0 0 4mm}
.lvh{flex-wrap:wrap}.lvh .lv{white-space:nowrap;font-family:'Noto Sans CJK KR';font-weight:900;color:#fff;background:var(--c1);border-radius:8px;padding:1mm 4mm;font-size:12pt}
.lvh .lv.l2{background:var(--c2)}.lvh .lv.l3{background:var(--d)}
.lvh .ds{font-family:'Noto Sans CJK KR';font-size:9pt;color:#4b5563}
.lvh .goal2{margin-left:auto;font-family:'Noto Sans CJK KR';font-size:8.4pt;color:#6b7280;border:1.2px solid var(--ln);border-radius:999px;padding:0 10px}
/* 서술형 */
.sv{break-inside:avoid}
.wbox{border:1.3px solid var(--ln);border-radius:8px;margin-top:2mm;position:relative;background:repeating-linear-gradient(transparent 0 7.4mm,#eef1f5 7.4mm 7.6mm)}
.wbox:after{content:"풀이";position:absolute;left:7px;top:3px;font-size:8pt;color:#9aa4b2;font-family:'Noto Sans CJK KR'}
table.rb{width:100%%;border-collapse:collapse;font-size:8.6pt;font-family:'Noto Sans CJK KR';margin-top:1.5mm}
table.rb td,table.rb th{border:1px solid var(--ln);padding:1mm 2mm}table.rb th{background:var(--t);color:var(--d)}
/* 자기 평가 */
.score{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;margin-bottom:4mm}
.score div{border:1.6px solid var(--ln);border-radius:12px;padding:2.5mm;text-align:center;font-family:'Noto Sans CJK KR'}
.score div b{display:block;color:var(--c1);font-size:11pt}.score div span{font-size:20pt;font-weight:900;color:#c7ced8}
.next{font-family:'Noto Sans CJK KR';font-size:8.8pt;margin-bottom:4mm;display:grid;grid-template-columns:1fr 1fr;gap:0 5mm}
.next div{display:flex;gap:3mm;align-items:center;padding:1.3mm 0;border-bottom:1px dashed var(--ln)}
.next em{font-style:normal;flex:none;width:26mm;font-weight:900;color:#fff;background:var(--c1);border-radius:999px;text-align:center;font-size:8.6pt}
.onote{border:1.6px solid var(--c1);border-radius:12px;overflow:hidden}
.onote .h{background:var(--c1);color:#fff;font-family:'Noto Sans CJK KR';font-weight:900;padding:1.6mm 4mm;font-size:10pt}
.onote table{width:100%%;border-collapse:collapse;font-family:'Noto Sans CJK KR';font-size:8.6pt}
.onote td{border-top:1px solid var(--ln);border-right:1px solid var(--ln);padding:2mm;vertical-align:top;height:14mm;color:#9aa4b2}
.onote td:last-child{border-right:0}
/* 정답과 해설 */
.ak{break-inside:avoid;margin-bottom:3.2mm;font-size:9pt;line-height:1.65}
.ak .h{display:flex;align-items:center;gap:6px;font-family:'Noto Sans CJK KR';margin-bottom:.6mm}
.ak .h b{color:#fff;background:var(--c1);border-radius:5px;padding:0 6px;font-size:8.6pt}
.ak .h .a{margin-left:auto;font-weight:900;color:var(--d);background:var(--hl);border-radius:4px;padding:0 8px}
.ak .tr{font-size:8.3pt;color:#4b5563;background:var(--t);border-radius:6px;padding:1.2mm 2.5mm;margin-top:1mm}.ak .tr b{font-family:'Noto Sans CJK KR';color:var(--c1);margin-right:3px}
.ak .trap{color:#b4232c;font-size:8.6pt;font-family:'Noto Sans CJK KR'}
.qa{display:grid;grid-template-columns:repeat(10,1fr);border:1.3px solid var(--c1);border-radius:8px;overflow:hidden;margin-bottom:5mm;font-family:'Noto Sans CJK KR';font-size:8.6pt;text-align:center}
.qa span{padding:1mm 0;border-right:1px solid var(--ln);border-bottom:1px solid var(--ln)}.qa span b{color:var(--c1);margin-right:3px}
.katex{font-size:1.04em}
.q .xp{display:block;margin-top:1.2mm;font-family:'Noto Sans CJK KR';font-size:6.8pt;font-weight:900;color:var(--c2);letter-spacing:-.3px}
.tyc{font-family:'Noto Sans CJK KR';font-size:7pt;color:#9aa4b2;margin-left:5px;white-space:nowrap}
.tag.bs{background:linear-gradient(90deg,#E0A800,#F2683A)}
.q.boss{border:2px solid #E0A800;border-radius:12px;padding:3mm 3mm 2mm 1mm;background:#FFFBEA;box-shadow:3px 3px 0 #F3D56B}
.hook{break-inside:avoid;display:flex;gap:4mm;align-items:stretch;margin-bottom:4mm}
.hook .hq{flex:1.4;background:var(--c1);color:#fff;border-radius:14px 14px 14px 4px;padding:2.4mm 4mm;font-size:9.5pt;line-height:1.6}
.hook .hq b{display:block;font-family:'Noto Sans CJK KR';color:var(--hl);font-size:9pt;margin-bottom:.5mm}
.hook .ha{flex:1;border:2px dashed var(--c1);border-radius:14px;padding:2.4mm 4mm;font-size:9pt;color:var(--d);line-height:1.6}
.ft .stp{width:30px;height:30px;border:1.4px dashed #b6bec9;border-radius:50%%;display:grid;place-items:center;font-size:6.8pt;color:#b6bec9;font-weight:700}
.stg{display:inline-block;font-size:7pt;font-weight:900;color:#fff;background:var(--c2);border-radius:4px;padding:0 5px;margin-right:6px}
.stamp{display:inline-block;width:26px;height:26px;border:1.5px dashed #9aa4b2;border-radius:50%%;vertical-align:middle}
.score div small{display:block;font-size:8pt;color:#9aa4b2}
.xpbar{border:2px solid var(--c2);border-radius:14px;padding:2.2mm 5mm;margin-bottom:3mm;background:#FFF8F2}
.xpbar .xh{display:flex;align-items:baseline;gap:3mm;font-family:'Noto Sans CJK KR'}.xpbar .xh b{color:var(--c2);font-size:11pt}
.xpbar .xpin{display:inline-block;width:24mm;border-bottom:1.6px solid #1b1f24}
.medals{display:flex;justify-content:space-around;margin:2mm 0 1mm}.medals div{text-align:center;font-family:'Noto Sans CJK KR';font-size:8.6pt}.medals b{display:block}.medals small{color:#9aa4b2;font-size:7.6pt}
.xn{text-align:center;font-family:'Noto Sans CJK KR';font-size:8.6pt;color:#6b7280}
table.ana{width:100%%;border-collapse:collapse;font-family:'Noto Sans CJK KR';font-size:8.6pt;margin-bottom:4mm}
table.ana th{background:var(--t);color:var(--d);padding:1mm}table.ana td{border-bottom:1px solid var(--ln);padding:.9mm 2mm}table.ana td.wr{width:22mm}
.sign{display:flex;gap:8mm;margin-top:3mm;font-family:'Noto Sans CJK KR';font-size:9pt;color:#4b5563}.sign span{flex:1;border-bottom:1.3px solid #9aa4b2;padding-bottom:3mm}
.tg{break-inside:avoid;margin-bottom:4.5mm}.tg .h{font-family:'Noto Sans CJK KR';font-weight:900;color:var(--d);font-size:10.5pt;border-left:4px solid var(--c1);padding-left:6px;margin-bottom:2mm}
table.tt2{width:100%%;border-collapse:collapse;font-size:8.8pt}table.tt2 th{background:var(--c1);color:#fff;font-family:'Noto Sans CJK KR';padding:1.4mm}table.tt2 td{border-bottom:1px solid var(--ln);padding:1.6mm 2mm;vertical-align:top}
.lvg{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm}.lvg div{border:1.4px solid var(--ln);border-radius:10px;padding:2.5mm 3mm;font-size:8.8pt}.lvg b{display:block;font-family:'Noto Sans CJK KR';color:var(--c1)}
ul.tips{padding-left:5mm;font-size:9pt}ul.tips li{margin:.8mm 0}
.dt{border-collapse:collapse;margin:2mm auto 0;font-family:'Noto Sans CJK KR';font-size:8pt}.dt th,.dt td{border:1px solid #9aa4b2;width:21px;height:16px;text-align:center;line-height:1.2}.dt th{background:var(--t)}.dt td.h{background:var(--hl);font-weight:900}
.cards i{display:inline-block;width:18px;height:24px;border:1.2px solid #1b1f24;border-radius:3px;text-align:center;line-height:22px;font-style:normal;font-family:'Noto Sans CJK KR';font-weight:800;margin:0 2px;font-size:9pt;background:#fff}
.talk{display:flex;gap:5px;margin:2mm 0}.talk div{flex:1;text-align:center}.talk p{border:1px solid #6b7280;border-radius:10px;padding:3px 6px;font-size:9pt;min-height:44px;text-align:left}.talk b{font-family:'Noto Sans CJK KR';font-size:8.4pt}
"""

def esc(s): return _h.escape(str(s))

def _logo(b):
    if b.get("logo_img"): return f'<div class=logo><img src="{b["logo_img"]}"></div>'
    return f'<div class=logo>{esc(b.get("mark") or b["academy"][0])}</div>'

class Book:
    def __init__(s, spec):
        s.S = spec; s.B = spec["brand"]; s.M = spec["meta"]; s.n = 0; s.pages = []; s.ans = []; s.cur = None; s.tys = []; s.stage = 1
    # ---- 문제 ----
    def lv(s, k):
        return f'<span class=lvb>{"".join("<b>●</b>" if i < k else "○" for i in range(3))}</span>'
    def q(s, p, gap=None):
        s.n += 1; n = s.n
        tags = "".join(f'<span class="tag {"hot" if t=="빈출" else "hard" if t in ("고난도","킬러") else "bs" if t=="BOSS" else ""}">{"👑 BOSS" if t=="BOSS" else esc(t)}</span>' for t in p.get("tags", []))
        ch = p.get("ch"); op = ""
        if ch:
            cls = p.get("opcls") or ("en" if s.M.get("subject") == "eng" else ("v2" if max(len(re.sub("<[^>]+>|\\$", "", c)) for c in ch) > 9 else ""))
            op = f'<div class="op {cls}">' + "".join(f"<i>{NUM[i]} {c}</i>" for i, c in enumerate(ch)) + "</div>"
        g = gap if gap is not None else p.get("gap", {1: 12, 2: 20, 3: 30}.get(p.get("lv", 2), 16))
        ty = p.get("ty") or s.cur; boss = "BOSS" in p.get("tags", [])
        if s.M.get("subject") != "eng":  # 수학: 풀이 공간 넉넉히 (Level 1 26mm · Level 2 34mm · BOSS 44mm)
            g = max(g, 44 if boss else {1: 26, 2: 34, 3: 40}[s.stage])
        xp = 50 if boss else {1: 10, 2: 20, 3: 30}[s.stage]
        s.ans.append({**p, "n": n, "ty": ty, "xp": xp, "stage": s.stage})
        code = f'<span class=tyc>유형{ty}</span>' if ty else ""
        return (f'<div class="q{" boss" if boss else ""}" style="margin-bottom:{g}mm"><div class=qn><b>{n:02d}</b><div class=rd><i></i><i></i><i></i></div><span class=xp>+{xp}</span></div>'
                f'<div class=qb>{tags}{p["q"]}{s.lv(p.get("lv",2))}{code}{op}</div></div>')
    # ---- 블록 ----
    def blk(s, b):
        t = b[0]
        if t == "html": return b[1]
        if t == "group": return '<div style="break-inside:avoid">' + "".join(s.blk(x) for x in b[1]) + "</div>"
        if t == "grid": return '<div class=g2>' + "".join(s.blk(x) for x in b[1]) + "</div>"
        if t == "band": return f'<div class=band><div><div class=k>{esc(b[1])}</div><h2>{b[2]}</h2></div><div class=bar></div></div>'
        if t == "concept":
            c = b[1]
            return (f'<div class=cc><h4><em>{esc(c.get("no",""))}</em>{c["t"]}</h4><div class=in>{c["body"]}'
                    + (f'<div class=eg><b>예</b>{c["eg"]}</div>' if c.get("eg") else "") + "</div></div>")
        if t == "map":
            cols = "".join('<div class=mc>' + "".join(f'<div class="mn{" k" if k else ""}"><b>{a}</b><small>{c}</small></div>' for a, c, k in col) + '</div>' for col in b[2])
            return f'<div class=map><div class="h sans">{esc(b[1])}</div><div class=mrow>{cols}</div></div>'
        if t == "hook": return f'<div class=hook><div class=hq><b>생각해 볼까?</b>{b[1]}</div><div class=ha>{b[2]}</div></div>'
        if t == "endtype": s.cur = None; return ""
        if t == "tip": return f'<div class=tip><b class=h>{esc(b[1])}</b>{b[2]}</div>'
        if t == "check":
            items = b[1]
            for i, (qq, a) in enumerate(items):
                s.ans.append(dict(n=f"개념 확인 {i+1}", q=qq, ans=a, sol="", mini=True))
            return '<div class=chk><div class="h sans">✔ 개념 확인</div><ol>' + "".join(f"<li><span>{qq}</span></li>" for qq, a in items) + "</ol></div>"
        if t == "type":
            T = b[1]; e = T["ex"]; s.cur = T["no"]; s.tys.append((T["no"], re.sub("<[^>]+>", "", T["name"])))
            st = "".join(f"<p><i>{k}</i><span>{v}</span></p>" for k, v in e["steps"])
            out = (f'<div class=ty><div class=tt><em>유형 {T["no"]}</em>{T["name"]}</div><div class=idea>{T["idea"]}</div>'
                   f'<div class=ex><span class=lb>대표 예제</span>{e["q"]}<div class=steps>{st}<div class=an>답<span>{e["a"]}</span></div></div></div></div>')
            return out
        if t == "q": return s.q(b[1], b[2] if len(b) > 2 else None)
        if t == "qs": return "".join(s.q(p) for p in b[1])
        if t == "lv":
            s.stage = b[1]
            return f'<div class=lvh><span class="lv l{b[1]}">Level {b[1]}</span><span class=ds>{esc(b[2])}</span><span class=goal2>목표 {esc(b[3])} · 한 문제 +{ {1:10,2:20,3:30}[b[1]] }XP</span></div>'
        if t == "voc":
            return '<div class=voc><div class="h sans">어휘 미리 보기</div><table>' + "".join(
                f"<tr><td>{esc(w)}</td><td>{esc(m)}</td><td>{esc(w2)}</td><td>{esc(m2)}</td></tr>" for (w, m), (w2, m2) in zip(b[1][::2], b[1][1::2])) + "</table></div>"
        if t == "essay":
            p = b[1]; s.n += 1
            s.ans.append(dict(n=s.n, q=p["q"], ans=p["ans"], sol=p.get("sol", ""), rb=p["rb"], ty=p.get("ty"), xp=30, lv=3, stage=3, tr=p.get("tr", "")))
            return (f'<div class="q sv" style="margin-bottom:5mm"><div class=qn><b>{s.n:02d}</b><div class=rd><i></i><i></i><i></i></div><span class=xp>+30</span></div><div class=qb>'
                    f'<span class="tag hard">서술형</span>{p["q"]}<div class=wbox style="height:{p.get("h",42)}mm"></div></div></div>')
        raise ValueError(t)
    # ---- 페이지 ----
    def frame(s, inner, sec, cols=False, bal=False, flow=False):
        no = len(s.pages) + 1
        body = f'<div class="cols{" bal" if bal else ""}">{inner}</div>' if cols else inner
        s.pages.append(
            f'<div class="pg{" flow" if flow else ""}"><div class=hd>{_logo(s.B)}<span class=ac>{esc(s.B["academy"])}</span>'
            f'<span class=un>{esc(s.M["grade"])} · {esc(s.M["unit"])}</span><span class=sc>{esc(sec)}</span></div>'
            f'<div class=body>{body}</div><div class=ft><span class=no></span><span class=mid>{esc(s.B["academy"])} 전용 교재 · 무단 복제·배포 금지</span>'
            f'<span class=stp>확인</span></div></div>')
    def cover(s):
        M, B = s.M, s.B
        ins = "".join(f"<div><b>{esc(a)}</b>{esc(b)}</div>" for a, b in M["inside"])
        s.pages.append(
            f'<div class=pg><div class=cover><div class=top>{_logo(B)}<div><div class=acn>{esc(B["academy"])}</div><div class=acs>{esc(B.get("slogan",""))}</div></div></div>'
            f'<div class=ttl><span class=gr>{esc(M["grade"])}</span><h1>{M["title"]}</h1><div class=st>{esc(M["sub"])}</div></div>'
            f'<div class=wave></div><div class=art>{M.get("art","")}</div>'
            f'<div class=low><div class=in>{ins}</div><div class=nm><span>이름</span><span>반</span><span>시작한 날</span></div>'
            f'<div class=pub><span>{esc(M["curri"])}</span><span>{esc(B["academy"])} 전용 · 제작 찰칵출판사</span></div></div></div></div>')
    def plan(s):
        P = s.S["plan"]; B = s.B
        rows = "".join(f'<tr><td><span class=stg>STAGE {i}</span>{esc(a)}</td><td data-sec="{esc(b)}"></td><td>&nbsp;&nbsp;월&nbsp;&nbsp;&nbsp;&nbsp;일</td><td><span class=stamp></span></td>'
                       f'<td><span class=face><i>☺</i><i>–</i><i>☹</i></span></td></tr>' for i, (a, b) in enumerate(P["rows"], 1))
        inner = (s.blk(("band", "START", "이 단원에서 배울 것")) +
                 '<div class=goal><h3>학습 목표</h3><ul>' + "".join(f"<li>{g}</li>" for g in P["goals"]) + "</ul></div>" +
                 (f'<div class=tip><b class=h>{esc(P["link"][0])}</b>{P["link"][1]}</div>' if P.get("link") else "") +
                 (s.blk(("map", "한눈에 보기", P["map"])) if P.get("map") else "") +
                 '<table class=plan><tr><th>퀘스트</th><th>쪽</th><th>공부한 날</th><th>선생님 도장</th><th>오늘 기분</th></tr>' + rows + "</table>" +
                 f'<div class=tchr><div class=who>{_logo(B)}{esc(B.get("teacher","선생님"))}</div><div class=bub>{P["msg"]}</div></div>')
        s.frame(inner, "학습 계획")
    def selfcheck(s, lv_counts=None):
        A = [a for a in s.ans if not a.get("mini")]
        tot = sum(a.get("xp", 0) for a in A)
        cnt = [sum(1 for a in A if a.get("stage") == k and "BOSS" not in a.get("tags", [])) for k in (1, 2, 3)]
        nb = sum(1 for a in A if "BOSS" in a.get("tags", []))
        inner = s.blk(("band", "CHECK", "스스로 점검하기 · XP 모으기"))
        cards = [(f"Level {i+1}", f"/ {c}", f"{c*x}XP") for i, (c, x) in enumerate(zip(cnt, (10, 20, 30))) if c]
        if nb: cards.append(("👑 BOSS", f"/ {nb}", f"{nb*50}XP"))
        inner += f'<div class=score style="grid-template-columns:repeat({len(cards)},1fr)">' + "".join(f"<div><b>{a}</b><span>&nbsp;&nbsp;&nbsp;{b}</span><small>최대 {c}</small></div>" for a, b, c in cards) + "</div>"
        tiers = [("브론즈", .4, "#C77B3A"), ("실버", .6, "#9AA4B2"), ("골드", .8, "#E0A800"), ("다이아", 1, "#4FB3E8")]
        inner += ('<div class=xpbar><div class=xh><b>나의 XP</b><span class=xpin>&nbsp;</span><span>/ ' + str(tot) + ' XP</span></div><div class=medals>'
                  + "".join(f'<div><svg viewBox="0 0 40 46" width="27"><path d="M12 0h16l-4 14h-8z" fill="{c}" opacity=".5"/><circle cx="20" cy="28" r="15" fill="#fff" stroke="{c}" stroke-width="3"/><text x="20" y="33" text-anchor="middle" font-size="11" font-weight="900" fill="{c}" font-family="Noto Sans CJK KR">{k[0]}</text></svg><b>{k}</b><small>{round(tot*r)}XP↑</small></div>' for k, r, c in tiers)
                  + '</div><div class=xn>받은 메달에 색칠해요! 지난번 나보다 1XP라도 더 모으면 성공 🎉</div></div>')
        if s.tys:
            rowsT = "".join(f'<tr><td><b>유형 {no}</b> {esc(nm)}</td><td>{" ".join(f"{a[chr(110)]:02d}" for a in A if a.get("ty")==no)}</td><td class=wr></td></tr>' for no, nm in s.tys)
            inner += '<table class=ana><tr><th>유형별 점검</th><th>해당 문제</th><th>틀린 개수</th></tr>' + rowsT + '</table>'
        inner += '<div class=next>' + "".join(f"<div><em>{esc(a)}</em><span>{b}</span></div>" for a, b in s.S["next"]) + "</div>"
        inner += ('<div class=onote><div class=h>오답 노트 — 틀린 문제는 꼭 다시!</div><table><tr><td style="width:14%">문제 번호</td><td style="width:43%">내가 쓴 풀이 / 틀린 이유</td><td>바른 풀이</td></tr>'
                  + "<tr><td></td><td></td><td></td></tr>" * 2 + "</table></div>")
        inner += '<div class=sign><span>선생님 확인</span><span>학부모 확인</span></div>'
        s.frame(inner, "자기 평가")
    def teacher(s):
        T = s.S["teacher"]; A = [a for a in s.ans if not a.get("mini")]
        inner = s.blk(("band", "FOR TEACHERS", "선생님 활용 가이드"))
        inner += '<div class=tg><div class=h>수업 회차안</div><table class=tt2><tr><th>회차</th><th>수업 (50분)</th><th>숙제</th></tr>' + "".join(f"<tr><td><b>{esc(a)}</b></td><td>{b}</td><td>{c}</td></tr>" for a, b, c in T["sessions"]) + "</table></div>"
        inner += '<div class=tg><div class=h>수준별 배정</div><div class=lvg>' + "".join(f'<div><b>{esc(a)}</b><span>{b}</span></div>' for a, b in T["levels"]) + "</div></div>"
        if s.tys:
            inner += '<div class=tg><div class=h>유형 코드표 (오답 분석용)</div><table class=tt2><tr><th>코드</th><th>유형</th><th>문제 번호</th></tr>' + "".join(
                f'<tr><td><b>유형{no}</b></td><td>{esc(nm)}</td><td>{" · ".join(f"{a[chr(110)]:02d}" for a in A if a.get("ty")==no)}</td></tr>' for no, nm in s.tys) + "</table></div>"
        inner += '<div class=tg><div class=h>이 교재의 약속</div><ul class=tips>' + "".join(f"<li>{x}</li>" for x in T["tips"]) + "</ul></div>"
        s.frame(inner, "선생님용")
    def answers(s):
        A = [a for a in s.ans if not a.get("mini")]; mini = [a for a in s.ans if a.get("mini")]
        quick = '<div class=qa>' + "".join(f"<span><b>{a['n']:02d}</b>{esc(a['ans']) if len(str(a['ans']))<6 else '풀이'}</span>" for a in A)
        quick += "<span></span>" * ((10 - len(A) % 10) % 10) + "</div>"
        items = ""
        if mini:
            items += '<div class=ak><div class=h><b>개념 확인</b></div>' + " · ".join(f"({i+1}) {a['ans']}" for i, a in enumerate(mini)) + "</div>"
        for a in A:
            rb = ""
            if a.get("rb"):
                rb = '<table class=rb><tr><th>채점 기준</th><th>배점</th></tr>' + "".join(f"<tr><td>{x}</td><td>{y}</td></tr>" for x, y in a["rb"]) + "</table>"
            items += (f'<div class=ak><div class=h><b>{a["n"]:02d}</b><span class=a>{a["ans"]}</span></div>{a.get("sol","")}'
                      + (f'<div class=tr><b>해석</b> {a["tr"]}</div>' if a.get("tr") else "")
                      + (f'<div class=trap>⚠ 오답 함정 · {a["trap"]}</div>' if a.get("trap") else "") + rb + "</div>")
        return quick, items
    def render(s):
        s.cover(); s.plan()
        for P in s.S["pages"]:
            if P.get("kind") == "selfcheck": s.selfcheck(); continue
            if P.get("kind") == "teacher": s.teacher(); continue
            if P.get("kind") == "answers":
                quick, items = s.answers()
                s.frame(s.blk(("band", "ANSWER", "정답과 해설")) + quick + f'<div class=cols style="flex:1;height:auto;min-height:0">{items}</div>', "정답과 해설", flow=True)
                continue
            head = "".join(s.blk(b) for b in P.get("head", []))
            inner = "".join(s.blk(b) for b in P["blocks"])
            if P.get("cols"):
                s.frame(head + f'<div class="cols{" one" if P.get("one") else ""}" style="flex:1;height:auto;min-height:0">{inner}</div>', P["sec"], flow=True)
            else:
                s.frame(head + inner, P["sec"])
        th = THEMES[s.M["theme"]]
        css = CSS % dict(th, body=s.M.get("font", "'Noto Serif CJK KR',serif"), fs=s.M.get("fs", "10.4pt"))
        return (f'<!doctype html><html lang=ko><head><meta charset=utf-8><link rel=stylesheet href="file://{KATEX}/katex.min.css">'
                f'<script src="file://{KATEX}/katex.min.js"></script><script src="file://{KATEX}/contrib/auto-render.min.js"></script>'
                f'<style>{css}</style></head><body>{"".join(s.pages)}'
                '<script>'
'''function flow(){ // 넘치는 문제를 다음 쪽으로 자동으로 넘김
 let guard=0;
 for(let i=0;i<document.querySelectorAll('.pg').length && guard<200;i++,guard++){
  const pg=document.querySelectorAll('.pg')[i]; if(!pg.classList.contains('flow')) continue;
  const body=pg.querySelector('.body'), cols=body.querySelector('.cols'); if(!cols) continue;
  const R=body.getBoundingClientRect(); const kids=[...cols.children];
  let cut=kids.findIndex(k=>{const r=k.getBoundingClientRect();return r.left>=R.right-2||r.bottom>R.bottom+1||r.right>R.right+1});
  if(cut<0) continue; if(cut===0) cut=1;
  const np=pg.cloneNode(true); const nb=np.querySelector('.body');
  [...nb.children].forEach(c=>{if(!c.classList.contains('cols')) c.remove()});
  const nc=nb.querySelector('.cols'); nc.innerHTML=''; kids.slice(cut).forEach(k=>nc.appendChild(k));
  pg.after(np);
 }
 const S={};document.querySelectorAll('.pg').forEach((p,i)=>{p.classList.toggle('even',i%2==1);const n=p.querySelector('.ft .no');if(n)n.textContent=i+1;
  const c=p.querySelector('.hd .sc');if(c){const k=c.textContent;(S[k]=S[k]||[]).push(i+1)}});
 document.querySelectorAll('td[data-sec]').forEach(t=>{const L=S[t.dataset.sec]||[];t.textContent=L.length?(L.length>1?L[0]+'~'+L[L.length-1]:L[0]):''});
}renderMathInElement(document.body,{delimiters:[{left:"$",right:"$",display:false}],throwOnError:false});document.fonts.ready.then(()=>{flow();document.body.dataset.ok=1})</script></body></html>''')

def build(spec): return Book(spec).render()

QA_JS = r"""() => { const out=[]; document.querySelectorAll('.pg').forEach((pg,i)=>{ const b=pg.querySelector('.body'); if(!b) return;
 const r=b.getBoundingClientRect(); let bad=0, ex='';
 b.querySelectorAll('*').forEach(e=>{ const q=e.getBoundingClientRect(); if(q.width===0&&q.height===0) return; if(e.closest('.katex-mathml')) return;
   if(q.bottom>r.bottom+1||q.right>r.right+1){ bad++; if(!ex) ex=(e.className||e.tagName)+':'+(e.textContent||'').slice(0,30)} });
 out.push([i+1,bad,ex,Math.round(r.bottom - Math.max(...[...b.children].map(c=>c.getBoundingClientRect().bottom),r.top))]); }); return out; }"""

def pdf(html, out, shots=None):
    p = pathlib.Path(out).with_suffix(".html"); p.write_text(html)
    js = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:794,height:1123}}}});
await pg.goto('file://{p}');await pg.waitForFunction(()=>document.body.dataset.ok);await pg.waitForTimeout(500);
const qa=await pg.evaluate({QA_JS});console.log(JSON.stringify(qa));
await pg.pdf({{path:'{out}',format:'A4',printBackground:true}});await b.close()}})()"""
    r = subprocess.run(["node", "-e", js], capture_output=True, text=True, cwd="/home/claude/textbook")
    if r.returncode: raise RuntimeError(r.stderr)
    qa = json.loads(r.stdout.strip().splitlines()[-1])
    if shots:
        subprocess.run(["pdftoppm", "-r", str(shots), "-png", out, str(pathlib.Path(out).with_suffix(""))+"_p"], check=True)
    return qa

def M(t):
    """태그 밖 텍스트에서 계산식 구간을 KaTeX $...$로 감싸기 (줄바꿈 방지)"""
    parts = re.split(r'(<[^>]+>)', t); out = []; insvg = 0
    for p in parts:
        if p.startswith('<'):
            if p.startswith('<svg'): insvg = 1
            if p.startswith('</svg'): insvg = 0
            out.append(p); continue
        if insvg or '$' in p: out.append(p); continue
        def rep(m):
            s = m.group(0); core = s.strip()
            if not re.search(r'[×＋－÷＝]', core) or not re.search(r'[0-9A-Za-z]', core): return s
            lead = s[:len(s)-len(s.lstrip())]; trail = s[len(s.rstrip()):]
            c = core.replace('×', r'\times ').replace('＋', '+').replace('－', '-').replace('÷', r'\div ').replace('＝', '=').replace('…', r'\cdots ')
            return f'{lead}${c}${trail}'
        out.append(re.sub(r'[0-9A-Za-z(][0-9A-Za-z()×＋－÷＝…\s.,]*[0-9A-Za-z)]', rep, p))
    return ''.join(out)
