names = []

while True:
    choice = int(input("what would you like to do? ADD, VIEW OR DELETE"))

    if choice==1:
        name = input("enter a name")
        names.append(name)

    if choice==2:
        print(names)
