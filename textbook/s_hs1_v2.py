import sys; sys.path.insert(0, "/home/claude/tbook")
from fractions import Fraction as F
import s_hs1_ineq as S, lesson_ineq as LI
from engine import build, pdf
G=[F(i,20) for i in range(-400,401)]
assert all(((2*x-3)*(x+1)<=0)==(-1<=x<=F(3,2)) for x in G)
assert all((x*x+2*x-8>0)==(x<-4 or x>2) for x in G)
assert all((x*x-x-6<0)==(-2<x<3) for x in G) and all((-x*x+3*x+10>=0)==(-2<=x<=5) for x in G) and all((x*x-9<0)==(-3<x<3) for x in G)
spec=dict(S.spec); pg=list(spec["pages"])
i=[k for k,p in enumerate(pg) if p.get("sec")=="개념"]
new=[dict(sec="개념",head=[("band","1회차 · 개념","이차부등식은 그래프로 ‘읽는’ 것")],blocks=[("html",LI.L1A)]),
     dict(sec="개념",head=[("band","1회차 · 연습","예제 → 따라 하기 → 혼자 풀기")],blocks=[("html",LI.L1B)])]
spec["pages"]=pg[:i[0]]+new+pg[i[-1]+1:]
if __name__=="__main__":
    for r in pdf(build(spec),"/home/claude/tbook/out/v2.pdf"): print(r)
