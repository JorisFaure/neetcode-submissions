class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 :
            return ""
        if len(strs) == 1 :
            return strs[0]
        res = ""
        for i, letter in enumerate(strs[0]) :
            for word in strs[1::] :
                if i >= len(word) or word[i] != letter :
                    return res
            res+=letter
        return res
        