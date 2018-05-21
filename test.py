# Any import statements
# https://www.jetbrains.com/shop/eform/students TO GET A BETTER FORM OF PYCHARM
import time

time_delay = .3  # Default is 3


def marriage_conversation():
    time_between = .1
    print("Queen Eleanor calls you to come to the dining room for dinner.")
    time.sleep(time_between)
    print("You go into the dining room, and you sit down to eat, but your mom keeps mumbling about something. ")
    time.sleep(time_between)
    print("Queen Eleanor: They've all accepted!")
    time.sleep(time_between)
    print("You: Who accepted what Mother?")
    time.sleep(time_between)
    print("Queen Eleanor: All three clans have accepted for the games for your hand in marriage.")
    time.sleep(time_between)
    print("You: WHAT?!?! THIS IS SO UNFAIR")
    time.sleep(time_between)
    print("Queen Eleanor: Merida, I don't know why your so upset, you've been preparing for this your entire life.")
    time.sleep(time_between)
    print("No. This is what you've been preparing for me and I won't go through with it.")


def talk_to_witch():
    time_between = .1  # Default is 2.5
    print("You go up the witch and start talking.")
    time.sleep(time_between)
    print("Witch: Welcome to my wood carving shop. Look around, everything is half off.")
    time.sleep(time_between)
    print("You: What the?")
    time.sleep(time_between)
    print("You: Why did the Willo-the-Wisps bring me here?")
    time.sleep(time_between)
    print("Crow: You know staring is rude.")
    time.sleep(time_between)
    print("You: THAT CROW JUST TALKED!! Your a witch!")
    time.sleep(time_between)
    print("Witch: No, woodcarver")
    time.sleep(time_between)
    print("You: I need a spell that will change my mum.")
    time.sleep(time_between)
    print("Witch: Too many unsatisfied customers. If you aren't going to buy anything, then get out.")
    time.sleep(time_between)
    print("You: I'll buy it all, every single wood carving, and a spell that can change my fate.")
    time.sleep(time_between)
    print("Witch: and how are going to pay for that?")
    time.sleep(time_between)


def trade_with_witch():
    print("The witch wants to trade with you for your special necklace.")
    print("You now have traded your special necklace for the potion from the witch.")


def talk_with_mom():
    print("You got the spell from the witch in a form of a little cake.")
    time.sleep(time_delay)
    print("Mom: Where have you been? I've been looking all over for you.")
    time.sleep(time_delay)
    print("You: I've just been in the forest with Angus.")
    time.sleep(time_delay)
    print("Mom: Well I've talked with the suitors about the marriage...")
    time.sleep(.1)
    print("You show your mom the little cake, and offer it as a peace offering.")
    time.sleep(time_delay)
    queen_eleanor.eat(cake)
    print("Your mom takes a bite of the cake, but there is something wrong going on with the cake.")
    time.sleep(2)
    print()
    print()
    print("After a while, your mom is not feeling so good, and you know it has to do with the cake.")
    time.sleep(time_delay)
    print("You take your Mom to your room, and she starts yelling at you about the cake.")
    time.sleep(time_delay)
    print("You tried to play it off, but something starts happening to your Mom. \n"
          "She falls off the bed, and she starts transforming into something else.")
    time.sleep(1)


def beginning_games():
    print("It is almost time for the games to begin. The games are for your hand in marriage. \n"
          "There are three clans here, in which none of their sons are worthy enough to you. \n"
          "Since you got to decide what the games are going to be, and since your the first born of your kingdom, \n"
          "you decide that that games are going to be archery \n"
          "you are going to play for your own hand so you don't have to marry.")
    time.sleep(time_delay)
    print("Now is your chance to compete. If you want to do it, then start shooting the targets right now.")


def argument():
    print("You start walking down to the targets and get ready to shoot your arrows.")
    time.sleep(time_delay)
    print("Mom: Merida, don't you dare shoot an arrow!!!")
    time.sleep(time_delay)
    print("You don't listen to her and you shoot the last target. And you have messed up everything.")
    time.sleep(time_delay)
    print("Your mom takes you into your room, and she is really, really mad at you.")
    time.sleep(time_delay)  # Makes this timer delay a little longer than normal
    print("Mom: You embarrassed them, you embarrassed me")
    time.sleep(time_delay)
    print("You: Mom it's not fair. You always tell me what to do, and what not to do. IT'S MY LIFE!!")
    time.sleep(time_delay)
    print("Mom: I AM THE QUEEN, YOU LISTEN TO ME")
    time.sleep(time_delay)


