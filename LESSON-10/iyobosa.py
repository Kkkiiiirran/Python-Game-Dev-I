import random
import pgzrun

WIDTH = 700
HEIGHT = 500

ITEMS = ["batteryimg", "bagimg", "bottleimg", "chipsimg"]

actors_list = []

n = 2

for i in range(n-1):
    rand_img = random.choice(ITEMS)
    actor = Actor(rand_img)
    actors_list.append(actor)

paper_img = Actor("paperimg")
actors_list.append(paper_img)

gap = WIDTH/(n+1)

for i in range(n):
    actors_list[i].pos = gap * (i+1), 35

def draw():
    for i in range(n):
        actors_list[i].draw()



pgzrun.go()