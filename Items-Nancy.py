class Item(object):
    def __init__(self, name, durability):
        self.name = name
        self.durability = durability

class Weapon(Item):
    def __init__(self, name):