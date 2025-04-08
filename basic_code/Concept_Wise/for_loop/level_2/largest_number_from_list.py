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