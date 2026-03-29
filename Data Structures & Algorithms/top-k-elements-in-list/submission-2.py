class Solution:
    from collections import defaultdict

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        ans = []

        for num in nums:
            hm[num] += 1

        sorted_hm = sorted(hm.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            ans.append(sorted_hm[i][0])
        
        return ans