class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1

        while i < j:
            ssum = numbers[i] + numbers[j]
            if ssum == target:
                return [i+1, j+1]
            elif ssum < target:
                i += 1
            else:
                j -= 1
        