def running_away():
    print("You get mad at your mom and you run off.")


class Item(object):
    inventory = []

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pick_up(self, person):
        print("%s picked up %s" % person.name, self.name)

    def drop(self):
        print("You dropped %s" % self.name)

    def trade(self):
        print("You traded %s" % self.name)

    def carry(self):
        print("You are carrying %s" % self.name)

    def take(self):
        print("You took %s" % self.name)


class Consumable(Item):
    def __init__(self, name, description):
        super(Consumable, self).__init__(name, description)

    def use(self):
        print("You use the %s" % self.name)

    def eat(self):
        print("You ate the %s" % self.name)


class Hay(Consumable):
    def __init__(self, name, description):
        super(Hay, self).__init__(name, description)

    def use(self):
        print("You give the hay to a horse.")


class Cake(Consumable):
    def __init__(self, name, color, taste, description):
        super(Cake, self).__init__(name, description)
        self.color = color
        self.taste = taste

    def use(self):
        print("This cake is used as a potion")

    def eat(self):
        print("You ate the cake, but now you will turn into a bear")


class Water(Consumable):
    def __init__(self, name, person, description):
        super(Water, self).__init__(name, description)
        self.container = container
        self.person = person

    def drink(self, person):
        print("%s drank water" % person.name, self.name)


class Apple(Consumable):
    def __init__(self, name, color, description):
        super(Apple, self).__init__(name, description)
        self.color = color


class Fish(Consumable):
    def __init__(self, name, description):
        super(Fish, self).__init__(name, description)


class Weapon(Item):
    def __init__(self, name, description):
        super(Weapon, self).__init__(name, description)

    def fight(self, person):
        print("%s attacked with %s" % person.name, self.name)


class Sword(Weapon):
    def __init__(self, name, sharpness, description):
        super(Sword, self).__init__(name, description)
        self.sharpness = sharpness

    def stab(self, person):
        print("You stabbed %s with the %s." % (person.name, self.name))


class BowAndArrow(Weapon):
    def __init__(self, name, description):
        super(BowAndArrow, self).__init__(name, description)

    def shoot(self, person):
        print("You shot %s with the bow and arrow" % person.name)

    def carry(self):
        print("You picked up the %s" % self.name)


class Furniture(Item):
    def __init__(self, name, description):
        super(Furniture, self).__init__(name, description)

    def move(self):
        print("You moved the %s" % self.name)


class Tapestry(Furniture):
    def __init__(self, name, description):
        super(Tapestry, self).__init__(name, description)

    def mend(self):
        print("You mended the tapestry with %s." % self.name)


class Table(Furniture):
    def __init__(self, name, food, description):
        super(Table, self).__init__(name, description)
        self.food = food


class Rug(Furniture):
    def __init__(self, name, pattern, description):
        super(Rug, self).__init__(name, description)
        self.pattern = pattern


class BearStatue(Furniture):
    def __init__(self, name, description):
        super(BearStatue, self).__init__(name, description)

    def look_around(self):
        print("You looked around the %s" % self.name)


class Dresser(Furniture):
    def __init__(self, name, crown, mirror, necklace, description):
        super(Dresser, self).__init__(name, description)
        self.crown = crown
        self.mirror = mirror
        self.necklace = necklace


class Shield(Furniture):
    def __init__(self, name, description):
        super(Shield, self).__init__(name, description)

    def protect(self):
        print("You used the %s as protection" % self.name)


class WoodCarving(Furniture):
    def __init__(self, name, bear, description):
        super(WoodCarving, self).__init__(name, description)
        self.bear = bear

    def buy(self, person):
        print("You bought %s from %s" % self.name, person.name)


class Magic(Item):
    def __init__(self, name, description):
        super(Magic, self).__init__(name, description)

    def make(self):
        print("You made %s with magic" % self.name)


