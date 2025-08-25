import pgzrun
import random

WIDTH = 700
HEIGHT = 700

score = 0

ss = []
sc = []
ec = []
sn = 1
for i in range(8):
    s = Actor("satellite")
    s.pos = random.randint(10,650),random.randint(10,650)
    ss.append(s)

cord = 0,0

def draw():
    screen.blit("background",(0,0))
    for i in range(8):
        ss[i].draw()
        screen.draw.text(f"{i+1}",center = (ss[i].x,ss[i].y-10),color = ("white"))
    
    for i in range(len(sc)):
        screen.draw.line(sc[i],ec[i],color = "white")
    screen.draw.text(f"{score}/7",center = (100,100),fontsize = (20),color = ("white"))



def update():
    pass

def on_mouse_down(pos):
    global score
    global cord
    global sn
    global sc
    global ec
    cord = pos
    click = False
    for i in range(8):
        if ss[i].collidepoint(pos):
            if i == sn:
                click = True
                sc.append(ss[i-1].pos)
                ec.append(ss[i].pos)
                if score < 7:
                    score += 1
                sn += 1
            else:
                sc = []
                ec = []
                sn = 1
        if score == 7:
            exit()
    if not click:
        sc = []
        ec = []
        sn = 1




pgzrun.go()