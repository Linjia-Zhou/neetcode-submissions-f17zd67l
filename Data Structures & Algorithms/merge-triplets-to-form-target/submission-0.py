class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [False, False, False]

        for trip in triplets:
            a, b, c = trip

            if a > target[0] or b > target[1] or c > target[2]:
                continue
            
            if a == target[0]: res[0] = True
            if b == target[1]: res[1] = True
            if c == target[2]: res[2] = True
        
        if False in res: return False
        return True

