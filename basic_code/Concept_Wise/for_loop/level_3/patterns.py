# *
# **
# ***
# ****
# *****
n = int(input("Enter number you want: "))
for i in range(n):
    print((i+1) * "*")


# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 

num = 1
for i in range(n):
    for j in range(i+1):
        print(num, end=" ")
        num += 1
    print()

# num = 1
# for i in range(n):
#     total_spae = (n-i-1)
#     space_count =[]
#     for j in range(i+1):
#         if i not in space_count:
#             space_count.append(i)
#             print(total_spae * " ", num, end=" ")
#         else:
#             print(num, end=" ")
#         num += 1
#     print()


#      *
#     **
#    ***
#   ****
#  *****
for i in range(n):
    total_spae = (n-i-1)
    print(total_spae * " ",(i+1) * "*")



#     *
#    * *
#   * * *
#  * * * *
# * * * * *
for i in range(n):
    total_spae = (n-i-1)
    print(total_spae * " ",(i+1) * "* ")



# *****
# *****
# *****
# *****
# *****
for i in range(n):
    print("*" * n)


# *****
# *   *
# *   *
# *   *
# *****
for i in range(n):
    if i==0 or i == n-1:
        print(n* "*")
    else:
        print("*"+(" "*(n-2))+"*")


# * * *
# *   *
# *   *
# *   *
# * * *
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()