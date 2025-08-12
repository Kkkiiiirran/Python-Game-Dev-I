import pgzrun
import random

WIDTH = 500
HEIGHT= 500

alien = Actor('alien')
alien.pos = (random.randint(50,450),random.randint(50,450))
def draw():
    screen.fill(color = (155,0,0))
    alien.draw()

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        alien.pos = (random.randint(50,450),random.randint(50,450))



pgzrun.go()