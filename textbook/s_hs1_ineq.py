import sys; sys.path.insert(0, "/home/claude/tbook")
import concept_ineq as CI, lesson_ineq as LI, pro_ineq as PI
from engine import build, pdf, M
from fractions import Fraction as F

# ---- 정답 검산 (정수 전수 조사 + 유리수 격자) ----
G = [F(i, 20) for i in range(-400, 401)]
Z = range(-30, 31)
# 강의 노트 예제 검산
assert all((x*x-5*x+4 < 0) == (1 < x < 4) for x in G) and all((x*x-5*x+4 > 0) == (x < 1 or x > 4) for x in G)
assert all((-x*x+x+6 > 0) == (-2 < x < 3) for x in G)
assert all((x*x-9 <= 0) == (-3 <= x <= 3) for x in G) and all((x*x+2*x+1 > 0) == (x != -1) for x in G)
assert not any(x*x-6*x+10 < 0 for x in G) and all((-x*x+4*x >= 0) == (0 <= x <= 4) for x in G)
assert all((x*x-2*x-3 < 0) == (-1 < x < 3) for x in G)
assert all(((2*x-3)*(x+1)<=0)==(-1<=x<=F(3,2)) for x in G) and all((x*x+2*x-8>0)==(x<-4 or x>2) for x in G)
assert all((x*x-x-6<0)==(-2<x<3) for x in G) and all((-x*x+3*x+10>=0)==(-2<=x<=5) for x in G) and all((x*x-9<0)==(-3<x<3) for x in G)
ks = [F(i, 10) for i in range(-50, 51)]
assert all((all(x*x-2*k*x+k+2 > 0 for x in G)) == (-1 < k < 2) for k in ks)
assert (2-1)*(2-4) < 0 and (5-1)*(5-4) > 0 and (0-1)*(0-4) > 0 and (3-1)*(3-4) < 0
# 시중형 개념·필수·기본 검산
assert all(((x+2)*(x-4)<=0)==(-2<=x<=4) for x in G) and all((-2*x*x+x+3<0)==(x<-1 or x>F(3,2)) for x in G)
assert all((x*x+x-6>0)==(x<-3 or x>2) for x in G) and all((-x*x+4*x-3>=0)==(1<=x<=3) for x in G)
assert all((all(x*x+2*(k-1)*x+k+5>0 for x in G))==(-1<k<4) for k in ks)
assert all((all(x*x-2*k*x+4>0 for x in G))==(-2<k<2) for k in ks)
assert all((k!=0 and all(k*x*x-4*x+k>0 for x in G))==(k>2) for k in ks)
assert all(((x*x-9<=0) and (x*x+2*x-8>=0))==(2<=x<=3) for x in G)
assert all(((x*x-x-2<0) and (x*x-4*x+3>0))==(-1<x<1) for x in G) and [n for n in Z if n*n-n-2<0 and n*n-4*n+3>0]==[0]
D=[lambda x:(x*x-3*x+2<0)==(1<x<2),lambda x:(x*x-x-12>=0)==(x<=-3 or x>=4),lambda x:(x*x+4*x>0)==(x<-4 or x>0),lambda x:(2*x*x-5*x-3<=0)==(F(-1,2)<=x<=3),
   lambda x:(-x*x+2*x+8>0)==(-2<x<4),lambda x:(x*x-6*x+9<=0)==(x==3),lambda x:(x*x-4*x+4>0)==(x!=2),lambda x:(x*x+2*x+3>0),lambda x:not(x*x+x+1<0),lambda x:(-x*x+6*x-9>=0)==(x==3),
   lambda x:((x*x-5*x+4<=0) and (x*x-2*x-3<0))==(1<=x<3),lambda x:((x*x-x-6>0) and (x*x-16<=0))==(-4<=x<-2 or 3<x<=4)]
