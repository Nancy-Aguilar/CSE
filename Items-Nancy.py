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


class BowArrow(Weapon):
    def __init__(self, name):
        super(BowArrow, self).__init__()
        self.name = name


class Keys(Item):
    def __init__(self, name):
        super(Keys, self).__init__()
        self.name = name


class CrystalHeart(Keys):
    def __init__(self, name):
        super(CrystalHeart, self).__init__()
        self.name = name


class Blackkey(Keys):
    def __init__(self, name):
        super(Blackkey, self).__init__()
        self.name = name


class Materials(Item):
    def __init__(self, name):
        super(Materials, self).__init__()
        self.name = name


class Carbon(Materials):
    def __init__(self, name):
        super(Carbon, self).__init__()
        self.name = name


class Bookofspells(Materials):
    def __init__(self, name):
        super(Bookofspells, self).__init__()
        self.name = name


class Potions(Materials):
    def __init__(self, name):
        super(Potions, self).__init__()
        self.name = name


class Consumables(Item):
    def __init__(self, name):
        super(Consumables, self).__init__()
        self.name = name


class Food(Consumables):
    def __init__(self, name):
        super(Food, self).__init__()
        self.name = name


class Medkit(Consumables):
    def __init__(self, name):
        super(Medkit, self).__init__()
        self.name = name


class Tools(Item):
    def __init__(self, name):
        super(Tools, self).__init__()
        self.name = name


class Flashlight(Tools):
    def __init__(self, name):
        super(Flashlight, self).__init__()
        self.name = name