import pygame as pg
from planet import Planet
from vector import Vector
from random import randint as rand
from math import sin, cos, pi, sqrt, e


def getR(x):
    t1 = 30/sqrt(2*pi)
    f1 = (x-240)/90
    exp = (-1)*0.5*f1*f1
    eterm = e**exp
    fin = t1*eterm
    return fin

def getM(x):
    t1 = 1530000/sqrt(2*pi)
    f1 = (x-240)/37
    exp = (-1)*0.5*f1*f1
    eterm = e**exp
    fin = t1*eterm
    return fin


WIDTH = 1224
HEIGHT = 612

pg.init()
display = pg.display.set_mode((WIDTH, HEIGHT))
pathLayer = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)


sun = Planet(display, (255, 255, 0), Vector(612,306), 3000, Vector(0,0), 30, 1)

planets = [sun]
space = 45
dt = 0.1
dz = 0.05
sf = 1

for i in range(10):
    if 0==0:#rand(0,3) != 0:
        # r = rand(50, 350)
        r = 75+((12+space)*i) + rand(-10, 10)
        # rad = rand(3,12)
        rad = getR(r) + rand(-2, 2)
        theta = (rand(0,100)/100)*2*pi
        # mass = rand(1,610000)//10000
        mass = getM(r)/10000
        momentum = mass*sqrt(sun.mass/r)
        ecc = 0.8+(rand(0,100)/100)*(1.2-0.8)
        colour = (rand(0,255), rand(0,255), rand(0,255))
        planets.append(Planet(display, colour, Vector(r*cos(theta), r*sin(theta)), mass, Vector(-sin(theta),cos(theta))*momentum*ecc, rad, i+5, sun))

for p in planets:
    p.plot(sf)
    p.g_refresh(dt)

run = True
while run:
    display.fill((0,0,0))
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 5:
                sf += dz
                pathLayer.fill((0,0,0))
            if event.button == 4:
                sf -= dz
                if sf <= dz: sf = dz
                pathLayer.fill((0,0,0))
        if event.type == pg.MOUSEMOTION:
            x, y = pg.mouse.get_pos()
            for p in planets:
                if p.isOver(x, y):
                    pass


    display.blit(pathLayer, (0,0))

    for p in planets:
        p.plot(sf)
        if not keys[pg.K_p]:
            p.g_refresh(dt)
            p.plotPath(pathLayer, sf)
            for other in planets:
                if p != other:
                    if other.isCollision(p.rect):
                        planets.remove(p)
                        other.r += 1
                        other.mass += p.mass


    pg.display.update()

pg.quit()
quit()
