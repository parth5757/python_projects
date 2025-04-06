import time
# method 1
arr = [3, 5, 7, 2, 2, 5, 7,94,8,4,1257,5,16,48,45,6,75,4848,497,4,49,49,48,4,4,94,94,9,49,95,74,2,5,769,84,4,6,49,7,]
# print(sorted(set(arr)))

unsrt_arr = []
start = time.time()
for i in range(len(arr)): # O(n)
    if arr[i] not in unsrt_arr: #O(n)
        unsrt_arr.append(arr[i])
arr = unsrt_arr
print(arr)
n = len(arr)
for i in range(n):
    print("i", i)
    for j in range(0, n-i-1):
        # print("j", j)
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            # print(arr)
print(arr)
end=time.time()
print(end-start)
# method 2
