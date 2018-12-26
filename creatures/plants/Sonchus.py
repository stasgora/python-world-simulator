from ..Plant import Plant


class Sonchus(Plant):

    def __init__(self, strength, initiative, symbol, position, world, color):
        super(Sonchus, self).__init__(strength, initiative, symbol, position, world, color)

    def action(self):
        super(Sonchus, self).action()
        self.spread()
        self.spread()
