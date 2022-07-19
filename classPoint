import math
from math import sqrt


class Point:

    list_points = []


    def __init__(self, coordinate1=0, coordinate2=0):
        self.move_to(coordinate1, coordinate2)
        Point.list_points.append(self)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):
        print(f'Точка с координатами ({self.x}, {self.y})')

    def get_distance(self, another_point):
        if not isinstance(another_point, Point):
            return "Не найдено" #ValueError("аргумент должен принадлижать классу Точка")
        return math.sqrt((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2)

#test
"""
p1 = Point()
p2 = Point()
p1.move_to(1, 2)
p2.move_to(4, 6)
d = p1.get_distance(10)
print(d)
"""
