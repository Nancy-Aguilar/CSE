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

    def remove(self, item):
        self.inventory.remove(item)
        print("You removed %s from inventory" % self.name)


class Player(Character):
    def __init__(self, name, description, health, attack, damage, interact):
        super(Player, self).__init__(name, description, health, attack, damage, interact)

    def eat(self):
        print("You eat %s" % self.name)

    def read(self):
        print("You read %s" % self.name)


class Monster(Character):
    def __init__(self, name, description, health, attack, damage, interact):
        super(Monster, self).__init__(name, description, health, attack, damage, interact)

    def growl(self):
        print("%s growls" % self.name)