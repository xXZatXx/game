import time

from classes import *
import enemies


def battle(player, enemy):
    print("BATTLE STARTED!")

    print("Your enemy is:", enemy.name)

    while player.hp > 0:

        player.attack(enemy)
        print("You attacked the enemy for:", player.str)
        time.sleep(2)

        if enemy.hp >= 0:
            enemy.attack(player)
            print("Enemy attacked you for:", enemy.str)
            time.sleep(2)

            player.showHp()
            enemy.showHp()
        else:
            enemy.hp = 0
            player.showHp()
            enemy.showHp()
            player.hp = 0 
            print("YOU HAVE WON!")

        
