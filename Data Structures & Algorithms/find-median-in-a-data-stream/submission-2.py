import heapq

class MedianFinder:

    def __init__(self):
        self.small = [] # max-heap for lower half
        self.large = [] # min-heap for upper half

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush_max(self.small, num)
        
        # reorganize if heap size differs by more than 1
        if len(self.large) > (len(self.small) + 1):
            heapq.heappush_max(self.small, heapq.heappop(self.large))
        if len(self.small) > (len(self.large) + 1):
            heapq.heappush(self.large, heapq.heappop_max(self.small))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            val = self.small[0] + self.large[0]
            return val / 2
            

        

            

        