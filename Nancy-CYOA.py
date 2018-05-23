import time


def conprincipal():  # Talking with principal
    print("Principal: I'm glad that you were able to make it here on time I was just about to leave")
    time.sleep(5)
    print("You: Yeah, it would of been bad if you left, then I wouldn't be able to go anywhere around campus")
    time.sleep(5)
    print("Principal: That's true, here is my spare card, now don't lose it and bring it to me tomorrow morning")
    time.sleep(5)
    print("You: Ok I will, thanks for lending me your card this will really help me a lot")
    time.sleep(5)
    print("Principal: Your welcome and don't ruin the campus, we have school tomorrow")
    time.sleep(5)
    print("You: I won't see, you tomorrow morning then bye!")
    time.sleep(5)
    print("Principal: Bye")
    time.sleep(5)
    print("*The principal leaves*")


def narstaute():
    time.sleep(5)
    print("You: *looks at the tree statue* It looks like it's missing a center piece")
    time.sleep(5)
    print("You: Well it's time to get my powers back, now where should I go?")
    time.sleep(5)
    print("You: The Library seems like a good start")


def narlibrary():
    time.sleep(5)
    print("You: Come to think about it, this is my first time in the library")
    time.sleep(5)
    print("You: There's a book on the floor on the east side of the library I should pick it up")
    time.sleep(5)
    print("You: It's a book of legends, maybe it will give me clues to get my powers back")
    time.sleep(5)
    print("*shake shake* You: What's going on? The shelf! It's opening? ")
    time.sleep(5)
    print("You: It looks like a room in there, I should go check it out")
    time.sleep(5)
    print("You: There's a lot of dust in here, and it looks like a letter is on the ground")
    time.sleep(5)
    print("You: I should go back now")
    time.sleep(5)
    print("*shake shake* You: The shelf is closing now")
    time.sleep(5)
    print("You: I should check the other shelf out, there might be books that could be useful")
    time.sleep(5)
    print("You: *reads* All of these books are about math, english and regular class subjects, I don't need these")
    time.sleep(5)
    print("*shake shake* You: This shelf is opening like the other one")
    time.sleep(5)
    print("You: There's a room in there too, I should go in, a clue might be in there")
    time.sleep(5)
    print("You: This room is also very dusty and there's nothing in here")
    time.sleep(5)
    print("You: I should go back now")
    time.sleep(5)
    print("*shake shake* You: The shelf is closing now")
    time.sleep(5)
    print("You: I should go somewhere else now the combat training room is up ahead maybe I should go there")


def ctrooms():
    time.sleep(5)
    print("You: There's nothing much in here but training equipment")
    time.sleep(5)
    print("You: I should go somewhere else")


def office():
    time.sleep(5)
    print("You: I wonder if there's something in here that I can use, hmm *sees flashlight* that might be useful")
    time.sleep(5)
    print("You: The Nurse's room is near here I should go check it out")


def nurseroom():
    time.sleep(5)
    print("You: There's a medical kit on the desk")
    time.sleep(5)
    print("You: Nothing much is in here that could help I should go somewhere else")


def loungeroom():
    time.sleep(5)
    print("You: There's nothing much in here just chairs and tables")
    time.sleep(5)
    print("You: The cafeteria is close by I should go grab a snack")


def cafe():
    time.sleep(5)
    print("You: There's an apple on a table I should go grab it")
    time.sleep(5)
    print("You: It looks like there isn't any other food around here")
    time.sleep(5)
    print("You: I should go somewhere else now")


def dorms():
    time.sleep(5)
    print("You: People are in here, I should be quiet")
    time.sleep(5)
    print("You: There isn't really anything here that would help me I should move on")


def ptr():
    time.sleep(5)
    print("You: All the equipment are out, there isn't really anything here that can be useful")
    time.sleep(5)
    print("You: There's a station for creating things up ahead, maybe I should check it out")


def sfc():
    time.sleep(5)
    print("You: There's a crystal heart on the table")
    time.sleep(5)
    print("You: It looks like someone created it")


def weapon():
    time.sleep(5)
    print("You: There's only a sword, bow and arrow, and axe in here")
    time.sleep(5)


