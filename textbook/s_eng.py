import sys; sys.path.insert(0, "/home/claude/tbook")
from engine import build, pdf

def ps(t): return f'<div class=ps>{t}</div>'
Q_MAIN = "다음 글의 요지로 가장 적절한 것은?"
Q_TOPIC = "다음 글의 주제로 가장 적절한 것은?"
Q_TITLE = "다음 글의 제목으로 가장 적절한 것은?"

P = {}
P["study"] = ("Many students believe that the more hours they spend at their desks, the more they will learn. They copy notes again and again, highlight entire pages, and reread chapters until the words feel familiar. Unfortunately, familiarity is not the same as understanding. When you reread a page, your brain recognizes the sentences and sends a comforting signal that you already know them. But recognition is much easier than recall. A more effective way is to close the book and try to explain the main ideas in your own words, or to solve problems without looking at the examples. This feels harder and slower, and you will make mistakes. Yet those small struggles are exactly what make memories stronger. <u>In short, how you study matters far more than how long you study.</u>")
P["trees"] = ("On a hot summer afternoon, the temperature in a neighborhood without trees can be several degrees higher than in a nearby area lined with them. Asphalt and concrete absorb sunlight during the day and release the heat slowly at night, so people in such areas get little relief even after sunset. Trees work differently. Their leaves block sunlight before it reaches the ground, and they release water vapor that cools the surrounding air. For this reason, some cities now treat trees not as decoration but as public infrastructure, just like roads and water pipes. They map where shade is missing and plant trees first in the places where elderly people and children spend the most time outdoors. Planting a tree, in other words, can be a health policy.")
P["teen"] = ("Parents often complain that teenagers stay up too late and cannot get up in the morning. It is easy to see this as laziness, but biology tells a different story. During adolescence, the body begins to release melatonin, the hormone that makes us sleepy, about one to two hours later than it did in childhood. As a result, many teenagers are simply not tired at ten o'clock, even if they want to be. When school starts early, they are forced to wake up in the middle of their natural sleep cycle, which is like asking an adult to get up at four in the morning. Some schools that pushed back their starting time found that students were late less often and paid more attention in class.")
P["ants"] = ("When an ant finds food, it returns to the nest leaving a chemical trail behind it. Other ants follow the trail and add their own chemicals as they go. At first, ants may travel along several different routes. However, ants on a shorter route complete their trips more quickly, so that route is marked again and again in the same amount of time. The chemical signal on the longer routes, meanwhile, fades away. After a while, almost the entire colony uses the shortest path, even though no single ant ever compared the routes. Engineers have borrowed this idea to design systems that find efficient delivery routes and manage traffic in computer networks.")
P["bored"] = ("We rarely allow ourselves to be bored anymore. The moment we have to wait for a bus or stand in line, we reach for our phones. Yet researchers have found that boredom is not simply a waste of time. In one experiment, people who first completed a dull task, such as copying numbers from a long list, later came up with more creative uses for everyday objects than those who skipped the dull task. When the mind has nothing interesting to focus on, it begins to wander, connecting distant memories and ideas in unexpected ways. So the next time you feel bored, try leaving your phone in your pocket. Your brain may be getting ready to do something surprising.")
P["sample"] = ("Walk through a supermarket on a weekend and you will probably be offered a free sample of cheese or dumplings. It seems like a simple act of kindness, but it is also a clever selling strategy. When someone gives us something, even something small, we feel a quiet pressure to give something back. Many shoppers who accept a sample end up buying the product, not because it tasted especially good, but because walking away feels a little rude. Charities use the same principle when they include a small gift, such as a pen or a set of stickers, with a request for donations. Understanding this tendency won't make free samples less tasty, but it can help you decide what you really want to buy.")
P["piano"] = ("Beginning piano students often play a difficult passage at full speed, stumbling over the same notes each time. They hope that repetition alone will eventually smooth things out. Experienced teachers, however, give the opposite advice: slow down. When you play slowly enough to make no mistakes, your fingers learn the correct movements instead of the errors. Each time you repeat a mistake, you are actually practicing it, making it harder to remove later. Once the passage feels easy at a slow tempo, you can raise the speed little by little. It may seem like a longer path, but it is usually the fastest way to play a piece well.")
P["recycle"] = ("Many people put items in the recycling bin simply because they hope those items can be recycled. A greasy pizza box, a plastic bag, or a coffee cup with a thin plastic lining may look recyclable, but they often are not. This habit, sometimes called ‘wish-cycling,’ does more harm than good. A single dirty item can contaminate a whole batch of paper or plastic, and workers must remove the wrong items by hand, which slows down the process and raises costs. In some cases, entire loads end up in landfills. Recycling works best not when we put more things in the bin, but when we put the right things in it.")
P["meeting"] = ("In many meetings, the first person to speak has a surprising amount of influence. Once an opinion is stated out loud, especially by a confident or senior member, others tend to adjust their own views toward it rather than offer something completely different. Doubts remain unspoken, and the group may agree quickly on an idea that few people truly support. One simple way to avoid this is to have everyone write down their thoughts before any discussion begins. When ideas are collected first and shared afterward, quieter members are heard, and the group can compare a wider range of options. Good decisions depend less on who speaks first than on how many voices reach the table.")
P["map"] = ("A map that showed every tree, stone, and blade of grass would be as large as the land itself and therefore useless. A map is valuable precisely because it leaves things out. A subway map, for example, ignores real distances and the shapes of streets, yet it is the best tool for getting from one station to another. The same is true of the models we use to understand the world, from weather forecasts to economic predictions. Each one simplifies reality in order to answer a particular question. Problems arise not when a model is simple, but when we forget what it has left out and use it to answer a question it was never designed for.")
P["gap"] = ("Why do we keep watching one more episode? Many shows end with a question left unanswered: a character in danger, a secret about to be revealed. Psychologists call this the ‘curiosity gap,’ the uncomfortable feeling we get when we know that something is missing from our knowledge. That small discomfort pushes us to look for the answer. Good teachers use the same tool. Instead of giving the explanation first, they start with a puzzling question, and students lean forward to find out more.")

