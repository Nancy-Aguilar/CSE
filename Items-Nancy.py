class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def collect(self):
        print("You collected %s" % self.name)

    def drop(self):
        print("You dropped %s" % self.name)


class Weapon(Item):
    def __init__(self, name, description):
        super(Weapon, self).__init__(name, description)

    def collect(self):
        print("You collected a %s" % self.name)

    def drop(self):
        print("You dropped %s" % self.name)


class Sword(Weapon):
    def __init__(self, name, description, power):
        super(Sword, self).__init__(name, description)
        self.power = power

    def stab(self):
        print("You attacked with %s" % self.name)

    def cut(self):
        print("You cut with the %s" % self.name)


class BowArrow(Weapon):
    def __init__(self, name, description, power):
        super(BowArrow, self).__init__(name, description)
        self.power = power

    def shoot(self):
        print("You shot an arrow with %s" % self.name)


class Axe(Weapon):
    def __init__(self, name, description, power):
        super(Axe, self).__init__(name, description)
        self.power = power

    def swing(self):
        print("You swing the %s" % self.name)


class Keys(Item):
    def __init__(self, name, description):
        super(Keys, self).__init__(name, description)

    def collect(self):
        print("You collected %s key" % self.name)

    def drop(self):
        print("You dropped the %s" % self.name)


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

    def drop(self):
        print("You drop %s" % self.name)


class Apple(Consumables):
    def __init__(self, name, description):
        super(Apple, self).__init__(name, description)

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

    def drop(self):
        print("You drop %s" % self.name)


class Flashlight(Tools):
    def __init__(self, name, description):
        super(Flashlight, self).__init__(name, description)

    def turn_on(self):
        print("You turn on %s" % self.name)

    def turn_off(self):
        print("You turn off the %s" % self.name)


class Cloths(Item):
    def __init__(self, name, description):
        super(Cloths, self).__init__(name, description)

    def collect(self):
        print("You collected %s" % self.name)

    def wear(self):
        print("You wear %s" % self.name)


class Pants(Cloths):
    def __init__(self, name, description):
        super(Pants, self).__init__(name, description)

    def put_on(self):
        print("You put on %s" % self.name)

    def take_off(self):
        print("You take off %s" % self.name)


class Sweater(Cloths):
    def __init__(self, name, description):
        super(Sweater, self).__init__(name, description)

    def put_on(self):
        print("You put on %s" % self.name)

    def take_off(self):
        print("You take off %s" % self.name)


class Book(Item):
    def __init__(self, name, description):
        super(Book, self).__init__(name, description)

    def collect(self):
        print("You collected %s " % self.name)

    def drop(self):
        print("You dropped %s" % self.name)


class Bookofspells(Book):
    def __init__(self, name, description):
        super(Bookofspells, self).__init__(name, description)

    def open(self):
        print("You opened the %s" % self.name)

    def read(self):
        print("The book says %s" % self.description)

    def close(self):
        print("You close the %s" % self.name)


class Letters(Item):
    def __init__(self, name, description):
        super(Letters, self).__init__(name, description)

    def collect(self):
        print("You collected %s" % self.name)

    def drop(self):
        print("You dropped %s" % self.name)


class Sorry(Letters):
    def __init__(self, name, description):
        super(Sorry, self).__init__(name, description)

    def open(self):
        print("You opened the %s" % self.name)

    def read(self):
        print("The letter says %s" % self.description)


class TheTree(Letters):
    def __init__(self, name, description):
        super(TheTree, self).__init__(name, description)

    def open(self):
        print("You open the %s" % self.name)

    def read(self):
        print("The letter says %s" % self.description)


class Creations(Item):
    def __init__(self, name, description):
        super(Creations, self).__init__(name, description)

    def take_out(self):
        print("You took out %s" % self.name)

    def drop(self):
        print("You dropped %s" % self.name)


class Crystalheart(Creations):
    def __init__(self, name, description):
        super(Crystalheart, self).__init__(name, description)

    def place_in(self):
        print("You place the % in the tree statue" % self.name)