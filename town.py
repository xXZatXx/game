import time
import os
from items import *

clear = lambda: os.system('cls')

def shop(items, player1): #a shop

    itemNames = []
    for i in range(len(items)):
        itemNames.append(items[i].name)

    longestName = max(itemNames, key=len)
    length = len(longestName)

    while True:
        clear()
        print("[ SHOP ]")
        print("==================")
        for i in range(len(items)):
            itemLength = len(items[i].name)
            diff = length - itemLength 

            print(i + 1, "|", items[i].name + ((diff + 2)*" "), items[i].price, "$")

        print("==================")
        print("1 > Buy  2 > Sell  3 > Back")

        inp = input(": ")

        if inp == "1":
            whichItem = int(input("Item(number): "))
            whichItem -= 1

            howM = int(input("How many(number):"))
            print("It will cost", (items[whichItem].price * howM), "$")
            
            print("1 > Buy 2 > Back to shop")
            inp2 = input(": ")
            
            if inp2 == "1" or inp2 == "buy":
                if player1.money >= (items[whichItem].price * howM):
                    player1.giveItem(items[whichItem])
                    print("You bought", items[whichItem].name, "for", (items[whichItem].price * howM), "$")
                    player1.money -= (items[whichItem].price * howM)
                    time.sleep(1)
                else:
                    print("You are low on money, you can't buy it now")
                    time.sleep(1)
            else:
                pass

        if inp == "2":
            clear()
            while True:
                clear()
                print("\n")
                print("[ Inventory ]")
                print("==================")
                player1.showInv()
                print("==================")

                tempInp = input(": ")
                if tempInp == "1":
                    try:
                        whichItem = int(input("Item(number): "))
                        whichItem -= 1

                        print(player1.data[whichItem].name)
                        print("You will get", int(round(player1.data[whichItem].price/2)), "$")
                        print("Are you sure you wanna sell it?")
                        print("1 > Yes")
                        print("2 > No")
                        choices = input(":")

                        if choices == "1" or choices == "Yes":
                            player1.money += int(round(player1.data[whichItem].price/2))
                            player1.removeItem(player1.data[whichItem])
                        else:
                            pass

                    except:
                        print("Something went wrong try again :)")

                elif tempInp == "2":
                    break

            if inp == "3":
                break        

            print("\n")

def explore(player1, place):
    if place == "cave":
        placeLoot = [item3, item4, item5, item6]

    while True:
        if player1.time == 0 and player1.expLocation == "none":
            print("Do you want to explore a " + place + "?")
            print("1 > Yes")
            print("2 > No")
            tempInp = input(": ")

            if tempInp == "1":
                player1.expLocation = place
                player1.time = 120
                print("You are exploring", player1.expLocation, "right now")
                print("Time left:", player1.time, "s")
                backInp = input("Press Enter to go back")
                break
            elif tempInp == "2":
                pass
        
        elif player1.expLocation != "none" and player1.time == 0:
            player1.expLocation = "none"
            print("You've done exploring!")
            print("[ LOOT ]")
            for i in range(len(placeLoot)):
                rand = randint(1, 100)
                if rand >= placeLoot[i].chance:
                    rand2 = randint(1, 100)
                    if rand2 > 70:
                        rand2 = 2
                    elif rand2 > 99:
                        rand2 = 3
                    else:
                        rand2 = 1
                    
                    print(placeLoot[i].name, rand2)

                    for j in range(rand2):
                        player1.giveItem(placeLoot[i])

            tempInp = input("Press Enter to go back")
            break

        elif player1.expLocation != "none":
            print("You are exploring", player1.expLocation, "right now")
            print("Time left:", player1.time, "s")

            backInp = input("Press Enter to go back")
            break
        

        else:
            print("yeet")
        
        


    