for k, v in P.items():  # 지문 길이 점검 (고1 학평 수준 110~170단어)
    n = len(v.replace("<u>", "").replace("</u>", "").split())
    assert 70 <= n <= 175, (k, n)

def gl(words): return '<div class=gl>* ' + " &nbsp;* ".join(f"<i>{w}</i> {m}" for w, m in words) + "</div>"

def item(stem, key, ch, ans, sol, trap="", glo=None, lv=2, tags=None, ty=None, gap=8):
    d = dict(q=f'{stem}{ps(P[key])}' + (gl(glo) if glo else ""), ch=ch, ans=ans, sol=sol, trap=trap, lv=lv, gap=gap, tr=TR.get(key, ""))
    if tags: d["tags"] = tags
    if ty: d["ty"] = ty
    if ch and all(ord(c[0]) > 0x3000 for c in ch): d["opcls"] = "v ko"
    return d

TR = {"trees": "무더운 여름 오후, 나무가 없는 동네의 기온은 나무가 늘어선 근처 지역보다 몇 도나 더 높을 수 있다. 아스팔트와 콘크리트는 낮 동안 햇빛을 흡수했다가 밤에 천천히 열을 내보내서, 그런 곳의 사람들은 해가 진 뒤에도 더위를 거의 피하지 못한다. 나무는 다르게 작용한다. 잎은 햇빛이 땅에 닿기 전에 막고, 수증기를 내보내 주변 공기를 식힌다. 이런 이유로 일부 도시는 이제 나무를 장식이 아니라 도로나 수도관처럼 공공 기반 시설로 다룬다. 그늘이 부족한 곳을 지도로 그리고, 노인과 어린이가 밖에서 가장 오래 지내는 곳부터 나무를 심는다. 다시 말해 나무 한 그루를 심는 것이 보건 정책이 될 수 있다.", "ants": "개미는 먹이를 찾으면 화학 물질 흔적을 남기며 둥지로 돌아간다. 다른 개미들은 그 흔적을 따라가며 자신의 화학 물질을 더한다. 처음에는 여러 길로 다닐 수 있다. 하지만 짧은 길의 개미가 더 빨리 왕복하므로, 같은 시간 동안 그 길이 더 자주 표시된다. 반면 긴 길의 신호는 사라진다. 얼마 후 군집 거의 전체가 가장 짧은 길을 쓰는데, 어떤 개미도 길을 비교한 적이 없다. 기술자들은 이 생각을 빌려 효율적인 배송 경로를 찾고 컴퓨터 네트워크의 통신량을 관리하는 시스템을 설계했다.", "sample": "주말에 마트를 걸으면 치즈나 만두 시식을 권유받을 것이다. 단순한 친절처럼 보이지만 영리한 판매 전략이기도 하다. 누군가 작은 것이라도 주면 우리는 무언가 돌려줘야 한다는 조용한 압박을 느낀다. 시식한 많은 손님이 결국 상품을 사는데, 특별히 맛있어서가 아니라 그냥 가 버리는 게 조금 무례하게 느껴지기 때문이다. 자선 단체도 기부 요청에 펜이나 스티커 같은 작은 선물을 넣을 때 같은 원리를 쓴다. 이 경향을 안다고 시식이 덜 맛있어지지는 않지만, 정말 사고 싶은 게 무엇인지 판단하는 데 도움이 된다.", "piano": "피아노 초보자들은 어려운 부분을 빠른 속도로 치다가 매번 같은 음에서 걸려 넘어진다. 반복만 하면 언젠가 매끄러워지리라 기대한다. 하지만 경험 많은 선생님들은 반대로 조언한다. 천천히 치라고. 실수하지 않을 만큼 천천히 치면 손가락은 실수 대신 바른 움직임을 배운다. 실수를 반복할 때마다 사실 그 실수를 연습하는 것이어서 나중에 없애기 더 어려워진다. 느린 속도에서 쉽게 느껴지면 조금씩 속도를 올리면 된다. 더 먼 길처럼 보여도, 대개 곡을 잘 치게 되는 가장 빠른 길이다.", "recycle": "많은 사람이 재활용되기를 ‘바라는’ 마음만으로 물건을 재활용 통에 넣는다. 기름 묻은 피자 상자, 비닐봉지, 얇은 플라스틱 코팅이 된 커피 컵은 재활용될 것 같지만 대개 그렇지 않다. ‘위시사이클링’이라고도 불리는 이 습관은 득보다 실이 크다. 더러운 물건 하나가 종이나 플라스틱 한 묶음 전체를 오염시킬 수 있고, 작업자가 잘못된 물건을 손으로 골라내야 해서 처리가 늦어지고 비용이 오른다. 때로는 통째로 매립지로 간다. 재활용은 통에 더 많이 넣을 때가 아니라, 맞는 것을 넣을 때 가장 잘 된다.", "meeting": "많은 회의에서 처음 말하는 사람은 놀랄 만큼 큰 영향력을 가진다. 의견이 소리 내어 나오면, 특히 자신감 있거나 높은 사람의 의견이면, 다른 사람들은 전혀 다른 의견을 내기보다 자기 생각을 그쪽으로 맞춘다. 의심은 말해지지 않고, 진심으로 지지하는 사람이 적은 생각에 모두가 빨리 동의하기도 한다. 이를 피하는 간단한 방법은 토론 전에 모두가 생각을 적게 하는 것이다. 의견을 먼저 모은 뒤 나누면 조용한 사람의 목소리도 들리고 더 다양한 선택지를 비교할 수 있다. 좋은 결정은 누가 먼저 말하느냐보다 얼마나 많은 목소리가 테이블에 닿느냐에 달려 있다.", "map": "나무, 돌, 풀잎 하나까지 다 보여 주는 지도는 땅만큼 커서 쓸모가 없을 것이다. 지도는 바로 무언가를 빼기 때문에 가치가 있다. 예를 들어 지하철 노선도는 실제 거리와 길 모양을 무시하지만, 역에서 역으로 가는 데는 가장 좋은 도구다. 일기 예보에서 경제 예측까지, 세상을 이해하려고 쓰는 모형도 마찬가지다. 각각은 특정한 질문에 답하려고 현실을 단순화한다. 문제는 모형이 단순할 때가 아니라, 무엇을 뺐는지 잊고 원래 만들어지지 않은 질문에 그 모형을 쓸 때 생긴다.", "gap": "우리는 왜 한 회만 더 보게 될까? 많은 드라마는 위험에 처한 인물, 밝혀지기 직전의 비밀처럼 답 없는 질문으로 끝난다. 심리학자들은 이를 ‘호기심의 틈’이라 부르는데, 내 지식에 무언가 빠져 있다는 걸 알 때 드는 불편한 느낌이다. 그 작은 불편함이 우리가 답을 찾게 만든다. 좋은 선생님도 같은 도구를 쓴다. 설명을 먼저 주는 대신 알쏭달쏭한 질문으로 시작하면, 학생들은 더 알고 싶어 몸을 앞으로 기울인다."}

