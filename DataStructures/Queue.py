class Node:
    def __init__(self,data):
        self.data = data #Assign Data to Node
        self.next = None #Give an empty pointer to next (there is no next node)

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def add(self,new_data):
        new_node = Node(new_data)
        if self.head == 

