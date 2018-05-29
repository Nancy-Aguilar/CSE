import time


def conprincipal():  # Talking with principal
    print("Principal: I'm glad that you were able to make it here on time I was just about to leave")
    time.sleep(1)
    print("You: Yeah, it would of been bad if you left, then I wouldn't be able to go anywhere around campus")
    time.sleep(1)
    print("Principal: That's true, here is my spare card, now don't lose it and bring it to me tomorrow morning")
    time.sleep(1)
    print("You: Ok I will, thanks for lending me your card this will really help me a lot")
    time.sleep(1)
    print("Principal: Your welcome and don't ruin the campus, we have school tomorrow")
    time.sleep(1)
    print("You: I won't, see you tomorrow morning then bye!")
    time.sleep(1)
    print("Principal: Bye")
    time.sleep(1)
    print("*The principal leaves*")


def narstatue():
    time.sleep(1)
    print("You: *looks at the tree statue* It looks like it's missing a center piece")
    time.sleep(1)
    print("You: Well it's time to get my powers back, now where should I go?")
    time.sleep(1)
    print("You: The Library seems like a good start")


def narstatue2():
    time.sleep(1)
    print("You: The crystal heart fitted! I have the key to the cave now")


def narlibrary():
    time.sleep(1)
    print("You: Come to think about it, this is my first time in the library")
    time.sleep(1)
    print("You: There's a book on the floor on the east side of the library I should go pick it up")


def narbse2():
    time.sleep(1)
    print("You: It's a book of legends, maybe it will give me clues to get my powers back")
    time.sleep(1)
    print("*shake shake* You: The shelf! It's opening?")
    time.sleep(1)
    print("You: It looks like a room in there, I should go check it out")


def narsecret2():
    time.sleep(1)
    print("You: There's a lot of dust in here, and it looks like a letter is on the ground")
    time.sleep(1)
    print("You: I should go back now")


def narbse1():
    time.sleep(1)
    print("You: I wonder if there are any books that could help me")
    time.sleep(1)
    print("You: *reads* All of these books are about math, english and regular class subjects, I don't need these")
    time.sleep(1)
    print("*shake shake* You: This shelf is opening!")
    time.sleep(1)
    print("You: There's a room in there, I should go in, a clue might be in there")


def narsecret1():
    time.sleep(1)
    print("You: This room is very dusty and there's nothing in here")
    time.sleep(1)
    print("You: I should go back now")


def ctrooms():
    time.sleep(1)
    print("You: There's nothing much in here but training equipment")
    time.sleep(1)
    print("You: I should go somewhere else")


def office():
    time.sleep(1)
    print("You: I wonder if there's something in here that I can use, hmm *sees flashlight* that might be useful")
    time.sleep(1)
    print("You: The Nurse's room is near here I should go check it out")


def nurseroom():
    time.sleep(1)
    print("You: There's a medkit on the desk")
    time.sleep(1)
    print("You: Nothing much is in here that could help I should go somewhere else")


def loungeroom():
    time.sleep(1)
    print("You: There's nothing much in here just sofas and tables")
    time.sleep(1)
    print("You: The cafeteria is close by I should go grab a snack")


def cafe():
    time.sleep(1)
    print("You: There's an apple on a table I should go grab it")
    time.sleep(1)
    print("You: It looks like there isn't any other food around here")
    time.sleep(1)
    print("You: I should go somewhere else now")


def dorms():
    time.sleep(1)
    print("You: People are in here, I should be quiet")
    time.sleep(1)
    print("You: There isn't really anything here that would help me I should move on")


def ptr():
    time.sleep(1)
    print("You: All the equipment are out, there isn't really anything here that can be useful")
    time.sleep(1)
    print("You: There's a station for creating things up ahead, maybe I should check it out")


def sfc():
    time.sleep(1)
    print("You: There's a crystal heart on the table")
    time.sleep(1)
    print("You: It looks like someone created it")


