import pgzrun

WIDTH = 500
HEIGHT = 500

# creating an actor
alien = Actor("alien")
message = ""

def draw():
    screen.fill((255,100,0))
    alien.draw()
    screen.draw.text(message, center=(400,20), color="white", fontsize =25)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "GOOD SHOT"
    else:
        message = "MISSED"




pgzrun.go()