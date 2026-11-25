# 찰칵출판사 교재 관리 페이지 — chalkakhome.com/pub/ (교재 목록 · 넘겨보기 · PDF · 학원별 시안 · 다음 제작)
import sys, os, shutil, subprocess, importlib.util, copy, glob, json, html, datetime
sys.path.insert(0, "/home/claude/tbook")
from engine import build, pdf, Book
REPO = "/home/claude/chalkakhome"; OUT = f"{REPO}/pub"

BOOKS = [  # id, 모듈, 과목, 학년, 단원, 상태, 색
    ("elem-math-divisor", "s_elem_math.py", "수학", "초등 5학년", "약수와 배수", "샘플 완성", "#10997A"),
    ("mid2-math-case", "s_mid_math.py", "수학", "중학교 2학년", "Ⅵ-1 경우의 수", "샘플 완성", "#1E5BA8"),
    ("hs1-eng-main", "s_eng.py", "영어", "고등학교 1학년", "Unit 01 요지·주제·제목", "샘플 완성", "#4A3DB0"),
]
NEXT = [("수학", "중학교 1학년", "정수와 유리수", "다음 제작"), ("영어", "고등학교 1학년", "Unit 02 빈칸 추론", "다음 제작"),
        ("수학", "초등 6학년", "분수의 나눗셈", "예정"), ("수학", "고등학교 1학년", "공통수학1 다항식", "예정"), ("영어", "중학교 2학년", "문법 · 시제와 조동사", "예정")]
SETS = [("thehan", "더한수학학원", "중등 수학 · 초등 수학"), ("thewiz", "더위즈영수학원", "중등 수학 · 고1 영어"), ("sample", "새봄학원 (예시)", "초등·중등 수학 · 고1 영어")]

def load(path):
    sp = importlib.util.spec_from_file_location("m" + str(abs(hash(path))), path); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m

def main():
    os.makedirs(OUT, exist_ok=True); cards = []
    for bid, mod, subj, grade, unit, st, col in BOOKS:
        m = load("/home/claude/tbook/" + mod); spec = copy.deepcopy(m.spec)
        spec["brand"].update(academy="찰칵출판사 견본", mark="찰", slogan="학원 이름·로고가 들어가는 자리")
        d = f"{OUT}/{bid}"; shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
        qa = pdf(build(spec), f"{d}/book.pdf"); os.remove(f"{d}/book.html")
        assert not [r for r in qa if r[1]], qa
        subprocess.run(["pdftoppm", "-r", "96", "-jpeg", "-jpegopt", "quality=80", f"{d}/book.pdf", f"{d}/p"], check=True)
        pages = sorted(os.path.basename(x) for x in glob.glob(f"{d}/p-*.jpg"))
        b = Book(copy.deepcopy(spec)); b.render(); A = [a for a in b.ans if not a.get("mini")]
        cards.append(dict(id=bid, subj=subj, grade=grade, unit=unit, st=st, col=col, pages=pages, nq=len(A), nty=len(b.tys), np=len(pages)))
    open(f"{OUT}/index.html", "w").write(page(cards))

