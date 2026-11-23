"""루루 1화 조립: 캡처 반쪽 2장씩 → 패널 → 말풍선(한/영) → 800px 세로 웹툰"""
from PIL import Image, ImageDraw, ImageFont
import math, os, sys

S = "/tmp/claude-chrome-screenshots-B89JL6/screenshot-"
P_ = "1795424"
H = {1: ("1795424685227-42", "1795424685228-43", 0), 2: ("1795424685229-44", "1795424685230-45", 0),
 3: ("1795424707316-46", "1795424707317-47", 0), 4: ("1795424707319-48", "1795424707320-49", 0),
 5: ("1795424730271-50", "1795424730273-51", 0), 6: ("1795424730275-52", "1795424730279-53", 0),
 7: ("1795424752553-54", "1795424752554-55", 0), 8: ("1795424752555-56", "1795424752556-57", 0),
 9: ("1795424774784-58", "1795424774785-59", 0), 10: ("1795424774786-60", "1795424774787-61", 0),
 11: ("1795424802243-62", "1795424802245-63", 0), 12: ("1795424802246-64", "1795424802248-65", 0)}
TOPX = {1: 0.18}
BOTX = {7: 0.50}   # 루루 발이 계산대 위에 보이는 부분 잘라내기
W = 800
FONT = {"ko": "/home/claude/minsung-ai/toon_tools/fonts/Jua-Regular.ttf",
        "en": "/home/claude/minsung-ai/toon_tools/fonts/ComicNeue-Bold.ttf"}
SFXF = "/home/claude/minsung-ai/toon_tools/fonts/BlackHanSans-Regular.ttf"
NARF = {"ko": "/home/claude/minsung-ai/toon_tools/fonts/GowunDodum-Regular.ttf",
        "en": "/home/claude/minsung-ai/toon_tools/fonts/PatrickHand-Regular.ttf"}
BG = (250, 246, 238)


def panel(n):
    a, b, hdr = H[n]
    A = Image.open(S + a + ".png").convert("RGB"); B = Image.open(S + b + ".png").convert("RGB")
    im = Image.new("RGB", (A.width, A.height + B.height)); im.paste(A, (0, 0)); im.paste(B, (0, A.height))
    top = int(A.height * TOPX[n]) if n in TOPX else (int(A.height * 0.115) if hdr else 0)          # 제미나이가 넣은 머리띠 글자 제거
    bot = int(B.height * BOTX.get(n, 0.24))                          # 오른쪽 아래 반짝이 표시 제거
    im = im.crop((0, top, im.width, im.height - bot))
    return im.resize((W, round(im.height * W / im.width)), Image.LANCZOS)


def wrap(d, text, f, maxw):
    out = []
    for para in text.split("\n"):
        words = para.split(" ") if " " in para else list(para)
        line = ""
        for w in words:
            t = (line + " " + w).strip() if " " in para else line + w
            if d.textlength(t, font=f) > maxw and line:
                out.append(line); line = w
            else:
                line = t
        out.append(line)
    return out


def bubble(img, text, cx, cy, tail=None, size=30, font="", shout=False, maxw=330):
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(font, size)
    lines = wrap(d, text, f, maxw)
    lh = size * 1.3
    tw = max(d.textlength(l, font=f) for l in lines); th = lh * len(lines)
    rx, ry = tw / 2 + size * 0.95, th / 2 + size * 0.75
    cx = min(max(cx, rx + 12), img.width - rx - 12); cy = max(cy, ry + 12)
    if tail:
        tx, ty = tail; ang = math.atan2(ty - cy, tx - cx)
        Lt = min(math.hypot(tx - cx, ty - cy), max(rx, ry) * 0.9 + 60)
        tx, ty = cx + Lt * math.cos(ang), cy + Lt * math.sin(ang)
        b1 = (cx + rx * .5 * math.cos(ang + .4), cy + ry * .5 * math.sin(ang + .4))
        b2 = (cx + rx * .5 * math.cos(ang - .4), cy + ry * .5 * math.sin(ang - .4))
        d.polygon([b1, (tx, ty), b2], fill="white", outline=(40, 40, 40))
    if shout:
        pts = [(cx + rx * (1.2 if k % 2 == 0 else 1.0) * math.cos(k / 30 * 2 * math.pi),
                cy + ry * (1.25 if k % 2 == 0 else 1.0) * math.sin(k / 30 * 2 * math.pi)) for k in range(30)]
        d.polygon(pts, fill="white", outline=(40, 40, 40), width=3)
    else:
        d.rounded_rectangle([cx - rx, cy - ry, cx + rx, cy + ry], radius=min(rx, ry), fill="white", outline=(40, 40, 40), width=3)
    if tail:
        d.polygon([b1, (cx, cy), b2], fill="white")
    y = cy - th / 2
    for l in lines:
        d.text((cx - d.textlength(l, font=f) / 2, y + (lh - size) / 2 - size * 0.08), l, font=f, fill=(30, 30, 30)); y += lh


