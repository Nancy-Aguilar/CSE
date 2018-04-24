class Character(object):
    def __init__(self, name, description, health, inventory, attack, take_damage, interact):
        self.name = name
        self.description = description
        self.health = health
        self.inventory = inventory
        self.attack = attack
        self.take_damage = take_damage
        self.interact = interact

    def collect(self):
        if self.interact:
            print("You collected %s" % self.name)

    def attack(self):
        if self.attack:
            print("You attacked")

    def protect(self):
        if self.take_damage:
            print("You protected yourself")


Character1 = Character('name', 'description', '100', 'items', '90', '0', 'interact')
Character1.collect()
Character1.attack()
Character1.protect()