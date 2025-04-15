import random as r

def rand_spell():
    f = open("txt/spells.txt", "r")
    content = f.read().splitlines()

    x = r.randint(0,5)
    y = r.randint(0,5)

    if x == y:
        style = content[x*6*3 + y] + "\n"
    else:
        style = content[x*6*3 + y] + " or " + content[y*6*3 + x] + "\n"

    x = r.randint(0,5)
    y = r.randint(0,5)

    if x == y:
        form = content[12 + x*6*3 + y] + "\n"
    else:
        form = content[12 + x*6*3 + y] + " or " + content[ 12 + y*6*3 + x] + "\n"

    x = r.randint(0,5)
    y = r.randint(0,5)

    if x == y:
        essence = content[6 + x*6*3 + y] + "\n"
    else:
        essence = content[6 + x*6*3 + y] + " or " + content[6 + y*6*3 + x] + "\n"

    return "*Style:*\n    " + style + "*Form:*\n    " + form + "*Essence:*\n    " + essence