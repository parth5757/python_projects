def are_anagrams(str1, str2):
    
    def bubble_sort(str):
        for i in range(0, len(str)):
            for j in range(i+1, len(str)):
                if str[j] < str[i]:
                    temp = str[j]    
                    str[j] = str[i]    
                    str[i] = temp    
        return str

    def quick_sort(str):



    sorted_str1 = bubble_sort(list(str1))
    print(sorted_str1)
    sorted_str2 = sorted(str2)
    print(sorted_str2)

    return sorted_str1 == sorted_str2
# Test the function
print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))    # Output: False