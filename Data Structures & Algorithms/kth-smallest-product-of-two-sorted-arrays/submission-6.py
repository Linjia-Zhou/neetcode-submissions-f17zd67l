import math
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def findProduct(m, n1, n2):
            # return how many product combinations are <= threshold m
            count = 0
            j = 0

            for i in range(len(n1)):
                while j < len(n2) and (n1[i] * n2[j] <= m):
                    j += 1
                
                count += j 

            return count
        
        l = min(nums1[0] * nums2[0], nums1[0] * nums2[-1], nums1[-1] * nums2[0], nums1[-1] * nums2[-1])
        r = max(nums1[0] * nums2[0], nums1[0] * nums2[-1], nums1[-1] * nums2[0], nums1[-1] * nums2[-1])

        n1 = n2 = 0

        while n1 < len(nums1) and nums1[n1] < 0:
            n1 += 1
        
        while n2 < len(nums2) and nums2[n2] < 0:
            n2 += 1

        count = 0
        while l <= r:
            m = (l + r) // 2
            
            count = findProduct(m, nums1[n1:][::-1], nums2[n2:]) 
            count += findProduct(m, nums1[n1:], nums2[:n2]) 
            count += findProduct(m, nums1[:n1][::-1], nums2[n2:][::-1]) 
            count += findProduct(m, nums1[:n1], nums2[:n2][::-1]) 

            if count >= k:
                r = m - 1
            else:
                l = m + 1
        
        return l






