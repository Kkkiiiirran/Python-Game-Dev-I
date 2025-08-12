import pgzrun
import random

WIDTH = 700
HEIGHT = 400
satellites = []
next_satellite = 1
lines = []
for i in range(8):
    sat = Actor("satellite")
    sat.pos = (random.randint(50,650), random.randint(50,350))
    satellites.append(sat)



def draw():
    screen.blit("background", (0,0))
    for i in range(8):
        satellites[i].draw()
        screen.draw.text(str(i+1), (satellites[i].pos[0], satellites[i].pos[1]+20))
    for line in lines:
        screen.draw.line(line[0], line[1], (255, 255, 255))

def on_mouse_down(pos):
    global next_satellite, lines
    if next_satellite<8:
        if satellites[next_satellite].collidepoint(pos):
            lines.append((satellites[next_satellite-1].pos, satellites[next_satellite].pos))
            next_satellite+=1
        else:
            lines = []
            next_satellite=1

pgzrun.go()