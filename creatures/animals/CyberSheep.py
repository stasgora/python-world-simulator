from ..Animal import Animal
from Point import Point


class CyberSheep(Animal):

    def __init__(self, strength, initiative, symbol, position, world, color):
        super(CyberSheep, self).__init__(strength, initiative, symbol, position, world, color)

    def get_move_pos(self):
        creature = self._world.find_closest_creature('B', self._position)
        if creature is None:
            return super(CyberSheep, self).get_move_pos()

        new_pos = creature.get_position()
        diff_point = Point(new_pos.x, new_pos.y).subtract(self._position)
        new_pos = Point(self._position.x, self._position.y)
        xStep = 1
        yStep = 1
        diff = 0
        aStep = 0
        bStep = 0

        if diff_point.x < 0:
            xStep *= -1
            diff_point.x *= -1
        if diff_point.y < 0:
            yStep *= -1
            diff_point.y *= -1

        if diff_point.x > diff_point.y:# - X
            aStep = 2 * (diff_point.y - diff_point.x)
            bStep = 2 * diff_point.y
            diff = bStep - diff_point.x
            new_pos.x += xStep
            if diff >= 0:
                new_pos.y += yStep
                diff += aStep
            else:
                diff += bStep
        else:# - Y
            aStep = 2 * (diff_point.x - diff_point.y)
            bStep = 2 * diff_point.x
            diff = bStep - diff_point.y
            new_pos.y += yStep
            if diff >= 0:
                new_pos.x += xStep
                diff += aStep
            else:
                diff += bStep
        
        return self._world.get_map().clamp_pos(new_pos)
