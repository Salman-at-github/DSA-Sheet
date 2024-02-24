class Queue:
    def __init__(self):
        # Initialize an empty list to store queue elements
        self.items = []

    def is_empty(self):
        # Check if the queue is empty
        return len(self.items) == 0

    def enqueue(self, item):
        # Add an element to the end of the queue
        self.items.append(item)

    def dequeue(self):
        # Remove and return the element from the front of the queue
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    def front(self):
        # Return the element at the front of the queue without removing it
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("front from an empty queue")

    def size(self):
        # Return the number of elements in the queue
        return len(self.items)


#                                          USAGE

# Use Queues When:

# You need to process elements in a first-in-first-out manner.
# You want to implement breadth-first traversal or exploration.
# You need a simple and effective way to manage tasks in order.


# (1) Breadth-First Search (BFS):
# BFS, another graph traversal algorithm, uses a queue to explore nodes level by level.

# (2) Task Scheduling:
# Queues are suitable for managing tasks in a scheduled manner, where tasks are processed in the order they are received.

# (3) Print Queue:
# In scenarios like print spooling, where multiple print jobs need to be processed in the order they are submitted, a queue is commonly used.

# (4) Buffer in Networking:
# Queues can be used to implement buffers in networking, where data is temporarily stored before being transmitted.

# (5) Multi-threaded Programming:
# Queues are often used to safely share data between multiple threads. For example, a producer-consumer scenario where one thread produces data and another consumes it.

# (6) Level Order Traversal in Trees:
# In tree structures, a queue is employed for level order traversal, ensuring that nodes at the same level are processed before moving to the next level.