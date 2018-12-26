from __future__ import print_function
from Map import Map
from Point import Point
from CreatureFactory import CreatureFactory
from creatures import Human
from os import path
from Commentator import Commentator


class World(object):

    SPAWN_QUANT = 0.05
    SAVES_FOLDER = "saves"
    SAVE_FILE_NAME = "save.txt"

    def __init__(self):
        self.__map = Map()
        self.__list = []
        self.__born = []
        self.__dead = []
        self.__human = None
        self.log_area = None

    def update(self):
        for creature in self.__list:
            if creature.id_dead():
                continue
            creature.action()
        for creature in self.__dead:
            self.__despawn(creature)
        for creature in self.__born:
            self.__spawn(creature)
        self.__dead.clear()
        self.__born.clear()

    def __pre_populate_map(self, size):
        spawn_num = size.x * size.y * World.SPAWN_QUANT
        while spawn_num > 0:
            spawn_num -= 1
            self.__spawn(CreatureFactory.spawn_new(' ', self.__map.get_empty_rand_pos(), self))
        self.__human = CreatureFactory.spawn_new('C', self.__map.get_empty_rand_pos(), self)
        self.__spawn(self.__human)

    def save_world_state(self):
        try:
            dir = path.dirname(__file__)
            save_file = open(path.join(dir, World.SAVES_FOLDER, World.SAVE_FILE_NAME), mode='w')
            print(len(self.__list), self.__map.get_size().x, self.__map.get_size().y, file=save_file)
            for creature in self.__list:
                string = str(creature.get_symbol()) + " " + str(creature.get_position().x) + " " + str(creature.get_position().y) \
                         + " " + str(creature.get_age()) + " " + str(creature.get_strength()) + " " + str(creature.get_last_mated())
                if isinstance(creature, Human.Human):
                    string += " " + str(creature.get_ability_counter())
                print(string, file=save_file)
            save_file.close()
        except FileNotFoundError:
            self.write_log(Commentator.report_file_saving_error())

    def load_world_state(self):
        try:
            dir = path.dirname(__file__)
            with open(path.join(dir, World.SAVES_FOLDER, World.SAVE_FILE_NAME), "r") as save_file:
                num, w, h = [int(x) for x in next(save_file).split()]
                self.__map.reset(Point(w, h))
                self.__list.clear()
                for line in save_file:
                    array = line.split()
                    creature = self.__spawn(CreatureFactory.spawn_new(array[0], Point(int(array[1]), int(array[2])), self))
                    creature.set_age(int(array[3]))
                    creature.set_strength(int(array[4]))
                    creature.set_last_mated(int(array[5]))
                    if isinstance(creature, Human.Human):
                        self.__human = creature
                        creature.set_ability_counter(int(array[6]))
            save_file.close()
        except FileNotFoundError:
            self.write_log(Commentator.report_file_loading_error())

    def find_closest_creature(self, symbol, position):
        min_dist = -1
        closest = None
        dist = 0
        for creature in self.__list:
            if creature.get_symbol() == symbol:
                ref = creature.get_position()
                dist = (ref.x - position.x) * (ref.x - position.x) + (ref.y - position.y) * (ref.y - position.y)
                if min_dist == -1 or min_dist > dist:
                    min_dist = dist
                    closest = creature
        return closest

    def reset(self, size):
        self.__map.reset(size)
        self.__list.clear()
        self.__dead.clear()
        self.__born.clear()
        self.__pre_populate_map(size)

    def __spawn(self, creature):
        self.__map.put(creature, creature.get_position())
        index = -1
        for iter in self.__list:
            if iter.get_initiative() < creature.get_initiative():
                self.__list.insert(index, creature)
                return creature
            index += 1
        self.__list.append(creature)
        return creature

    def __despawn(self, creature):
        if creature is self.__human:
            self.__human = None
        if creature in self.__list:
            self.__list.remove(creature)

    def kill(self, lives, dies):
        if dies is self.__human:
            self.__human = None
        self.__map.remove(dies.get_position())
        dies.die(lives)
        self.__dead.append(dies)
        self.write_log(Commentator.report_death(lives, dies))

    def give_birth(self, symbol, position, can_spawn=False):
        creature = CreatureFactory.spawn_new(symbol, position, self)
        if creature is None or not self.__map.position_fits(creature.get_position()) \
                or self.__map.get(creature.get_position()) is not None:
            return
        if isinstance(creature, Human.Human):
            if self.__human is None:
                self.__human = creature
            else:
                return
        self.__map.put(creature, creature.get_position())
        self.write_log(Commentator.report_birth(creature))
        if can_spawn:
            self.__spawn(creature)
        else:
            self.__born.append(creature)

    def get_human(self):
        return self.__human

    def use_human_ability(self):
        if self.__human is not None:
            self.__human.use_ability()

    def get_map(self):
        return self.__map

    def get_list(self):
        return self.__list

    def write_log(self, message):
        self.log_area.configure(state='normal')
        self.log_area.insert('end', message)
        self.log_area.configure(state='disabled')
