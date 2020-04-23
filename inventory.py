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

item1 = Potion("Small potion", "A small potion which heals 50hp", 50)