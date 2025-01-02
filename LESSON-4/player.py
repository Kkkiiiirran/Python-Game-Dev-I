import pgzrun
from random import randint
from pgzero.builtins import *
import pgzero.screen
screen : pgzero.screen.Screen

# Pygame Standard for deciding the title of your game window
TITLE = "Good Shot"
# Pygame Standard for deciding the width and height for your game window in pixels
WIDTH = 500
HEIGHT = 500

# variable to store the message displayed on your screen
message = ""

# Actor is built-in object in pgzero
# interacts with other actors, move around on screen
# Similar to Sprite in Scratch
player = Actor('alien')  # Assuming 'player' image is available
player.x = WIDTH // 2
player.y = HEIGHT // 2
player.dx = 5  # Initial horizontal movement speed

# Default function which will be called to update the screen
def draw():
    # screen is another built-in object
    screen.clear()
    screen.fill(color=(128, 0, 0))
    player.draw()
    screen.draw.text(message, center=(400, 10), fontsize=30)

# Move player and bounce off walls
def update():
    global message
    player.x += player.dx  # Move horizontally
    if player.x > WIDTH - player.width or player.x < player.width:
        player.dx = -player.dx  # Reverse direction if it hits a wall

def place_player():
    player.x = randint(50, WIDTH-50)
    player.y = randint(50, HEIGHT-50)

def on_mouse_down(pos):
    global message
    if player.collidepoint(pos):
        message = "Good Shot"
        place_player()
    else:
        message = "You missed"

# Initial position of the player
place_player()

# Start the game
pgzrun.go()
