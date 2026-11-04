class Solution:
    def maxDifference(self, s: str) -> int:
        d = Counter(s)
        maxOdd, minEven = 0, float('inf')

        for ch in d:
            if d[ch] % 2 == 0: minEven = min(minEven, d[ch])
            else: maxOdd = max(maxOdd, d[ch])
        
        return maxOdd - minEven