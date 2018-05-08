class Character(object):
    def __init__(self, name, description, health, attack, damage, interact):
        self.name = name
        self.description = description
        self.health = health
        self.inventory = []
        self.attack = attack
        self.damage = damage
        self.interact = interact

    def collect(self, item):
        self.inventory.append(item)
        print("You collected %s" % self.name)

    def attack(self):



class Player(Character):
    def __init__(self, name, description, health, attack, damage, interact):
        super(Player, self).__init__(name, description, health, attack, damage, interact)

    def eat(self):
        print("You eat %s" % self.name)

    def collect(self, item):
        print("You collect %s" % self.name)

    def drop(self):
        print("You drop %s" % self.name)

    def create(self):
        print("You create %s" % self.name)

    def read(self):
        print("You read %s" % self.name)

    def open(self):
        print("You open %s" % self.name)

    def close(self):
        print("You close %s" % self.name)

    def put_on(self):
        print("You put on %s" % self.name)


class Monster(Character):
    def __init__(self, name, description, health, attack, damage, interact):
        super(Monster, self).__init__(name, description, health, attack, damage, interact)