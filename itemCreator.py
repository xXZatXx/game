
#item20 = Helmet("Warriors Helmet", "item20", "The best so far helmet for warriors", 30, 20, 0, 5, 0, 30)

def itemAttr():
    print("Name")
    name = input(": ")
    name = "\"" + name + "\""

    print("Item Number")
    number = input(": ")

    print("Description")
    desc = input(": ")
    desc = "\"" + desc + "\""

    print("Price")
    price = input(": ")

    return name, number, desc, price

def wep():
    print("HP")
    hp = input(": ")

    print("MP")
    mp = input(": ")

    print("STR")
    strr = input(": ")

    print("AGL")
    agl = input(": ")

    return hp, mp, strr, agl

def chan():
    print("Chance")
    chance = input(": ")

    return chance

def rec():
    print("Recipe")
    recipe = input(": ")
    recipe = ("[" + recipe + "]")

    return recipe

def hpA():
    print("Hp Amount")
    hpAmount = input(": ")

    return hpAmount

def loots():
    print("Loot")
    loot = input(": ")
    loot = "[", loot, "]"

    return loot

def itemC():
    print("Item to learn")
    itemC = input(": ")
    
    return itemC


print("1 > Item \n2 > Potion \n3 > Weapon \n4 > Bag \n5 > Helmet \n6 > Chestplate \n7 > Leggings \n8 > Boots \n9 > Scroll")
typee = input(": ")

if typee == "1":
    typee = "Item"

    first = itemAttr()
    third = chan()
    fourth = rec()

elif typee == "2":
    typee = "Potion"

    first = itemAttr()
    fifth = hpA()
    third = chan()
    fourth = rec()

elif typee == "3":
    typee = "Weapon"

    first = itemAttr()
    second = wep()
    third = chan()
    fourth = rec()

elif typee == "4":
    typee = "Bag"

    first = itemAttr()
    sixth = loots()
    
elif typee == "5":
    typee = "Helmet"

    first = itemAttr()
    second = wep()
    third = chan()
    fourth = rec()

elif typee == "6":
    typee = "Chestplate"

    first = itemAttr()
    second = wep()
    third = chan()
    fourth = rec()
    
elif typee == "7":
    typee = "Leggings"

    first = itemAttr()
    second = wep()
    third = chan()
    fourth = rec()
    
elif typee == "8":
    typee = "Boots"

    first = itemAttr()
    second = wep()
    third = chan()
    fourth = rec()

elif typee == "9":
    typee = "CraftingScroll"

    first = itemAttr()
    third = chan()
    itemC = itemC()

name = first[0]
number = first[1]
desc = first[2]
price = first[3]

itemName = "item" + number + " "

if typee == "Item":
    chance = third[0]
    recipe = fourth

    code = typee + "(" + name + ", " + "\"" + itemName + "\"" + ", " + desc + ", " + price + ", " + chance + ", " + recipe + ")"

elif typee == "Weapon" or typee == "Helmet" or typee == "Chestplate" or typee == "Leggings" or typee == "Boots":
    chance = third[0]
    recipe = fourth
    hp = second[0]
    mp = second[1]
    strr = second[2]
    agl = second[3]

    code = typee + "(" + name + ", " + "\"" + itemName + "\"" + ", " + desc + ", " + price + ", " + hp + ", " + mp + ", " + strr + ", " + agl + ", " + chance + ", " + recipe + ")"

elif typee == "Potion":
    hpAmount = fifth[0]
    chance = third[0]
    recipe = fourth

    code = typee + "(" + name + ", " + "\"" + itemName + "\"" + ", " + desc + ", " + price + ", " + hpAmount + ", " + chance + ", " + recipe + ")"

elif typee == "Bag":
    loot = sixth
    chance = third[0]
    recipe = fourth[0]

    code = typee + "(" + name + ", " + "\"" + itemName + "\"" + ", " + desc + ", " + price + ", " + loot + ", " + chance + ", " + recipe + ")"

elif typee == "CraftingScroll":
    chance = third[0]

    code = itemName + " = "+ typee + "(" + name + ", " + "\"" + itemName + "\"" + ", " + desc + ", " + price + ", " + chance + ", " + itemC + ")"



with open("items.py", "r+") as f:
    data = f.readlines()

for i in range(len(data)):
    if itemName in data[i]:
        data[i] = data[i].replace(" 0", " " + code)

with open("items.py", "w") as f:
    f.writelines(data)