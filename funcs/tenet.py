import random as r

def rand_tenet():
    f = open("txt/tenet.txt", "r")
    content = f.read().splitlines()

    x = r.randint(0,5)
    y = r.randint(0,5)
    z = r.randint(0,5)

    a = content[x]
    b = content[y + 6]
    c = content[z + 12]

    return "*I swear to bring*\n    " + a + "\n" + "*To - For the*\n    " + b + "\n" + "*Despite - Because of*\n    " + c + "\n"