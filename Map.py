from Point import Point
from random import randint
import sys


class Map(object):
	MAX_TRY_NUM = 30

	def __init__(self):
		self.__size = None
		self.__map = None

	def get_empty_rand_pos(self):
		position = Point(randint(0, self.__size.x - 1), randint(0, self.__size.y - 1))
		limit = Map.MAX_TRY_NUM
		while self.__map[position.x][position.y] is not None:
			position.x = randint(0, self.__size.x - 1)
			position.y = randint(0, self.__size.y - 1)
			limit -= 1
			if limit <= 0:
				break
		if self.__map[position.x][position.y] is not None:
			return None
		return position

	def get_birth_pos(self, one, two):
		return self.get_pos_nearby(one if randint(0, 1) == 0 else two, True, 1)

	def get_pos_nearby(self, position, empty=False, range_=1, max_strength=sys.maxsize):
		new_pos = self.__get_pos_nearby(position, range_)
		limit = Map.MAX_TRY_NUM
		while new_pos == position or (self.__map[new_pos.x][new_pos.y] is not None
		                              and (empty or self.__map[new_pos.x][new_pos.y].get_strength() > max_strength)):
			new_pos = self.__get_pos_nearby(position, range_)
			limit -= 1
			if limit <= 0:
				break
		if new_pos == position or (self.__map[new_pos.x][new_pos.y] is not None
		                           and (empty or self.__map[new_pos.x][new_pos.y].get_strength() > max_strength)):
			return None
		return new_pos

	def __get_pos_nearby(self, position, range_):
		return self.clamp_pos(Point(position.x + randint(0, range_ * 2) - range_,
		                            position.y + randint(0, range_ * 2) - range_))

	def get_neighbours(self, position):
		list_ = []
		for i in range(-1, 1):
			for j in range(-1, 1):
				pos = Point(position.x + i, position.y + j)
				if (i == 0 and j == 0) or not self.position_fits(pos):
					continue
				neighbour = self.__map[pos.x][pos.y]
				if neighbour is not None:
					list_.append(neighbour)
		return list_

	def get(self, position):
		return self.__map[position.x][position.y]

	def put(self, creature, position):
		self.__map[position.x][position.y] = creature

	def move(self, old_pos, new_pos):
		self.__map[new_pos.x][new_pos.y] = self.__map[old_pos.x][old_pos.y]
		self.remove(old_pos)

	def remove(self, position):
		self.__map[position.x][position.y] = None

	def reset(self, size):
		self.__size = Point(size.x, size.y)
		self.__map = [[None for x in range(size.x)] for y in range(size.y)]

	def position_fits(self, pos):
		return 0 <= pos.x < self.__size.x and 0 <= pos.y < self.__size.y

	def clamp_pos(self, position):
		return position.clamp(Point(0, 0), Point(self.__size.x - 1, self.__size.y - 1))

	def get_size(self):
		return self.__size

	def get_map(self):
		return self.__map
