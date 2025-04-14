# Python program to swap two variables
# method 1
print("method 1")
x = "parth"
y = "krishna"

# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

# method 2 # this method is only for the int value variable only with using any 3rd variable.
print("method 2")
x, y = 10, 50

x = x + y
y = x - y
x = x - y

print(f"updated x = {x} & y = {y}")

# method 3
print("method 3")
x, y = "Ram", "Sita"

x, y = y, x

print(f"updated x = {x} & y = {y}")

# method 4 # using xor(^)(it only use when the variable value data type is integer).
print("method 4")
x, y = 10, 50

x = x ^ y  
y = x ^ y  
x = x ^ y  

print("x:", x)
print("y:", y)
