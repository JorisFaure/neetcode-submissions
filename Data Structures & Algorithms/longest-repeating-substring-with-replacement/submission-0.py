class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        occurences = {}
        start = 0
        end = 0
        max_occur = float('-inf')
        max_total = 0
        current_max = 0

        while end < len(s) :
            #min_occur = min(min_occur, occurences[s[end]])
            occurences[s[end]] = occurences.get(s[end], 0) + 1
            max_occur = max(max_occur, occurences[s[end]])
            while (end - start + 1) - max_occur > k :
                occurences[s[start]] -= 1
                if occurences[s[start]] == 0 :
                    occurences.pop(s[start])
                start += 1
            
            max_total = max(end - start + 1, max_total)
            end+=1
        return max_total
            #elif len(occurences) == 2 and min_occur > 2 :


            
        