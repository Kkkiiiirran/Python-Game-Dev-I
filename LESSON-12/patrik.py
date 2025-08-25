

import pgzrun

WIDTH = 800
HEIGHT = 600

base = Actor("base")
base.pos = (400, 550)

ball = Actor("ball")
ball.pos = (400, 300)


flip = 3
flipx = 3

def update():
    global flip,flipx
    if keyboard.a:
        base.x -= 5
    if keyboard.d:
        base.x += 5

    ball.y +=  flip 
    ball.x += flipx

    if ball.colliderect(base):
        flip*=-1
    
    if ball.x < 0 or ball.x >800:
        flipx*=-1
    
    if ball.y<0 :
        flip*=-1
    
    if ball.y>600:
        ball.pos = 80, 20

def draw():
    screen.clear()
    base.draw()
    ball.draw()

pgzrun.go()



















pgzrun.go()