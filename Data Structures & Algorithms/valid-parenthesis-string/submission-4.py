from collections import deque
class Solution:
    def checkValidString(self, s: str) -> bool:
        stars = deque()
        opens = deque()

        # skip every star, star += 1
        # if stack is empty
            # s[i] == '(', simply append
            # s[i] == ')', check if there's stars that weren't used

        for i in range(len(s)):
            if s[i] == '(':
                opens.append(i)
            elif s[i] == ')':
                if len(opens) == 0 and len(stars) == 0:
                    return False
                if len(opens) > 0:
                    opens.pop()
                else:
                    stars.pop()
            else:
                stars.append(i)
        
        while len(opens) > 0:
            if len(stars) == 0 or opens.pop() > stars.pop():
                return False
        
        return True
