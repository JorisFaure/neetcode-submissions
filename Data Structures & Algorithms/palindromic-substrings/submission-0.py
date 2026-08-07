class Solution:
    def countSubstrings(self, s: str) -> int:
        self.res = 0

        def findPalindrome(i) :
            left = i
            right = i

            while left >=0 and right < len(s) and s[left]==s[right] :
                self.res+=1
                left-=1
                right+=1
            
            left = i
            right = i+1

            while left >=0 and right < len(s) and s[left]==s[right] :
                self.res+=1
                left-=1
                right+=1
            return
            




        for i in range(len(s)) :
            findPalindrome(i)
        
        return self.res




        