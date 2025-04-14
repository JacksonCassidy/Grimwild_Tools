import random as r

def rand_heritage():

    f = open("txt/heritage.txt", "r")
    content = f.read().splitlines()

    x = r.randint(0,5)
    y = r.randint(0,5)

    if x == y:
        folk = content[x*6*3 + y] + "\n"
    else:
        folk = content[x*6*3 + y] + " or " + content[y*6*3 + x] + "\n"

    x = r.randint(0,5)
    y = r.randint(0,5)

    if x == y:
        mood = content[12 + x*6*3 + y] + "\n"
    else:
        mood = content[12 + x*6*3 + y] + " or " + content[ 12 + y*6*3 + x] + "\n"

    x = r.randint(0,5)
    y = r.randint(0,5)

    if x == y:
        land = content[6 + x*6*3 + y] + "\n"
    else:
        land = content[6 + x*6*3 + y] + " or " + content[6 + y*6*3 + x] + "\n"

    return "*Folk:* " + folk + "*Mood:* " + mood + "*Land:* " + land