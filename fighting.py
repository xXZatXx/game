import time
from random import randint

from classes import *

def battle(player, enemy):
    global tempHp
    print("==| BATTLE STARTED! |==")

    print("Your enemy is:", enemy.name)
    enemy.stats()

    while player.hp > 0:
        if player.hp <= 0:
            rand = randint(1, 30)
            print("You D I E D :c")
            print("You dropped", rand, "$")

            if player.money >= rand:
                player.money -= rand
            elif player.money < rand:
                player.money = 0

            player.battles += 1

            break

        if player.agl > enemy.agl and enemy.hp >= 0:
            dmg = player.attack(enemy)
            print("You attacked the enemy for:", dmg)
            time.sleep(2)
        
        if enemy.hp >= 0:
            dmg = enemy.attack(player)
            print("Enemy attacked you for:", dmg)
            time.sleep(2)

            player.showHp()
            enemy.showHp()
            print("")
            if not player.agl > enemy.agl:
                dmg = player.attack(enemy)
                print("You attacked the enemy for:", dmg)
                time.sleep(2)
        else:
            enemy.hp = 0
            player.showHp()
            enemy.showHp()
            print("")

            tempHp = player.hp

            player.hp = 0 
            print("YOU HAVE WON!")
            dropXp = randint(15, 30) + int(round(player.lvlXp/25, 0))

            print("You've got", dropXp, "xp")
            player.xp += dropXp

            enemy.dropItems(player)
            rand = randint(1, 10)

            player.money += (enemy.moneyDrop + rand)
            print(enemy.moneyDrop + rand, "$") 

            tempInp = input("Press Enter to return")

            print("You will return in...")
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)

            player.battles += 1            
            return tempHp 
