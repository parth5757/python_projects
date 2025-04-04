n = int(input("Enter the number of terms: "))
# method 1
print("method 1")
# fib_dict = {0: 1, 1: 1}  # Initialize first two values
# fib_dict.update({i: fib_dict[i-1] + fib_dict[i-2] for i in range(2, n+1)})
# print(fib_dict)

# a,b = b, a+b
a, b = 0, 1
for i in range(n):
    a, b = b, a+b
print(b)


# method 2
print("method 2")
fib_dict = {0:1, 1:1}
[ans := fib_dict.update({0: fib_dict[1], 1:fib_dict[0]+fib_dict[1]}) for i in range(n)]
# for i in range(n):
#     fib_dict.update({0: fib_dict[1], 1:fib_dict[0]+fib_dict[1]})

# print(fib_dict[0])
print(ans)