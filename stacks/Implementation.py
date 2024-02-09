class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.items = []

    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0

    def push(self, item):
        # Add an element to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the element from the top of the stack
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        # Return the element at the top of the stack without removing it
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        # Return the number of elements in the stack
        return len(self.items)


#                                       DIFF B/W STACK AND Q

# Summary:
# Stack:

# Insertion and deletion both happen at the top.
# LIFO behavior (Last-In-First-Out).
# Queue:

# Insertion at the rear, deletion at the front.
# FIFO behavior (First-In-First-Out).

#                                       USAGE

# Use Stacks When:

# You need to keep track of the order of elements.
# You want to reverse the order of elements.
# You are dealing with recursive or nested structures.

# (1) Expression Evaluation:
# Stacks are often used to evaluate arithmetic expressions, check for balanced parentheses, and perform infix to postfix conversion.

# (2) Function Call Management:
# Function call stack in programming languages is implemented using a stack. Each function call pushes a frame onto the stack, and returning from a function pops the frame.

# (3) Undo Mechanism:
# Stacks are useful for implementing undo mechanisms in applications, where the most recent actions can be easily reversed by popping from the stack.

# (4) Backtracking Algorithms:
# In backtracking problems, a stack can be used to store the state and backtrack when needed. Examples include maze-solving and the Eight-Queens problem.

# (5) Depth-First Search (DFS):
# DFS, a graph traversal algorithm, often uses a stack to keep track of the vertices to visit.