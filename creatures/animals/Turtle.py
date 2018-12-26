from ..Animal import Animal
from random import random


class Turtle(Animal):

    DEFENDS_BELOW = 5
    MOVE_CHANCE = 0.25

    def __init__(self, strength, initiative, symbol, position, world, color):
        super(Turtle, self).__init__(strength, initiative, symbol, position, world, color)

    def get_move_pos(self):
        if random() > Turtle.MOVE_CHANCE:
            return None
        return super(Turtle, self).get_move_pos()

    def defend(self, aggressor):
        return aggressor.get_strength() < Turtle.DEFENDS_BELOW