class Potion(Magic):
    def __init__(self, name, description):
        super(Potion, self).__init__(name, description)

    def transform(self, person):
        print("%s consumed the %s and now you transformed into a bear" % person.name, self.name)


class WillowtheWisp(Magic):
    def __init__(self, name, description):
        super(WillowtheWisp, self).__init__(name, description)

    def follow(self, person):
        print("%s followed the Willow the Wisp" % person.name, self.name)

    def appear(self):
        print("The %s appeared in front of you" % self.name)


class Misc(Item):
    def __init__(self, name, description):
        super(Misc, self).__init__(name, description)


class NeedleAndThread(Misc):
    def __init__(self, name, description):
        super(NeedleAndThread, self).__init__(name, description)

    def sew(self):
        print("You sewed the %s with the needle and thread " % self.name)


class Container(Misc):
    def __init__(self, name, items, description):
        super(Container, self).__init__(name, description)
        self.inventory = items

    def open(self, person):
        print("You opened the %s" % person.name, self.name)

    def put_in(self):
        print("You put %s into the %s" % (self.name, self.name))

    def take_out(self):
        print("You took %s out of the %s" % (self.name, self.name))

    def carry(self):
        print("You are carrying the %s" % self.name)

    def close(self):
        print("You closed the %s" % self.name)


class Bear(Item):
    def __init__(self, name, description):
        super(Bear, self).__init__(name, description)


class Target(Weapon):
    def __init__(self, name, description):
        super(Target, self).__init__(name, description)

    def shoot_in(self, person):
        print("%s shot the target with a %s" % person.name, self.name)


class SpecialNecklace(Misc):
    def __init__(self, name, description):
        super(SpecialNecklace, self).__init__(name, description)

    def wear(self, person):
        print("%s are wearing the %s" % person.name, self.name)

    def place(self):
        print("You placed the necklace in the %s" % self.name)


class Character(object):
    character = []

    def __init__(self, name, description, item, health, damage=10):
        self.name = name
        self.description = description
        self.inventory = [special_necklace]
        self.character = []
        self.item = item
        self.health = health
        self.damage = damage
        self.alive = False
        self.location = None
        self.first_time = True
        self.first_time_cottage = True
        self.bear = False

    # self.location = location

    # def look(self):
    # print(self.location.name)
    # print("You have looked around")
    # def eat_cake(self, item):

    def take(self, item):
        self.inventory.append(item)
        print("You have picked up %s" % item.name)

    def remove(self, item):
        self.inventory.remove(item)
        print("You dropped %s" % item.name)

    def eat(self, item):
        print("%s ate the %s" % (self.name, item.name))

    def transform(self):
        print("%s turned into a bear" % self.name)

    def shoot(self):
        print("%s shot with a bow and arrow" % self.name)

    def shoot_target(self):
        print("%s shoot at the target with the bow and arrow." % self.name)

    def rip_tapestry(self, tapestry):
        print("The tapestry of the family has been torn by %s." % self.name)

    def fish(self):
        print("%s caught some fish" % self.name)

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

    def move(self, direction):
        self.location = globals()[getattr(self.location, direction)]


class Room(object):
    def __init__(self, name, north, south, east, west, up, down, northeast, northwest, southeast, description,
                 items=None, characters=None):
        if items is None:
            items = []
        if characters is None:
            characters = []
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.northeast = northeast
        self.northwest = northwest
        self.southeast = southeast
        self.description = description
        self.items = items
        self.characters = characters
        self.first_time = True
        self.first_time_cottage = True


# Instantiation of class Room BEGINNING OF ITEMS
hay = Item("Hay", "There is hay in the stables to feed the horses.")

water = Item("Water", "In the dining room there is a bottle of water left on the table.")

apple = Item("Apple", "There is a bowl full of apples in the kitchen.")

cake = Item("Cake", "There is a little cake topped off with blueberries on the table.")

fish = Item("Fish", "There are fishes in the river.")

sword = Item("Sword", "The swords are kept in the fighting area, but Merida secretly has one in her room.")

bow_and_arrow = Item("Bow and Arrow", "These are kept in the fighting area, but Merida has her own bow and arrow \n"
                                      "that she keeps in her room.")

