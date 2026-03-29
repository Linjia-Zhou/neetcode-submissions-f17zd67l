"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0: return True

        new_intervals = []
        for interval in intervals:
            new_intervals.append([interval.start, interval.end])
        
        new_intervals.sort()
        prev_end = new_intervals[0][1]

        for start, end in new_intervals[1:]:
            if start < prev_end:
                return False
            else:
                prev_end = end
        
        return True
