import pgzrun

def read_input_file():

    questions = []

    with open("questions.txt", "r") as file:
        
        data = file.readlines()
        for line in data:
            line_split = line.split(",")
            
            question = {
                'question': line_split[0],
                'options': line_split[1:5],
                'answer': int(line_split[5])
            }
            
            questions.append(question)
    
    return questions


def get_new_question():
    global question_number
    question = questions_list[question_number]
    question_number+=1
    return question


WIDTH = 600
HEIGHT = 450

question_number = 0

questions_list = read_input_file()
ques = get_new_question()



r_1 = Rect((20,50),(450,100))

r_2 = Rect((490,50),(100,100))

r_3 = Rect((20,180),(210,100))

r_4 = Rect((20,310),(210,100))

r_5 = Rect((260,310),(210,100))

r_6 = Rect((260,180),(210,100))

r_7 = Rect((490,180),(100,300))


def draw():
    screen.fill(color = "black")
    screen.draw.filled_rect(r_1, color = "blue")
    screen.draw.filled_rect(r_2, color = "orange")
    screen.draw.filled_rect(r_3, color = "orange")
    screen.draw.filled_rect(r_4, color = "orange")
    screen.draw.filled_rect(r_5, color = "orange")
    screen.draw.filled_rect(r_6, color = "orange")
    screen.draw.filled_rect(r_7, color = "darkgreen")

    # screen.draw.textbox("hello",(225,90),fontsize = 50,color = "white")
    screen.draw.textbox(ques['question'],r_1 )
    screen.draw.textbox(ques['options'][0],r_3 )
    screen.draw.textbox(ques['options'][1],r_4 )
    screen.draw.textbox(ques['options'][2],r_5 )
    screen.draw.textbox(ques['options'][3],r_6 )




pgzrun.go()





# with open("lesson 6/questions.txt","r")as file:
#     data = file.readlines()
#     for line in data:
#         print(line)