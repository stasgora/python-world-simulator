from ..Animal import Animal
from random import random


class Antelope(Animal):

    ESCAPE_CHANCE = 0.5

    def __init__(self, strength, initiative, symbol, position, world, color):
        super(Antelope, self).__init__(strength, initiative, symbol, position, world, color)
        self._range = 2

    def defend(self, aggressor):
        if random() > Antelope.ESCAPE_CHANCE:
            return False
        new_pos = self._world.get_map().get_pos_nearby(self._position, False, 1)
        if new_pos is None:
            return False
        self.move(new_pos)
        return True
