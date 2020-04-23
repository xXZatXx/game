from random import randint
import time
import os
from classes import * 
from enemies import *
from fighting import *
from inventory import *

clear = lambda: os.system('cls')

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
    with open("save1.txt", "a") as f:
        f.write(str(player1.name) + "\n")
        f.write(str(player1.pClass) + "\n")
        f.write(str(player1.hp) + "\n")
        f.write(str(player1.maxHp) + "\n")
        f.write(str(player1.mn) + "\n")
        f.write(str(player1.str) + "\n")
        f.write(str(player1.agl) + "\n")
        for i in range(len(player1.items)):
            f.write(str(player1.items[i].name) + "\n")
        for j in range(len(player1.on)):
            f.write(str(player1.on[j].name) + "\n")
        f.write(str(player1.lvl) + "\n")
        f.write(str(player1.xp) + "\n")
        f.write(str(player1.lvlXp) + "\n")

    f.close()

        



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

        elif pClass == "2" or pClass == "archer":
            pClass = 1
            php = 80
            pmn = 50
            pstr = 10
            pagl = 20
        elif pClass == "3" or pClass == "mage":
            pClass = 2
            php = 80
            pmn = 100
            pstr = 5
            pagl = 10
        else:
            print("Error: Wrong class")

    clear()
    print("Character created!")
    player1 = Player(name, pClass, php, pmn, pstr, pagl)
    player1.giveItem(item1)

print("IM JUST BORED THE GAME")
print("1 > Start")
print("2 > Continue")
print("3 > Quit")

inp = input(": ").lower()


if inp == "1" or inp == "start":
    start()

    while True:
        if player1.xp >= player1.lvlXp:
            player1.lvlup()

        player1.stats()
        
        print("------------------")
        print("MENU")
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
                ogre = Enemy("Ogre", 50, 0, 15, 5) 
                tempHp = battle(player1, ogre)
                player1.hp = tempHp
                player1.round = 1
                clear()

        elif what == "3":
            print("[ Inventory ]")
            print("==================")
            player1.showInv()
            print("==================")
            print("1 > Use  2 > Info  3 > Drop")

            invOp = input("")
            
            if invOp == "1":
                whichItem = int(input("Item(number): "))

                try:
                    if isinstance(player1.items[whichItem], Potion) == True:
                        #if is a potion
                        player1.items[whichItem].heal(player1)
                        player1.removeItem(player1.items[whichItem])
                    elif isinstance(player1.items[whichItem], Weapon) == True: 
                        #if is a weapon
                        player1.equip(player1.items[whichItem])
                except:
                    print("Wrong item number or nothing in inventory")

            if invOp == "2":
                whichItem = int(input("Item(number): "))
                try:
                    if isinstance(player1.items[whichItem], Item) == True:
                        #if is a potion
                        player1.items[whichItem].showDescription()
                        print("Return(write anything)")
                        tempInp = input(": ")

                    else:
                        #if is a weapon
                        print("What?")
                except: 
                    print("Wrong item number or nothing in inventory")

        elif what == "4":
            print("Player info:")
            player1.stats()
            player1.showEquiped()

            tempInp = input("Press Anything")

        elif what == "5":
            save()

        elif what == "6":
            exit()
        
        elif what == "420":
            player1.xp += 199

        elif what == "69":
            player1.giveItem(item4)


elif inp == "2" or inp == "continue":
    #nothing yet
    print("AAh")
elif inp == "3" or inp == "quit":
    exit()
else:
    print("Error: Wrong input")
