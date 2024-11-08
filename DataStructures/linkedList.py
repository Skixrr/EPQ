class Node:
    def __init__(self,data):
        self.data = data #Assign Data to Node
        self.next = None #Give an empty pointer to next (there is no next node)

class LinkedList:
    def __init__(self):
        self.head = Node('empty')
    
    def add(self,new_data): #Add to start
        new_node = Node(new_data) #Create head node
        new_node.next = self.head #Link to old head
        self.head = new_node #Make into new head
    
    def delStart(self):
        if self.head.next != None:
            self.head = self.head.next
        else:
            self.head = None

    def printList(self):
        while self.head.next != None: # Go over list
            print(new_list.head.data)
            self.delStart()

new_list = LinkedList()
new_list.add(69)
new_list.add(78)
new_list.add(89)

new_list.printList()