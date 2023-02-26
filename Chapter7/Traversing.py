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

# Inorder traversal
# Left -> Root -> Right
    def inorderTraversal (self, root):
        res = []
        if root:
            res = self.inorderTraversal (root.left)
            res.append(root.data)
            res = res + self.inorderTraversal (root.right)    
        return res

# Preorder traversal
#Root -> Left ->Right
    def PreorderTraversal (self, root):
        res = []
        if root:
            res.append(root.data)
            res = res = self.PreorderTraversal(root.left) 
            res = res = self.PreorderTraversal (root.right) 
        return res

# Postorder traversal
# Left ->Right -> Root
    def PostorderTraversal (self, root):
        res = []
        if root:
            res= self.PostorderTraversal (root.left)
            res = res = self.PostorderTraversal (root.right) 
            res.append(root.data)
        return res
    
###
root = Node(10)
root.insert(30)
root.insert(40)
root.insert(35)
root.insert(20)
root.insert(47)
root.insert(5)
root.PrintTree()
###

print (root. inorderTraversal (root)) 
print (root. PreorderTraversal (root)) 
print (root. PostorderTraversal (root))