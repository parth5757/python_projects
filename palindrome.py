#Example 1:
#Input: s = "A man, a plan, a canal: Panama"
#Output: true
#Explanation: "amanaplanacanalpanama" is a palindrome.
#Example 2:

#Input: s = "race a car"
#Output: false
#Explanation: "raceacar" is not a 
# 6.
#Example 3:

#Input: s = " "
#Output: true
#Explanation: s is an empty string "" after removing non-alphanumeric characters.
#Since an empty string reads the same forward and backward, it is a palindrome.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Ensure consistent use of spaces or tabs here

        clean_str = ''.join(letter for letter in s if letter.isalnum()).lower()
        print(clean_str)
        return clean_str == clean_str[::-1]


sol = Solution()
s = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(s))