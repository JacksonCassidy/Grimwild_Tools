import random as r

def month_name(option):
    f = open("txt/season.txt", "r")
    content = f.read().splitlines()

    offset = option - 1

    x = r.randint(0,5)
    y = r.randint(0,5)

    result = content[12*offset + x] + content[12*offset + 6 + y] + "\n"
    return "    " + result