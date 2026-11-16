import sys,glob
from PIL import Image
fs=sorted(glob.glob(sys.argv[1]+'/f*.jpg'));W,H=216,384;n=len(fs)
s=Image.new('RGB',(W*n+10*(n+1),H+20),'#444')
for i,f in enumerate(fs): s.paste(Image.open(f).resize((W,H)),(10+i*(W+10),10))
s.save(sys.argv[2])
