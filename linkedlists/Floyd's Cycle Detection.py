#Principle: If there is a cycle, if we initialize two pointers fast and slow, the fast pointer will get inside the cycle loop first, and once the slow enters it too, they'll meet eventually, confirming the cycle.

class Node:
    def __init__(self, data):
        # Node constructor to initialize a node with data and a reference to the next node
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        # LinkedList constructor to initialize an empty linked list with a head node
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
    
    def has_cycle(self):
        # init slow pointer (one node at a time) and fast pointer (moves two nodes ahead at a time)
        slow_pointer = self.head_node
        fast_pointer = self.head_node
        # Iterate until either the fast pointer reaches the end of the list or there is a cycle (fast pointer catches up to the slow pointer)
        while fast_pointer is not None and fast_pointer.next_node is not None:
            # move slow by one step
            slow_pointer = slow_pointer.next_node

            #move fast by two steps
            fast_pointer = fast_pointer.next_node.next_node

            #check both meet after every iter, indicating a cycle
            if slow_pointer == fast_pointer:
                return True
        
        return False

# Create a linked list with a cycle
my_linked_list = LinkedList()
my_linked_list.add_item(1)
my_linked_list.add_item(2)
my_linked_list.add_item(3)
my_linked_list.add_item(4)
my_linked_list.add_item(5)

# Creating a cycle by connecting the last node to the second node
my_linked_list.head_node.next_node.next_node.next_node.next_node = my_linked_list.head_node.next_node

# Check if the linked list has a cycle
result = my_linked_list.has_cycle()
print(result)  # Output should be True

