class Item(object):
    def __init__(self, name, description, durability):
        self.name = name
        self.description = description
        self.durability = durability


class Weapon(Item):
    def __init__(self, name, description, durability):
        super(Weapon, self).__init__(name, description, durability)

    def collect(self):
        print("You collected a %s" % self.name)


class Sword(Weapon):
    def __init__(self, name, description, durability):
        super(Sword, self).__init__(name, description, durability)

    def attack(self):
        print("You attacked")


class BowArrow(Weapon):
    def __init__(self, name, description, durability):
        super(BowArrow, self).__init__(name, description, durability)

    def attack(self):
        print("You attacked")


class Keys(Item):
    def __init__(self, name, description, durability):
        super(Keys, self).__init__(name, description, durability)

    def collect(self):
        print("You collected %s key" % self.name)


class CrystalHeart(Keys):
    def __init__(self, name, description, durability):
        super(CrystalHeart, self).__init__(name, description, durability)

    def insert_key(self):
        print("You put the key in")


class Blackkey(Keys):
    def __init__(self, name, description, durability):
        super(Blackkey, self).__init__(name, description, durability)

    def insert_key(self):
        print("You put the key in")


class Dromkey(Keys):
    def __init__(self, name, description, durability):
        super(Dromkey, self).__init__(name, description, durability)

    def insert_key(self):
        print("You put the key in")


class Materials(Item):
    def __init__(self, name, description, durability):
        super(Materials, self).__init__(name, description, durability)

    def collect(self):
        print(" You collected %s" % self.name)


class Carbon(Materials):
    def __init__(self, name, description, durability):
        super(Carbon, self).__init__(name, description, durability)

    def put_pressure(self):
        print("You put pressure on the carbon and it turned into a diamond")


class Bookofspells(Materials):
    def __init__(self, name, description, durability):
        super(Bookofspells, self).__init__(name, description, durability)

    def spells_page(self):
        print("You are on the spells page")


class Potions(Materials):
    def __init__(self, name, description, durability):
        super(Potions, self).__init__(name, description, durability)

    def pour_in_beaker(self):
        print("You poured in the potion into the beaker")


class Consumables(Item):
    def __init__(self, name, description, durability):
        super(Consumables, self).__init__(name, description, durability)

    def collect(self):
        print("You collected %s" % self.name)


class Food(Consumables):
    def __init__(self, name, description, durability):
        super(Food, self).__init__(name, description, durability)

    def eat(self):
        print("You eat the food")


class Medkit(Consumables):
    def __init__(self, name, description, durability):
        super(Medkit, self).__init__(name, description, durability)

    def use(self):
        print("You use the Medkit")


class Tools(Item):
    def __init__(self, name, description, durability):
        super(Tools, self).__init__(name, description, durability)

    def collect(self):
        print("You collected %s" % self.name)


class Flashlight(Tools):
    def __init__(self, name, description, durability):
        super(Flashlight, self).__init__(name, description, durability)

    def turn_on(self):
        print("You turn on the flashlight")


class Cloths(Item):
    def __init__(self, name, description, durability):
        super(Cloths, self).__init__(name, description, durability)

    def collect(self):
        print("You collected %s" % self.name)


class Pants(Cloths):
    def __init__(self, name, description, durability):
        super(Pants, self).__init__(name, description, durability)

    def put_on(self):
        print("You put on the pants")


class Sweater(Cloths):
    def __init__(self, name, description, durability):
        super(Sweater, self).__init__(name, description, durability)

    def put_on(self):
        print("You put on the sweater")