# import statements
# class definitions
# start with items to put in rooms
# then with characters
# and then finally the rooms
# instantiate
# controller (change controller)


class Item(object):
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


Sword = Sword('Hinoken', 'the blade of the sword is covered in fire', 40)
Sword.stab()
Sword.cut()


class BowArrow(Weapon):
    def __init__(self, name, description, power):
        super(BowArrow, self).__init__(name, description)
        self.power = power

    def shoot(self):
        print("You shot an arrow with %s" % self.name)


BowArrow = BowArrow('Seimitsuna shotto', 'shoots are always precise', 29)
BowArrow.shoot()


class Axe(Weapon):
    def __init__(self, name, description, power):
        super(Axe, self).__init__(name, description)
        self.power = power

    def swing(self):
        print("You swing the %s" % self.name)


Axe = Axe('Ono', 'small but durable', 25)
Axe.swing()


class Keys(Item):
    def __init__(self, name, description):
        super(Keys, self).__init__(name, description)

    def collect(self):
        print("You collected %s key" % self.name)

    def drop(self):
        print("You dropped the %s" % self.name)


class Blackkey(Keys):
    def __init__(self, name, description, room):
        super(Blackkey, self).__init__(name, description,)
        self.room = room

    def insert(self):
        print("You insert the %s" % self.name)


Blackkey = Blackkey('Black Key', 'Their are some words engraved on the key', 'CAVE')
Blackkey.insert()


class Dormkey(Keys):
    def __init__(self, name, description, room):
        super(Dormkey, self).__init__(name, description)
        self.room = room

    def insert(self):
        print("You insert the %s" % self.name)


Dormkey = Dormkey('Dorm Key', 'The key to your dorm #16', 'DORMS1')
Dormkey.insert()


class Materials(Item):
    def __init__(self, name, description):
        super(Materials, self).__init__(name, description)

    def collect(self):
        print(" You collected %s" % self.name)


class Carbon(Materials):
    def __init__(self, name, description):
        super(Carbon, self).__init__(name, description)

    def pressure(self):
        print("You put pressure on the %s and it turned into a diamond" % self.name)


Carbon = Carbon('Carbon', 'A median size chunck of Carbon')
Carbon.pressure()


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


Apple = Apple('Apple', 'red and delicious')
Apple.eat()


class Medkit(Consumables):
    def __init__(self, name, description):
        super(Medkit, self).__init__(name, description)

    def use(self):
        print("You use the %s" % self.name)


Medkit = Medkit('Medkit', 'Contains bandages, rubbing alcohol, and pain killers')
Medkit.use()


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


Flashlight = Flashlight('Flashlight', 'Shines very bright in the dark')
Flashlight.turn_on()
Flashlight.turn_off()


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


Pants = Pants('Pants', 'color of the pants are black')
Pants.put_on()
Pants.take_off()


class Sweater(Cloths):
    def __init__(self, name, description):
        super(Sweater, self).__init__(name, description)

    def put_on(self):
        print("You put on %s" % self.name)

    def take_off(self):
        print("You take off %s" % self.name)


Sweater = Sweater('Hoodie', 'color of the hoodie is grey')
Sweater.put_on()
Sweater.take_off()


class Book(Item):
    def __init__(self, name, description):
        super(Book, self).__init__(name, description)

    def collect(self):
        print("You collected %s " % self.name)

    def drop(self):
        print("You dropped %s" % self.name)


class Bookofpotions(Book):
    def __init__(self, name, description):
        super(Bookofpotions, self).__init__(name, description)

    def open(self):
        print("You opened the %s" % self.name)

    def read(self):
        print("The book says %s" % self.description)

    def close(self):
        print("You close the %s" % self.name)


Bookofpotions = Bookofpotions('Book Of Potions', 'Contains many potions to do many things')
Bookofpotions.open()
Bookofpotions.read()
Bookofpotions.close()


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


Sorry = Sorry('Student 051603A', 'We have been informed that you have lost your magical abilities during the battle '
                                 'against the Nirads and you have requested to find a way to return your abilities. The'
                                 'head council have granted you permission to let you use the campus as needed.')
Sorry.open()
Sorry.read()


class TheTree(Letters):
    def __init__(self, name, description):
        super(TheTree, self).__init__(name, description)

    def open(self):
        print("You open the %s" % self.name)

    def read(self):
        print("The letter says %s" % self.description)


TheTree = TheTree('The Tree', 'The tree is real, they said it was not but it is real. It was not easy to find it and '
                              'journey was tough but it was worth it, if it meant getting my abilities back.')
TheTree.open()
TheTree.read()


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

####
# Characters
####


class Room(object):
    def __init__(self, name, description, north, south, east, west):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# north, south, east, west
# Initialize Rooms
STATUE = Room("Tree Statue", "You're standing next to a tree statue, it appears to missing a heart shaped object in "
                             "its center, up North is the Library", 'LIBRARY', None, None, None)
LIBRARY = Room("Library", "You're inside the library, standing in the center and their are two book shelves on the "
                          "West and East side of the library, up North is Combat Training room 1", 'CT1', 'STATUE',
               'BSE2', 'BSE1')
BSE1 = Room("Book shelves", "You approached the book shelves and they suddenly moved to reveal a secret room", None,
            None, 'LIBRARY', 'SECRET1')
BSE2 = Room("Book shelves", "You approached the book shelves and they suddenly moved to reveal a secret room", None,
            None, 'SECRET2', 'LIBRARY')
SECRET1 = Room("Secret Room #1", "You're inside a secret room and the only thing in there is a dusty old book on the "
                                 "ground", None, None, 'BSE1', None)
