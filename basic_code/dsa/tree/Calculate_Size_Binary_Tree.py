class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# Complete recursion example.
def getSize(root):
    if root is None:
        return 0
    
    left = getSize(root.left)
    right = getSize(root.right)

    return left + right + 1
    
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(getSize(root))