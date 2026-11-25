import sys; sys.path.insert(0,"/home/claude/tbook")
import copy, pypdf, s_hs1_ineq as S, pro_ineq as PI
from engine import build, pdf
def guide_pdf(brand=None, out="/home/claude/tbook/out/guide.pdf"):
    sp=copy.deepcopy(S.spec)
    if brand: sp["M"].update(brand) if "M" in sp else None
    sp["pages"]=[dict(sec="선생님 안내",head=[("band","FOR TEACHERS","선생님 1분 사용 안내")],blocks=[("html",PI.GUIDE)])]
    pdf(build(sp), out); return out
if __name__=="__main__":
    print(guide_pdf())
