import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        remaining = k

        minHeap = []

        for x, y in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(minHeap, [dist, x, y])
        
        print(minHeap)
        ans = []

        for _ in range(k):
            if len(minHeap) > 0:
                ans.append(heapq.heappop(minHeap)[1:])
        
        return ans





