# Create  a matrix by taking the user input and print the trace of the matrix. 
# The trace of the matrix is the sum of the diagonal elements of the matrix. 
# Keep the matrix square to keep it simple.

matrix = [[1,2,3], [4,5,6], [7,8,9]]
total = 0

for i in range(3):
    total+=matrix[i][i]

print(total)
