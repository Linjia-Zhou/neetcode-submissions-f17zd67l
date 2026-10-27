class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums = [0, 0, 1, 1], val = 0
        no_vals = []

        for n in nums:
            if n != val: no_vals.append(n)
        
        nums[:len(no_vals)+1] = no_vals[:]

        return len(no_vals)



