import pgzrun

HEIGHT=870
WIDTH=650

marquee_box=Rect(0,0,880,80)
question_box=Rect(0,0,650,150)
timer_box=Rect(0,0,150,150)
answerbox1=Rect(0,0,300,150)
answerbox2=Rect(0,0,300,150)
answerbox3=Rect(0,0,300,150)
answerbox4=Rect(0,0,300,150)
skip_box=Rect(0,0,150,330)


marquee_message=''
score=0
timer=20
question_file='LESSON-11/questions.txt'
game_over= False
answerboxes=[answerbox1,answerbox2,answerbox3,answerbox4]
questions=[]
question_count=0
question_index=0

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
answerbox1.move_ip(20,270)
answerbox2.move_ip(370,270)
answerbox3.move_ip(20,450)
answerbox4.move_ip(370,450)
skip_box.move_ip(700,270)

def draw():
    global marquee_message
    screen.clear()
    screen.draw.filled_rect(marquee_box, 'black')
    screen.draw.filled_rect(question_box,' navy blue')
    screen.draw.filled_rect(timer_box,' navy blue')
    screen.draw.filled_rect(skip_box,' green')
    for answer_box in answerboxes:
        screen.draw.filled_rect(answer_box,' orange')
    
    marquee_message='Welcome to Quiz Master!'
    marquee_message= marquee_message+ f'Q: {question_index} of {question_count}'

    screen.draw.textbox(marquee_message,marquee_box, color='white')
    screen.draw.textbox(str(timer),timer_box,color='white', shadow=(0.5,0.5),scolor='red')
    screen.draw.textbox('skip',skip_box,color='white',shadow=(0.5,0.5),scolor='red',angle=-90)
    screen.draw.textbox(questions[0].strip(),question_box,color='white',shadow='red',scolor=(0.5,0.5))

    index=1
    for answerbox in answerboxes:
        screen.draw.textbox(questions[index].strip(),answerbox,color= 'black')
        index= index+1

def update():
    move_marqueebox()

def move_marqueebox():
    marquee_box.x=marquee_box.x-2
    if marquee_box.right <0:
        marquee_box.left= WIDTH

def read_question_file():
    global question_count,questions
    q_file=open(question_file,'r')
    for question in q_file:
        questions.append(question)
        question_count=question_count+1
    q_file.close()

def read_next_question():
    global question_index
    question_index=question_index+1
    return questions.pop(0).split(',')

def on_mouse_down(pos):
    index=1
    for box in answerboxes:
        if box.collidepoint(pos):
            if index is int(questions[5]):
                correct_answer()
            else:
                game_over()
        index= index+1
    if skip_box.collidepoint(pos):
        skip_question()


def correct_answer():
    global score,questions,timer,questions
    score= score+1
    if questions:
        question== read_next_question()
        timer=10
    else:
        game_over()

def game_over():
    global question,timer,game_over
    message= f'Game over!\nYou got {score} questions correct!'
    question= [message,'-','-','-','-',5]
    timer=0
    game_over= True

def skip_question():
    global question, timer
    if questions and not game_over:
        question = read_next_question()
        timer=10
    else:
        game_over()

def update_time_left():
    global timer
    if timer:
        timer= timer-1
    else:
        game_over()
read_question_file()
question = read_next_question()
clock.schedule_interval(update_time_left,1)
pgzrun.go()





       











    
    

   

