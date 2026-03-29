import heapq
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start, end = [], []

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        
        start.sort()
        end.sort()

        count = 0 # number of ongoing meetings
        ans = 0
        s, e = 0, 0 # 2 pointers for start and end

        while s < len(intervals):
            if start[s] < end[e]: # current meeting is starting before prev meeting ended
                count += 1
                s += 1
            else: # a meeting has ended
                count -= 1
                e += 1
            
            ans = max(ans, count)
        
        return ans


        






