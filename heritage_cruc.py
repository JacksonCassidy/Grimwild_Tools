import random as r

def rand_heritage():

    f = open("heritage.txt", "r")
    content = f.read().splitlines()


    x = r.randint(0,5)
    y = r.randint(0,5)
    #print("Rolled %d and %d" % (x+1, y+1))

    #print("FOLK:")
    if x == y:
        #print(content[x*6*3 + y] + "\n")
        folk = content[x*6*3 + y] + "\n"
    else:
        #print(content[x*6*3 + y] + " or " + content[y*6*3 + x] + "\n")
        folk = content[x*6*3 + y] + " or " + content[y*6*3 + x] + "\n"


    x = r.randint(0,5)
    y = r.randint(0,5)
    #print("Rolled %d and %d" % (x+1, y+1))

    #print("MOOD:\n")
    if x == y:
        #print(content[12 + x*6*3 + y] + "\n")
        mood = content[12 + x*6*3 + y] + "\n"
    else:
        #print(content[12 + x*6*3 + y] + " or " + content[ 12 + y*6*3 + x] + "\n")
        mood = content[12 + x*6*3 + y] + " or " + content[ 12 + y*6*3 + x] + "\n"


    x = r.randint(0,5)
    y = r.randint(0,5)
    #print("Rolled %d and %d" % (x+1, y+1))

    #print("LAND:\n")
    if x == y:
        #print(content[6 + x*6*3 + y] + "\n")
        land = content[6 + x*6*3 + y] + "\n"
    else:
        #print(content[6 + x*6*3 + y] + " or " + content[6 + y*6*3 + x] + "\n")
        land = content[6 + x*6*3 + y] + " or " + content[6 + y*6*3 + x] + "\n"

    return "*Folk:* " + folk + "*Mood:* " + mood + "*Land:* " + land