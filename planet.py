import pygame as pg
from math import sin, cos, tan, asin, acos, atan, pi, radians, degrees
from vector import Vector


class Planet:
    def __init__(self, display, colour, vector, mass, mom, r, idd, sun=None):
        self.colour = colour
        self.r = r
        self.display = display
        self.mass = mass
        self.mom = mom
        self.vector = vector
        self.sun = sun
        self.id = idd

    def plot(self, sf):
        if not self.sun:
            self.rect = pg.draw.circle(self.display, self.colour, (self.vector.x, self.vector.y), sf*self.r)
        else:
            self.rect = pg.draw.circle(self.display, self.colour, (int(self.vector.x*sf)+self.sun.vector.x, int(self.vector.y*sf)+self.sun.vector.y), sf*self.r)

    def plotPath(self, layer, sf):
        if not self.sun:
            pg.draw.rect(layer, self.colour, (self.vector.x, self.vector.y, 1, 1))
        else:
            pg.draw.rect(layer, self.colour, (int(self.vector.x*sf)+self.sun.vector.x, int(self.vector.y*sf)+self.sun.vector.y, 1, 1))


    def g_refresh(self, dt):
        g=1
        r_vec = self.vector
        r_mag = r_vec.mag
        try:
            r_hat = r_vec/r_mag
        except:
            r_hat = Vector(0,0)
        try:
            f_mag = (g*self.mass*self.sun.mass)/(r_mag**2)
        except:
            f_mag = 0
        f_vec = r_hat*(-f_mag)
        self.mom = self.mom + (f_vec * dt)
        self.prev_vec = self.vector
        try:
            self.vector = self.vector + ((self.mom*dt)/self.mass)
        except:
            # print(self.mass)
            self.vector = self.vector + ((self.mom*dt)/0.001) 

    def isCollision(self, rect):
        if self.rect.colliderect(rect):
            return True
        else:
            return False

    def isOver(self, x, y):
        if self.rect.collidepoint(x, y):
            return True
        else:
            return False
        