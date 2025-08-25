import pgzrun
def read_questions():

    questions = []

    with open("questions.txt","r") as file:
        data = file.readlines()

        for line in data:
            line_split = line.split(",")

            question = {
                "question": line_split[0],
                "options" : line_split[1:5],
                "answer" : int(line_split[5])
            }

            questions.append(question)
    
    return questions
    
def read_next_question():
    return QUESTIONS[next_ques]


def update_time():
    global start_time

    if start_time>0:
        start_time-=1

WIDTH = 600
HEIGHT = 450

x = 300


QUESTIONS = read_questions()
next_ques = 0

ques_dict = read_next_question()

start_time = 10
game_over=False



r_1 = Rect((20,50),(450,100))

r_2 = Rect((490,50),(100,100))

r_3 = Rect((20,180),(210,100))

r_4 = Rect((20,310),(210,100))

r_5 = Rect((260,310),(210,100))

r_6 = Rect((260,180),(210,100))

r_7 = Rect((490,180),(100,300))


options= [r_3, r_4, r_5, r_6]


def draw():
    if not game_over:
        screen.fill(color = "black")
        screen.draw.filled_rect(r_1, color = "blue")
        screen.draw.textbox(ques_dict["question"] ,r_1, color="white")
        screen.draw.filled_rect(r_2, color = "orange")
        screen.draw.filled_rect(r_3, color = "orange")
        screen.draw.filled_rect(r_4, color = "orange")
        screen.draw.filled_rect(r_5, color = "orange")
        screen.draw.filled_rect(r_6, color = "orange")
        screen.draw.filled_rect(r_7, color = "darkgreen")


        screen.draw.textbox(ques_dict["options"][0], r_3, color="white")
        screen.draw.textbox(ques_dict["options"][1], r_4, color="white")
        screen.draw.textbox(ques_dict["options"][2], r_5, color="white")
        screen.draw.textbox(ques_dict["options"][3], r_6, color="white")

        screen.draw.textbox(str(start_time), r_2, color="white")

        screen.draw.text("Welcome To Quiz Master ",(x,15),fontsize = 50,color = "white")

    else:
        screen.fill(color="white")


def update():
    pass
    global x
    x-=3

    if x <= -400:
        x = 700

def on_mouse_down(pos):
    global next_ques, ques_dict, start_time, game_over

    for i in range(4):
        if options[i].collidepoint(pos):
            if ques_dict["answer"] == i+1:
                next_ques+=1
                ques_dict = read_next_question()
                start_time=10
        else:
            game_over = True
            




clock.schedule_interval(update_time, 1)


   





pgzrun.go()





# with open("lesson 6/questions.txt","r")as file:
#     data = file.readlines()
#     for line in data:
#         print(line)