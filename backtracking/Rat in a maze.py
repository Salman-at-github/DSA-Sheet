# Define the directions to move: Down, Left, Right, Up
direction = "DLRU"

# Define the changes in row and column for each direction
dr = [1, 0, 0, -1]
dc = [0, -1, 1, 0]

# Check if the move is within the bounds of the maze and the cell is not blocked (1)
def is_valid_move(r, c, n, maze):
    return 0 <= r < n and 0 <= c < n and maze[r][c] == 1

# Recursively find a path from (r, c) to the destination in the maze
def find_path(r, c, maze, n, ans, current_path):
    # If the rat reaches the destination, add the current path to the list of paths
    if r == n - 1 and c == n - 1:
        ans.append(current_path[:])
        return

    # Mark the current cell as visited
    maze[r][c] = 0

    # Explore each possible move
    for i in range(4):
        nextr = r + dr[i]
        nextc = c + dc[i]
        if is_valid_move(nextr, nextc, n, maze):
            # Append the current direction to the path
            current_path.append(direction[i])
            # Recursive call for the next move
            find_path(nextr, nextc, maze, n, ans, current_path)
            # Backtrack by removing the last direction
            current_path.pop()

    # Mark the current cell as unvisited when backtracking
    maze[r][c] = 1

if __name__ == "__main__":
    # Define the maze as a 2D list
    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]
    ]

    # Get the size of the maze
    n = len(maze)

    # Initialize variables for result and current path
    result = []
    current_path = []

    # Start the backtracking from the source (0, 0) with an empty path
    find_path(0, 0, maze, n, result, current_path)

    # Display the result
    if not result:
        print(-1)
    else:
        for path in result:
            print("".join(path), end=" ")
        print()
