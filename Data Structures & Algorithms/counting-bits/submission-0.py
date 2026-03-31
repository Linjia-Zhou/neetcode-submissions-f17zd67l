class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]

        for num in range(1, n+1):
            count = 0
            while num:
                num = num & (num-1)
                count += 1
            ans.append(count)
        
        return ans
