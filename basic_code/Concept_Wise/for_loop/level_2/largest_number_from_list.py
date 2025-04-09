number = [344, 784, 12, 45, 90, 56]
# method 1 
print("method 1") #my own method simple with just for loop and if else condition
largest_number = "" 
for i in number: 
    if i == number[0]:
        largest_number = i
    if i > int(largest_number):
        largest_number = i
    else:
        continue
print(largest_number)


# method 2 
print("method 2") #my own method same as previous but use len function to reduce time of extra if condition which always check i with number[0
largest_number = number[0]
for i in number: 
    if i > int(largest_number):
        largest_number = i
    else:
        continue
print(largest_number)


# method 3
print("method 3")
print(max(number))

# method 4
print("method 4")
largest_number = sorted(number, reverse=True)
print(largest_number[0])

# method 5
print("method 5")
# Bubble Sort
def bubble_sort(s):
    s = list(s)
    for i in range(len(s)):
        for j in range(len(s) - i - 1):
            if s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]
    return s[-1]
# Quick Sort
def quick_sort(s):
    s = list(s)
    for i in range(len(s)):
        min_idx = i
        for j in range(i + 1, len(s)):
            if s[j] < s[min_idx]:
                min_idx = j
        s[i], s[min_idx] = s[min_idx], s[i]
    return s[-1]
largest_number = bubble_sort(number), quick_sort(number)
print(largest_number)


# method 6 # enumerate use but not make scene to use just time and space more consuming.
print("method 6")
largest_number = number[0]
for idx, val in enumerate(number):
    if val > largest_number:
        largest_number = val
print(largest_number)

# method 7
print("method 7")
from functools import reduce
largest_number = reduce(lambda x, y: x if x>y else y, number)
print(largest_number)
    