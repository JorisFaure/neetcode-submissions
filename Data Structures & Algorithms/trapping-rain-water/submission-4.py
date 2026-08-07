class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3 :
            return 0

        l = 0
        r = len(height)-1
   
        left_max = height[0]
        right_max = height[len(height)-1]

        total = 0

        while l < r :

            if left_max < right_max :
                l+=1
                left_max = max(left_max, height[l])
                total+=(left_max - height[l])
            else :
                r -= 1
                right_max = max(right_max, height[r])
                total+=(right_max - height[r])
        return total

