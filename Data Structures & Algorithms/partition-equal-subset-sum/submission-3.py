class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2: return False

        target = sum(nums) // 2
        dp = set() # represents all possible sums so far
        dp.add(0)

        for n in nums:
            dummy_dp = set() # don't need to assign dummy_dp = dp b/c we're gonna add every element from dp in the nested loop
            
            for t in dp:
                if (n+t) == target: return True

                dummy_dp.add(n+t) # adding n
                dummy_dp.add(t) # not adding n
            
            dp = dummy_dp
        
        return target in dp
            
        
        