SECRET2 = Room("Secret Room #2", "You're inside a secret room and the only thing in there is letter on the ground",
               None, None, None, 'BSE2')
CT1 = Room("Combat Training Room #1", "You're inside the training room for 1st years, facing West is the training room "
                                      "for 3rd years, facing East is the training room for 2nd years, and North is the "
                                      "training room for 4th years", 'CT4', 'LIBRARY', 'CT2', 'CT3')
CT2 = Room("Combat Training Room #2", "You're inside the combat training room for 2nd years, on the East side is the "
                                      "office and on the West side is the combat training room for 1st years", None,
           None, 'OFFICE', 'CT1')
CT3 = Room("Combat Training Room #3", "You're inside the combat training room for 3rd years, on the East side is the "
                                      "combat training room for 1st years, on the West side are the dorms for 1st "
                                      "years", None, None, 'CT1', 'DORMS1')
CT4 = Room("Combat Training Room #4", "You're inside the combat training room for 4th years and up North are the "
                                      "classrooms", 'CLASS', 'CT1', None, None)
OFFICE = Room("Office", "You're inside the office and facing East is the Nurse's room and facing West is the training "
                        "room for 2nd years", None, None, 'NURSE', 'CT2')
NURSE = Room("Nurse's Room", "You're inside the Nurse's room and facing East is the Nurse's room and facing North is "
                             "the lounge room and facing West is the office", 'LOUNGE', None, None, 'OFFICE')
LOUNGE = Room("Lounge Room", "You're at the lounge room and there is a bag of carbon on a sofa, facing West is the "
                             "Cafeteria", None, 'NURSE', None, 'CAFE')
CAFE = Room("Cafeteria", "You're inside the Cafeteria with many tables and chairs and some food trays. Facing East is "
                         "the lounge room", None, None, 'LOUNGE', None)
DORMS1 = Room("Dorms for 1st years", "You're inside a dorm building, all the rooms are closed and facing North are "
                                     "the 2nd year dorms", 'DORMS2', None, 'CT3', None)

DORMS2 = Room("Dorms for 2nd years", "You're inside a dorm building, all the rooms are closed and facing North are "
                                     "the 3rd year dorms", 'DORMS3', 'DORMS1', None, None)
DORMS3 = Room("Dorms for 3rd years", "You're inside a dorm building, all the rooms are closed and facing North are "
                                     "the 4th year dorms", 'DORMS4', 'DORMS2', None, None)

DORMS4 = Room("Dorms for 4th years", "You're inside a dorm building, all the rooms are closed and facing North is "
                                     "the power training room", 'PTR', 'DORMS3', None, None)
PTR = Room("Power Training Room", "You're in the power training room and their's a station for creating items up "
                                  "North and facing East is the weapon room", 'CREATION', 'DORMS4', 'WEAPON', None)
CREATION = Room("Creation Table", "You're standing in front of a table that has four potions, you can create anything "
                                  "you want with the right materials, facing East is the weapon room", None, 'DORMS4',
                'WEAPON', None)
WEAPON = Room("Weapon Room", "You're inside the weapon room, there's a sword and bow/arrow on a table and there is an "
                             "entrance to a cave but it's locked and facing South are the classrooms", None, 'CLASS',
              'CP1', 'PTR')
CLASS = Room("Classroom", "You're inside the classrooms and all the rooms are locked, facing North is the weapon room",
             'WEAPON', 'CT4', None, None)
CP1 = Room("Cave Place #1", "You're inside the cave and people say that there are many dangerous things inside and "
                            "multiple places in the cave, there's a light leading South and East", None, 'CP7', 'CP2',
           'WEAPON')
CP2 = Room("Cave PLace #2", "There's nothing here but a light leading East, South, and West", None, 'CP8', 'CP3',
           'CP1')
CP3 = Room("Cave PLace #3", "There's nothing here but a light leading East, South, and West", None, 'CP6', 'CP4',
           'CP2')
CP4 = Room("Cave PLace #4", "There's nothing here but a light leading East, South, and West", None, 'CP9', 'CP5', 'CP3')
CP5 = Room("Cave PLace #5", "There's nothing here but a light leading South and West", None, 'CP10', None, 'CP4')
CP6 = Room("Cave PLace #6", "There's nothing here but a light leading North", 'CP3', None, None, None)
CP7 = Room("Cave PLace #7", "There's nothing here but a light leading North, South, and East", 'CP1', 'CP11', 'CP8',
           None)
CP8 = Room("Cave PLace #8", "There's nothing here but a light leading North, South, and West", 'CP2', 'CP12', None,
           'CP7')
CP9 = Room("Cave PLace #9", "There's nothing here but a light leading North, South, and East", 'CP4', 'CP14', 'CP10',
           None)
CP10 = Room("Cave PLace #10", "There's nothing here but a light leading North, South, and West", 'CP5', 'CP15', None,
            'CP9')
CP11 = Room("Cave PLace #11", "There's nothing here but a light leading North and East", 'CP7', None, 'CP12', None)
CP12 = Room("Cave PLace #12", "There's nothing here but a light leading North, East, and West", 'CP8', None, 'CP13',
            'CP11')
CP13 = Room("Cave PLace #13", "There's nothing here but a light leading North, East, and West", 'TREE', None, 'CP14',
            'CP12')
CP14 = Room("Cave PLace #14", "There's nothing here but a light leading North, East, and West", 'CP9', None, 'CP15',
            'CP13')
CP15 = Room("Cave PLace #15", "There's nothing here but a light leading North and West", 'CP10', None, None, 'CP14')
TREE = Room("Crystal Heart Tree", "You're standing in front of a big light tree and in its center it has a crystal "
                                  "heart", None, 'CP13', None, None)

current_node = STATUE
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']

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