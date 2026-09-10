class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = [[] for i in range(len(nums))]

        h = {}

        for n in nums :
            h[n] = h.get(n, 0) + 1
        
        for (n, f) in h.items() :
            freq[f-1].append(n)

        res = []
        for i in range(len(nums) - 1, -1, -1) :
            if k == 0 :
                return res
            while 0 < k and freq[i] :
                res.append(freq[i].pop())
                k-=1
        return res

        