import sys; sys.path.insert(0,'.')
from render import *
V='/home/claude/minsung-ai/web/dstage/voice/'; R='/home/claude/minsung-ai/web/realty/img/'
CAP=[(0.3,4.3,['율하에서 제일 많이','물어보시는 집이에요'],{1:(255,214,80)}),
(4.6,6.1,['거실 창 좀 보세요'],None),
(6.2,8.6,['하루 종일 햇살이','이렇게 들어와요'],{1:(255,214,80)}),
(8.7,11.5,['주방은 작년에','새로 고쳤어요'],None),
(11.6,14.3,['초등학교까지','걸어서 5분'],{1:(150,230,170)})]
def ov(d,t,idx,s):
    # top badge
    f=font(FS,40); tag='장유 율하 · 34평 아파트'
    tw=d.textlength(tag,font=f); d.rounded_rectangle(((W-tw)/2-26,150,(W+tw)/2+26,222),36,fill=(255,255,255,235)); d.text(((W-tw)/2,158),tag,font=f,fill=(30,40,60))
    for a,b,lines,hl in CAP:
        if a<=t<b: text_karaoke(d,lines,1120,92,min(1,(t-a)/max(0.5,(b-a)*0.85)))
    if 14.5<=t<17.6:
        card(d,(130,980,950,1420),(255,255,255,240))
        f1=font(FS,46); f2=font(FB,120); f3=font(FS,40)
        for txt,ff,y,c in [('34평 · 방 3 · 욕실 2',f1,1020,(90,100,120)),('매매 4억 2천',f2,1095,(20,30,50)),('남향 · 공원 앞 · 초등학교 5분',f3,1270,(90,100,120))]:
            tw=d.textlength(txt,font=ff); d.text(((W-tw)/2,y),txt,font=ff,fill=c)
    if t>=17.6:
        card(d,(110,930,970,1460),(18,32,58,235))
        f1=font(FB,84); f2=font(FS,50); f3=font(FS,38)
        for txt,ff,y,c in [('보러 오실 분은',f2,980,(220,228,240)),('편하게 전화 주세요',f1,1060,(255,214,80)),('장유 바른공인중개사',f2,1210,(255,255,255)),('055-000-0000 (예시)',f3,1290,(200,210,225)),('찰칵부동산 시안',f3,1370,(150,165,190))]:
            tw=d.textlength(txt,font=ff); d.text(((W-tw)/2,y),txt,font=ff,fill=c)
spec=dict(dur=20.3,audio=V+'realty_v1.wav',overlay=ov,scenes=[
 dict(t0=0,img=V+'living_v.jpg',cropb=.08,m='in'),
 dict(t0=4.4,img=R+'living.jpg',m='left'),
 dict(t0=6.2,img=V+'living_v.jpg',cropb=.08,m='out'),
 dict(t0=8.7,img=V+'kitchen_v.jpg',cropb=.08,m='right'),
 dict(t0=11.6,img=V+'school.jpg',cropb=.08,m='in'),
 dict(t0=14.5,img=R+'apt.jpg',mode='blurbg',m='in'),
 dict(t0=17.6,img=V+'living_v.jpg',cropb=.08,m='out')])
render(spec,'/home/claude/chalkak-video/v2/realty_v3.mp4')
