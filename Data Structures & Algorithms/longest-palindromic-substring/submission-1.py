class Solution:
    def longestPalindrome(self, s: str) -> str:

        self.res = ""

        def isPalindrome(s) :
            return s == s[::-1]

        def rec(start) :
            if start >= len(s) :
                return


            curr_word = s[start:]
            for i in range(len(curr_word)):
                if isPalindrome(curr_word[:i+1]) :
                    if len(self.res) < len(curr_word[:i+1]) :
                        self.res = curr_word[:i+1]
            
        for i in range(len(s)) :
            rec(i)

        return self.res 

            



        
        