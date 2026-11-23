import sys
from PIL import Image
a,b,out=sys.argv[1:4]
A=Image.open(a).convert('RGB');B=Image.open(b).convert('RGB')
C=Image.new('RGB',(A.width,A.height+B.height));C.paste(A,(0,0));C.paste(B,(0,A.height))
P=C.crop((770,1100,860,1190));C.paste(P,(860,1100))
C.save(out,quality=88);print(out,C.size)
