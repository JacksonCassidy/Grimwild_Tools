import random as r

def rand_herb():
    f = open("txt/herbs.txt", "r")
    content = f.read().splitlines()

    x = r.randint(0,5)
    y = r.randint(0,5)

    x2 = r.randint(0,5)
    y2 = r.randint(0,5)

    if x==y:
        prefix = [content[x*6 + y]]
    else:
        prefix = [content[x*6 + y], content[y*6 + x]]

    if x2==y2:
        suffix = [content[36 + x2*6 + y2]]
    else:
        suffix = [content[36 + x2*6 + y2], content[36 + y2*6 + x2]]


    output = ""
    for i in prefix:
        for j in suffix:
            output += "    " + i + j + "\n"
    
    return "*Herbs:*\n" + output