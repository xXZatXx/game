from random import randint
import time
import os
from classes import * 
from enemies import *
from fighting import *

clear = lambda: os.system('cls')

player1 = "none"

#progress bar
#print("[" + u"\u25AE" u"\u25AE" u"\u25AE" u"\u25AE" u"\u25AE" + "]")

def save():
    print(player1)

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

print("IM JUST BORED THE GAME")
print("1 > Start")
print("2 > Continue")
print("3 > Quit")

inp = input(": ").lower()


if inp == "1" or inp == "start":
    start()

    while True:
        player1.stats()

        if player1.xp > player1.lvlXp:
            player1.lvlup()

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
                tempHp = battle(player1, ogre)
                player1.hp = tempHp
                clear()

        elif what == "4":
            print("Player info:")
            player1.stats()
        
        elif what == "5":
            save()

        elif what == "6":
            exit()
        
        elif what == "420":
            player1.xp = 199


elif inp == "2" or inp == "continue":
    #nothing yet
    print("AAh")
elif inp == "3" or inp == "quit":
    exit()
else:
    print("Error: Wrong input")

