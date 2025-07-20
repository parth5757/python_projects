squares = [x for x in range(1,11)]

print(squares)

# events
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)

# Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(fahrenheit)

# letter of words in sentence
sentence = "List comprehensions provide a concise way to create lists"
letter = [letter[0] for letter in sentence.split()]
print(letter)


# Flatten a 2D List
matrix = [[1, 2, 3], [4, 5], [6, 7, 8]]
flatten = [num for row in matrix for num in row]
print(flatten)

# common element from 2 list

list1 = [1, 2, 3, 7, 5]
list2 = [3, 4, 5, 6, 7]

common = [x for x in list1 if x in list2]
print("common:", common.sort())

# Find Palindromic Words
words = ["level", "world", "radar", "python", "madam"]
palindromic = [word for word in words if word==word[::-1]] 

print(palindromic)

# Filter Dictionary by Value
ages = {'John': 25, 'Alice': 19, 'Bob': 30, 'Carol': 17}
adults = {name: age for name, age in ages.items() if age > 18}
print(adults)