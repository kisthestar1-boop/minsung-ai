import sys; sys.path.insert(0,'.')
from render import *
V='/home/claude/minsung-ai/web/dstage/voice/'; F='/home/claude/minsung-ai/web/flyer/img/'
CAP=[(0.3,3.6,['오늘처럼 쌀쌀한 날은','이거 하나면 돼요'],{1:(255,214,80)}),
(3.8,6.9,['새벽부터 12시간','우린 국물'],{1:(255,214,80)}),
(7.0,9.9,['한 입 뜨면','속이 싹 풀려요'],None),
(10.0,13.0,['고기도 아낌없이','듬뿍'],{1:(255,214,80)}),
(13.1,16.0,['깍두기는','매일 아침 새로'],None)]
def ov(d,t,idx,s):
    f=font(FS,40); tag='장유 · 국밥 맛집'
    tw=d.textlength(tag,font=f); d.rounded_rectangle(((W-tw)/2-26,150,(W+tw)/2+26,222),36,fill=(255,255,255,235)); d.text(((W-tw)/2,158),tag,font=f,fill=(70,40,20))
    for a,b,lines,hl in CAP:
        if a<=t<b: text_karaoke(d,lines,1120,96,min(1,(t-a)/max(0.5,(b-a)*0.85)))
    if t>=16.1:
        card(d,(110,930,970,1460),(40,22,12,235))
        f1=font(FB,86); f2=font(FS,50); f3=font(FS,38)
        for txt,ff,y,c in [('장유에서 국밥 생각나면',f2,980,(240,228,215)),('여기 한 번 와 보세요',f1,1060,(255,200,90)),('뚝배기 한 그릇 (예시)',f2,1210,(255,255,255)),('새벽 6시 ~ 밤 9시 · 주차 가능',f3,1290,(220,205,190)),('찰칵영상 시안',f3,1370,(170,150,135))]:
            tw=d.textlength(txt,font=ff); d.text(((W-tw)/2,y),txt,font=ff,fill=c)
spec=dict(dur=19.8,audio=V+'food_v1.wav',overlay=ov,scenes=[
 dict(t0=0,img=V+'food_spoon.jpg',cropb=.08,m='in'),
 dict(t0=3.8,img=V+'food_pot.jpg',cropb=.08,m='up'),
 dict(t0=7.0,img=F+'food.jpg',m='in'),
 dict(t0=10.0,img=V+'food_spoon.jpg',cropb=.08,m='out'),
 dict(t0=13.1,img=V+'food_kkak.jpg',cropb=.08,m='left'),
 dict(t0=16.1,img=F+'food.jpg',m='out')])
render(spec,'/home/claude/chalkak-video/v2/food_v3.mp4')
