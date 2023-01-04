class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return pow(self.x ** 2 + self.y ** 2, 1 / 2)

# не понял задание совсем
class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def edge_distance_from_origin(self):
        return self.distance_from_origin() - self.radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius

    def __rsub__(self, other):
        sub = abs(other.radius - self.radius)
        if sub:
            return sub
        else:
            return Point(self.x, self.y)

    def __sub__(self, other):
        sub = abs(self.radius - other.radius)
        if sub:
            return sub
        else:
            return Point(self.x, self.y)


a = Circle(1, 2, 5)
b = Circle(3, 4, 5)

pt = Point(x=3, y=4)
print(pt)
print(pt.distance_from_origin())
c = a - b
d = b - a
print(f'c={c} d={d}')
