import pgzrun


WIDTH = 800
HEIGHT = 500

items = ['paper', 'bag']

actors_list = []
def draw():
    screen.blit("new_bg", (0,0))
    make_actor()
    for item in actors_list:
        item.draw()

def make_actor():
    for i in range(2):
        item = Actor(items[i]+"img")
        actors_list.append(item)
        item.x = 100
        



def update():
    pass
pgzrun.go()