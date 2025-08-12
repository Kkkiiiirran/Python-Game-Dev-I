import pgzrun
import random

HEIGHT=600
WIDTH=800

bugs= []
bullets=[]

starship= Actor('galaga')
starship.pos=(400,550)
gap=70
gap2 = 35
for i in range(4):
    for j in range(4):

        bug= Actor('bug')
        bug.pos=(gap*(j+1)), gap2*(i+1)
        bugs.append(bug)

bullet= Actor('bullet')




def draw():
    screen.fill('blue')
    starship.draw()
    for bug in bugs:
        bug.draw()
    
    for bullet in bullets:
        bullet.draw()
    




def on_key_down(key):
    if key==keys.D:
        starship.x+=15
    elif key==keys.A:
        starship.x-=15

direction= 5
def update():
    global direction
    
    for bullet in bullets:
        bullet.y-=10

        for bug in bugs:
            if bug.colliderect(bullet):
                bullets.remove(bullet)
                bugs.remove(bug)
                break
    for bug in bugs:
        bug.x+=direction
    if bugs[-1].x>WIDTH or bugs[0].x < 0:
        direction*=-1
        for bug in bugs:
            bug.y+=35
        



   
    if keyboard.space:
        bullet2= Actor('bullet')
        bullet2.pos=(starship.x,starship.y-10)
        bullets.append(bullet2)
    for bullet in bullets:
        if bullet.y < 0:
            bullets.remove(bullet)




        

        









pgzrun.go()