# 시안 링크 페이지 생성기 — chalkakhome.com/p/<slug>/ 하나에 [홈페이지 시안 + 학원 전용 교재 샘플 + 관리 화면] 묶음
# 사용: python3 mkset.py <slug> "<학원명>" <과목들: elem,mid,eng> [표시 글자]
import sys, os, shutil, subprocess, importlib.util, copy, glob, html, json
sys.path.insert(0, "/home/claude/tbook")
from engine import build, pdf

REPO = "/home/claude/chalkakhome"
SUBJ = {"elem": ("/home/claude/tbook/s_elem_math.py", "초등 수학", "약수와 배수"),
        "mid": ("/home/claude/tbook/s_mid_math.py", "중등 수학", "경우의 수"),
        "eng": ("/home/claude/tbook/s_eng.py", "고1 영어 독해", "요지·주제·제목")}

def load(path):
    sp = importlib.util.spec_from_file_location("m" + str(abs(hash(path))), path); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m

def make(slug, name, subjects, mark=None, slogan=""):
    d = f"{REPO}/p/{slug}"; os.makedirs(d, exist_ok=True)
    # 기존 홈페이지 시안은 home/ 으로 옮김 (예전 링크는 묶음 페이지로 열림)
    old = f"{d}/index.html"
    if os.path.exists(old) and "data-chalkak-set" not in open(old).read():
        os.makedirs(f"{d}/home", exist_ok=True); shutil.move(old, f"{d}/home/index.html")
    home = "home/" if os.path.exists(f"{d}/home/index.html") else "/ex/academy/"
    books = []
    for s in subjects:
        mod = load(SUBJ[s][0]); spec = copy.deepcopy(mod.spec)
        spec["brand"].update(academy=name, mark=mark or name[0], slogan=slogan or spec["brand"].get("slogan", ""))
        out = f"{d}/book-{s}.pdf"; qa = pdf(build(spec), out)
        bad = [r for r in qa if r[1]]; assert not bad, bad
        os.remove(out.replace(".pdf", ".html"))
        pd = f"{d}/book-{s}"; shutil.rmtree(pd, ignore_errors=True); os.makedirs(pd)
        subprocess.run(["pdftoppm", "-r", "96", "-jpeg", "-jpegopt", "quality=80", out, f"{pd}/p"], check=True)
        pages = sorted(os.path.basename(x) for x in glob.glob(f"{pd}/p-*.jpg"))
        books.append((s, SUBJ[s][1], SUBJ[s][2], pages))
    open(f"{d}/index.html", "w").write(page(name, slug, home, books))
    return d

