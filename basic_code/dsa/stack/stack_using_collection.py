from collections import deque
stack = deque()

# append work as push
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial Stack')
print(stack)

print('\nElement popped from stack: ')

print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nstack element after all element are poped: ')

print(stack)