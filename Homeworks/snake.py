import random
import pgzrun
import time

# Constants
CELL_SIZE = 20
GRID_WIDTH = 20
GRID_HEIGHT = 20

WIDTH = GRID_WIDTH * CELL_SIZE
HEIGHT = GRID_HEIGHT * CELL_SIZE

# Game state
snake = [(10, 10)]
direction = (0, -1)
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
game_over = False

# Timer settings
last_move_time = 0
move_delay = 0.2  # seconds between snake moves

def update():
    global last_move_time
    if game_over:
        return

    current_time = time.time()
    if current_time - last_move_time >= move_delay:
        move_snake()
        last_move_time = current_time

def move_snake():
    global game_over, food

    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = (head_x + dx, head_y + dy)

    # Check collisions
    if (
        new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
        new_head[1] < 0 or new_head[1] >= GRID_HEIGHT or
        new_head in snake
    ):
        game_over = True
        return

    snake.insert(0, new_head)

    if new_head == food:
        food = generate_food()
    else:
        snake.pop()

def draw():
    screen.clear()
    if game_over:
        screen.draw.text("Game Over", center=(WIDTH//2, HEIGHT//2), fontsize=50, color="red")
        return

    for segment in snake:
        screen.draw.filled_rect(Rect(segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE), "green")

    screen.draw.filled_rect(Rect(food[0]*CELL_SIZE, food[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE), "red")

def on_key_down(key):
    global direction
    if key == keys.UP and direction != (0, 1):
        direction = (0, -1)
    elif key == keys.DOWN and direction != (0, -1):
        direction = (0, 1)
    elif key == keys.LEFT and direction != (1, 0):
        direction = (-1, 0)
    elif key == keys.RIGHT and direction != (-1, 0):
        direction = (1, 0)

def generate_food():
    while True:
        new_food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if new_food not in snake:
            return new_food

pgzrun.go()
