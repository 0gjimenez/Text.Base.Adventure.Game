def craft(alist,x,y):
    indexx = alist.index(x)
    indexy = alist.index(y)
    del alist[indexx]
    del alist[indexy]

def craft_sword(alist):
    craft(alist, wood, stone)
    alist.append(sword)

def craft_shield(alist):
    craft(alist, wood, stone)
    alist.append(shield)

def craft_bandage(alist):
    craft(alist, string, leaves)
    alist.append(bandage)
