class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        corres = {']' : '[', '}' : '{', ')' : '(',}
        for c in s :
            if c in corres :
                if not stack or stack[-1] != corres[c] :
                    return False
                stack.pop()
            else :
                stack.append(c)
        return len(stack) == 0
            
