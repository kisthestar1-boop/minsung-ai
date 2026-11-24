import sys, json, math, subprocess, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H,FPS=1080,1920,30
FB='/home/claude/minsung-ai/toon_tools/fonts/BlackHanSans-Regular.ttf'
FS='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def font(p,s): return ImageFont.truetype(p,s)
def cover(im,w,h):
    r=max(w/im.width,h/im.height); im=im.resize((int(im.width*r)+1,int(im.height*r)+1),Image.LANCZOS)
    l=(im.width-w)//2; t=(im.height-h)//2; return im.crop((l,t,l+w,t+h))
def prep(path,crop_bottom=0.0,mode='cover'):
    im=Image.open(path).convert('RGB')
    if crop_bottom: im=im.crop((0,0,im.width,int(im.height*(1-crop_bottom))))
    if mode=='blurbg' and im.width>im.height:
        bg=cover(im,int(W*1.15),int(H*1.15)).filter(ImageFilter.GaussianBlur(40))
        fg=im.resize((int(W*1.15),int(im.height*W*1.15/im.width)),Image.LANCZOS)
        bg.paste(fg,(0,(bg.height-fg.height)//2-80)); return bg
    return cover(im,int(W*1.15),int(H*1.15))
def kb(base,t,motion):
    # base is 1.15x; motion: in/out/left/right/up ; t 0..1, slow
    bw,bh=base.size; z0,z1=(1.0,1.08) if motion!='out' else (1.08,1.0)
    z=z0+(z1-z0)*t; w=int(W*1.15/z); h=int(H*1.15/z)
    cx,cy=bw/2,bh/2
    if motion=='left': cx=bw/2+ (bw-w)/2*(0.6-1.2*t)
    if motion=='right': cx=bw/2- (bw-w)/2*(0.6-1.2*t)
    if motion=='up': cy=bh/2+ (bh-h)/2*(0.6-1.2*t)
    l=int(max(0,min(bw-w,cx-w/2))); tt=int(max(0,min(bh-h,cy-h/2)))
    return base.crop((l,tt,l+w,tt+h)).resize((W,H),Image.BILINEAR)
def text_block(d,lines,y,size,fill=(255,255,255),stroke=(20,20,20),sw=10,fnt=FB,hl=None):
    f=font(fnt,size)
    for i,ln in enumerate(lines):
        tw=d.textlength(ln,font=f); x=(W-tw)/2; yy=y+i*int(size*1.25)
        if hl and i in hl:
            pad=18; d.rounded_rectangle((x-pad,yy-8,x+tw+pad,yy+size+18),18,fill=hl[i])
            d.text((x,yy),ln,font=f,fill=(25,25,25))
        else:
            d.text((x,yy),ln,font=f,fill=fill,stroke_width=sw,stroke_fill=stroke)
def card(d,box,fill,r=36): d.rounded_rectangle(box,r,fill=fill)
def render(spec,out):
    scenes=spec['scenes']; dur=spec['dur']; N=int(dur*FPS)
    bases=[prep(s['img'],s.get('cropb',0),s.get('mode','cover')) for s in scenes]
    tmp=out+'_frames'; os.makedirs(tmp,exist_ok=True)
    XF=0.35
    for n in range(N):
        t=n/FPS
        idx=max(i for i,s in enumerate(scenes) if s['t0']<=t+1e-6)
        s=scenes[idx]; t1=scenes[idx+1]['t0'] if idx+1<len(scenes) else dur
        p=(t-s['t0'])/max(0.01,t1-s['t0'])
        fr=kb(bases[idx],min(1,p),s.get('m','in'))
        if idx+1<len(scenes) and t>t1-XF:
            s2=scenes[idx+1]; a=(t-(t1-XF))/XF
            fr=Image.blend(fr,kb(bases[idx+1],0,s2.get('m','in')),a)
        # dark gradient for text
        ov=Image.new('RGBA',(W,H),(0,0,0,0)); od=ImageDraw.Draw(ov)
        for yy in range(0,520): od.line((0,yy,W,yy),fill=(0,0,0,int(120*(1-yy/520))))
        for yy in range(H-760,H): od.line((0,yy,W,yy),fill=(0,0,0,int(150*((yy-(H-760))/760))))
        fr=Image.alpha_composite(fr.convert('RGBA'),ov)
        d=ImageDraw.Draw(fr)
        spec['overlay'](d,t,idx,s)
        fr.convert('RGB').save(f'{tmp}/{n:05d}.jpg',quality=88)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i',f'{tmp}/%05d.jpg','-i',spec['audio'],'-filter_complex',f"[1:a]apad,atrim=0:{dur},volume=1.0[a]",'-map','0:v','-map','[a]','-c:v','libx264','-preset','veryfast','-crf','21','-pix_fmt','yuv420p','-c:a','aac','-b:a','160k','-shortest',out],check=True)
    subprocess.run(['rm','-rf',tmp])

def text_karaoke(d,lines,y,size,prog,hi=(255,214,80),base=(255,255,255),dim=(235,235,235),sw=10,fnt=FB):
    f=font(fnt,size); total=sum(len(l) for l in lines); upto=int(total*prog+0.999); c=0
    for i,ln in enumerate(lines):
        tw=d.textlength(ln,font=f); x=(W-tw)/2; yy=y+i*int(size*1.28)
        # soft pill for readability
        d.rounded_rectangle((x-30,yy-14,x+tw+30,yy+size+22),28,fill=(0,0,0,110))
        for ch in ln:
            col=hi if c<upto else dim
            d.text((x,yy),ch,font=f,fill=col,stroke_width=sw,stroke_fill=(15,15,15))
            x+=d.textlength(ch,font=f); c+=1
