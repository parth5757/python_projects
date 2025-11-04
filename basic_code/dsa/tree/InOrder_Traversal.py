class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
    
def inOrder(node, res):
    if node is None:
        return

    inOrder(node.left, res)

    res.append(node.data)

    inOrder(node.right, res)


if __name__ == "__main__":
    # Create binary tree
    #       1
    #      /  \
    #    2     3
    #   / \     \
    #  4   5     6
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    res = []
    inOrder(root, res)

    for node in res:
        print(node, end=" ")