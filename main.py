from random import randint
import time
import os
import random
from classes import Enemy, Player
from fighting import *
from iclasses import *
from items import *
from town import shop, explore
import threading


clear = lambda: os.system('cls')

info = []
items = []
eq = []
rc = []

player1 = "none"

#progress bar
#print("[" + u"\u25AE" u"\u25AE" u"\u25AE" u"\u25AE" u"\u25AE" + "]")



def save(saveSlot): #saving the game

    if os.path.exists('save' + str(saveSlot) + '.txt'):
        os.remove('save' + str(saveSlot) + '.txt') 

    with open("save"+ str(saveSlot) +".txt", "a") as f:
        f.write(str(player1.name) + "\n")
        f.write(str(player1.pClass) + "\n")
        f.write(str(player1.hp) + "\n")
        f.write(str(player1.maxHp) + "\n")
        f.write(str(player1.mp) + "\n")
        f.write(str(player1.str) + "\n")
        f.write(str(player1.agl) + "\n")
        f.write(str(player1.lvl) + "\n")
        f.write(str(player1.xp) + "\n")
        f.write(str(player1.lvlXp) + "\n")
        f.write(str(player1.money) + "\n")
        f.write(str(player1.battles) + "\n")
        f.write(str(player1.saveSlot) + "\n")
        f.write(str(player1.time) + "\n")
        f.write(str(player1.expLocation) + "\n")

        for i in range(len(player1.items)):
            f.write(str(player1.items[i].varN + "\n"))

        for i in range(len(player1.on)):
            f.write(str(player1.on[i].varN.upper() + "\n"))

        for i in range(len(player1.recipes)):
            f.write(str("iCtem" + player1.recipes[i].varN.replace("item", "") + "\n"))

    f.close()

def load(saveSlot): #loading the game

    with open("save" + str(saveSlot) + ".txt", "r") as f:
        for line in f:
            if "item" in line:
                items.append(line.replace("\n", ""))
            elif "ITEM" in line:
                eq.append(line.replace("\n", "").lower())
            elif "iCtem" in line:
                rc.append(line.replace("C", "").replace("\n", ""))
            else:
                info.append(line.replace("\n", ""))

    if info == []:
        print("Nothing to load")
    else:
        return info, items, eq, rc

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
            pmp = 50
            pstr = 20
            pagl = 10

            player1 = Player(name, pClass, php, pmp, pstr, pagl)
            player1.giveItem(item150)

        elif pClass == "2" or pClass == "archer":
            pClass = 1
            php = 80
            pmp = 50
            pstr = 10
            pagl = 20

            player1 = Player(name, pClass, php, pmp, pstr, pagl)
            player1.giveItem(item151)

        elif pClass == "3" or pClass == "mage":
            pClass = 2
            php = 80
            pmp = 100
            pstr = 5
            pagl = 10

            player1 = Player(name, pClass, php, pmp, pstr, pagl)
            player1.giveItem(item152)

        else:
            print("Error: Wrong class")

    clear()
    print("Character created!")
    player1.giveItem(item1)
    player1.saveSlot = slot

def exploring():
    while player1.time > 0:
        player1.time -= 1
        time.sleep(1)

def startThreading():
    explore = threading.Thread(target=exploring, args=())
    explore.start()