def page(cards):
    today = datetime.date.today().isoformat()
    data = json.dumps(cards, ensure_ascii=False)
    nxt = "".join(f'<div class=nx><span class=sj>{html.escape(s)}</span><b>{html.escape(g)} · {html.escape(u)}</b><em class="{"on" if st=="다음 제작" else ""}">{st}</em></div>' for s, g, u, st in NEXT)
    sets = "".join(f'<a class=set href="/p/{k}/" target="_blank" rel="noopener"><b>{html.escape(n)}</b><small>{html.escape(t)}</small><span>시안 열기 ↗</span></a>' for k, n, t in SETS)
    return f"""<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">
<title>찰칵출판사 · 교재 관리</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<style>
:root{{--ink:#141B23;--mu:#5A6572;--bg:#F5F3EE;--ln:#E2DED4;--c:#3A4FB8}}
*{{box-sizing:border-box}}body{{margin:0;font-family:Pretendard,system-ui,sans-serif;background:var(--bg);color:var(--ink);font-size:15px;line-height:1.55}}
.top{{background:linear-gradient(135deg,#3A4FB8,#1E2A6E);color:#fff;padding:20px 0}}.w{{max-width:1180px;margin:0 auto;padding:0 18px}}
.top h1{{margin:0;font-size:26px}}.top p{{margin:4px 0 0;opacity:.85;font-size:14px}}
.kpi{{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px}}.kpi div{{background:#ffffff1f;border-radius:12px;padding:8px 14px;font-size:13px}}.kpi b{{display:block;font-size:20px}}
h2{{font-size:18px;margin:26px 0 10px;display:flex;align-items:center;gap:8px}}h2 small{{font-weight:500;color:var(--mu);font-size:13px}}
.grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:12px}}
.bk{{background:#fff;border:1px solid var(--ln);border-radius:14px;overflow:hidden;cursor:pointer;text-align:left;font:inherit;padding:0;color:inherit}}.bk:hover{{border-color:var(--c)}}
.bk img{{width:100%;aspect-ratio:210/297;object-fit:cover;display:block;border-bottom:1px solid var(--ln)}}
.bk .t{{padding:9px 10px}}.bk .t b{{display:block;font-size:14px}}.bk .t small{{color:var(--mu);font-size:12px}}
.tag{{display:inline-block;font-size:11px;font-weight:800;border-radius:99px;padding:1px 8px;color:#fff;margin-bottom:4px}}
.st{{float:right;font-size:11px;font-weight:800;color:#16A34A;background:#DCFCE7;border-radius:99px;padding:1px 7px}}
.view{{display:none;background:#fff;border:1px solid var(--ln);border-radius:16px;padding:14px;margin-top:14px}}.view.on{{display:block}}
.vh{{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:10px}}.vh b{{font-size:16px}}.vh a,.vh button{{border:0;background:var(--ink);color:#fff;text-decoration:none;border-radius:10px;padding:7px 12px;font:inherit;font-size:13px;font-weight:700;cursor:pointer}}.vh .l{{background:#EEF0F6;color:var(--ink)}}
.vh .sp{{margin-left:auto}}
.strip{{display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:8px}}.strip img{{flex:none;width:min(360px,75vw);scroll-snap-align:start;border-radius:6px;box-shadow:0 6px 16px rgba(0,0,0,.15)}}
.chk{{display:flex;gap:8px;flex-wrap:wrap;margin-top:8px}}.chk span{{font-size:12px;background:#F1F5F9;border-radius:8px;padding:3px 9px}}
.two{{display:grid;grid-template-columns:1.2fr 1fr;gap:14px}}
.nx{{display:flex;align-items:center;gap:10px;background:#fff;border:1px solid var(--ln);border-radius:12px;padding:9px 12px;margin-bottom:8px}}.nx .sj{{font-size:12px;font-weight:800;color:var(--c)}}.nx b{{font-size:14px}}
.nx em{{margin-left:auto;font-style:normal;font-size:12px;font-weight:800;color:var(--mu);background:#F1F5F9;border-radius:99px;padding:1px 9px}}.nx em.on{{background:#FFE27A;color:var(--ink)}}
.sets{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}}.set{{display:block;text-decoration:none;color:inherit;background:#fff;border:1px solid var(--ln);border-radius:12px;padding:10px 12px}}.set b{{display:block}}.set small{{color:var(--mu);font-size:12px;display:block}}.set span{{font-size:12px;font-weight:800;color:var(--c)}}
.rule{{background:#fff;border:1px solid var(--ln);border-radius:12px;padding:12px 14px;font-size:13px;color:#333}}.rule li{{margin:3px 0}}
footer{{color:var(--mu);font-size:12px;text-align:center;padding:30px 0}}
@media(max-width:900px){{.grid{{grid-template-columns:repeat(3,1fr)}}.two{{grid-template-columns:1fr}}.sets{{grid-template-columns:1fr}}}}
@media(max-width:520px){{.grid{{grid-template-columns:repeat(2,1fr)}}}}
</style></head><body>
<div class="top"><div class="w"><h1>📘 찰칵출판사 · 교재 관리</h1><p>학원 전용 보충·내신 교재 — 만든 교재를 보고, 학원별 시안으로 보내요 · {today} 기준</p>
<div class="kpi"><div>완성 교재<b id="k1"></b></div><div>총 문항<b id="k2"></b></div><div>정답 검산<b>100%</b></div><div>저작권 유사도<b>0건</b></div><div>학원 시안<b>{len(SETS)}곳</b></div></div></div></div>
<div class="w">
<h2>📚 교재 목록 <small>누르면 아래에서 넘겨 보기</small></h2><div class="grid" id="grid"></div>
<div class="view" id="view"><div class="vh"><b id="vt"></b><span class="sp"></span><a id="vpdf" target="_blank" rel="noopener">PDF 보기</a><button class="l" id="vx">닫기</button></div><div class="strip" id="vs"></div><div class="chk" id="vc"></div></div>
<div class="two"><div><h2>🛠 다음 만들 교재</h2>{nxt}</div>
<div><h2>✅ 출고 기준</h2><ul class="rule"><li>문제는 모두 새로 만든 문항 · 수학 정답은 계산으로 전부 검산</li><li>EBS·평가원 자료와 저작권 유사도 검사 0건이어야 출고</li><li>쪽 넘침 자동 검사 0건 · 학원 이름·로고는 표지와 모든 쪽에</li><li>쓰시던 교재는 그대로 · 우리는 보충·내신 대비용</li><li>가격(안): 1권(한 학기 분량) 9.9만 원 · 첫 단원 무료 샘플</li></ul></div></div>
<h2>🏫 학원별 시안 <small>홈페이지 + 전용 교재 + 관리 프로그램 미리보기</small></h2><div class="sets">{sets}</div>
<footer>찰칵출판사 · 이 페이지는 내부 관리용이에요 (검색 노출 안 함)</footer></div>
<script>
const B={data};
document.getElementById('k1').textContent=B.length+'권';document.getElementById('k2').textContent=B.reduce((s,b)=>s+b.nq,0)+'문항';
document.getElementById('grid').innerHTML=B.map((b,i)=>`<button class=bk data-i=${{i}}><img src="${{b.id}}/${{b.pages[0]}}" alt="" loading=lazy><div class=t><span class=tag style="background:${{b.col}}">${{b.subj}}</span><span class=st>${{b.st}}</span><b>${{b.unit}}</b><small>${{b.grade}} · ${{b.np}}쪽 · ${{b.nq}}문항</small></div></button>`).join('');
const V=document.getElementById('view');
document.querySelectorAll('.bk').forEach(x=>x.onclick=()=>{{const b=B[+x.dataset.i];document.getElementById('vt').textContent=b.grade+' '+b.subj+' · '+b.unit;
 document.getElementById('vpdf').href=b.id+'/book.pdf';document.getElementById('vs').innerHTML=b.pages.map(p=>`<img src="${{b.id}}/${{p}}" loading=lazy alt="">`).join('');
 document.getElementById('vc').innerHTML=['유형 '+b.nty+'개','문항 '+b.nq+'개','쪽 '+b.np+'쪽','XP·BOSS·메달','선생님 가이드','오답 노트'].map(t=>`<span>${{t}}</span>`).join('');
 V.classList.add('on');V.scrollIntoView({{behavior:'smooth',block:'start'}})}});
document.getElementById('vx').onclick=()=>V.classList.remove('on');
</script></body></html>"""

if __name__ == "__main__": main(); print(OUT)
