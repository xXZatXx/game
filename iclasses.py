import random
from random import randint

class Item():
    def __init__(self, name, varName, description, price, chance, recipe):
        self.name = name
        self.desc = description
        self.varN = varName
        self.price = price
        self.chance = chance
        self.recipe = recipe 

    def showDescription(self):
        print("[ Item Name:", self.name, "]")
        print(self.desc)

class Potion(Item):
    def __init__(self, name, varName, description, price, hpAmount, chance, recipe):
        self.hpAmount = hpAmount
        super().__init__(name, varName, description, price, chance, recipe)

    def heal(self, player):
        print(player.name, "has been healed")
        player.hp = player.hp + self.hpAmount

        if player.hp >= player.maxHp:
            player.hp = player.maxHp

class Weapon(Item):
    def __init__(self, name, varName, description, price, health, mana, strength, agility, chance, recipe):
        self.hp = health
        self.mp = mana
        self.str = strength
        self.agl = agility 

        super().__init__(name, varName, description, price, chance, recipe)

class Tool(Item):
    def __init__(self, name, varName, description, price, health, mana, strength, agility, chance, recipe):
        self.hp = health
        self.mp = mana
        self.str = strength
        self.agl = agility 

        super().__init__(name, varName, description, price, chance, recipe)

class Bag(Item):
    def __init__(self, name, varName, description, price, loot, chance, recipe):
        self.loot = loot

        super().__init__(name, varName, description, price, chance, recipe)

    def giveLoot(self, player):
        
        print("You have got: ")
        rand = randint(1, 100)
        
        for i in range(len(self.loot)):
            if self.loot[i].chance <= rand or self.loot[i].chance == 100:
                print(self.loot[i].name)
                player.giveItem(self.loot[i])

class Helmet(Item):
    def __init__(self, name, varName, description, price, health, mana, strength, agility, chance, recipe):
        self.hp = health
        self.mp = mana
        self.str = strength
        self.agl = agility 
        super().__init__(name, varName, description, price, chance, recipe)

class Chestplate(Item):
    def __init__(self, name, varName, description, price, health, mana, strength, agility, chance, recipe):
        self.hp = health
        self.mp = mana
        self.str = strength
        self.agl = agility 
        super().__init__(name, varName, description, price, chance, recipe)

class Leggings(Item):
    def __init__(self, name, varName, description, price, health, mana, strength, agility, chance, recipe):
        self.hp = health
        self.mp = mana
        self.str = strength
        self.agl = agility 
        super().__init__(name, varName, description, price, chance, recipe)

class Boots(Item):
    def __init__(self, name, varName, description, price, health, mana, strength, agility, chance, recipe):
        self.hp = health
        self.mp = mana
        self.str = strength
        self.agl = agility 
        super().__init__(name, varName, description, price, chance, recipe)

class CraftingScroll(Item):
    def __init__(self, name, varName, description, price, chance, item, recipe):
        self.itemC = item
        super().__init__(name, varName, description, price, chance, recipe)

        
    