TY = [
 ("type", dict(no="01", name="글의 요지 찾기 <small style='font-weight:500;color:#6b7280'>(학평 22번 유형)</small>",
  idea="요지는 <b>글쓴이가 하고 싶은 말 한 문장</b>. <span class=mk>In short · Therefore · However</span> 뒤, 또는 반복되는 핵심어가 모인 문장을 찾으세요.",
  ex=dict(q=Q_MAIN + ps(P["study"]) + '<div class="op v ko">' + "".join(f"<i>{n} {c}</i>" for n, c in zip("①②③④⑤", [
      "공부 시간을 늘리는 것이 성적 향상의 핵심이다.", "학습 효과는 시간보다 스스로 떠올려 보는 방식에 달려 있다.", "노트 필기는 내용을 오래 기억하는 데 도움이 된다.",
      "실수를 줄이려면 예제를 반복해서 읽어야 한다.", "익숙한 내용부터 공부해야 자신감이 생긴다."])) + "</div>",
   steps=[("STEP 1", "반복되는 말 찾기 → <i>recall · explain in your own words · struggles</i>"), ("STEP 2", "신호어 문장 → <i>In short, how you study matters far more than how long you study.</i>"),
          ("STEP 3", "선택지 비교 → ①은 글쓴이가 반박하는 생각(시간), ③④는 본문이 비판한 방법")], a="②"))),
 ("q", item(Q_MAIN, "trees", ["도시의 도로 포장재를 친환경 소재로 바꿔야 한다.", "노인과 어린이는 여름철 야외 활동을 줄여야 한다.", "도시의 나무는 주민 건강을 지키는 기반 시설로 다루어야 한다.",
                              "나무는 장식 효과가 커서 도시 미관을 개선한다.", "밤 기온을 낮추려면 에어컨 사용을 늘려야 한다."], "③",
            "도심 열기를 나무가 낮추므로, 나무를 장식이 아닌 <b>공공 기반 시설</b>로 보고 심어야 한다는 글. 마지막 문장 <i>Planting a tree ... can be a health policy</i>가 요지.",
            "④ ‘장식(decoration)’은 글쓴이가 <b>not as decoration</b>이라며 부정한 말이에요.", glo=[("asphalt", "아스팔트"), ("infrastructure", "기반 시설")], lv=1)),
 ("type", dict(no="02", name="글의 주제 찾기 <small style='font-weight:500;color:#6b7280'>(학평 23번 유형)</small>",
  idea="주제는 요지를 <b>짧은 영어 명사구</b>로 줄인 것. 너무 넓거나(전체 과학), 너무 좁은(한 예시) 선택지는 지워요.",
  ex=dict(q=Q_TOPIC + ps(P["teen"]) + gl([("adolescence", "청소년기"), ("melatonin", "멜라토닌(수면 호르몬)")]) + '<div class="op en">' + "".join(f"<i>{n} {c}</i>" for n, c in zip("①②③④⑤", [
      "reasons why teenagers should exercise in the morning", "a biological explanation for teenagers’ late sleep patterns", "the negative effects of smartphones on sleep quality",
      "how parents can teach their children good habits", "the importance of eating breakfast before school"])) + "</div>",
   steps=[("STEP 1", "첫 문장의 통념 → ‘10대는 게을러서 늦게 잔다’"), ("STEP 2", "반전 신호 <i>but biology tells a different story</i> → 생물학적 이유(멜라토닌)"),
          ("STEP 3", "③ 스마트폰, ⑤ 아침밥은 본문에 없는 내용 → 지우기")], a="②"))),
 ("q", item(Q_TOPIC, "ants", ["the dangers ants face when searching for food", "how simple individual actions produce an efficient group solution", "differences between ants and other social insects",
                              "why chemical signals are harmful to the environment", "the history of computer network design"], "②",
            "개미 한 마리는 길을 비교하지 않지만, 흔적을 남기는 단순한 행동이 모여 무리 전체가 <b>가장 짧은 길</b>을 찾게 된다는 글.",
            "⑤는 마지막 문장에 나온 <b>예시 하나</b>일 뿐, 글 전체의 주제가 아니에요.", glo=[("colony", "(개미 등의) 군집")], lv=2)),
 ("type", dict(no="03", name="글의 제목 찾기 <small style='font-weight:500;color:#6b7280'>(학평 24번 유형)</small>",
  idea="제목은 <b>요지 + 흥미</b>. 비유나 질문 형태도 많아요. 먼저 요지를 우리말로 정리한 뒤 같은 뜻의 제목을 고르세요.",
  ex=dict(q=Q_TITLE + ps(P["bored"]) + '<div class="op en">' + "".join(f"<i>{n} {c}</i>" for n, c in zip("①②③④⑤", [
      "Why Waiting in Line Makes Us Angry", "Boredom: A Hidden Door to Creativity", "Smartphones Help Us Think Faster", "How to Finish Dull Tasks Quickly", "Memory Loss in the Digital Age"])) + "</div>",
   steps=[("STEP 1", "요지를 우리말로 → ‘지루함은 창의성을 깨운다’"), ("STEP 2", "근거 문장 → <i>boredom is not simply a waste of time</i>, 실험 결과"),
          ("STEP 3", "<i>Hidden Door</i>(숨은 문) 같은 비유도 요지와 같으면 정답!")], a="②"))),
 ("q", item(Q_TITLE, "sample", ["Free Samples: Gifts That Ask for Something Back", "How Supermarkets Keep Food Fresh", "The Hidden Cost of Charity Work",
                                "Why Shoppers Prefer Cheese to Dumplings", "Kindness Always Makes People Happy"], "①",
            "무료 시식은 친절처럼 보이지만, 받으면 <b>보답하고 싶은 심리</b>를 이용한 판매 전략이라는 글.",
            "⑤ ‘친절은 늘 행복하게 한다’는 글쓴이의 주장과 반대 방향이에요.", lv=2)),
]

