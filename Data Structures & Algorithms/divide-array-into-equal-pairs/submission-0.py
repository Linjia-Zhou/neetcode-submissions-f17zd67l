class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = Counter(nums)
        n = len(nums) // 2

        for k, v in d.items():
            p = v // 2 # how many pairs can be made with this integer (k)
            n -= p
        
        return n <= 0