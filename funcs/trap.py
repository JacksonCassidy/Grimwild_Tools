import random as r

def trap_names():
    f = open("txt/trap.txt", "r")
    content = f.read().splitlines()

    x = r.randint(0,5)
    y = r.randint(0,5)
    x2 = r.randint(0,5)
    y2 = r.randint(0,5)
    x3 = r.randint(0,5)
    y3 = r.randint(0,5)

    result = content[x] + " " + content[6 + y] + " trap" + "\n"
    result2 = content[x2] + " " + content[6 + y2] + " trap" + "\n"
    result3 = content[x3] + " " + content[6 + y3] +  " trap" + "\n"

    return "*Traps:*\n    " + result + "    " + result2 + "    " + result3