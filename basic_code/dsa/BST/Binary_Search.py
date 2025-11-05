n = int(input("Enter total len of arr: "))
arr = list(map(int, input("Enter array value space seprated: ").split()))
target = int(input("Enter target: "))

low = 0
high = n - 1
found = -1

while low <= high:
    mid = (low+high)//2
    if(arr[mid]==target):
        found = mid
        break
    elif(arr[mid] < target):
        low = mid + 1
    else:
        high = mid -1

print(found)



# Test Case
# 6
# -1 0 3 5 9 12
# 9