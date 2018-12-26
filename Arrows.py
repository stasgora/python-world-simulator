from enum import Enum
import Point


class Arrows(Enum):
    UP, DOWN, RIGHT, LEFT = range(4)

move_pos = {Arrows.UP: Point.Point(0, -1), Arrows.DOWN: Point.Point(0, 1), Arrows.RIGHT: Point.Point(1, 0), Arrows.LEFT: Point.Point(-1, 0)}