L2 = [
 item(Q_MAIN, "piano", ["연습할 곡은 쉬운 것부터 골라야 한다.", "악기 연습은 매일 같은 시간에 하는 것이 좋다.", "실수 없이 천천히 연습하는 것이 결국 가장 빠른 길이다.",
                        "실수를 두려워하지 말고 빠르게 반복해야 한다.", "좋은 선생님을 만나는 것이 실력 향상의 핵심이다."], "③",
      "실수를 반복하면 실수를 연습하게 되므로, <b>틀리지 않을 만큼 천천히</b> 연습한 뒤 속도를 올리는 것이 가장 빠르다는 글.",
      "④는 글 앞부분 초보자들의 생각(빠르게 반복)이에요. <i>however</i> 뒤가 글쓴이의 생각!", ty="01", tags=["빈출"]),
 item(Q_TOPIC, "recycle", ["the rising cost of building new landfills", "the problems caused by recycling items incorrectly", "ways to reduce the use of pizza boxes",
                           "why workers prefer sorting plastic by hand", "the history of recycling programs in cities"], "②",
      "재활용될 것이라 ‘바라며’ 아무거나 넣는 습관(wish-cycling)이 오염·비용·매립을 일으킨다는 글.",
      "①은 결과 중 하나(매립)만 다룬 <b>좁은</b> 선택지예요.", glo=[("contaminate", "오염시키다"), ("landfill", "쓰레기 매립지")], ty="02"),
 item(Q_TITLE, "meeting", ["Why Senior Members Should Lead Every Meeting", "Speak First, Win the Argument", "Write Before You Talk: Hearing Every Voice",
                           "Quick Agreement Makes Teams Stronger", "How to Stay Silent in Difficult Meetings"], "③",
      "회의에서 먼저 말한 사람의 의견에 끌려가는 문제를 막으려면, <b>토론 전에 각자 생각을 적게</b> 해야 한다는 글.",
      "②는 첫 발언자의 영향력을 ‘좋은 전략’처럼 바꿔 버린 함정이에요.", ty="03"),
 item(Q_MAIN, "map", ["지도는 실제 거리를 정확하게 반영해야 한다.", "복잡한 모형일수록 현실을 더 잘 설명한다.", "모형은 단순화의 산물이므로 목적과 한계를 알고 사용해야 한다.",
                      "일기 예보와 경제 예측은 믿을 만하지 않다.", "지하철 노선도는 여행자에게 가장 유용한 지도이다."], "③",
      "지도·예보 같은 모형은 무언가를 <b>빼서</b> 쓸모가 생긴다. 문제는 단순함이 아니라, 무엇을 뺐는지 잊고 원래 목적 밖에 쓰는 것.",
      "⑤는 예시를 일반화한 <b>좁은</b> 선택지, ②는 글과 정반대예요.", lv=3, tags=["BOSS"], ty="01", gap=6),
]

