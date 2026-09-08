class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        s = {}

        for i, n in enumerate(numbers) :
            r = target-n
            if r in s :
                return [s[r] + 1, i + 1]
            s[n] = i
        return [-1, -1]