class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def createAnagrams(s1) :
            h1 = [0]*26
            for i in range(len(s1)) :
                h1[ord(s1[i]) - ord('a')] += 1
            return h1
        
        anagrams = defaultdict(list)

        output = []

        for i, words in enumerate(strs) :
            w1 = createAnagrams(words)
            anagrams[tuple(w1)].append(words)

        
        return list(anagrams.values())

            


        