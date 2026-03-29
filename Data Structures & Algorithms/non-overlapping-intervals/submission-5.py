from collections import defaultdict
import heapq
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals) 
        prevEnd = intervals[0][1]
        ans = 0

        for start, end in intervals[1:]:
            if start >= prevEnd: # not overlapping
                prevEnd = end
            else: 
                ans += 1
                prevEnd = min(end, prevEnd) # we are deleting the interval with the larger end value
        
        return ans

