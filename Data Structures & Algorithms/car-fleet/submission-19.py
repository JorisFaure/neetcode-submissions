import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = []
        for i, elt in enumerate(position) :
            posSpeed.append([elt, speed[i]])
        posSpeed.sort(key = lambda x: x[0])
        fleets = []
        for i in range(len(posSpeed)-1, -1, -1) :
            time_to_end = (target - posSpeed[i][0]) / posSpeed[i][1]
            if fleets and fleets[-1] >= time_to_end :
                continue
            fleets.append(time_to_end) 
        return len(fleets)
