class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.end = len(cost)
        self.memo = {}
        def climb(step) :
            if step >= self.end :
                return 0
            if step in self.memo :
                return self.memo[step]
            
            self.memo[step] = cost[step] + min(climb(step+1), climb(step+2))
            return self.memo[step]
        x = climb(0)
        y = climb(1)
        return min(x, y)
        