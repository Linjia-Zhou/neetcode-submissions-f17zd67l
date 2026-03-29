class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        i = 0

        for n in sorted(self.nums):
            if i == (len(self.nums)-self.k): return n
            i += 1