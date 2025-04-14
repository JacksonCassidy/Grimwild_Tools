import random as r

def explore(option):
    f = open("txt/explore.txt", "r")
    content = f.read().splitlines()

    offset = option - 1

    x = r.randint(0,5)
    y = r.randint(0,5)

    if x == y:
        first = content[72*offset + x*6*2 + y] + "\n"
    else:
        first = content[72*offset +  x*6*2 + y] + " or " + content[72*offset + y*6*2 + x] + "\n"

    x = r.randint(0,5)
    y = r.randint(0,5)

    if x == y:
        second = content[72*offset + 6 + x*6*2 + y] + "\n"
    else:
        second = content[72*offset + 6 +  x*6*2 + y] + " or " + content[72*offset + 6 + y*6*2 + x] + "\n"

    return "    " + first + "    " + second