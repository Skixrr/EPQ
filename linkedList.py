class Node:
    def __init__(self,data):
        self.data = data #Assign Data to Node
        self.next = None #Give an empty pointer to next (there is no next node)

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self,new_data): #Add to start
        new_node = Node(new_data) #Create head node
        new_node.next = self.head #Link to old head
        self.head = new_node #Make into new head

