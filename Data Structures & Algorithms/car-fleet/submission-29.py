import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) < 2 :
            return len(position)
        
        cars = sorted(zip(position, speed), reverse=True)

        stack = []

        for pos, spe in cars :
            time_to_end = (target - pos) / spe

            if not stack or stack[-1] < time_to_end :
                stack.append(time_to_end)

        
        return len(stack)




        
        