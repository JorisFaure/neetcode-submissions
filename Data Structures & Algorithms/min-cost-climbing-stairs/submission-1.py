class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def dfs(step) :
            if step >= len(cost) :
                return 0
            return cost[step] + min(dfs(step+1), dfs(step+2))
        left = dfs(0)
        right = dfs(1)

        return min(left, right)

        