tapestry = Item("Tapestry", "Merida's mom has the tapestry hanging in her room. The tapestry has Merida's family \n"
                            "stitched on it.")

table = Item("Table", "The table is in the dining room. \n"
                      "There is a bottle of water on the table")

rug = Item("Rug", "There strange looking rug on the floor in the back in the witch's cottage. \n"
                  "It seems like the rug leads down to something, but the witch won't let you near the rug.")

bear_statue = Item("Bear Statue", "In the dining room, there is a bear statue in the corner. \n"
                                  "The bear statue is decoration, but sometimes the king uses the statue as practice \n"
                                  "defeating Mordu.")

dresser = Item("Dresser", "On the dresser has the King and Queen's things that they use to get ready in the morning. ")

shield = Item("Shield", "This shield that the one the King used in the war that they won against another country.\n"
                        "It hangs proudly in the dining room where everyone can see it.")

wood_carving = Item("Wood Carvings", "All of the wood carvings you see in the witch's cottage are bear themed. \n"
                                     "Inside you find many wood carvings, but one carving in the back catches your eye")

potion = Item("Potion", "The witch makes many different types of potions that helps change people's fate.\n"
                        "The witch can only make one potion for you, in exchange for a special necklace. \n"
                        "Her potions tend to change not only people's fate, but also their physical appearance.")

willo_the_wisp = Item("Willo-the-Wisp", "Willo-the-Wisps are little magic creatures that show up when you most need \n"
                                        "need help. People say that they can guide you to change your fate")

needle_and_thread = Item("Needle and Thread", "Queen Elanor keeps her sewing materials in their room.")

container = Item("Container", "You have a little brown sack that has all of your stuff.")

special_necklace = Item("Special Necklace", "This special necklace is the one that the Queen gave you. It's valuable \n"
                                            "and it has three bears in a circle engraved onto it.")
# END OF ITEMS BEGINNING OF CHARACTERS


merida = Character("Merida", "Merida is the princes of Dunbroch and has three little brothers. She is adventurous, \n"
                             "brave, and independent. Merida is the complete opposite of her mom, the Queen.", 1, 1)

queen_eleanor = Character("Queen Eleanor", "Queen Eleanor is Merida's mother. She wants her daughter to act like a \n"
                                           "princess and ladylike, but Merida is not like that at all.", 1, [])

king_fergus = Character("King Fergus", "King Fergus is Merida's father. The story of how King Fergus lost his left to\n"
                                       "Mordu became legend.", [], 1)

triplets = Character("Triplets", "The triplets are Merida's three little brothers. They are very mischievous, but \n"
                                 "they never get caught.", [], 1)

witch = Character("Witch", "The witch covers her identity as a woodcarver and carves pictures of bears. She has a \n"
                           "secret magic room where she does all of her magic making.", [], 1)

mordu = Character("Mordu", "Mordu is actually the oldest prince of the kingdom, before the kingdom fell.\n"
                           "He found the witch, and asked her for a spell that would give him the strength of 10 men\n"
                           "but that spell changed him into a bear. If he did mend the bond he broke, he could have \n"
                           "turned back into a human.", [], 1)

angus = Character("Angus", "Angus is Merida's horse. She always takes Angus out on the days she has off. ", [], 1)
# END OF CHARACTERS BEGINNING OF ROOMS
meridas_room = Room("Meridas Room", None, 'dining_room', 'parents_room', 'kitchen', None, None, None, None, None,
                    'Welcome to Meridas room! In here there is a bow and arrow, a sword, and a container. \n'
                    'There is a door South, East, and West of the room.', [sword, bow_and_arrow, container], [merida])
parents_room = Room("Parents Room", None, None, None, 'meridas_room', None, None, None, None, None,
                    'This is where the king and queen stay.\n'
                    "There is a dresser, and a small box that is full of Queen Elanor's needle and threads in the \n"
                    "room and a door to the West.",
                    [dresser, needle_and_thread, tapestry], [king_fergus, queen_eleanor])
