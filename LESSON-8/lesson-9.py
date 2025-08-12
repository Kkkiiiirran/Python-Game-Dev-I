import pgzrun
from pgzero.builtins import *
import random
from time import time

WIDTH = 800
HEIGHT = 600

satellites = []

next_sat=1
if satellites[next_sat].collidepoint(pos):

for i in range(8):
    sat = Actor("satellite")
    satellites.append(sat)

num_of_sats = 8
next_satellite = 0
lines = []

start_time = 0
total_time = 0
game_over = False  


def time_up():
    global game_over, lines, satellites
    lines.clear()
    satellites.clear()
    # screen.fill("pink")
    
    game_over = True  


def create_satelite():
    global satellites, start_time
    for i in range(num_of_sats):
        satellite = Actor('satellite')
        satellite.pos = random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)
        satellites.append(satellite)

    start_time = time()


def draw():
    global lines, start_time, total_time, game_over
    screen.blit('background', (0, 0))
    number = 1

    for i in range(8):
        satellites[i].draw()
        screen.draw.text(str(i+1), (satellites[i].x, satellites[i].y+20))




    for satellite in satellites:
        satellite.draw()
        screen.draw.text(str(number), (satellite.pos[0], satellite.pos[1]+20))
        number += 1

    for line in lines:
        screen.draw.line(line[0], line[1], (255, 255, 255))

  
    if not game_over and next_satellite < num_of_sats:
        total_time = time() - start_time
    else:
        screen.draw.text("Game Over", center=(WIDTH / 2, HEIGHT / 2), fontsize=50, color="white")
    
    screen.draw.text(str(round(total_time, 1)), (20, 20), fontsize=30)


def update():
    pass


def on_mouse_down(pos):
    global next_satellite, lines

    if next_satellite < num_of_sats and not game_over:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite-1].pos, satellites[next_satellite].pos))
            next_satellite += 1
        else:
            lines = []
            next_satellite = 0


create_satelite()
clock.schedule(time_up, 60.0)
pgzrun.go()
