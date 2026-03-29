class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sset = set(nums)
        longest = 0
        starts = []

        for n in nums:
            if (n-1) not in sset:
                length = 1
                while (n+length) in sset:
                    length += 1
                longest = max(longest, length)

        return longest
