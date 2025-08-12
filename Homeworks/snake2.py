import random
import pgzrun
import time
CELL_SIZE = 20
CELL_WIDTH = 20
CELL_HEIGHT = 20

WIDTH = CELL_WIDTH*20
HEIGHT = CELL_HEIGHT*20

direction = (0,-1)
snake = [[10,10]]

food_cord = (5,10)
radius = 10

def move_snake():
    global food_cord,snake
    dx = snake[0][0]+direction[0]
    dy = snake[0][1]+direction[1]
    snake.insert(0,[dx,dy])
    
    if snake[0][0]== food_cord[0] and snake[0][1]==food_cord[1]:
        x,y = random.randint(1,19), random.randint(1,19)
        food_cord = (x,y)
    else:
        snake.pop()

def draw():
    screen.clear()
    for segment in snake:
        snake2 = Rect((segment[0]*CELL_SIZE, segment[1]*CELL_SIZE), (CELL_SIZE,CELL_SIZE))
        screen.draw.filled_rect(snake2,"green")
    screen.draw.filled_circle((food_cord[0]*CELL_SIZE, food_cord[1]*CELL_SIZE), radius, "red")

def on_key_down(key):
    global direction
    if key==keys.UP:
        direction = (0,-1)
    if key==keys.DOWN:
        direction=(0,1)
    if key==keys.LEFT:
        direction =  (-1,0)
    if key==keys.RIGHT:
        direction = (1,0)
last_time=0
def update():
    global last_time
    curr = time.time()
    if curr-last_time>0.15:
        move_snake()
        last_time=curr

pgzrun.go()