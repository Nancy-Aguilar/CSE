class Character(object):
    character = []

    def __init__(self, name, description, health, damage):
        self.name = name
        self.description = description
        self.health = health
        self.inventory = []
        self.damage = damage
        self.alive = True
        self.location = None
        self.first_time = True
        self.first_time_STATUE = True
        self.first_time_LIBRARY = True
        self.first_time_BSE1 = True
        self.first_time_BSE2 = True
        self.first_time_SECRET1 = True
        self.first_time_SECRET2 = True
        self.first_time_CT1 = True
        self.first_time_CT2 = True
        self.first_time_CT3 = True
        self.first_time_CT4 = True
        self.first_time_OFFICE = True
        self.first_time_NURSE = True
        self.first_time_LOUNGE = True
        self.first_time_CAFE = True
        self.first_time_DORMS1 = True
        self.first_time_DORMS2 = True
        self.first_time_DORMS3 = True
        self.first_time_DORMS4 = True
        self.first_time_PTR = True
        self.first_time_CREATION = True
        self.first_time_WEAPON = True
        self.first_time_CLASS = True
        self.first_time_CP1 = True
        self.first_time_CP2 = True
        self.first_time_CP3 = True
        self.first_time_CP4 = True
        self.first_time_CP5 = True
        self.first_time_CP6 = True
        self.first_time_CP7 = True
        self.first_time_CP8 = True
        self.first_time_CP9 = True
        self.first_time_CP10 = True
        self.first_time_CP11 = True
        self.first_time_CP12 = True
        self.first_time_CP13 = True
        self.first_time_CP14 = True
        self.first_time_CP15 = True

    def collect(self, item1):
        self.inventory.append(item1)
        print("You collected the %s" % item1.name)

    def remove(self, item2):
        self.inventory.remove(item2)
        print("You removed the %s" % item2.name)

    def eat(self, apple):
        print("You ate the %s" % apple.name)
        self.health = 100

    def give(self):
        print("%s gives card" % self.name)

    def put(self, crystalheart):
        print("You put the %s in the statue" % crystalheart.name)

    def touch(self):
        print("You touch the tree and get your powers back")

    def use(self):
        print("You use the Medical kit")
        self.health = 100

    def health(self):
        print(self.name.damage)
        print("You have health")

    def cut(self, nirad1):
        print("You cut the %s" % nirad1.name)

    def shoot(self):
        print("You shoot %s" % self.name)

    def take_damage(self, amt):
        if self.health <= 0:
            print("%s is dead" % self.name)
            return
        self.health -= amt
        if self.health <= 0:
                self.alive = False
                print("%s is dead" % self.name)

    def attack(self, target):
        if self.alive:
            print("%s attacks %s. The Nirad's health is %d." % (self.name, target.name, target.health))

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

    def give(self):
        print("%s gives card" % self.name)


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

player.attack(nirad)
nirad.attack(player)
principal.give()
