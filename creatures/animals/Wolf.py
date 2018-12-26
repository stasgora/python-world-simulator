from ..Animal import Animal


class Wolf(Animal):

    def __init__(self, strength, initiative, symbol, position, world, color):
        super(Wolf, self).__init__(strength, initiative, symbol, position, world, color)
