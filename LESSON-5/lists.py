# Create a 2D - List
matrix = [[1,2,3], [4,5,6], [7,8,9]]

print(matrix)

# Number of rows
print(len(matrix))

# Number of columns
print(len(matrix[0]))

# Accessing a element in 2D List
print(matrix[1][2])

# Looping through values in the 2D List
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        print(matrix[i][j], end = " ")
    print("\n")
    
# Take an input for a matrix and print the elements 

rows = int(input("Enter the number of rows - "))
columns = int(input("Enter the number of columns - "))

matrix = []

for i in range(rows):
    temp = []
    for j in range(columns):
        x = int(input("Enter your element - "))
        temp.append(x)
    matrix.append(temp)
    
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end = " ")
    print("\n")


# Take the square-matrix as input and print the diagonal elements

n = int(input("Enter the dimensions of the matrix - "))

for i in range(n):
    temp = []
    for j in range(n):
        x = int(input("Enter your element - "))
        temp.append(x)
    matrix.append(temp)
    
for i in range(n):
    print(matrix[i][i])


# Program for addition and subtraction and subtraction of 2 2D Lists

matrixA = [[1,2], [3,4]]
matrixB = [[5,6], [7,8]]

additionResult = [[0,0], [0,0]]
subtractionResult = [[0,0], [0,0]]

for i in range(0,2):
    for j in range(0,2):
        additionResult[i][j] = matrixA[i][j] + matrixB[i][j]) 
        subtractionResult[i][j] = matrixA[i][j] - matrixB[i][j])
      
# Addition Result
for i in range(2):
    for j in range(2):
        print(additionResult[i][j], end = " ")
    print("\n")
    
# Subtraction Result
for i in range(2):
    for j in range(2):
        print(subtractionResult[i][j], end = " ")
    print("\n")


# Optional - Program for multiplication of matrices

matrixA = [[1,2], [3,4]]
matrixB = [[5,6], [7,8]]

result = [[0,0], [0,0]]

for i in range(0,2):
  for j in range(0,2):
    for k in range(0,2):
      result[i][j] = result[i][j] + (matrixA[i][k] * matrixB[k][j]) 
      
for i in range(2):
    for j in range(2):
        print(result[i][j], end = " ")
    print("\n")