import pgzrun
import random

WIDTH = 800
HEIGHT = 500
LEVEL = 1
items = ['bag', 'battery', 'chips', 'bottle']
actors_list = []
def draw():
    screen.blit('new_bg', (0,0))
    for i in range(LEVEL+1):
        actors_list[i].draw()

def make_actor():
    for i in range(LEVEL):
        ritem = random.choice(items)
        item = Actor(ritem+'img')
        actors_list.append(item)
    
    actors_list.append(Actor('paperimg'))
    gap = WIDTH//(LEVEL+2)
    random.shuffle(actors_list)
    for i in range(LEVEL+1):
        actors_list[i].x = (i+1)*gap
        animate(actors_list[i], duration=10, y=HEIGHT)

def on_mouse_down(pos):
    global actors_list, LEVEL
    for i in range(LEVEL+1):
        if actors_list[i].collidepoint(pos):
            actors_list.clear()
            LEVEL+=1
            make_actor()


make_actor()
def update():
    pass

pgzrun.go()