"""루루 1화 조립: 캡처 반쪽 2장씩 → 패널 → 말풍선(한/영) → 800px 세로 웹툰"""
from PIL import Image, ImageDraw, ImageFont
import math, os, sys

S = "/tmp/claude-chrome-screenshots-B89JL6/screenshot-"
H = {  # 패널: (위 반쪽, 아래 반쪽, 상단 머리띠 제거 여부)
 1: ("1795422228253-2", "1795422228254-3", 0), 2: ("1795422228255-4", "1795422228256-5", 0),
 3: ("1795422248228-6", "1795422248229-7", 1), 4: ("1795422248230-8", "1795422248231-9", 1),
 5: ("1795422248231-10", "1795422248232-11", 1), 6: ("1795422274780-14", "1795422274783-15", 1),
 7: ("1795422274794-16", "1795422274796-17", 1), 8: ("1795422274797-18", "1795422274798-19", 1),
 9: ("1795422296344-20", "1795422296345-21", 1), 10: ("1795422296346-22", "1795422296347-23", 1),
 11: ("1795422296348-24", "1795422296349-25", 1), 12: ("1795422296350-26", "1795422296351-27", 0)}
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
    top = int(A.height * 0.115) if hdr else 0          # 제미나이가 넣은 머리띠 글자 제거
    bot = int(B.height * 0.24)                          # 오른쪽 아래 반짝이 표시 제거
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


T = {  # (ko, en)
 "n1": ("장유동 골목 끝, 24시 편의점.", "At the end of a quiet street, a 24-hour convenience store."),
 "b2": ("야간 알바 구한 지 석 달째...\n오늘 온다던 신입은...", "Three months looking for a night-shift worker...\nand the new hire is late..."),
 "b3a": ("안녕하세요! 공고 보고 왔어요!", "Hi!! I'm here for the job!"),
 "b3b": ("'종족 무관'이라고 써 있어서요!", "It said \"all species welcome\"!"),
 "b4": ("...그거 장난으로 쓴 건데.", "...I wrote that as a joke."),
 "b5": ("꼬, 꼬리 없어요!\n완전 인간이에요!", "N-no tail here!\nI'm 100% human!"),
 "b6a": ("(한숨) ...야간 할 사람이 없으니까.\n지금부터 일해.", "(sigh) ...Nobody else wants nights.\nYou start now."),
 "b6b": ("앗, 바로요?!", "R-right now?!"),
 "b7": ("손님이 도시락 사면 데워 드려.\n30초.", "When someone buys a lunchbox, heat it up.\n30 seconds."),
 "b8": ("데우는 건 제 전문이에요!", "Heating things up is my specialty!"),
 "s9": ("화르르륵!!", "FWOOSH!!"),
 "b10": ("...전자레인지가 뭔지\n몰랐어요.", "...I didn't know what a\n\"microwave\" was."),
 "b11": ("어머, 직화 도시락이네?\n이거 줘요~", "Oh my, flame-grilled!\nI'll take that one~"),
 "b12": ("...전자레인지는\n내일 가르쳐 줄게.", "...I'll teach you the\nmicrowave tomorrow."),
 "n12": ("그렇게, 아기 드래곤의 첫 출근이 끝났다.", "And so ended the baby dragon's first shift."),
}


def build(lang):
    L = 0 if lang == "ko" else 1; F = FONT[lang]; NF = NARF[lang]
    sz = 30 if lang == "ko" else 26
    P = {n: panel(n) for n in H}
    def h(n): return P[n].height
    narr(P[1], T["n1"][L], 24, 24, NF)
    bubble(P[2], T["b2"][L], 250, 120, (330, h(2) * .52), sz, F, maxw=360)
    bubble(P[3], T["b3a"][L], 230, 100, (360, h(3) * .40), sz, F)
    bubble(P[3], T["b3b"][L], 200, h(3) * .55, (330, h(3) * .44), sz - 2, F, maxw=300)
    bubble(P[4], T["b4"][L], 560, 90, (470, h(4) * .55), sz, F, maxw=300)
    bubble(P[5], T["b5"][L], 230, 90, (360, h(5) * .48), sz + 2, F, shout=True, maxw=300)
    bubble(P[6], T["b6a"][L], 520, 95, (270, h(6) * .37), sz - 2, F, maxw=400)
    bubble(P[6], T["b6b"][L], 230, h(6) * .62, (560, h(6) * .45), sz, F, maxw=260)
    bubble(P[7], T["b7"][L], 400, 90, (270, h(7) * .36), sz - 2, F, maxw=440)
    bubble(P[8], T["b8"][L], 400, 80, (400, h(8) * .30), sz, F, shout=True, maxw=380)
    sfx(P[9], T["s9"][L], 330, h(9) * .50, 84 if lang == "ko" else 80)
    bubble(P[10], T["b10"][L], 480, 90, (630, h(10) * .52), sz, F, maxw=330)
    bubble(P[11], T["b11"][L], 520, 90, (560, h(11) * .40), sz, F, maxw=330)
    bubble(P[12], T["b12"][L], 260, 95, (650, h(12) * .33), sz, F, maxw=330)
    narr(P[12], T["n12"][L], 24, h(12) - 110, NF)
    # 제목 카드 + 엔드 카드
    title = Image.new("RGB", (W, 360), BG); d = ImageDraw.Draw(title)
    tf = ImageFont.truetype(SFXF if lang == "ko" else FONT["en"], 54 if lang == "ko" else 46)
    t1 = "편의점 알바는 아기 드래곤" if lang == "ko" else "My Part-Timer Is a Baby Dragon"
    t2 = "1화 - 첫 출근" if lang == "ko" else "Episode 1 · First Shift"
    d.text(((W - d.textlength(t1, font=tf)) / 2, 120), t1, font=tf, fill=(46, 110, 70))
    sf = ImageFont.truetype(F, 34); d.text(((W - d.textlength(t2, font=sf)) / 2, 210), t2, font=sf, fill=(120, 90, 60))
    end = Image.new("RGB", (W, 300), BG); d = ImageDraw.Draw(end)
    e1 = "다음 화: 전자레인지 수업" if lang == "ko" else "Next: Microwave Lesson"
    e2 = "구독하면 루루가 내일도 출근해요! 🐉" if lang == "ko" else "Subscribe and Ruru shows up for her next shift!"
    e2 = e2.replace(" 🐉", "")
    d.text(((W - d.textlength(e1, font=sf)) / 2, 100), e1, font=sf, fill=(46, 110, 70))
    ef = ImageFont.truetype(F, 28); d.text(((W - d.textlength(e2, font=ef)) / 2, 170), e2, font=ef, fill=(120, 90, 60))
    parts = [title] + [P[n] for n in sorted(P)] + [end]
    GAP = 70
    total = sum(p.height for p in parts) + GAP * (len(parts) - 1)
    out = Image.new("RGB", (W, total), BG); y = 0
    for p in parts:
        out.paste(p, (0, y)); y += p.height + GAP
    od = f"/home/claude/minsung-ai/_stage/ruru/ep1_{lang}"; os.makedirs(od, exist_ok=True)
    out.save(f"{od}/full.jpg", quality=88)
    # 1280px 조각 (CANVAS 업로드용)
    k = 0
    for yy in range(0, out.height, 1280):
        k += 1; out.crop((0, yy, W, min(out.height, yy + 1280))).save(f"{od}/ep1_{k:02d}.jpg", quality=90)
    print(lang, out.size, k)


for lg in sys.argv[1:] or ["ko", "en"]:
    build(lg)
