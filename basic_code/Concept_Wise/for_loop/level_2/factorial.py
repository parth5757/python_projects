#method 1
print("method 1")
n = int(input("enter number: "))
ans = 1
for i in range(1, n+1):
    ans *= i
print(f"factorial on {n} is {ans}")

# method 2
print("method 2")
ans = 1
[ans := ans * i for i in range(1, n+1)]
print(f"factorial on {n} is {ans}")


# method 3
print("method 3")
import math
numbers = range(1, n+1)
ans = math.prod(numbers)
print(f"factorial on {n} is {ans}")

# method 4
print("method 4")
from functools import reduce
ans = reduce(lambda x, y: x * y, range(1, n+1)) #learn reduce it have own magic function
print(f"factorial on {n} is {ans}")


# method 5
print("method 5")
ans = {0: 1}
for i in range(1, n+1):
    ans[i] = ans[i-1] * i
    # print(ans[i], i)
print(f"factorial on {n} is {ans[i]}")



# enumerate work but it not feasible at here
# # method 3
# print("method 3")
# ans = 1
# for i, val in enumerate(n):
#     ans *= i
