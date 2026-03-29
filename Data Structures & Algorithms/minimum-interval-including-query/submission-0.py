import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # what to keep track of:
        # 1. if interval contains query number
        # 2. if this is the smallest interval that contains query number
        # if both 1 + 2 are true, then append to answer
        
        intervals.sort()
        min_heap = [] # (size, right_i) need right_i as a tiebreaker in case 2 intervals have same size and to check if interval includes query
        d = {} # dict to start, convert to list later
        i = 0 # intervals index

        for q in sorted(queries): # don't want to actually sort queries b/c we need output to be in order
            while i < len(intervals) and intervals[i][0] <= q: # pushing possible intervals onto min_heap
                l, r = intervals[i]
                heapq.heappush(min_heap, (r-l+1, r))
                i += 1
            
            while len(min_heap) > 0 and min_heap[0][1] < q: # removing intervals that are no longer valid
                heapq.heappop(min_heap)
            
            d[q] = min_heap[0][0] if min_heap else -1 # minheap is same as len(min_heap) > 0

        ans = []
        for q in queries: # convert dictionary to list
            ans.append(d[q])
        
        return ans