import random as r

def gm_cruc():
    f = open("txt/gm_cruc.txt", "r")
    content = f.read().splitlines()

    x = r.randint(0,5)
    y = r.randint(0,5)

    if x == y:
        first = content[x*6 + y] + "\n"
    else:
        first = content[x*6 + y] + " or " + content[y*6 + x] + "\n"

    x = r.randint(0,5)
    y = r.randint(0,5)

    if x == y:
        second = content[36 + x*6 + y] + "\n"
    else:
        second = content[36 + x*6 + y] + " or " + content[36+ y*6 + x] + "\n"

    return first + second