class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        for n in s :
            s_hash[n] = s_hash.get(n, 0) + 1
        for n in t :
            if n in s_hash :
                s_hash[n]-=1
                if s_hash[n] == 0:
                    del(s_hash[n])
            else :
                return False 
        return len(s_hash) == 0