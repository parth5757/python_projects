# Method 1
print("Method 1")
for i in range(1, 21):
    if i % 2 != 0:
        print(i)
    else:
        continue

# Method 2
print("Method 2")
for i in range(1, 21, 2):
    print(i)

# Method 3
print("Method 3")
odd_numbers = [i for i in range(1, 21) if i%2 != 0]
for num in odd_numbers:
    print(num)

# Method 4
print("Method 4")
def isOdd(n):
    isOdd = False
    for i in range(1, n+1):
        if isOdd == False:
            print(i)
            isOdd = True
        else:
            isOdd=False

    return isOdd
n=20
if isOdd(n)==True:
    print(f"{n} is Odd")
else:
    print(f"{n} is Even")

# Method 5
print("Method 5")
for i in range(1, 21):
    if i & 1:
        print(i)
# Method 5 ni explanation

# & bitwise operator is only use in the for finding odd number not even number

# 1 in binary  → 0001
# 1 in binary  → 0001
# ---------------
# Result        → 0001 → 1 # last digit is match with 1 digit

