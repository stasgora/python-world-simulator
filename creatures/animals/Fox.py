from ..Animal import Animal


class Fox(Animal):

    def __init__(self, strength, initiative, symbol, position, world, color):
        super(Fox, self).__init__(strength, initiative, symbol, position, world, color)

    def get_move_pos(self):
        return self._world.get_map().get_pos_nearby(self._position, False, self._range, self._strength)
