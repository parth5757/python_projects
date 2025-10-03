class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
        
node1 = Node(20)
node2 = Node(40)
node3 = Node(60)
node4 = Node(80)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

current = head
print(head.data)
print(head.next)
while current:
    print(current.data, end="-> ")
    current = current.next
print(None)