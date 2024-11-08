class Node:
    def __init__(self,data):
        self.data = data #Assign Data to Node
        self.next = None #Give an empty pointer to next (there is no next node)

class LinkedList:
    def __init__(self):
        self.head = Node('empty')
        self.tail = None
        self.hasHead = False
    
    def add(self,new_data): #Add to start
        if self.hasHead == False:
            new_node = Node(new_data) #Create head node
            new_node.next = self.head #Link to old head
            self.head = new_node #Make into new head
            self.tail = new_node
            self.hasHead = True
        else:
            new_node = Node(new_data)
            self.tail.next = new_node
            self.tail = self.tail.next

    def delStart(self):
        if self.head.next != None:
            self.head = self.head.next
        else:
            self.head = None
    
    def printList(self):
        self.currNode = self.head
        def nextNode(self):
            self.currNode = self.currNode.next
        while self.currNode.next != None:
            print(self.currNode.data)
            nextNode(self)
        print(self.tail.data)


new_list = LinkedList()
new_list.add(69)
new_list.add(78)
new_list.add(89)

new_list.printList()