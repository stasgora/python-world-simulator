import math

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add_n(self, num):
        self.x += num
        self.y += num
        return self

    def add(self, point):
        self.x += point.x
        self.y += point.y
        return self

    def subtract_n(self, num):
        self.x -= num
        self.y -= num
        return self

    def subtract(self, point):
        self.x -= point.x
        self.y -= point.y
        return self

    def multiply_n(self, num):
        self.x *= num
        self.y *= num
        return self

    def multiply(self, point):
        self.x *= point.x
        self.y *= point.y
        return self

    def divide_n(self, num):
        self.x = math.floor(self.x / num)
        self.y = math.floor(self.y / num)
        return self

    def divide(self, point):
        self.x = math.floor(self.x / point.x)
        self.y = math.floor(self.y / point.y)
        return self

    def clamp_n(self, min_, max_):
        self.x = min(max_, max(min_, self.x))
        self.y = min(max_, max(min_, self.y))
        return self

    def clamp(self, min_point, max_point):
        self.x = min(max_point.x, max(min_point.x, self.x))
        self.y = min(max_point.y, max(min_point.y, self.y))
        return self

    def min(self, point):
        return Point(min(self.x, point.x), min(self.y, point.y))

    def max(self, point):
        return Point(max(self.x, point.x), max(self.y, point.y))

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __ne__(self, other):
        if isinstance(other, Point):
            return self.x != other.x or self.y != other.y
        return False

    def __str__(self):
        return "( " + str(self.x) + ", " + str(self.y) + " )"
