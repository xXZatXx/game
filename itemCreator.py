
#item20 = Helmet("Warriors Helmet", "item20", "The best so far helmet for warriors", 30, 20, 0, 5, 0, 30)

print("1 > Item \n2 > Potion \n3 > Weapon \n4 > Bag \n5 > Helmet \n6 > Chestplate \n7 > Leggings \n8 > Boots")
typee = input(": ")

if typee == "1":
    typee = "Item"
elif typee == "2":
    typee = "Potion"
elif typee == "3":
    typee = "Weapon"
elif typee == "4":
    typee = "Bag"
elif typee == "5":
    typee = "Helmet"
elif typee == "6":
    typee = "Chestplate"
elif typee == "7":
    typee = "Leggings"
elif typee == "8":
    typee = "Boots"

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

print("HP")
hp = input(": ")

print("MP")
mp = input(": ")

print("STR")
strr = input(": ")

print("AGL")
agl = input(": ")

print("Chance")
chance = input(": ")


code = "item" + number + " = "+ typee + "(" + name + ", " + "\"" + "item" + number + "\"" + ", " + desc + ", " + price + ", " + hp + ", " + mp + ", " + strr + ", " + agl + ", " + chance + ")\n"

with open("items.py", "a") as f:
    f.write(code)