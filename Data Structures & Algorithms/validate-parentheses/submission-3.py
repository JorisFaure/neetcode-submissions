class Solution:
    def isValid(self, s: str) -> bool:
        open_sign = {'{', '(', '['}
        closing_sign = {'}' : '{', ')' : '(', ']': '['}

        stack = []

        for c in s :
            if c in open_sign :
                stack.append(c)
            else :
                if not stack or closing_sign[c] != stack.pop() :
                    return False
        return len(stack) == 0


        