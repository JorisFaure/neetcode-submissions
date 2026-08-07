class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1
        while left < right :
            while left < right and not s[left].isalpha() and not s[left].isnumeric() :
                left += 1
            while left < right and not s[right].isalpha() and not s[right].isnumeric() :
                right -= 1
            if s[left] != s[right] :
                return False
            left += 1
            right -= 1
        return True