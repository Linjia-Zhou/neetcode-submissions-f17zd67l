class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def find_peak() -> int:
            l, r = 0, mountainArr.length()-1
            l_val, r_val = mountainArr.get(l), mountainArr.get(r)
            res = -1

            while l <= r:
                m = (l + r) // 2
                m_val = mountainArr.get(m)

                if m_val <= l_val: # m is in the right half, peak is to the left
                    r = m - 1
                    r_val = mountainArr.get(r)
                elif m_val <= r_val: # m is in left half, peak is to the right
                    l = m + 1
                    l_val = mountainArr.get(l)
                else: # if m_val > l_val or m_val > r_val, we can't conclude anything
                    l += 1
                    r -= 1
                    l_val = mountainArr.get(l)
                    r_val = mountainArr.get(r)
                
            return m
        
        def search_left(l, r): # search for target on left side
            while l <= r:
                m = (l + r) // 2
                m_val = mountainArr.get(m)

                if m_val == target: 
                    return m
                elif m_val < target:
                    l = m + 1
                else:
                    r = m - 1

            return -1

        def search_right(l, r): # search for target on left side
            while l <= r:
                m = (l + r) // 2
                m_val = mountainArr.get(m)

                if m_val == target: 
                    return m
                elif m_val > target:
                    l = m + 1
                else:
                    r = m - 1

            return -1
        
        peak = find_peak()
        print(peak)

        left = search_left(0, peak - 1)
        if left != -1: return left

        right = search_right(peak, mountainArr.length() - 1)
        if right != -1: return right

        return -1

        





