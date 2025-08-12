import pgzrun
from pgzero.builtins import *
import pgzero.screen
screen : pgzero.screen.Screen
import random

WIDTH = 500
HEIGHT = 500

message = ""
alien = Actor('alien')

def draw():
    screen.clear()
    
    screen.fill(color = (128, 0, 0))
    alien.draw()
    screen.draw.text(message, center = (400, 20), fontsize = 30)

def place_alien():
    alien.x = random.randint(50, WIDTH-50)
    alien.y = random.randint(50, HEIGHT-50)

def on_mouse_down(pos):
    print(pos)
    global message
    if alien.collidepoint(pos):
        message = "Good Shot!"
        place_alien()
    else:
        message = "You missed.."
place_alien()
pgzrun.go()


    



