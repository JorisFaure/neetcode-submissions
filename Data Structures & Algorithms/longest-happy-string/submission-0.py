import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        max_heap = []
        if a > 0 :
            heapq.heappush(max_heap, (-a, 'a'))
        if b > 0 :
            heapq.heappush(max_heap, (-b, 'b'))
        if c > 0 :
            heapq.heappush(max_heap, (-c, 'c'))

        res = ""
        freq_temp, letter_temp = None, None
        while max_heap :
            freq, letter = heapq.heappop(max_heap)
            if len(res) > 1 :
                if letter == res[-1] and letter == res[-2] :
                    freq_temp, letter_temp = freq, letter
                    if not max_heap :
                        return res
                    freq, letter = heapq.heappop(max_heap)
            freq += 1
            res += letter
            if freq < 0 :
                heapq.heappush(max_heap, (freq, letter))
            if freq_temp :
                heapq.heappush(max_heap, (freq_temp, letter_temp))
                freq_temp = None
        return res

        

        