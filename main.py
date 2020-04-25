from random import randint
import time
import os
import random
from classes import Enemy, Player
from fighting import *
from inventory import *


clear = lambda: os.system('cls')

info = []
items = []
eq = []

player1 = "none"

#progress bar
#print("[" + u"\u25AE" u"\u25AE" u"\u25AE" u"\u25AE" u"\u25AE" + "]")

def save():
    #self.name = name
    #self.pClass = pClass
    #self.hp = health
    #self.maxHp = health 
    #self.mn = mana
    #self.str = strength
    #self.agl = agility
    #self.items = []
    #self.on = []
    #self.round = 1
    #self.lvl = 1
    #self.xp = 0
    #self.lvlXp = 200
    if os.path.exists('save1.txt'):
        os.remove('save1.txt') 
    if os.path.exists('save1i.txt'):
        os.remove('save1i.txt') 
    if os.path.exists('save1e.txt'):
        os.remove('save1e.txt') 

    with open("save1.txt", "a") as f:
        f.write(str(player1.name) + "\n")
        f.write(str(player1.pClass) + "\n")
        f.write(str(player1.hp) + "\n")
        f.write(str(player1.maxHp) + "\n")
        f.write(str(player1.mn) + "\n")
        f.write(str(player1.str) + "\n")
        f.write(str(player1.agl) + "\n")
        f.write(str(player1.lvl) + "\n")
        f.write(str(player1.xp) + "\n")
        f.write(str(player1.lvlXp) + "\n")
        f.write(str(player1.money) + "\n")
        f.write(str(player1.battles) + "\n")

    f.close()

    with open("save1i.txt", "a") as f2:
        for i in range(len(player1.items)):
            f2.write(str(player1.items[i].varN) + "\n")

    f2.close()

    with open("save1e.txt", "a") as f3:
        for j in range(len(player1.on)):
            f3.write(str(player1.on[j].varN) + "\n")

    f3.close()

def load():
    with open("save1.txt", "r") as f:
        for line in f:
            info.append(line.replace("\n", ""))

    with open("save1i.txt", "r") as f2:
        for line in f2:
            items.append(line.replace("\n", ""))

    with open("save1e.txt", "r") as f3:
        for line in f3:
            eq.append(line.replace("\n", ""))

    if info == []:
        print("Nothing to load")
    else:
        return info, items, eq


def start():
    global player1

    name = 0
    pClass = 3

    while name == 0 or len(str(name)) > 8:
        print("Enter your name")
        name = input(": ")
        if len(str(name)) > 8:
            print("Error: Name to long max 8 characters")
    
    while pClass == 3:
        print("Choose your class")
        print("1 > Warrior")
        print("2 > Archer")
        print("3 > Mage")

        pClass = input(": ").lower()

        if pClass == "1" or pClass == "warrior":
            pClass = 0
            php = 100
            pmn = 50
            pstr = 20
            pagl = 10

            player1 = Player(name, pClass, php, pmn, pstr, pagl)
            player1.giveItem(item4)

        elif pClass == "2" or pClass == "archer":
            pClass = 1
            php = 80
            pmn = 50
            pstr = 10
            pagl = 20

            player1 = Player(name, pClass, php, pmn, pstr, pagl)
            player1.giveItem(item5)

        elif pClass == "3" or pClass == "mage":
            pClass = 2
            php = 80
            pmn = 100
            pstr = 5
            pagl = 10

            player1 = Player(name, pClass, php, pmn, pstr, pagl)
            player1.giveItem(item6)

        else:
            print("Error: Wrong class")

    clear()
    print("Character created!")
    player1.giveItem(item1)

