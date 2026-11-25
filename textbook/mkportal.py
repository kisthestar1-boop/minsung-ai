# 찰칵출판사 자료실 · 학원 전용 다운로드 페이지 생성기
# orders.json 하나만 고치고:  python3 mkportal.py   (--force 면 모두 다시 만들기)
import sys, os, json, shutil, subprocess, importlib.util, copy, glob, html, secrets, datetime
sys.path.insert(0, "/home/claude/tbook")
from engine import build, pdf, split, Book
REPO = "/home/claude/chalkakhome"; T = "/home/claude/tbook"; FORCE = "--force" in sys.argv
O = json.load(open(f"{T}/orders.json")); CH = O["chapters"]
E = html.escape
KIND = [("student", "📝 학생용 문제", "표지·개념·유형·실전·자기 평가"), ("answers", "✅ 정답과 해설", "빠른 정답표·풀이·오답 함정"), ("teacher", "🧑‍🏫 선생님용", "수업 회차안·수준별 배정 + 해설")]

def load(path):
    sp = importlib.util.spec_from_file_location("m" + str(abs(hash(path))), path); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m

def make_chapter(cid, brand, outdir, previews=False):
    """챕터 하나를 학원 브랜드로 만들어 3개 PDF로 나눔. 결과: {kind: (파일명, 쪽수)}, 문항 수"""
    c = CH[cid]; os.makedirs(outdir, exist_ok=True)
    meta = f"{outdir}/meta.json"
    if not FORCE and os.path.exists(meta): return json.load(open(meta))
    m = load(f"{T}/{c['mod']}"); spec = copy.deepcopy(m.spec); spec["brand"].update(brand)
    full = f"{outdir}/_full.pdf"; qa = pdf(build(spec), full); os.remove(full.replace(".pdf", ".html"))
    assert not [r for r in qa if r[1]], (cid, qa)
    parts = split(full, qa, outdir, cid)
    b = Book(copy.deepcopy(spec)); b.render(); nq = len([a for a in b.ans if not a.get("mini")])
    if previews:
        for f in glob.glob(f"{outdir}/p-*.jpg"): os.remove(f)
        subprocess.run(["pdftoppm", "-r", "90", "-jpeg", "-jpegopt", "quality=78", parts["student"][0], f"{outdir}/p"], check=True)
    os.remove(full)
    res = dict(files={k: [os.path.basename(p), n] for k, (p, n) in parts.items()}, nq=nq, nty=len(b.tys),
               pages=sorted(os.path.basename(x) for x in glob.glob(f"{outdir}/p-*.jpg")))
    json.dump(res, open(meta, "w"), ensure_ascii=False); return res

HEAD = """<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">
<title>{title}</title><link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<style>
:root{{--ink:#141B23;--mu:#5A6572;--bg:#F5F3EE;--ln:#E2DED4;--c:#3A4FB8}}*{{box-sizing:border-box}}
body{{margin:0;font-family:Pretendard,system-ui,sans-serif;background:var(--bg);color:var(--ink);font-size:15px;line-height:1.55;word-break:keep-all}}
.top{{background:linear-gradient(135deg,#3A4FB8,#1E2A6E);color:#fff;padding:22px 0}}.w{{max-width:1180px;margin:0 auto;padding:0 18px}}
.top h1{{margin:0;font-size:26px}}.top p{{margin:5px 0 0;opacity:.88;font-size:14px}}
h2{{font-size:18px;margin:26px 0 10px}}h2 small{{font-weight:500;color:var(--mu);font-size:13px;margin-left:6px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:12px}}
.ch{{background:#fff;border:1px solid var(--ln);border-radius:14px;overflow:hidden;display:flex;flex-direction:column}}
.ch img{{width:100%;aspect-ratio:210/297;object-fit:cover;display:block;border-bottom:1px solid var(--ln);cursor:zoom-in}}
.ch .t{{padding:10px 11px;display:flex;flex-direction:column;gap:6px;flex:1}}.ch .t b{{font-size:14.5px}}.ch .t small{{color:var(--mu);font-size:12px}}
.tag{{display:inline-block;font-size:11px;font-weight:800;border-radius:99px;padding:1px 8px;color:#fff}}
.dl{{display:flex;flex-direction:column;gap:5px;margin-top:auto}}.dl a{{display:flex;justify-content:space-between;align-items:center;text-decoration:none;color:var(--ink);background:#F1F3F8;border-radius:9px;padding:7px 10px;font-size:13px;font-weight:700}}
.dl a:hover{{background:#E3E8F7}}.dl a small{{font-weight:500;color:var(--mu);font-size:11px}}
.box{{background:#fff;border:1px solid var(--ln);border-radius:14px;padding:14px 16px}}
.nx{{display:flex;align-items:center;gap:10px;padding:7px 0;border-bottom:1px dashed var(--ln)}}.nx:last-child{{border:0}}.nx em{{margin-left:auto;font-style:normal;font-size:12px;font-weight:800;background:#F1F5F9;border-radius:99px;padding:1px 9px}}.nx em.on{{background:#FFE27A}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:14px}}.btn{{display:inline-block;background:var(--ink);color:#fff;text-decoration:none;border-radius:11px;padding:10px 16px;font-weight:800}}
.lb{{position:fixed;inset:0;background:rgba(0,0,0,.8);display:none;align-items:center;justify-content:center;gap:10px;overflow-x:auto;padding:20px}}.lb.on{{display:flex}}.lb img{{height:92vh;border-radius:6px}}
footer{{color:var(--mu);font-size:12px;text-align:center;padding:30px 0}}@media(max-width:760px){{.two{{grid-template-columns:1fr}}}}
</style></head><body>"""
LB = """<div class="lb" id="lb"></div><script>const lb=document.getElementById('lb');document.querySelectorAll('[data-pv]').forEach(i=>i.onclick=()=>{const P=JSON.parse(i.dataset.pv);lb.innerHTML=P.map(p=>`<img src="${p}" loading=lazy>`).join('');lb.classList.add('on')});lb.onclick=()=>lb.classList.remove('on')</script>"""

