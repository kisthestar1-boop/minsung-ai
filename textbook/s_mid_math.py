import sys; sys.path.insert(0, "/home/claude/tbook")
from engine import build, pdf, M
src = open("/home/claude/textbook/build2.py").read(); src = src[:src.index("concept=RH")]; exec(src)

LV = {"하": 1, "중": 2, "상": 3}

def dice(x, y, s, pips, rot=0, c="#fff"):
    P = {1: [(.5, .5)], 2: [(.27, .27), (.73, .73)], 3: [(.25, .25), (.5, .5), (.75, .75)], 4: [(.27, .27), (.73, .27), (.27, .73), (.73, .73)],
         5: [(.25, .25), (.75, .25), (.5, .5), (.25, .75), (.75, .75)], 6: [(.27, .22), (.73, .22), (.27, .5), (.73, .5), (.27, .78), (.73, .78)]}[pips]
    d = "".join(f'<circle cx="{x+px*s}" cy="{y+py*s}" r="{s*.085}" fill="{"#E5475F" if pips==1 else "#1b1f24"}"/>' for px, py in P)
    return f'<g transform="rotate({rot} {x+s/2} {y+s/2})"><rect x="{x+4}" y="{y+6}" width="{s}" height="{s}" rx="{s*.18}" fill="rgba(0,0,0,.18)"/><rect x="{x}" y="{y}" width="{s}" height="{s}" rx="{s*.18}" fill="{c}" stroke="#1b1f24" stroke-width="2.4"/>{d}</g>'

ART = ('<svg viewBox="0 0 360 300" width="100%" font-family="Noto Sans CJK KR">'
       '<g stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round" opacity=".45"><path d="M20 150 L90 95 M20 150 L90 205 M110 95 L175 65 M110 95 L175 125 M110 205 L175 175 M110 205 L175 235"/></g>'
       '<g font-weight="900" font-size="15" fill="#fff" opacity=".8"><text x="92" y="100">H</text><text x="92" y="210">T</text><text x="180" y="70">H</text><text x="180" y="130">T</text><text x="180" y="180">H</text><text x="180" y="240">T</text></g>'
       + dice(205, 40, 92, 5, -12) + dice(250, 150, 80, 3, 9, "#FFF3D6") +
       '<circle cx="60" cy="255" r="34" fill="#F2683A" stroke="#1b1f24" stroke-width="2.4"/><circle cx="60" cy="255" r="24" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="3 4"/><text x="60" y="262" text-anchor="middle" fill="#fff" font-size="20" font-weight="900">100</text>'
       '<g font-weight="900" font-size="22" fill="#F2683A"><text x="145" y="285">×</text><text x="180" y="28">＋</text></g></svg>')

def ty(i):
    name, idea, (eq, es, ea), us = U[i]
    st = [(f"STEP {k+1}", M(x)) for k, x in enumerate(es.split("<br>"))]
    T_ = dict(no=f"{i+1:02d}", name=name, idea=M(idea), ex=dict(q=M(eq), steps=st, a=ea))
    qs = [dict(q=M(q), lv=LV[d], ans=a, sol=M(s), gap=10) for q, d, a, s in us]
    return [("type", T_)] + [("q", p) for p in qs]

TT = []
TYS = ["01", "03", "05", "04", "05", "03", "06", "06"]
for (q, ch, a, s, pt), t in zip(T, TYS):
    TT.append(dict(q=M(q), ch=[M(c) for c in ch], ans=a, sol=M(s), lv=2, gap=16, ty=t))
TT[1]["tags"] = ["빈출"]; TT[3]["tags"] = ["빈출"]; TT[5]["lv"] = 3; TT[5]["tags"] = ["BOSS"]; TT[4]["lv"] = 3
TT[1]["trap"] = "P와 Q 사이 길을 지나는 두 경우(H→P→Q→S, H→Q→P→S)를 빠뜨리면 10을 고르게 된다."
TT[3]["trap"] = "A와 B가 (2, 4)처럼 C를 사이에 두고 앉는 경우는 이웃이 아니다."
TT[5]["trap"] = "B와 D는 이웃하지 않으므로 같은 색을 칠해도 된다. 모두 다른 색으로 세면 24가 된다."
SVQ = [dict(ty=t, q=M(q), ans=a, rb=[(f"{x}<br><small>{M(y)}</small>", p) for x, y, p in r], sol=M(" → ".join(y for x, y, p in r)), h=58) for (q, a, r), t in zip(SV, ["05", "06"])]

concepts = [("concept", dict(no=f"{i}", t=h, body=M(b), eg=M(e))) for i, (h, b, e) in enumerate(CB, 1)]

