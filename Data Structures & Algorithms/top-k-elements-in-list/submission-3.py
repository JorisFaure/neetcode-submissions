class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_h = {}
        frq_table = [[] for i in range(len(nums) + 1)]

        for n in nums :
            freq_h[n] = freq_h.get(n, 0) + 1
        
        for num, count in freq_h.items() :
            frq_table[count].append(num)
        
        res = []
        for i in range(len(frq_table) - 1, -1, -1) :
            for nums in frq_table[i] :
                res.append(nums)
                if len(res) == k :
                    return res



        