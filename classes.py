class Player:
    def __init__(self, name, pClass):
        self.name = name
        self.pClass = pClass
        self.xp = 0
        self.round = 1

        if pClass == 0:
            self.hp = 100
            self.mn = 50
            self.str = 20
            self.agl = 10

            self.pClass = "Warrior"

        elif pClass == 1:
            self.hp = 80
            self.mn = 50
            self.str = 10
            self.agl = 20

            self.pClass = "Archer"

        elif pClass == 2:
            self.hp = 80
            self.mn = 100
            self.str = 5
            self.agl = 10
        
            self.pClass = "Mage"
        
        else: 
            print("Wrong Class")

    def stats(self):
        print("[ Player Name:", self.name, "]", "[ Class:", self.pClass, "]")
        print("| HP", self.hp, "MN", self.mn, "STR", self.str, "AGL", self.agl, "|")

    def showHp(self):
        print("[ Player HP:", self.hp ,"]")

    def attack(self, other):
        print("Round:", self.round)

        other.hp -= self.str

        self.round += 1
         

class Enemy:
    def __init__(self, name, health, mana, strength, agility):
        self.name = name
        self.hp = health
        self.mn = mana
        self.str = strength
        self.agl = agility

    def stats(self):
        print("[ Enemy Name:", self.name, "]")
        print("| HP", self.hp, "MN", self.mn, "STR", self.str, "AGL", self.agl, "|")

    def showHp(self):
        print("[ Enemy HP:", self.hp ,"]")

    def attack(self, other):
        other.hp -= self.str
        
