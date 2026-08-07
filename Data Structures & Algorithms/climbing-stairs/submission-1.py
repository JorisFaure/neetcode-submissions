class Solution:
    res = 0
    def climbStairs(self, n: int) -> int:
        def dfs(i) :
            if n-i == 0 :
                return 1
            if n-i < 0 :
                return 0
            return dfs(i+1) + dfs(i + 2)
        return dfs(0)
            

        