class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # [1, 1, 1]
        # (0, 1), (0, 2)
        # (1, 2)

        # [1, 1, 1, 1]
        # (0, 1), (0, 2), (0, 3)
        # (1, 2), (1, 3)
        # (2, 3)

        # (n(n-1))/2

        d = Counter(nums)
        ans = 0

        for c in d.values():
            ans += ((c * (c - 1)) // 2)
        
        return ans

