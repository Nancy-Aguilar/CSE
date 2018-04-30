class Character(object):
    def __init__(self, name, description, health, attack, damage, interact):
        self.name = name
        self.description = description
        self.health = health
        self.inventory = []
        self.attack = attack
        self.damage = damage
        self.interact = interact
        self.alive = False

    def collect(self, item):
        self.inventory.append(item)
        print("You collected %s" % self.name)

    def heath(self):
        print(self.name.damage)
        print("You have health")

    def take_damage(self):
        if self.health <= 0:
            print("%s is already dead" % self.name)
            return
        self.health -= 100
        if self.health <= 0:
            self.alive = False
            print("%s died" % self.name)

    def attack(self, target):
        if self.alive:
            print("%s attacks %s. %s health is %d. The enemy's health is %d" % (self.name, target.name, self.name,
                                                                                self.health, target.health))


Character1 = Character("name", "You're wearing casual clothing", 100, 45, 10, None)
Character2 = Character("Monster", "This monster is very big", 100, 50, 30, None)