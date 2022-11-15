files = open('yamlf.txt', encoding="utf8")
red = files.readlines()
for i in range(len(red)):
    symb = red[i]; red[i] = symb[:-1]
files.close()
total = []
exm = open('csv.txt', 'w')
c = 0; k = 0; t = ""
for i in red:
    strr = i
    if strr[0] == "-" and strr[1] == " ":
        strr = strr[2:]
        resp = strr.split(": ")
        t += resp[0] + " "
    if strr[0] == " " and strr[1] == " " and strr[2] == "-":
        t += "weeks/" + str(c) + " "
        c += 1
    else:
        if strr[0] == " " and strr[1] == " " and "weeks" not in strr:
            strr = strr[2:]
            resp = strr.split(": ")
            t += resp[0] + " "
exm.write(t + '\n')
t = ""
for i in red:
    strr = i
    if strr[0] == "-" and strr[1] == " ":
        exm.write(t[:-1] + '\n')
        t = ""
        resp = strr.split(": ")
        t += resp[1] + ","
    else:
        if strr[0] == " " and strr[1] == " " and strr[2] == "-":
            resp = strr.split("- ")
            t += resp[1] + ","
        else:
            if strr[0] == " " and strr[1] == " " and "weeks" not in strr:
                resp = strr.split(": ")
                t += resp[1] + ","
exm.write(t[:-1])