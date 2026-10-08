class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        max_conseq = 0

        view = set()

        for n in nums :
            view.add(n)
        
        i = 0
        while i < len(nums) :
            curr_conseq = 1
            val = nums[i]
            if val - 1 not in view :
                while val+1 in view :
                    curr_conseq+=1
                    val = val+1
                max_conseq = max(max_conseq, curr_conseq)
            i+=1
        return max_conseq
            

        