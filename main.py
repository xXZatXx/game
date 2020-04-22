class Player:
    def __init__(self, name, health, mana, strength, agility):
        self.name = name
        self.hp = health
        self.mn = mana
        self.str = strength
        self.agl = agility

    def stats(self):
        print("[ Name: ", self.name, "]")
        print("| HP", self.hp, "MN", self.mn, "STR", self.str, "AGL", self.agl, "|")

player = Player("Player1", 100, 50, 10, 10)

player.stats()