class Item(object):
    inventory = []

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def collect(self):
        print("You collected %s" % self.name)

    def drop(self):
        print("You dropped %s" % self.name)


class Weapon(Item):
    def __init__(self, name, description):
        super(Weapon, self).__init__(name, description)

    def collect(self):
        print("You collected a %s" % self.name)

    def drop(self):
        print("You dropped %s" % self.name)


class Sword(Weapon):
    def __init__(self, name, description, power):
        super(Sword, self).__init__(name, description)
        self.power = power

    def stab(self):
        print("You attacked with %s" % self.name)

    def cut(self):
        print("You cut with the %s" % self.name)


class BowArrow(Weapon):
    def __init__(self, name, description, power):
        super(BowArrow, self).__init__(name, description)
        self.power = power

    def shoot(self):
        print("You shot an arrow with %s" % self.name)


class Axe(Weapon):
    def __init__(self, name, description, power):
        super(Axe, self).__init__(name, description)
        self.power = power

    def swing(self):
        print("You swing the %s" % self.name)


class Keys(Item):
    def __init__(self, name, description):
        super(Keys, self).__init__(name, description)

    def collect(self):
        print("You collected %s key" % self.name)

    def drop(self):
        print("You dropped the %s" % self.name)


class Blackkey(Keys):
    def __init__(self, name, description):
        super(Blackkey, self).__init__(name, description,)

    def insert(self):
        print("You insert the %s" % self.name)


class Dormkey(Keys):
    def __init__(self, name, description):
        super(Dormkey, self).__init__(name, description)

    def insert(self):
        print("You insert the %s" % self.name)


class Schoolkey(Keys):
    def __init__(self, name, description):
        super(Schoolkey, self).__init__(name, description)

    def insert(self):
        print("You insert the %s" % self.name)


class Consumables(Item):
    def __init__(self, name, description):
        super(Consumables, self).__init__(name, description)

    def collect(self):
        print("You collected %s" % self.name)

    def drop(self):
        print("You drop %s" % self.name)


class Apple(Consumables):
    def __init__(self, name, description):
        super(Apple, self).__init__(name, description)

    def eat(self):
        print("You eat the %s" % self.name)


class Medkit(Consumables):
    def __init__(self, name, description):
        super(Medkit, self).__init__(name, description)

    def use(self):
        print("You use the %s" % self.name)


class Tools(Item):
    def __init__(self, name, description):
        super(Tools, self).__init__(name, description)

    def collect(self):
        print("You collected %s" % self.name)

    def drop(self):
        print("You drop %s" % self.name)


class Flashlight(Tools):
    def __init__(self, name, description):
        super(Flashlight, self).__init__(name, description)

    def turn_on(self):
        print("You turn on %s" % self.name)

    def turn_off(self):
        print("You turn off the %s" % self.name)


class Cloths(Item):
    def __init__(self, name, description):
        super(Cloths, self).__init__(name, description)

    def collect(self):
        print("You collected %s" % self.name)

    def wear(self):
        print("You wear %s" % self.name)


class Pants(Cloths):
    def __init__(self, name, description):
        super(Pants, self).__init__(name, description)

    def put_on(self):
        print("You put on %s" % self.name)

    def take_off(self):
        print("You take off %s" % self.name)


class Sweater(Cloths):
    def __init__(self, name, description):
        super(Sweater, self).__init__(name, description)

    def put_on(self):
        print("You put on %s" % self.name)

    def take_off(self):
        print("You take off %s" % self.name)


class Book(Item):
    def __init__(self, name, description):
        super(Book, self).__init__(name, description)

    def collect(self):
        print("You collected %s " % self.name)

    def drop(self):
        print("You dropped %s" % self.name)


class Bookoflegends(Book):
    def __init__(self, name, description):
        super(Bookoflegends, self).__init__(name, description)

    def open(self):
        print("You opened the %s" % self.name)

    def read(self):
        print("The book says %s" % self.description)

    def close(self):
        print("You close the %s" % self.name)


class Letters(Item):
    def __init__(self, name, description):
        super(Letters, self).__init__(name, description)

    def collect(self):
        print("You collected %s" % self.name)

    def drop(self):
        print("You dropped %s" % self.name)


