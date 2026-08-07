import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1 :
            val1 = heapq.heappop(maxHeap)
            val2 = heapq.heappop(maxHeap)
            if val1 == val2 :
                continue
            heapq.heappush(maxHeap, val1 - val2)
        if not maxHeap :
            return 0
        return -maxHeap[0]
