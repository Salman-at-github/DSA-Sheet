# Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.

def generate_matrix(m,n): #row,col
    mat = [[i*j for j in range(n)] for i in range(m) ]
    for line in mat:
        print(line)

generate_matrix(4,4)

