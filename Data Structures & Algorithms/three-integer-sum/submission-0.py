class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        set_ans = set()
        ans = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: # if there is a duplicate first num, we want to skip it
                continue
            j, k = i+1, len(nums)-1

            while j < k:
                ssum = nums[i] + nums[j] + nums[k]
                if ssum < 0:
                    j += 1
                elif ssum > 0:
                    k -= 1
                else:
                    set_ans.add((nums[i], nums[j], nums[k]))
                    j += 1

        for tup in set_ans:
            ans.append(list(tup))
        
        return ans