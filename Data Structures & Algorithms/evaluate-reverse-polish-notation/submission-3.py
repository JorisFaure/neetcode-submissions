class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens :
            print(stack)
            if t[0] == '-' and len(t) > 1 :
                n = int(t[1:])
                stack.append(-n)
            elif t[0].isdigit() :
                n = int(t)
                stack.append(n)
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                if t == "+" :
                    stack.append(op1+op2)
                if t == "*" :
                    stack.append(op1*op2)
                if t == "/" :
                    stack.append(int(op2/op1))
                if t == "-" :
                    stack.append(op2-op1)
            
        return stack[-1]
        