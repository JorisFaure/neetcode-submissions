class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordSet = set(wordDict)
        self.memo = {}

        def rec(curr_i) :
            if curr_i in self.memo :
                return self.memo[curr_i]
            if curr_i == len(s) :
                return True

            for i in range(curr_i, len(s)) :
                if s[curr_i:i+1] in wordSet and rec(i+1) :
                    self.memo[curr_i] = True
                    return True
            self.memo[curr_i] = False
            return False
        return rec(0)
        