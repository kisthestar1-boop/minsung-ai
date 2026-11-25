# 실제 문제집 스타일 (명조 본문, 대표 유형 예제+풀이, 그림, 난이도, 채점 기준)
road='''<svg viewBox="0 0 260 90" width="230"><g font-family="Noto Sans CJK KR" font-size="13" font-weight="700">
<circle cx="25" cy="45" r="16" fill="#fff" stroke="#222"/><text x="20" y="50">A</text>
<circle cx="130" cy="45" r="16" fill="#fff" stroke="#222"/><text x="125" y="50">B</text>
<circle cx="235" cy="45" r="16" fill="#fff" stroke="#222"/><text x="230" y="50">C</text></g>
<g fill="none" stroke="#222" stroke-width="1.3"><path d="M41 40 Q78 10 114 40"/><path d="M41 45 L114 45"/><path d="M41 50 Q78 80 114 50"/>
<path d="M146 40 Q183 18 219 40"/><path d="M146 50 Q183 72 219 50"/><path d="M28 29 Q130 -18 232 29" stroke-dasharray="4 3"/></g></svg>'''
cards=lambda ns:'<span class=cards>'+''.join(f'<i>{n}</i>' for n in ns)+'</span>'
dice='<table class=dt><tr><th>A＼B</th>'+''.join(f'<th>{b}</th>' for b in range(1,7))+'</tr>'+''.join('<tr><th>%d</th>'%a+''.join(f'<td class="{"h" if a+b==8 else ""}">{a+b}</td>' for b in range(1,7))+'</tr>' for a in range(1,7))+'</table>'
tree='''<svg viewBox="0 0 230 120" width="200" font-family="Noto Serif CJK KR" font-size="11"><g stroke="#333" fill="none">
<path d="M10 60 L60 30 M10 60 L60 90 M75 30 L125 15 M75 30 L125 45 M75 90 L125 75 M75 90 L125 105"/>
<path d="M140 15 L175 8 M140 15 L175 22 M140 45 L175 38 M140 45 L175 52 M140 75 L175 68 M140 75 L175 82 M140 105 L175 98 M140 105 L175 112"/></g>
<g fill="#111"><text x="62" y="34">앞</text><text x="62" y="94">뒤</text><text x="127" y="19">앞</text><text x="127" y="49">뒤</text><text x="127" y="79">앞</text><text x="127" y="109">뒤</text>
<text x="178" y="12">앞</text><text x="178" y="26">뒤</text><text x="178" y="42">앞 ◀</text><text x="178" y="56">뒤</text><text x="178" y="72">앞 ◀</text><text x="178" y="86">뒤</text><text x="178" y="102">앞 ◀</text><text x="178" y="116">뒤</text></g></svg>'''
U=[ # 유형명, 개념요약, 예제(q, 풀이, 답), 유제[(q,난이도,답,풀이)]
("사건과 경우의 수","빠짐없이, 중복 없이 센다. 두 주사위 문제는 표를 그리면 실수가 줄어든다.",
 ("서로 다른 두 개의 주사위 A, B를 동시에 던질 때, 나오는 두 눈의 수의 합이 8인 경우의 수를 구하시오.",
  "두 눈의 수의 합을 표로 나타내면 합이 8인 칸은 (2, 6), (3, 5), (4, 4), (5, 3), (6, 2)이다."+dice,"5"),
 [("1부터 15까지의 자연수가 각각 하나씩 적힌 15장의 카드 중에서 한 장을 뽑을 때, 3의 배수가 적힌 카드가 나오는 경우의 수를 구하시오.","하","5","3, 6, 9, 12, 15의 5가지"),
  ("100원짜리 동전 3개와 50원짜리 동전 4개가 있다. 이 동전을 사용하여 거스름돈 없이 300원을 지불하는 방법의 수는?<div class=op><i>① 1</i><i>② 2</i><i>③ 3</i><i>④ 4</i><i>⑤ 5</i></div>","중","③","(100원, 50원)의 개수를 순서쌍으로 나타내면 (3, 0), (2, 2), (1, 4)의 3가지")]),
("사건 A 또는 사건 B가 일어나는 경우의 수","두 사건이 동시에 일어나지 않을 때 (A의 경우의 수)＋(B의 경우의 수). 겹치는 것이 있으면 한 번 빼 준다.",
 ("한 개의 주사위를 던질 때, 2 이하의 눈 또는 5 이상의 눈이 나오는 경우의 수를 구하시오.",
  "2 이하의 눈: 1, 2의 2가지 / 5 이상의 눈: 5, 6의 2가지<br>두 사건은 동시에 일어나지 않으므로 2＋2＝4","4"),
 [("1부터 20까지의 자연수가 각각 하나씩 적힌 20장의 카드 중에서 한 장을 뽑을 때, 4의 배수 또는 7의 배수가 적힌 카드가 나오는 경우의 수를 구하시오.","하","7","4의 배수 5가지, 7의 배수 2가지, 공통인 수 없음 → 5＋2＝7"),
  ("서점에 수학 문제집이 5종류, 영어 문제집이 4종류 있다. 이 중 한 권을 사는 방법의 수는?<div class=op><i>① 4</i><i>② 5</i><i>③ 9</i><i>④ 18</i><i>⑤ 20</i></div>","하","③","5＋4＝9"),
  ("서로 다른 두 개의 주사위를 동시에 던질 때, 두 눈의 수의 합이 4 또는 9인 경우의 수를 구하시오.","중","7","합이 4: (1,3), (2,2), (3,1)의 3가지 / 합이 9: (3,6), (4,5), (5,4), (6,3)의 4가지 → 3＋4＝7")]),
("사건 A와 사건 B가 동시에 일어나는 경우의 수","두 사건이 동시에(잇달아) 일어날 때 (A의 경우의 수)×(B의 경우의 수). 길 찾기는 '거쳐 가는 경우'와 '바로 가는 경우'를 나누어 더한다.",
 ("오른쪽 그림과 같이 A 지점에서 B 지점으로 가는 길은 3가지, B 지점에서 C 지점으로 가는 길은 2가지이고, A 지점에서 C 지점으로 바로 가는 길이 1가지 있다. A 지점에서 C 지점까지 가는 방법의 수를 구하시오. (단, 같은 지점은 두 번 이상 지나지 않는다.)<div class=fig>"+road+"</div>",
  "B를 거쳐 가는 경우: 3×2＝6<br>바로 가는 경우: 1<br>따라서 6＋1＝7","7"),
 [("티셔츠 4종류와 바지 3종류 중에서 각각 한 가지씩 골라 짝 지어 입는 방법의 수를 구하시오.","하","12","4×3＝12"),
  ("동전 한 개와 주사위 한 개를 동시에 던질 때, 동전은 앞면이 나오고 주사위는 홀수의 눈이 나오는 경우의 수를 구하시오.","중","3","동전 앞면 1가지 × 홀수의 눈 3가지 ＝ 3"),
  ("학교 매점에 빵 4종류와 음료 5종류가 있다. 빵과 음료를 각각 한 가지씩 골라 사는 방법의 수는?<div class=op><i>① 9</i><i>② 12</i><i>③ 16</i><i>④ 20</i><i>⑤ 25</i></div>","하","④","4×5＝20")]),
("한 줄로 세우는 경우의 수","n명을 한 줄로 세우기: n×(n－1)×…×1 / 이웃하는 것은 한 묶음으로 보고, 묶음 안에서 자리 바꾸는 수를 곱한다.",
 ("A, B, C, D 4명을 한 줄로 세울 때, A와 B가 이웃하여 서는 방법의 수를 구하시오.",
  "A와 B를 한 묶음으로 생각하여 3명을 한 줄로 세우는 방법: 3×2×1＝6<br>묶음 안에서 A, B가 자리를 바꾸는 방법: 2<br>따라서 6×2＝12","12"),
 [("민수, 지아, 서준, 하린 4명을 한 줄로 세우는 방법의 수를 구하시오.","하","24","4×3×2×1＝24"),
  ("5명의 학생 중에서 3명을 뽑아 한 줄로 세우는 방법의 수를 구하시오.","하","60","5×4×3＝60"),
  ("A, B, C, D, E 5명을 한 줄로 세울 때, A가 맨 앞에, E가 맨 뒤에 서는 방법의 수는?<div class=op><i>① 6</i><i>② 12</i><i>③ 24</i><i>④ 60</i><i>⑤ 120</i></div>","중","①","A, E의 자리를 고정하고 B, C, D 3명을 세움 → 3×2×1＝6")]),
("자연수를 만드는 경우의 수","0이 포함되면 맨 앞자리에는 0이 올 수 없다. 짝수·홀수는 일의 자리부터 정한다.",
 ("0, 1, 2, 3이 각각 하나씩 적힌 4장의 카드 "+cards([0,1,2,3])+" 중에서 2장을 뽑아 만들 수 있는 두 자리 자연수의 개수를 구하시오.",
  "십의 자리에는 0을 제외한 1, 2, 3의 3가지<br>일의 자리에는 십의 자리에 온 수를 제외한 3가지<br>따라서 3×3＝9","9"),
 [("1, 2, 3, 4가 각각 하나씩 적힌 4장의 카드 중에서 2장을 뽑아 만들 수 있는 두 자리 자연수의 개수를 구하시오.","하","12","4×3＝12"),
  ("1부터 5까지의 자연수가 각각 하나씩 적힌 5장의 카드 중에서 2장을 뽑아 두 자리 자연수를 만들 때, 짝수의 개수를 구하시오.","중","8","일의 자리: 2, 4의 2가지 / 십의 자리: 나머지 4가지 → 2×4＝8")]),
("대표를 뽑는 경우의 수","자격이 다르면(회장·부회장) 한 줄로 세우기와 같다. 자격이 같으면 같은 것끼리 중복되는 수로 나눈다.",
 ("6명의 학생 중에서 대표 2명을 뽑는 방법의 수를 구하시오.",
  "회장 1명, 부회장 1명을 뽑는다면 6×5＝30<br>대표 2명은 자격이 같으므로 (A, B)와 (B, A)는 같은 경우이다.<br>따라서 30÷2＝15","15"),
 [("6명의 학생 중에서 회장 1명, 부회장 1명을 뽑는 방법의 수를 구하시오.","하","30","6×5＝30"),
  ("원 위에 있는 서로 다른 5개의 점 중에서 두 점을 이어 만들 수 있는 선분의 개수는?<div class=op><i>① 5</i><i>② 10</i><i>③ 15</i><i>④ 20</i><i>⑤ 25</i></div>","중","②","선분 AB와 BA는 같으므로 (5×4)÷2＝10")]),
]
route2='<svg viewBox="0 0 300 150" width="250" font-family="Noto Sans CJK KR" font-size="13" font-weight="700"><g fill="none" stroke="#222" stroke-width="1.2"><path d="M42 72 Q80 20 133 26"/><path d="M42 75 Q92 40 133 32"/><path d="M42 78 Q100 58 134 38"/><path d="M167 26 Q230 20 258 70"/><path d="M167 34 Q215 48 256 74"/><path d="M42 82 Q85 118 133 124"/><path d="M42 86 Q95 140 134 130"/><path d="M167 124 Q230 128 258 82"/><path d="M167 130 Q240 140 260 86"/><path d="M150 44 L150 108"/></g><g><circle cx="28" cy="78" r="15" fill="#fff" stroke="#222"/><text x="22" y="83">H</text><circle cx="150" cy="30" r="15" fill="#fff" stroke="#222"/><text x="145" y="35">P</text><circle cx="150" cy="124" r="15" fill="#fff" stroke="#222"/><text x="144" y="129">Q</text><circle cx="272" cy="78" r="15" fill="#fff" stroke="#222"/><text x="267" y="83">S</text></g><text x="10" y="108" font-size="10" font-weight="400">집</text><text x="262" y="108" font-size="10" font-weight="400">학교</text></svg>'
seats='<svg viewBox="0 0 260 50" width="230" font-family="Noto Sans CJK KR" font-size="11">'+''.join(f'<rect x="{5+i*50}" y="8" width="44" height="30" fill="{"#e6e6e6" if i==2 else "#fff"}" stroke="#222"/><text x="{20+i*50}" y="28">{"C" if i==2 else "좌석"+str(i+1) if False else i+1}</text>' for i in range(5))+'<text x="103" y="48" font-size="9">(가운데 좌석)</text></svg>'
colr='<svg viewBox="0 0 200 110" width="170" font-family="Noto Sans CJK KR" font-size="14" font-weight="700"><rect x="5" y="5" width="190" height="45" fill="#fff" stroke="#222"/><text x="95" y="33">A</text><rect x="5" y="50" width="63" height="55" fill="#fff" stroke="#222"/><text x="30" y="83">B</text><rect x="68" y="50" width="64" height="55" fill="#fff" stroke="#222"/><text x="94" y="83">C</text><rect x="132" y="50" width="63" height="55" fill="#fff" stroke="#222"/><text x="157" y="83">D</text></svg>'
talk=lambda L:'<div class=talk>'+''.join(f'<div><p>{t}</p><b>학생 {n}</b></div>' for n,t in L)+'</div>'
bogi=lambda L:'<div class=bogi><div class=bt>&lt; 보 기 &gt;</div>'+''.join(f'<p>{k}. {t}</p>' for k,t in zip("ㄱㄴㄷ",L))+'</div>'
T=[("서로 다른 두 개의 주사위 A, B를 동시에 던질 때 나오는 눈의 수에 대하여 학생 A, B, C가 다음과 같이 말하였다."+talk([("A","두 눈의 수의 합이 7인 경우의 수는 6이야."),("B","두 눈의 수의 곱이 홀수인 경우의 수는 9야."),("C","두 눈의 수의 차가 2인 경우의 수는 4야.")])+"제시한 내용이 옳은 학생만을 있는 대로 고른 것은?",["A","A, B","C","B, C","A, B, C"],"②","합 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1)의 6가지 → A 옳음<br>곱이 홀수: 두 눈이 모두 홀수 → 3×3＝9 → B 옳음<br>차가 2: (1,3), (2,4), (3,5), (4,6)과 순서를 바꾼 것 → 8가지 → C 틀림",""),
("그림은 집 H에서 학교 S까지 가는 길을 나타낸 것이다. 두 지점 P, Q 사이에는 길이 하나 있다. 집에서 학교까지 가는 방법의 수는? (단, 같은 지점은 두 번 이상 지나지 않는다.)<div class=fig>"+route2+"</div>",["14","16","18","20","24"],"④","H→P→S: 3×2＝6 / H→Q→S: 2×2＝4 / H→P→Q→S: 3×1×2＝6 / H→Q→P→S: 2×1×2＝4<br>따라서 6＋4＋6＋4＝20","[3점]"),
("1, 2, 3, 4, 5가 각각 하나씩 적힌 5장의 카드 중에서 서로 다른 3장을 뽑아 세 자리 자연수를 만들려고 한다. 이에 대한 설명으로 옳은 것만을 &lt;보기&gt;에서 있는 대로 고른 것은?"+bogi(["만들 수 있는 세 자리 자연수는 모두 60개이다.","300보다 큰 수는 36개이다.","5의 배수는 15개이다."]),["ㄱ","ㄴ","ㄱ, ㄴ","ㄴ, ㄷ","ㄱ, ㄴ, ㄷ"],"③","ㄱ. 5×4×3＝60 (옳음)<br>ㄴ. 백의 자리가 3, 4, 5 → 3×4×3＝36 (옳음)<br>ㄷ. 일의 자리가 5 → 4×3＝12 (틀림)",""),
("그림과 같이 한 줄로 놓인 5개의 좌석에 A, B, C, D, E 5명이 앉으려고 한다. C는 가운데 좌석에 앉고, A와 B는 서로 이웃하지 않도록 앉는 방법의 수는?<div class=fig>"+seats+"</div>",["12","16","20","24","28"],"②","C를 가운데에 고정하면 나머지 4명이 앉는 방법은 4×3×2×1＝24<br>A, B가 이웃하는 경우는 (1, 2) 또는 (4, 5) 좌석 → 2×2×2＝8<br>따라서 24－8＝16",""),
("0부터 9까지의 숫자 중 서로 다른 4개를 사용하여 네 자리 비밀번호를 만들려고 한다. 첫째 자리에는 홀수, 마지막 자리에는 짝수가 오도록 만들 수 있는 비밀번호의 개수는? (단, 첫째 자리에 0이 와도 된다.)",["840","1050","1120","1260","1400"],"⑤","첫째 자리 홀수 5가지, 마지막 자리 짝수 5가지, 가운데 두 자리는 남은 8개 중 8×7<br>따라서 5×5×56＝1400","[3점]"),
("그림의 A, B, C, D 네 영역을 서로 다른 4가지 색 중에서 골라 칠하려고 한다. 이웃한 영역은 서로 다른 색을 칠할 때, 칠하는 방법의 수는? (단, 같은 색을 여러 번 사용할 수 있다.)<div class=fig>"+colr+"</div>",["48","56","64","72","96"],"①","A는 B, C, D와 모두 이웃하므로 먼저 칠한다. A: 4가지, C: A와 다른 3가지, B: A, C와 다른 2가지, D: A, C와 다른 2가지<br>따라서 4×3×2×2＝48","[3점]"),
("어느 학급 회의에 남학생 4명과 여학생 3명이 참석하였다. 이 중에서 회장 1명과 부회장 1명을 뽑을 때, 회장과 부회장의 성별이 서로 다르도록 뽑는 방법의 수는?",["18","20","22","24","28"],"④","(회장 남, 부회장 여) 4×3＝12, (회장 여, 부회장 남) 3×4＝12 → 12＋12＝24",""),
("6명의 학생 중에서 대표를 뽑는 경우에 대하여 옳은 것만을 &lt;보기&gt;에서 있는 대로 고른 것은?"+bogi(["대표 2명을 뽑는 방법의 수는 15이다.","회장 1명, 부회장 1명을 뽑는 방법의 수는 30이다.","대표 3명을 뽑는 방법의 수는 대표 2명을 뽑는 방법의 수의 2배이다."]),["ㄱ","ㄷ","ㄱ, ㄴ","ㄴ, ㄷ","ㄱ, ㄴ, ㄷ"],"③","ㄱ. (6×5)÷2＝15 (옳음) ㄴ. 6×5＝30 (옳음)<br>ㄷ. 대표 3명: (6×5×4)÷(3×2×1)＝20, 15의 2배인 30과 다름 (틀림)","")]
SV=[("0, 1, 2, 3, 4가 각각 하나씩 적힌 5장의 카드 중에서 서로 다른 3장을 뽑아 세 자리 자연수를 만들 때, 짝수의 개수를 구하는 과정을 서술하고 답을 구하시오.","30",[("일의 자리가 0인 경우의 수 구하기","4×3＝12","40 %"),("일의 자리가 2 또는 4인 경우의 수 구하기","2×(3×3)＝18 (백의 자리에 0 제외)","40 %"),("짝수의 개수 구하기","12＋18＝30","20 %")]),
("남학생 3명과 여학생 4명 중에서 대표 3명을 뽑을 때, 여학생이 적어도 한 명 포함되도록 뽑는 방법의 수를 구하는 과정을 서술하고 답을 구하시오.","34",[("7명 중 대표 3명을 뽑는 방법의 수 구하기","(7×6×5)÷6＝35","40 %"),("남학생만 3명 뽑는 방법의 수 구하기","1","30 %"),("답 구하기","35－1＝34","30 %")])]
NUM="①②③④⑤"
st=lambda d:{'하':'●○○','중':'●●○','상':'●●●'}[d]
css="""@page{size:A4;margin:0}*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Noto Serif CJK KR',serif;color:#1a1a1a;font-size:10.6pt;line-height:1.72;word-break:keep-all}
.pg{width:210mm;height:297mm;padding:15mm 14mm 14mm;position:relative;page-break-after:always;overflow:hidden}
.rh{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2px solid #0b5394;padding-bottom:4px;margin-bottom:9mm;font-family:'Noto Sans CJK KR';font-size:8.5pt;color:#0b5394;font-weight:700}
.rh b{font-size:8.5pt}.pn{position:absolute;bottom:8mm;font-family:'Noto Sans CJK KR';font-size:9pt;color:#555}.pn.l{left:14mm}.pn.r{right:14mm}
.sec{font-family:'Noto Sans CJK KR';display:flex;align-items:center;gap:8px;margin:0 0 5mm}.sec .no{background:#0b5394;color:#fff;font-weight:900;font-size:12pt;padding:1px 9px}.sec h2{font-size:15pt;font-weight:900;letter-spacing:-.5px}
.cols{column-count:2;column-gap:8mm;column-rule:.6px solid #c9d3e0;column-fill:balance}
.ut{break-inside:avoid;font-family:'Noto Sans CJK KR';font-weight:800;font-size:9.5pt;color:#0b5394;border-top:1px solid #0b5394;border-bottom:1px solid #c9d3e0;padding:2px 0;margin:2mm 0 2mm}
.ut em{font-style:normal;background:#0b5394;color:#fff;padding:0 5px;margin-right:5px;font-size:8.5pt}
.memo{break-inside:avoid;font-size:9pt;background:#f2f6fb;border-left:3px solid #0b5394;padding:4px 8px;margin-bottom:2.5mm;font-family:'Noto Sans CJK KR';color:#333}
.ex{break-inside:avoid;border:1px solid #9fb6d3;padding:3mm;margin-bottom:3mm}
.ex .lb{font-family:'Noto Sans CJK KR';font-weight:900;color:#c0392b;font-size:9pt;margin-right:4px}
.sol{margin-top:2mm;padding-top:2mm;border-top:1px dashed #9fb6d3;font-size:9.6pt}.sol b.k{font-family:'Noto Sans CJK KR';font-size:8.5pt;color:#0b5394;margin-right:4px}
.ans{text-align:right;font-family:'Noto Sans CJK KR';font-size:9pt;font-weight:700}.ans span{border:1px solid #333;padding:0 6px;margin-left:4px}
.q{break-inside:avoid;display:flex;gap:6px;margin-bottom:11mm}.q .n{font-family:"Noto Sans CJK KR";font-weight:900;color:#0b5394;min-width:30px;font-size:10.5pt;line-height:1.3}
.q .lv{font-family:'Noto Sans CJK KR';font-size:7.5pt;color:#0b5394;letter-spacing:-1px;margin-left:3px}
.op{display:grid;grid-template-columns:repeat(5,auto);justify-content:space-between;margin-top:1.5mm}.op i{font-style:normal}
.fig{text-align:center;margin:2mm 0}
.cards i{display:inline-block;width:18px;height:24px;border:1px solid #333;border-radius:2px;text-align:center;line-height:24px;font-style:normal;font-family:'Noto Sans CJK KR';font-weight:700;margin:0 2px;font-size:9pt}
.dt{border-collapse:collapse;margin:2mm auto 0;font-family:'Noto Sans CJK KR';font-size:8pt}.dt th,.dt td{border:1px solid #9aa;width:20px;height:16px;text-align:center}.dt th{background:#eef2f7}.dt td.h{background:#ffe38a;font-weight:900}
.sv{break-inside:avoid;margin-bottom:6mm}.sv .tag{font-family:'Noto Sans CJK KR';background:#c0392b;color:#fff;font-size:8pt;padding:0 5px;margin-right:4px}
.wbox{border:1px solid #bbb;height:38mm;margin-top:2mm;position:relative}.wbox:after{content:"풀이";position:absolute;left:6px;top:3px;font-size:8pt;color:#999;font-family:'Noto Sans CJK KR'}
.ak{break-inside:avoid;margin-bottom:4mm;font-size:9.4pt}.ak .h{font-family:'Noto Sans CJK KR';font-weight:900;color:#0b5394}.ak .r{float:right;font-family:'Noto Sans CJK KR';font-weight:700}
table.sc{width:100%;border-collapse:collapse;font-size:8.5pt;font-family:'Noto Sans CJK KR';margin-top:1.5mm}table.sc td,table.sc th{border:1px solid #9aa;padding:2px 4px}table.sc th{background:#eef2f7}
.cv{display:grid;grid-template-columns:1fr 1fr;gap:4mm}.cb{border:1px solid #9fb6d3;padding:3mm}.cb h4{font-family:'Noto Sans CJK KR';font-size:10pt;color:#0b5394;border-bottom:1px solid #c9d3e0;margin-bottom:2mm}
.cb p{font-size:9.6pt}.cb .eg{font-size:9pt;color:#444;margin-top:1.5mm}.cb .eg b{font-family:'Noto Sans CJK KR';color:#c0392b;font-size:8pt;margin-right:3px}
.talk{display:flex;gap:6px;margin:2mm 0}.talk div{flex:1;text-align:center}.talk p{border:1px solid #555;border-radius:10px;padding:4px 6px;font-size:9pt;min-height:46px}.talk b{font-family:'Noto Sans CJK KR';font-size:8.5pt}
.bogi{border:1px solid #333;padding:5mm 3mm 2mm;margin:3mm 0 1mm;position:relative}.bogi .bt{position:absolute;top:-9px;left:50%;transform:translateX(-50%);background:#fff;padding:0 6px;font-size:9pt}.bogi p{font-size:9.6pt}
.pt{font-family:'Noto Sans CJK KR';font-weight:500;font-size:8.5pt}
.chk{font-family:'Noto Sans CJK KR';font-size:9pt}"""
RH=lambda l,r:f'<div class=rh><span>Ⅵ. 확률</span><b>{l}</b><span>{r}</span></div>'
def page(n,body,side): return f'<div class=pg>{body}<div class="pn {side}">{n}</div></div>'
# 개념 페이지
CB=[("사건과 경우의 수","실험이나 관찰에 의하여 나타나는 결과를 <b>사건</b>, 어떤 사건이 일어나는 가짓수를 그 사건의 <b>경우의 수</b>라고 한다.","주사위 한 개를 던질 때 짝수의 눈이 나오는 경우 → 2, 4, 6의 3가지"),
("사건 A 또는 사건 B가 일어나는 경우의 수","두 사건 A, B가 동시에 일어나지 않을 때, A가 일어나는 경우의 수가 m, B가 일어나는 경우의 수가 n이면 <b>m＋n</b>","주사위 한 개를 던질 때 1 또는 6이 나오는 경우 → 1＋1＝2"),
("사건 A와 사건 B가 동시에 일어나는 경우의 수","사건 A가 일어나는 경우의 수가 m, 그 각각에 대하여 사건 B가 일어나는 경우의 수가 n이면 <b>m×n</b>","동전 한 개와 주사위 한 개를 던질 때 → 2×6＝12"),
("한 줄로 세우는 경우의 수","n명을 한 줄로 세우는 경우의 수는 n×(n－1)×…×2×1<br>n명 중 r명을 뽑아 한 줄로 세우는 경우의 수는 n×(n－1)×…×(n－r＋1)","3명을 한 줄로 세우기 → 3×2×1＝6"),
("자연수를 만드는 경우의 수","0을 포함한 카드로 자연수를 만들 때는 맨 앞자리에 0이 올 수 없음에 주의한다.","1, 2, 3으로 두 자리 자연수 → 3×2＝6"),
("대표를 뽑는 경우의 수","자격이 다른 대표를 뽑는 경우는 한 줄로 세우는 경우와 같고, 자격이 같은 대표 2명을 뽑는 경우는 (n×(n－1))÷2이다.","4명 중 대표 2명 → (4×3)÷2＝6")]
concept=RH("1. 경우의 수","개념 정리")+'<div class=sec><span class=no>01</span><h2>경우의 수</h2></div><div class=cv>'+''.join(f'<div class=cb><h4>{i}. {h}</h4><p>{b}</p><div class=eg><b>예</b>{e}</div></div>' for i,(h,b,e) in enumerate(CB,1))+'</div>'
concept+='<div class=cv style="margin-top:5mm"><div class=cb><h4>수형도로 빠짐없이 세기</h4><p>동전 3개를 던질 때 앞면이 2개 나오는 경우를 수형도로 나타내면 ◀ 표시한 3가지이다.</p><div class=fig>'+tree+'</div></div><div class=cb><h4>꼭 구분하기</h4><p><b>또는</b> → 더한다 (＋)<br><b>동시에 · 잇달아 · 그리고</b> → 곱한다 (×)</p><p class=eg style="margin-top:3mm"><b>주의</b>두 사건에 겹치는 경우가 있으면 겹치는 수를 한 번 뺀다.<br>예) 1～10 중 2의 배수 또는 3의 배수 → 5＋3－1＝7</p></div></div><div class=memo style="margin-top:5mm"><b>개념 확인</b> ⑴ 한 개의 주사위를 던질 때 3의 배수의 눈이 나오는 경우의 수 ( &nbsp; ) &nbsp; ⑵ 3명을 한 줄로 세우는 경우의 수 ( &nbsp; ) &nbsp; ⑶ 동전 2개를 던질 때 일어나는 모든 경우의 수 ( &nbsp; )</div>'
# 유형 페이지
G=[];k=0;AK=[]
for ui,(un,memo,(eq,es,ea),ys) in enumerate(U,1):
  items=[];G.append(items)
  items.append(f'<div class=ut><em>유형 {ui:02d}</em>{un}</div><div class=memo>{memo}</div>')
  items.append(f'<div class=ex><span class=lb>대표 예제</span>{eq}<div class=sol><b class=k>풀이</b>{es}<div class=ans>답<span>{ea}</span></div></div></div>')
  for q,lv,a,s in ys:
    k+=1;items.append(f'<div class=q><span class=n>{k:02d}<br><span class=lv style="margin:0">{st(lv)}</span></span><div>{q}</div></div>');AK.append((f'{k:02d}',a,s))
