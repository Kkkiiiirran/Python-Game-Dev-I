# with open("homework.txt", 'w') as file:
#     file.write("Do algebra problems \nEnglish essay on clouds \nLearn 10 new words of French")

# with open("homework.txt", 'a') as file:
#     file.write("\nGive permission slip")

# with open("homework.txt", 'r') as file:
#     hw=file.read()
#     print(hw)
import pgzrun
import random

WIDTH=500
HEIGHT=500
current_quest=0


def readfile():
    QUESTIONS=[]
    with open("questions.txt", 'r') as file:
        data=file.readlines()

        for line in data:
            x=line.split(",")
            quest_dict={
                "question": x[0],
                "options": x[1:5], 
                "answer":int(x[-1])
            }
            print(quest_dict)
            QUESTIONS.append(quest_dict)
    return QUESTIONS

def read_next_ques(Questions, next_index):
    return Questions[next_index]
    

QUESTIONS = readfile()
text_graph=read_next_ques(QUESTIONS, current_quest)
current_quest+=1

quest_box=Rect((20, 70), (330, 200))
ans_box1=Rect((10,390), (170, 100))
ans_box2=Rect((190,390), (170, 100))
ans_box3=Rect((10,280), (170, 100))
ans_box4=Rect((190,280), (170, 100))
skip_box=Rect((380,280), (100, 200))
timer_box=Rect((380,100), (100, 100))

options=[0,1,2]

text_x=5

answerboxes = [ans_box1, ans_box2, ans_box3, ans_box4]

def draw():
    screen.fill("pink")
    screen.draw.filled_rect(ans_box1, color = "orange")
    screen.draw.filled_rect(ans_box2, color = "orange")
    screen.draw.filled_rect(ans_box3, color = "orange")
    screen.draw.filled_rect(ans_box4, color = "orange")
    screen.draw.filled_rect(quest_box, color = "blue")
    screen.draw.filled_rect(timer_box, color = "blue")
    screen.draw.filled_rect(skip_box, color = "dark green")
    screen.draw.textbox(text_graph["options"][0],ans_box1 )
    screen.draw.textbox(text_graph["options"][1],ans_box2 )
    screen.draw.textbox(text_graph["options"][2],ans_box3 )
    screen.draw.textbox(text_graph["options"][3],ans_box4 )
    screen.draw.textbox(text_graph["question"],quest_box )
    screen.draw.textbox("SKIP", skip_box)
    screen.draw.text("Question "+str(current_quest+1)+" out of 10", (text_x, 5), color="black", fontsize=70)

def update():
    global text_x, text_y
    text_x -=5
    if text_x <-550:
        text_x=550
    

def on_mouse_down(pos):
    global text_graph, current_quest
    for i in range(4):
        if answerboxes[i].collidepoint(pos):
            if i+1==text_graph["answer"]:
                print("CORRECT")
                text_graph=read_next_ques(QUESTIONS, current_quest)
                current_quest+=1



    



pgzrun.go()

# git init
# git add .
# git commit -m "message"
# git push