from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int) # counts how many times each point appears
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for p in self.pts:
            x, y = p

            if (x != px and y != py) and (abs(px - x) == abs(py - y)): # diagonal corner found
                res += (self.ptsCount[(x, py)] * self.ptsCount[(px, y)]) # (x, py) and (px, y) must be the other 2 points
        
        return res
