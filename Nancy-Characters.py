class Character(object):
    def __init__(self, name, description, health, attack, damage, interact):
        self.name = name
        self.description = description
        self.health = health
        self.inventory = []
        self.attack = attack
        self.damage = damage
        self.interact = interact
        self.power = 0
        self.health = 100

    def collect(self, item):
        self.inventory.append(item)
        print("You collected %s" % self.name)

    def remove(self, item):
        self.inventory.remove(item)
        print("You removed %s from inventory" % self.name)

    def attack(self):
        print("You attacked with %d power" % self.power)


class Player(Character):
    def __init__(self, name, description, health, attack, damage, interact):
        super(Player, self).__init__(name, description, health, attack, damage, interact)

    def eat(self):
        print("You eat %s" % self.name)

    def read(self):
        print("You read %s" % self.name)


class Principal(Character):
    def __init__(self, name, description, health, attack, damage, interact):
        super(Principal, self).__init__(name, description, health, attack, damage, interact)


class Monster1(Character):
    def __init__(self, name, description, health, attack, damage, interact):
        super(Monster1, self).__init__(name, description, health, attack, damage, interact)

    def growl(self):
        print("%s growls" % self.name)


class Monster2(Character):
    def __init__(self, name, description, health, attack, damage, interact):
        super(Monster2, self).__init__(name, description, health, attack, damage, interact)

    def growl(self):
        print("%s growls" % self.name)


class Monster3(Character):
    def __init__(self, name, description, health, attack, damage, interact):
        super(Monster3, self).__init__(name, description, health, attack, damage, interact)

    def growl(self):
        print("%s growls" % self.name)


class Monster4(Character):
    def __init__(self, name, description, health, attack, damage, interact):
        super(Monster4, self).__init__(name, description, health, attack, damage, interact)

    def growl(self):
        print("%s growls" % self.name)


class Monster5(Character):
    def __init__(self, name, description, health, attack, damage, interact):
        super(Monster5, self).__init__(name, description, health, attack, damage, interact)

    def growl(self):
        print("%s growls" % self.name)


class Monster6(Character):
    def __init__(self, name, description, health, attack, damage, interact):
        super(Monster6, self).__init__(name, description, health, attack, damage, interact)

    def growl(self):
        print("%s growls" % self.name)


class Monster7(Character):
    def __init__(self, name, description, health, attack, damage, interact):
        super(Monster7, self).__init__(name, description, health, attack, damage, interact)

    def growl(self):
        print("%s growls" % self.name)


class Monster8(Character):
    def __init__(self, name, description, health, attack, damage, interact):
        super(Monster8, self).__init__(name, description, health, attack, damage, interact)

    def growl(self):
        print("%s growls" % self.name)
