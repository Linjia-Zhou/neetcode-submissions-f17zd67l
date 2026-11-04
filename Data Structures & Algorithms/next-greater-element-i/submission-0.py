class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def NGE(i, nums2, d2):
            # keep going till you find a either a larger number or a number with an NGE that's larger
            j = i + 2

            for j in range(len(nums2)):
                if nums2[j] > nums2[i]:
                    return nums2[j]

                if d2[nums2[j]] > nums2[i]:
                    return d2[nums2[j]]

                if d2[nums2[j]] == -1:
                    return -1

            return -1

        d2 = defaultdict(int) # (num: NGE)

        # desending list like [4, 3, 2, 1] would be worst time complexity, would have to traverse list fully every time
        # b/c we will never find a greater value to the right

        # so, if we go backwards in the list, we could add a condition that says,
        # if previous number is less than current number AND previous number's NGE is -1, then we know current number's NGE is also -1
        # this is because, let's say [a, b, c, d] and a > b > c > d. Then, by transitive property, a > d
            # since c > d (d < c), c doesn't have any NGE. We can apply same logic to b > d (d < b), and so on

        # [3, 5, 2, 7, 6]
        # [3, 5, 2, 4, 6]

        # [1, 2, 3, 4] 

        d2[nums2[len(nums2) - 1]] = -1

        for i in range(len(nums2)-2, -1, -1):
            if nums2[i] > nums2[i+1]:
                if d2[nums2[i+1]] == -1:
                    d2[nums2[i]] = -1 
                elif d2[nums2[i+1]] > nums2[i]:
                    d2[nums2[i]] = d2[nums2[i+1]]
                else: # d2[nums2[i+1]] < nums2[i]
                   # keep going till you find a either a larger number or a number with an NGE that's larger
                    d2[nums2[i]] = NGE(i, nums2, d2)

            else: # nums2[i] < nums2[i+1]
                d2[nums2[i]] = nums2[i+1]
        
        ans = []
        for n in nums1:
            ans.append(d2[n])

        return ans

# [2, 6, 7, 5, 4, 3]
# [2, 6, 7, 5, 3, 8]

        

        
        

        