def classrooms():
    time.sleep(1)
    print("You: All the classrooms are closed, I should go somewhere else")


def weapon():
    time.sleep(1)
    print("You: There's a sword and a bow and arrow in here, these could be useful")
    time.sleep(1)


def caveplace1():
    time.sleep(1)
    print("You: There isn't a lot of light in here but I can still see")
    time.sleep(1)
    print("You: I hope I don't get lost")


def caveplace2():
    time.sleep(1)
    print("You: This looks like the same place as before")
    time.sleep(1)
    print("I should continue looking for the tree")


def caveplace3():
    time.sleep(1)
    print("You: A Nirad is here! I should attack it before it could attack me")


def thetree():
    time.sleep(1)
    print("You: I can't believe it the legend is true!")
    time.sleep(1)
    print("You: I can get my power back!")


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


class Keys(Item):
    def __init__(self, name, description):
        super(Keys, self).__init__(name, description)

    def collect(self):
        print("You collected %s key" % self.name)

    def drop(self):
        print("You dropped the %s" % self.name)


class Blackkey(Keys):
    def __init__(self, name, description):
        super(Blackkey, self).__init__(name, description, )

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


player = Character("Student 051603A", "You're a student attending Aurora Academy Of Magics, you lost your power,"
                                      "during a battle with the Nirads, now you're determined to get them back", 100,
                   0)

principal = Character("Principal", "Principal Rose helps run the school but the people who really run the school are"
                                   "the head councils, she's going to meet you at the statue to give you some help",
                      100, 100)

nirad = Character("Nirad", "A Nirad is a four armed monster these creatures are the reason your powers are gone, "
                           "you over used them trying to defeat them", 100, 0)


# Character ends


class Room(object):
    def __init__(self, name, description, north, south, east, west, items, characters):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.items = items
        self.characters = characters
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

    def move(self, direction):
        player.location = globals()[getattr(self, direction)]


Sword = Sword('sword', 'the blade of the sword is covered in fire', 20)

BowArrow = BowArrow('bow and arrow', 'shoots are always precise', 20)

Blackkey = Blackkey('black Key', 'Their are some words engraved on the key')

Dormkey = Dormkey('dorm Key', 'The key to your dorm #16')

Schoolkey = Schoolkey('spare Key', 'this key can open an door on campus except the dorms')

Apple = Apple('apple', 'red and delicious')

Medkit = Medkit('medkit', 'Contains bandages, rubbing alcohol, and pain killers')

Flashlight = Flashlight('flashlight', 'Shines very bright in the dark')

Pants = Pants('pants', 'color of the pants are black')

Sweater = Sweater('hoodie', 'color of the hoodie is grey')

Bookoflegends = Bookoflegends('Book Of Legends', 'Legend says that there is a special tree hidden within a cave, it is '
                                                 'the source of magic, and those who have lost their powers can get '
                                                 'them back by touching the tree.')

Sorry = Sorry('Student 051603A', 'We have been informed that you have lost your magical abilities during the battle \n'
                                 'against the Nirads and you have requested to find a way to return your abilities. '
                                 'The head council have granted you permission to let you use the campus as needed.')

TheTree = TheTree('letter', 'The tree is real, and this school is the key to it, the tree statue holds the key to \n '
                            'the cave that the weapon rooms hides, and the cave is not an easy task to get through, '
                            'but \n it was worth it if it meant getting my abilities back')

Crystalheart = Crystalheart('crystal heart', 'A median sized crystal heart that shines very bright')

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
SECRET1 = Room("Secret Room #1", "You're inside a secret room and there is nothing in here", None, None, 'BSE1', None,
               None, [player])
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
NURSE = Room("Nurse's Room", "You're inside the Nurse's room and facing North is the lounge room and facing West is "
                             "the office", 'LOUNGE', None, None, 'OFFICE', [Medkit],
             [player])
LOUNGE = Room("Lounge Room", "You're at the lounge room and there are many places to sit, facing West is the "
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
                                  "North and facing East is the weapon room", 'CREATION', 'DORMS4', 'WEAPON', None,
           None, [player])
