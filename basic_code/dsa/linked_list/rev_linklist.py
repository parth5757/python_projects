class Node:
    def __init__(self, node):
        self.data = node
        self.next = None
        # self.previous = None

def rev_lst(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def linklist(head):
    current = head
    while current:
        print(current.data, end="")
        if current.next:
            print(" → ", end="")
        current = current.next

    print()

if __name__ == "__main__":
    node = Node(10)
    node.next = Node(20)
    node.next.next = Node(30)
    node.next.next.next = Node(40)

    # print("Original List: ", linklist(node))
    linklist(node)

    print()

    reversed_head = rev_lst(node)
    linklist(reversed_head)