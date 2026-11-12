class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = Counter(nums)
        for k, v in d.items():
            if v % 2 == 1: return False # there is 1 extra number that can't be paired
        
        return True