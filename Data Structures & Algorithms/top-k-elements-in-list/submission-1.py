class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_h = {}
        frq_table = [[] for i in range(len(nums) + 1)]

        for n in nums :
            freq_h[n] = freq_h.get(n, 0) + 1
        
        for keys in freq_h :
            print(keys)
            print(freq_h[keys])
            frq_table[freq_h[keys]].append(keys)
        
        res = []
        for i in range(len(frq_table) - 1, -1, -1) :
            while len(frq_table[i])>0 and k > 0 :
                res.append(frq_table[i].pop())
                k-=1
            if k == 0 :
                break
        
        return res



        