def narr(img, text, x, y, font, size=26, maxw=560):
    d = ImageDraw.Draw(img); f = ImageFont.truetype(font, size)
    lines = wrap(d, text, f, maxw); lh = size * 1.4
    tw = max(d.textlength(l, font=f) for l in lines)
    d.rectangle([x, y, x + tw + 36, y + lh * len(lines) + 22], fill=(255, 250, 235), outline=(90, 70, 50), width=2)
    yy = y + 11
    for l in lines:
        d.text((x + 18, yy), l, font=f, fill=(60, 45, 35)); yy += lh


def sfx(img, text, cx, cy, size=96, angle=-12):
    f = ImageFont.truetype(SFXF if not text.isascii() else FONT["en"], size)
    tmp = Image.new("RGBA", (int(size * len(text) * 1.2), int(size * 1.8)), (0, 0, 0, 0))
    d = ImageDraw.Draw(tmp)
    d.text((20, 20), text, font=f, fill=(255, 196, 60), stroke_width=7, stroke_fill=(150, 40, 10))
    tmp = tmp.rotate(angle, expand=True)
    img.paste(tmp, (int(cx - tmp.width / 2), int(cy - tmp.height / 2)), tmp)


T = {
 "n1": ("다음 날 밤, 9시.", "The next night, 9 p.m."),
 "b1a": ("오늘은 전자레인지부터\n배운다.", "Today you learn\nthe microwave first."),
 "b1b": ("넵! 맡겨 주세요!", "Yes sir! Leave it to me!"),
 "b2": ("문 열고, 넣고, 30초.\n끝.", "Open, put it in, 30 seconds.\nDone."),
 "b3a": ("이 상자 안에...\n작은 태양이 살아요!", "There's a tiny sun\nliving in this box!"),
 "b3b": ("...그냥 전구야.", "...It's a light bulb."),
 "s4": ("삑삑삑삑!", "BEEP BEEP!"),
 "b4": ("잠깐, 그건―!", "Wait, not that―!"),
 "n5": ("빙글빙글... 빙글빙글...", "Round and round... round and round..."),
 "b6a": ("...미지근해요.", "...It's lukewarm."),
 "b6b": ("직화 아니면\n안 사요!", "No flame,\nno sale!"),
 "b7a": ("불은 딱 1초만.\n할 수 있어?", "Fire for exactly ONE second.\nCan you do it?"),
 "b7b": ("...1초요?", "...One second?"),
 "b8": ("0.8... 0.9... 1초!", "0.8... 0.9... one!"),
 "s8": ("후―", "Fff―"),
 "s9": ("치이익!", "SIZZLE!"),
 "b10a": ("이 불맛...!\n야근이 다 녹아요...", "This smoky flavor...!\nMy overtime just melted away..."),
 "b10b": ("1초 직화예요!", "One-second flame grill!"),
 "s11": ("쏴아아아!!", "SPLASH!!"),
 "b11": ("불 안 냈어요오!\n연기만 났어요!", "I didn't start a fire!\nJust a little smoke!"),
 "b12": ("...내일은\n소화기 수업이다.", "...Tomorrow's lesson:\nthe fire extinguisher."),
 "s12": ("에취!", "ACHOO!"),
}


