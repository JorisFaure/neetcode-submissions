class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        hashlist = []
        
        for word in strs :
            found = False
            hashmap = {}
            for c in word : #Create hashmap
                hashmap[c] = hashmap.get(c, 0) + 1
            #Check if a similar hashmap was created
            if len(hashlist) > 0 :
                for i, (w, h) in enumerate(hashlist) :
                    if h == hashmap :
                        results[i].append(word)
                        found = True
                        break
            if not found :
                hashlist.append((word, hashmap))
                results.append([word])
        return results
