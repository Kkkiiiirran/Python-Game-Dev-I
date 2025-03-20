import pgzrun
import random


WIDTH = 500
HEIGHT = 500

def draw():
    w = 50
    h = 50
    r = 255
    g = 0
    b = random.randint(120,255)

    for i in range(20):
        rect = Rect((100, 100), (w, h))  
        rect.center = (250, 250) 
        screen.draw.rect(rect, (r, g, b))
        w+=10
        h+=10
        r-=10
        g+=10

    
pgzrun.go()