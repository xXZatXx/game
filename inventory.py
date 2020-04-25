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
        self.mn = mana
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
                print(self.loot[i])
                player.giveItem(self.loot[i])

class Helmet(Item):
    def __init__(self, name, varName, description, price, health, mana, strength, agility, chance):
        self.hp = health
        self.mn = mana
        self.str = strength
        self.agl = agility 
        self.varN = varName
        self.chance = chance
        self.price = price
        super().__init__(name, varName, description, price)

class Chestplate(Item):
    def __init__(self, name, varName, description, price, health, mana, strength, agility, chance):
        self.hp = health
        self.mn = mana
        self.str = strength
        self.agl = agility 
        self.varN = varName
        self.chance = chance
        self.price = price
        super().__init__(name, varName, description, price)

class Leggings(Item):
    def __init__(self, name, varName, description, price, health, mana, strength, agility, chance):
        self.hp = health
        self.mn = mana
        self.str = strength
        self.agl = agility 
        self.varN = varName
        self.chance = chance
        self.price = price
        super().__init__(name, varName, description, price)

class Boots(Item):
    def __init__(self, name, varName, description, price, health, mana, strength, agility, chance):
        self.hp = health
        self.mn = mana
        self.str = strength
        self.agl = agility 
        self.varN = varName
        self.chance = chance
        self.price = price
        super().__init__(name, varName, description, price)


item1 = Potion("Small potion", "item1", "A small potion which heals 50hp", 20, 50, 100)
item2 = Potion("Medium potion", "item2", "A slightly bigger potion than small potion, heals 80hp", 50, 80, 50)
item3 = Potion("Big potion", "item3", "A potion which PROS use, heals 200hp", 90, 200, 1)

item4 = Weapon("Newbie sword", "item4", "The first sword you can have as a warrior str + 5", 45, 0, 0, 5, 0, 50)
item5 = Weapon("Newbie bow", "item5", "The first bow you can even use str + 2 agl + 3", 45, 0, 0, 2, 3, 50)
item6 = Weapon("Newbie staff", "item6", "The first staff you can equip as a mage hp + 10 str + 3", 45, 10, 0, 3, 0, 50)

item7 = Item("Ogre scrap", "item7", "A scrap of ogres chestplate, can be used for crafting items", 5)



item10 = Bag("Loot bag", "item10", "Gives you items", 60, [item1, item2])
item11 = Bag("Loot bag", "item10", "Gives you items", 20, [item1, item2])
item12 = Bag("Loot bag", "item10", "Gives you items", 20, [item1, item2])
item13 = Bag("Loot bag", "item10", "Gives you items", 20, [item1, item2])
item14 = Bag("Loot bag", "item10", "Gives you items", 20, [item1, item2])
item15 = Bag("Loot bag", "item10", "Gives you items", 20, [item1, item2])
item16 = Bag("Loot bag", "item10", "Gives you items", 20, [item1, item2])



item20 = Helmet("Warriors Helmet", "item20", "The best so far helmet for warriors", 30, 20, 0, 5, 0, 30)