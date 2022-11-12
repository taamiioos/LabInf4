import re
from time import time
sec = time()
pattern1 = r'^([a-zA-z]+)(: )(.+)'; pattern2 = r'^([a-zA-z]+)(:)( )$'; pattern3 = r'(- )([a-zA-z]+)(:)(.+)'; pattern4 = r'(  )([a-zA-z]+)(:)( )$'; pattern5 = r'^(  - )[0-9]+'; pattern6 = r'(  )([a-zA-z]+)(: )(.+)'
i = 0
files = open('yamlf.txt', encoding="utf8")
red = files.readlines()
for i in range(len(red)):
    symb = red[i]
    red[i] = symb[:-1]
files.close()
total = []
for i in red:
    strr = i
    ree = re.search(pattern3, strr)
    if ree:
        total.append("</lessons>")
        total.append("<lessons>")
        strr = strr[2:]
        resp = re.split(r': ', strr)
        total.append("  <" + resp[0] + ">" + resp[1] + "</" + resp[0] + ">")
    else:
        ree = re.search(pattern5, strr)
        if ree:
            resp = re.split(r'- ', strr)
            total.append("  <weeks>" + resp[1] + "</weeks>")
        else:
            ree = re.search(pattern6, strr)
            if ree:
                strr = strr[2:]
                resp = re.split(r': ', strr)
                total.append("  <" + resp[0] + ">" + resp[1] + "</" + resp[0] + ">")
            else:
                ree = re.search(pattern2, strr)
                if ree:
                    resp = re.split(r': ', strr)
                    total.append("<" + resp[0] + ">")
                else:
                    ree = re.search(pattern1, strr)
                    if ree:
                        resp = re.split(r': ', strr)
                        total.append("<" + resp[0] + ">" + resp[1] + "</" + resp[0] + ">")
total.append("</lessons>")
exm = open('total.txt', 'w')
for i in range(len(total)):
    if i != 1 and i != 2:
        exm.write(total[i] + '\n')
print(f'Time:{time() - sec}')