class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0: return False

        target = nums_sum // 2
        dp = set() 
        dp.add(0)

        for n in nums:
            dummy_dp = set()

            for t in dp:
                if (n+t) == target: return True

                dummy_dp.add(t)
                dummy_dp.add(n+t)
        
            dp = dummy_dp
        
        return target in dp
            

            


