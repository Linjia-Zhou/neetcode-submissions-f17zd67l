class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0: return 0

        nums.sort()
        print(nums)
        l, r = 0, nums[-1]
        ans = 0

        while l <= r:
            m = (l + r) // 2
            i = count = 0
            # print(f'm: {m}')

            while i < len(nums) - 1:
                diff = nums[i+1] - nums[i]
                # print(f'i: {i}, diff: {diff}')

                if diff <= m:
                    count += 1
                    i += 2
                else:
                    i += 1
                # print(f'count: {count}')
            
            if count >= p: 
                ans = m
                r = m - 1
            else: 
                l = m + 1
        
        return ans


