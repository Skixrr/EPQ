import ctypes

class Node:
    def __init__(self,data:int,depth: int):
        self.data = data
        self.next = []
        self.depth = depth
        self.location = id(self)

class Tree:
    def __init__(self):
        self.depth = 0
        self.master = None

    def add(self,data,root=None):
        if root == None:
            root = self.master
        else:
            root = ctypes.cast()
        if self.master == None:
            self.master = Node(data,1)
        else:
            root.next.append(Node(data,root.depth + 1))
    
    def output(self):
        def recurse(currNode):
            print(currNode.data)
            if currNode.next != []:
                for i in currNode.next:
                    recurse(i)
        recurse(self.master)

new_tree = Tree()
new_tree.add(4)
new_tree.add(5)
new_tree.add(6)
new_tree.output()

#how do i add to an existing node apart from master...