def card(cid, base, res, extra=""):
    c = CH[cid]; pv = json.dumps([f"{base}/{p}" for p in res["pages"]])
    img = f'<img src="{base}/{res["pages"][0]}" alt="" loading="lazy" data-pv=\'{pv}\' title="눌러서 넘겨 보기">' if res["pages"] else ""
    dl = "".join(f'<a href="{base}/{res["files"][k][0]}" download>{t}<small>{res["files"][k][1]}쪽 · PDF</small></a>' for k, t, _ in KIND)
    return (f'<div class="ch">{img}<div class="t"><div><span class="tag" style="background:{c["color"]}">{E(c["subj"])}</span> <small>{E(c["grade"])}</small></div>'
            f'<b>{E(c["unit"])}</b><small>{res["nq"]}문항 · 유형 {res["nty"]}개{extra}</small><div class="dl">{dl}</div></div></div>')

def pub():
    out = f"{REPO}/pub"; cards = ""
    for cid in CH:
        res = make_chapter(cid, dict(academy="찰칵출판사 견본", mark="찰", slogan="학원 이름·로고가 들어가는 자리", teacher="원장 선생님"), f"{out}/{cid}", previews=True)
        cards += card(cid, cid, res)
    nxt = "".join(f'<div class="nx"><b style="color:var(--c);font-size:12px">{E(a)}</b>{E(b)} · {E(c)}<em class="{"on" if d=="다음 제작" else ""}">{E(d)}</em></div>' for a, b, c, d in O["next"])
    mail = "mailto:kisthestar1@gmail.com?subject=" + "[찰칵출판사] 교재 챕터 요청" + "&body=" + "학원 이름:%0A학교·학년·과목:%0A교과서 출판사(예: 천재·비상·미래엔):%0A시험 범위(단원·쪽):%0A받으실 날짜:%0A"
    page = HEAD.format(title="찰칵출판사 · 학원 전용 교재 자료실") + f"""
<div class="top"><div class="w"><h1>📘 찰칵출판사 · 학원 전용 교재 자료실</h1><p>쓰시던 교재는 그대로 두시고, 필요한 챕터만 받아 보충·내신 대비용으로 쓰세요. 챕터마다 학생용 · 정답과 해설 · 선생님용 3개 파일이에요.</p></div></div>
<div class="w"><h2>견본 챕터 <small>표지를 누르면 넘겨 보기 · 학원 구독 시 학원 이름·로고가 들어가요</small></h2><div class="grid">{cards}</div>
<div class="two"><div><h2>🛠 다음 만들 챕터</h2><div class="box">{nxt}</div></div>
<div><h2>📮 이렇게 받아 보세요</h2><div class="box"><p style="margin:0 0 8px">① 필요한 챕터를 메일·인스타 DM으로 알려 주세요 (학교·교과서 출판사·시험 범위)<br>② 학원 이름이 들어간 챕터를 만들어 <b>학원 전용 다운로드 페이지</b>에 올려 드려요<br>③ 언제든 다시 내려받아 인쇄해 쓰시면 돼요 · 첫 챕터는 무료</p>
<a class="btn" href="{mail}">✉ 챕터 요청 메일 쓰기</a></div></div></div>
<h2>✅ 출고 기준</h2><div class="box">문항은 모두 새로 만든 문제 · 수학 정답은 계산으로 전부 검산 · EBS·평가원 자료와 저작권 유사도 검사 0건 · 쪽 넘침 자동 검사 0건 · 2022 개정 교육과정 반영</div>
<footer>찰칵출판사 · 찰칵홈 chalkakhome.com</footer></div>{LB}</body></html>"""
    open(f"{out}/index.html", "w").write(page)
    for old in glob.glob(f"{out}/*/book.pdf") + glob.glob(f"{out}/*-*-*/p-*.jpg"):
        pass

