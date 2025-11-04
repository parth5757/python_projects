a = 15
b = 4

print("Addition", a+b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division", a // b)
print("Modulus", a % b)
# a = 3
# b = 3
print("Exponent", a ** b)

# BackSlash Usages

result = 10 * 5 + 2 * 3
print(result)
# result = 10 * 5 + 2 * 3 - # it give syntax error (Invalid Syntax)
result = 10 * 5 + 2 * 3 - \
        8 
print(result)
result = 10 * 5 + 2 * 3 - \
        8 + 7 * 6
print(result)


# Airthmatic same type of operator with another example.
if 10 > 5 and \
    20 > 15 and \
    30 > 25:
    print("All condition True")

# same thing written as this following way also.
if 10 > 5 and 20 > 15 and  30 > 25:
    print("Same this way All condition True")

# It can be use with the list
numbers = [1, 2, 3, 4, \
           5, 6, 7, 8]
print(numbers)

# Use with print statment also.
print("Python allows breaking long lines \
for better readability.")
