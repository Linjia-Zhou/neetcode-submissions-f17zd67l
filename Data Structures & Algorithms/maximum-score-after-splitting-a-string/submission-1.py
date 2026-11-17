class Solution:
    def maxScore(self, s: str) -> int:
        # number of ones and zeroes to the right of index i
        split = [] # (zeroes to left, ones to right)

        if s[0] == '0':
            split.append((1, s.count('1')))
        else:
            split.append((0, s.count('1') - 1))

        for i in range(1, len(s)-1):
            if s[i] == '0':
                tup = (split[i-1][0] + 1, split[i-1][1])
            else:
                tup = (split[i-1][0], split[i-1][1] - 1)
            split.append(tup)
        
        ans = sum(split[0])
        for tup in split:
            ans = max(ans, sum(tup))
        
        return ans
        
