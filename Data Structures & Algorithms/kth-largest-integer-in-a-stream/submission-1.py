class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        i = 0

        '''
        for i in range(len(sorted(self.nums))):
            print(sorted(self.nums))
            if i == (len(self.nums)-self.k): return self.nums[i]
        '''

        for n in sorted(self.nums):
            if i == (len(self.nums)-self.k): return n
            i += 1

        # [4, 5, 8, 2] --> [4, 5, 8, 2, 3]
        # sorted: [2, 3, 4, 5, 8]
        # 5 - 3 = 2