def portals():
    changed = False
    for key, a in O["academies"].items():
        if not a.get("code"): a["code"] = key + "-" + secrets.token_hex(3); changed = True
        base = f"{REPO}/s/{a['code']}"; os.makedirs(base, exist_ok=True)
        mine = [o for o in O["orders"] if o["acad"] == key]
        done = [o for o in mine if o["status"] == "전달"]; doing = [o for o in mine if o["status"] != "전달"]
        cards = ""
        for o in done:
            res = make_chapter(o["ch"], dict(academy=a["name"], mark=a.get("mark") or a["name"][0]), f"{base}/{o['ch']}", previews=True)
            cards += card(o["ch"], o["ch"], res, f" · {E(o['date'])} 전달")
        wait = "".join(f'<div class="nx">{E(CH.get(o["ch"],{}).get("grade",""))} · {E(CH.get(o["ch"],{}).get("unit",o["ch"]))}<em class="on">{E(o["status"])}</em></div>' for o in doing) or '<div class="nx" style="color:var(--mu)">진행 중인 요청이 없어요</div>'
        mail = f"mailto:kisthestar1@gmail.com?subject=[{a['name']}] 교재 챕터 요청&body=학교·학년·과목:%0A교과서 출판사(예: 천재·비상·미래엔):%0A시험 범위(단원·쪽):%0A받으실 날짜:%0A"
        page = HEAD.format(title=f"{a['name']} · 전용 교재") + f"""
<div class="top"><div class="w"><h1>📘 {E(a['name'])} 전용 교재</h1><p>받으신 챕터는 여기서 언제든 다시 내려받으실 수 있어요. 이 주소는 원장님만 아시는 주소예요.</p></div></div>
<div class="w"><h2>받은 챕터 <small>{len(done)}개 · 표지를 누르면 넘겨 보기</small></h2><div class="grid">{cards or '<div class="box">아직 받은 챕터가 없어요.</div>'}</div>
<div class="two"><div><h2>⏳ 만들고 있는 챕터</h2><div class="box">{wait}</div></div>
<div><h2>➕ 새 챕터 요청</h2><div class="box"><p style="margin:0 0 8px">학년·단원·시험 범위만 알려 주시면 학원 이름을 넣어 만들어 드려요.</p><a class="btn" href="{mail}">✉ 요청 메일 쓰기</a> <a class="btn" style="background:#fff;color:var(--ink);border:1.5px solid var(--ink)" href="/pub/" target="_blank">견본 자료실 보기</a></div></div></div>
<footer>찰칵출판사 · 무단 복제·배포 금지 · {E(a['name'])} 전용</footer></div>{LB}</body></html>"""
        open(f"{base}/index.html", "w").write(page)
    if changed: json.dump(O, open(f"{T}/orders.json", "w"), ensure_ascii=False, indent=1)
    rb = f"{REPO}/robots.txt"; t = open(rb).read() if os.path.exists(rb) else "User-agent: *\n"
    for d in ("/s/", "/pub/"):
        if f"Disallow: {d}" not in t: t = t.rstrip("\n") + f"\nDisallow: {d}\n"
    open(rb, "w").write(t)

if __name__ == "__main__":
    pub(); portals()
    for key, a in O["academies"].items(): print(a["name"], f"https://chalkakhome.com/s/{a['code']}/")
