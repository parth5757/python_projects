class Node:
    def __init__(self, val):
        self.data = val
        self.left = self.right = None
    
def sum_tree(root):
    if root is None:
        return 0
    return sum_tree(root.left) + sum_tree(root.right) + root.data

def is_sum_tree(root):
    if root is None or (root.left is None and root.right is None):
        return True
    
    ls = sum_tree(root.left)
    rs = sum_tree(root.right)

    # This following both condition work well but if you more secure use second syntax.
    return root.data == ls + rs
    # return root.data == ls + rs and \
  	# 	is_sum_tree(root.left) and \
  	#  	is_sum_tree(root.right)


if __name__ == "__main__":
    root = Node(26)
    root.left = Node(10)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right.right = Node(3)

    if is_sum_tree(root):
        print("True")
    else:
        print("False")