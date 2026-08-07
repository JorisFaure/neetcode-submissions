import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones :
            heapq.heappush(heap, -s)
        while len(heap) > 1 :
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            if x == y :
                continue
            if x < y :
                heapq.heappush(heap, -(y-x))
            else :
                heapq.heappush(heap, -(x-y))
        if len(heap) > 0 :
            return -heap[0]
        return 0