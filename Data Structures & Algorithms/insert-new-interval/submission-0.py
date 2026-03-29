class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[1]: # newInterval is less than current interval
                res.append(newInterval)
                return res + intervals[i:] # can immediately return b/c intervals is ascending order, so guarantee no more overlap
            elif newInterval[0] > intervals[i][1]: # newInterval is greater than current interval
                res.append(intervals[i]) # can't return b/c maybe there is overlap later on
            else: # overlap
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval) # need to append here in case if and elif statements don't run in for loop
        return res

            