import Arrows
from .Animal import Animal
import Point
from Commentator import Commentator


class Human(Animal):

    def __init__(self, strength, initiative, symbol, position, world, color):
        super(Human, self).__init__(strength, initiative, symbol, position, world, color)
        self.__ability_counter = 0
        self.__next_move = None

    def action(self):
        super(Human, self).action()
        if self.__ability_counter > 0:
            if self.__ability_counter > 5:
                self._strength -= 1
                self._world.write_log(Commentator.report_ability_use(self))
            self.__ability_counter -= 1

    def get_move_pos(self):
        return self.__next_move

    def set_next_move(self, key):
        if key is None:
            return
        self.__next_move = Point.Point(self._position.x, self._position.y).add(Arrows.move_pos[key])

    def use_ability(self):
        if self.__ability_counter == 0:
            self.__ability_counter = 10
            self._strength += 5

    def get_ability_counter(self):
        return self.__ability_counter

    def set_ability_counter(self, ability_counter):
        self.__ability_counter = ability_counter
