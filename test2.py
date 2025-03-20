import pgzrun
import random

WIDTH = 200
HEIGHT = 200

def draw():
    screen.fill((100,255,67))
    r = 255
    g = 0
    b = random.randint(120,200)
    w= 150
    h = 150
    for i in range(20):
        rect = Rect((0,0),(w,h))
        rect.center = 100,100
        screen.draw.rect(rect, (r,g,b))

        r-=10
        g+=10
        w-=10
        h+=10




pgzrun.go()