assert all(all(f(x) for x in G) for f in D)
assert all((x*x-7*x+10<0)==(2<x<5) for x in G) and all((-x*x+x+6>0)==(-2<x<3) for x in G)
assert all((all(x*x-2*k*x+4*k-3>0 for x in G))==(1<k<3) for k in ks) and all((all(x*x+(k+1)*x+k+1>=0 for x in G))==(-1<=k<=3) for k in ks)
assert [n for n in Z if n*n-4*n-5 < 0 and n*n-3*n >= 0] == [0, 3, 4]
assert all((x*x-4 <= 0) == (-2 <= x <= 2) for x in G) and all(((x-3)**2 > 0) == (x != 3) for x in G) and all((-x*x+1 < 0) == (x < -1 or x > 1) for x in G)
assert [x for x in G if x*x - 5*x + 6 < 0] and min(x for x in G if x*x-5*x+6 < 0) > 2 and max(x for x in G if x*x-5*x+6 < 0) < 3
assert all((2*x*x + x - 6 >= 0) == (x <= -2 or x >= F(3, 2)) for x in G)
assert all((x*x - 4*x + 4 > 0) == (x != 2) for x in G)
a, b = 2, 3; assert all((-x*x + a*x + b > 0) == (-1 < x < 3) for x in G) and a + b == 5
a, b = -5, 4; assert all((x*x + a*x + b < 0) == (1 < x < 4) for x in G) and a + b == -1
assert [k for k in Z if k*k - k - 6 < 0] == [-1, 0, 1, 2]
assert [k for k in Z if (k-1)**2 - 9 <= 0] == list(range(-2, 5))
def nosol(a): return not any(a*x*x + 4*x + a - 3 > 0 for x in G)
assert [a for a in range(-8, 8) if nosol(a)] == list(range(-8, 0)[7:]) or [a for a in range(-8, 8) if nosol(a)] == [-8, -7, -6, -5, -4, -3, -2, -1]
assert not nosol(0) and nosol(-1) and not nosol(F(-1, 2))
assert [x for x in Z if x*x - x - 12 <= 0 and x*x - 3*x + 2 > 0] == [-3, -2, -1, 0, 3, 4]
assert max(x for x in G if x*x - x - 6 > 0 and (x-2)*(x-4) <= 0) == 4 and min(x for x in G if x*x-x-6 > 0 and (x-2)*(x-4) <= 0) > 3
ok = [F(i, 10) for i in range(-20, 40) if len([x for x in Z if 0 < x < 4 and x > F(i, 10)]) == 2]; assert min(ok) == 1 and max(ok) < 2
ks = [F(i, 10) for i in range(11, 80) if len([x for x in Z if (x-1)*(x-F(i, 10)) < 0]) == 3]; assert min(ks) > 4 and max(ks) == 5
assert [x for x in Z if x*x - 2*abs(x) - 3 < 0] == [-2, -1, 0, 1, 2]
assert [k for k in Z if (k+2)**2 - 4 < 0] == [-3, -2, -1]
assert [x for x in range(0, 11) if x*(20-2*x) >= 48] == [4, 5, 6]
boss = [a for a in range(-10, 16) if len([x for x in Z if x*x-5*x-6 < 0 and (x-1)*(x-a) >= 0]) == 3]; assert boss == [5]
assert [x for x in Z if x*x-5*x-6 < 0 and (x-1)*(x-5) >= 0] == [0, 1, 5]

def ty(no, name, idea, q, steps, a, us):
    return [("type", dict(no=no, name=name, idea=M(idea), ex=dict(q=q, steps=steps, a=a)))] + \
           [("q", dict(q=qq, ch=ch, ans=an, sol=so, lv=lv)) for qq, ch, an, so, lv in us]

