# શબ્દને આડાઅવળા ગોઠવીને બનાવેલો નવો શબ્દ, વાક્યોને આડાઅવળા ગોઠવીને બનાવેલા નવા વાક્ય

def are_anagrams(str1, str2):
    # print(sorted(str1), sorted(str2))
    return sorted(str1) == sorted(str2)

# Test the function
print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))    # Output: False