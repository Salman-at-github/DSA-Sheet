class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
    

class LinkedList:
    def __init__(self):
        self.head_node = None
    
    def is_empty(self):
        return self.head_node is None
    
    def add_item(self, data):
        new_node = Node(data)
        # if LL is empty, add node as head
        if  self.is_empty():
            self.head_node = new_node
        else: #else traverse the LL and add node to end
            current_node = self.head_node
            while current_node.next_node:
                current_node = current_node.next_node
            
            # once traverse is complete, we're at the end of the LL so add node here
            current_node.next_node = new_node
    
    def print_items(self):
        """
            Show all items
        """
        if not self.is_empty():
            current_node = self.head_node
            while current_node:
                print(current_node.data, end="-->")
                current_node = current_node.next_node
            print("None")
        else:
            print("No items to show")
    
    def add_head(self, data):
        """
            Insert element at the beginning O(1)
        """
        new_node = Node(data)
        new_node.next_node = self.head_node
        self.head_node = new_node
    
    def delete_item(self, data):
        if not self.is_empty():
            # Check if the head node contains the data to be deleted
            if self.head_node.data == data:
                self.head_node = self.head_node.next_node
            else:
                current_node = self.head_node
                # Traverse the list to find the node with the specified data
                while current_node.next_node and current_node.next_node.data != data:
                    current_node = current_node.next_node
                
                # Check if the data is found and delete the node if so
                if current_node.next_node and current_node.next_node.data == data:
                    current_node.next_node = current_node.next_node.next_node
                else:
                    print(f"Data {data} not found in the list.")
        else:
            print("List is empty already!")

    def get_length(self):
        if not self.is_empty():
            iter = 1
            current_node = self.head_node
            while current_node.next_node:
                current_node = current_node.next_node
                iter += 1
            return iter

    def insert_at(self, data, index):
        new_node = Node(data)

        if index == 0:
            self.add_head(new_node)

        iter = 0
        current_node = self.head_node
        while current_node.next_node and iter < (index - 1):
            current_node = current_node.next_node
            iter += 1
                
        if iter != index - 1:
            print("Index out of bounds")
            return
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
        




myLL = LinkedList()
myLL.add_item(5)
myLL.add_item(10)
myLL.add_item(12)
myLL.add_item(13)
myLL.add_item(14)
myLL.add_head(100)
# myLL.print_items()
# myLL.delete_item(12)
myLL.print_items()

myLL.insert_at(99, 2)
res = myLL.get_length()
myLL.print_items()
print("Size is ", res)
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
