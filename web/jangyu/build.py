import re,os
head=open('_head.txt').read()
names={'dibmil':'딥밀','erben':'에르벤','daedongheon':'대동헌','loveangel':'러브엔젤플라워','jjomani':'쪼마니헤어','bbhair':'비비헤어스토리','hansuwi':'한수위 영어수학전문학원','ilta':'일타수학원','sumyeo':'수며들다 수학과학전문학원','sein':'세인영어수학'}
for s,n in names.items():
    b=open(f'src/{s}.html').read()
    os.makedirs(s,exist_ok=True)
    ban=f'<div class="chk">찰칵홈이 {n} 사장님께 드리는 홈페이지 시안입니다 · 마음에 드시면 <a href="mailto:kisthestar1@gmail.com">kisthestar1@gmail.com</a></div>'
    open(f'{s}/index.html','w').write('<!doctype html><html lang="ko"><head>'+head+'</head><body>'+b+ban+'<div style="height:40px"></div></body></html>')
print('ok')
