class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        sett = set([n for n in range(1, len(nums)+1)])
        
        for n in nums:
            sett.discard(n)
        
        return list(sett)