# Try AI directly in your favorite apps … Use Gemini to generate drafts and refine content, plus get Gemini Pro with access to Google's next-gen AI for ₹1,950.00 ₹0 for 1 month
import pgzrun
import random
#screen dimensions
WIDTH = 1200
HEIGHT = 600

#definiting colours
WHITE = (255,255,255)
BLUE = (0,0,255)
score=0

#create a ship
ship = Actor('galaga')
ship.pos = (WIDTH//2, HEIGHT-60)
bug = Actor('bug')
#define a list for bullets
bullets = []
speed=5

#defining a list of enemies
enemies = []
enemies.append(Actor('bug'))
enemies[-1].x = 10
enemies[-1].y = -100
def draw():
    screen.clear()
    screen.fill(BLUE)
    #ship.draw()
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    #ship to be drawn last
    for bullet in bullets:
        bullet.draw()
    ship.draw()

def on_key_down(key):
    if key == keys.SPACE:        
        bullets.append(Actor('bullet'))
        #the last bullet added , set its position
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y - 50
def update():
    global score
    #move the ship left or right with arrow keys
    if keyboard.left:
        ship.x -= speed
        if ship.x <= 0:
            ship.x = 0
            
    elif keyboard.right:
        ship.x += speed
        if ship.x >= WIDTH:
            ship.x = WIDTH
    
    for enemy in enemies:
        enemy.y += 5
        #as the bug touches the bottom, make it go back up
        if enemy.y >= HEIGHT:
            enemy.y  = -100
            enemy.x = random.randint(50,WIDTH-50)
        for bullet in bullets :
            if enemy.colliderect(bullet):
                score +=100
                #we also want to destory the bullet
                bullets.remove(bullet)
                #destroy the bug
                enemies.remove(enemy)
        #checking if the enemy hits a bullet while 
    for bullet in bullets:
        #if the bullet reaches the top of the screen it should get removed
        #else the list will become huge
        if bullet.y <=0 :
            bullets.remove(bullet)
        else:
            bullet.y -= 10
pgzrun.go()