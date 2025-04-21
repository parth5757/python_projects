import time
import random

# for i in range(1, 1000000000):
#     numbers.append(random.randrange(1, 100000000000))
          
# method 1
print("method 1")
def bubble_sort(numbers):
    # bubble sort method used 
    start = time.time()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            # print("Before",i, j , numbers) # just for the reference how the logic is actually working
            if numbers[i] > numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
            # print("After", numbers)
    print("time required in bubble sort: ", time.time() - start)
    # print(numbers)
    return "second largest number is: ", numbers[-2]

# # own quick sort method totally wrong becuase it work on some non median value list array if distributed array median value come then It will not work(one thing is remaining here it that quick sort recusing )
# def quick_sort(numbers):
#     pivot = int(len(numbers) // 2)
#     print(numbers[pivot])
#     print(numbers)
#     left = []
#     right = []
#     for i in range(0, len(numbers)):
#         if numbers[i] < numbers[pivot]:
#             left.append(numbers[i])
#         else:
#             pivot = i
#             # print(pivot, numbers[i])
#             # pivot = numbers[i]
#             right.append(numbers[i])
#     print(left + right)


# quick sort
def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = len(numbers) // 2
    # print(numbers[pivot])
    left = [x for x in numbers if x < numbers[pivot]]
    mid = [x for x in numbers if x == numbers[pivot]]
    right = [x for x in numbers if x > numbers[pivot]]
    numbers = quick_sort(left) + mid + quick_sort(right)
    # second_largest = numbers[-2]  # not working this thing here so extra sorted_numbers variable add then print the second_largest value because of the 3 total 3 time the quick sort program is called in recursive maner
    # print(second_largest)
    return numbers


numbers = [12, 45, 78, 90, 56, 89]
print("using bubble sort: ",bubble_sort(numbers))
numbers = [12, 45, 78, 90, 56, 89]
sorted_numbers = quick_sort(numbers)
print("using quick sort: ", f"second largest number is: {sorted_numbers[-2]}")