class Solution:
    def isPalindrom(self, s) :
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr_path = []

        def rec(index) :
            if index == len(s) :
                res.append(curr_path[:])
                return
            
            for i in range(index, len(s)) :
                if self.isPalindrom(s[index:i+1]) :
                    curr_path.append(s[index:i+1])
                    rec(i+1)
                    curr_path.pop()
        rec(0)
        return res

        