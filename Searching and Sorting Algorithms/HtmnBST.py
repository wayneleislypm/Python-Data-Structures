class BSTNode:
    #creating a node that holds information about our binary search tree
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
    # method to insert application s inro the tree 
    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if str(val.national_id) < str(self.val.national_id):
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
    #method to check while traversing the branch of the tree 
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val
    # traversing the other side if the binary search tree to find the largest 
    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val
    # method to delete application s // applications in the binary search tree 
    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self
    # method check for existance of an application 
    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)
    #preorder binary search tree traversal 
    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals
    # inorder binary search tree traversal
    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals
    # post order tree traversal 
    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals
bst = BSTNode()
bst.insert(45)