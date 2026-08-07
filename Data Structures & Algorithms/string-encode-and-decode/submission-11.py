class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs :
            res+=(str(len(word))+"#"+word)
        return res




    def decode(self, s: str) -> List[str]:
        if not s :
            return []

        
        i = 0
        res = []
        while i < len(s) :
            word_len = 0
            while '0' <= s[i] <= '9' :
                word_len = word_len*10 + int(s[i])
                i+=1
            i+=1
            res.append(s[i:i+word_len])
            i+=word_len
        return res

        