p2=RH("1. 경우의 수","유형별 문제")+f'<div class=cols>{"".join("".join(g) for g in G[:2])}</div>'
p3c=RH("1. 경우의 수","유형별 문제")+f'<div class=cols>{"".join("".join(g) for g in G[4:])}</div>'
p3=RH("1. 경우의 수","유형별 문제")+f'<div class=cols>{"".join("".join(g) for g in G[2:4])}</div>'
TQ=[f'' for _ in []];tq=''.join(f'<div class=q><span class=n>{i:02d}</span><div>{q} <b class=pt>{pt}</b><div class=op>{"".join(f"<i>{NUM[j]} {o}</i>" for j,o in enumerate(op))}</div></div></div>' for i,(q,op,a,e,pt) in enumerate(T,1))
tq+=''.join(f'<div class=sv><span class=n style="font-family:Noto Sans CJK KR;font-weight:900;color:#0b5394">{9+i:02d}</span> <span class=tag>서술형</span>{q}<div class=wbox></div></div>' for i,(q,a,sc) in enumerate(SV))
qs=[f'<div class=q><span class=n>{i:02d}</span><div>{q} <b class=pt>{pt}</b><div class=op>{"".join(f"<i>{NUM[j]} {o}</i>" for j,o in enumerate(op))}</div></div></div>' for i,(q,op,a,e,pt) in enumerate(T,1)]
svs=[f'<div class=sv><span class=n style="font-family:Noto Sans CJK KR;font-weight:900;color:#0b5394">{9+i:02d}</span> <span class=tag>서술형</span>{q}<div class=wbox></div></div>' for i,(q,a,sc) in enumerate(SV)]
p4=RH("1. 경우의 수","중단원 마무리")+'<div class=sec><span class=no>실전</span><h2>중단원 마무리 · 학평형 &nbsp;<small style="font-size:9pt;font-weight:500;color:#555">맞힌 개수 ____ / 10</small></h2></div>'+f'<div class=cols>{"".join(qs[:4])}</div>'
p4b=RH("1. 경우의 수","중단원 마무리")+f'<div class=cols>{"".join(qs[4:])}{"".join(svs)}</div>'
ak=''.join(f'<div class=ak><span class=h>{n}</span> {s}<span class=r>답 {a}</span></div>' for n,a,s in AK)
tk=''.join(f'<div class=ak><span class=h>{i:02d}</span> {e}<span class=r>답 {a}</span></div>' for i,(q,op,a,e,pt) in enumerate(T,1))
tk+=''.join(f'<div class=ak><span class=h>{9+i:02d}</span><table class=sc><tr><th>단계</th><th>채점 기준</th><th>풀이</th><th>비율</th></tr>'+''.join(f'<tr><td>{j}단계</td><td>{c}</td><td>{s}</td><td>{p}</td></tr>' for j,(c,s,p) in enumerate(sc,1))+f'</table><div class=ans>답<span>{a}</span></div></div>' for i,(q,a,sc) in enumerate(SV))
p5=RH("정답과 풀이","")+'<div class=sec><span class=no>정답</span><h2>정답과 풀이</h2></div>'+f'<div class=cols><div class=ut><em>유형별</em>문제</div>{ak}</div>'
p5b=RH("정답과 풀이","")+f'<div class=cols><div class=ut><em>실전</em>중단원 마무리</div>{tk}</div>'
rows=''.join('<tr><td style="height:21mm"></td><td></td><td></td><td></td></tr>' for _ in range(9))
p6=RH("오답 노트","")+'<div class=sec><span class=no>NOTE</span><h2>오답 노트</h2></div><p class=chk style="margin-bottom:3mm">틀린 문제는 이유를 적고, 일주일 뒤에 다시 풀어 봅니다.</p><table class=sc style="font-size:9pt"><tr><th style="width:12%">문제 번호</th><th style="width:26%">틀린 이유 □개념 □계산 □문제 이해</th><th>다시 풀기</th><th style="width:12%">재확인</th></tr>'+rows+'</table>'
cover='''<div class=pg style="padding:0;background:#fff"><div style="position:absolute;inset:0 0 auto 0;height:150mm;background:#0b5394"></div>
<div style="position:absolute;left:16mm;top:20mm;font-family:Noto Sans CJK KR;color:#bcd3ee;font-size:10pt;letter-spacing:4px;font-weight:700">중학 수학 2(하) · 2022 개정 교육과정</div>
<div style="position:absolute;left:16mm;top:42mm;font-family:Noto Sans CJK KR;color:#fff;font-size:44pt;font-weight:900;letter-spacing:-2px;line-height:1.15">경우의 수<br>유형 완성</div>
<div style="position:absolute;left:16mm;top:104mm;font-family:Noto Sans CJK KR;color:#dbe7f6;font-size:11pt;line-height:1.8">개념 정리 · 대표 유형 6 · 유형별 문제 14<br>학평형 중단원 마무리 10 · 정답과 풀이 · 오답 노트</div>
<div style="position:absolute;left:16mm;top:168mm;font-family:Noto Sans CJK KR;font-size:26pt;font-weight:900;color:#0b5394">○○학원</div>
<div style="position:absolute;left:16mm;top:184mm;font-family:Noto Sans CJK KR;font-size:11pt;color:#555">원장님 학원 이름과 로고가 들어가는 자리입니다</div>
<div style="position:absolute;right:16mm;top:162mm;width:42mm;height:42mm;border:1px dashed #9aa;display:grid;place-items:center;font-family:Noto Sans CJK KR;font-size:9pt;color:#999">LOGO</div>
<div style="position:absolute;left:16mm;right:16mm;bottom:14mm;border-top:1px solid #ccc;padding-top:3mm;display:flex;justify-content:space-between;font-family:Noto Sans CJK KR;font-size:9pt;color:#444"><b style="font-size:12pt;color:#0b5394">찰칵출판사</b><span>이름 ______________ &nbsp; 반 ______</span></div></div>'''
html=f'<html><head><meta charset=utf-8><style>{css}</style></head><body>{cover}{page(84,concept,"l")}{page(85,p2,"r")}{page(86,p3,"l")}{page(87,p3c,"r")}{page(88,p4,"l")}{page(89,p4b,"r")}{page(90,p5,"l")}{page(91,p5b,"r")}{page(92,p6,"l")}</body></html>'
open('sample2.html','w').write(html)
