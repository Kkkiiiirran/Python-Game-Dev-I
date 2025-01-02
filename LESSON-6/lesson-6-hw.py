import pgzrun
import pgzero.screen
screen: pgzero.screen.Screen
from pgzero.builtins import *
import random

WIDTH = 660
HEIGHT = 400

score = 0

jerry = Actor('jerry')
cheeze = Actor('cheeze')
cheeze.pos = (100,200)

def draw():
    global score
    screen.blit('checkboard', (0,0))
    jerry.draw()
    cheeze.draw()
    screen.draw.text(f"Score: {score}", (580, 10), color="red")

def place_cheeze():
    cheeze.x = random.randint(100, WIDTH-100)
    cheeze.y = random.randint(50,HEIGHT-50)
    clock.schedule_unique(place_cheeze, 4.0)

def update():
    global score
    if keyboard.left:
        jerry.x-=2
    if keyboard.right:
        jerry.x+=2
    if keyboard.up:
        jerry.y-=2
    if keyboard.down:
        jerry.y+=2

    if jerry.colliderect(cheeze):
        place_cheeze()
        score+=1
    
place_cheeze()

pgzrun.go()