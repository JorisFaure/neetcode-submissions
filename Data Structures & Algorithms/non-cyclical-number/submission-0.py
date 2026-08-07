class Solution:
    def isHappy(self, n: int) -> bool:
        self.memo = set()
        def rec(n) :
            if n == 1 :
                return True
            if n in self.memo :
                return False
            self.memo.add(n)

            new_number = 0
            
            while n > 0 :
                reste = n % 10
                new_number = new_number + reste**2
                n = n // 10
            return rec(new_number)
        return rec(n)

            
        