from collections import deque
import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.truediv}
        
        if len(tokens) == 1: return int(tokens[0])
        stack = deque()

        for ch in tokens:
            if ch.lstrip('-').isdigit():
                stack.append(ch)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                ans = ops[ch](num1, num2)
                stack.append(ans)
        
        return int(stack.pop())