dining_room = Room("Dining Room", 'meridas_room', None, None, None, None, 'secret_room', None, None, None,
                   'There is a table in the middle of the room.\n'
                   'There is a shield on the wall and a bear statue in the corner.\n'
                   'There is a door to the north.', [bear_statue, shield], [triplets])
kitchen = Room("Kitchen", 'outside', None, 'meridas_room', None, None, None, None, 'stables', None,
               'There is a door that leads Northwest, North, and East.\n'
               'There is a little crate on the floor next to the door.\n'
               'There are some apples in the barrel', [apple, cake], [queen_eleanor])
outside = Room("Outside", 'stables', 'kitchen', None, 'forest', None, None, None, None, 'fighting_area',
               'Out here is the main gate.\n'
               'West to the gate is the forest.\n'
               'You can also go South or Southeast.')
fighting_area = Room("Fighting Area", None, 'water', None, None, None, None, None, 'outside', None,
                     'Here are lots of '
                     'weapons.\n Off to the South there is water and some boats \n'
                     'Northwest leads to the gate to outside', [sword, bow_and_arrow], [king_fergus])
stables = Room("Stables", None, 'outside', None, None, None, None, 'kitchen', None, None,
               'Here are all the horses.\n'
               'There is hay and water here as well.\n'
               'You can go South or Northeast.', [hay, water], [angus])
forest = Room("Forest", None, 'fire_fall', 'outside', None, None, None, None, None, 'the_ring_of_stones',
              'There is a path to the South and to the Southeast.\n'
              'There is also a path that leads to the East', [willo_the_wisp])
fire_fall = Room("Fire Fall", 'forest', None, 'the_ring_of_stones', None, None, None, None, None, None,
                 'Here there is a water fall and a rock to climb.\n'
                 'Legends say that only kings were brave enough to drink from this water fall. \n'
                 'There are paths to North, and East')
the_ring_of_stones = Room("The Ring of Stones", None, 'river', 'witches_cottage', 'fire_fall', None, None, None,
                          'forest',
                          None, 'Here are stones that are placed in a circular pattern.\n'
                                'People said that The Ring of Stones tends to take you places to change your fate.\n'
                                'There are paths that lead to East, West, Northwest, and South', [willo_the_wisp])
witches_cottage = Room("Witches Cottage", None, None, None, 'the_ring_of_stones', 'dining_room', 'magic_room', None,
                       None, None, 'You have found the witches cottage.\n'
                                   'Inside you find many wood carvings, but one carving in the back catches your eye.\n'
                                   'You also find a strange looking rug on the floor in the back. \n'
                                   'From here you can go West.', [rug, wood_carving, potion], [witch])
magic_room = Room("Magic Room", None, None, None, None, 'witches_cottage', None, None, None, None,
                  'This is where the witch does her magic.\n'
                  'The only way out is from the door you came in from.', [cake, potion], [witch])
river = Room("River", 'the_ring_of_stones', None, None, None, None, None, 'ancient_kingdom_ruins', None, None,
             'There is a river that runs off into two separate rivers.\n'
             'Here you see some bears catching fish.\n'
             'There is a path that leads north and northeast', [fish])
ancient_kingdom_ruins = Room("Ancient Kingdom Ruins", None, None, None, None, None, 'moruds_cave', None, None, 'river',
                             'This is the old kingdom of Dunbroch before Mordu destroyed it.\n'
                             'You find the same symbol you saw in the castle of the three bears.\n'
                             'There is a path that leads down and another one that goes southeast.')
mordus_cave = Room("Mordus Cave", None, None, None, None, 'ancient_kingdom_ruins', None, None, None, None,
                   'Your in a dark cave with only faint light from above.\n'
                   'There are bones everywhere, and many broken weapons.\n'
                   'There is also a tapestry of four princes.\n'
                   'You hear heavy breathing behind you, and you see Mordu behind you.', [mordu])

water = Room("Water", 'fighting_area', None, None, None, None, None, None, None, None,
             'Out here, there is a lake in front of you and some boats tied to the dock \n'
             'You can not go onto the boats.', [triplets])

merida.location = meridas_room
directions = ['north', 'south', 'east', 'west', 'up', 'down', 'northeast', 'northwest', 'southeast']
short_directions = ['n', 's', 'e', 'w', 'u', 'd', 'ne', 'nw', 'se']
inventory = ['inventory']
character = ['character']
moved = True

