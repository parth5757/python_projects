class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
    
def preOrder(node, res):
    if not node:
        return
    
    res.append(node.data)

    preOrder(node.left, res)
    
    preOrder(node.right, res)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    res = []
    preOrder(root, res)

    for node in res:
        print(node, end=" ")