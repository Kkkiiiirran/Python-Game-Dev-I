
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


