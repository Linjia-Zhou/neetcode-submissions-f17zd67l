class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = [0, 0]
        nums = {n for n in range(1, (len(grid) ** 2) + 1)}
        visited = set()

        for lst in grid:
            for n in lst:
                if n in visited: ans[0] = n
                else: visited.add(n)

                nums.discard(n)
        
        ans[1] = nums.pop()
        return ans
                

