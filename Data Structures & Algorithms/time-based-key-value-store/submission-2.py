from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.d = defaultdict(list) # {key: [val, timestamp]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ''
        lst = self.d[key]
        l, r = 0, len(lst)-1

        while l <= r:
            m = (l+r) // 2
            if lst[m][1] <= timestamp:
                ans = lst[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return ans