CREATION = Room("Creation Table", "You're standing in front of a table that has a crystal heart on top of it", None,
                'PTR', 'WEAPON', None, [Crystalheart], [player])
WEAPON = Room("Weapon Room", "You're inside the weapon room, there's a sword and bow and arrow on a table and there is "
                             "an entrance to a cave but it's locked and facing South are the classrooms", None,
              'CLASS', 'CP1', 'PTR', [Sword, BowArrow], [player])
CLASS = Room("Classroom", "You're inside the classrooms and all the rooms are locked, facing North is the weapon room",
             'WEAPON', 'CT4', None, None, None, [player])
CP1 = Room("Cave Place #1", "You're inside the cave and people say that there are many dangerous things inside and "
                            "multiple places in the cave, there's a light leading South and East", None, 'CP7', 'CP2',
           'WEAPON', None, [player])
CP2 = Room("Cave PLace #2", "There's a light leading East, South, and West", None, 'CP8', 'CP3',
           'CP1', None, [player, nirad])
CP3 = Room("Cave PLace #3", "There's a light leading East, South, and West", None, 'CP6', 'CP4',
           'CP2', None, [player])
CP4 = Room("Cave PLace #4", "There's a light leading East, South, and West", None, 'CP9', 'CP5', 'CP3',
           None, [player])
CP5 = Room("Cave PLace #5", "There's a light leading South and West", None, 'CP10', None, 'CP4', None,
           [player, nirad])
CP6 = Room("Cave PLace #6", "There's a light leading North", 'CP3', None, None, None, None,
           [player, nirad])
CP7 = Room("Cave PLace #7", "There's a light leading North, South, and East", 'CP1', 'CP11', 'CP8',
           None, None, [player])
CP8 = Room("Cave PLace #8", "There's a light leading North, South, and West", 'CP2', 'CP12', None,
           'CP7', None, [player, nirad])
CP9 = Room("Cave PLace #9", "There's a light leading North, South, and East", 'CP4', 'CP14', 'CP10',
           None, None, [player, nirad])
CP10 = Room("Cave PLace #10", "There's a light leading North, South, and West", 'CP5', 'CP15', None,
            'CP9', None, [player])
CP11 = Room("Cave PLace #11", "There's a light leading North and East", 'CP7', None, 'CP12', None,
            None, [player, nirad])
CP12 = Room("Cave PLace #12", "There's a light leading North, East, and West", 'CP8', None, 'CP13',
            'CP11', None, [player])
CP13 = Room("Cave PLace #13", "There's a light leading North, East, and West", 'TREE', None, 'CP14',
            'CP12', None, [player, nirad])
CP14 = Room("Cave PLace #14", "There's a light leading North, East, and West", 'CP9', None, 'CP15',
            'CP13', None, [player])
CP15 = Room("Cave PLace #15", "There's a light leading North and West", 'CP10', None, None, 'CP14',
            None, [player, nirad])
TREE = Room("Crystal Heart Tree", "You're standing in front of a big light tree and in its center it has a crystal "
                                  "heart that's sparkling", None, 'CP13', None, None, None, [player])

player.location = STATUE
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']

