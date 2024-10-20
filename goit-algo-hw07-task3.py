class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    # If the tree is empty, return a new node
    if root is None:
        return Node(key)

    # Otherwise, recur down the tree
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root

def sumOfValues(root):
    # Base case: empty subtree
    if root is None:
        return 0

    # Recursive case: sum of values in the left subtree, the root's value, and the right subtree
    return sumOfValues(root.left) + root.val + sumOfValues(root.right)

# Example usage:
root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

print("Sum of all values in the tree is:", sumOfValues(root))