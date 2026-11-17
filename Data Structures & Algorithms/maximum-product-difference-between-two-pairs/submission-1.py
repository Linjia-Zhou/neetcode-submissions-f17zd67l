class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        first_max = 1
        second_max = 1
        first_min = 10000
        second_min = 10000

        for n in nums:
            if n >= first_max:
                second_max = first_max
                first_max = n
            elif n >= second_max:
                second_max = n
            
            if n <= first_min:
                second_min = first_min
                first_min = n
            elif n <= second_min:
                second_min = n
        
        print(f'first_max: {first_max}')
        print(f'second_max: {second_max}')
        print(f'first_min: {first_min}')
        print(f'second_min: {second_min}')
        return (first_max * second_max) - (first_min * second_min)
           

