class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

            
###
    def delete(self, data):
        if self is None:
            return self

        if data < self.data:
            if self.left is not None:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right is not None:
                self.right = self.right.delete(data)
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp

            elif self.right is None:
                temp = self.left
                self = None
                return temp

            temp = self.right.get_min_value()
            self.data = temp.data
            self.right = self.right.delete(temp.data)

        return self

    def get_min_value(self):
        current = self
        while current.left is not None:
            current = current.left
        return current
###

root = Node(10)
root.insert(30)
root.insert(40)
root.insert(35)
root.insert(20)
root.insert(47)
root.insert(5)

root.delete(20)#

root.PrintTree()