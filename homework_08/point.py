from math import sqrt


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_zero(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def distance_to_point(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return sqrt(dx ** 2 + dy ** 2)


point1 = Point(12, 16)  # 20
point2 = Point(8, 6)  # 10
point3 = Point(3, 4)  # 5

print(point1.distance_to_zero())
print(point2.distance_to_zero())
print(point3.distance_to_zero())
print(point1.distance_to_point(point2))
print(point2.distance_to_point(point3))