def page(name, slug, home, books):
    N = html.escape(name)
    tabs = "".join(f'<button class="bt{" on" if i==0 else ""}" data-b="{i}">{html.escape(t)} · {html.escape(u)}</button>' for i, (s, t, u, p) in enumerate(books))
    data = json.dumps([dict(s=s, p=p, pdf=f"book-{s}.pdf") for s, t, u, p in books])
    return f"""<!doctype html><html lang="ko" data-chalkak-set><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">
<title>{N} 원장님께 · 홈페이지·관리·교재 시안 | 찰칵홈</title>
<meta property="og:title" content="{N} 원장님께 드리는 시안 · 찰칵홈"><meta property="og:description" content="우리 학원 홈페이지 · 학원 관리 화면 · 학원 이름이 들어간 전용 교재 샘플을 한 번에 보세요.">
{'<meta property="og:image" content="https://chalkakhome.com/p/'+slug+'/og.jpg">' if os.path.exists(f"{REPO}/p/{slug}/og.jpg") else ''}
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<style>
:root{{--ink:#141B23;--mu:#5A6572;--bg:#F7F5F0;--ln:#E4E0D6;--c1:#1E4A7A;--c2:#F2683A;--hl:#FFE27A}}
*{{box-sizing:border-box}}body{{margin:0;font-family:Pretendard,system-ui,sans-serif;background:var(--bg);color:var(--ink);line-height:1.65;word-break:keep-all;font-size:17px}}
a{{color:inherit}}.w{{max-width:1100px;margin:0 auto;padding:0 20px}}
header{{padding:22px 0 8px}}header .w{{display:flex;align-items:center;gap:10px;font-weight:800;color:var(--mu);font-size:14px}}header .w span{{margin-left:auto}}
.hero{{padding:34px 0 26px}}.hero .k{{display:inline-block;background:var(--ink);color:#fff;border-radius:999px;padding:4px 14px;font-size:14px;font-weight:700}}
.hero h1{{font-size:clamp(30px,5vw,50px);line-height:1.25;margin:14px 0 10px;letter-spacing:-.03em}}.hero h1 b{{background:linear-gradient(transparent 60%,var(--hl) 60%)}}
.hero p{{color:var(--mu);margin:0 0 22px;max-width:640px}}
.three{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}}.three a{{display:block;text-decoration:none;background:#fff;border:1.5px solid var(--ln);border-radius:16px;padding:16px 18px;transition:transform .2s}}
.three a:hover{{transform:translateY(-2px)}}.three b{{display:block;font-size:19px}}.three small{{color:var(--mu);font-size:14px}}.three i{{font-style:normal;font-size:26px}}
section{{padding:44px 0;border-top:1px solid var(--ln)}}section h2{{font-size:clamp(24px,3.4vw,34px);margin:6px 0 8px;letter-spacing:-.02em}}
.no{{color:var(--c2);font-weight:900;font-size:14px;letter-spacing:.12em}}.lead{{color:var(--mu);margin:0 0 20px}}
.dev{{display:grid;grid-template-columns:2.2fr 1fr;gap:18px;align-items:start}}
.desk,.phone{{background:#fff;border:1.5px solid var(--ln);border-radius:16px;overflow:hidden;box-shadow:0 10px 30px rgba(20,27,35,.08)}}
.desk .bar{{height:28px;background:#EEEAE1;display:flex;align-items:center;gap:6px;padding:0 10px}}.desk .bar i{{width:9px;height:9px;border-radius:50%;background:#CFC8B8}}
.desk iframe{{width:166.6%;height:833px;border:0;transform:scale(.6);transform-origin:0 0;margin-bottom:-333px}}
.phone{{border-radius:28px;border:8px solid var(--ink)}}.phone iframe{{width:250%;height:1625px;border:0;transform:scale(.4);transform-origin:0 0;margin-bottom:-975px;display:block}}
.go{{display:inline-flex;gap:8px;align-items:center;margin-top:14px;background:var(--ink);color:#fff;text-decoration:none;border-radius:12px;padding:12px 20px;font-weight:800}}
.go.l{{background:transparent;color:var(--ink);border:2px solid var(--ink)}}
.bts{{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px}}.bt{{border:1.5px solid var(--ln);background:#fff;border-radius:999px;padding:8px 16px;font:inherit;font-size:15px;font-weight:700;cursor:pointer}}.bt.on{{background:var(--ink);color:#fff;border-color:var(--ink)}}
.view{{position:relative;background:#E9E5DC;border-radius:18px;padding:16px}}
.strip{{display:flex;gap:14px;overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:8px}}
.strip img{{scroll-snap-align:center;flex:none;width:min(420px,78vw);border-radius:6px;box-shadow:0 8px 22px rgba(0,0,0,.18);background:#fff}}
.nav{{display:flex;align-items:center;gap:10px;margin-top:10px}}.nav button{{border:0;background:#fff;width:40px;height:40px;border-radius:50%;font-size:18px;cursor:pointer}}.nav span{{font-weight:700;color:var(--mu);font-size:14px}}
.pts{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:16px}}.pts div{{background:#fff;border-radius:14px;padding:12px 14px;font-size:14px;color:var(--mu)}}.pts b{{display:block;color:var(--ink);font-size:16px}}
.adm{{background:#fff;border:1.5px solid var(--ln);border-radius:16px;overflow:hidden}}.adm iframe{{width:100%;height:860px;border:0;display:block}}
.cta{{background:var(--ink);color:#fff;border-radius:22px;padding:34px 28px;text-align:center}}.cta h2{{color:#fff}}.cta p{{color:#C9D2DC}}
.cta .gift{{display:inline-block;background:var(--hl);color:var(--ink);font-weight:900;border-radius:999px;padding:6px 16px;margin-bottom:10px}}
.cta a{{display:inline-block;margin:6px;background:#fff;color:var(--ink);text-decoration:none;border-radius:12px;padding:12px 20px;font-weight:800}}
footer{{text-align:center;color:var(--mu);font-size:13px;padding:30px 0 40px}}
@media(max-width:820px){{.three,.pts{{grid-template-columns:1fr 1fr}}.dev{{grid-template-columns:1fr}}.desk{{display:none}}.phone{{max-width:340px;margin:0 auto}}}}
@media(max-width:480px){{.three{{grid-template-columns:1fr}}}}
</style></head><body>
<header><div class="w">찰칵홈 · 학원 파트너 시안<span>{N}</span></div></header>
<div class="hero"><div class="w"><span class="k">{N} 원장님께</span>
<h1>원장님은 <b>수업만</b> 하세요.<br>홈페이지·관리·교재는 저희가 할게요.</h1>
<p>원장님 학원을 생각하며 미리 만들어 본 시안이에요. 아래 세 가지를 편하게 둘러보시고, <b>시안 먼저 보시고 결정하셔도 돼요.</b></p>
<div class="three"><a href="#home"><i>🖥</i><b>① 우리 학원 홈페이지</b><small>휴대폰·PC에서 바로 보이는 시안</small></a>
<a href="#book"><i>📘</i><b>② 우리 학원 전용 교재</b><small>학원 이름이 들어간 교재 샘플</small></a>
<a href="#admin"><i>📊</i><b>③ 학원 관리 프로그램</b><small>개발 중 · 미리보기</small></a></div></div></div>

<section id="home"><div class="w"><div class="no">01 · HOMEPAGE</div><h2>우리 학원 홈페이지 시안</h2><p class="lead">학부모님이 인스타·검색으로 들어왔을 때 가장 먼저 보는 화면이에요. 내용·사진은 원장님 학원에 맞게 바꿔 드려요.</p>
<div class="dev"><div class="desk"><div class="bar"><i></i><i></i><i></i></div><iframe src="{home}" loading="lazy" title="홈페이지 시안 PC"></iframe></div>
<div class="phone"><iframe src="{home}" loading="lazy" title="홈페이지 시안 휴대폰"></iframe></div></div>
<a class="go" href="{home}" target="_blank" rel="noopener">홈페이지 시안 크게 보기 →</a></div></section>

<section id="book"><div class="w"><div class="no">02 · TEXTBOOK</div><h2>{N} 전용 교재 샘플</h2>
<p class="lead">표지와 모든 쪽에 <b>{N}</b> 이름이 들어가요. 학생은 퀘스트·XP로 재미있게, 선생님은 유형 코드·수준별 배정·학부모 확인 칸으로 편하게 쓰시도록 만들었어요.</p>
<div class="bts">{tabs}</div>
<div class="view"><div class="strip" id="strip"></div><div class="nav"><button id="pv" aria-label="이전 쪽">‹</button><button id="nx" aria-label="다음 쪽">›</button><span id="cnt"></span><a id="pdf" class="go l" style="margin:0 0 0 auto;padding:8px 14px" target="_blank" rel="noopener">PDF로 보기</a></div></div>
<div class="pts"><div><b>🎮 퀘스트 · XP · 메달</b>학생이 스스로 하고 싶게</div><div><b>📈 Level 1 → 2 → 3 + BOSS</b>기초부터 학평·수능형까지</div><div><b>🧾 유형 코드 · 오답 분석</b>약한 유형이 한눈에</div><div><b>✍ 선생님 가이드</b>회차안 · 수준별 숙제 배정</div></div>
<p class="lead" style="margin-top:14px;font-size:14px">모든 문제는 새로 만든 문항이고, 정답은 계산으로 전부 검산했어요. 학교 시험 범위·진도에 맞춘 단원도 만들어 드려요.</p></div></section>

<section id="admin"><div class="w"><div class="no">03 · MANAGEMENT</div><h2>학원 관리 프로그램 미리보기 <small style="font-size:15px;background:#FFE27A;border-radius:99px;padding:3px 10px;vertical-align:middle">개발 중</small></h2><p class="lead">지금 만들고 있는 관리 프로그램의 미리보기예요. 출결을 누르면 학부모 문자가 자동으로 써지고, 원비·교재 진도까지 한 화면에서 보게 될 거예요. 먼저 함께하시는 학원은 완성되면 가장 먼저 무료로 써 보실 수 있어요. (예시 데이터)</p>
<div class="adm"><iframe src="/demo/academy/?n={html.escape(name)}" loading="lazy" title="학원 관리 화면 미리보기"></iframe></div></div></section>

<section><div class="w"><div class="cta"><span class="gift">처음 함께하는 3곳 · 특별 조건</span><h2>마음에 드시면 편하게 답장 주세요</h2>
<p>홈페이지 · 학원 전용 교재는 바로 시작할 수 있고, 학원 관리 프로그램은 완성되는 대로 먼저 써 보실 수 있어요.<br>시안은 무료이고, 보시고 결정하셔도 괜찮아요. 수정은 메일로 편하게 보내 주시면 돼요.</p>
<a href="mailto:kisthestar1@gmail.com?subject={html.escape(name)}%20시안%20문의">✉ 메일로 답장하기</a><a href="https://chalkakhome.com/#contact" target="_blank" rel="noopener">찰칵홈 둘러보기</a></div></div></section>
<footer>찰칵홈 · 찰칵출판사 — 동네 학원의 홈페이지·관리·교재 파트너</footer>
<script>
const B={data};let bi=0;const st=document.getElementById('strip'),cnt=document.getElementById('cnt');
function show(i){{bi=i;const b=B[i];st.innerHTML=b.p.map((p,k)=>`<img src="book-${{b.s}}/${{p}}" alt="교재 ${{k+1}}쪽" loading="${{k<3?'eager':'lazy'}}">`).join('');st.scrollLeft=0;
 document.getElementById('pdf').href=b.pdf;document.querySelectorAll('.bt').forEach((x,k)=>x.classList.toggle('on',k==i));upd()}}
function upd(){{const im=st.querySelector('img');if(!im)return;const w=im.getBoundingClientRect().width+14;cnt.textContent=Math.min(B[bi].p.length,Math.round(st.scrollLeft/w)+1)+' / '+B[bi].p.length+'쪽'}}
st.addEventListener('scroll',upd,{{passive:true}});
document.getElementById('pv').onclick=()=>{{const w=st.querySelector('img').getBoundingClientRect().width+14;st.scrollBy({{left:-w,behavior:'smooth'}})}};
document.getElementById('nx').onclick=()=>{{const w=st.querySelector('img').getBoundingClientRect().width+14;st.scrollBy({{left:w,behavior:'smooth'}})}};
document.querySelectorAll('.bt').forEach(b=>b.onclick=()=>show(+b.dataset.b));show(0);
</script></body></html>"""

if __name__ == "__main__":
    slug, name, subs = sys.argv[1], sys.argv[2], sys.argv[3].split(",")
    print(make(slug, name, subs, sys.argv[4] if len(sys.argv) > 4 else None))
