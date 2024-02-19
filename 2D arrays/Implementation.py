def add_matrix(ar1, ar2):
    """
    Adds two matrices and returns the result.

    Parameters:
    - ar1 (list of lists): First matrix
    - ar2 (list of lists): Second matrix

    Returns:
    - list of lists: Sum of the two matrices
    """
    # Check if the matrices have the same dimensions
    if len(ar1) != len(ar2) or len(ar1[0]) != len(ar2[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    
    # Create a matrix to store the sum
    sum_matrix = [
        [0 for _ in range(len(ar1[0]))] for _ in range(len(ar1))
    ]

    # Iterate over each element and add the corresponding elements from both matrices
    for i in range(len(ar1)):
        for j in range(len(ar1[0])):
            sum_matrix[i][j] = ar1[i][j] + ar2[i][j]

    return sum_matrix

# Example usage:
ar1 = [
    [3, 4],
    [8, 9]
]  # 2x2 matrix

ar3 = [
    [7, 6],
    [2, 1]
]  # Another 2x2 matrix for demonstration

res = add_matrix(ar1, ar3)
print(res)

#5x4
#0,0
#1,0    0,1
#2,0    1,1     0,2
#3,0    2,1     1,2     0,3 
#4,0    3,1     2,2     1,3
#4,1    3,2     2,3
#4,2    3,3
#4,3

#[i,j]
#[(i +1),j]    [i, (j+1)]
#[(i+1) +1,j]    [(i+1, j+1)]     [i,(j+2)]
#[u +1,j]   [2,1]     [1,2]     [0,3]
#4,0    3,1     2,2     1,3
#4,1    3,2     2,3
#4,2    3,3
#4,3
