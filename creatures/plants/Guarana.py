from ..Plant import Plant
from Commentator import Commentator


class Guarana(Plant):

    STRENGTH_VALUE_GIVEN = 3

    def __init__(self, strength, initiative, symbol, position, world, color):
        super(Guarana, self).__init__(strength, initiative, symbol, position, world, color)

    def die(self, aggressor):
        super(Guarana, self).die(aggressor)
        aggressor.set_strength(aggressor.get_strength() + Guarana.STRENGTH_VALUE_GIVEN)
        self._world.write_log(Commentator.report_eating_guarana(aggressor, self))
