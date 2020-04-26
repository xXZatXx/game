import random
from random import randint

class Item():
    def __init__(self, name, varName, description, price):
        self.name = name
        self.desc = description
        self.varN = varName
        self.price = price

    def showDescription(self):
        print("[ Item Name:", self.name, "]")
        print(self.desc)

class Potion(Item):
    def __init__(self, name, varName, description, price, hpAmount, chance):
        self.hpAmount = hpAmount
        self.chance = chance
        self.price = price
        super().__init__(name, varName, description, price)

    def heal(self, player):
        print(player.name, "has been healed")
        player.hp = player.hp + self.hpAmount

        if player.hp >= player.maxHp:
            player.hp = player.maxHp

class Weapon(Item):
    def __init__(self, name, varName, description, price, health, mana, strength, agility, chance):
        self.hp = health
        self.mp = mana
        self.str = strength
        self.agl = agility 
        self.varN = varName
        self.chance = chance
        self.price = price
        super().__init__(name, varName, description, price)

class Bag(Item):
    def __init__(self, name, varName, description, price, loot):
        self.loot = loot
        self.varN = varName
        self.price = price
        super().__init__(name, varName, description, price)

    def giveLoot(self, player):
        
        print("You have got: ")
        rand = randint(1, 100)
        
        for i in range(len(self.loot)):
            if self.loot[i].chance <= rand or self.loot[i].chance == 100:
                print(self.loot[i].name)
                player.giveItem(self.loot[i])

class Helmet(Item):
    def __init__(self, name, varName, description, price, health, mana, strength, agility, chance):
        self.hp = health
        self.mp = mana
        self.str = strength
        self.agl = agility 
        self.varN = varName
        self.chance = chance
        self.price = price
        super().__init__(name, varName, description, price)

class Chestplate(Item):
    def __init__(self, name, varName, description, price, health, mana, strength, agility, chance):
        self.hp = health
        self.mp = mana
        self.str = strength
        self.agl = agility 
        self.varN = varName
        self.chance = chance
        self.price = price
        super().__init__(name, varName, description, price)

class Leggings(Item):
    def __init__(self, name, varName, description, price, health, mana, strength, agility, chance):
        self.hp = health
        self.mp = mana
        self.str = strength
        self.agl = agility 
        self.varN = varName
        self.chance = chance
        self.price = price
        super().__init__(name, varName, description, price)

class Boots(Item):
    def __init__(self, name, varName, description, price, health, mana, strength, agility, chance):
        self.hp = health
        self.mp = mana
        self.str = strength
        self.agl = agility 
        self.varN = varName
        self.chance = chance
        self.price = price
        super().__init__(name, varName, description, price)


