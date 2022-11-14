#доп.задание №3
from time import time
sec = time()
#доп.задание №3

i = 0
total = []
files = open('yamlf.txt', encoding="utf8")
red = files.readlines()
for i in range(len(red)):
    symb = red[i]
    red[i] = symb[:-1] #убираем \n
files.close()
for i in range(len(red)):
    if red[i] != "---" and red[i] != "lessons:":
        if red[i][0] + red[i][1] != "  " and red[i][0] + red[i][1] != "- ":
            strr = red[i].split(": ")
            exm = "<" + strr[0] + ">" + strr[1] + "</" + strr[1] + ">"
            total.append(exm)
        elif red[i][0] == "-":
            total.append("</lessons>")
            total.append("<lessons>")
            n = red[i][2:] #убираем '- '
            strr = n.split(": ")
            exm = "  <" + strr[0] + ">" + strr[1] + "</" + strr[0] + ">"
            total.append(exm)
        elif red[i][2] == "-":
                n = red[i]
                strr = n.split("- ")[1]
                exm = "  <" + "weeks" + ">" + strr + "</" + "weeks" + ">"
                total.append(exm)
        elif red[i][0] + red[i][1] == "  ":
                n = red[i][2:]
                strr = n.split(": ")
                exm = "  <" + strr[0] + ">" + strr[1] + "</" + strr[0] + ">"
                total.append(exm)
exm = open('xmlf.txt', 'w')
total.append("</lessons>")
for i in range(len(total)):
    if i != 1:
        exm.write(total[i] + '\n')


#доп.задание №3
print(f'Time:{time() - sec}')