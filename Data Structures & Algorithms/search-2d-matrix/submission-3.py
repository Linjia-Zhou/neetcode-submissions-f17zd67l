class Solution:
    def binary_search(self, lst, t):
        l, r = 0, len(lst)-1

        while l <= r:
            mid = (l+r)//2

            if lst[mid] < t:
                l = mid+1
            elif lst[mid] > t:
                r = mid-1
            else:
                return True
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_row = 0
        l, r = 0, len(matrix)-1

        while l <= r:
            mid = (l+r)//2

            if matrix[mid][0] < target:
                l = mid+1
            elif matrix[mid][0] > target:
                r = mid-1
            else:
                return True
            
            if l == r:
                if l == 0:
                    target_row = l
                elif matrix[l-1][-1] > target:
                    target_row = l-1
                elif matrix[l-1][-1] < target:
                    target_row = l
                else:
                    return True
        
        return self.binary_search(matrix[target_row], target)

