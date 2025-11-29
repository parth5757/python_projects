# # Desired Output 432 - 4+3+2=9
# def sum_of_num(val):
#     Val = str(val)
#     n = len(Val)
#     def sum_num(till):
#         if n == -1:
#             return 0
#         else:
#             return int(Val[n-1]) + sum(int(n)-1)
#     ans = sum_num(n)
#     return ans

# print(sum_of_num(432))




def sum_of_num(val):
    val = str(val)
    
    def helper(i):
        if i < 0:
            return 0
        return int(val[i]) + helper(i - 1)
    
    return helper(len(val) - 1)


print(sum_of_num(432))  # Output: 9
