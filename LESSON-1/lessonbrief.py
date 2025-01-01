# CREATE
# DIFFERENTIATE
# ACCESS VALUES
# DIFFERENT TYPES OF DATA STORED
# NESTED DICTIONARIES
# LOOPING THROUGH A DICTIONARY
# ACCESSING ALL KEYS
# ACCESSING ALL VALUES
# CONCATENATING TWO DICTIONARY
# DELETING AN ENTRY OR POPPING
# USES
# CLEARING

#Create a dictionary
data = {
  "name": "Kiran",
  "age": 25,
  "city": "Delhi",
}

# Accessing values in a dictionary
print(data["name"])
print(data)

# Create a list with the same information to show the difference between list and a dictionary
sample_list = ["Kiran", 25, "Delhi"]
print(sample_list[0])

# Get the list of keys
print(data.keys())

# Get the list of values
print(data.values())

for key in data.keys():
	print(key, data[key])
	
# Check if the key exists in the dictionary or not
if "country" in data:
	print(data["country"])
else:
	print("key does not exist")
	
# Add a key-value pair to the dictionary
data["Profession"] = "Software Engineer"
print(data)

# Delete a key-value pair
del(data["Profession"])
print(data)

# Change a value in the dictionary
data["city"] = "Bangalore"
print(data)

# Store a list as a value in the dictionary
data["marks"] = [99,87, 85, 92, 90]
print(data)

# Access a value in the list stored in the dictionary
print(data["marks"][1])

# Create a nested dictionary
classroom = {
  "PulkitChawla" : {
    "age": 23,
    "marks": [89, 85, 90, 86, 90]
  },
  "Kanishk": {
    "age": 13,
    "marks": [90, 95, 85, 87, 80]
  }
}

# Go through basic dictionary operations for nested dictionary
print(classroom.keys())
print(classroom.values())

for i in classroom.keys():
	print(classroom[i])

classroom["PulkitChawla"]["age"] = 30

