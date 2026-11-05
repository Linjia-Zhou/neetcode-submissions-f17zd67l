from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = {} # num: nge
        stack = [] # all nums that still need a nge

        for n in nums2:
            while stack and stack[-1] < n: # checking to see if n can be the nge for any number to its left
                nge[stack[-1]] = n
                stack.pop()
                
            stack.append(n)
        
        # now, every num on stack has no nge
        # and all these nums on stack are not in dict: nge
        ans = []
        for n in nums1:
            if n in nge:
                ans.append(nge[n])
            else:
                ans.append(-1)
        
        return ans




        

        


        
