from ..Plant import Plant


class Grass(Plant):

    def __init__(self, strength, initiative, symbol, position, world, color):
        super(Grass, self).__init__(strength, initiative, symbol, position, world, color)
