class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = [[] for i in range(len(nums) + 1)]

        h = {}

        for n in nums :
            h[n] = h.get(n, 0) + 1
        
        for (n, f) in h.items() :
            freq[f].append(n)

        res = []
        for i in range(len(freq)-1, -1, -1) :
            
            for n in freq[i] :
                res.append(n)
                if len(res) == k :
                    return res
            

        