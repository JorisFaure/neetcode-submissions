class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs :
            res+=(str(len(word)) + '#' + word)
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l = len(s)
        i = 0
        curr_num = 0
        if l == 2 :
            return [""]
        while i < l - 2 :
            while '0'<=s[i]<='9' :
                curr_num = curr_num*10 + int(s[i])
                i+=1
            w = s[i+1:i+1+curr_num]
            res.append(w)
            i = i+1+curr_num
            curr_num = 0

        return res


            
        