def build(lang):
    L = 0 if lang == "ko" else 1; F = FONT[lang]; NF = NARF[lang]
    sz = 30 if lang == "ko" else 26
    P = {n: panel(n) for n in H}
    def h(n): return P[n].height
    narr(P[1], T["n1"][L], 24, 24, NF)
    bubble(P[1], T["b1a"][L], 560, 170, (640, 330), sz - 2, F, maxw=360)
    bubble(P[1], T["b1b"][L], 200, h(1) * .45, (320, h(1) * .62), sz - 2, F, maxw=300)
    bubble(P[2], T["b2"][L], 300, 110, (620, h(2) * .33), sz, F, maxw=380)
    bubble(P[3], T["b3a"][L], 220, 150, (420, h(3) * .50), sz, F, shout=True, maxw=300)
    bubble(P[3], T["b3b"][L], 640, 130, (660, h(3) * .32), sz - 4, F, maxw=240)
    bubble(P[4], T["b4"][L], 250, 130, (600, h(4) * .30), sz, F, maxw=300)
    sfx(P[4], T["s4"][L], 360, h(4) * .80, 72 if lang == "ko" else 64, angle=-8)
    narr(P[5], T["n5"][L], 24, h(5) - 100, NF)
    bubble(P[6], T["b6b"][L], 190, h(6) * .50, (230, h(6) * .64), sz - 2, F, shout=True, maxw=240)
    bubble(P[6], T["b6a"][L], 640, h(6) * .45, (520, h(6) * .64), sz, F, maxw=280)
    bubble(P[7], T["b7a"][L], 260, 120, (560, h(7) * .38), sz - 2, F, maxw=420)
    bubble(P[7], T["b7b"][L], 140, h(7) * .48, (240, h(7) * .62), sz - 4, F, maxw=200)
    bubble(P[8], T["b8"][L], 250, 130, (560, h(8) * .36), sz, F, maxw=340)
    sfx(P[8], T["s8"][L], 170, h(8) * .62, 56, angle=0)
    sfx(P[9], T["s9"][L], 400, 110, 90 if lang == "ko" else 76, angle=-6)
    bubble(P[10], T["b10a"][L], 240, 140, (230, h(10) * .45), sz - 2, F, maxw=360)
    bubble(P[10], T["b10b"][L], 600, 140, (560, h(10) * .45), sz - 2, F, shout=True, maxw=260)
    sfx(P[11], T["s11"][L], 400, h(11) * .30, 84 if lang == "ko" else 76, angle=-8)
    bubble(P[11], T["b11"][L], 610, h(11) * .48, (500, h(11) * .62), sz - 2, F, shout=True, maxw=300)
    bubble(P[12], T["b12"][L], 600, 170, (330, h(12) * .45), sz, F, maxw=330)
    sfx(P[12], T["s12"][L], 690, h(12) * .60, 56, angle=10)
    # 제목 카드 + 엔드 카드
    title = Image.new("RGB", (W, 360), BG); d = ImageDraw.Draw(title)
    tf = ImageFont.truetype(SFXF if lang == "ko" else FONT["en"], 54 if lang == "ko" else 46)
    t1 = "편의점 알바는 아기 드래곤" if lang == "ko" else "My Part-Timer Is a Baby Dragon"
    t2 = "2화 - 전자레인지 수업" if lang == "ko" else "Episode 2 · Microwave Lesson"
    d.text(((W - d.textlength(t1, font=tf)) / 2, 120), t1, font=tf, fill=(46, 110, 70))
    sf = ImageFont.truetype(F, 34); d.text(((W - d.textlength(t2, font=sf)) / 2, 210), t2, font=sf, fill=(120, 90, 60))
    end = Image.new("RGB", (W, 300), BG); d = ImageDraw.Draw(end)
    e1 = "다음 화: 꼬리 손님" if lang == "ko" else "Next: The Tail Customer"
    e2 = "1초 직화 도시락, 내일도 팔 수 있을까?" if lang == "ko" else "Can the one-second flame grill survive another night?"
    e2 = e2.replace(" 🐉", "")
    d.text(((W - d.textlength(e1, font=sf)) / 2, 100), e1, font=sf, fill=(46, 110, 70))
    ef = ImageFont.truetype(F, 28); d.text(((W - d.textlength(e2, font=ef)) / 2, 160), e2, font=ef, fill=(120, 90, 60))
    e3 = "구독하면 루루가 내일도 출근해요!" if lang == "ko" else "Subscribe and Ruru shows up for her next shift!"
    d.text(((W - d.textlength(e3, font=ef)) / 2, 220), e3, font=ef, fill=(150, 120, 90))
    parts = [title] + [P[n] for n in sorted(P)] + [end]
    GAP = 70
    total = sum(p.height for p in parts) + GAP * (len(parts) - 1)
    out = Image.new("RGB", (W, total), BG); y = 0
    for p in parts:
        out.paste(p, (0, y)); y += p.height + GAP
    od = f"/home/claude/minsung-ai/_stage/ruru/ep2_{lang}"; os.makedirs(od, exist_ok=True)
    out.save(f"{od}/full.jpg", quality=88)
    # 1280px 조각 (CANVAS 업로드용)
    k = 0
    for yy in range(0, out.height, 1280):
        k += 1; out.crop((0, yy, W, min(out.height, yy + 1280))).save(f"{od}/ep2_{k:02d}.jpg", quality=90)
    print(lang, out.size, k)


for lg in sys.argv[1:] or ["ko", "en"]:
    build(lg)
