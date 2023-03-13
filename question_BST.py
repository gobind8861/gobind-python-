
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.count = 0
        
    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
            self.count += 1
            return
        current = self.root
        while True:
            if val < current.val:
                if current.left is None:
                    current.left = TreeNode(val)
                    self.count += 1
                    return
                else:
                    current = current.left
            elif val > current.val:
                if current.right is None:
                    current.right = TreeNode(val)
                    self.count += 1
                    return
                else:
                    current = current.right
            else:
                return
    
    def delete(self, val):
        if self.root is None:
            return False
        elif self.root.val == val:
            if self.root.left is None:
                self.root = self.root.right
                self.count -= 1
                return True
            elif self.root.right is None:
                self.root = self.root.left
                self.count -= 1
                return True
            else:
                temp = self.root.right
                while temp.left is not None:
                    temp = temp.left
                self.root.val = temp.val
                self.root.right = self.deleteHelper(self.root.right, temp.val)
                self.count -= 1
                return True
        else:
            if self.deleteHelper(self.root, val):
                self.count -= 1
                return True
            else:
                return False
                
    def deleteHelper(self, node, val):
        if node is None:
            return False
        elif val < node.val:
            node.left = self.deleteHelper(node.left, val)
            return node
        elif val > node.val:
            node.right = self.deleteHelper(node.right, val)
            return node
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = node.right
                while temp.left is not None:
                    temp = temp.left
                node.val = temp.val
                node.right = self.deleteHelper(node.right, temp.val)
                return node
    
    def search(self, val):
        current = self.root
        while current is not None:
            if val == current.val:
                return True
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return False
    
    def size(self):
        return self.count
# create a new binary search tree
bst = BST()

# insert some nodes into the tree
bst.insert(5)
bst.insert(2)
bst.insert(8)
bst.insert(1)
bst.insert(4)
bst.insert(6)
bst.insert(9)

# search for a node in the tree
print(bst.search(6)) 
print(bst.search(3)) 

# get the size of the tree
print(bst.size()) 

# delete a node from the tree
bst.delete(5)

# get the size of the tree again
print(bst.size()) 
