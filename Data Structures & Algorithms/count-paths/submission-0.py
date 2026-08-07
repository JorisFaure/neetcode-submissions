class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.memo = {}
        def rec(curr_m, curr_n) :
            if curr_m >= m or curr_n >= n :
                return 0
            if (curr_m, curr_n) in self.memo :
                return self.memo[(curr_m, curr_n)]
            if curr_m == m-1 and curr_n == n-1 :
                return 1
            
            down = rec(curr_m+1, curr_n)
            right = rec(curr_m, curr_n+1)
            self.memo[(curr_m, curr_n)] = down+right
            return self.memo[(curr_m, curr_n)]
        return rec(0, 0)
