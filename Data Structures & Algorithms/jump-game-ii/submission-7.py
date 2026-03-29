class Solution:
    def jump(self, nums: List[int]) -> int:
        r, l, count = 0, 0, 0

        while r < len(nums) - 1:
            maxIndex = 0
            for i in range(l, r+1):
                maxIndex = max(maxIndex, i + nums[i])
            l = r + 1
            r = maxIndex
            count += 1
        
        return count


            

