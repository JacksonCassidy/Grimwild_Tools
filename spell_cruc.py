import random as r

def rand_spell():
    f = open("spells.txt", "r")
    content = f.read().splitlines()

    x = r.randint(0,5)
    y = r.randint(0,5)
    #print("Rolled %d and %d" % (x+1, y+1))

    #print("STYLE:")
    if x == y:
        #print(content[x*6*3 + y] + "\n")
        style = content[x*6*3 + y] + "\n"
    else:
        #print(content[x*6*3 + y] + " or " + content[y*6*3 + x] + "\n")
        style = content[x*6*3 + y] + " or " + content[y*6*3 + x] + "\n"


    x = r.randint(0,5)
    y = r.randint(0,5)
    #print("Rolled %d and %d" % (x+1, y+1))

    #print("FORM:\n")
    if x == y:
        #print(content[12 + x*6*3 + y] + "\n")
        form = content[12 + x*6*3 + y] + "\n"
    else:
        #print(content[12 + x*6*3 + y] + " or " + content[ 12 + y*6*3 + x] + "\n")
        form = content[12 + x*6*3 + y] + " or " + content[ 12 + y*6*3 + x] + "\n"


    x = r.randint(0,5)
    y = r.randint(0,5)
    #print("Rolled %d and %d" % (x+1, y+1))

    #print("ESSENCE:\n")
    if x == y:
        #print(content[6 + x*6*3 + y] + "\n")
        essence = content[6 + x*6*3 + y] + "\n"
    else:
        #print(content[6 + x*6*3 + y] + " or " + content[6 + y*6*3 + x] + "\n")
        essence = content[6 + x*6*3 + y] + " or " + content[6 + y*6*3 + x] + "\n"

    return "*Style:* " + style + "*Form:* " + form + "*Essence:* " + essence