# Method 1
print("method 1")
for i in range(1, 11):
    print(f"5 * {i} ", i * 5)

# Method 2
print("method 2")
for index,i in enumerate(range(1, 11)):
    print(f"5 * {index+1} = {5*i}")

# Method 3
print("method 3")
for i, val in zip(range(1,11), [5 * j for j in range(1, 11)]):
    print(f"5 * {i} = {val}")