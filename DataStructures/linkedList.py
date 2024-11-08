class Node:
    def __init__(self,data,index=0):
        self.data = data #Assign Data to Node
        self.index = index
        self.next = None #Give an empty pointer to next (there is no next node)

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = Node('empty')
        self.tail = None
        self.hasHead = False
    
    def len(self):
        print(self.length)

    def add(self,new_data): #Add to start
        if type(new_data) == list:
            for i in new_data:
                self.add(i)
        else:
            self.length += 1
            if self.hasHead == False:
                new_node = Node(new_data,self.length - 1) #Create head node
                new_node.next = self.head #Link to old head
                self.head = new_node #Make into new head
                self.tail = new_node
                self.hasHead = True
            else:
                new_node = Node(new_data,self.length - 1)
                self.tail.next = new_node
                self.tail = self.tail.next

    def delStart(self):
        def indexUpdate(self):
            self.currNode = self.head
            def nextNode(self):
                self.currNode = self.currNode.next
            while self.currNode.next != None:
                self.currNode.index -= 1
                nextNode(self)
            self.tail.index -= 1
        if self.head.next != None:
            self.head = self.head.next
            indexUpdate(self)
        else:
            self.head = None
    
    def delete(self,ind):
        self.currNode = self.head
        def nextNode(self):
            self.currNode = self.currNode.next
        if ind >= self.length:
            return 'Index Out of Range'
        elif ind == 0:
            self.delStart(self)
        elif ind == self.tail.index:
            self.delEnd(self)
        else:
            while self.currNode.index < ind-1:
                nextNode(self)
            self.currNode.next = self.currNode.next.next
            def indexUpdate(self):
                self.currNode = self.head
                def nextNode(self):
                    self.currNode = self.currNode.next
                while self.currNode.next != None:
                    self.currNode.index -= 1
                    nextNode(self)
                self.tail.index -= 1

    def delEnd(self):
        self.currNode = self.head
        def nextNode(self):
            self.currNode = self.currNode.next
        while self.currNode.next != self.tail:
            nextNode(self)
        self.tail = None
        self.currNode = self.tail

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
new_list.add([89,67,34,[3,['w']]])
new_list.printList()