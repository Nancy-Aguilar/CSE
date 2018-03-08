class Shoes(object):
    def __init__(self, name, talking, interact, inventory, abilities, stats, health, status_effects,
                 physique, description, dialogue, attack, take_damage, defend):
        self.name = name
        self.talking = talking
        self.interact = interact
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

    def attacking(self):
        if self.attack:
            print("You attacked")
        else:
            print("You missed")