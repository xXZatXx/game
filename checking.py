import numpy as np

item1 = "yes"
item2 = "yess"
item3 = "yesss"

inventory = [item1, item2, item2, item2, item3, item3]
crafting = [item1, item2, item2, item2, item1]
data = list(dict.fromkeys(crafting))
checking = []

for i in range(len(data)):
    if inventory.count(data[i]) >= crafting.count(data[i]):
        checking.append(True)
    else:
        checking.append(False)

if all(checking):
    print("Can craft")
else:
    print("Cant craft")

print(checking)