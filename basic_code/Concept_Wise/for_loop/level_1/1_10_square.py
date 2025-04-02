# Method 1
print("Method 1")
for i in range(1, 11):
    print(i ** 2)

# Method 2
print("Method 2")
for i in range(1, 11):
    print(f"{i}² = {i * i}")

# Method 3
print("Method 3")
current_odd = 1
sum_sq = 0
for _ in range(1,11):
    # print(current_odd, sum_sq) # Just for reference
    sum_sq += current_odd
    print(sum_sq)
    current_odd += 2 
    # print(current_odd) #Just for reference