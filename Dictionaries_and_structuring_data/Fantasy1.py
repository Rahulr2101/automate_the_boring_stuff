def addToInventory(inventory, addedItems):
    # your code goes here
    for x in range(len(addedItems)):
        if addedItems[x] in inventory:
            inventory[addedItems[x]] += 1
        else:
            inventory[addedItems[x]] = 1
    return inventory



def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v,k)
        item_total += v
        
    print("Total number of items: " + str(item_total))

inventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inventory, dragonLoot)
displayInventory(inv)