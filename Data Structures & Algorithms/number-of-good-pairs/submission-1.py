class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = Counter(nums)
        ans = 0

        for c in d.values():
            ans += ((c * (c - 1)) // 2) # combinatorics equation for num of pairs
        
        return ans

