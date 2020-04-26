from iclasses import *



item1 = Potion("Small potion", "item1", "A small potion which heals 50hp", 20, 50, 100, [])
item2 = Potion("Medium potion", "item2", "A slightly bigger potion than small potion, heals 80hp", 50, 80, 50, [])
item3 = Potion("Big potion", "item3", "A potion which PROS use, heals 200hp", 90, 200, 1, [])

item4 = Weapon("Newbie sword", "item4", "The first sword you can have as a warrior str + 5", 45, 0, 0, 5, 0, 50, [])
item5 = Weapon("Newbie bow", "item5", "The first bow you can even use str + 2 agl + 3", 45, 0, 0, 2, 3, 50, [])
item6 = Weapon("Newbie staff", "item6", "The first staff you can equip as a mage hp + 10 str + 3", 45, 10, 0, 3, 0, 50, [])

item7 = Item("Ogre scrap", "item7", "A scrap of ogres chestplate, can be used for crafting items", 5, [])
item8 = Item("Stick", "item8", "Just a stick", 5, [])



item10 = Bag("Loot bag", "item10", "Gives you items", 60, [item1, item2], [])
item11 = Bag("Loot bag", "item10", "Gives you items", 20, [item1, item2], [])
item12 = Bag("Loot bag", "item10", "Gives you items", 20, [item1, item2], [])
item13 = Bag("Loot bag", "item10", "Gives you items", 20, [item1, item2], [])
item14 = Bag("Loot bag", "item10", "Gives you items", 20, [item1, item2], [])
item15 = Bag("Loot bag", "item10", "Gives you items", 20, [item1, item2], [])
item16 = Bag("Loot bag", "item10", "Gives you items", 20, [item1, item2], [])



item20 = Helmet("Basic Helmet", "item20", "You need to protect your head!", 25, 10, 0, 2, 2, 30, [item7, item7, item7, item8])
item21 = Chestplate("Basic Chestplate", "item21", "Not so bad not so good", 50, 40, 0, 10, 5, 10, [])
item22 = Leggings("Basic Leggings", "item22", "If you dont want to run around naked", 35, 30, 0, 3, 5, 20, [])

