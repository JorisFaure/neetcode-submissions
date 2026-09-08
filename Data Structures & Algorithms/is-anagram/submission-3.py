class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        histo_a = [0]*26
        histo_b = [0]*26

        for c in s :
            histo_a[ord(c)-ord('a')] += 1
        for c in t :
            histo_b[ord(c)-ord('a')] += 1
        return histo_a == histo_b