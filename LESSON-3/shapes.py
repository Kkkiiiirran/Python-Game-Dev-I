import pgzrun

# circle

WIDTH = 500
HEIGHT = 500

rect = Rect((40,80) , (180,50))
rect.center = (250,250)
def draw():
    # screen.draw.circle(color=("red"), pos = (250,250) , radius = 20)
    screen.draw.rect(rect, color="red")






pgzrun.go()