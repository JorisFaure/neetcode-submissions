class Solution:
    res = 0
    def climbStairs(self, n: int) -> int:
        def rec(n_stair, n) :
            if n - n_stair == 0 :
                self.res += 1
                return
            if n - n_stair < 0 :
                return
            n -= n_stair
            rec(1, n)
            rec(2, n)
            return
        rec(0, n)
        return self.res
            

        