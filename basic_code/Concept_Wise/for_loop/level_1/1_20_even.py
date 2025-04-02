# Method 1 (with modulo condition)
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)


# # Method 2 (with range + step of gap)
# for i in range(2, 20, 2):
#     print(i)



# Method 3(with isEven Custom function)
def isEven(n):
    isEven = True
    for i in range(1, n+1):
        if isEven == True:
            # print(i, isEven)
            isEven = False
            # print(i, isEven)
        else:
            # print(i, isEven)
            isEven = True
            print(i, isEven)

 
    return isEven

n = 20
if isEven(n) == True:
    print("Even")
else:
    print("Odd")