TY = (
 ty("01", "이차부등식의 풀이", "인수분해 → 두 근 사이(＜0)인지 바깥(＞0)인지. 그래프를 떠올리면 실수가 없어요.",
    "이차부등식 $x^2-5x+6<0$의 해를 구하시오.",
    [("STEP 1", "$(x-2)(x-3)<0$"), ("STEP 2", "그래프가 $x$축 아래 → 두 근 사이")], "$2<x<3$",
    [("이차부등식 $2x^2+x-6\\ge 0$의 해를 구하시오.", None, "$x\\le -2$ 또는 $x\\ge \\frac{3}{2}$", "$(x+2)(2x-3)\\ge0$ → 두 근 바깥", 1),
     ("이차부등식 $x^2-4x+4>0$의 해를 구하시오.", None, "$x\\ne 2$인 모든 실수", "$(x-2)^2>0$ → $x=2$일 때만 0", 2)]) +
 ty("02", "해가 주어진 이차부등식", "해가 $\\alpha<x<\\beta$ ⇔ $a(x-\\alpha)(x-\\beta)<0$ (단, $a>0$). 부등호 방향으로 최고차항 부호를 정해요.",
    "이차부등식 $-x^2+ax+b>0$의 해가 $-1<x<3$일 때, $a+b$의 값을 구하시오.",
    [("STEP 1", "해가 $-1<x<3$ → $(x+1)(x-3)<0$ → $x^2-2x-3<0$"), ("STEP 2", "양변에 $-1$: $-x^2+2x+3>0$ → $a=2,\\ b=3$")], "5",
    [("이차부등식 $x^2+ax+b<0$의 해가 $1<x<4$일 때, $a+b$의 값을 구하시오.", None, "$-1$", "$(x-1)(x-4)=x^2-5x+4$ → $a=-5,\\ b=4$", 1)]) +
 ty("03", "항상 성립하는 이차부등식", "모든 실수 $x$에 대해 $x^2+bx+c>0$ ⇔ 판별식 $D<0$. 등호(≥)가 있으면 $D\\le 0$.",
    "모든 실수 $x$에 대하여 $x^2+2kx+k+6>0$이 성립하도록 하는 정수 $k$의 개수를 구하시오.",
    [("STEP 1", "$\\frac{D}{4}=k^2-(k+6)<0$"), ("STEP 2", "$(k+2)(k-3)<0$ → $-2<k<3$ → 정수 $-1,0,1,2$")], "4",
    [("모든 실수 $x$에 대하여 $x^2-2(k-1)x+9\\ge 0$이 성립하도록 하는 정수 $k$의 개수를 구하시오.", None, "7", "$(k-1)^2-9\\le 0$ → $-2\\le k\\le 4$ → 7개", 2),
     ("이차부등식 $ax^2+4x+a-3>0$의 해가 존재하지 않도록 하는 실수 $a$의 값의 범위를 구하시오.", None, "$a\\le -1$",
      "$a<0$이고 $\\frac{D}{4}=4-a(a-3)\\le 0$ → $a\\le -1$ 또는 $a\\ge 4$ → $a\\le -1$ ($a=0$이면 $4x-3>0$은 해가 있음)", 3)]) +
 ty("04", "연립이차부등식", "각각 풀고 <b>수직선에 함께</b> 그려 공통부분을 찾아요. 등호(●/○)를 꼭 표시!",
    "연립부등식 $\\begin{cases}x^2-x-12\\le 0\\\\ x^2-3x+2>0\\end{cases}$을 만족시키는 정수 $x$의 개수를 구하시오.",
    [("STEP 1", "$-3\\le x\\le 4$, $\\ x<1$ 또는 $x>2$"), ("STEP 2", "공통부분 $-3\\le x<1$ 또는 $2<x\\le 4$ → 정수 $-3,-2,-1,0,3,4$")], "6",
    [("연립부등식 $\\begin{cases}x^2-x-6>0\\\\ x^2-(a+2)x+2a\\le 0\\end{cases}$의 해가 $3<x\\le 4$일 때, 상수 $a$의 값을 구하시오. (단, $a>2$)", None, "4",
      "첫째 $x<-2$ 또는 $x>3$, 둘째 $2\\le x\\le a$ → 공통부분 $3<x\\le a$ → $a=4$", 2),
     ("연립부등식 $\\begin{cases}x^2-4x<0\\\\ x>a\\end{cases}$를 만족시키는 정수 $x$가 2개일 때, 실수 $a$의 값의 범위를 구하시오.", None, "$1\\le a<2$",
      "$0<x<4$ 중 $x>a$인 정수가 $2,3$뿐 → $1\\le a<2$", 3)]) +
 ty("05", "이차부등식의 활용", "구하는 것을 $x$로 놓고 범위 조건(길이 ＞ 0 등)을 꼭 함께 써요.",
    "길이가 20 m인 철망으로 한쪽 면이 벽인 직사각형 울타리를 만들려고 한다. 벽에 수직인 변의 길이를 $x$ m라 할 때, 넓이가 48 m² 이상이 되는 $x$의 값의 범위를 구하시오.",
    [("STEP 1", "넓이 $x(20-2x)\\ge 48$"), ("STEP 2", "$x^2-10x+24\\le 0$ → $(x-4)(x-6)\\le 0$")], "$4\\le x\\le 6$",
    [("모든 실수 $x$에 대하여 이차함수 $y=x^2-2x+3$의 그래프가 직선 $y=kx+2$보다 항상 위쪽에 있도록 하는 정수 $k$의 개수를 구하시오.", None, "3",
      "$x^2-(k+2)x+1>0$ 항상 → $(k+2)^2-4<0$ → $-4<k<0$ → 3개", 2)])
)

