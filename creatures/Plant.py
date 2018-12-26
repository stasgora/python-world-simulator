from .Creature import Creature
from random import random


class Plant(Creature):

    SPREAD_CHANCE = 0.1

    def __init__(self, strength, initiative, symbol, position, world, color):
        super(Plant, self).__init__(strength, initiative, symbol, position, world, color)

    def action(self):
        super(Plant, self).action()
        self.spread()

    def spread(self):
        if not self._mature or self._mated or random() > Plant.SPREAD_CHANCE:
            return
        seed_pos = self._world.get_map().get_pos_nearby(self._position)
        if seed_pos is None or self._world.get_map().get(seed_pos) is not None:
            return
        self.mate()
        self._world.give_birth(self._symbol, seed_pos)

    @staticmethod
    def is_animal(symbol):
        return symbol == 'J' or symbol == 'T' or symbol == 'G' or symbol == 'M' or symbol == 'B'

    @staticmethod
    def get_names():
        return ["Belladonna", "Grass", "Guarana", "Sonchus", "SosnowskyHogweed"]
