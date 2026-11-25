# 저작권 유사도 검사: 우리 문항 vs 참고 자료(EBS·평가원 PDF 텍스트) — 영어 7단어 연속, 한글 15글자 연속 일치를 찾음
import re, glob, sys, json, html
corp = " ".join(open(f, errors="ignore").read() for f in glob.glob("/home/claude/tbook/corpus/*.txt"))
en_words = re.findall(r"[a-z']+", corp.lower()); EN = set(tuple(en_words[i:i+7]) for i in range(len(en_words)-6))
ko = re.sub(r"[^가-힣0-9]", "", corp); KO = set(ko[i:i+15] for i in range(len(ko)-14))
STEMS = ["서로 다른 두 개의 주사위를 동시에 던질 때", "서로 다른 두 개의 주사위", "동시에 던질 때 일어나는 모든 경우의 수", "만들 수 있는 두 자리 자연수의 개수를 구하시오", "회장 1명, 부회장 1명을 뽑는",
         "이에 대한 설명으로 옳은 것만을", "옳은 것만을 <보기>에서 있는 대로 고른 것은", "있는 대로 고른 것은", "다음 글의 요지로 가장 적절한 것은", "다음 글의 주제로 가장 적절한 것은",
         "다음 글의 제목으로 가장 적절한 것은", "글의 내용을 한 문장으로 요약하고자 한다"]  # 시험 공통 발문(저작물 아님)
def check(text):
    t = html.unescape(re.sub("<[^>]+>|\\$[^$]*\\$", " ", text))
    for st in STEMS: t = t.replace(st, " ").replace(st.replace("<보기>", "&lt;보기&gt;"), " ")
    t = html.unescape(t).replace("<보기>", " ")
    for st in STEMS: t = t.replace(st.replace("<보기>", " "), " ")
    w = re.findall(r"[a-z']+", t.lower()); hitsE = [" ".join(w[i:i+7]) for i in range(len(w)-6) if tuple(w[i:i+7]) in EN and sum(len(x) > 1 for x in w[i:i+7]) >= 4]
    k = re.sub(r"[^가-힣0-9]", "", t); hitsK = [k[i:i+15] for i in range(len(k)-14) if k[i:i+15] in KO]
    return hitsE, hitsK
if __name__ == "__main__":
    import importlib.util
    total = 0; bad = []
    for mod in sys.argv[1:]:
        spec = importlib.util.spec_from_file_location("m", mod); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        from engine import Book
        b = Book(m.spec); b.render()
        for a in b.ans:
            txt = str(a.get("q", "")) + " " + " ".join(map(str, a.get("ch") or []))
            e, k = check(txt); total += 1
            if e or k: bad.append((mod.split("/")[-1], a["n"], e[:3], k[:3]))
    print(json.dumps(dict(checked=total, flagged=bad), ensure_ascii=False, indent=1))
