class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        prev_max = arr[-1]
        arr[-1] = -1

        for i in range(len(arr) - 2, -1, -1):
            curr = arr[i]
            arr[i] = prev_max
            prev_max = max(prev_max, curr)
        
        return arr