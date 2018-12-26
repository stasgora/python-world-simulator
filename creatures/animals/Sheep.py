from ..Animal import Animal


class Sheep(Animal):

    def __init__(self, strength, initiative, symbol, position, world, color):
        super(Sheep, self).__init__(strength, initiative, symbol, position, world, color)
