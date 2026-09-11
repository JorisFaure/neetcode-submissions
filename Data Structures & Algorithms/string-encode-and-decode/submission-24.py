class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs :
            l = str(len(word))
            word = l+'#'+word
            res+=word
        
        return res


    def decode(self, s: str) -> List[str]:
        if not s :
            return []
        res = []

        i = 0

        print(s)
        while i < len(s) :
            curr_len = 0
            while s[i] != '#' :
                curr_len = curr_len*10 + ord(s[i]) - ord('0')
                i+=1
            res.append(s[i+1:i+1+curr_len])
            i+=curr_len
            i+=1
        return res
