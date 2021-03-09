import pygame as pg
from math import sin, cos, tan, asin, acos, atan, pi, radians, degrees


class System:
    def __init__(self, colour, x, y, r, display):
        self.colour = colour
        self.x = x
        self.y = y
        self.r = r
        self.display = display

    def plot(self):
        pg.draw.circle(self.display, self.colour, (self.x, self.y), self.r)