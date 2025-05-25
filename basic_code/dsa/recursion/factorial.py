# fact with recursion 
def fact(n):
    # print(n)
    if n == 0:
        return 1
    else:
        print("n:", n)
        print(n * fact(n-1))
        return n * fact(n-1)
    
print(fact(5))


# factorial without recursion
# def fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact * i
#     return fact
# print(fact(5))