def game():
    while True:
        if player1.xp >= player1.lvlXp:
            player1.lvlup()

        player1.stats()

        startThreading()

        print("------------------")
        print("MENU")
        print("------------------")
        print("1 > Fight")
        print("2 > Town")
        print("3 > Inventory")
        print("4 > Player info")
        print("5 > Recipe Book")
        print("6 > Save")
        print("")
        print("7 > Exit")
        print("------------------\n")

        what = input(": ")

        if what == "1":
            if player1.expLocation == "none":
                print("Rolling the dice...")
                time.sleep(2)
                rndNum = randint(1, 6)
                print(rndNum)

                if rndNum in range(1, 5):
                    ogre = Enemy("Ogre", [item2, item70] ,50, 0, 15, 5, 20) 
                    dwarf = Enemy("Dwarf", [item70] ,40, 0, 15, 25, 15)
                    
                    enemies = [ogre, dwarf]

                    tempHp = battle(player1, random.choice(enemies))
                    player1.hp = tempHp
                    player1.round = 1
                    clear()

                elif rndNum == 6 :
                    if player1.battles >= 10:
                        ogreKing = Boss("Ogre King", [item1, item2, item3], 150, 10, 30, 15, 150, 400) 
                        
                        enemies = [ogreKing]

                        tempHp = battle(player1, random.choice(enemies))
                        player1.hp = tempHp
                        player1.round = 1
                        clear()
                    else:
                        print("Your battles arent over 10. You can't fight boss now")
                        time.sleep(1)
            else:
                print("You are exploring now you can't fight")
                time.sleep(1)


        elif what == "2":
            print("TOWN")
            print("------------------")
            print("1 > Shop")
            print("2 > Explore")
            print("3 > Blacksmith")
            print("------------------")

            tempInp = input(": ")
            if tempInp == "1":
                shop([item70, item71, item72, item350], player1)
            elif tempInp == "2":
                explore(player1, "cave")
            elif tempInp == "3":
                pass
        elif what == "3": #inventory
            while True:
                clear()
                print("\n")
                player1.showEquiped()
                print("[ Inventory ]")
                print("==================")
                player1.showInv()

                #for i in range(len(player1.data)):
                #        try:
                #            print(player1.data[i].name)
                #        except:
                #            print(player1.data[i])

                print("==================")
                print("1 > Use  2 > Info 3 > Unequip  4 > Drop  5 > Back")

                invOp = input("")
                
                if invOp == "1": #using / equiping stuff
                    whichItem = int(input("Item(number): "))
                    whichItem -= 1

                    try:
                        if isinstance(player1.data[whichItem], Potion) == True:
                            #if is a potion
                            player1.data[whichItem].heal(player1)
                            player1.removeItem(player1.data[whichItem])

                        elif isinstance(player1.data[whichItem], Weapon) == True: 
                            #if is a weapon

                            if any(isinstance(x, Weapon) for x in player1.on) == True:
                                
                                for i in range(len(player1.on)):
                                    if isinstance(player1.on[i], Weapon) == True:
                                        print("You can equip it, you already have a weapon equiped")
                                        time.sleep(1)
                            else:
                                player1.equip(player1.data[whichItem])

                        elif isinstance(player1.data[whichItem], Helmet) == True: 
                            #if is a helmet

                            if any(isinstance(x, Helmet) for x in player1.on) == True:
                                
                                for i in range(len(player1.on)):
                                    if isinstance(player1.on[i], Helmet) == True:
                                        print("You can equip it, you already have a helmet equiped")
                                        time.sleep(1)
                            else:
                                player1.equip(player1.data[whichItem])

                        elif isinstance(player1.data[whichItem], Chestplate) == True: 
                            #if is a weapon

                            if any(isinstance(x, Chestplate) for x in player1.on) == True:
                                
                                for i in range(len(player1.on)):
                                    if isinstance(player1.on[i], Chestplate) == True:
                                        print("You can equip it, you already have a chestplate equiped")
                                        time.sleep(1)
                            else:
                                player1.equip(player1.data[whichItem])

                        elif isinstance(player1.data[whichItem], Leggings) == True: 
                            #if is a weapon

                            if any(isinstance(x, Leggings) for x in player1.on) == True:
                                
                                for i in range(len(player1.on)):
                                    if isinstance(player1.on[i], Leggings) == True:
                                        print("You can equip it, you already have leggings equiped")
                                        time.sleep(1)
                            else:
                                player1.equip(player1.data[whichItem])

                        elif isinstance(player1.data[whichItem], Boots) == True: 
                            #if is a weapon

                            if any(isinstance(x, Boots) for x in player1.on) == True:
                                
                                for i in range(len(player1.on)):
                                    if isinstance(player1.on[i], Boots) == True:
                                        print("You can equip it, you already have boots equiped")
                                        time.sleep(1)
                            else:
                                player1.equip(player1.data[whichItem])
                        
                        elif isinstance(player1.data[whichItem], Bag) == True: 
                            #if is a bag
                            if player1.items != player1.bagLimit:
                                player1.data[whichItem].giveLoot(player1)
                                player1.removeItem(player1.data[whichItem])
                            else:
                                print("Bag is full")
                            time.sleep(1)

                        elif isinstance(player1.data[whichItem], CraftingScroll) == True:
                            #if is a craftingScroll
                            player1.learnRecipe(globals()[player1.data[whichItem].varN])
                            player1.removeItem(player1.data[whichItem])
                            time.sleep(1)

                        else:
                            print("You can't use this item")
                            time.sleep(1)
                    except:
                        print("Wrong item number or nothing in inventory")
                        time.sleep(5)

                if invOp == "2": #info about items
                    whichItem = int(input("Item(number): "))
                    whichItem -= 1

                    try:
                        if isinstance(player1.data[whichItem], Item) == True:
                            #if is a potion
                            player1.data[whichItem].showDescription()
                            print("Press Enter to return")
                            tempInp = input(": ")

                        else:
                            #if is a weapon
                            print("What?")
                    except: 
                        print("Wrong item number or nothing in inventory")

                if invOp == "4": #droping an item
                    try:
                        print("Are you sure?")
                        print("1 > Yes")
                        print("2 > No")
                        inp = input(": ")

                        if inp == "1":
                            try:
                                whichItem = int(input("Item(number):"))
                                whichItem -= 1 
                                player1.drop(player1.data[whichItem])
                            except:
                                print("Something went wrong")

                        if inp == "2":
                            pass
                    except:
                        print("Something went wrong")
                
                if invOp == "3": #unequiping stuff
                    whichItem = int(input("Item(number):"))
                    whichItem -= 1

                    try:
                        player1.unEquip(player1.on[whichItem])
                    except:
                        print("Wrong item number or nothing equiped")

                if invOp == "5": #gettin back
                    break

        elif what == "4": #player info
            print("Player info:")
            player1.stats()
            print("Number of battles:", player1.battles, "\n")
            player1.showEquiped()

            tempInp = input("Press Enter to return")

        elif what == "5":
            while True:
                player1.showRecipes()

                print("1 > Craft  2 > Back")
                inp = input(": ")

                if inp == "1" or inp == "craft":
                    whichItem = int(input("Item(number): "))
                    whichItem -= 1

                    try:
                        player1.craft(player1.recipes[whichItem])
                    except:
                        print("Error")
                else:
                    break

        elif what == "6": #saving
            save(int(player1.saveSlot))

        elif what == "7": #exit
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

        elif "give money" in what:
            what = what.replace("give money ", "")
            what = int(what)
            try:
                player1.money += what
            except:
                print("yeet")


