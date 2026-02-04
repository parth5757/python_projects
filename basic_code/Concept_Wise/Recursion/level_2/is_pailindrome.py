def reverse_number(n, rev=0):
    if n == 0:
        return rev
    
    return reverse_number(n//10, rev * 10 + n % 10)

def isPalindrome(n):
    original = abs(n)
    return reverse_number(original) == original

# for string
# def isPalindrome(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return isPalindrome(s[1:-1])

if __name__ == "__main__":
    n = 12321
    # n = "AAPPAA"
    if isPalindrome(n):
        print("True")
    else:
        print("False")