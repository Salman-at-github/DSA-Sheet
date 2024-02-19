# Check if the move is within the bounds of the maze and the cell is not blocked (1)
def is_valid(x, y, n, maze):
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 1

# Find all paths from (x, y) to (n-1, n-1) in the maze
def find_paths(x, y, maze, n, ans, current_path):
    # If the rat reaches the destination, add the current path to the list of paths
    if x == n - 1 and y == n - 1:
        ans.append("".join(current_path))
        return

    # Mark the current cell as visited
    maze[x][y] = 0
    
    # Define possible moves: Left, Right, Up, Down
    moves = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]}

    # Explore each possible move
    for move in 'LRUD':
        dx, dy = moves[move]
        next_x, next_y = x + dx, y + dy
        if is_valid(next_x, next_y, n, maze):
            # Recursive call for the next move
            current_path.append(move)
            find_paths(next_x, next_y, maze, n, ans, current_path)
            # Backtrack by removing the last move
            current_path.pop()

    # Mark the current cell as unvisited when backtracking
    maze[x][y] = 1

if __name__ == "__main__":
    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]
    ]

    n = len(maze)
    result = []
    current_path = []

    # Start the backtracking from the source (0, 0) with an empty path
    find_paths(0, 0, maze, n, result, current_path)

    # Display the result
    if not result:
        print(-1)
    else:
        for path in result:
            print(path, end=" ")
        print()
