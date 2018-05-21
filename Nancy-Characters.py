class Character(object):
    def __init__(self, name, description, health, damage=10):
        self.name = name
        self.description = description
        self.health = health
        self.inventory = []
        self.damage = damage
        self.location = None
        self.health = 100
        self.alive = False

    def collect(self, item):
        self.inventory.append(item)
        print("You collected %s" % self.name)

    def remove(self, item):
        self.inventory.remove(item)
        print("You dropped %s" % item.name)

    def eat(self, item):
        print("%s ate the %s" % (self.name, item.name))

    def health(self):
        print(self.name.damage)
        print("You have health")

    def take_damage(self, amt):
        if self.health <= 0:
            print("%s is already dead" % self.name)
            return
        self.health -= amt
        if self.health <= 0:
            self.alive = False
            print("%s has died." % self.name)

    def attack(self, target):
        if self.alive:
            print("%s attacks %s. %s's health is %d. The enemy's health is %d." % (self.name, target.name, self.name,
                                                                                   self.health,
                                                                                   target.health))
            target.take_damage(self.damage)
        else:
            print("%s is dead and cannot attack" % self.name)


class Player(Character):
    def __init__(self, name, description, health, damage):
        super(Player, self).__init__(name, description, health, damage)

    def attack(self, target):
        if self.alive:
            print("%s attacks %s. %s's health is %d. The enemy's health is %d." % (self.name, target.name, self.name,
                                                                                   self.health,
                                                                                   target.health))
            target.take_damage(self.damage)
        else:
            print("%s is dead and cannot attack" % self.name)


player = Character("Student 051603A", "You're a student attending Aurora Academy Of Magics, you lost your power, \n"
                                      "during a battle with the Nirads, now you're determined to get them back \n",
                   0, 100, )


class Principal(Character):
    def __init__(self, name, description, health, damage):
        super(Principal, self).__init__(name, description, health, damage)


principal = Character("Principal", "Principal Rose helps run the school but the people who really run the school are \n"
                      "the head councils, she's going to meet you at the statue to give you some help \n", 0, 100)


class Nirad(Character):
    def __init__(self, name, description, health, damage):
        super(Nirad, self).__init__(name, description, health, damage)

    def growl(self):
        print("%s growls" % self.name)

    def attack(self, target):
        if self.alive:
            print("%s attacks %s. %s's health is %d. The enemy's health is %d." % (self.name, target.name, self.name,
                                                                                   self.health,
                                                                                   target.health))
            target.take_damage(self.damage)
        else:
            print("%s is dead and cannot attack" % self.name)


nirad = Character("Nirad", "A Nirad is a four armed monster that seems almost impossible to beat, these creatures \n "
                           "are the reason your powers are gone, you over used them trying to defeat them \n", 0, 100)
