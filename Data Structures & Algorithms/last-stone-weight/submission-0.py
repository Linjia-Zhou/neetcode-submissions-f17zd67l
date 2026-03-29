from collections import deque

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[0]

        sorted_stones = deque(sorted(stones))

        while len(sorted_stones) > 1:
            x = sorted_stones.pop()
            y = sorted_stones.pop()

            if abs(x-y) > 0:
                sorted_stones.append(abs(x-y))
                sorted_stones = sorted(sorted_stones)

        if len(sorted_stones) == 0: return 0
        else: return sorted_stones.pop()