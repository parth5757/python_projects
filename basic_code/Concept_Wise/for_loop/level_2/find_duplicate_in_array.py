import time
import tracemalloc
tracemalloc.start()
start_time = time.time()
# method 1
arr = [3, 5, 7, 2, 2, 5, 7,94,8,4,1257,5,16,48,45,6,75,4848,497,4,49,49,48,4,4,94,94,9,49,95,74,2,5,769,84,4,6,49,7,]
# print(sorted(set(arr)))

# time complexity for the duplicate element finding is O(n²) # because one for loop which go in all around the array to all element & second if condition check all possible element of element with another array or not and unstr_arr have constant one element is appending in array not all arr element only unique one so it time complexity is O(1), So final answer of finding duplicate element in array time complexity is O(n²)
new_arr = []
for i in range(len(arr)): # O(n)
    if arr[i] not in new_arr: #O(n)
        new_arr.append(arr[i]) # O(1)
arr = new_arr
# time complexity - O(n²) for Bubble Sort
# Bubble Sort has worst-case and average-case time complexity of O(n²)
# print(arr)
n = len(arr)
for i in range(n): #O(n)
    # print("i", i)
    for j in range(0, n-i-1): #O(n²)
        # print("j", j)
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            # print(arr)
end_time=time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print("Final Sorted:", arr)
print(f"Time taken: {end_time - start_time:.6f} seconds")
print(f"Current memory usage: {current / 1024:.2f} KB")
print(f"Peak memory usage: {peak / 1024:.2f} KB")
# Space complexity is for this code is O(n)
# arr stores original elements, new_arr stores unique elements — both are lists of integers.
# So overall, space complexity is O(n), not counting the trace memory overhead 

# # method 2