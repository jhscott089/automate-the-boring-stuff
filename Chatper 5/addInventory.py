
def displayInventory(inv):
    print("Inventory:")
    item_total = 0
    for k, v in inv.items():
        print(v,k)
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for loot in addedItems:
        inv.setdefault(loot, 0)
        inv[loot] += 1
    return(inv)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)