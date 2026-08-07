class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneMap = {
                    "1": [],
                    "2": ["a", "b", "c"],
                    "3": ["d", "e", "f"],
                    "4": ["g", "h", "i"],
                    "5": ["j", "k", "l"],
                    "6": ["m", "n", "o"],
                    "7": ["p", "q", "r", "s"],
                    "8": ["t", "u", "v"],
                    "9": ["w", "x", "y", "z"],
                    "0": ["+"],
                    "*": [],
                    "#": []
                }
        res = []
        self.current_path = ""
        
        def rec(index) :
            while index < len(digits) and (digits[index] == '1' or digits[index] == '*' or digits[index] == '#') :
                index += 1
            if index == len(digits) :
                if self.current_path:
                    res.append(self.current_path) 
                return
            
            for val in phoneMap[digits[index]] :
                self.current_path+=val
                rec(index+1)
                self.current_path = self.current_path[:-1]
            return
        
        rec(0)
        return res
        