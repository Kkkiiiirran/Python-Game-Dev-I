import pgzrun
import random

WIDTH = 700
HEIGHT = 700

score = 0
sat_no = 1


start_cord = []
end_cord = []

satellites = []
for i in range(8):
    s = Actor("satellite")
    s.pos = random.randint(0,650),random.randint(0,650)
    satellites.append(s)


cord = 0,0

def draw():

    screen.blit("background",(0,0))


    for i in range(8):
        satellites[i].draw()
    
    for i in range(len(start_cord)):
        screen.draw.line(start_cord[i], end_cord[i], color="white")


    screen.draw.text(f"{score}/8",center = (100,100),fontsize = (20),color = ("white"))

def update():
    pass

def on_mouse_down(pos):
    global score
    global cord
    cord = pos

    for i in range(8):
        if satellites[i].collidepoint(pos):
            if i == sat_no:
                start_cord.append(satellites[i-1].pos)
                end_cord.append(satellites[i].pos)





pgzrun.go()