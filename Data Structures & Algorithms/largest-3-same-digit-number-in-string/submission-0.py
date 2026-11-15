class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = -1

        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]: ans = max(ans, int(num[i:i+3]))
        
        if ans == 0:
            return '000'
        elif ans == -1:
            return ''
        else:
            return str(ans)
            