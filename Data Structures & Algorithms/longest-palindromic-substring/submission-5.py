class Solution:
    def longestPalindrome(self, s: str) -> str:

        self.res = ""

        def isPalindrome(s) :
            return s == s[::-1]

        def rec(start) :
            if start >= len(s) :
                return


            
            for i in range(len(s)-start):
                curr_word = s[start:start+i+1]
                if isPalindrome(curr_word) :
                    if len(self.res) < len(curr_word) :
                        self.res = curr_word
            
        for i in range(len(s)) :
            rec(i)

        return self.res 

            



        
        