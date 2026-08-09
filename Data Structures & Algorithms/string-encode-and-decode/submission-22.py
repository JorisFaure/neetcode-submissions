class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for word in strs :
            n = len(word)
            final_str += str(n)
            final_str += '#'
            for i in range(n) :
                final_str += word[i]
        return final_str
            




    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s) :
            j = i

            while s[j] != '#' :
                j+=1
            
            length = int(s[i:j]) #la borne droite est exclu

            i = j+1
            j = i+length

            res.append(s[i:j])
            i = j
            
        return res


