class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pref = [1]*len(nums)
        post = [1]*len(nums)

        for i in range(len(nums)) :
            if i == 0 :
                pref[i] = nums[i]
                post[i-1] = nums[i-1]
                continue
            pref[i] = pref[i-1]*nums[i]
            post[len(nums)-i-1] = post[len(nums)-i]*nums[len(nums)-i-1]
        

        for i in range(0, len(nums)) :
            if i == 0 :
                nums[i] = post[i+1]
            elif i == len(nums)-1 :
                nums[i] = pref[i-1]
            else :
                nums[i] = pref[i-1]*post[i+1]
                nums[len(nums)-i-1] = pref[len(nums)-i-2]*post[len(nums)-i]
        return nums

            

        