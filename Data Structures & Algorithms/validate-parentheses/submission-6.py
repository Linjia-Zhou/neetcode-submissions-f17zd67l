from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else: 
                # "if stack" is checking if stack is empty
                if stack and ((stack[-1] == '(' and ch == ')') or
                    (stack[-1] == '[' and ch == ']') or
                    (stack[-1] == '{' and ch == '}')):
                    stack.pop()
                else:
                    return False
        
        return not stack
                