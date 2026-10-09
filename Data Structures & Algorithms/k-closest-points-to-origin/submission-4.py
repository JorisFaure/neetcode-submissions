class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        h = []

        for [x, y] in points :
            heapq.heappush(h, (-math.sqrt(x**2+y**2), (x,y)))

            if len(h) > k :
                heapq.heappop(h)

        print(h)
        res = []

        while k > 0 :
            _, (x,y) = heapq.heappop(h)
            res.append([x,y])
            k-=1


        return res