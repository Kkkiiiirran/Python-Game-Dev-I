import pgzrun

WIDTH = 500
HEIGHT = 500

def draw():
    rect = Rect((0,0), (100,100))
    rect.center = 250,250
    screen.draw.rect(rect, (200,200,200))

pgzrun.go()
