countries = {}

while True:
    print("1. Insert")
    print("2. Display all countries")
    print("3. Display all capitals")
    print("4. Get capital")
    print("5. Delete")

    choice = int(input("Enter your choice: "))

    if choice==1:
        country = (input("Enter a country: ")).upper()
        if country not in countries:
            capital = (input("Enter a capital ")).upper()
            countries[country] = capital

    elif choice==2:
        print(list(countries.keys()))
    elif choice==3:
        print(list(countries.values()))
    elif choice==4:
        country = (input("Enter a country ")).upper()
        if country in countries:
            print(countries[country])
    elif choice==5:
        country = (input("Enter the country you want to delete ")).upper()
        del countries[country]
        print(list(countries.keys()))
    else:
        print("Please enter a valid choice ")