import time
from turtle import color
import pgzrun

TITLE = "Qui Master"
WIDTH = 870
HEIGHT = 1000

marquee_box = Rect(0,0,880,80)
question_box = Rect(0, 0, 630, 150)
answer_box1 = Rect(0, 0,  300, 200)
answer_box2 = Rect(0, 0, 300, 200)
answer_box3 = Rect(0, 0, 300, 200)
answer_box4 = Rect(0,0,300, 200)
timer_box = Rect(0,0, 150,150)
skip_box = Rect(0,0,150, 430)

question_box.move_ip(20, 100)
answer_box1.move_ip(20, 270)
answer_box3.move_ip(20, 500)
answer_box2.move_ip(350, 270)
answer_box4.move_ip(350, 500)
timer_box.move_ip(700,100)
skip_box.move_ip(700,270)

questions = []
question_index = 0
question_file_name = "LESSON-11/questions.txt"

is_game_over = False
score = 0
time_left = 10
marquee_message = ""

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

def draw():
    global marquee_message
    screen.fill("pink")
    screen.draw.filled_rect(marquee_box, "pink")
    screen.draw.filled_rect(question_box, "navy blue")
    screen.draw.filled_rect(answer_box1, "orange")
    screen.draw.filled_rect(answer_box2, "orange")
    screen.draw.filled_rect(answer_box3, "orange")
    screen.draw.filled_rect(answer_box4, "orange")
    screen.draw.filled_rect(timer_box, "navy blue")
    screen.draw.filled_rect(skip_box, "dark green")

    marquee_message = f"Welcome to Quiz Master...Q: {question_index} of 10"
    screen.draw.textbox(marquee_message, marquee_box, color="red")

    screen.draw.textbox(str(time_left), timer_box, color="white")

    screen.draw.textbox(question['question'], question_box, color="white")

    screen.draw.textbox(question['options'][0], answer_box1, color="white")
    screen.draw.textbox(question['options'][1], answer_box2, color="white")
    screen.draw.textbox(question['options'][2], answer_box3, color="white")
    screen.draw.textbox(question['options'][3], answer_box4, color="white")
    screen.draw.textbox(
        "Skip", skip_box,
        color="black", angle=-90
    )

def update():
    move_marquee()

def on_mouse_down(pos):
    options = question['options']
    for i in range(len(answer_boxes)):
        box = answer_boxes[i]
        if box.collidepoint(pos):
            if options[i]== question['answer']:
                correct_answer()
            else:
                gameOver()
    
    if skip_box.collidepoint(pos):
        skip_question()


def move_marquee():
    marquee_box.x = marquee_box.x - 2
    if marquee_box.right < 0:
        marquee_box.left = WIDTH

def update_time_left():
    global time_left
    if time_left:
        time_left = time_left - 1
    else:
        gameOver()

def skip_question():
    global question, time_left
    if questions and not is_game_over:
        question = read_next_question()
        time_left = 10
    else:
        gameOver()

def read_question_file():
    global questions
    file = open(question_file_name, 'r')
    for line in file:
        q_list = line.split(',')
        question = q_list[0]
        options = []
        for i in range(4):
            options.append(q_list[i+1])
        print(options)
        answer_index = int(q_list[5])-1
        new_question = {'question': question,
                     'options': options,
                     'answer' : options[answer_index]
                     }
        questions.append(new_question)
        print(questions)
    file.close()
    print(questions)

def read_next_question():
    global question_index
    question_index = question_index + 1
    return questions.pop(0)

def gameOver():
    global question, time_left, is_game_over
    message = f"Game over!\n You got {score} questions correct"
    question = {'question': message,
                     'options': ["-", "-", "-", "-"],
                     'answer' : 5
                     }
    time_left = 0
    is_game_over = True

def correct_answer():
    global score, question, time_left, questions

    score+=1

    if questions:
        question = read_next_question()
        time_left = 10
    else:
        gameOver()
read_question_file()
question = read_next_question()
clock.schedule_interval(update_time_left,1)
pgzrun.go()