ESSAY = dict(ty="01", h=26, tr=TR["gap"],
  q="다음 글을 읽고, 글의 내용을 한 문장으로 요약하고자 한다. 빈칸 (A), (B)에 들어갈 말을 본문에서 찾아 쓰시오. (단, (B)는 어법에 맞게 쓸 것)" + ps(P["gap"]) +
    '<div class=bogi style="font-family:Lora,serif"><div class=bt>요약문</div>When people notice a(n) &nbsp;(A)&nbsp;<span class=blank></span> in their knowledge, the small discomfort &nbsp;(B)&nbsp;<span class=blank></span> them to search for the answer.</div>',
  ans="(A) gap (B) pushes", rb=[("(A) gap", "40 %"), ("(B) pushes", "40 %"), ("(B)를 주어 the small discomfort에 맞게 3인칭 단수형으로 씀", "20 %")],
  sol="모르는 부분이 있다는 걸 알 때 생기는 불편함(curiosity gap)이 답을 찾게 만든다. 본문 <i>That small discomfort pushes us to look for the answer.</i>")

def strip(h):
    import re
    return re.sub("<[^>]+>", " ", h)

spec = dict(
    brand=dict(academy="새봄영어학원", mark="E", slogan="장유 · 읽히는 영어, 풀리는 독해", teacher="원장 선생님"),
    meta=dict(theme="eng", subject="eng", grade="고등학교 1학년", unit="Unit 01. 요지 · 주제 · 제목", font="'Noto Serif CJK KR',serif", fs="10.2pt",
              title="수능형 독해<br>핵심을 잡는 눈", sub="요지 · 주제 · 제목 — 30초 안에 글의 중심을 잡는 연습", curri="2022 개정 교육과정 · 공통영어 / 수능·학평 독해 대비",
              art=('<svg viewBox="0 0 360 300" width="100%" font-family="Lora,serif">'
                   '<rect x="40" y="30" width="200" height="250" rx="10" fill="#fff" stroke="#1b1f24" stroke-width="2.5" transform="rotate(-6 140 155)"/>'
                   + "".join(f'<rect x="{62}" y="{60+i*20}" width="{150 if i%4 else 110}" height="6" rx="3" fill="#C9C4F0" transform="rotate(-6 140 155)"/>' for i in range(10))
                   + '<rect x="58" y="136" width="160" height="12" rx="3" fill="#FFE680" transform="rotate(-6 140 155)"/>'
                   '<g transform="translate(250 175)"><circle r="62" fill="none" stroke="#fff" stroke-width="10"/><circle r="62" fill="rgba(255,255,255,.15)"/><path d="M44 44 L92 92" stroke="#fff" stroke-width="16" stroke-linecap="round"/>'
                   '<text y="-6" text-anchor="middle" fill="#FFE680" font-size="26" font-weight="700">Main</text><text y="24" text-anchor="middle" fill="#fff" font-size="26" font-weight="700">Idea</text></g></svg>'),
              inside=[("전략 4", "핵심 찾는 법"), ("유형 3", "요지·주제·제목"), ("지문 11", "모두 새로 쓴 글"), ("해설", "오답 함정까지")]),
    plan=dict(goals=["글에서 <span class=mk>반복되는 핵심어와 신호어</span>를 찾아 중심 문장을 고를 수 있다.",
                     "요지(문장) · 주제(명사구) · 제목(요지+흥미)의 차이를 안다.", "너무 넓은 · 너무 좁은 · 반대 방향 선택지를 지울 수 있다."],
              link=("이어지는 공부", "중학 독해 → <b>Unit 01 요지·주제·제목</b> → Unit 02 빈칸 추론 → Unit 03 순서·삽입"),
              map=[[("통념 제시", "Many people believe…", 0), ("예시·근거", "For example…", 0)], [("반전 신호", "However · But · Yet", 1)],
                   [("요지", "글쓴이의 한 문장", 0), ("주제", "영어 명사구", 0), ("제목", "요지 + 흥미", 0)], [("다음 Unit", "빈칸 추론", 1)]],
              rows=[("독해 전략 + 개념 확인", "개념"), ("Level 1 대표 유형 01~03", "대표 유형"), ("Level 2 실전 · Level 3 서술형", "실전"), ("스스로 점검 · 오답 노트", "자기 평가"), ("정답과 해설로 채점하기", "정답과 해설")],
              msg="모든 문장을 다 해석하려고 하지 마세요! <b>반복되는 말</b>과 <b>However 뒤 한 문장</b>만 잡아도 절반은 풀려요. 한 지문에 <b>1분 30초</b> 목표, 문제 옆 □□□에 회독 체크!"),
    next=[("Level 1 틀림", "‘독해 전략’ 4개를 다시 읽고 대표 예제의 STEP을 소리 내어 따라 하기"), ("Level 2 2개↓", "‘오답 함정’을 읽고 틀린 선택지가 왜 넓은지/좁은지 써 보기"),
          ("Level 3 감점", "요약문의 주어·동사 수 일치 다시 확인하기"), ("모두 맞힘", "다음 Unit ‘빈칸 추론’으로 GO! 시간 재고 풀기")],
    teacher=dict(
        sessions=[("1회차", "훅 질문 → 독해 전략 4개 → 개념 확인 → 유형 01 대표 예제 함께 STEP 풀이", "유형 01 따라 풀기 + 어휘 미리 보기 암기"),
                  ("2회차", "어휘 테스트 → 유형 02·03 대표 예제 (선택지 지우기 연습)", "유형 02·03 따라 풀기"),
                  ("3회차", "Level 2 실전 (지문당 1분 30초 타이머) · BOSS 함께 도전", "서술형 요약문 · 오답 노트 · 자기 평가")],
        levels=[("기초반", "지문마다 핵심어에 동그라미 · Level 1 중심 · 해설의 우리말 요약 먼저 읽기"), ("기본반", "Level 1 숙제 → Level 2 시간 재고 풀기 · 서술형"),
                ("심화반", "Level 2~3 + BOSS · 오답 선택지가 틀린 이유를 영어로 설명하기")],
        tips=["모든 지문은 찰칵출판사가 직접 새로 쓴 글입니다(기출·EBS 지문 아님). 저작권 유사도 검사를 통과했습니다.",
              "학원 이름·로고·선생님 말씀은 원하시는 대로 바꿔 드립니다. 학교 교과서 범위에 맞춘 지문도 만들어 드립니다.",
              "문제 번호 아래 □□□는 학생 3회독 체크, 쪽 아래 ‘확인’ 칸은 선생님 도장 자리입니다.",
              "자기 평가 쪽의 ‘학부모 확인’ 칸으로 상담·학부모 연락에 바로 쓰실 수 있습니다."]),
    pages=[
        dict(sec="개념", head=[("band", "STRATEGY", "독해 전략 · 글의 중심 잡기")], blocks=[
            ("hook", "영어 지문 한 개, 30초 안에 요지를 잡을 수 있을까? 모든 문장을 해석할 필요는 없어요.", "비밀은 <b>반복되는 말</b>과 <b>However 뒤 한 문장</b>. 이 Unit에서 그 눈을 길러요!"),
            ("grid", [("concept", dict(no="1", t="중심 문장은 어디에?", body="<b>처음</b>(두괄식) · <b>끝</b>(미괄식) · <b>반전 뒤</b>(중괄식). 수능형 지문은 ‘통념 → 반전 → 주장’ 구조가 가장 많아요.", eg="Many people think A. <span class=mk>However, B.</span> → 요지는 B")),
                      ("concept", dict(no="2", t="신호어에 밑줄 긋기", body="<b>However · But · Yet · In fact</b> → 글쓴이의 진짜 생각<br><b>In short · Therefore · In other words</b> → 요약·결론", eg="<i>In short, how you study matters…</i> → 바로 요지!")),
                      ("concept", dict(no="3", t="요지 · 주제 · 제목", body="<b>요지</b>: 글쓴이의 주장 한 문장(우리말)<br><b>주제</b>: 글이 다루는 대상(영어 명사구)<br><b>제목</b>: 요지 + 흥미(비유·질문 가능)", eg="요지 ‘지루함은 창의성을 깨운다’ ↔ 제목 <i>Boredom: A Hidden Door to Creativity</i>")),
                      ("concept", dict(no="4", t="오답 선택지 3종 세트", body="① <b>너무 넓음</b>: 글보다 큰 이야기<br>② <b>너무 좁음</b>: 예시 하나만 다룸<br>③ <b>반대 · 본문에 없음</b>: 통념을 정답처럼", eg="개미 글에서 ‘컴퓨터 네트워크의 역사’ → 예시만 다룬 좁은 선택지"))]),
            ("voc", [("familiarity", "익숙함"), ("recall", "떠올리기, 회상"), ("infrastructure", "기반 시설"), ("adolescence", "청소년기"),
                     ("contaminate", "오염시키다"), ("tendency", "경향"), ("simplify", "단순화하다"), ("unspoken", "말해지지 않은")]),
            ("check", [("<i>However</i>, <i>In fact</i> 뒤에는 주로 글쓴이의 <span class=blank></span>이(가) 온다.", "주장(진짜 생각)"),
                       ("주제는 명사구, 요지는 <span class=blank></span>(으)로 나타낸다.", "문장"),
                       ("본문의 예시 하나만 다룬 선택지는 너무 <span class=blank></span> 선택지이다.", "좁은"),
                       ("<i>In short</i>가 이끄는 문장은 글의 <span class=blank></span>일 가능성이 높다.", "요지(요약)")])]),
        dict(sec="대표 유형", cols=True, one=True, head=[("lv", 1, "대표 유형 익히기 · STEP 보고 따라 풀기", "모두 맞히기")], blocks=TY),
        dict(sec="실전", head=[("lv", 2, "학력평가 수준 실전 · 지문당 1분 30초", "4문제 중 3개 이상")], cols=True, one=True,
             blocks=[("endtype",)] + [("q", p) for p in L2] + [("group", [("lv", 3, "요약문 완성 서술형", "채점 기준 80%↑"), ("essay", ESSAY)])]),
        dict(kind="selfcheck"), dict(kind="answers"), dict(kind="teacher"),
    ])

if __name__ == "__main__":
    import json
    json.dump({k: strip(v) for k, v in P.items()}, open("/home/claude/tbook/out/eng_passages.json", "w"), ensure_ascii=False)
    qa = pdf(build(spec), "/home/claude/tbook/out/고1영어_요지주제제목.pdf")
    for r in qa: print(r)
