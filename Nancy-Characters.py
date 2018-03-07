class Shoes(object):
    def __init__(self, name, talking, interact, inventory, abilities, stats, health, status_effects,
                 physique, description, dialogue, attack, take_damage, defend):
        self.name = name
        self.talking = False
        self.interact = False
        self.inventory = inventory
        self.abilities = abilities
        self.stats = stats
        self.health = health
        self.status_effects = status_effects
        self.physique = physique
        self.description = description
        self.dialogue = dialogue
        self.attack = attack
        self.take_damage = take_damage
        self.defend = defend

    def wear(self):
        self.talking = True
        self.interact = False
        print("You wear the shoes")