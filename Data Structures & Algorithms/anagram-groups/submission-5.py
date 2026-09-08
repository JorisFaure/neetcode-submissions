class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def createHisto(s) :
            histo = [0]*26
            for c in s :
                histo[ord(c)-ord('a')]+=1
            return histo
        
        res = []
        if not strs :
            return []

        res = defaultdict(list)
        
        for s in strs :
            h = createHisto(s)
            res[tuple(h)].append(s)
        
        res = list(res.values())

        return res






        