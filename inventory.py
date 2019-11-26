

class Item(object):
    def values(self, name, weight):
        self.name = name
        self.weight = weight

class Inventory(object):
    def itemList(self):
        self.list = {}

    def itemPickup(self, item):
        self.items[item.name] = item
