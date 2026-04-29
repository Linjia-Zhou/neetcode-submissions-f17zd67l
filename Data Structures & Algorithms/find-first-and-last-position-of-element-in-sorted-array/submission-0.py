class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_start():
            # return index of starting position
            l, r = 0, len(nums) - 1
            start = -1

            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    start = min(start, m) if start != -1 else m
                    r = m - 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1

            return start
        
        def find_end():
            # return index of ending position
            l, r = 0, len(nums) - 1
            end = -1

            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    end = max(end, m) if end != -1 else m
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            
            return end
        
        return [find_start(), find_end()]