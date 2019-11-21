from random import randint
from source.model.box import Box
import source.constants as constants


class Labyrinth:
    """Decrypt and stock the structure of labyrinth"""

    def __init__(self, file="./resource/labyrinth"):

        self.file = file
        self.matrix = []

        self.build()

    def get_box(self, line, column):
        """Take coordinate and return a box"""
        return self.matrix[line][column]

    def set_box_content(self, line, column, content):
        """Take coordinate and a content to assign to a box"""
        self.get_box(line, column).content = content

    def emptying_box(self, line, column):
        """Take coordinate and set a box content to None"""
        self.get_box(line, column).content = None

    def get_valid_matrix(self, is_false=False):
        """Return a matrix with a boolean for each box"""
        # return a matrix of False if is_false is True
        return [[x.is_valid if not is_false else False for x in y] for y in self.matrix]

    def get_random_coordinate(self):
        """Return random coordinate"""
        line = randint(0, len(self.matrix) - 1)
        column = randint(0, len(self.matrix[line]) - 1)
        return line, column

    def build(self):
        """Build labyrinth from an external file"""

        key = constants.KEY

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
        if self.get_valid_matrix() == self.get_valid_matrix(is_false=True):
            raise Exception('No valid Box')

        # Get a first random box coordinate
        line, column = self.get_random_coordinate()

        # Repeat the accusation while box isn't accessible
        while not self.get_box(line, column).is_valid:
            line, column = self.get_random_coordinate()

        return line, column

    def get_valid_move(self, line, column, direction):
        """Check cardinal movement"""
        return self.get_box(line, column).get_direction(direction)

    def event(self, player, box_position):
        """Call "Box.event" method if exist"""
        if self.matrix[box_position[0]][box_position[1]].content is not None:
            self.matrix[box_position[0]][box_position[1]].content.event(player)
