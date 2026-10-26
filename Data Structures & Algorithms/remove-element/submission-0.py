class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last_pos = 0
        for curr_pos in range(len(nums)) :
            if nums[curr_pos] == val :
                continue
            nums[last_pos] = nums[curr_pos]
            last_pos += 1
        
        return last_pos

    
        