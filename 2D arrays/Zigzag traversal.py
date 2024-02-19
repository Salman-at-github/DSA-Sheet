def zigzag_traversal(matrix):
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])
    result = []

    for i in range(rows + cols - 1):
        if i % 2 == 0:
            # Traverse upward in the column
            row = min(i, rows - 1)
            col = i - row
            while row >= 0 and col < cols:
                result.append(matrix[row][col])
                row -= 1
                col += 1
        else:
            # Traverse downward in the column
            col = min(i, cols - 1)
            row = i - col
            while col >= 0 and row < rows:
                result.append(matrix[row][col])
                row += 1
                col -= 1

    return result

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = zigzag_traversal(matrix)
print(result)
