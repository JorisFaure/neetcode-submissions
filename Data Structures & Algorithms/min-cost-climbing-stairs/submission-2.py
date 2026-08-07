class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memo = {}
        def dfs(step) :
            if step >= len(cost) :
                return 0
            if step in self.memo :
                return self.memo[step]
            
            self.memo[step] = cost[step] + min(dfs(step+1), dfs(step+2))
            return self.memo[step]
        left = dfs(0)
        right = dfs(1)

        return min(left, right)

        