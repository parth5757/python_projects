# anagrams string
def anagrams(str1, str2):
    def sorting(str):
        for i in range(0, len(str)):
            for j in range(i+1, len(str)):
                if str[j] < str[i]:
                    temp = str[j]
                    str[j] =str[i]
                    str[i] = temp
                return str
    return sorting(str1) == sorting((str2))
    
print(anagrams("listen", "silent"))


# Bubble Sort
def bubble_sort(s):
    s = list(s)
    for i in range(len(s)):
        for j in range(len(s) - i - 1):
            if s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]
    return ''.join(s)

# Selection Sort
def selection_sort(s):
    s = list(s)
    for i in range(len(s)):
        min_idx = i
        for j in range(i + 1, len(s)):
            if s[j] < s[min_idx]:
                min_idx = j
        s[i], s[min_idx] = s[min_idx], s[i]
    return ''.join(s)

# Insertion Sort
def insertion_sort(s):
    s = list(s)
    for i in range(1, len(s)):
        key = s[i]
        j = i - 1
        while j >= 0 and s[j] > key:
            s[j + 1] = s[j]
            j -= 1
        s[j + 1] = key
    return ''.join(s)

# Quick Sort
def quick_sort(s):
    if len(s) <= 1:
        return ''.join(s)
    pivot = s[0]
    left = [x for x in s[1:] if x <= pivot]
    right = [x for x in s[1:] if x > pivot]
    return quick_sort(left) + pivot + quick_sort(right)

# Merge Sort
def merge_sort(s):
    if len(s) <= 1:
        return ''.join(s)
    mid = len(s) // 2
    left = merge_sort(s[:mid])
    right = merge_sort(s[mid:])
    return merge_lists(left, right)

def merge_lists(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return ''.join(result)

# Test for Anagram using all sorting algorithms
anagram_strings = ["listen", "silent", "enlist", "inlets", "tinsel"]
sorting_algorithms = [bubble_sort, selection_sort, insertion_sort, quick_sort, merge_sort]

for algo in sorting_algorithms:
    print(f"Using {algo.__name__}:")
    sorted_strings = [algo(string) for string in anagram_strings]
    print("Sorted Strings:", sorted_strings)
    print("Are all strings anagrams?", len(set(sorted_strings)) == 1)
    print()



















# def anagrams(str1, str2):
#     def sorting(str):
#         for i in range(0, len(str)):
#             for j in range(i+1, len(str)):
#                 if str[j] < str[i]:
#                     temp = str[j]    
#                     str[j] = str[i]    
#                     str[i] = temp    
#             return str
#     return sorting(str1) == sorted(str2)