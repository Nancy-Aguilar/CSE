class Character(object):
    def __init__(self, name, description, health, inventory, dialogue, attack, take_damage, interact):
        self.name = name
        self.description = description
        self.health = health
        self.inventory = inventory
        self.dialogue = dialogue
        self.attack = attack
        self.take_damage = take_damage
        self.interact = interact

    def collect(self):
        if self.interact:
            print("You collected %s" % self.name)

    def attack(self):
        if self.attack:
            print("You attacked")