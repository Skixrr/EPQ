class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.length = 0
        self.bottom = None
        self.top = None
    
    def add(self,next_node):
        self.length += 1
        next_node = Node(next_node)
        if self.bottom == None:
            self.bottom = next_node
            self.top = next_node
        else:
            self.top.next = next_node
            self.top = next_node
    
    def delete(self):
        self.length -= 1
        curr_node = self.bottom
        while curr_node.next != None:
            curr_node = curr_node.next
        curr_node.next = None
        self.top = curr_node
    
    def output(self):
        temp = []
        curr_node = self.bottom
        while curr_node.next != self.top:
            temp.append(curr_node.data)
            curr_node = curr_node.next
        temp.append(curr_node.data)
        for i in range(len(temp)-1,-1,-1):
            print(temp[i])
            

new_Stack = Stack()
new_Stack.add(34)
new_Stack.add(89)
new_Stack.add(98)
new_Stack.delete()
new_Stack.output()

