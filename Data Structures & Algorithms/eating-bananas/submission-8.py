class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles) + 1

        def eat_hours(k) :
            total_hours = 0
            for n in piles :
                total_hours += math.ceil(n/k)
                if total_hours > h :
                    return total_hours
            return total_hours
        
        min_k = max(piles)
        
        while left <= right :
            mid = left + (right - left) // 2

            hours_to_eat = eat_hours(mid)

            if hours_to_eat > h :
                left = mid + 1
            
            if hours_to_eat <= h :
                min_k = min(min_k, mid)
                right = mid - 1
        return min_k



        




        