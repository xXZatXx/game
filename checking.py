Hp = "Hp"
Mp = "Mp"
Str = "Str"
Agl = "Agl"

Items = ["Item1", "Item2", "Item3", "Item4"]
Equipped = ["Item1", "Item2", "Item3", "Item3", "Item3", "Item3"]
Skills = ["Skill1", "Skill2", "Skill3", "Skill4"] 

def save():
    with open("Test.txt", "a") as f:
        f.write(Hp + "\n")
        f.write(Mp + "\n")
        f.write(Str + "\n")
        f.write(Agl + "\n")
        for i in range(len(Items)):
            f.write(Items[i] + "\n")
        for i in range(len(Skills)):
            f.write(Skills[i] + "\n")
        for i in range(len(Equipped)):
            f.write("EQ" + Equipped[i] + "\n")    

def load():
    data = []
    items = []

    with open("Test.txt", "r") as f:
        for line in f:
            data.append(line.replace("\n", ""))

    player = data
    
    for i in range(len(player)):
        if "Item" in player[i]:
            items.append(player[i])

    print(items)

load()
