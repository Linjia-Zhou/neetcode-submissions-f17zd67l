class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # brute force

        for n in nums:
            if n == target: return True
        
        return False