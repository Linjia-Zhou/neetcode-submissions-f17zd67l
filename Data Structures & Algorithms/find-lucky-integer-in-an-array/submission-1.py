class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = Counter(arr)
        ans = -1

        for k in d:
            if k == d[k]: 
                ans = max(ans, k)
        
        return ans