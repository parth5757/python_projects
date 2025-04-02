n = int(input("Enter the number  till you have to print: "))
# method 1
print("method 1")
for i in range(int(n)):
    print(i+1)

# method 2
print("method 2")
for i in range(1, n+1):
    print(i)

# method 3
print("method 3")
print("".join(map(str, range(1, n+1))))

# method 4
print("method 4")
def n_num_gen(n):
    for i in range(1, n+1):
        yield i
for num in n_num_gen(n):
    print(num)

# method 5
print("method 5")
numbers = [i for i in range(1,n+1)]
print(numbers)

# method 6
print("method 6")
for i, val in enumerate(range(1, n+1)):
    print(val)

# # "method 2"
# print("method 2")
# i = 1
# while i <= int(n):
#     print(i)
#     i += 1