while True:
    if player.location == STATUE and player.first_time_STATUE is True:
        conprincipal()
        time.sleep(1)
        narstatue()
    player.first_time_STATUE = False

    if player.location == STATUE and player.first_time_STATUE is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == STATUE and Blackkey in player.inventory:
        narstatue2()

    if player.location == LIBRARY and player.first_time_LIBRARY is True:
        narlibrary()
        time.sleep(1)
        player.first_time_LIBRARY = False

    if player.location == LIBRARY and player.first_time_LIBRARY is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == BSE2 and player.first_time_BSE2 is True:
        narbse2()
        time.sleep(1)
        player.first_time_BSE2 = False

    if player.location == BSE2 and player.first_time_BSE2 is False:
        print(player.location.name)
        print("There are many books on the shelf")

    if player.location == SECRET2 and player.first_time_SECRET2 is True:
        narsecret2()
        time.sleep(1)
        player.first_time_SECRET2 = False

    if player.location == SECRET2 and player.first_time_SECRET2 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == BSE1 and player.first_time_BSE1 is True:
        narbse1()
        time.sleep(1)
        player.first_time_BSE1 = False

    if player.location == BSE1 and player.first_time_BSE1 is False:
        print(player.location.name)
        print("There are many books on the shelf")

    if player.location == SECRET1 and player.first_time_SECRET1 is True:
        narsecret1()
        time.sleep(1)
        player.first_time_SECRET1 = False

    if player.location == SECRET1 and player.first_time_SECRET1 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == CT1 and player.first_time_CT1 is True:
        ctrooms()
        time.sleep(1)
        player.first_time_CT1 = False

    if player.location == CT1 and player.first_time_CT1 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == CT2 and player.first_time_CT2 is True:
        ctrooms()
        time.sleep(1)
        player.first_time_CT2 = False

    if player.location == CT2 and player.first_time_CT2 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == CT3 and player.first_time_CT3 is True:
        ctrooms()
        time.sleep(1)
        player.first_time_CT3 = False

    if player.location == CT3 and player.first_time_CT3 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == CT4 and player.first_time_CT4 is True:
        ctrooms()
        time.sleep(1)
        player.first_time_CT4 = False

    if player.location == CT4 and player.first_time_CT4 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == DORMS1 and player.first_time_DORMS1 is True:
        dorms()
        time.sleep(1)
        player.first_time_DORMS1 = False

    if player.location == DORMS1 and player.first_time_DORMS1 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == DORMS2 and player.first_time_DORMS2 is True:
        dorms()
        time.sleep(1)
        player.first_time_DORMS2 = False

    if player.location == DORMS2 and player.first_time_DORMS2 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == DORMS3 and player.first_time_DORMS3 is True:
        dorms()
        time.sleep(1)
        player.first_time_DORMS3 = False

    if player.location == DORMS3 and player.first_time_DORMS3 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == DORMS4 and player.first_time_DORMS4 is True:
        dorms()
        time.sleep(1)
        player.first_time_DORMS4 = False

    if player.location == DORMS4 and player.first_time_DORMS4 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == OFFICE and player.first_time_OFFICE is True:
        office()
        time.sleep(1)
        player.first_time_OFFICE = False

    if player.location == OFFICE and player.first_time_OFFICE is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == NURSE and player.first_time_NURSE is True:
        nurseroom()
        time.sleep(1)
        player.first_time_NURSE = False

    if player.location == NURSE and player.first_time_NURSE is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == LOUNGE and player.first_time_LOUNGE is True:
        loungeroom()
        time.sleep(1)
        player.first_time_LOUNGE = False

    if player.location == LOUNGE and player.first_time_LOUNGE is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == CAFE and player.first_time_CAFE is True:
        cafe()
        time.sleep(1)
        player.first_time_CAFE = False

    if player.location == CAFE and player.first_time_CAFE is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == PTR and player.first_time_PTR is True:
        ptr()
        time.sleep(1)
        player.first_time_PTR = False

    if player.location == PTR and player.first_time_PTR is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == CREATION and player.first_time_CREATION is True:
        sfc()
        time.sleep(1)
        player.first_time_CREATION = False

    if player.location == CREATION and player.first_time_CREATION is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == CLASS and player.first_time_CLASS is True:
        classrooms()
        time.sleep(1)
        player.first_time_CLASS = False

    if player.location == CLASS and player.first_time_CLASS is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == WEAPON and player.first_time_WEAPON is True:
        weapon()
        time.sleep(1)
        player.first_time_WEAPON = False

    if player.location == WEAPON and player.first_time_WEAPON is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == CP1 and player.first_time_CP1 is True and Blackkey in player.inventory:
        caveplace1()
        time.sleep(1)
        player.first_time_CP1 = False

    if player.location == CP1 and player.first_time_CP1 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == CP1 and player.first_time_CP1 is True and Blackkey not in player.inventory:
        print("You need to key to enter the cave")

    if player.location == CP2 and player.first_time_CP2 is True:
        caveplace3()
        time.sleep(1)
        player.first_time_CP2 = False

    if player.location == CP2 and player.first_time_CP2 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == CP3 and player.first_time_CP3 is True:
        caveplace1()
        time.sleep(1)
        player.first_time_CP3 = False

    if player.location == CP3 and player.first_time_CP3 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == CP4 and player.first_time_CP4 is True:
        caveplace1()
        time.sleep(1)
        player.first_time_CP4 = False

    if player.location == CP4 and player.first_time_CP4 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == CP5 and player.first_time_CP5 is True:
        nirad.health = 100
        caveplace3()
        time.sleep(1)
        player.first_time_CP5 = False


    if player.location == CP5 and player.first_time_CP5 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == CP6 and player.first_time_CP6 is True:
        nirad.health = 100
        caveplace3()
        time.sleep(1)
        player.first_time_CP6 = False

    if player.location == CP6 and player.first_time_CP6 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == CP7 and player.first_time_CP7 is True:
        caveplace1()
        time.sleep(1)
        player.first_time_CP7 = False

    if player.location == CP7 and player.first_time_CP7 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == CP8 and player.first_time_CP8 is True:
        nirad.health = 100
        caveplace3()
        time.sleep(1)
        player.first_time_CP8 = False

    if player.location == CP8 and player.first_time_CP8 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == CP9 and player.first_time_CP9 is True:
        nirad.health = 100
        caveplace3()
        time.sleep(1)
        player.first_time_CP9 = False

    if player.location == CP9 and player.first_time_CP9 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == CP10 and player.first_time_CP10 is True:
        caveplace1()
        time.sleep(1)
        player.first_time_CP10 = False

    if player.location == CP10 and player.first_time_CP10 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == CP11 and player.first_time_CP11 is True:
        nirad.health = 100
        caveplace3()
        time.sleep(1)
        player.first_time_CP11 = False

    if player.location == CP11 and player.first_time_CP11 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == CP12 and player.first_time_CP12 is True:
        caveplace1()
        time.sleep(1)
        player.first_time_CP12 = False

    if player.location == CP12 and player.first_time_CP12 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == CP13 and player.first_time_CP13 is True:
        nirad.health = 100
        caveplace3()
        time.sleep(1)
        player.first_time_CP13 = False

    if player.location == CP13 and player.first_time_CP13 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == CP14 and player.first_time_CP14 is True:
        caveplace1()
        time.sleep(1)
        player.first_time_CP14 = False

    if player.location == CP14 and player.first_time_CP14 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == CP15 and player.first_time_CP15 is True:
        nirad.health = 100
        caveplace3()
        time.sleep(1)
        player.first_time_CP15 = False

    if player.location == CP15 and player.first_time_CP15 is False:
        print(player.location.name)
        print(player.location.description)

    if player.location == TREE:
        thetree()
        time.sleep(1)
        print(player.location.name)
        print(player.location.description)

    command = input('>_').lower()
    if command == 'quit':
        quit()
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            player.location.move(command)
        except KeyError:
            print("You cannot go this way")

    elif 'collect' in command:
        collect_name = command[8:]
        found = None
        for item in player.location.items:
            if collect_name == item.name.lower():
                player.collect(item)
                found = item
        if found is None:
            print("There isn't anything to collect")
        else:
            player.location.items.remove(found)

    elif 'remove' in command:
        remove_name = command[7:]
        remove = None
        for item in player.inventory:
            if remove_name == item.name.lower():
                player.remove(item)
                player.location.items.append(item)
                drop = item

    elif 'cut' in command:
        if Sword in player.inventory:
            player.cut(nirad)
        else:
            print("You don't have a weapon in your inventory")

    elif 'eat' in command:
        if Apple in player.inventory:
                player.eat(apple=Apple)
                player.inventory.remove(Apple)

        else:
            print("You have nothing to eat")

    elif 'attack' in command:
        attack_nirad = command[7:]
        if player.location == CP2 and Sword in player.inventory:
            player.attack(nirad)
            nirad.health -= 20
            if nirad.health == 0:
                print("The Nirad is dead")

        if nirad.location == CP2 and BowArrow in player.inventory:
            player.attack(nirad)
            nirad.health -= 20
            if nirad.health == 0:
                print("The Nirad is dead")

        if player.location == CP5 and Sword in player.inventory:
            player.attack(nirad)
            nirad.health -= 20
            if nirad.health == 0:
                print("The Nirad is dead")

        if nirad.location == CP5 and BowArrow in player.inventory:
            player.attack(nirad)
            nirad.health -= 20
            if nirad.health == 0:
                print("The Nirad is dead")

        if player.location == CP6 and Sword in player.inventory:
            player.attack(nirad)
            nirad.health -= 20
            if nirad.health == 0:
                print("The Nirad is dead")

        if nirad.location == CP6 and BowArrow in player.inventory:
            player.attack(nirad)
            nirad.health -= 20
            if nirad.health == 0:
                print("The Nirad is dead")

        if player.location == CP8 and Sword in player.inventory:
            player.attack(nirad)
            nirad.health -= 20
            if nirad.health == 0:
                print("The Nirad is dead")

        if nirad.location == CP8 and BowArrow in player.inventory:
            player.attack(nirad)
            nirad.health -= 20
            if nirad.health == 0:
                print("The Nirad is dead")

        if player.location == CP9 and Sword in player.inventory:
            player.attack(nirad)
            nirad.health -= 20
            if nirad.health == 0:
                print("The Nirad is dead")

        if nirad.location == CP9 and BowArrow in player.inventory:
            player.attack(nirad)
            nirad.health -= 20
            if nirad.health == 0:
                print("The Nirad is dead")

        if player.location == CP11 and Sword in player.inventory:
            player.attack(nirad)
            nirad.health -= 20
            if nirad.health == 0:
                print("The Nirad is dead")

        if nirad.location == CP11 and BowArrow in player.inventory:
            player.attack(nirad)
            nirad.health -= 20
            if nirad.health == 0:
                print("The Nirad is dead")

        if player.location == CP13 and Sword in player.inventory:
            player.attack(nirad)
            nirad.health -= 20
            if nirad.health == 0:
                print("The Nirad is dead")

        if nirad.location == CP13 and BowArrow in player.inventory:
            player.attack(nirad)
            nirad.health -= 20
            if nirad.health == 0:
                print("The Nirad is dead")

        if player.location == CP15 and Sword in player.inventory:
            player.attack(nirad)
            nirad.health -= 20
            if nirad.health == 0:
                print("The Nirad is dead")

        if nirad.location == CP15 and BowArrow in player.inventory:
            player.attack(nirad)
            nirad.health -= 20
            if nirad.health == 0:
                print("The Nirad is dead")

    elif 'put' in command:
        if player.location == STATUE and Crystalheart in player.inventory:
            player.put(Crystalheart)
            player.inventory.append(Blackkey)
            player.inventory.remove(Crystalheart)
            print("You collected the Black key")
        else:
            print("You have nothing to put")

    elif 'touch' in command:
        if player.location == TREE:
            player.touch()
            print("You did it, now you can go to school with your abilities back :)")
            print("You finished the game!")
            quit()

    elif 'read book' in command:
        if Bookoflegends in player.inventory:
            print(Bookoflegends.description)
        else:
            print("You have nothing to read")

    elif 'read letter' in command:
        if TheTree in player.inventory:
            print(TheTree.description)
        else:
            print("You have nothing to read")

    elif 'use' in command:
        if Medkit in player.inventory:
            player.use()
            player.health += 100

    else:
        print('Command not recognized')