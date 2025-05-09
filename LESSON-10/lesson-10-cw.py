import pgzrun
import random
FONT_option = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
CENTRE_X = WIDTH / 2
CENTRE_Y = HEIGHT / 2
CENTRE = (CENTRE_X, CENTRE_Y)
FINAL_LEVEL = 6
START_SPEED = 10
ITEMS = ["bag","battery","bottle","chips"]

game_over = False
game_complete = False
current_level = 1
items = []
animations = []

def draw():
    screen.blit('new_bg', (0,0))
    for item in items:
        item.draw()

def update():
    if len(items)==0:
        make_new_items(current_level)

def make_new_items(current_level):
    global items
    new_items = ['paper']
    for i in range(current_level):
        new_item = random.choice(ITEMS)
        new_items.append(new_item)
    random.shuffle(new_items)

    items_blueprint = []
    for item in new_items:
        new_item = Actor(item+"img")
        items_blueprint.append(new_item)

    # layout_items_list = []
    gaps = len(items_blueprint)+1
    gap_size = WIDTH/gaps

    for i in range(len(items_blueprint)):
        x_pos = (i+1)*gap_size
        items_blueprint[i].x = x_pos
    
    global animations
    for item in items_blueprint:
        duration = START_SPEED - current_level
        item.anchor = ("center", "bottom")
        animation = animate(item, duration=duration, y=HEIGHT, on_finished=handle_game_over)
        animations.append(animation)
    
    items = items_blueprint

def on_mouse_down(pos):
    global items, current_level
    for item in items:
        if item.collidepoint(pos):
            if "paper" in item.image:
                handle_game_complete()
            else:
                handle_game_over()

def handle_game_complete():
    global current_level, items, animations, game_complete
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level += 1
        items = []
        animations = []

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize=60, center=CENTRE, color="white")
    screen.draw.text(sub_heading_text, fontsize=30, center=(CENTRE_X, CENTRE_Y + 30), color="white")


def handle_game_over():
    global game_over
    game_over = True
pgzrun.go()