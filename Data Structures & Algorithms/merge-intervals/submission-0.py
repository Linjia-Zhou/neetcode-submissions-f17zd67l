class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res, newInt = [], intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] > newInt[1]:
                res.append(newInt)
                newInt = intervals[i]
            elif intervals[i][1] < newInt[0]:
                res.append(intervals[i])
            else:
                newInt = [min(intervals[i][0], newInt[0]), max(intervals[i][1], newInt[1])]

        res.append(newInt)
        return res

