# Given a 2D matrix, print all elements of the given matrix in diagonal order. For example, consider the following 5 X 4 input matrix.  
# 1     2     3     4
# 5     6     7     8
# 9    10    11    12
# 13    14    15    16
# 17    18    19    20
# Diagonal printing of the above matrix is
# 1
# 5 2
# 9 6 3
# 13 10 7 4
# 17 14 11 8
# 18 15 12
# 19 16
# 20

#T: O(r*c)
#S: O(r + c)
def diagonalOrder(arr, r, c): 
    # Initialize a 2D list 'ans' to store diagonals. 
    # The number of rows in 'ans' is (r + c - 1), 
    # representing the total number of diagonals in the input array.
    ans = [[] for i in range(r + c - 1)] 
    
    # Iterate through each column of the input matrix.
    for i in range(c): 
        # For each column, iterate through each row.
        for j in range(r): 
            # Append the element at position (j, i) in the input array to the corresponding diagonal in 'ans'.
            ans[i + j].append(arr[j][i]) 
    
    # Iterate through each diagonal in 'ans'.
    for i in range(len(ans)): 
        # Iterate through each element in the current diagonal and print it.
        for j in range(len(ans[i])): 
            print(ans[i][j], end=" ") 
        # Move to the next line after printing all elements of the current diagonal.
        print() 

# Driver Code 
# Define the number of rows and columns in the matrix.
r = 5
c = 4

# Define the input matrix.
arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20]
]

# Call the diagonalOrder function with the input matrix dimensions.
# diagonalOrder(arr, r, c)

R = 5
C = 4

def isValid(i, j): 
    # Check if the given indices (i, j) are within the bounds of the matrix.
    if (i < 0 or i >= R or j >= C or j < 0): 
        return False
    return True

def diagonalOrder(arr): 
    # Iterate through each element of the first column as a starting point and print the diagonal starting at it.
    for k in range(0, R): 
        print(arr[k][0], end=" ") 

        # Set row index for the next point in the diagonal.
        i = k - 1

        # Set column index for the next point in the diagonal.
        j = 1

        # Print diagonally upward
        while (isValid(i, j)): 
            print(arr[i][j], end=" ") 
            i -= 1
            j += 1 # move in the upright direction 

        print() 

    # Iterate through each element of the last row (except arr[0][C-1]) as a starting point and print the diagonal starting at it.
    for k in range(1, C): 
        print(arr[R-1][k], end=" ") 

        # Set row index for the next point in the diagonal.
        i = R - 2

        # Set column index for the next point in the diagonal.
        j = k + 1

        # Print diagonally upward
        while (isValid(i, j)): 
            print(arr[i][j], end=" ") 
            i -= 1
            j += 1 # move in the upright direction 

        print() 

# Driver Code 
arr2 = [[ 1,  2,    3,   4], 
        [ 5,  6,    7,   8], 
        [ 9, 10,   11,  12], 
        [13, 14,   15,  16], 
        [17, 18,   19,  20]]

# Function call 
diagonalOrder(arr2) 
