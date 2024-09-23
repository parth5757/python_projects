# if n = 5 than it do 1*2*3*4*5 = 120
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test the function
print(factorial(5))  # Output: 120