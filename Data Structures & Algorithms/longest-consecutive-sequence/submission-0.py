class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        begins = set()
        for n in nums :
            if not n-1 in num_set :
                begins.add(n)
        longest = 0
        for b in begins :
            curr = 1
            while b+1 in num_set :
                curr+=1
                b+=1
            longest = max(longest, curr)
        return longest

        
        