# Sum of numbers from 1 to n using recursion
def recursive_sum(n):
    print(f"Entering recursive_sum({n})")  # Step print
    if n == 1:
        print(f"Base case reached: returning 1")
        return 1
    else:
        result = n + recursive_sum(n - 1)
        print(f"Returning {result} for recursive_sum({n})")
        return result

print("Final result:", recursive_sum(4))


# # simple sum
# def total_sum(n):
#     total = 0 
#     print("Before for loop")
#     for i in range(1, n+1):
#         print("it's I:", i)
#         total = total + i
    
#     return total

# print(total_sum(4))


def print_str(s:str):
    n = len(s)
    print(f"entering in string {n}")
    if n == 0:
        print("Last step reached at s[0] 1")
    else:
        result = print_str(s[0: n-1])
        print(f"Returning {s[0: n]} ({n})")        
        return 

s = "parth"
print(print_str(s))
# s = "parth"
# n = len(s)
# print(s[0:n+1])

''' recursion always not in reverse it depend on your code here example it on the one
forward manner it also work '''
def print_forward(s, idx=0):
    if idx == len(s):
        return
    print(s[idx])
    print_forward(s, idx + 1)

print_forward("parth")