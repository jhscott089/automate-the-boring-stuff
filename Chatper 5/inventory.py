import pprint
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12, 'hooks': 24, 'wood':50, 'fish':6, 'fishing poles':1, 'shields':1}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v,k)
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)