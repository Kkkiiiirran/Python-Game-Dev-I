# tuple = immutable
# access it using indexing

import pgzrun

WIDTH = 500
HEIGHT = 500



def draw():
    rect = Rect((50,50),(100,100))
    screen.draw.filled_rect(rect, (255,0,0)  )

pgzrun.go()