class Sorry(Letters):
    def __init__(self, name, description):
        super(Sorry, self).__init__(name, description)

    def open(self):
        print("You opened the %s" % self.name)

    def read(self):
        print("The letter says %s" % self.description)


class TheTree(Letters):
    def __init__(self, name, description):
        super(TheTree, self).__init__(name, description)

    def open(self):
        print("You open the %s" % self.name)

    def read(self):
        print("The letter says %s" % self.description)


class Creations(Item):
    def __init__(self, name, description):
        super(Creations, self).__init__(name, description)

    def take_out(self):
        print("You took out %s" % self.name)

    def drop(self):
        print("You dropped %s" % self.name)


class Crystalheart(Creations):
    def __init__(self, name, description):
        super(Crystalheart, self).__init__(name, description)

    def place_in(self):
        print("You place the % in the tree statue" % self.name)


# Character starts

class Character(object):
    character = []

    def __init__(self, name, description, health, damage):
        self.name = name
        self.description = description
        self.health = health
        self.inventory = [Dormkey, Sorry, Schoolkey]
        self.damage = damage
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


player = Character("Student 051603A", "You're a student attending Aurora Academy Of Magics, you lost your power, \n"
                                      "during a battle with the Nirads, now you're determined to get them back \n", 100,
                   0)

principal = Character("Principal", "Principal Rose helps run the school but the people who really run the school are \n"
                      "the head councils, she's going to meet you at the statue to give you some help \n", 100, 100)

nirad1 = Character("Nirad", "A Nirad is a four armed monster that seems almost impossible to beat, these creatures \n"
                            "are the reason your powers are gone, you over used them trying to defeat them \n", 100, 0)

nirad2 = Character("Nirad", "A Nirad is a four armed monster that seems almost impossible to beat, these creatures \n"
                            "are the reason your powers are gone, you over used them trying to defeat them \n", 100, 0)

nirad3 = Character("Nirad", "A Nirad is a four armed monster that seems almost impossible to beat, these creatures \n"
                            "are the reason your powers are gone, you over used them trying to defeat them \n", 100, 0)

nirad4 = Character("Nirad", "A Nirad is a four armed monster that seems almost impossible to beat, these creatures \n"
                            "are the reason your powers are gone, you over used them trying to defeat them \n", 100, 0)

nirad5 = Character("Nirad", "A Nirad is a four armed monster that seems almost impossible to beat, these creatures \n"
                            "are the reason your powers are gone, you over used them trying to defeat them \n", 100, 0)

nirad6 = Character("Nirad", "A Nirad is a four armed monster that seems almost impossible to beat, these creatures \n"
                            "are the reason your powers are gone, you over used them trying to defeat them \n", 100, 0)

nirad7 = Character("Nirad", "A Nirad is a four armed monster that seems almost impossible to beat, these creatures \n"
                            "are the reason your powers are gone, you over used them trying to defeat them \n", 100, 0)

nirad8 = Character("Nirad", "A Nirad is a four armed monster that seems almost impossible to beat, these creatures \n"
                            "are the reason your powers are gone, you over used them trying to defeat them \n", 100, 0)

# Character ends


class Room(object):
    def __init__(self, name, description, north, south, east, west, items=None, characters=None):
        if items is None:
            items = []
        if characters is None:
            characters = []
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.items = items
        self.characters = characters

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


Sword = Sword('Hinoken', 'the blade of the sword is covered in fire', 40)

BowArrow = BowArrow('Seimitsuna shotto', 'shoots are always precise', 29)

Axe = Axe('Ono', 'small but durable', 25)

Blackkey = Blackkey('Black Key', 'Their are some words engraved on the key')

Dormkey = Dormkey('Dorm Key', 'The key to your dorm #16')

Schoolkey = Schoolkey('Spare Key', 'this key can open an door on campus except the dorms')

Apple = Apple('Apple', 'red and delicious')

Medkit = Medkit('Medkit', 'Contains bandages, rubbing alcohol, and pain killers')

Flashlight = Flashlight('Flashlight', 'Shines very bright in the dark')

Pants = Pants('Pants', 'color of the pants are black')

