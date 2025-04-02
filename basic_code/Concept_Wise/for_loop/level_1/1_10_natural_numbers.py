# Method 1
sum = 0 # Most prefer not use the sum as variable because it is inbuilt function
for i in range(1, 11):
    sum += i
print(sum)

# Method 2 (without any variable and use math formula sn=n(n+1)/2)
# print(10(10+1)/2) # it give error because it is 10(10+1) at 10 before the start ( is taken as the function name
print(int(10*(10+1)/2))

# Method 3
del sum # to delete sum variable and use built in sun function
print(sum(i for i in range(1, 11)))

# Method 4
# List comprehension
total = sum([i for i in range (1, 11)])
print(total)


# Method 5
storage = []
for i in range(1, 11):
    storage.append(i)
print(sum(storage))