L2 = [
 dict(q="이차부등식 $(x-1)(x-k)<0$을 만족시키는 정수 $x$가 3개일 때, 실수 $k$의 값의 범위는? (단, $k>1$)", ch=["$3<k\\le 4$", "$4<k\\le 5$", "$4\\le k<5$", "$4<k<5$", "$5<k\\le 6$"], ans="②",
      sol="$1<x<k$의 정수가 $2,3,4$ → $4<k\\le 5$", trap="$k=5$이면 $1<x<5$ → 정수 3개(포함), $k=4$이면 2개(제외)", ty="04", tags=["빈출"]),
 dict(q="부등식 $x^2-2|x|-3<0$을 만족시키는 정수 $x$의 개수는?", ch=["3", "4", "5", "6", "7"], ans="③",
      sol="$|x|^2-2|x|-3<0$ → $(|x|-3)(|x|+1)<0$ → $|x|<3$ → $-2\\sim2$ 5개", trap="$x^2=|x|^2$로 바꾸면 한 번에 풀려요.", ty="01"),
 dict(q="모든 실수 $x$에 대하여 $x^2-2(a-1)x+a+5>0$이 성립하도록 하는 정수 $a$의 최댓값은?", ch=["1", "2", "3", "4", "5"], ans="③",
      sol="$(a-1)^2-(a+5)<0$ → $a^2-3a-4<0$ → $-1<a<4$ → 최댓값 3", ty="03"),
 dict(q="이차부등식 $x^2+ax+b\\le 0$의 해가 $x=3$뿐일 때, $a+b$의 값은?", ch=["$-3$", "$0$", "$3$", "$6$", "$9$"], ans="③",
      sol="$(x-3)^2\\le 0$ → $x^2-6x+9$ → $a=-6,\\ b=9$ → $3$", trap="해가 한 점뿐이면 완전제곱식이에요.", ty="02", tags=["빈출"]),
 dict(q="연립부등식 $\\begin{cases}x^2-5x-6<0\\\\ (x-1)(x-a)\\ge 0\\end{cases}$을 만족시키는 정수 $x$가 3개일 때, 정수 $a$의 값은? (단, $a>1$)", ch=["2", "3", "4", "5", "6"], ans="④",
      sol="첫째 $-1<x<6$ → 정수 $0\\sim5$. 둘째 $x\\le 1$ 또는 $x\\ge a$ → $0,1$과 $a\\sim5$ → $2+(6-a)=3$ → $a=5$", trap="둘째 부등식은 등호 포함이라 $x=1$, $x=a$도 해예요.", ty="04", tags=["BOSS"], lv=3),
]
SVQ = [dict(ty="03", q="이차부등식 $ax^2+4x+a-3>0$의 해가 존재하지 않도록 하는 실수 $a$의 값의 범위를 구하는 과정을 서술하시오.",
            ans="$a\\le -1$", rb=[("$a=0$일 때 해가 있음을 확인", "20 %"), ("$a<0$, $\\frac{D}{4}\\le 0$ 조건 세우기", "40 %"), ("$a^2-3a-4\\ge 0$ 풀어 공통부분 $a\\le -1$", "40 %")],
            sol="$a<0$이고 $4-a(a-3)\\le 0$ → $a\\le -1$", h=55),
       dict(ty="05", q="길이가 20 m인 철망으로 한쪽 면이 벽인 직사각형 울타리를 만들 때, 넓이가 48 m² 이상이 되도록 하는 벽에 수직인 변의 길이 $x$ m의 범위를 구하는 과정을 서술하시오.",
            ans="$4\\le x\\le 6$", rb=[("넓이를 $x(20-2x)$로 나타내기", "30 %"), ("부등식 $x^2-10x+24\\le 0$ 세우기", "30 %"), ("$4\\le x\\le 6$ (길이 조건 $0<x<10$ 확인)", "40 %")],
            sol="$x(20-2x)\\ge48$ → $(x-4)(x-6)\\le 0$", h=55)]

