class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
    
    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)
    
    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search(root.left, key)
        return self._search(root.right, key)
    
    def delete(self, key):
        self.root = self._delete(self.root, key)
    
    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._minValueNode(root.right)
            root.val = temp.val
            root.right = self._delete(root.right, temp.val)
        return root
    
    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def inorder(self):
        self._inorder(self.root)
        print()
    
    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.val, end=' ')
            self._inorder(root.right)
    
    def preorder(self):
        self._preorder(self.root)
        print()
    
    def _preorder(self, root):
        if root:
            print(root.val, end=' ')
            self._preorder(root.left)
            self._preorder(root.right)
    
    def postorder(self):
        self._postorder(self.root)
        print()
    
    def _postorder(self, root):
        if root:
            self._postorder(root.left)
            self._postorder(root.right)
            print(root.val, end=' ')
    
    def print_tree(self):
        self._print_tree(self.root, 0, "Root: ")
    
    def _print_tree(self, root, level, prefix):
        if not root:
            return
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left:
            self._print_tree(root.left, level + 1, "L--- ")
        if root.right:
            self._print_tree(root.right, level + 1, "R--- ")

# Driver code
if __name__ == "__main__":
    bst = BST()
    
    # Insert nodes
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    
    # Print in-order traversal
    print("In-order traversal of the BST:")
    bst.inorder()
    
    # Print pre-order traversal
    print("Pre-order traversal of the BST:")
    bst.preorder()
    
    # Print post-order traversal
    print("Post-order traversal of the BST:")
    bst.postorder()
    
    # Print the tree structure
    print("Tree structure:")
    bst.print_tree()
    
    # Search for a value
    key = 60
    result = bst.search(key)
    if result:
        print(f"Node with key {key} found.")
    else:
        print(f"Node with key {key} not found.")
    
    # Delete a node
    bst.delete(20)
    print("In-order traversal after deleting 20:")
    bst.inorder()
    
    bst.delete(30)
    print("In-order traversal after deleting 30:")
    bst.inorder()
    
    bst.delete(50)
    print("In-order traversal after deleting 50:")
    bst.inorder()
