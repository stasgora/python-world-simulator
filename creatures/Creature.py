class Creature(object):

    CHILDHOOD_TIME = 4
    MATED_TIME = 2

    def __init__(self, strength, initiative, symbol, position, world, color):
        self._strength = strength
        self._initiative = initiative
        self._symbol = symbol
        self._position = position
        self._world = world
        self._color = color

        self._dead = False
        self._mature = False
        self._age = 0
        self._mated = False
        self._last_mated = -1

    def action(self):
        self._age += 1
        if self._age >= Creature.CHILDHOOD_TIME:
            self._mature = True
        if self._last_mated >= Creature.MATED_TIME:
            self._mated = False
        if self._mated:
            self._last_mated += 1

    def defend(self, aggressor):
        return False

    def die(self, aggressor):
        self._dead = True

    def mate(self):
        self._mated = True
        self._last_mated = 0

    def get_strength(self):
        return self._strength

    def set_strength(self, strength):
        self._strength = strength

    def get_initiative(self):
        return self._initiative

    def get_symbol(self):
        return self._symbol

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_last_mated(self):
        return self._last_mated

    def set_last_mated(self, last_mated):
        self._last_mated = last_mated

    def get_position(self):
        return self._position

    def is_mated(self):
        return self._mated

    def is_mature(self):
        return self._mature

    def id_dead(self):
        return self._dead

    def get_color(self):
        return self._color
