import pygame as pg
from math import sin, cos, tan, asin, acos, atan, pi, radians, degrees


class System:
    def __init__(self, name, colour, x, y, r, display):
        self.colour = colour
        self.x = x
        self.y = y
        self.r = r
        self.display = display
        self.name = name

    def plot(self):
        self.rect = pg.draw.circle(self.display, self.colour, (self.x, self.y), self.r)

    def isOver(self, x, y):
        if self.rect.collidepoint(x, y):
            return True
        else:
            return False



