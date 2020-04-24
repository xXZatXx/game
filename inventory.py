class Item():
    def __init__(self, name, varName, description):
        self.name = name
        self.desc = description
        self.varN = varName

    def showDescription(self):
        print("[ Item Name:", self.name, "]")
        print(self.desc)

class Potion(Item):
    def __init__(self, name, varName, description, hpAmount):
        self.hpAmount = hpAmount
        super().__init__(name, varName, description)

    def heal(self, player):
        
        print(player.name, "has been healed")
        player.hp = player.hp + self.hpAmount

        if player.hp > player.maxHp:
            player.hp = player.maxHp

class Weapon(Item):
    def __init__(self, name, varName, description, health, mana, strength, agility):
        self.hp = health
        self.mn = mana
        self.str = strength
        self.agl = agility 
        self.varN = varName
        super().__init__(name, varName, description)

        


item1 = Potion("Small potion", "item1", "A small potion which heals 50hp", 50)
item2 = Potion("Medium potion", "item2", "A slightly bigger potion than small potion, heals 80hp", 80)
item3 = Potion("Big potion", "item3", "A potion which PROS use, heals 200hp", 200)

item4 = Weapon("Newbie sword", "item4", "The first sword you can have as a warrior str + 5", 0, 0, 5, 0)
item5 = Weapon("Newbie bow", "item5", "The first bow you can even use str + 2 agl + 3", 0, 0, 2, 3)
item6 = Weapon("Newbie staff", "item6", "The first staff you can equip as a mage hp + 10 str + 3", 10, 0, 3, 0)

item7 = Item("Ogre scrap", "item7", "A scrap of ogres chestplate, can be used for crafting items")