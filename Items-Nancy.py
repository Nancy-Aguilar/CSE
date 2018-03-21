class Item(object):
    def __init__(self, name, description, durability):
        self.name = name
        self.description = description
        self.durability = durability


class Weapon(Item):
    def __init__(self, name):
        super(Weapon, self).__init__()
        self.name = name


class Sword(Weapon):
    def __init__(self, name):
        super(Sword, self).__init__()
        self.name = name


class Bow_Arrow(Weapon):
    def __init__(self, name):
        super(Bow_Arrow, self).__init__()
        self.name = name