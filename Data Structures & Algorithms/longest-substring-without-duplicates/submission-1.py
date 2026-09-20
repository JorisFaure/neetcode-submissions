class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        histo = {}

        max_str = 0

        left = 0
        right = 0

        while right < len(s) :
            curr = s[right]
            histo[curr] = histo.get(curr, 0) + 1

            while histo[curr] > 1 :
                l = s[left]
                histo[l] -= 1
                if histo[l] == 0 :
                    histo.pop(l)
                left += 1
            max_str = max(max_str, len(histo))
            right += 1
        return max_str
        