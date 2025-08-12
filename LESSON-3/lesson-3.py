import pgzrun
import random

WIDTH = 300
HEIGHT = 300


def draw():
    w = 300
    h = 100
    r = 255
    g = 0
    b = random.randint(120,255)
    for i in range(20):
        rect = Rect((0,0), (w, h))
        rect.center = 150,150
 
        screen.draw.rect(rect,(r,g,b))
    # screen.draw.filled_circle((150,150), 50, (255,255,255) )
    # screen.draw.line((20,20), (100,100), (255,255,255))
    

        r-=10
        g+=10

        w-=10
        h+=10




pgzrun.go()

