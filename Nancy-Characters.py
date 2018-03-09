class Shoes(object):
    def __init__(self, name, inventory, abilities, health, status_effects,
                 physique, description, dialogue, attack, take_damage, defend):
        self.name = name
        self.interact = False
        self.inventory = inventory
        self.abilities = abilities
        self.health = health
        self.status_effects = status_effects
        self.physique = physique
        self.description = description
        self.dialogue = dialogue
        self.attack = attack
        self.take_damage = take_damage
        self.defend = defend

    def interact(self):
        if self.interact:
            self.interact = True
            print("You picked up the book")
        else:
            print("There's nothing to pick up")

