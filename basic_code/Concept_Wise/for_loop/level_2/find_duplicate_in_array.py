# method 1
arr = [3, 5, 7, 2, 2, 5, 7, 7]
# print(sorted(set(arr)))

unsrt_arr = []
for i in range(len(arr)):
    if arr[i] not in unsrt_arr:
        unsrt_arr.append(arr[i])
arr = unsrt_arr
print(arr)
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)

# method 2
