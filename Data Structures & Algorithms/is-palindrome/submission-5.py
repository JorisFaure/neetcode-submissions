class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNum(c) :
            if 'a' <= c <= 'z' or '0' <= c <= '9' :
                return True
            return False
        s = s.lower()

        l = 0
        r = len(s)-1

        while l < r :
            while not isAlphaNum(s[l]) and l < r :
                l+=1
            while not isAlphaNum(s[r]) and l < r :
                r-=1
            if s[l] != s[r] :
                return False
            l+=1
            r-=1
        
        return True
