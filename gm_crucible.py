import random as r

def gm_cruc():
    f = open("gm_cruc.txt", "r")
    content = f.read().splitlines()

    x = r.randint(0,5)
    y = r.randint(0,5)
    #print("Rolled %d and %d" % (x+1, y+1))

    if x == y:
        #print(content[x*6 + y] + "\n")
        first = content[x*6 + y] + "\n"
    else:
        #print(content[x*6 + y] + " or " + content[y*6 + x] + "\n")
        first = content[x*6 + y] + " or " + content[y*6 + x] + "\n"


    x = r.randint(0,5)
    y = r.randint(0,5)
    #print("Rolled %d and %d" % (x+1, y+1))
    if x == y:
        #print(content[36 + x*6 + y] + "\n")
        second = content[36 + x*6 + y] + "\n"
    else:
        #print(content[36 + x*6 + y] + " or " + content[36+ y*6 + x] + "\n")
        second = content[36 + x*6 + y] + " or " + content[36+ y*6 + x] + "\n"

    return first + second