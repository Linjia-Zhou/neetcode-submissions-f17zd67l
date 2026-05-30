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

        nums1_neg = []
        nums1_pos = []
        nums2_neg = []
        nums2_pos = []

        for n in nums1:
            if n < 0:
                nums1_neg.append(n)
            else:
                nums1_pos.append(n)
        
        for n in nums2:
            if n < 0:
                nums2_neg.append(n)
            else:
                nums2_pos.append(n)

        count = 0
        ans = 0
        while l <= r:
            m = (l + r) // 2

            count = findProduct(m, nums1_pos[::-1], nums2_pos) #if len(nums1_pos) > 0 and len(nums2_pos) > 0 else 0
            count += findProduct(m, nums1_pos, nums2_neg) #if len(nums1_pos) > 0 and len(nums2_neg) > 0 else 0
            count += findProduct(m, nums1_neg[::-1], nums2_pos[::-1]) #if len(nums1_neg) > 0 and len(nums2_pos) > 0 else 0
            count += findProduct(m, nums1_neg, nums2_neg[::-1]) #if len(nums1_neg) > 0 and len(nums2_neg) > 0 else 0

            if count >= k:
                ans = m
                r = m - 1
            else:
                l = m + 1
        
        return ans






