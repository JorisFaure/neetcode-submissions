class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hs = {}
        ht = {}

        if len(s) != len(t) :
            return False

        for i in range(len(s)) :
            hs[s[i]] = hs.get(s[i], 0) + 1
            ht[t[i]] = ht.get(t[i], 0) + 1
        
        return hs == ht

        