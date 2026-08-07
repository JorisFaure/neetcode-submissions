class Solution:
    def longestPalindrome(self, s: str) -> str:

        self.res = ""
        self.longest = 0

        def checkPal(i) :

            l = i
            r = i
            while l >= 0 and r < len(s) and s[l]==s[r] :
                if self.longest < (r-l+1):
                    self.longest = (r-l+1)
                    self.res = s[l:r+1]
                l-=1
                r+=1

            l = i
            r = i+1

            while l >= 0 and r < len(s) and s[l]==s[r] :
                if self.longest < (r-l+1):
                    self.longest = (r-l+1)
                    self.res = s[l:r+1]
                l-=1
                r+=1
            return
            
       
        for i in range(len(s)) :
            checkPal(i)

        return self.res 

            



        
        