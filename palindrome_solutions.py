"""Solution using inbuilt functions, debateably not efficient due to using extra memory"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_value = ''
        for x in s:
            if x.isalnum():
                string_value += x.lower()
                
        return string_value == string_value[::-1]
        