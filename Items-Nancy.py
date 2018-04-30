class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def collect(self):
        print("You collected %s" % self.name)


class Weapon(Item):
    def __init__(self, name, description):
        super(Weapon, self).__init__(name, description)

    def collect(self):
        print("You collected a %s" % self.name)


class Sword(Weapon):
    def __init__(self, name, description, power):
        super(Sword, self).__init__(name, description)
        self.power = power

    def attack(self):
        print("You attacked with %s" % self.name)


class BowArrow(Weapon):
    def __init__(self, name, description, power):
        super(BowArrow, self).__init__(name, description)
        self.power = power

    def shoot(self):
        print("You shot an arrow with %s" % self.name)


class Keys(Item):
    def __init__(self, name, description):
        super(Keys, self).__init__(name, description)

    def collect(self):
        print("You collected %s key" % self.name)


class CrystalHeart(Keys):
    def __init__(self, name, description, room):
        super(CrystalHeart, self).__init__(name, description)
        self.room = room

    def insert(self):
        print("You insert the %s" % self.name)


class Blackkey(Keys):
    def __init__(self, name, description, room):
        super(Blackkey, self).__init__(name, description,)
        self.room = room

    def insert(self):
        print("You insert the %s" % self.name)


class Dormkey(Keys):
    def __init__(self, name, description, room):
        super(Dormkey, self).__init__(name, description)
        self.room = room

    def insert(self):
        print("You insert the %s" % self.name)


class Materials(Item):
    def __init__(self, name, description):
        super(Materials, self).__init__(name, description)

    def collect(self):
        print(" You collected %s" % self.name)


class Carbon(Materials):
    def __init__(self, name, description):
        super(Carbon, self).__init__(name, description)

    def pressure(self):
        print("You put pressure on the %s and it turned into a diamond" % self.name)


class Consumables(Item):
    def __init__(self, name, description):
        super(Consumables, self).__init__(name, description)

    def collect(self):
        print("You collected %s" % self.name)


class Food(Consumables):
    def __init__(self, name, description):
        super(Food, self).__init__(name, description)

    def eat(self):
        print("You eat the %s" % self.name)


class Medkit(Consumables):
    def __init__(self, name, description):
        super(Medkit, self).__init__(name, description)

    def use(self):
        print("You use the %s" % self.name)


class Tools(Item):
    def __init__(self, name, description):
        super(Tools, self).__init__(name, description)

    def collect(self):
        print("You collected %s" % self.name)


class Flashlight(Tools):
    def __init__(self, name, description):
        super(Flashlight, self).__init__(name, description)

    def turn_on(self):
        print("You turn on %s" % self.name)


class Cloths(Item):
    def __init__(self, name, description):
        super(Cloths, self).__init__(name, description)

    def collect(self):
        print("You collected %s" % self.name)


class Pants(Cloths):
    def __init__(self, name, description):
        super(Pants, self).__init__(name, description)

    def put_on(self):
        print("You put on %s" % self.name)


class Sweater(Cloths):
    def __init__(self, name, description):
        super(Sweater, self).__init__(name, description)

    def put_on(self):
        print("You put on %s" % self.name)