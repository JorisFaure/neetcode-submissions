class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        histo = {}
        max_freq = 0
        res = 0

        start = 0

        for end in range(len(s)) :
            histo[s[end]] = histo.get(s[end], 0) + 1

            max_freq = max(max_freq, histo[s[end]])

            while (end - start + 1) - max_freq > k :
                histo[s[start]] = histo[s[start]] - 1
                start += 1
            res = max(res, end - start + 1)

        return res
        


        



        