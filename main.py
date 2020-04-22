from classes import * 
import enemies

player = "none"

def start():
    global player

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
        elif pClass == "2" or pClass == "archer":
            pClass = 1
        elif pClass == "3" or pClass == "mage":
            pClass = 2
        else:
            print("Error: Wrong class")

    print("Character created!")
    player = Player(name, pClass)

print("IM JUST BORED THE GAME")
print("1 > Start")
print("2 > Continue")
print("3 > Quit")

inp = input(": ").lower()


if inp == "1" or inp == "start":
    start()
    player.stats()
elif inp == "2" or inp == "continue":
    #nothing yet
    print("nice to see ya there")
elif inp == "3" or inp == "quit":
    exit()
else:
    print("Error: Wrong input")