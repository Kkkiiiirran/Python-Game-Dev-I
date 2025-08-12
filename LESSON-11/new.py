file = open("sample.txt", "r")
data = file.readlines()
for line in data:
    x = line.split(":")
    print(x)
print(data)
file.close()
