from .Creature import Creature

class Animal(Creature):

    def __init__(self, strength, initiative, symbol, position, world, color):
        super(Animal, self).__init__(strength, initiative, symbol, position, world, color)
        self._range = 1

    def action(self):
        super(Animal, self).action()
        new_pos = self.get_move_pos()
        if new_pos is None or new_pos == self._position:
            return
        if self._world.get_map().get(new_pos) is not None:
            self.collide(self._world.get_map().get(new_pos))
        else:
            self.move(new_pos)

    def get_move_pos(self):
        return self._world.get_map().get_pos_nearby(self._position, False, self._range)

    def move(self, position):
        self._world.get_map().move(self._position, position)
        self._position = position

    def reproduce(self, parent):
        new_pos = self._world.get_map().get_birth_pos(self._position, parent.get_position())
        if new_pos is None:
            return
        self.mate()
        parent.mate()
        self._world.give_birth(self._symbol, new_pos)

    def collide(self, creature):
        if self._symbol != creature.get_symbol():
            self.attack(creature)
        elif self._mature and creature.is_mature() and not self._mated and not creature.is_mated():
            self.reproduce(creature)

    def attack(self, creature):
        if creature.defend(self):
            return
        if self._strength >= creature.get_strength():
            self._world.kill(self, creature)
            self.move(creature.get_position())
        else:
            self._world.kill(creature, self)

    @staticmethod
    def is_animal(symbol):
        return symbol == 'A' or symbol == 'X' or symbol == 'L' or \
               symbol == 'O' or symbol == 'Z' or symbol == 'W' or symbol == 'C'

    @staticmethod
    def get_names():
        return ["Antelope", "CyberSheep", "Fox", "Sheep", "Turtle", "Wolf", "Human"]
