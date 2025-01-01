# The new academic year is starting and you as the store manager are told 
# to take care of accounts of textbook purchases. As a python programmer, 
# you decide to maintain a dictionary of textbooks and its cost. Create the dictionary.

# a) Later you found that the cost of the physics book was entered wrong. Correct price is 200. Make this change
# b) Add the cost of 2 more books to the dictionary.
# c) Print cost of the book entered by the user.
# d) Print all the books and their cost.

accounts = {"English": 600, "Maths": 700, "Science": 400, "Python": 1000, "Physics": 600}

accounts["Physics"] = 200

accounts["Chemistry"] = 600
accounts["Object Oriented Prog"] = 1500

book = input("Enter the book: ").title()

if book in accounts:
    print(f"The cost of the {book} book is ${accounts[book]}")


print(accounts)




