import os, re

f = "ex4.tex"
f_copy = re.subn("\.","_copy.",f,1)[0]

o = open(f_copy,"wb")
inp = open(f,"rb")

text1 = inp.read()
text = str(text1,'WINDOWS-1251')

o.write(bytes(text,'utf-8'))
o.close()
inp.close()

path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f)
os.remove(path)
os.rename(f_copy,f)
