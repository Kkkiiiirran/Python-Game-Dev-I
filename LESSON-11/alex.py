# file manipulation

# modfiy, add content, rewite or read a file

# pgzero --> star.jpg
# w
# r
# a

# print("""hey
#       how are you""")
# """
# """
from tkinter.messagebox import QUESTION


file_path = "C:/Users/Kiranpreet Kaur/OneDrive/Documents/JetLearn/Python Game Dev - I/LESSON-11/questions.txt"
file_path2 = "LESSON-11/questions.txt"
file_path3 = "questions.txt"


# QUESTIONS = [["Where is the stonehenge?", "India", "England", "Scottland", "Canada", 2], 
#              ["Where is the stonehenge?", "India", "England", "Scottland", "Canada", 2], 
#              ["Where is the stonehenge?", "India", "England", "Scottland", "Canada", 2],
#              ["Where is the stonehenge?", "India", "England", "Scottland", "Canada", 2]]


QUESTIONS = []


with open(file_path, "r") as file:
    data = file.readlines()

    for line in data:
        question_detail = line.split(",")  #storing a list
        # print(question_detail)

        q = {"question": question_detail[0],
             "options": question_detail[1:5],
            "answer": question_detail[5]
            }
        
        QUESTIONS.append(q)

print(QUESTIONS)


