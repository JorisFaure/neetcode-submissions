class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        meet = set()

        for n in nums :
            if n in meet :
                return n
            meet.add(n)


        