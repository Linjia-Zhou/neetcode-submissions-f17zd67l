class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = {}
        stack = []

        for n in nums2:
            while stack and stack[-1] < n:
                nge[stack.pop()] = n
            stack.append(n)
        
        return [nge.get(n, -1) for n in nums1]