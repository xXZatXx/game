import time
from random import randint

from classes import *
import enemies

def battle(player, enemy):
    global tempHp
    print("==| BATTLE STARTED! |==")

    print("Your enemy is:", enemy.name)
    enemy.stats()

    while player.hp > 0:

        if player.agl > enemy.agl and enemy.hp >= 0:
            player.attack(enemy)
            print("You attacked the enemy for:", player.str)
            time.sleep(2)
        
        if enemy.hp >= 0:
            enemy.attack(player)
            print("Enemy attacked you for:", enemy.str)
            time.sleep(2)

            player.showHp()
            enemy.showHp()
            print("")
            if not player.agl > enemy.agl:
                player.attack(enemy)
                print("You attacked the enemy for:")
                time.sleep(2)
        else:
            enemy.hp = 0
            player.showHp()
            enemy.showHp()
            print("")

            tempHp = player.hp

            player.hp = 0 
            print("YOU HAVE WON!")
            dropXp = randint(15, 30)

            print("You've got", dropXp, "xp")
            player.xp += dropXp

            print(tempHp)

            print("You will return in...")
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
                        
            return tempHp 
