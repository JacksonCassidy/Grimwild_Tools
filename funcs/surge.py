import random as r

def wild_surge():
    f = open("txt/surge.txt", "r")
    content = f.read().splitlines()

    s = r.randint(1,6)
    s2 = r.randint(1,6)

    path = r.randint(0,7)
    tech = r.randint(0,7)

    match path:
        case 0:
            path_s = "blood"
        case 1:
            path_s = "decay"
        case 2:
            path_s = "flame"
        case 3:
            path_s = "frost"
        case 4:
            path_s = "lux"
        case 5:
            path_s = "shadow"
        case 6:
            path_s = "stone"
        case 7:
            path_s = "tempest"
        case _:
            return
    
    match tech:
        case 0:
            tech_s = "attack"
        case 1:
            tech_s = "create"
        case 2:
            tech_s = "defend"
        case 3:
            tech_s = "enhance"
        case 4:
            tech_s = "hinder"
        case 5:
            tech_s = "influence"
        case 6:
            tech_s = "transform"
        case 7:
            tech_s = "traverse"
        case _:
            return

    x = r.randint(0,5)
    y = r.randint(0,5)

    x2 = r.randint(0,5)
    y2 = r.randint(0,5)


    if x==y:
        a = content[x*6 + y]
    else:
        a = content[x*6 + y] + " or " + content[y*6 + x]

    if x2==y2:
        b = content[36 + x2*6 + y2]
    else:
        b = content[36 + x2*6 + y2] + " or " + content[36 + y2*6 + x2]

    story_roll = "*Story Roll:*\n    " + str(s) + ", " + str(s2) + "\n"

    path_tech = "*Sorcery path:*\n    " + path_s + "\n" + "*Sorcery technique:*\n    " + tech_s + "\n"

    return story_roll + "*Wild Surge:*\n    " + a + "\n    " + b + "\n" + path_tech