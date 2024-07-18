class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

def print_tree(root):
    if not root:
        return
    
    queue = [(root, 0)]
    current_level = 0
    current_level_nodes = []
    
    while queue:
        node, level = queue.pop(0)
        
        if level > current_level:
            print("Level", current_level, ": ", current_level_nodes)
            current_level_nodes = []
            current_level += 1
        
        current_level_nodes.append(node.val)
        
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    
    if current_level_nodes:
        print("Level", current_level, ": ", current_level_nodes)


if __name__ == "__main__":
    root = Node(50)
    
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)
    
    print("In-order traversal of the binary tree:")
    inorder(root)
    print()
    
    print("Tree structure:")
    print_tree(root)
    
    key = 60
    result = search(root, key)
    if result:
        print(f"Node with key {key} found.")
    else:
        print(f"Node with key {key} not found.")
