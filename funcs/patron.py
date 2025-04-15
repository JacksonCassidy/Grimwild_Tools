import random as r

def rand_patron():
    f = open("txt/patron.txt", "r")
    content = f.read().splitlines()

    x = r.randint(0,5)
    y = r.randint(0,5)

    x2 = r.randint(0,5)
    y2 = r.randint(0,5)

    x3 = r.randint(0,5)
    y3 = r.randint(0,5)

    x4 = r.randint(0,5)
    y4 = r.randint(0,5)

    if x==y:
        nat = content[x*6 + y]
    else:
        nat = content[x*6 + y] + " - " + content[y*6 + x]
    
    if x2==y2:
        nat2 = content[x2*6 + y2]
    else:
        nat2 = content[x2*6 + y2] + " - " + content[y2*6 + x2]

    if x==x2 and y==y2:
        nature = nat
    else:
        nature = nat + " - " + nat2


    if x3==y3:
        des = content[36 + x3*6 + y3]
    else:
        des = content[36 + x3*6 + y3] + " - " + content[36 + y3*6 + x3]

    if x4==y4:
        des2 = content[36 + x4*6 + y4]
    else:
        des2 = content[36 + x4*6 + y4] + " - " + content[36 + y4*6 + x4]

    if x3==x4 and y3==y4:
        desire = des
    else:
        desire = des + " - " + des2

    
    return "*Nature:*\n    " + nature + "\n" + "*Desires:*\n    " + desire + "\n"