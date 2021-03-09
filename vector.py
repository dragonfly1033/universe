from math import sin, cos, asin, pi, sqrt, degrees, radians, atan2

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.theta = atan2(self.y, self.x)
        self.mag = sqrt(self.x**2 + self.y**2)

    def __add__(self, other):
        newx = self.x + other.x
        newy =  self.y + other.y
        return Vector(newx, newy)

    def __sub__(self, other):
        newx = self.x - other.x
        newy = self.y - other.y
        return Vector(newx, newy)

    def __truediv__(self, other):
        newx = self.x / other
        newy = self.y / other
        return Vector(newx, newy)

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            newx = self.x * other
            newy = self.y * other
            return Vector(newx, newy)

    def __repr__(self):
        return f'({self.x}, {self.y})'#f'x: {self.x}, y: {self.y}, mag: {self.mag}'



