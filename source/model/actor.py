class ActorMixin:
    """Mixin class for all actor-like object"""

    def __init__(self, name: str):
        self.name = name

    def event(self, player):
        """Need to be overridden to call different Player methods in different condition"""
        raise NotImplemented("'event' class is not overridden with {}".format(type(self)))


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
