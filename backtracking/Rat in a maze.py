directions = "DLRU"
dr = [1, 0, 0, -1]
dc = [0, -1, 1, 0]

def is_valid_move(r, c, n, maze ):
    return 0 <= r < n and 0 <= c <= n and maze[r][c] == 1


def find_path(r, c, n, maze, result_arr, current_path):
    # if its the destination, add path to result
    if r == n-1 and c == n-1:
        result_arr.append(current_path[:])
        return
    
    # else check for all moves, start by marking current cell as visited
    maze[r][c] = 0
    for i in range(len(directions)):
        next_r = r + dr[i]
        next_c = c + dc[i]
        # check if next moves are valid
        if is_valid_move(next_r, next_c, n, maze):
            #add its direction to current path if valid
            current_path.append(directions[i])
            # recursively check next moves too
            find_path(next_r, next_c, n, maze, result_arr, current_path)

            # backtrack the prev move once recursion is exited due to any reason
            current_path.pop()
    
    # unmark the current cell so that we can backtrack if any other paths are available
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
    result_arr = []
    current_path = []

    # Start the backtracking from the source (0, 0) with an empty path
    find_path(0, 0, n, maze, result_arr, current_path)

    # Display the result
    if not result_arr:
        print(-1)
    else:
        for path in result_arr:
            print("".join(path), end=" ")
        print()

