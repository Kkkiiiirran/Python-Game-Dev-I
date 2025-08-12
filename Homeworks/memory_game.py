import random
import pgzrun
import time

GRID_SIZE = 4
CELL_SIZE = 100
MARGIN = 10
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE

# 8 unique image names (without ".png"), each duplicated to form pairs
IMAGE_NAMES = ['1', '2', '3', '4', '5', '6', '7', '8']
images = IMAGE_NAMES * 2
random.shuffle(images)

cards = []
revealed = []
matched = []


last_flip_time = 0
reveal_delay = 1.0
waiting = False


for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        image = images.pop()
        cards.append({
            'pos': (i, j),
            'name': image,
            'actor': Actor(image),
            'revealed': False
        })

def draw():
    screen.clear()
    screen.fill(color = (255, 210, 254))
    for card in cards:
        x, y = card['pos']
        rect = Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE - MARGIN, CELL_SIZE - MARGIN)
        card['actor'].pos = rect.center

        if card in revealed or card in matched:
            card['actor'].draw()
        else:
            screen.draw.filled_rect(rect, 'black')

    if len(matched) == len(cards):
        screen.draw.text("You Win! 🎉", center=(WIDTH//2, HEIGHT//2), fontsize=60, color="green")

def on_mouse_down(pos):
    global last_flip_time, waiting

    if waiting or len(matched) == len(cards):
        return

    x = pos[0] // CELL_SIZE
    y = pos[1] // CELL_SIZE

    for card in cards:
        if card['pos'] == (x, y) and card not in revealed and card not in matched:
            revealed.append(card)
            break

    if len(revealed) == 2:
        waiting = True
        last_flip_time = time.time()

def update():
    global revealed, matched, waiting

    if waiting and time.time() - last_flip_time > reveal_delay:
        card1, card2 = revealed

        if card1['name'] == card2['name']:
            matched.extend(revealed)
        revealed = []
        waiting = False

pgzrun.go()