print("IM JUST BORED THE GAME")
print("1 > Start")
print("2 > Continue")
print("3 > Quit")

inp = input(": ").lower()


if inp == "1" or inp == "start": #start the game
    if os.path.exists('save1.txt'):
        print("1 > Save slot")
        sts = load(1)
        info, items, eq, rc = [], [], [], []
        print("Name:", sts[0][0], "Class:", sts[0][1], "HP", sts[0][3], "MP", sts[0][4], "STR", sts[0][5], "AGL", sts[0][6])
    else:
        print("1 > Save slot")
        print("NOTHING THERE")

    if os.path.exists('save2.txt'):
        print("2 > Save slot")
        sts = load(2)
        info, items, eq, rc = [], [], [], []
        print("Name:", sts[0][0], "Class:", sts[0][1], "HP", sts[0][3], "MP", sts[0][4], "STR", sts[0][5], "AGL", sts[0][6])
    else:
        print("2 > Save slot")
        print("NOTHING THERE")

    if os.path.exists('save3.txt'):
        print("3 > Save slot")
        sts = load(3)
        info, items, eq, rc = [], [], [], []
        print("Name:", sts[0][0], "Class:", sts[0][1], "HP", sts[0][3], "MP", sts[0][4], "STR", sts[0][5], "AGL", sts[0][6])
    else:
        print("3 > Save slot")
        print("NOTHING THERE")


    slot = input(": ")

    if isinstance(slot, str):
        if slot == "1" or slot == "2" or slot == "3":
            slot = int(slot)

            if slot < 4:
                start()
                game()
            else:
                print("Wrong slot")
        else:
            print("An error happened")

elif inp == "2" or inp == "continue": #continue the game from saving slot

    if os.path.exists('save1.txt'):
        print("1 > Save slot")
        sts = load(1)
        info, items, eq, rc = [], [], [], []
        print("Name:", sts[0][0], "Class:", sts[0][1], "HP", sts[0][3], "MP", sts[0][4], "STR", sts[0][5], "AGL", sts[0][6])
    else:
        print("1 > Save slot")
        print("NOTHING THERE")

    if os.path.exists('save2.txt'):
        print("2 > Save slot")
        sts = load(2)
        info, items, eq, rc = [], [], [], []
        print("Name:", sts[0][0], "Class:", sts[0][1], "HP", sts[0][3], "MP", sts[0][4], "STR", sts[0][5], "AGL", sts[0][6])
    else:
        print("2 > Save slot")
        print("NOTHING THERE")

    if os.path.exists('save3.txt'):
        print("3 > Save slot")
        sts = load(3)
        info, items, eq, rc = [], [], [], []
        print("Name:", sts[0][0], "Class:", sts[0][1], "HP", sts[0][3], "MP", sts[0][4], "STR", sts[0][5], "AGL", sts[0][6])
    else:
        print("3 > Save slot")
        print("NOTHING THERE")


    slot = input(": ")
    
    lol = load(int(slot))

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
        player1.saveSlot = int(lol[0][12])
        player1.time = int(lol[0][13])
        player1.expLocation = lol[0][14]

        for i in range(len(lol[1])):
            player1.giveItem(globals()[lol[1][i]])

        for j in range(len(lol[2])):
            player1.on.append(globals()[lol[2][j]])

        for k in range(len(lol[3])):
            player1.recipes.append(globals()[lol[3][k]])

        game()  
    
elif inp == "3" or inp == "quit": #closes the game
    exit()

else:
    print("Error: Wrong input")
