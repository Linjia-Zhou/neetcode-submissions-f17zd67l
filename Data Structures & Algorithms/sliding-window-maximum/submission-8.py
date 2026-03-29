class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums

        max_dict = defaultdict(int) # {max_val: index}
        max_val = float('-inf')
        res = []
        # first window
        for i in range(k):
            if nums[i] >= max_val:
                if len(max_dict) > 0:
                    max_dict = defaultdict(int) # reset max_dict
                max_val = nums[i]
                max_dict[max_val] = i
        
        res.append(max_val)
        if len(nums) == k: return res

        # max_val is maximum of first window
        l, r = 1, k

        while r < len(nums):
            max_val_index = max_dict[max_val]
            if l <= max_val_index <= r: # this means the previous max_val is still here, so we just need to check if the newly added value is bigger
                if nums[r] >= max_val:
                    del max_dict[max_val]
                    max_val = nums[r]
                    max_dict[max_val] = r
                res.append(max_val)
            else:
                del max_dict[max_val] # finding new max_val for this window
                max_val = float('-inf')
                for i in range(l, r+1):
                    if nums[i] >= max_val:
                        max_val = nums[i]
                        max_dict[max_val] = i
                res.append(max_val)
            print(l, r, max_dict)
            r += 1
            l += 1
            
        return res