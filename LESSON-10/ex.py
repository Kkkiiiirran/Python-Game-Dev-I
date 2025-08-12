import pgzrun
import random

WIDTH = 800
HEIGHT = 500

stars = ["red-star.png","orange-star.png","purple-star.png","yellow-star.png","blue-star.png"]
actor_stars = []
selected_stars = []
animation = []


# pick random stars
# add it to the selected_stars

level = 1
gameOver = False


def makeActors():

    gap = WIDTH/(level+2)
    for i in range(level):
        chosen_star = random.choice(stars)
        selected_stars.append(chosen_star)

    selected_stars.append("green-star.png") 
    random.shuffle(selected_stars)

    for i in range(len(selected_stars)):
        star = Actor(selected_stars[i])
        actor_stars.append(star)
        actor_stars[i].pos = gap*(i+1),20
    
    animate_star()

def animate_star():
    for i in range(len(actor_stars)):
        ani = animate(actor_stars[i],duration = 7,y = HEIGHT+15)
        animation.append(ani)
        

def stop_animation():
    for ani in animation:
        ani.stop()

makeActors()


def draw():
    if not gameOver:
        screen.blit("space.png",(0,0))
        for star in actor_stars:
            star.draw()
    else:
        screen.fill("green")
        screen.draw.text("GAME OVER", center=(WIDTH//2, HEIGHT//2), color="red", fontsize = 40)


def on_mouse_down(pos):
    global animation,level,actor_stars,selected_stars, gameOver
    for i in range(len(actor_stars)):
        if actor_stars[i].collidepoint(pos):
            if selected_stars[i]=="green-star.png":
                stop_animation()
                level+=1
                selected_stars=[]
                actor_stars=[]
                animation = []
                makeActors()
            else:
                gameOver = True

            
        

def update():
    pass




pgzrun.go()