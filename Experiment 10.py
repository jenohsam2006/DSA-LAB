class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        print(f"Insert {key} → Root created")
        return Node(key)
    elif key < root.data:
        print(f"Insert {key} → Placed to the left of {root.data}")
        root.left = insert(root.left, key)
    elif key > root.data:
        print(f"Insert {key} → Placed to the right of {root.data}")
        root.right = insert(root.right, key)
    return root

def inorder(root):
    return inorder(root.left) + [root.data] + inorder(root.right) if root else []


def preorder(root):
    return [root.data] + preorder(root.left) + preorder(root.right) if root else []


def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.data] if root else []

print("Enter the number of employees:")
n = int(input())

root = None
print("\nEnter Employee IDs one by one:")
ids = []
for i in range(n):
    emp_id = int(input(f"Employee {i+1} ID: "))
    ids.append(emp_id)

print("\nBST Insertion Process:")
for emp_id in ids:
    root = insert(root, emp_id)

print("\nBinary Search Tree Traversals:\n")
print("Inorder Traversal   :", *inorder(root))
print("Preorder Traversal  :", *preorder(root))
print("Postorder Traversal :", *postorder(root))
