class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        output = []
        for i, words in enumerate(strs) :
            h1 = [0]*26
            for i in range(len(words)) :
                h1[ord(words[i]) - ord('a')] += 1
            anagrams[tuple(h1)].append(words)
        return list(anagrams.values())

            


        