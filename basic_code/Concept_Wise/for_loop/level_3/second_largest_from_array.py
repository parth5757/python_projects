# method 1
print("method 1")
numbers = [12, 45, 78, 90, 56, 89]
def bubble_sort(numbers):
    # bubble sort method used 
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            # print("Before",i, j , numbers) # just for the reference how the logic is actually working
            if numbers[i] > numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
            # print("After", numbers)
    return "second largest number is: ", numbers[-2]



print(bubble_sort(numbers))