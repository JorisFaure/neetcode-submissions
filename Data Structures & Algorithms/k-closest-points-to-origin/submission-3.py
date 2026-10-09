class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        h = []

        for [x, y] in points :
            h.append((math.sqrt(x**2+y**2), (x,y)))
        
        heapq.heapify(h)

        print(h)
        res = []

        while k > 0 :
            _, (x,y) = heapq.heappop(h)
            res.append([x,y])
            k-=1


        return res