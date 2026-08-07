import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        heap = []
        for n in nums :
            h[n] = h.get(n, 0) + 1
        print(h)
        for key in h :
            heapq.heappush(heap, (-h[key], key))
        res = []
        while k > 0 :
            _, key = heapq.heappop(heap)
            res.append(key)
            k-=1
        return res



        