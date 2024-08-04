# Prime number means that number is only divided by that own number or 1
'''
For example:

The number 2 is a prime number because its only divisors are 1 and 2.
The number 3 is a prime number because its only divisors are 1 and 3.
The number 4 is not a prime number because it can be divided by 1, 2, and 4 (4 = 2 × 2).
The number 5 is a prime number because its only divisors are 1 and 5.
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, and so on.
'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        # print(int(n ** 0.5) )
        if n % i == 0:
            return False
    return True

# Test the function
print(is_prime(11))  # Output: True
print(is_prime(4))   # Output: False


