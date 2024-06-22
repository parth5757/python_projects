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


