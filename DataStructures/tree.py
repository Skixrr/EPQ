class Node:
    def __init__(self,data:int,depth: int,next=[]):
        self.data = data
        self.next = next
        self.depth = depth

class Tree:
    def __init__(self):
        self.depth = 0
        self.master = None

    def add(self,data,root=None):
        if root == None:
            root = self.master
        if self.master == None:
            self.master = Node(data,1)
        else:
            root.next.append(Node(data,root.depth + 1,[]))
    
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