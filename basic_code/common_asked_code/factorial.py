# if n = 5 than it do 1*2*3*4*5 = 120
def factorial(n):
    if n < 0:
        return "enter valid number"
    elif n == 0:
        return 1
    else:
        print( f"recursion: {n-1}")        
        return n * factorial(n-1) # this is recursion

# # Test the function

#  for loop use
# def factorial(n):
#     f = 1
#     for i in range(1,n+1):
#         f*=i
#     return f



# while loop
# def factorial(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers."
#     f = 1
#     counter = n

#     while counter > 0:
#         f *= counter
#         counter -=1
#     return f


print(factorial(5))  # Output: 120
