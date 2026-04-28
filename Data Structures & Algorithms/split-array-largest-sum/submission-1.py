class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # brute force

        '''
        for example, you said the split should’ve return earlier. 

it looks true on the surface, but it assumes split will be zero at some point, what if this is not true, can you construct a case where its not true. 

Or can you prove split is bound to be zero at some point. 
        '''
        maxx = sum(nums)
        minn = max(nums)

        for summ in range(minn, maxx+1):
            temp_sum = 0
            temp_k = k
            i = 0

            while temp_k > 0 and i < len(nums):
                temp_sum += nums[i]
                if summ == 5: print(f'temp_k: {temp_k}, i: {i}, temp_sum: {temp_sum}, summ: {summ}')
                if temp_sum == summ:
                    if summ == 5: print(f'temp_sum: {temp_sum}')
                    temp_k -= 1
                    temp_sum = 0
                    i += 1
                elif temp_sum > summ:
                    temp_k -= 1
                    temp_sum = 0
                else:
                    i += 1

            if summ == 5: print(f'temp_k: {temp_k}, i: {i}, temp_sum: {temp_sum}')
            if temp_k >= 0 and i >= len(nums):
                return summ
        

                
                