CC = [("이차부등식과 그래프", "$y=ax^2+bx+c$ ($a>0$)의 그래프가 $x$축과 $\\alpha,\\beta$에서 만나면 $<0$의 해는 <span class=mk>두 근 사이</span>, $>0$의 해는 <span class=mk>두 근 바깥</span>.", "$(x-1)(x-4)<0$ → $1<x<4$"),
      ("판별식과 해", "$D>0$: 두 근 사이/바깥 · $D=0$: $(x-\\alpha)^2$ 꼴 · $D<0$: 그래프가 $x$축과 만나지 않음 → <b>모든 실수</b> 또는 <b>해 없음</b>.", "$x^2+1>0$ → 모든 실수"),
      ("해가 주어진 부등식 만들기", "해가 $\\alpha<x<\\beta$ ⇔ $(x-\\alpha)(x-\\beta)<0$. 최고차항이 음수면 부등호가 뒤집혀요.", "해 $x<1$ 또는 $x>3$ → $(x-1)(x-3)>0$"),
      ("항상 성립 · 해가 없음", "모든 $x$에서 $ax^2+bx+c>0$ ⇔ $a>0,\\ D<0$. 해가 없음 ⇔ 반대 부등식이 항상 성립.", "$a=0$인 경우를 꼭 따로 확인"),
      ("연립이차부등식", "각 부등식의 해를 <b>한 수직선</b> 위에 그리고 공통부분. 끝점의 포함(●)·불포함(○)을 표시.", "정수 해 개수 문제는 끝점에서 실수가 많아요"),
      ("절댓값이 있는 부등식", "$x^2=|x|^2$를 이용하거나 $x\\ge0$, $x<0$으로 나누어 풀어요.", "$x^2-2|x|-3<0$ → $|x|<3$")]