def game():
    while True:
        if player1.xp >= player1.lvlXp:
            player1.lvlup()

        player1.stats()
        
        print("------------------")
        print("MENU")
        print("------------------")
        print("1 > Fight")
        print("2 > Shop")
        print("3 > Inventory")
        print("4 > Player info")
        print("5 > Save")
        print("")
        print("6 > Exit")
        print("------------------\n")

        what = input(": ")


        if what == "1":
            print("Rolling the dice...")
            time.sleep(2)
            rndNum = randint(1, 6)
            print(rndNum)

            if rndNum in range(1, 6):
                ogre = Enemy("Ogre", [item7, item1] ,50, 0, 15, 5, 20) 
                dwarf = Enemy("Dwarf", [item1] ,40, 0, 15, 25, 15)
                
                enemies = [ogre, dwarf]

                tempHp = battle(player1, random.choice(enemies))
                player1.hp = tempHp
                player1.round = 1
                clear()

        elif what == "3":
            while True:
                clear()
                print("[ Inventory ]")
                print("==================")
                player1.showInv()
                print("==================")
                print("1 > Use  2 > Info 3 > Unequip  4 > Drop  5 > Back")

                invOp = input("")
                
                if invOp == "1":
                    whichItem = int(input("Item(number): "))
                    whichItem -= 1

                    try:
                        if isinstance(player1.items[whichItem], Potion) == True:
                            #if is a potion
                            player1.items[whichItem].heal(player1)
                            player1.removeItem(player1.items[whichItem])
                        elif isinstance(player1.items[whichItem], Weapon) == True: 
                            #if is a weapon

                            if any(isinstance(x, Weapon) for x in player1.on) == True:
                                
                                for i in range(len(player1.on)):
                                    if isinstance(player1.on[i], Weapon) == True:
                                        print("You can equip it, you already have a weapon equiped")
                                        time.sleep(1)

                            else:
                                player1.equip(player1.items[whichItem])

                        elif isinstance(player1.items[whichItem], Bag) == True: 
                            #if is a bag
                            if player1.items != player1.bagLimit:
                                player1.items[whichItem].giveLoot(player1)
                                player1.removeItem(player1.items[whichItem])
                            else:
                                print("Bag is full")
                            time.sleep(1)

                        else:
                            print("You can't use this item")
                            time.sleep(1)

                    except:
                        print("Wrong item number or nothing in inventory")
                        time.sleep(1)

                if invOp == "2":
                    whichItem = int(input("Item(number): "))
                    try:
                        if isinstance(player1.items[whichItem], Item) == True:
                            #if is a potion
                            player1.items[whichItem].showDescription()
                            print("Press Enter to return")
                            tempInp = input(": ")

                        else:
                            #if is a weapon
                            print("What?")
                    except: 
                        print("Wrong item number or nothing in inventory")

                if invOp == "4":
                    whichItem = int(input("Item(number):"))

                    inp = input("Are you sure?")
                    print("1 > Yes")
                    print("2 > No")

                    if inp == "1":
                        player1.drop(player1.items[whichItem])

                    if inp == "2":
                        pass
                
                if invOp == "3":
                    whichItem = int(input("Item(number):"))
                    whichItem -= 1

                    try:
                        player1.unEquip(player1.on[whichItem])
                    except:
                        print("Wrong item number or nothing equiped")


                if invOp == "5":
                    break

        elif what == "4":
            print("Player info:")
            player1.stats()
            print("Number of battles:", player1.battles, "\n")
            player1.showEquiped()

            tempInp = input("Press Enter to return")

        elif what == "5":
            save()

        elif what == "6":
            exit()
        
        elif what == "420":
            player1.xp += 199

        elif what == "69":
            player1.giveItem(item4)
        
        elif "give item" in what:
            what = what.replace("give item ", "")
            if player1.items != player1.bagLimit:
                try:
                    player1.giveItem(globals()[what])
                except:
                    print("Wrong item name")
            else:
                print("Bag is full")
            

print("IM JUST BORED THE GAME")
print("1 > Start")
print("2 > Continue")
print("3 > Quit")

inp = input(": ").lower()


if inp == "1" or inp == "start":
    start()
    game()

elif inp == "2" or inp == "continue":
    #self.name = name
    #self.pClass = pClass
    #self.hp = health
    #self.maxHp = health 
    #self.mn = mana
    #self.str = strength
    #self.agl = agility
    #self.items = []
    #self.on = []
    #self.round = 1
    #self.lvl = 1
    #self.xp = 0
    #self.lvlXp = 200
    lol = load()

    if lol == []:
        pass
    else:

        if lol[0][1] == "Warrior":
            lol[0][1] = 0
        elif lol[0][1] == "Archer":
            lol[0][1] = 1
        elif lol[0][1] == "Mage":
            lol[0][1] = 2

        player1 = Player(lol[0][0], lol[0][1], int(lol[0][3]), int(lol[0][4]), int(lol[0][5]), int(lol[0][6]))
        player1.hp = int(lol[0][2])
        player1.lvl = int(lol[0][7])
        player1.xp = int(lol[0][8])
        player1.lvlXp = int(lol[0][9])
        player1.money = int(lol[0][10])
        player1.battles = int(lol[0][11])

        for i in range(len(lol[1])):
            player1.giveItem(globals()[lol[1][i]])

        for j in range(len(lol[2])):
            player1.on.append(globals()[lol[2][j]])

        game()
    
elif inp == "3" or inp == "quit":
    exit()
else:
    print("Error: Wrong input")
