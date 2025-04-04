n = int(input("enter number you want: "))
# method 1
print("method 1")
is_prime = True
for i in range(2, int(n**0.5) + 1):
    # print(2, n,  n**0.5, 1)
    # print(i)
    if n % i == 0:
        is_prime = False
        break
if n < 2:
    print(f"{n} is not prime number")
elif is_prime:
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")



# method 2
print("method 2")
is_prime = True
# here range 1 is not start
for i in range(2, n):
    # print(n, i, n % i)
    if n % i == 0:
        is_prime = False
        break
if n < 2:
    print(f"{n} is not prime number")
elif is_prime:
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")


# method 3
print("method 3")
if n < 2:
    print(f"{n} is not prime number")
elif n == 2:
    print(f"{n} is prime number")
elif n % 2 == 0:
    print(f"{n} is not prime number")
else:
    is_prime =True
    for i in range(3, n, 2):
        if n % i == 0:
            is_prime = False
    if is_prime:
        print(f"{n} is prime number")
    else:
        print(f"{n} is not prime number")

# you can also use math.sqrt function to find the square root


# method 4 
print("method 4") # it count how many number is divide by the an n numbers if it will 2 then it ok that 1 and that same n number
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        # print(i)
        count += 1

if count == 2:  # Prime numbers have exactly two divisors (1 and itself)
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")


# method 5 
print("method 5") # list comprehension
divisors = [i for i in range(1, n+1) if n % i ==0]
# print(divisors) # it store only the number which division will be zero by 1 or that n number which entered

if len(divisors) == 2:
    # print(len(divisors))
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")


# method 6
print("method 6") # recursion 

