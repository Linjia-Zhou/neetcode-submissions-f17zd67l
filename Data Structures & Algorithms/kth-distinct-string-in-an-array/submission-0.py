class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = Counter(arr)

        for key in d:
            if d[key] == 1: k -= 1
            if k == 0: return key
        
        return ''