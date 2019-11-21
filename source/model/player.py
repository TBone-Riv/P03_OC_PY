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
        self.is_win = bool(all([item in self.list_item for item in list_item]))