# Measuring running time growth
# time complexity




# Big O notation is used to measure how running time or space requirements for your program grow as input size.
# Big O notation is always use in find in worst case scenario
# (Big O notation not show an always perfect time and space complexity it giv you ruff idea of them.)
        # |           
        # |                    /
        # |                  /
        # |                /
   #T   # |              / 
   #I   # |            /
   #M   # |          /
   #E   # |        /
        # |      /
        # |    /
        # |  /
        # |/
        # |____________________________________
        # |
        # |
                    # Size(arr) or n

import time

def foo(arr):
    begin = time.time()
    for i in range(1, arr+1):
        count =+ i
        print(count)
    end = time.time()
    print(end - begin)
arr1 = 10
foo(arr1)
#o/p = 0.0029
arr2 = 100
foo(arr2)
#o/p = 0.029

# to find time complexity there are some rule

# time = a*n(size of arr) + b

# 1. keep fastest growing term here is a*n n size changeing(increasing)

# time = a*n

#2. Drop the constant element

# time = O(n)

# Example for this

def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n * n)
    return squared_numbers

numbers = [5,88, 46, 94]
a = get_squared_numbers(numbers)
print(a)



#  Constant function


        # |           
        # |                   
        # |                  
        # |                
   #T   # |              
   #I   # |            
   #M   # |          
   #E   # |        
        # |      
        # |    
        # |  
        # |_/\__/\__/\____/\__/  \_______/\___
        # |____________________________________
        # |
        # |
                    # Size(arr) or n


# time = a

# 1. keep fastest growing term
# 2. Drop constants

# time = O(1)

# Example

def find_first_pe(prices, eps, index):
    pe = prices[index]/eps[index]
    return pe

# (n(square))
# time = a*n² + b

#Examples

nums = [3,6,2,4,3,6,8,9]
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j]:
            print(nums[i], "is duplicate")
            break

# time = a * n² + b

# 1. keep fastest growing term
# 2. Drop constants

# time = O(n²)


nums1 = [3,6,2,4,3,6,8,9]
duplicate = None
for i in range (len (nums1)):
    for j in range(i+1, len(nums1)): #n² iterations
        if nums1[i] == nums1 [j]:
            duplicate = nums1[i]
            break
for i in range (len (nums1)): #n iterations
    if nums1[i] == duplicate:
        print(i)            

# time = a*n² + b*n + c

# 1. keep fastest growing term
# time = a*n² + b*n
# time = a*n²
# 2. Drop constants
# time = O(n²)


# Measuring running space growth
# space complexity

#  search 68
num2 = [4,9,15,21,34,57,68,91]

for i in range(len(num2)):
    if num2[i] == 68:
        print("index is", i)

# space complexity is  O(n)


# Binary Search here use
# [4,9,15,21,34,57,68,91] Search 68

# now 21 is taken middle value
# [4,9,15,21,34,57,68,91] from middle value to left side all element value check which is smaller then 68 so all element discarded            Iteration 1 = n/2

# [34,57,68,91] now 57 is middle value and from there all left side element removed      Iteration 2 = (n/2)/2 = n/2²

# [69, 91] now 57 is middle value and 68 here match it return the element      Iteration 3 = (n/2²)/2 = n/2³


# log still remaining