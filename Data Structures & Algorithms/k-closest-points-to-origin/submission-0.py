import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [-math.sqrt(p[0]**2 + p[1]**2) for p in points]
        h = []
        for i, d in enumerate(distances) :
            heapq.heappush(h, (d,i))
            print(h)
            if len(h)>k :
                heapq.heappop(h)
        res = [points[x[1]] for x in h]
        return res