spec = dict(
    brand=dict(academy="새봄수학학원", mark="봄", slogan="장유 · 한 명 한 명 끝까지", teacher="원장 선생님"),
    meta=dict(theme="math", subject="math", grade="중학교 2학년", unit="Ⅵ. 확률 ― 1. 경우의 수",
              title="경우의 수<br>완전 정복", sub="개념 → 대표 유형 6 → 학평형 실전 → 서술형까지 한 권으로",
              curri="2022 개정 교육과정 · 수학 2(하)", art=ART,
              inside=[("개념 6", "꼭 알아야 할 핵심만"), ("유형 6", "대표 예제 + 따라 풀기"), ("실전 10", "학평 수준 문제"), ("해설", "오답 함정까지")]),
    plan=dict(goals=["사건과 경우의 수의 뜻을 알고, <span class=mk>빠짐없이·중복 없이</span> 셀 수 있다.",
                     "<b>또는</b>이면 더하고, <b>동시에</b>이면 곱하는 이유를 설명할 수 있다.",
                     "한 줄로 세우기 · 자연수 만들기 · 대표 뽑기 문제를 풀 수 있다."],
              link=("이전에 배운 것", "중1 자료의 정리 · 초등 규칙 찾기 → <b>이 단원</b> → 다음 단원 <b>확률</b>의 기초가 돼요."),
              rows=[("개념 정리 + 개념 확인", "개념"), ("Level 1 대표 유형 01~06", "대표 유형"), ("Level 2 실전 · Level 3 서술형", "실전"), ("스스로 점검 · 오답 노트", "자기 평가"), ("정답과 해설로 채점하기", "정답과 해설")],
              map=[[("사건", "실험·관찰의 결과", 0), ("경우의 수", "사건이 일어나는 가짓수", 1)],
                   [("또는 → 더하기", "동시에 일어나지 않는 두 사건", 0), ("동시에 → 곱하기", "잇달아 일어나는 두 사건", 0)],
                   [("한 줄로 세우기", "n×(n－1)×…", 0), ("자연수 만들기", "맨 앞자리 0 주의", 0), ("대표 뽑기", "자격이 같으면 ÷2", 0)],
                   [("다음 단원", "확률", 1)]],
              msg="경우의 수는 <b>‘세는 방법’을 정하는 단원</b>이에요. 처음엔 수형도나 표를 직접 그려 보고, 익숙해지면 곱셈으로 빠르게! 문제 번호 아래 □□□에 몇 번째 풀었는지 체크하세요."),
    next=[("Level 1 틀림", "개념 정리(3쪽)를 다시 읽고 대표 예제를 손으로 다시 풀기"), ("Level 2 3개↓", "‘오답 함정’을 읽고 같은 유형 예제 1개 더 풀기"),
          ("Level 3 감점", "채점 기준표를 보고 빠진 단계를 오답 노트에 쓰기"), ("모두 맞힘", "다음 단원 ‘확률’로 GO! 선생님께 도전 문제 받기")],
    teacher=dict(
        sessions=[("1회차", "개념 정리 6개 설명 → 개념 확인 4문제 즉석 확인 → 유형 01~03 대표 예제", "유형 01~03 따라 풀기 (01~08)"),
                  ("2회차", "숙제 확인(유형 코드로 오답 체크) → 유형 04~06 대표 예제", "유형 04~06 따라 풀기 (09~15)"),
                  ("3회차", "Level 2 실전 16~23 풀이 · BOSS 21 함께 도전", "서술형 24~25 · 오답 노트 · 자기 평가")],
        levels=[("기초반", "Level 1(01~15) 중심 · 개념 확인 반복 · Level 2는 16·19·22만"), ("기본반", "Level 1 숙제 → Level 2 전체 · 서술형 1문항"),
                ("심화반", "Level 1은 숙제로 · 수업은 Level 2~3 + BOSS 풀이 발표")],
        tips=["모든 문제는 찰칵출판사가 새로 만든 문항이며, 정답은 계산으로 전부 검산했습니다.",
              "학원 이름·로고·선생님 말씀은 원하시는 대로 바꿔 드립니다. 진도·학교 시험 범위에 맞춘 추가 문제도 만들어 드립니다.",
              "문제 번호 아래 □□□는 학생 3회독 체크, 쪽 아래 ‘확인’ 칸은 선생님 도장 자리입니다.",
              "자기 평가 쪽의 ‘학부모 확인’ 칸으로 상담·학부모 연락에 바로 쓰실 수 있습니다."]),
    pages=[
        dict(sec="개념", head=[("band", "CONCEPT", "개념 정리 · 경우의 수")], blocks=[
            ("hook", "스마트폰 잠금 비밀번호 4자리(0~9)는 모두 몇 개일까? 하나씩 다 써 보면 하루가 걸려요.", "이 단원을 끝내면 <b>10초</b> 만에 계산해요. 정답은 10×10×10×10＝10000개!"),("grid", concepts),
            ("tip", "꼭 구분하기", M("<b>또는</b> → 더한다 (＋) &nbsp;|&nbsp; <b>동시에 · 잇달아 · 그리고</b> → 곱한다 (×) &nbsp;|&nbsp; 겹치는 경우가 있으면 한 번 뺀다.")),
            ("check", [(M("주사위 한 개를 던질 때 3의 배수의 눈이 나오는 경우의 수는 <span class=blank></span>이다."), "2"),
                       (M("동전 2개를 동시에 던질 때 일어나는 모든 경우의 수는 <span class=blank></span>이다."), "4"),
                       (M("4명을 한 줄로 세우는 경우의 수는 4×3×2×1＝<span class=blank></span>이다."), "24"),
                       (M("5명 중 대표 2명을 뽑는 경우의 수는 (5×4)÷2＝<span class=blank></span>이다."), "10")])]),
        dict(sec="대표 유형", cols=True, head=[("lv", 1, "대표 유형 익히기 · 예제 보고 따라 풀기", "모두 맞히기")], blocks=sum((ty(i) for i in range(6)), [])),
        dict(sec="실전", head=[("lv", 2, "학력평가 수준 실전 문제", "8문제 중 6개 이상")], cols=True,
             blocks=[("endtype",)] + [("q", p) for p in TT] + [("group", [("lv", 3, "풀이 과정을 쓰는 서술형", "채점 기준 80%↑"), ("essay", SVQ[0])]), ("essay", SVQ[1])]),
        dict(kind="selfcheck"),
        dict(kind="answers"),
        dict(kind="teacher"),
    ])

if __name__ == "__main__":
    import engine
    # concept 카드는 Book 인스턴스 없이 그려도 되도록 별도 처리
    qa = pdf(build(spec), "/home/claude/tbook/out/중등수학_경우의수.pdf", shots=40)
    for r in qa: print(r)
