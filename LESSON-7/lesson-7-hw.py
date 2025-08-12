# In your class, there are five groups that participated and got prizes in 
# different competitions held in various schools. 
# Your class teacher asks your help to record all the details. 
# Write a program and use a tuple data structure to store each record. 
# The program should ask the user to enter details like groupname, Sizeofthegroup, 
# dateofthecompetition, venue, typeofthemedal. Store it as a tuple.

# This should be done for all the five groups

records = {}

for i in range(5):
    groupname = input("Enter your group name")
    group_size = int(input("Enter the size of the group"))
    date = input("enter date as yy:mm:dd")
    venue = input("enter the venue")
    medal = input("enter your medal type")
    records[groupname] = group_size, date, venue, medal

print(records)