Sweater = Sweater('Hoodie', 'color of the hoodie is grey')

Bookoflegends = Bookoflegends('Book Of Legends', 'Contains many legends that were passed down from generations')

Sorry = Sorry('Student 051603A', 'We have been informed that you have lost your magical abilities during the battle '
                                 'against the Nirads and you have requested to find a way to return your abilities. The'
                                 'head council have granted you permission to let you use the campus as needed.')

TheTree = TheTree('The Tree', 'The tree is real, and this school is the key to it, the tree statue holds the key to the'
                              'cave the weapon rooms hides, and the cave is not an easy task to get through, but it was'
                              'worth it if it meant getting my abilities back')

Crystalheart = Crystalheart('Crystal Heart', 'A median sized crystal heart that shines very bright')


# north, south, east, west, items, characters
# Initialize Rooms
STATUE = Room("Tree Statue", "You're standing next to a tree statue, it appears to be missing a heart shaped object in "
                             "its center, up North is the Library", 'LIBRARY', None, None, None, [Schoolkey],
              [player, principal])
LIBRARY = Room("Library", "You're inside the library, standing in the center and their are two book shelves on the "
                          "West and East side of the library, up North is Combat Training room 1", 'CT1', 'STATUE',
               'BSE2', 'BSE1', None, [player])
BSE1 = Room("Book shelves", "You approached the book shelves and they suddenly moved to reveal a secret room", None,
            None, 'LIBRARY', 'SECRET1', None, [player])
BSE2 = Room("Book shelves", "You approached the book shelves and they suddenly moved to reveal a secret room", None,
            None, 'SECRET2', 'LIBRARY', [Bookoflegends], [player])
SECRET1 = Room("Secret Room #1", "You're inside a secret room and the only thing in there is a dusty old book on the "
                                 "ground", None, None, 'BSE1', None, None, [player])
SECRET2 = Room("Secret Room #2", "You're inside a secret room and the only thing in there is letter on the ground",
               None, None, None, 'BSE2', [TheTree], [player])
CT1 = Room("Combat Training Room #1", "You're inside the training room for 1st years, facing West is the training room "
                                      "for 3rd years, facing East is the training room for 2nd years, and North is the "
                                      "training room for 4th years", 'CT4', 'LIBRARY', 'CT2', 'CT3', None, [player])
CT2 = Room("Combat Training Room #2", "You're inside the combat training room for 2nd years, on the East side is the "
                                      "office and on the West side is the combat training room for 1st years", None,
           None, 'OFFICE', 'CT1', None, [player])
CT3 = Room("Combat Training Room #3", "You're inside the combat training room for 3rd years, on the East side is the "
                                      "combat training room for 1st years, on the West side are the dorms for 1st "
                                      "years", None, None, 'CT1', 'DORMS1', None, [player])
CT4 = Room("Combat Training Room #4", "You're inside the combat training room for 4th years and up North are the "
                                      "classrooms", 'CLASS', 'CT1', None, None, None, [player])
OFFICE = Room("Office", "You're inside the office and facing East is the Nurse's room and facing West is the training "
                        "room for 2nd years", None, None, 'NURSE', 'CT2', [Flashlight], [player])
NURSE = Room("Nurse's Room", "You're inside the Nurse's room and facing East is the Nurse's room and facing North is "
                             "the lounge room and facing West is the office", 'LOUNGE', None, None, 'OFFICE', [Medkit],
             [player])
LOUNGE = Room("Lounge Room", "You're at the lounge room and there is a bag of carbon on a sofa, facing West is the "
                             "Cafeteria", None, 'NURSE', None, 'CAFE', None, [player])
CAFE = Room("Cafeteria", "You're inside the Cafeteria with many tables and chairs and some food trays. Facing East is "
                         "the lounge room", None, None, 'LOUNGE', None, [Apple], [player])
DORMS1 = Room("Dorms for 1st years", "You're inside a dorm building, all the rooms are closed and facing North are "
                                     "the 2nd year dorms", 'DORMS2', None, 'CT3', None, None, [player])

