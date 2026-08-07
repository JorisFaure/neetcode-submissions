class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}

        for word in strs :
            freq = [0] * 26
            for c in word :
                freq[ord(c) - ord('a')] += 1
            if tuple(freq) not in results :
                results[tuple(freq)] = [word]
            else :
                results[tuple(freq)].append(word)
        return list(results.values())
