class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs :
            histo = [0]*26
            for c in s :
                histo[ord(c)-ord('a')]+=1
            res[tuple(histo)].append(s)
        return list(res.values())






        