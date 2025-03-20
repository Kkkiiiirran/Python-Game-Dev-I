# ordered
# mutable
# 

# mutable
# not ordered

temp = {}

# store data
temp = {"name": "Thanishka", "age": 15, 7: "jsdfhj"}

print(temp)

temp["new_value"] = 77

print(temp)

temp["name"] = "ABC"

print(temp)

print(temp["age"])

for c in temp:
    print(c, temp[c])

print(temp.items()) 
for key, value in temp.items():
    print(key,value)


print(list(temp.keys()))

# string = "sfhsf"
# print(list(23))

