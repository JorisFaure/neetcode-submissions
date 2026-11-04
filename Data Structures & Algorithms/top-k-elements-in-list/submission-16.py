class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        histo = {}

        for n in nums :
            histo[n] = histo.get(n, 0) + 1

        heap = []

        for val, freq in histo.items() :
            heapq.heappush(heap, (freq, val))

            if len(heap) > k :
                heapq.heappop(heap)

        res = []

        while heap :
            freq, val = heapq.heappop(heap)
            res.append(val)
        return res


        