import random as r

def explore(option):
    f = open("explore.txt", "r")
    content = f.read().splitlines()

    '''
    print("Options:\n1:Building\n2:Settlement\n3:Sites\n4:Dangers\n5:Curiosities\n6:Barrier\n7:Factions")
    opt = input()
    print("\n")
    match opt:
        case "1":
            offset = 0
        case "2":
            offset = 1
        case "3":
            offset = 2
        case "4":
            offset = 3
        case "5":
            offset = 4
        case "6":
            offset = 5
        case "7":
            offset = 6
        case _:
            print("bad input")
            exit()
    '''

    offset = option - 1

    x = r.randint(0,5)
    y = r.randint(0,5)
    #print("Rolled %d and %d" % (x+1, y+1))
    if x == y:
        #print(content[72*offset + x*6*2 + y] + "\n")
        first = content[72*offset + x*6*2 + y] + "\n"
    else:
        #print(content[72*offset +  x*6*2 + y] + " or " + content[72*offset + y*6*2 + x] + "\n")
        first = content[72*offset +  x*6*2 + y] + " or " + content[72*offset + y*6*2 + x] + "\n"


    x = r.randint(0,5)
    y = r.randint(0,5)
    #print("Rolled %d and %d" % (x+1, y+1))
    if x == y:
        #print(content[72*offset + 6 + x*6*2 + y] + "\n")
        second = content[72*offset + 6 + x*6*2 + y] + "\n"
    else:
        #print(content[72*offset + 6 +  x*6*2 + y] + " or " + content[72*offset + 6 + y*6*2 + x] + "\n")
        second = content[72*offset + 6 +  x*6*2 + y] + " or " + content[72*offset + 6 + y*6*2 + x] + "\n"

    return "    " + first + "    " + second