while True:
    # Room information
    if moved:
        print(merida.location.name)
        print(merida.location.description)
    moved = False
    removed = False
    # Take input
    command = input('> ').strip().lower()

    # Pre-processing
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Finds the command in short directions (index number)
        pos = short_directions.index(command)
        command = directions[pos]

    # Processing
    if command in directions:
        try:
            merida.move(command)
            moved = True
        except KeyError:
            print("You cannot go that way.")

    elif command == 'inventory':
        try:
            for item_ in merida.inventory:
                print(item_.name)
        except KeyError:
            print("You don't have anything in your inventory.")

    elif command == 'character':
        try:
            for character_ in merida.character:
                print(character_.name)
        except KeyError:
            print("There is no one with you.")

    elif 'take' in command:
        take_name = command[5:]
        found = None
        for item in merida.location.items:
            if take_name == item.name.lower():
                merida.take(item)
                found = item
        if found is None:
            print("It is not in the room.")
        else:
            merida.location.items.remove(found)
    elif 'remove' in command:
        remove_name = command[7:]
        remove = None
        for item in merida.inventory:
            if remove_name == item.name.lower():
                merida.remove(item)
                merida.location.items.append(item)
                remove = item
    elif 'shoot' in command:
        if bow_and_arrow in merida.inventory:
            merida.shoot()
        else:
            print("You don't have it in your inventory")
    elif 'catch fish' in command:
        if merida.location == river:
            merida.fish()
            merida.inventory.append(fish)
    elif 'eat' in command:
        eat_name = command[4:]
        for item in merida.inventory:
            if eat_name == item.name.lower():
                merida.eat(item)
                merida.inventory.remove(item)
    else:
        print("Command not Recognized")

    # React to new room
    if merida.location == witches_cottage and merida.first_time_cottage is True:
        print(merida.location.name)
        print(merida.location.description)
        time.sleep(time_delay)
        print()
        item = ""
        if potion not in merida.inventory and merida.first_time_cottage is True:
            talk_to_witch()
            merida.first_time_cottage = False
            response = input(">_")
            while response != 'special necklace':
                print("That's not worth enough.")
                print("What else do you got?")
                response = input(">_").lower()
            else:
                print("That's a deal.")
                trade_with_witch()
                merida.inventory.append(potion)
                merida.inventory.remove(special_necklace)
        else:
            print("The witch is gone. \n"
                  "The witch did leave a message for you in her secret magic room.")

    if merida.location == outside and merida.first_time and queen_eleanor.first_time is False:  # Starting of games
        print(merida.location.name)
        print(merida.location.description)
        time.sleep(time_delay)
        print()
        beginning_games()
        merida.first_time = False
        response = input(">_")
        while response != 'shoot target' and merida.location == outside and merida.first_time is False:
            print("You are not shooting yet. Try again")
            response = input(">_").lower()
        else:
            print(argument())
            merida.rip_tapestry(tapestry)
            print(running_away())

    if merida.location == kitchen:
        if potion in merida.inventory:
            print(merida.location.name)
            print(merida.location.description)
            time.sleep(time_delay)
            print()
            talk_with_mom()
            time.sleep(2)
            queen_eleanor.transform()
            queen_eleanor.bear = True
            merida.inventory.remove(potion)
            if queen_eleanor.bear is True:
                merida.character.append(queen_eleanor.name)
                print("You can't let anyone see your mom as a bear, so now you have to hide your mom.")
            for character in merida.character:
                print(merida.character.__str__())
    if merida.location == dining_room and queen_eleanor.first_time:
        print(merida.location.name)
        print(merida.location.description)
        time.sleep(time_delay)
        print()
        marriage_conversation()
        queen_eleanor.first_time = False

    if merida.location == magic_room:
        if queen_eleanor.bear is True:
            print("The witch is not here right now, but she forgot to tell you that if the spell is not broken \n"
                  "by the second sunrise, the spell will be permanent.")
            time.sleep(time_delay)
            print("The message is: Faith be changed \n"
                  "Look inside \n"
                  "Mend the bond torn by pride.")