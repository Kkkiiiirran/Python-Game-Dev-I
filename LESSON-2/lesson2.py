student_record = {}

num = int(input("How many students are there?"))

for i in range(num):
    name = input("Enter name")
    english = int(input("Enter English marks"))
    science = int(input("Enter Science marks"))
    python = int(input("Enter Python marks"))
    maths = int(input("Enter Maths marks"))
    socialstudies = int(input("Enter Social Studies marks"))
  
    student_record[name] = {"English":english, "Science": science, "Maths": maths, "Python": python, "Social Studies": socialstudies}

print(student_record)