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
        print("You attacked")


Sword = Sword('Sōrāsōdo', 'This sword can release sun bolts which can cause quite a lot of damage', '90')
Sword.attack()


class BowArrow(Weapon):
    def __init__(self, name, description, power):
        super(BowArrow, self).__init__(name, description)
        self.power = power

    def shoot(self):
        print("You shot an arrow")


BowArrow = BowArrow('Seimitsuna Shotto', 'This bow and arrow can shoot very precise shots to any target you want', '85')
BowArrow.shoot()


class Keys(Item):
    def __init__(self, name, description):
        super(Keys, self).__init__(name, description)

    def collect(self):
        print("You collected %s key" % self.name)


class CrystalHeart(Keys):
    def __init__(self, name, description, ):
        super(CrystalHeart, self).__init__(name, description,)

    def insert_key(self):
        print("You put the key in")



class Blackkey(Keys):
    def __init__(self, name, description, ):
        super(Blackkey, self).__init__(name, description, )

    def insert_key(self):
        print("You put the key in")


class Dromkey(Keys):
    def __init__(self, name, description, ):
        super(Dromkey, self).__init__(name, description, )

    def insert_key(self):
        print("You put the key in")


class Materials(Item):
    def __init__(self, name, description, ):
        super(Materials, self).__init__(name, description, )

    def collect(self):
        print(" You collected %s" % self.name)


class Carbon(Materials):
    def __init__(self, name, description, ):
        super(Carbon, self).__init__(name, description, )

    def put_pressure(self):
        print("You put pressure on the carbon and it turned into a diamond")


class Bookofspells(Materials):
    def __init__(self, name, description, ):
        super(Bookofspells, self).__init__(name, description, )

    def spells_page(self):
        print("You are on the spells page")


class Potions(Materials):
    def __init__(self, name, description, ):
        super(Potions, self).__init__(name, description, )

    def pour_in_beaker(self):
        print("You poured in the %s into the beaker" % self.name)


class Consumables(Item):
    def __init__(self, name, description, ):
        super(Consumables, self).__init__(name, description, )

    def collect(self):
        print("You collected %s" % self.name)


class Food(Consumables):
    def __init__(self, name, description, ):
        super(Food, self).__init__(name, description, )

    def eat(self):
        print("You eat the %s" % self.name)


class Medkit(Consumables):
    def __init__(self, name, description, ):
        super(Medkit, self).__init__(name, description, )

    def use(self):
        print("You use the %s" % self.name)


class Tools(Item):
    def __init__(self, name, description, ):
        super(Tools, self).__init__(name, description, )

    def collect(self):
        print("You collected %s" % self.name)


class Flashlight(Tools):
    def __init__(self, name, description, ):
        super(Flashlight, self).__init__(name, description, )

    def turn_on(self):
        print("You turn on %s" % self.name)


class Cloths(Item):
    def __init__(self, name, description, ):
        super(Cloths, self).__init__(name, description, )

    def collect(self):
        print("You collected %s" % self.name)


class Pants(Cloths):
    def __init__(self, name, description, ):
        super(Pants, self).__init__(name, description, )

    def put_on(self):
        print("You put on %s" % self.name)


class Sweater(Cloths):
    def __init__(self, name, description, ):
        super(Sweater, self).__init__(name, description, )

    def put_on(self):
        print("You put on %s" % self.name)