import re, os

f = "ex2.tex"
f_copy = re.subn("\.","_copy.",f,1)[0]

o = open(f_copy,"wb")
inp = open(f,"rb")

text1 = inp.read()
text = str(text1,'utf-8')

regexp1 = r"([^\$]|^)\$([^\$]*?)\\limits([^\$]*?)\$([^\$]|$)"    #+
subs1 = r"\g<1>$\g<2>\g<3>$\g<4>"

regexp2 = r"(\s|^)''([\s|\S]+?)''"    #+
subs2 = "\g<1><<\g<2>>>"

regexp3 = "\.{3}"   #+
subs3 = "\\\\ldots "

regexp4 = r"(?P<fn>[А-Я][а-я]+)\-(?P<sn>[А-Я][а-я]+)"   #+
subs4 = "\g<fn>--\g<sn>"

regexp5 = r"([^\w\\]|^|\d|_)(max|min|sup|lim|inf|sin|\
                cos|tan|sec|csc|cot|arg|sinh|cosh|tanh|coth|\
                exp|ker|dim|arcsin|arccos|arctan|log|ln|lg|\
                deg|det|tg|ctg|cth|sh|ch|th|cosec|arctg)([^\w]|$|\d|_)"
subs5 = r"\g<1>\\\g<2>\g<3>"

regexp6 = r"\$([\s|\S]+?)<([^\$]+?),([^\$]+?)>([\s|\S]+?)\$"   #+
subs6 = r"$\g<1>\\left<\g<2>,\g<3>\\right>\g<4>$"

regexp7 = r"\$\$([s|\S]*?)\(([s|\S]*?)\\frac([s|\S]*?)\)([s|\S]*?)\$\$"
subs7 = r"$$\g<1>\\left(\g<2>\\frac\g<3>\\right)\g<4>$$"    #+

##text = re.sub(regexp1,subs1,text)
##text = re.sub(regexp3,subs3,text)
##text = re.sub(regexp4,subs4,text)
##text = re.sub(regexp5,subs5,text)
##text = re.sub(regexp6,subs6,text)
##text = re.sub(regexp7,subs7,text)
text = re.sub(regexp2,subs2,text)

o.write(bytes(text,'utf-8'))
o.close()
inp.close()

path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f)
os.remove(path)
os.rename(f_copy,f)
