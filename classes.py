from inventory import *

class Player:
    def __init__(self, name, pClass, health, mana, strength, agility):
        self.name = name
        self.pClass = pClass
        self.hp = health
        self.maxHp = health 
        self.mn = mana
        self.str = strength
        self.agl = agility
        self.items = []
        self.on = []

        self.round = 1

        self.lvl = 1
        self.xp = 0
        self.lvlXp = 200

        if pClass == 0:
            self.pClass = "Warrior"
            self.giveItem(item4)

        elif pClass == 1:
            self.pClass = "Archer"

        elif pClass == 2:
            self.pClass = "Mage"
        
        else: 
            print("Wrong Class")


    def equip(self, item):
        self.on.append(item)
        for i in range(len(self.on)):
            self.hp += self.on[i].hp 
            self.mn += self.on[i].mn 
            self.str += self.on[i].str
            self.agl += self.on[i].agl

        self.items.remove(item)

    def removeItem(self, item):
        self.items.remove(item)

    def giveItem(self, item):
        self.items.append(item)

    def showEquiped(self):
        print("[ Equiped ]")
        for i in range(len(self.on)):
            print(self.on[i].name, "HP", self.on[i].hp, "MN", self.on[i].mn, "STR",self.on[i].str, "AGL",self.on[i].agl)

    def showInv(self):
        for i in range(len(self.items)):
            print(i, "|", self.items[i].name)

    def stats(self):
        print("[", self.lvl, "]", "[ Player Name:", self.name, "]", "[ Class:", self.pClass, "]")
        print("| HP", self.hp, "/", self.maxHp, "MN", self.mn, "STR", self.str, "AGL", self.agl, "|")
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

        other.hp -= self.str

        self.round += 1

    def lvlup(self):
        self.lvl += 1
        self.maxHp += 30
        self.str += 8
        self.mn += 6
        self.agl += 5
        self.xp -= self.lvlXp
        self.lvlXp += 100 + int(round(self.hp/2, 0))

class Enemy:
    def __init__(self, name, health, mana, strength, agility):
        self.name = name
        self.hp = health
        self.maxHp = health
        self.mn = mana
        self.str = strength
        self.agl = agility

    def stats(self):
        print("[ Enemy Name:", self.name, "]")
        print("| HP", self.hp, "/", self.maxHp, "MN", self.mn, "STR", self.str, "AGL", self.agl, "|")

    def showHp(self):
        print("[ Enemy HP:", self.hp, "/", self.maxHp, "]")

    def attack(self, other):
        other.hp -= self.str
        
