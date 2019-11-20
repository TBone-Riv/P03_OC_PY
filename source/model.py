#! /usr/bin/env python3
# coding: utf-8
"""Model module"""


from random import randint, choice


class Player:
    """Core object from model"""

    def __init__(self, list_item: list):

        # Variable iterable related
        self.list_item = []
        self.index = 0

        # Initialise labyrinth
        self.labyrinth = Labyrinth()
        self.box_position = None
        self.set_labyrinth(list_item)
        self.set_position()

        # Win condition
        self.is_win = None

    # Iterable related method
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        try:
            result = self.list_item[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

    def set_labyrinth(self, list_item):
        """Set random position for all item"""
        while 1:
            box = choice(choice(self.labyrinth.matrix))
            if box.is_valid:
                box.content = Guardian('guardian', list_item)
                break

        for item in list_item:
            while 1:
                box = choice(choice(self.labyrinth.matrix))
                if box.is_valid:
                    box.content = item
                    break

    def set_position(self):
        """Set random position for player"""
        line, column = self.labyrinth.get_valid_box()
        self.box_position = [line, column]

    def append(self, item):
        """Add object to iterable variable and remove it from labyrinth"""
        # Confirm that method is call by an Item
        if not isinstance(item, Item):
            raise TypeError("item is not of type 'Item'")

        # Adding item to the list and remove it from the matrix
        self.list_item.append(item)
        self.labyrinth.matrix[self.box_position[0]][self.box_position[1]].content = None

    def move_to(self, direction):
        """Handle player movement"""
        if self.labyrinth.valid_move(self.box_position, direction):
            if direction == 'north':
                self.box_position[0] += -1
            elif direction == 'south':
                self.box_position[0] += 1
            elif direction == 'east':
                self.box_position[1] += 1
            else:
                self.box_position[1] += -1

        # Call "Box.event" method if exist
        self.labyrinth.event(self, self.box_position)

    def win_event(self, list_item):
        """Check win condition"""
        # Check if itch guardian list element are in player list
        condition = all([item in self.list_item for item in list_item])
        self.is_win = True if condition else False


class ActorMixin:
    """Mixin class for all actor-like object"""

    def __init__(self, name: str):
        self.name = name

    def event(self, *args, **kwargs):
        """Need to be overridden to call different Player methods in different condition"""
        raise AttributeError("'event' class is not overridden wive {}".format(type(self)))


class Item(ActorMixin):
    """Collectible item"""

    def event(self, player):
        player.append(self)


class Guardian(ActorMixin):
    """Actor handling win condition"""

    def __init__(self, name: str, list_item: list):
        super().__init__(name)
        self.list_item = list_item

    def event(self, player):
        player.win_event(self.list_item)


class Box:
    """Define structure of labyrinth"""

    def __init__(self, north=False, south=False, east=False, west=False):

        self.north = north
        self.south = south
        self.east = east
        self.west = west

        self.content = None

    @property
    def is_valid(self):
        """Return True if box is accessible and empty"""
        # Check if box is accessible and empty
        return any([self.north, self.south, self.east, self.west]) and self.content is None


class Labyrinth:
    """Decrypt and stock the structure of labyrinth"""

    def __init__(self, file="./resource/labyrinth"):

        self.file = file
        self.matrix = []

        self.build()

    def build(self):
        """Build labyrinth from an external file"""

        key = {"□": [],
               "←": ["west"],
               "↑": ["north"],
               "→": ["east"],
               "↓": ["south"],
               "━": ["west", "east"],
               "┃": ["north", "south"],
               "┏": ["south", "east"],
               "┓": ["south", "west"],
               "┗": ["north", "east"],
               "┛": ["north", "west"],
               "┣": ["north", "south", "east"],
               "┫": ["north", "south", "west"],
               "┳": ["south", "west", "east"],
               "┻": ["north", "west", "east"],
               "╋": ["north", "south", "west", "east"]
               }

        with open(self.file, 'r', errors='ignore', encoding="UTF8") as file:
            read_lab = file.read()

        for wall_line in read_lab.split('\n'):
            list_wall = []

            for wall in wall_line:
                list_wall.append(Box(**{k: True for k in key[wall]}))

            self.matrix.append(list_wall)

    def get_valid_box(self):
        """Return random box coordinate """

        # Check if an accessible box exist
        if [[x.is_valid for x in y] for y in self.matrix] ==\
                [[False for _ in y] for y in self.matrix]:
            raise Exception('No valid Box')

        # Get a first random box coordinate
        line = randint(0, len(self.matrix) - 1)
        column = randint(0, len(self.matrix[line]) - 1)

        # Repeat the accusation while box isn't accessible
        while not self.matrix[line][column].is_valid:
            line = randint(0, len(self.matrix) - 1)
            column = randint(0, len(self.matrix[line]) - 1)

        return line, column

    def valid_move(self, box_position, direction):
        """Check cardinal movement"""
        return getattr(self.matrix[box_position[0]][box_position[1]], direction)

    def event(self, player, box_position):
        """Call "Box.event" method if exist"""
        if self.matrix[box_position[0]][box_position[1]].content is not None:
            self.matrix[box_position[0]][box_position[1]].content.event(player)
