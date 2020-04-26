from iclasses import *
from items import *
import os 
from random import randint
import random
import time

clear = lambda: os.system('cls')

class Player:
    def __init__(self, name, pClass, health, mana, strength, agility):
        self.name = name
        self.pClass = pClass
        self.hp = health
        self.maxHp = health 
        self.mp = mana
        self.str = strength
        self.agl = agility
        self.money = 0
        self.battles = 0
        self.bagLimit = 10
        self.saveSlot = 0
        self.items = []
        self.on = []

        self.round = 1

        self.lvl = 1
        self.xp = 0
        self.lvlXp = 200

        if pClass == 0:
            self.pClass = "Warrior"

        elif pClass == 1:
            self.pClass = "Archer"

        elif pClass == 2:
            self.pClass = "Mage"
        
        else: 
            print("Wrong Class")

    def craft(self, item):
        data = list(dict.fromkeys(item.recipe))
        checking = []

        for i in range(len(data)):
            if self.items.count(data[i]) >= item.recipe.count(data[i]):
                checking.append(True)
            else:
                checking.append(False)

        if all(checking):
            print("Crafting", item.name)
            for j in range(len(item.recipe)):
                self.removeItem(item.recipe[j])

            self.giveItem(globals()[item.varN])
            time.sleep(2)
        else:
            missing = checking.index(False)

            print("You can't craft it!", "You need more", data[missing].name)

        time.sleep(2)

    def drop(self, item):
        self.items.remove(item)

    def unEquip(self, item):
        self.on.remove(item)
        self.hp -= item.hp 
        self.mp -= item.mp
        self.str -= item.str
        self.agl -= item.agl

        self.giveItem(item)

    def equip(self, item):
        self.on.append(item)
        for i in range(len(self.on)):
            self.hp += self.on[i].hp 
            self.mp += self.on[i].mp
            self.str += self.on[i].str
            self.agl += self.on[i].agl

        self.items.remove(item)

    def removeItem(self, item):
        
        if item in self.items:
            self.items.remove(item)


    def giveItem(self, item):
        self.items.append(item)

    def showEquiped(self):
        print("[ Equiped ]")
        for i in range(len(self.on)):
            print(i+1, "|", self.on[i].name, "HP", self.on[i].hp, "MP", self.on[i].mp, "STR",self.on[i].str, "AGL",self.on[i].agl)

    def showInv(self):
        self.data = []
        self.names = []

        for i in range(len(self.items)):
            num = self.items.count(self.items[i])
            if self.items[i] in self.names:
                pass
            else:
                self.data.append(self.items[i])
                self.names.append(self.items[i])
                self.names.append(num)
        
        allNames = []

        for i in range(len(self.data)):
            allNames.append(self.data[i].name)
        longestName = max(allNames, key=len)
        length = len(longestName) + 1
        
        for i in range(self.bagLimit):
            if i <= 8:
                yeet = " |"
            else:
                yeet = "|"

            try:
                nameLength = len(self.names[i*2].name) + 1
                spaces = length - nameLength 

                full = self.names[i*2].name + " " + (spaces*" ") + str(self.names[(i*2)+1])

                print(i+1, yeet, full)
            except:
                print(i+1, yeet)

        



    def stats(self):
        clear()
        print("[", self.lvl, "]", "[ Name:", self.name, "]", "[ Class:", self.pClass, "]")
        print("| HP", self.hp, "/", self.maxHp, "MP", self.mp, "STR", self.str, "AGL", self.agl, "|", "Money:", self.money, "$", "|")
        self.xpBar()
        print("")

    def xpBar(self):
        #self.lvl = 1
        #self.xp = 0
        #self.lvlXp = 200
        lineN = 0
        print("Experience:")
        prs = ["["," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "]"]
        x = self.lvlXp * 10
        x = x / 100 

        if self.xp > 0:
            lineN = self.xp/x
            lineN = round(lineN, 0)
            
        for i in range(int(lineN)):
            prs[i+1] = u"\u25AE"

        print(self.xp, str(prs[0]) + str(prs[1]) + str(prs[2]) + str(prs[3]) + str(prs[4]) + str(prs[5]) + str(prs[6]) + str(prs[7]) + str(prs[8]) + str(prs[9]) + str(prs[10]) + str(prs[11]), self.lvlXp)


    def showHp(self):
        print("[ Player HP:", self.hp, "/", self.maxHp ,"]")

    def attack(self, other):
        
        print("| Round:", self.round, "|")
        self.round += 1
        rand = randint(1, 100)

        if rand <= 40:
            dealedDmg = self.str + int(round(self.str/2, 0))
            print("CRITICAL HIT!")
            other.hp -= dealedDmg

            return dealedDmg
        else:
            other.hp -= self.str
            return self.str

        

    def lvlup(self):
        self.lvl += 1
        self.maxHp += 30
        self.str += 8
        self.mp += 6
        self.agl += 5
        self.xp -= self.lvlXp
        self.lvlXp += 100 + int(round(self.hp/2, 0))





class Enemy:
    def __init__(self, name, drop, health, mana, strength, agility, money):
        self.name = name
        self.hp = health
        self.maxHp = health
        self.mp = mana
        self.str = strength
        self.agl = agility
        self.drop = drop
        self.moneyDrop = money

    def stats(self):
        print("[ Enemy Name:", self.name, "]")
        print("| HP", self.hp, "/", self.maxHp, "MP", self.mp, "STR", self.str, "AGL", self.agl, "|")

    def showHp(self):
        print("[ Enemy HP:", self.hp, "/", self.maxHp, "]")

    def attack(self, other):
        other.hp -= self.str
        return self.str

    def dropItems(self, player):
        rand = randint(0, 9)

        print("[ Loot ]")
        if rand > 4:
            loot = random.choice(self.drop)
            print(loot.name)
            player.giveItem(loot)
        
class Boss(Enemy):
    def __init__(self, name, drop, health, mana, strength, agility, money, experience):
        self.exp = experience
        super().__init__(name, drop, health, mana, strength, agility, money)
