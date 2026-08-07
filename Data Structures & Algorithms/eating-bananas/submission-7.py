import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #On sais que notre rate est entre 1 et le max de la pile (donc 4 dans le 1er exemple)
        #On prend le rate du milieu : 2, on parcours la liste avec 2, si on met trop de temps, on fait une dichotomie sur la moitié sup
        #Sinon dichotomie sur la moitié inf

        left = 1
        right = max(piles)
        min_h = right
        while left <= right :
            mid = (right - left) // 2 + left
            current_time_to_eat = 0
            for i in range(len(piles)) :
                current_time_to_eat += math.ceil(piles[i]/mid)
            if current_time_to_eat > h :
                left = mid + 1
            else :
                min_h =min(min_h, mid)
                right = mid - 1
        return min_h
        


        