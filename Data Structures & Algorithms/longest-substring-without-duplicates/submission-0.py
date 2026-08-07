class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_longest = 0
        start = 0
        end = 0
        hashmap = {}
        while end < len(s) :
            while s[end] in hashmap :
                hashmap[s[start]] -= 1
                if hashmap[s[start]] == 0 :
                    hashmap.pop(s[start])
                start += 1    
            hashmap[s[end]] = 1
            end+=1
            max_longest = max(max_longest, len(hashmap))
        return max_longest

        