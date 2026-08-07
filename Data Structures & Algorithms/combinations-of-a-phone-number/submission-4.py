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
        
        def rec(index, current_path) :
            while index < len(digits) and (digits[index] == '1' or digits[index] == '*' or digits[index] == '#') :
                index += 1
            if index == len(digits) :
                res.append(current_path) 
                return
            
            for val in phoneMap[digits[index]] :
                rec(index+1, current_path+val)
            return
        
        if digits :
            rec(0, "")
        return res
        