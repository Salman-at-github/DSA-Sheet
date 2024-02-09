class Node:
    def __init__(self, data):
        # Node constructor to initialize a node with data and a reference to the next node
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        # LinkedList constructor to initialize an empty linked list with a head node
        self.head = None

    def is_empty(self):
        # Check if the linked list is empty
        return self.head is None

    def append(self, data):
        # Append a new node with the given data to the end of the linked list
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def prepend(self, data):
        # Add a new node with the given data to the beginning of the linked list
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def delete(self, data):
        # Delete the first occurrence of a node with the given data
        if not self.is_empty():
            if self.head.data == data:
                self.head = self.head.next_node
            else:
                current_node = self.head
                while current_node.next_node and current_node.next_node.data != data:
                    current_node = current_node.next_node

                if current_node.next_node:
                    current_node.next_node = current_node.next_node.next_node

    def display(self):
        # Display the elements of the linked list
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next_node
        print("Linked List:", elements)

# Usage example:
my_linked_list = LinkedList()

# Append elements to the linked list
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

# Display the linked list
my_linked_list.display()

# Prepend an element to the linked list
my_linked_list.prepend(0)

# Display the updated linked list
my_linked_list.display()

# Delete an element from the linked list
my_linked_list.delete(2)

# Display the final linked list
my_linked_list.display()


#                                               USES

# 1. LRU Cache (Least Recently Used Cache):
# Implementing an LRU cache where the least recently used element is removed when the cache reaches its capacity.
# 2. Josephus Problem:
# Solving the Josephus problem where every kth person in a circle is eliminated until only one person remains.
# 3. Detecting a Cycle in a Linked List:
# Determining if a linked list has a cycle using Floyd's cycle-finding algorithm.
# 4. Reversing a Linked List:
# Reversing the order of elements in a linked list.
# 5. Intersection Point in Y Shaped Linked Lists:
# Finding the point where two linked lists merge.
# 6. Flattening a Multilevel Doubly Linked List:
# Flattening a multilevel doubly linked list into a single-level doubly linked list.
# 7. Palindrome Linked List:
# Checking if a linked list is a palindrome.
# 8. Merge k Sorted Lists:
# Merging k sorted linked lists into a single sorted linked list.
# 9. Add Two Numbers Represented by Linked Lists:
# Adding two numbers represented by linked lists.
# 10. Clone a Linked List with Next and Random Pointer:
# 11. Implementing a Stack and Queue using Linked List:
# arduino
# Copy code
# 12. Implementing a Polynomial Class:
# arduino
# Copy code
# 13. Evaluating Postfix Expressions:
# css
# Copy code
# 14. Implementing an Undo Mechanism:
# sql
# Copy code
# 15. Circular Linked List Operations:
# csharp
