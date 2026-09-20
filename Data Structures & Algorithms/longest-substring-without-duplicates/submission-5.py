class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_occur_index = {}

        max_str = 0

        left = 0
        right = 0

        while right < len(s) :
            curr = s[right]

            if curr in last_occur_index :
                left = max(left, last_occur_index[curr] + 1)

            last_occur_index[curr] = right
            max_str = max(max_str, right - left + 1)

            right += 1
            
        return max_str
        