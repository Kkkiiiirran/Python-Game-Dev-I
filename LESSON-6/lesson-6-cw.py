import pgzrun
import pgzero.screen
screen: pgzero.screen.Screen
from pgzero.builtins import *
import random

WIDTH = 500
HEIGHT = 500

bee = Actor('bee')
bee.pos= (250,250)
flower = Actor('flower')
score = 0
game_over = False

def times_up():
    global game_over
    game_over= True

def draw():
    screen.blit('background', (0,0))
    
    bee.draw()
    flower.draw()
    message = f"Score: {score}"
    screen.draw.text(message, (400,20), fontsize=30)

    if game_over:
        screen.fill("pink")
        screen.draw.text(f"Times Up! You final score is {score}", midtop=(250, 250), fontsize = 40, color= 'red')

def place_flower():
    flower.x = random.randint(50, WIDTH-50)
    flower.y = random.randint(100, HEIGHT-50)

def update():
    global score
    if keyboard.left:
        bee.x-=2
    if keyboard.right:
        bee.x+=2
    if keyboard.up:
        bee.y-=2
    if keyboard.down:
        bee.y+=2
    
    if bee.colliderect(flower):
        place_flower()
        score+=5
place_flower()

clock.schedule(times_up, 60.0)

pgzrun.go()