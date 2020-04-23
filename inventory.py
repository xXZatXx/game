class Item():
    def __init__(self, name, description):
        self.name = name
        self.desc = description

    def showDescription(self):
        print("[ Item Name:", self.name, "]")
        print(self.desc)

class Potion(Item):
    def __init__(self, name, description, hpAmount):
        self.hpAmount = hpAmount
        super().__init__(name, description)

    def heal(self, player):
        
        print(player.name, "has been healed")
        player.hp = player.hp + self.hpAmount

        if player.hp > player.maxHp:
            player.hp = player.maxHp

class Weapon(Item):
    def __init__(self, name, description, health, mana, strength, agility):
        self.hp = health
        self.mn = mana
        self.str = strength
        self.agl = agility 
        super().__init__(name, description)

        

item1 = Potion("Small potion", "A small potion which heals 50hp", 50)
item2 = Potion("Medium potion", "A slightly bigger potion than small potion, heals 80hp", 80)
item3 = Potion("Big potion", "A potion which PROS use, heals 200hp", 200)

item4 = Weapon("Newbie sword", "The first sword you can have as a warrior str + 5", 0, 0, 5, 0)