DORMS2 = Room("Dorms for 2nd years", "You're inside a dorm building, all the rooms are closed and facing North are "
                                     "the 3rd year dorms", 'DORMS3', 'DORMS1', None, None, None, [player])
DORMS3 = Room("Dorms for 3rd years", "You're inside a dorm building, all the rooms are closed and facing North are "
                                     "the 4th year dorms", 'DORMS4', 'DORMS2', None, None, None, [player])

DORMS4 = Room("Dorms for 4th years", "You're inside a dorm building, all the rooms are closed and facing North is "
                                     "the power training room", 'PTR', 'DORMS3', None, None, None, [player])
PTR = Room("Power Training Room", "You're in the power training room and their's a station for creating items up "
                                  "North and facing East is the weapon room", 'CREATION', 'DORMS4', 'WEAPON', None, None
           [player])
CREATION = Room("Creation Table", "You're standing in front of a table that has a crystal heart on top of it", None,
                'DORMS4', 'WEAPON', None, None, [player])
WEAPON = Room("Weapon Room", "You're inside the weapon room, there's a sword and bow/arrow on a table and there is an "
                             "entrance to a cave but it's locked and facing South are the classrooms", None, 'CLASS',
              'CP1', 'PTR', [Sword, BowArrow, Axe], [player])
CLASS = Room("Classroom", "You're inside the classrooms and all the rooms are locked, facing North is the weapon room",
             'WEAPON', 'CT4', None, None, None, [player])
CP1 = Room("Cave Place #1", "You're inside the cave and people say that there are many dangerous things inside and "
                            "multiple places in the cave, there's a light leading South and East", None, 'CP7', 'CP2',
           'WEAPON', None [player])
CP2 = Room("Cave PLace #2", "There's nothing here but a light leading East, South, and West", None, 'CP8', 'CP3',
           'CP1', None, [player, nirad1])
CP3 = Room("Cave PLace #3", "There's nothing here but a light leading East, South, and West", None, 'CP6', 'CP4',
           'CP2', None, [player])
CP4 = Room("Cave PLace #4", "There's nothing here but a light leading East, South, and West", None, 'CP9', 'CP5', 'CP3',
           None, [player])
CP5 = Room("Cave PLace #5", "There's nothing here but a light leading South and West", None, 'CP10', None, 'CP4', None,
           [player, nirad2])
CP6 = Room("Cave PLace #6", "There's nothing here but a light leading North", 'CP3', None, None, None, None,
           [player, nirad3])
CP7 = Room("Cave PLace #7", "There's nothing here but a light leading North, South, and East", 'CP1', 'CP11', 'CP8',
           None, None, [player])
CP8 = Room("Cave PLace #8", "There's nothing here but a light leading North, South, and West", 'CP2', 'CP12', None,
           'CP7', None, [player, nirad4])
CP9 = Room("Cave PLace #9", "There's nothing here but a light leading North, South, and East", 'CP4', 'CP14', 'CP10',
           None, None, [player, nirad5])
CP10 = Room("Cave PLace #10", "There's nothing here but a light leading North, South, and West", 'CP5', 'CP15', None,
            'CP9', None, [player])
CP11 = Room("Cave PLace #11", "There's nothing here but a light leading North and East", 'CP7', None, 'CP12', None,
            None, [player, nirad6])
CP12 = Room("Cave PLace #12", "There's nothing here but a light leading North, East, and West", 'CP8', None, 'CP13',
            'CP11', None, [player])
CP13 = Room("Cave PLace #13", "There's nothing here but a light leading North, East, and West", 'TREE', None, 'CP14',
            'CP12', None, [player, nirad7])
CP14 = Room("Cave PLace #14", "There's nothing here but a light leading North, East, and West", 'CP9', None, 'CP15',
            'CP13', None, [player])
CP15 = Room("Cave PLace #15", "There's nothing here but a light leading North and West", 'CP10', None, None, 'CP14',
            None, [player, nirad8])
TREE = Room("Crystal Heart Tree", "You're standing in front of a big light tree and in its center it has a crystal "
                                  "heart", None, 'CP13', None, None, None, [player])

current_node = STATUE
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']
inventory = ['inventory']
character = ['character']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way")
    else:
        print('Command not recognized')
