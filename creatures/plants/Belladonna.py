from ..Plant import Plant


class Belladonna(Plant):

    def __init__(self, strength, initiative, symbol, position, world, color):
        super(Belladonna, self).__init__(strength, initiative, symbol, position, world, color)

    def die(self, aggressor):
        super(Belladonna, self).die(aggressor)
        self._world.kill(self, aggressor)
