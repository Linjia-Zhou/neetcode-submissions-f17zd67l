import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [] # nested tuples [(distance, index in points)]

        for i in range(len(points)):
            x, y = points[i]
            d = math.sqrt(x**2 + y**2)

            distance.append((d, i))
        
        heapq.heapify(distance)
        closest = []

        for _ in range(k):
            closest.append(heapq.heappop(distance))
        
        ans = []
        
        for tup in closest:
            ans.append(points[tup[1]])
        
        return ans