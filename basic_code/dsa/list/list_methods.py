# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: 5

# Adding elements
my_list.append(6)  # Adds 6 to the end of the list
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Inserting elements
my_list.insert(2, 'a')  # Inserts 'a' at index 2
print(my_list)  # Output: [1, 2, 'a', 3, 4, 5, 6]

# Removing elements
my_list.remove('a')  # Removes the first occurrence of 'a'
# my_list.remove(3) # with index
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Popping elements
element = my_list.pop()  # Removes and returns the last item
print(element)  # Output: 6
print(my_list)  # Output: [1, 2, 3, 4, 5]

# Slicing
print(my_list[1:3])  # Output: [2, 3]

# Update
my_list[3] = 10
print(my_list)