spec = dict(
    brand=dict(academy="새봄수학학원", mark="봄", slogan="장유 · 한 명 한 명 끝까지", teacher="원장 선생님"),
    meta=dict(theme="math", subject="math", grade="고등학교 1학년", unit="공통수학1 · 이차부등식과 연립부등식",
              title="이차부등식<br>그래프로 꿰뚫기", sub="해의 구조 → 미정계수 → 항상 성립 → 연립·정수 해까지 학교 시험 핵심만", curri="2022 개정 교육과정 · 공통수학1 Ⅱ 방정식과 부등식",
              art=('<svg viewBox="0 0 360 300" width="100%"><g stroke="#fff" stroke-width="3" fill="none"><path d="M20 200 H340" opacity=".6"/><path d="M60 40 Q180 380 300 40" stroke="#FFE680" stroke-width="5"/></g>'
                   '<path d="M108 200 H252" stroke="#F2683A" stroke-width="12" stroke-linecap="round"/><circle cx="108" cy="200" r="9" fill="#fff" stroke="#F2683A" stroke-width="4"/><circle cx="252" cy="200" r="9" fill="#fff" stroke="#F2683A" stroke-width="4"/>'
                   '<text x="180" y="250" fill="#fff" font-size="26" font-weight="900" text-anchor="middle" font-family="Noto Sans CJK KR">α ＜ x ＜ β</text></svg>'),
              inside=[("개념 · 필수 예제 · 기본 16", "왜 그럴까? 원리 노트"), ("유형 5", "예제 보고 따라 풀기"), ("실전 5", "학교 시험형 + BOSS"), ("해설", "끝점 함정까지")]),
    plan=dict(goals=["이차부등식의 해를 <span class=mk>그래프와 연결</span>해 구할 수 있다.", "해가 주어진 부등식·항상 성립하는 부등식의 미정계수를 구할 수 있다.",
                     "연립이차부등식의 <b>정수 해의 개수</b> 조건을 다룰 수 있다."],
              link=("이어지는 공부", "이차방정식·판별식 → 이차함수 그래프 → <b>이차부등식</b> → 경우의 수·행렬"),
              map=[[("이차방정식", "근 · 판별식", 0), ("이차함수", "그래프와 x축", 0)], [("이차부등식", "두 근 사이 / 바깥", 1)],
                   [("미정계수", "해가 주어진 부등식", 0), ("항상 성립", "D＜0", 0), ("연립", "공통부분 · 정수 해", 0)], [("다음 단원", "경우의 수", 1)]],
              rows=[("개념 정리 + 개념 확인", "개념"), ("Level 1 대표 유형 01~05", "대표 유형"), ("Level 2 실전 · Level 3 서술형", "실전"), ("스스로 점검 · 오답 노트", "자기 평가"), ("정답과 해설로 채점하기", "정답과 해설")],
              msg="부등식은 <b>그래프를 그리는 순간</b> 쉬워져요. 끝점이 포함인지(●) 아닌지(○)만 정확히 표시해도 시험 점수가 달라져요. 문제 번호 아래 □□□에 회독 체크!"),
    next=[("Level 1 틀림", "개념 그래프를 다시 그리고 대표 예제 다시 풀기"), ("Level 2 2개↓", "‘오답 함정’의 끝점 조건을 수직선으로 다시 확인"),
          ("Level 3 감점", "채점 기준표에서 빠진 조건(a＝0, 길이＞0)을 오답 노트에 쓰기"), ("모두 맞힘", "다음 단원 ‘경우의 수’로 GO!")],
    teacher=dict(
        sessions=[("1회차", "그래프로 이차부등식 · 판별식과 해 → 유형 01~02", "유형 01~02 따라 풀기"),
                  ("2회차", "항상 성립·해 없음 · 연립이차부등식 → 유형 03~04 (수직선 그리기)", "유형 03~04 따라 풀기"),
                  ("3회차", "활용 유형 05 · Level 2 실전 · BOSS 함께 도전", "서술형 · 오답 노트 · 자기 평가")],
        levels=[("기초반", "유형 01·02·04 중심 · 수직선 그리기 반복"), ("기본반", "Level 1 숙제 → Level 2 전체 · 서술형 1문항"), ("심화반", "Level 2~3 + BOSS · 조건이 바뀐 문제 직접 만들어 보기")],
        tips=["모든 문제는 찰칵출판사가 새로 만든 문항이며, 정답은 계산(정수 전수·유리수 격자 조사)으로 전부 검산했습니다.",
              "학원 이름·로고·선생님 말씀은 원하시는 대로 바꿔 드립니다. 학교·교과서 출판사·시험 범위에 맞춘 챕터도 만들어 드립니다.",
              "문제 번호 아래 □□□는 학생 3회독 체크, 쪽 아래 ‘확인’ 칸은 선생님 도장 자리입니다.",
              "자기 평가 쪽의 ‘학부모 확인’ 칸으로 상담·학부모 연락에 바로 쓰실 수 있습니다."]),
    pages=[
        dict(sec="개념", head=[("band", "개념원리 이해", "01 이차부등식")], blocks=[("html", PI.C1)]),
        dict(sec="개념", head=[("band", "필수 예제", "개념을 문제로 연결하기")], blocks=[("html", PI.C2)]),
        dict(sec="개념", head=[("band", "기본 다지기", "개념 바로 적용 16문제")], blocks=[("html", PI.C3)]),
        dict(sec="대표 유형", cols=True, head=[("lv", 1, "대표 유형 익히기 · 예제 보고 따라 풀기", "모두 맞히기")], blocks=list(TY)),
        dict(sec="실전", head=[("lv", 2, "학교 시험 · 학평 수준 실전", "5문제 중 4개 이상")], cols=True,
             blocks=[("endtype",)] + [("q", p) for p in L2] + [("group", [("lv", 3, "풀이 과정을 쓰는 서술형", "채점 기준 80%↑"), ("essay", SVQ[0])]), ("essay", SVQ[1])]),
        dict(kind="selfcheck"), dict(kind="answers"), dict(kind="teacher"),
    ])

if __name__ == "__main__":
    qa = pdf(build(spec), "/home/claude/tbook/out/고1수학_이차부등식.pdf")
    for r in qa: print(r)
