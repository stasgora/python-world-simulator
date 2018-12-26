from ..Plant import Plant
from ..Animal import Animal


class SosnowskyHogweed(Plant):

    def __init__(self, strength, initiative, symbol, position, world, color):
        super(SosnowskyHogweed, self).__init__(strength, initiative, symbol, position, world, color)

    def die(self, aggressor):
        super(SosnowskyHogweed, self).die(aggressor)
        if aggressor.get_symbol() != 'X':
            self._world.kill(self, aggressor)

    def action(self):
        super(SosnowskyHogweed, self).action()
        neighbours = self._world.get_map().get_neighbours(self._position)
        for creature in neighbours:
            if Animal.is_animal(creature.get_symbol()) and 'X' != creature.get_symbol() != self._symbol:
                self._world.kill(self, creature)
