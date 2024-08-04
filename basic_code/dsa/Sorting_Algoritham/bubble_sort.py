'''
Initial List:
csharp
Copy code
[7, 6, 0, 3, 5]
Pass 1:
Compare 7 and 6, and swap them since 7 > 6.

csharp
Copy code
[6, 7, 0, 3, 5]
Compare 7 and 0, and swap them since 7 > 0.

csharp
Copy code
[6, 0, 7, 3, 5]
Compare 7 and 3, and swap them since 7 > 3.

csharp
Copy code
[6, 0, 3, 7, 5]
Compare 7 and 5, and swap them since 7 > 5.

csharp
Copy code
[6, 0, 3, 5, 7]
List after Pass 1:
csharp
Copy code
[6, 0, 3, 5, 7]
Pass 2:
Compare 6 and 0, and swap them since 6 > 0.

csharp
Copy code
[0, 6, 3, 5, 7]
Compare 6 and 3, and swap them since 6 > 3.

csharp
Copy code
[0, 3, 6, 5, 7]
Compare 6 and 5, and swap them since 6 > 5.

csharp
Copy code
[0, 3, 5, 6, 7]
List after Pass 2:
csharp
Copy code
[0, 3, 5, 6, 7]
Pass 3:
Compare 0 and 3, no swap needed since 0 < 3.

csharp
Copy code
[0, 3, 5, 6, 7]
Compare 3 and 5, no swap needed since 3 < 5.

csharp
Copy code
[0, 3, 5, 6, 7]
Compare 5 and 6, no swap needed since 5 < 6.

csharp
Copy code
[0, 3, 5, 6, 7]
List after Pass 3:
csharp
Copy code
[0, 3, 5, 6, 7]
Pass 4:
Compare 0 and 3, no swap needed since 0 < 3.

csharp
Copy code
[0, 3, 5, 6, 7]
Compare 3 and 5, no swap needed since 3 < 5.

csharp
Copy code
[0, 3, 5, 6, 7]
List after Pass 4:
csharp
Copy code
[0, 3, 5, 6, 7]
Pass 5:
Compare 0 and 3, no swap needed since 0 < 3.
csharp
Copy code
[0, 3, 5, 6, 7]
Final Sorted List:
csharp
Copy code
[0, 3, 5, 6, 7]
'''



# Coding start from here
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        print(f"Pass {i+1}:")
        for j in range(0, n-i-1):
            # Print the comparison of the current pair
            print(f"  Comparing {arr[j]} and {arr[j+1]}")
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                # Print the list after swap
                print(f"  Swapped: {arr}")
            else:
                print(f"  No swap needed")
        
        # Print the list after each pass
        print(f"After pass {i+1}: {arr}\n")
        
        # If no two elements were swapped by the inner loop, then break
        if not swapped:
            break

# Example list
arr = [7, 6, 0, 3, 5]
print(f"Initial list: {arr}\n")
bubble_sort(arr)
print(f"Sorted list: {arr}")
